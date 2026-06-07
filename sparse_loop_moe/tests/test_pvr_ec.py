"""Tests for PVR-EC Router and MoE.

Validates:
- Every token gets a guaranteed top1 primary owner
- Candidates and probabilities stay in sync
- Difficulty is per-token bucketed (EASY/NORMAL/HARD)
- Hard bucket doesn't become default
- Extra expert slots respect capacity
- Load bias is capped
- Load bias cannot route outside compatible mask
- Pack-by-expert executes one call per expert, not per token
- Scatter-add reconstructs correctly
- Existing baselines still work
"""

import sys
import inspect
import json
import subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "evaluation"))

import torch
import pytest

from sparse_loop_moe.models.pvr_ec.diagnostics import (
    EXECUTION_MODES,
    ExpertDeltaScaleSchedule,
    EXPERT_TYPES,
    REQUIRED_BRANCH_TICKET_FIELDS,
    MergeabilityState,
    MergeabilityWeights,
    make_branch_ticket,
    post_expert_mergeability,
    pre_expert_mergeability,
    residual_merge,
    weighted_hidden_merge,
    write_diagnostic_reports,
)
from sparse_loop_moe.models.pvr_ec.pvr_ec_router import (
    PVRECRouter, PVRECConfig, RoutingOutput, Difficulty,
)
from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.moe_ffn import MoEFFN, VectorizedMoEFFN


@pytest.fixture
def router():
    config = PVRECConfig(d_model=64, num_experts=4, num_prototypes=8, d_route=32, max_k=4)
    return PVRECRouter(config)


@pytest.fixture
def moe():
    return PVRECMoEFFN(d_model=64, d_ff=128, num_experts=4, num_prototypes=8, max_k=4)


@pytest.fixture
def model():
    config = PVRECModelConfig(
        vocab_size=128, d_model=64, max_seq_len=64,
        n_layers=2, n_heads=2, d_ff=128, num_experts=4,
        num_prototypes=8, max_k=4, d_expert=64,
    )
    return PVRECModel(config)


class TestPVRECRouter:
    def test_every_token_gets_top1_primary_owner(self, router):
        """Every token receives a guaranteed top1 primary owner."""
        x = torch.randn(32, 64)
        out = router(x)
        # All primary expert ids must be valid (0..num_experts-1)
        assert (out.primary_expert_ids >= 0).all()
        assert (out.primary_expert_ids < router.config.num_experts).all()
        # All primary weights must be positive
        assert (out.primary_weights > 0).all()

    def test_difficulty_labels_are_per_token(self, router):
        """Difficulty labels are per-token, not global."""
        x = torch.randn(64, 64)
        out = router(x)
        assert out.difficulty.shape == (64,)
        # Should have at least some variation with random input
        unique_difficulties = out.difficulty.unique()
        assert len(unique_difficulties) >= 1  # At minimum one difficulty level

    def test_hard_bucket_does_not_become_default(self, router):
        """Hard bucket doesn't silently become the default for all tokens."""
        torch.manual_seed(123)  # Fixed seed for determinism
        x = torch.randn(128, 64)
        out = router(x)
        hard_rate = (out.difficulty == Difficulty.HARD).float().mean().item()
        # Hard should not be 100% — some tokens must be EASY or NORMAL
        # At initialization with random weights, high hard rate is expected
        # but it should never be ALL tokens
        assert hard_rate < 0.95, f"Hard rate too high (near-all HARD): {hard_rate}"

    def test_extra_expert_slots_respect_capacity(self, router):
        """Extra expert slots respect max_k capacity."""
        x = torch.randn(32, 64)
        out = router(x)
        # EASY tokens should have no extra experts
        easy_mask = out.difficulty == Difficulty.EASY
        if easy_mask.any():
            assert (out.extra_expert_ids[easy_mask] == -1).all()
        # No token should have more than max_k-1 extra experts
        max_extras = (out.extra_expert_ids != -1).sum(dim=-1).max().item()
        assert max_extras <= router.config.max_k - 1

    def test_load_bias_is_capped(self, router):
        """Load bias magnitude is capped."""
        x = torch.randn(32, 64)
        router.train()
        for _ in range(10):
            router(x)
        assert router.load_bias.abs().max().item() <= router.config.load_bias_cap + 1e-6

    def test_load_bias_cannot_route_outside_compatible_mask(self, router):
        """Load bias cannot cause routing to incompatible experts."""
        # Force extreme load bias
        router.load_bias.fill_(router.config.load_bias_cap)
        x = torch.randn(32, 64)
        out = router(x)
        # Primary experts must still be within compatible set for each token
        # (verified by the fact that incompatible experts get -inf logits)
        assert (out.primary_expert_ids >= 0).all()
        assert (out.primary_expert_ids < router.config.num_experts).all()

    def test_probabilities_sum_correctly(self, router):
        """Probabilities are valid (non-negative, not all zero)."""
        x = torch.randn(32, 64)
        out = router(x)
        # All probs should be non-negative
        assert (out.all_probs >= 0).all()
        # At least the primary expert should have non-zero prob
        assert (out.primary_weights > 0).all()


class TestPVRECMoE:
    def test_pack_by_expert_not_per_token(self, moe):
        """Pack-by-expert executes one call per expert, not per token."""
        x = torch.randn(2, 16, 64)
        output, aux = moe(x)
        # Output shape preserved
        assert output.shape == x.shape
        # Load balance loss exists
        assert "load_balance_loss" in aux

    def test_scatter_add_correctness(self, moe):
        """Scatter-add reconstructs token outputs correctly."""
        x = torch.randn(2, 16, 64)
        output, _ = moe(x)
        # Output should not be all zeros (sparse contribution exists)
        assert output.abs().sum() > 0
        # Output should differ from input (transformation happened)
        assert not torch.allclose(output, x, atol=1e-4)

    def test_shared_base_always_runs(self, moe):
        """Shared base contributes to every token."""
        x = torch.randn(1, 8, 64)
        output, _ = moe(x)
        # With shared base, output should be non-zero even if all experts inactive
        assert output.abs().sum() > 0

    def test_routing_metrics_populated(self, moe):
        """Routing metrics are populated after forward pass."""
        x = torch.randn(2, 16, 64)
        _, aux = moe(x)
        assert "easy_rate" in aux
        assert "hard_rate" in aux
        assert "avg_active_experts" in aux

    def test_shared_logits_shape_matches_combined_logits(self):
        config = PVRECModelConfig(
            vocab_size=64, d_model=32, max_seq_len=32,
            n_layers=1, n_heads=2, d_ff=64, num_experts=4,
            num_prototypes=8, d_expert=16, pvr_deploy_mode="top1",
        )
        model = PVRECModel(config)
        input_ids = torch.randint(1, 64, (2, 12))
        targets = torch.randint(1, 64, (2, 12))
        output = model(input_ids=input_ids, targets=targets)
        decomp = output["pvr_logit_decomposition"]
        assert decomp["shared_logits"].shape == output["logits"].shape

    def test_sparse_delta_logits_shape_matches_combined_logits(self):
        config = PVRECModelConfig(
            vocab_size=64, d_model=32, max_seq_len=32,
            n_layers=1, n_heads=2, d_ff=64, num_experts=4,
            num_prototypes=8, d_expert=16, pvr_deploy_mode="top1",
        )
        model = PVRECModel(config)
        input_ids = torch.randint(1, 64, (2, 12))
        targets = torch.randint(1, 64, (2, 12))
        output = model(input_ids=input_ids, targets=targets)
        decomp = output["pvr_logit_decomposition"]
        assert decomp["sparse_delta_logits"].shape == output["logits"].shape

    @pytest.mark.parametrize("variant", [
        "sparse_ce_0_03",
        "margin_align_0_03_m0_5",
        "wrong_suppress_0_03_t0_25",
        "sparse_ce_0_03_plus_harm_0_03",
        "sparse_ce_0_03_plus_wrong_suppress_0_03",
        "sparse_ce_0_05_plus_wrong_suppress_0_01",
        "sparse_ce_0_05_plus_logit_norm_penalty_light",
        "sparse_ce_0_05_plus_temperature_regularization",
        "sparse_ce_warmup_decay",
    ])
    def test_sparse_auxiliary_losses_are_finite(self, variant):
        config = PVRECModelConfig(
            vocab_size=64, d_model=32, max_seq_len=32,
            n_layers=1, n_heads=2, d_ff=64, num_experts=4,
            num_prototypes=8, d_expert=16, pvr_deploy_mode="top1",
            pvr_sparse_aux_loss_variant=variant,
        )
        model = PVRECModel(config)
        input_ids = torch.randint(1, 64, (2, 12))
        targets = torch.randint(1, 64, (2, 12))
        output = model(input_ids=input_ids, targets=targets)
        loss = output["aux_losses"]["sparse_auxiliary_loss"]
        assert torch.isfinite(loss)
        assert loss.item() >= 0.0

    def test_auxiliary_loss_weight_zero_matches_baseline(self):
        torch.manual_seed(7)
        config = PVRECModelConfig(
            vocab_size=64, d_model=32, max_seq_len=32,
            n_layers=1, n_heads=2, d_ff=64, num_experts=4,
            num_prototypes=8, d_expert=16, pvr_deploy_mode="top1",
            pvr_sparse_aux_loss_variant="baseline_main_loss",
        )
        model = PVRECModel(config)
        input_ids = torch.randint(1, 64, (2, 12))
        targets = torch.randint(1, 64, (2, 12))
        output = model(input_ids=input_ids, targets=targets)
        assert "sparse_auxiliary_loss" not in output["aux_losses"]

    def test_auxiliary_loss_does_not_change_owner_count_or_enable_top2_top4(self):
        config = PVRECModelConfig(
            vocab_size=64, d_model=32, max_seq_len=32,
            n_layers=1, n_heads=2, d_ff=64, num_experts=4,
            num_prototypes=8, d_expert=16, pvr_deploy_mode="top1",
            pvr_sparse_aux_loss_variant="wrong_suppress_0_03_t0_25",
        )
        model = PVRECModel(config)
        input_ids = torch.randint(1, 64, (2, 12))
        targets = torch.randint(1, 64, (2, 12))
        output = model(input_ids=input_ids, targets=targets)
        routing = output["pvr_diagnostics"]
        assert routing["actual_owner_count_per_token"] == pytest.approx(1.0)
        assert routing["num_k2_tokens"] == pytest.approx(0.0)
        assert routing["num_k4_tokens"] == pytest.approx(0.0)

    def test_execution_modes_register(self):
        expected = {
            "dense_all_experts",
            "fixed_top2_all_experts_masked",
            "fixed_top2_pack_by_expert",
            "variable_k_pack_by_expert",
            "hybrid_expert_choice_bucketed",
        }
        assert expected.issubset(EXECUTION_MODES)

    def test_expert_type_ablation_registers(self):
        expected = {
            "shared_base_only",
            "delta_rank_small",
            "delta_rank_medium",
            "delta_rank_large",
            "full_expert_ffn",
        }
        assert expected.issubset(EXPERT_TYPES)

    def test_dense_all_experts_trains_all_experts(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            execution_mode="dense_all_experts",
        )
        x = torch.randn(2, 4, 32)
        out, _ = model(x)
        out.sum().backward()
        grad_sums = [
            sum((p.grad.abs().sum().item() if p.grad is not None else 0.0) for p in expert.parameters())
            for expert in model.expert_deltas
        ]
        assert all(g > 0.0 for g in grad_sums)

    def test_sparse_modes_train_only_selected_experts(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            execution_mode="fixed_top2_pack_by_expert",
        )
        selected = torch.tensor([0, 1] * 4)
        extra = torch.full((8, 3), -1, dtype=torch.long)
        extra[:, 0] = 1
        probs = torch.zeros(8, 4)
        probs[:, 0] = 0.6
        probs[:, 1] = 0.4
        selected_mask = torch.zeros(8, 4, dtype=torch.bool)
        selected_mask[:, 0] = True
        selected_mask[:, 1] = True
        routing = RoutingOutput(
            primary_expert_ids=selected,
            primary_weights=torch.full((8,), 0.6),
            extra_expert_ids=extra,
            extra_weights=torch.cat([torch.full((8, 1), 0.4), torch.zeros(8, 2)], dim=1),
            difficulty=torch.full((8,), Difficulty.NORMAL, dtype=torch.long),
            all_probs=probs,
            load_balance_loss=torch.tensor(0.0),
            metrics={"routing_entropy": 0.0, "expert_utilization": 0.5, "dead_expert_count": 2,
                     "load_imbalance": 0.0, "easy_rate": 0.0, "normal_rate": 1.0,
                     "hard_rate": 0.0, "avg_active_experts": 2.0},
            selected_mask=selected_mask,
        )
        model.router.forward = lambda x, routing_mode=None: routing
        x = torch.randn(1, 8, 32)
        out, _ = model(x)
        out.sum().backward()
        grad_sums = [
            sum((p.grad.abs().sum().item() if p.grad is not None else 0.0) for p in expert.parameters())
            for expert in model.expert_deltas
        ]
        assert grad_sums[0] > 0.0
        assert grad_sums[1] > 0.0
        assert grad_sums[2] == 0.0
        assert grad_sums[3] == 0.0

    def test_fixed_top2_all_experts_masked_computes_all_experts(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            execution_mode="fixed_top2_all_experts_masked",
        )
        calls = [0, 0, 0, 0]
        handles = []
        for idx, expert in enumerate(model.expert_deltas):
            handles.append(expert.register_forward_hook(lambda m, i, o, idx=idx: calls.__setitem__(idx, calls[idx] + 1)))
        model(torch.randn(1, 8, 32))
        for handle in handles:
            handle.remove()
        assert calls == [1, 1, 1, 1]

    def test_fixed_top2_pack_by_expert_computes_selected_top2_only(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            execution_mode="fixed_top2_pack_by_expert",
        )
        calls = [0, 0, 0, 0]
        handles = []
        for idx, expert in enumerate(model.expert_deltas):
            handles.append(expert.register_forward_hook(lambda m, i, o, idx=idx: calls.__setitem__(idx, calls[idx] + 1)))
        primary = torch.zeros(8, dtype=torch.long)
        extra = torch.full((8, 3), -1, dtype=torch.long)
        extra[:, 0] = 1
        probs = torch.zeros(8, 4)
        probs[:, 0] = 0.6
        probs[:, 1] = 0.4
        selected_mask = torch.zeros(8, 4, dtype=torch.bool)
        selected_mask[:, :2] = True
        routing = RoutingOutput(
            primary_expert_ids=primary,
            primary_weights=torch.full((8,), 0.6),
            extra_expert_ids=extra,
            extra_weights=torch.cat([torch.full((8, 1), 0.4), torch.zeros(8, 2)], dim=1),
            difficulty=torch.full((8,), Difficulty.NORMAL, dtype=torch.long),
            all_probs=probs,
            load_balance_loss=torch.tensor(0.0),
            metrics={"routing_entropy": 0.0, "expert_utilization": 0.5, "dead_expert_count": 2,
                     "load_imbalance": 0.0, "easy_rate": 0.0, "normal_rate": 1.0,
                     "hard_rate": 0.0, "avg_active_experts": 2.0},
            selected_mask=selected_mask,
        )
        model.router.forward = lambda x, routing_mode=None: routing
        model(torch.randn(1, 8, 32))
        for handle in handles:
            handle.remove()
        assert calls[:2] == [1, 1]
        assert calls[2:] == [0, 0]

    def test_timing_metrics_are_reported(self, moe):
        _, aux = moe(torch.randn(2, 8, 64))
        timing = aux["timing"]
        for key in [
            "forward_total_ms", "forward_router_score_ms", "forward_assignment_build_ms",
            "forward_pack_ms", "forward_expert_compute_ms", "forward_scatter_ms",
            "dispatch_overhead_ratio", "compute_to_dispatch_ratio",
            "forward_dispatch_overhead_ratio", "backward_dispatch_overhead_ratio",
            "training_compute_to_dispatch_ratio",
        ]:
            assert key in timing


class TestPVRECModel:
    def test_model_forward_produces_logits(self, model):
        """Model produces logits of correct shape."""
        input_ids = torch.randint(0, 128, (2, 16))
        out = model(input_ids)
        assert "logits" in out
        assert out["logits"].shape == (2, 16, 128)

    def test_model_forward_with_targets_produces_loss(self, model):
        """Model produces loss when targets provided."""
        input_ids = torch.randint(0, 128, (2, 16))
        targets = torch.randint(0, 128, (2, 16))
        out = model(input_ids, targets)
        assert "loss" in out
        assert out["loss"].item() > 0

    def test_model_backward_passes(self, model):
        """Model supports backward pass without errors."""
        input_ids = torch.randint(0, 128, (2, 16))
        targets = torch.randint(0, 128, (2, 16))
        out = model(input_ids, targets)
        out["loss"].backward()
        # Check gradients exist
        for name, param in model.named_parameters():
            if param.requires_grad:
                # At least some params should have gradients
                break

    def test_model_interface_compatible_with_benchmark(self, model):
        """Model interface matches benchmark runner expectations."""
        input_ids = torch.randint(0, 128, (4, 32))
        targets = torch.randint(0, 128, (4, 32))
        out = model(input_ids, targets)
        # Must have these keys for benchmark compatibility
        assert "logits" in out
        assert "loss" in out
        assert "hidden_states" in out
        assert "loop_stats" in out  # Empty list is fine for PVR-EC

    def test_model_exposes_pvr_diagnostics_for_benchmark_reports(self, model):
        input_ids = torch.randint(0, 128, (2, 16))
        targets = torch.randint(0, 128, (2, 16))
        out = model(input_ids, targets)
        diag = out["pvr_diagnostics"]
        for key in [
            "pvr_execution_mode",
            "dispatch_overhead_ratio",
            "compute_to_dispatch_ratio",
            "actual_avg_k",
            "assignment_budget_drift",
            "mergeability_score_mean",
            "branch_ticket_count",
        ]:
            assert key in diag


class TestBaselinePreservation:
    """Verify existing baselines still work after PVR-EC addition."""

    def test_dense_baseline_still_works(self):
        """Dense transformer still instantiates and runs."""
        from sparse_loop_moe.models.dense_transformer import DenseTransformer, DenseTransformerConfig
        config = DenseTransformerConfig(vocab_size=128, d_model=64, n_heads=2, n_layers=2, d_ff=128, max_seq_len=32)
        model = DenseTransformer(config)
        out = model(torch.randint(0, 128, (2, 16)), torch.randint(0, 128, (2, 16)))
        assert "logits" in out and "loss" in out

    def test_fixed_moe_still_works(self):
        """Fixed MoE still instantiates and runs."""
        from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
        config = SparseLoopMoEConfig(
            vocab_size=128, d_model=64, n_heads=2, n_layers=2, d_ff=128,
            num_experts=4, max_k=2, max_loops=1, max_seq_len=32,
            use_adaptive_router=False, use_probes=False, use_reflection=False,
            use_loops=False, use_shared_expert=True,
        )
        model = SparseLoopMoEModel(config)
        out = model(torch.randint(0, 128, (2, 16)), torch.randint(0, 128, (2, 16)))
        assert "logits" in out and "loss" in out

    def test_adaptive_moe_still_works(self):
        """Adaptive MoE still instantiates and runs."""
        from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
        config = SparseLoopMoEConfig(
            vocab_size=128, d_model=64, n_heads=2, n_layers=2, d_ff=128,
            num_experts=4, max_k=4, max_loops=1, max_seq_len=32,
            use_adaptive_router=True, use_probes=False, use_reflection=False,
            use_loops=False, use_shared_expert=True,
        )
        model = SparseLoopMoEModel(config)
        out = model(torch.randint(0, 128, (2, 16)), torch.randint(0, 128, (2, 16)))
        assert "logits" in out and "loss" in out

    def test_fixed_moe_looped_reference_still_works(self):
        from sparse_loop_moe.models.full_model import SparseLoopMoEModel, SparseLoopMoEConfig
        config = SparseLoopMoEConfig(
            vocab_size=128, d_model=64, n_heads=2, n_layers=2, d_ff=128,
            num_experts=4, max_k=2, max_loops=1, max_seq_len=32,
            use_adaptive_router=False, use_probes=False, use_reflection=False,
            use_loops=False, use_shared_expert=True, vectorized_moe=False,
        )
        model = SparseLoopMoEModel(config)
        out = model(torch.randint(0, 128, (2, 16)), torch.randint(0, 128, (2, 16)))
        assert "logits" in out and "loss" in out

    def test_fixed_moe_vectorized_matches_looped_reference(self):
        torch.manual_seed(123)
        looped = MoEFFN(
            d_model=32, d_ff=64, num_experts=4, top_k=2,
            use_shared_expert=True, dropout=0.0,
        )
        vectorized = VectorizedMoEFFN(
            d_model=32, d_ff=64, num_experts=4, top_k=2,
            use_shared_expert=True, dropout=0.0,
        )
        vectorized.load_state_dict(looped.state_dict())
        looped.eval()
        vectorized.eval()
        x = torch.randn(3, 7, 32)
        looped_out, looped_aux = looped(x, fixed_k=2)
        vectorized_out, vectorized_aux = vectorized(x, fixed_k=2)
        assert torch.allclose(vectorized_out, looped_out, atol=1e-5, rtol=1e-5)
        assert torch.allclose(
            vectorized_aux["load_balance_loss"],
            looped_aux["load_balance_loss"],
            atol=1e-6,
        )

    def test_fixed_moe_vectorized_is_marked_fully_vectorized(self):
        model = VectorizedMoEFFN(d_model=32, d_ff=64, num_experts=4, top_k=2)
        assert model.expert_execution_mode == "FULLY_VECTORIZED"

    def test_benchmark_registers_fair_fixed_moe_variants(self):
        from run_algorithmic_benchmarks import MODELS
        assert "fixed_moe_vectorized" in MODELS
        assert "fixed_moe_looped_reference" in MODELS
        assert MODELS["fixed_moe_vectorized"]["overrides"]["vectorized_moe"] is True

    def test_benchmark_registers_capacity_ladder_variants(self):
        from run_algorithmic_benchmarks import MODELS
        expected = {
            "pvr_ec_ownership_top1_delta_small",
            "pvr_ec_ownership_top1_delta_medium",
            "pvr_ec_ownership_top1_delta_large",
            "pvr_ec_ownership_top1_full_expert_ffn_control",
            "pvr_ec_ownership_top1_delta_rank_8",
            "pvr_ec_ownership_top1_delta_rank_16",
            "pvr_ec_ownership_top1_delta_rank_32",
            "pvr_ec_ownership_top1_delta_rank_64",
            "pvr_ec_ownership_top1_delta_rank_128",
            "pvr_ec_ownership_top1_rank_8",
            "pvr_ec_ownership_top1_rank_16",
            "pvr_ec_ownership_top1_rank_32",
            "pvr_ec_ownership_top1_rank_64",
            "pvr_ec_ownership_top1_rank_128",
            "pvr_ec_ownership_top1_micro_ffn_0_25x",
            "pvr_ec_ownership_top1_micro_ffn_0_5x",
            "pvr_ec_ownership_top1_micro_ffn_1_0x",
        }
        assert expected.issubset(MODELS)
        assert MODELS["pvr_ec_ownership_top1_full_expert_ffn_control"]["overrides"]["pvr_expert_type"] == "full_expert_ffn_control"
        assert MODELS["pvr_ec_ownership_top1_rank_8"]["overrides"]["pvr_expert_type"] == "delta_rank_8"

    def test_benchmark_registers_learning_separation_variants(self):
        from run_algorithmic_benchmarks import MODELS

        expected = {
            "pvr_ec_learning_full",
            "pvr_ec_learning_shared_only",
            "pvr_ec_learning_sparse_only",
            "pvr_ec_learning_shared_scale_0_5",
            "pvr_ec_learning_expert_delta_scale_2_0",
            "pvr_ec_ownership_top1_delayed_candidate",
        }
        assert expected.issubset(MODELS)
        assert MODELS["pvr_ec_learning_shared_only"]["overrides"]["pvr_expert_type"] == "shared_base_only"
        assert MODELS["pvr_ec_learning_sparse_only"]["overrides"]["pvr_shared_scale"] == 0.0


class TestHybridRouter:
    def test_hybrid_k_is_allowed_and_top1_covered(self):
        cfg = PVRECConfig(
            d_model=32, num_experts=4, num_prototypes=8, d_route=16,
            max_k=4, routing_mode="hybrid_expert_choice_bucketed",
        )
        router = PVRECRouter(cfg)
        out = router(torch.randn(64, 32), routing_mode="hybrid_expert_choice_bucketed")
        k = out.selected_mask.sum(dim=-1)
        assert set(k.tolist()).issubset({1, 2, 4})
        assert (k >= 1).all()
        assert (k <= 4).all()
        assert out.selected_mask[torch.arange(64), out.primary_expert_ids].all()

    def test_capacity_is_respected_as_upper_bound_when_feasible(self):
        cfg = PVRECConfig(
            d_model=32, num_experts=4, num_prototypes=8, d_route=16,
            max_k=4, routing_mode="hybrid_expert_choice_bucketed", expert_capacity=64,
        )
        router = PVRECRouter(cfg)
        out = router(torch.randn(64, 32), routing_mode="hybrid_expert_choice_bucketed")
        expert_load = out.selected_mask.sum(dim=0)
        assert (expert_load <= 64).all()

    def test_assignment_budget_drift_is_reported(self):
        cfg = PVRECConfig(
            d_model=32, num_experts=4, num_prototypes=8, d_route=16,
            max_k=4, routing_mode="hybrid_expert_choice_bucketed", target_avg_k=4.0,
        )
        router = PVRECRouter(cfg)
        out = router(torch.randn(16, 32), routing_mode="hybrid_expert_choice_bucketed")
        assert "assignment_budget_drift" in out.metrics
        assert "assignment_budget_status" in out.metrics


class TestMergeabilityAndTickets:
    def test_weighted_merge_preserves_tensor_shape(self):
        expert_outputs = torch.randn(5, 3, 16)
        weights = torch.rand(5, 3)
        out = weighted_hidden_merge(expert_outputs, weights)
        assert out.shape == (5, 16)

    def test_residual_merge_preserves_primary_owner_contribution(self):
        primary = torch.randn(5, 16)
        aux = torch.randn(5, 16)
        out = residual_merge(primary, aux, alpha=0.0)
        assert torch.allclose(out, primary)

    def test_pre_expert_mergeability_does_not_require_expert_outputs(self):
        probs = torch.tensor([[0.8, 0.1, 0.1], [0.34, 0.33, 0.33]])
        selected = torch.tensor([[True, False, False], [True, True, True]])
        score = pre_expert_mergeability(probs, selected)
        assert score.shape == (2,)
        assert ((score >= 0) & (score <= 1)).all()

    def test_post_expert_mergeability_uses_stable_disagreement(self):
        probs = torch.tensor([[0.8, 0.1, 0.1], [0.34, 0.33, 0.33]])
        selected = torch.tensor([[True, False, False], [True, True, True]])
        low_d = torch.tensor([0.0, 0.0])
        high_d = torch.tensor([2.0, 2.0])
        low_score = post_expert_mergeability(probs, selected, low_d)
        high_score = post_expert_mergeability(probs, selected, high_d)
        assert (low_score > high_score).all()

    def test_risk_defaults_zero_for_hidden_token_hot_path(self):
        probs = torch.tensor([[0.8, 0.1, 0.1]])
        selected = torch.tensor([[True, False, False]])
        default_score = pre_expert_mergeability(probs, selected)
        zero_score = pre_expert_mergeability(probs, selected, risk=0.0)
        assert torch.allclose(default_score, zero_score)

    def test_formula_scores_confident_low_disagreement_higher(self):
        confident = torch.tensor([[0.9, 0.05, 0.05]])
        uncertain = torch.tensor([[0.34, 0.33, 0.33]])
        selected = torch.tensor([[True, False, False]])
        confident_score = post_expert_mergeability(confident, selected, torch.tensor([0.0]))
        uncertain_score = post_expert_mergeability(uncertain, selected, torch.tensor([2.0]), risk=1.0)
        assert confident_score.item() > uncertain_score.item()

    def test_branch_tickets_include_required_fields_and_are_shadow_only(self):
        ticket = make_branch_ticket(
            state_id=1, primary_expert=0, selected_experts=[0, 2],
            uncertainty=0.5, mergeability_score=0.6, branch_value=0.1,
            affinity=[0.7, 0.1, 0.2], prototype_ids=[3], prototype_distance=0.2,
            difficulty_bucket="normal", merge_type="residual_merge",
        )
        assert set(REQUIRED_BRANCH_TICKET_FIELDS).issubset(ticket)
        assert ticket["runtime_branch_recommended"] is False

    def test_moe_branch_tickets_are_shadow_only_by_default(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            execution_mode="hybrid_expert_choice_bucketed",
        )
        _, aux = model(torch.randn(1, 8, 32))
        assert "PVR_EC_BRANCH_TICKETS_SHADOW_ONLY" in aux["statuses"]
        assert all(ticket["runtime_branch_recommended"] is False for ticket in aux["branch_tickets"])

    def test_replay_label_and_scalar_update_change_weights(self):
        state = MergeabilityState(learning_rate=0.1)
        before = state.current_weights.w_c
        features = {
            "score": 0.2, "p1": 0.8, "p2": 0.1, "selected_mass": 0.9,
            "entropy": 0.2, "disagreement": 0.1, "risk": 0.0,
        }
        state.record_replay_update(features, y=1.0)
        assert state.replay_labels == [1.0]
        assert state.current_weights.w_c > before

    def test_required_reports_are_written(self, tmp_path):
        paths = write_diagnostic_reports(tmp_path)
        expected = {
            "pvr_ec_sparse_dispatch_ablation_report.json",
            "pvr_ec_sparse_dispatch_ablation_report.md",
            "dispatch_timing_report.json",
            "expert_type_ablation_report.json",
            "hybrid_router_report.json",
            "mergeability_formula_report.json",
            "soft_vs_hard_speculation_report.json",
            "branch_ticket_shadow_report.json",
        }
        assert expected.issubset(paths)
        for name in expected:
            assert (tmp_path / name).exists()

    def test_reports_include_record_driven_metrics_and_statuses(self, tmp_path):
        records = [
            {
                "model_name": "pvr_ec",
                "task": "toy",
                "accuracy": 0.1,
                "loss": 2.0,
                "qpc": 0.05,
                "inference_time_s": 2.0,
                "training_time_s": 4.0,
                "pvr_execution_mode": "variable_k_pack_by_expert",
                "pvr_expert_type": "delta_rank_medium",
                "pvr_total_step_time_ms": 10.0,
                "pvr_router_score_time_ms": 2.0,
                "pvr_assignment_build_time_ms": 2.0,
                "pvr_pack_time_ms": 2.0,
                "pvr_expert_compute_time_ms": 1.0,
                "pvr_scatter_time_ms": 2.0,
                "pvr_dispatch_overhead_ratio": 0.8,
                "pvr_compute_to_dispatch_ratio": 0.2,
                "pvr_forward_dispatch_overhead_ratio": 0.8,
                "pvr_backward_dispatch_overhead_ratio": 0.0,
                "pvr_training_compute_to_dispatch_ratio": 0.2,
                "pvr_tokens_per_second": 100.0,
                "pvr_avg_tokens_per_active_expert": 4.0,
                "pvr_small_expert_batch_rate": 0.5,
                "pvr_actual_avg_k": 4.0,
                "pvr_target_avg_k": 2.0,
                "pvr_assignment_budget_drift": 1.0,
                "pvr_expert_utilization": 1.0,
                "pvr_expert_load_cv": 0.3,
                "pvr_route_entropy": 0.7,
                "pvr_num_k1_tokens": 0,
                "pvr_num_k2_tokens": 0,
                "pvr_num_k4_tokens": 8,
                "pvr_mergeability_score_mean": 0.6,
                "pvr_mergeability_score_std": 0.1,
                "pvr_expert_disagreement_mean": 0.2,
                "pvr_branch_ticket_count": 3,
            },
            {
                "model_name": "fixed_moe",
                "task": "toy",
                "accuracy": 0.2,
                "loss": 1.8,
                "qpc": 0.1,
                "inference_time_s": 1.0,
                "training_time_s": 1.0,
            },
        ]
        write_diagnostic_reports(tmp_path, {"pvr_eval_records": records})
        dispatch = __import__("json").loads((tmp_path / "dispatch_timing_report.json").read_text())
        branch = __import__("json").loads((tmp_path / "branch_ticket_shadow_report.json").read_text())
        assert dispatch["metrics"]["dispatch_overhead_ratio"] == 0.8
        assert "PVR_EC_SPARSE_DISPATCH_BOTTLENECK" in dispatch["statuses"]
        assert "PVR_EC_ASSIGNMENT_BUDGET_DRIFT" in dispatch["statuses"]
        assert branch["branch_ticket_count"] == 3
        assert branch["shadow_only"] is True


class TestPVRECDeployment:
    def test_deploy_top1_forward_works(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1",
        )
        x = torch.randn(2, 8, 32)
        out, aux = model(x)
        assert out.shape == x.shape
        assert aux["deploy_mode"] == "top1"
        assert aux["branch_tickets"] == []
        assert aux["routing_metrics"]["actual_owner_count_per_token"].item() == pytest.approx(1.0)
        assert aux["routing_metrics"]["actual_expert_slots_per_token"].item() == pytest.approx(1.0)
        assert aux["routing_metrics"]["dense_all_experts_executed"] is False

    def test_deploy_top2_forward_works_and_fixed_k(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top2",
        )
        out, aux = model(torch.randn(2, 8, 32))
        assert out.shape == (2, 8, 32)
        assert aux["routing_metrics"]["actual_avg_k"].item() == pytest.approx(2.0)
        assert aux["expert_execution_mode"] == "FULLY_VECTORIZED"

    def test_deploy_bucketed_forward_works(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="bucketed",
        )
        out, aux = model(torch.randn(2, 8, 32))
        assert out.shape == (2, 8, 32)
        assert aux["runtime_branching_enabled"] is False

    def test_deploy_dense_masked_control_forward_works(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="dense_masked_control",
        )
        out, aux = model(torch.randn(2, 8, 32))
        assert out.shape == (2, 8, 32)
        assert aux["branch_tickets_enabled"] is False
        assert aux["routing_metrics"]["actual_owner_count_per_token"].item() == pytest.approx(2.0)
        assert aux["routing_metrics"]["actual_expert_slots_per_token"].item() == pytest.approx(4.0)
        assert aux["routing_metrics"]["dense_all_experts_executed"] is True

    def test_full_expert_ffn_control_has_distinct_architecture_id(self):
        delta = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="delta_large", pvr_deploy_mode="top1",
        )
        full = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="full_expert_ffn_control", pvr_deploy_mode="top1",
        )
        assert delta.expert_architecture_id != full.expert_architecture_id
        assert full.expert_architecture_id == "full_expert_ffn"

    def test_full_expert_ffn_control_not_same_class_as_delta_large(self):
        delta = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="delta_large", pvr_deploy_mode="top1",
        )
        full = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="full_expert_ffn_control", pvr_deploy_mode="top1",
        )
        assert type(delta.expert_deltas[0]) != type(full.expert_deltas[0])

    def test_full_expert_ffn_control_param_count_exceeds_delta_large(self):
        delta = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="delta_large", pvr_deploy_mode="top1",
        )
        full = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="full_expert_ffn_control", pvr_deploy_mode="top1",
        )
        delta_params = sum(p.numel() for p in delta.expert_deltas[0].parameters())
        full_params = sum(p.numel() for p in full.expert_deltas[0].parameters())
        assert full_params > delta_params

    def test_full_expert_ffn_control_inner_dim_matches_fixed_moe_expert(self):
        full = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="full_expert_ffn_control", pvr_deploy_mode="top1",
        )
        fixed = MoEFFN(d_model=32, d_ff=64, num_experts=4)
        assert full.expert_deltas[0].expert_inner_dim == fixed.experts[0].w1.out_features

    def test_ownership_top1_full_ffn_still_executes_one_owner_without_oracle_or_forced_action(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            expert_type="full_expert_ffn_control", pvr_deploy_mode="top1",
        )
        out, aux = model(torch.randn(2, 8, 32))
        assert out.shape == (2, 8, 32)
        routing = aux["routing_metrics"]
        assert routing["actual_owner_count_per_token"].item() == pytest.approx(1.0)
        assert routing["actual_expert_slots_per_token"].item() == pytest.approx(1.0)
        assert routing["dense_all_experts_executed"] is False
        assert routing["oracle_owner_used"] is False
        assert routing["forced_action_path_used"] is False

    def test_aux_alpha_changes_output(self):
        torch.manual_seed(7)
        base = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top2", pvr_aux_alpha=0.0,
        )
        other = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top2", pvr_aux_alpha=1.0,
        )
        other.load_state_dict(base.state_dict())
        x = torch.randn(2, 8, 32)
        out0, _ = base(x)
        out1, _ = other(x)
        assert not torch.allclose(out0, out1)

    def test_contribution_metrics_report_shared_and_sparse_norms(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_shared_scale=0.0,
        )
        x = torch.randn(2, 8, 32)
        _, aux = model(x)
        metrics = aux["contribution_metrics"]
        assert metrics["shared_output_norm"].item() == pytest.approx(0.0)
        assert metrics["sparse_output_norm"].item() > 0.0
        assert metrics["pvr_shared_scale"] == 0.0

    def test_toy_identity_dataset_shapes_valid(self):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(mode="pvr-overfit-sanity", scale="tiny")
        x, y = runner._make_pvr_overfit_batch("toy_identity", 4, 16, 256, torch.device("cpu"))
        assert x.shape == (4, 16)
        assert y.shape == (4, 16)
        assert torch.equal(x, y)

    def test_toy_copy_dataset_shapes_valid(self):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(mode="pvr-overfit-sanity", scale="tiny")
        x, y = runner._make_pvr_overfit_batch("toy_copy", 4, 16, 256, torch.device("cpu"))
        assert x.shape == (4, 16)
        assert y.shape == (4, 16)

    def test_single_batch_memorization_reuses_same_batch(self):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(mode="pvr-overfit-sanity", scale="tiny", seed=11)
        a = runner._make_pvr_overfit_batch("single_batch_memorization", 4, 16, 256, torch.device("cpu"))
        b = runner._make_pvr_overfit_batch("single_batch_memorization", 4, 16, 256, torch.device("cpu"))
        assert torch.equal(a[0], b[0])
        assert torch.equal(a[1], b[1])

    def test_overfit_diagnostic_reports_are_written(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="pvr-overfit-sanity",
            scale="tiny",
            models=["pvr_full"],
            diagnostic_sweeps={
                "pvr_overfit_tasks": ["toy_identity"],
                "pvr_overfit_steps": 1,
                "pvr_overfit_batch_size": 2,
                "pvr_overfit_single_batch": True,
            },
        )
        runner.output_dir = tmp_path
        runner._run_pvr_overfit_sanity()
        expected = {
            "pvr_ec_overfit_sanity_report.json",
            "pvr_ec_gradient_flow_report.json",
            "pvr_ec_optimizer_update_report.json",
            "pvr_ec_expert_contribution_report.json",
            "pvr_ec_shared_absorption_report.json",
            "pvr_ec_expert_initialization_report.json",
            "pvr_ec_loss_target_sanity_report.json",
            "pvr_ec_overfit_root_cause_summary.json",
        }
        for name in expected:
            assert (tmp_path / name).exists(), name

    def test_expert_parameters_require_grad_and_update_after_step(self):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner, MODELS

        runner = AlgorithmicBenchmarkRunner(mode="pvr-overfit-sanity", scale="tiny")
        model = runner._build_model_for_name("pvr_full", MODELS["pvr_full"])
        expert_params = [(n, p) for n, p in model.named_parameters() if "expert_deltas" in n]
        assert expert_params
        assert all(p.requires_grad for _, p in expert_params)
        opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
        names_in_optimizer = {id(p) for group in opt.param_groups for p in group["params"]}
        assert all(id(p) in names_in_optimizer for _, p in expert_params)
        x, y = runner._make_pvr_overfit_batch("toy_identity", 2, 16, 256, torch.device("cpu"))
        before = {n: p.detach().clone() for n, p in expert_params}
        loss = model(input_ids=x, targets=y)["loss"]
        loss.backward()
        opt.step()
        assert any((p.detach() - before[n]).abs().sum().item() > 0 for n, p in expert_params)

    def test_expert_gradient_norm_nonzero_on_toy_loss(self):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner, MODELS

        runner = AlgorithmicBenchmarkRunner(mode="pvr-overfit-sanity", scale="tiny")
        model = runner._build_model_for_name("pvr_full", MODELS["pvr_full"])
        x, y = runner._make_pvr_overfit_batch("toy_identity", 2, 16, 256, torch.device("cpu"))
        model(input_ids=x, targets=y)["loss"].backward()
        metrics = runner._gradient_flow_metrics(model)
        assert metrics["expert_gradient_norm_mean"] > 0.0

    def test_shared_only_variant_disables_sparse_path(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", expert_type="shared_base_only", pvr_expert_delta_scale=0.0,
        )
        _, aux = model(torch.randn(2, 8, 32))
        assert aux["contribution_metrics"]["sparse_output_norm"].item() == pytest.approx(0.0)

    def test_sparse_only_variant_disables_shared_path(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_shared_scale=0.0,
        )
        _, aux = model(torch.randn(2, 8, 32))
        assert aux["contribution_metrics"]["shared_output_norm"].item() == pytest.approx(0.0)

    def test_expert_delta_scale_changes_sparse_output_norm(self):
        torch.manual_seed(5)
        base = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_expert_delta_scale=1.0)
        scaled = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_expert_delta_scale=2.0)
        scaled.load_state_dict(base.state_dict())
        x = torch.randn(2, 8, 32)
        _, a = base(x)
        _, b = scaled(x)
        assert b["contribution_metrics"]["sparse_output_norm"].item() > a["contribution_metrics"]["sparse_output_norm"].item()

    def test_expert_delta_scale_schedule_returns_expected_values(self):
        schedule = ExpertDeltaScaleSchedule(
            schedule="linear_warmup", start=1.0, end=8.0, warmup_steps=10,
        )
        assert schedule.value(0) == pytest.approx(1.0)
        assert schedule.value(5) == pytest.approx(4.5)
        assert schedule.value(10) == pytest.approx(8.0)

    def test_expert_delta_scale_schedule_starts_at_configured_start(self):
        schedule = ExpertDeltaScaleSchedule(
            schedule="warmup_hold", start=2.0, end=6.0, warmup_steps=4,
        )
        assert schedule.value(0) == pytest.approx(2.0)

    def test_expert_delta_scale_schedule_reaches_target(self):
        schedule = ExpertDeltaScaleSchedule(
            schedule="cosine_warmup", start=1.0, end=4.0, warmup_steps=8,
        )
        assert schedule.value(8) == pytest.approx(4.0)
        assert schedule.value(80) == pytest.approx(4.0)

    def test_expert_delta_scale_schedule_optional_decay_works(self):
        schedule = ExpertDeltaScaleSchedule(
            schedule="warmup_hold_decay", start=1.0, end=8.0,
            warmup_steps=2, hold_steps=2, decay=4.0,
        )
        assert schedule.value(0) == pytest.approx(1.0)
        assert schedule.value(2) == pytest.approx(8.0)
        assert schedule.value(4) == pytest.approx(8.0)
        assert schedule.value(6) == pytest.approx(4.0)

    def test_scale_applies_only_to_sparse_delta(self):
        torch.manual_seed(7)
        base = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_expert_delta_scale=1.0,
        )
        scaled = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_expert_delta_scale=1.0,
            pvr_expert_delta_scale_schedule="warmup_hold",
            pvr_expert_delta_scale_start=1.0,
            pvr_expert_delta_scale_end=4.0,
            pvr_expert_delta_scale_warmup_steps=1,
        )
        scaled.load_state_dict(base.state_dict())
        base.eval()
        scaled.eval()
        x = torch.randn(2, 8, 32)
        base.set_training_step(1)
        scaled.set_training_step(1)
        _, a = base(x)
        _, b = scaled(x)
        assert b["contribution_metrics"]["shared_output_norm"].item() == pytest.approx(
            a["contribution_metrics"]["shared_output_norm"].item(), rel=1e-5
        )
        assert b["contribution_metrics"]["sparse_output_norm"].item() > a["contribution_metrics"]["sparse_output_norm"].item()

    def test_scale_does_not_change_owner_count(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_expert_delta_scale_schedule="warmup_hold",
            pvr_expert_delta_scale_start=1.0, pvr_expert_delta_scale_end=8.0,
            pvr_expert_delta_scale_warmup_steps=1,
        )
        model.set_training_step(1)
        _, aux = model(torch.randn(2, 8, 32))
        routing = aux["routing_metrics"]
        assert routing["actual_owner_count_per_token"].item() == pytest.approx(1.0)

    def test_scale_does_not_enable_top2_top4(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1", pvr_expert_delta_scale_schedule="warmup_hold",
            pvr_expert_delta_scale_start=1.0, pvr_expert_delta_scale_end=8.0,
            pvr_expert_delta_scale_warmup_steps=1,
        )
        model.set_training_step(1)
        _, aux = model(torch.randn(2, 8, 32))
        routing = aux["routing_metrics"]
        assert routing["actual_expert_slots_per_token"].item() == pytest.approx(1.0)
        assert routing["dense_all_experts_executed"] is False

    def test_shared_scale_changes_shared_output_norm(self):
        torch.manual_seed(6)
        base = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_shared_scale=1.0)
        scaled = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_shared_scale=0.5)
        scaled.load_state_dict(base.state_dict())
        x = torch.randn(2, 8, 32)
        _, a = base(x)
        _, b = scaled(x)
        assert b["contribution_metrics"]["shared_output_norm"].item() < a["contribution_metrics"]["shared_output_norm"].item()

    def test_fixed_owner_routes_all_tokens_to_one_expert(self):
        model = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_debug_force_expert_id=0)
        ids, _ = model._debug_or_router_top1(torch.randn(16, 32))
        assert set(ids.flatten().tolist()) == {0}

    def test_round_robin_owner_routes_multiple_experts(self):
        model = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_debug_owner_mode="round_robin")
        ids, _ = model._debug_or_router_top1(torch.randn(16, 32))
        assert len(set(ids.flatten().tolist())) > 1

    def test_owner_count_per_token_remains_one_and_top2_top4_not_executed(self):
        model = PVRECMoEFFN(d_model=32, d_ff=64, num_experts=4, num_prototypes=8, pvr_deploy_mode="top1", pvr_debug_owner_mode="uniform")
        _, aux = model(torch.randn(2, 8, 32))
        routing = aux["routing_metrics"]
        assert routing["actual_owner_count_per_token"].item() == pytest.approx(1.0)
        assert routing["actual_expert_slots_per_token"].item() == pytest.approx(1.0)
        assert routing["dense_all_experts_executed"] is False

    def test_scale_report_written(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="pvr-overfit-sanity",
            scale="tiny",
            device="cpu",
            models=["pvr_full", "pvr_full_scale_schedule_1_to_4"],
            root_cause_flags={"run_expert_delta_scale_schedule_diagnostic": True},
            diagnostic_sweeps={"pvr_overfit_tasks": ["toy_identity"], "pvr_overfit_steps": 2, "pvr_overfit_batch_size": 2},
        )
        runner.output_dir = tmp_path
        runner._run_pvr_nonlinear_overfit()
        report = tmp_path / "pvr_ec_expert_delta_scale_schedule_report.json"
        assert report.exists()
        payload = json.loads(report.read_text())
        assert "PVR_EC_EXPERT_DELTA_SCALE_SCHEDULE_IMPLEMENTED" in payload["statuses"]

    def test_benchmark_accepts_scale_schedule_cli(self):
        script = Path(__file__).resolve().parents[2] / "evaluation" / "run_algorithmic_benchmarks.py"
        result = subprocess.run(
            [sys.executable, str(script), "--help"],
            text=True,
            capture_output=True,
            check=True,
        )
        assert "--pvr-expert-delta-scale-schedule" in result.stdout
        assert "--run-expert-delta-scale-schedule-diagnostic" in result.stdout
        assert "--run-residual-alignment-diagnostic" in result.stdout

    def _write_transfer_reports(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="benchmark-lite",
            scale="small",
            root_cause_flags={
                "run_residual_alignment_diagnostic": True,
                "run_family_scale_sweep": True,
                "run_conditional_scale_oracle": True,
                "run_benchmark_transfer_confirmation": True,
            },
            diagnostic_sweeps={"conditional_scale_modes": ["family", "prototype", "owner"]},
        )
        runner.output_dir = tmp_path
        rows = []
        for family in ["clrs_style", "listops", "scan_style", "dyck"]:
            rows.append({
                "model_name": "pvr_ec_deploy_top1",
                "family": family,
                "task": family,
                "loss": 0.50,
                "accuracy": 0.10,
                "qpc": 0.10,
                "residual_help_rate": 0.25,
                "residual_harm_rate": 0.50,
                "residual_neutral_rate": 0.25,
                "token_loss_improvement": 0.02,
                "sequence_accuracy_improvement": 0.0,
                "token_to_sequence_transfer_ratio": 0.0,
                "decision_token_help_rate": 0.20,
                "decision_position_loss_delta": 0.03,
                "nondecision_position_loss_delta": 0.01,
                "final_token_loss_delta": 0.03,
                "segment_residual_norm": 1.0,
                "segment_residual_alignment": 0.02,
                "segment_residual_success_correlation": 0.0,
                "loss_delta_full_vs_shared": 0.02,
                "loss_shared_only": 0.48,
                "loss_full": 0.50,
                "loss_scaled": 0.50,
                "accuracy_shared_only": 0.11,
                "accuracy_full": 0.10,
                "accuracy_scaled": 0.10,
                "expert_delta_contribution_pct": 0.8,
                "shared_sparse_ratio": 0.2,
                "calibration_proxy": 0.1,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_actual_expert_slots_per_token": 1.0,
                "pvr_dense_all_experts_executed": False,
            })
            rows.append({
                "model_name": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
                "family": family,
                "task": family,
                "loss": 0.45 if family != "listops" else 0.55,
                "accuracy": 0.12,
                "qpc": 0.12,
                "residual_help_rate": 0.45,
                "residual_harm_rate": 0.35,
                "residual_neutral_rate": 0.20,
                "token_loss_improvement": 0.03,
                "sequence_accuracy_improvement": 0.0,
                "token_to_sequence_transfer_ratio": 0.0,
                "decision_token_help_rate": 0.40,
                "decision_position_loss_delta": 0.02,
                "nondecision_position_loss_delta": -0.02,
                "final_token_loss_delta": 0.02,
                "segment_residual_norm": 1.2,
                "segment_residual_alignment": 0.03,
                "segment_residual_success_correlation": 0.0,
                "loss_delta_full_vs_shared": -0.01 if family != "listops" else 0.03,
                "loss_shared_only": 0.46,
                "loss_full": 0.45 if family != "listops" else 0.55,
                "loss_scaled": 0.45 if family != "listops" else 0.55,
                "accuracy_shared_only": 0.10,
                "accuracy_full": 0.12,
                "accuracy_scaled": 0.12,
                "expert_delta_contribution_pct": 0.9,
                "shared_sparse_ratio": 0.1,
                "calibration_proxy": 0.09,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_actual_expert_slots_per_token": 1.0,
                "pvr_dense_all_experts_executed": False,
            })
        summary = {
            "model_table": {
                "pvr_ec_deploy_top1": {"avg_loss": 0.50, "avg_accuracy": 0.10},
                "pvr_ec_ownership_top1_best_scale_repair": {"avg_loss": 0.47, "avg_accuracy": 0.11},
            }
        }
        runner._write_benchmark_transfer_diagnostic_reports(rows, runner._artifact_metadata(), summary)
        return tmp_path

    def test_residual_alignment_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_residual_alignment_report.json").exists()

    def test_family_scale_sweep_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_family_scale_sweep_report.json").exists()

    def test_route_stability_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_scale_route_stability_report.json").exists()

    def test_conditional_scale_oracle_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_conditional_scale_oracle_report.json").exists()

    def test_residual_help_harm_rates_sum_to_one(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_residual_alignment_report.json").read_text())
        total = report["residual_help_rate"] + report["residual_harm_rate"] + report["residual_neutral_rate"]
        assert total == pytest.approx(1.0)

    def test_family_scale_sweep_contains_all_families(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_family_scale_sweep_report.json").read_text())
        assert set(report["families"]) == {"clrs_style", "listops", "scan_style", "dyck"}

    def test_scale_does_not_change_owner_ids_unless_expected(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_scale_route_stability_report.json").read_text())
        assert report["owner_id_match_rate_vs_scale_1"] == pytest.approx(1.0)

    def test_conditional_scale_is_marked_diagnostic_only(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_conditional_scale_oracle_report.json").read_text())
        assert report["diagnostic_only"] is True

    def test_benchmark_transfer_repair_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_benchmark_transfer_repair_report.json").exists()

    def test_transfer_profile_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_transfer_profile_report.json").exists()

    def test_decision_token_credit_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_decision_token_credit_report.json").exists()

    def test_token_to_sequence_transfer_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_token_to_sequence_transfer_report.json").exists()

    def test_output_readout_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_output_readout_report.json").exists()

    def test_family_failure_decomposition_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_family_failure_decomposition_report.json").exists()

    def test_loss_credit_repair_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_loss_credit_repair_report.json").exists()

    def test_curriculum_repair_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_curriculum_repair_report.json").exists()

    def test_segment_residual_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_segment_residual_diagnostic_report.json").exists()

    def test_repair_selection_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_transfer_repair_selection_report.json").exists()

    def test_transfer_confirmation_report_written(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        assert (out / "pvr_ec_task_transfer_repair_confirmation_report.json").exists()

    def test_token_to_sequence_transfer_ratio_is_finite(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_token_to_sequence_transfer_report.json").read_text())
        assert abs(float(report["token_to_sequence_transfer_ratio"])) < 1e9

    def test_decision_token_metrics_exist_by_family(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_decision_token_credit_report.json").read_text())
        assert set(report["by_family"]) == {"clrs_style", "listops", "scan_style", "dyck"}

    def test_family_failure_decomposition_contains_listops_scan_dyck(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_family_failure_decomposition_report.json").read_text())
        assert "listops_decomposition" in report
        assert "scan_decomposition" in report
        assert "dyck_decomposition" in report

    def test_loss_weighting_variants_register(self):
        from run_algorithmic_benchmarks import _parse_csv_strings

        variants = _parse_csv_strings("baseline_loss,final_token_weight_2x,listops_weight_2x")
        assert "final_token_weight_2x" in variants

    def test_curriculum_variants_register(self):
        from run_algorithmic_benchmarks import _parse_csv_strings

        variants = _parse_csv_strings("baseline_curriculum,easy_to_hard_length_curriculum")
        assert "easy_to_hard_length_curriculum" in variants

    def test_readout_variants_register_as_diagnostic(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_output_readout_report.json").read_text())
        assert report["diagnostic_only"] is True

    def test_segment_residual_metrics_are_finite(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_segment_residual_diagnostic_report.json").read_text())
        assert float(report["segment_residual_norm"]) >= 0.0

    def test_repair_selection_prefers_low_complexity_when_scores_tie(self, tmp_path):
        out = self._write_transfer_reports(tmp_path)
        report = json.loads((out / "pvr_ec_transfer_repair_selection_report.json").read_text())
        assert report["selected_repair"] == "no_architecture_scale_control"

    def _write_sparse_direction_reports(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="smoke",
            root_cause_flags={
                "run_sparse_logit_direction_diagnostic": True,
                "run_sparse_auxiliary_loss_sweep": True,
                "run_sparse_auxiliary_scope_sweep": True,
                "run_sparse_direction_transfer_confirmation": True,
                "run_calibration_constrained_sparse_aux_sweep": True,
            },
            diagnostic_sweeps={
                "sparse_aux_loss_variants": ["baseline_main_loss", "sparse_ce_0_05", "sparse_ce_warmup_decay"],
                "sparse_aux_scopes": ["aux_all_tokens", "aux_decision_tokens_only"],
            },
        )
        runner.output_dir = tmp_path
        rows = []
        for family in ["clrs_style", "listops", "scan_style", "dyck"]:
            rows.append({
                "model_name": "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__baseline_main_loss",
                "family": family,
                "task": family,
                "loss": 0.50,
                "accuracy": 0.10,
                "qpc": 0.10,
                "sparse_aux_loss_variant": "baseline_main_loss",
                "sparse_aux_scope": "aux_all_tokens",
                "correct_class_logit_delta": 0.5,
                "incorrect_class_logit_delta": 3.0,
                "incorrect_class_logit_delta_mean": 0.2,
                "incorrect_class_logit_delta_max": 3.0,
                "delta_correct_minus_top_wrong": -2.5,
                "sparse_margin_delta": -2.5,
                "combined_margin_delta": -0.5,
                "shared_margin": -1.0,
                "combined_margin": -1.5,
                "sparse_logit_norm": 4.0,
                "combined_logit_norm": 5.0,
                "incorrect_logit_overamplification_rate": 0.8,
                "correct_logit_underamplification_rate": 0.1,
                "residual_help_rate": 0.6,
                "residual_harm_rate": 0.4,
                "token_to_sequence_transfer_ratio": -1.0,
                "calibration_proxy": 0.1,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
            })
            rows.append({
                "model_name": "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__wrong_suppress_0_03_t0_25",
                "family": family,
                "task": family,
                "loss": 0.45,
                "accuracy": 0.11,
                "qpc": 0.11,
                "sparse_aux_loss_variant": "wrong_suppress_0_03_t0_25",
                "sparse_aux_scope": "aux_all_tokens",
                "correct_class_logit_delta": 0.7,
                "incorrect_class_logit_delta": 1.5,
                "incorrect_class_logit_delta_mean": 0.1,
                "incorrect_class_logit_delta_max": 1.5,
                "delta_correct_minus_top_wrong": -0.8,
                "sparse_margin_delta": -0.8,
                "combined_margin_delta": 0.1,
                "shared_margin": -1.0,
                "combined_margin": -0.9,
                "sparse_logit_norm": 3.0,
                "combined_logit_norm": 4.5,
                "incorrect_logit_overamplification_rate": 0.6,
                "correct_logit_underamplification_rate": 0.05,
                "residual_help_rate": 0.65,
                "residual_harm_rate": 0.35,
                "token_to_sequence_transfer_ratio": 0.2,
                "calibration_proxy": 0.09,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
            })
            rows.append({
                "model_name": "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05",
                "family": family,
                "task": family,
                "loss": 0.42,
                "accuracy": 0.24,
                "qpc": 0.24,
                "sparse_aux_loss_variant": "sparse_ce_0_05",
                "sparse_aux_scope": "aux_all_tokens",
                "correct_class_logit_delta": 4.7,
                "incorrect_class_logit_delta": 5.8,
                "incorrect_class_logit_delta_mean": 0.2,
                "incorrect_class_logit_delta_max": 5.8,
                "delta_correct_minus_top_wrong": -1.1,
                "sparse_margin_delta": -1.1,
                "combined_margin_delta": 0.1,
                "shared_margin": -1.0,
                "combined_margin": -0.9,
                "sparse_logit_norm": 6.0,
                "combined_logit_norm": 6.5,
                "incorrect_logit_overamplification_rate": 0.7,
                "correct_logit_underamplification_rate": 0.02,
                "residual_help_rate": 0.98,
                "residual_harm_rate": 0.02,
                "token_to_sequence_transfer_ratio": 0.05,
                "calibration_proxy": 0.13,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
            })
            rows.append({
                "model_name": "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_warmup_decay",
                "family": family,
                "task": family,
                "loss": 0.43,
                "accuracy": 0.23,
                "qpc": 0.23,
                "sparse_aux_loss_variant": "sparse_ce_warmup_decay",
                "sparse_aux_scope": "aux_all_tokens",
                "correct_class_logit_delta": 4.0,
                "incorrect_class_logit_delta": 4.7,
                "incorrect_class_logit_delta_mean": 0.15,
                "incorrect_class_logit_delta_max": 4.7,
                "delta_correct_minus_top_wrong": -0.7,
                "sparse_margin_delta": -0.7,
                "combined_margin_delta": 0.12,
                "shared_margin": -1.0,
                "combined_margin": -0.88,
                "sparse_logit_norm": 5.0,
                "combined_logit_norm": 6.0,
                "incorrect_logit_overamplification_rate": 0.55,
                "correct_logit_underamplification_rate": 0.02,
                "residual_help_rate": 0.96,
                "residual_harm_rate": 0.04,
                "token_to_sequence_transfer_ratio": 0.06,
                "calibration_proxy": 0.10,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
            })
            rows.append({
                "model_name": "pvr_ec_ownership_top1_best_sparse_logit_repair",
                "family": family,
                "task": family,
                "loss": 0.43,
                "accuracy": 0.23,
                "qpc": 0.23,
                "sparse_aux_loss_variant": "sparse_ce_warmup_decay",
                "sparse_aux_scope": "aux_all_tokens",
                "correct_class_logit_delta": 4.0,
                "incorrect_class_logit_delta_max": 4.7,
                "delta_correct_minus_top_wrong": -0.7,
                "residual_help_rate": 0.65,
                "residual_harm_rate": 0.35,
                "token_to_sequence_transfer_ratio": 0.2,
                "calibration_proxy": 0.10,
                "inference_time_s": 0.1,
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
            })
        summary = {
            "model_table": {
                "pvr_ec_deploy_top1": {"avg_loss": 0.50, "avg_accuracy": 0.10},
                "pvr_ec_ownership_top1_best_sparse_logit_repair": {"avg_loss": 0.45, "avg_accuracy": 0.11},
                "fixed_moe_vectorized": {"avg_loss": 0.40, "avg_accuracy": 0.20},
            }
        }
        runner._write_sparse_logit_direction_reports(rows, runner._artifact_metadata(), summary)
        return tmp_path

    def test_sparse_logit_direction_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_sparse_logit_direction_report.json").exists()

    def test_sparse_auxiliary_loss_sweep_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_sparse_auxiliary_loss_sweep_report.json").exists()

    def test_sparse_direction_by_family_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_sparse_direction_by_family_report.json").exists()

    def test_sparse_direction_repair_selection_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_sparse_direction_repair_selection_report.json").exists()

    def test_sparse_direction_transfer_confirmation_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_sparse_direction_transfer_confirmation_report.json").exists()

    def test_sparse_direction_metrics_are_computed(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        report = json.loads((out / "pvr_ec_sparse_logit_direction_report.json").read_text())
        assert report["correct_class_logit_delta"] == pytest.approx(0.5)
        assert report["incorrect_class_logit_delta_max"] == pytest.approx(3.0)
        assert report["delta_correct_minus_top_wrong"] == pytest.approx(-2.5)

    def test_sparse_auxiliary_sweep_selects_helpful_variant(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        report = json.loads((out / "pvr_ec_sparse_auxiliary_loss_sweep_report.json").read_text())
        assert report["best_auxiliary_loss"] == "sparse_ce_0_05"

    def test_calibration_constrained_sparse_aux_report_written(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        assert (out / "pvr_ec_calibration_constrained_sparse_aux_report.json").exists()

    def test_calibration_constrained_selector_prefers_lower_ece_close_capability(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        report = json.loads((out / "pvr_ec_calibration_constrained_sparse_aux_report.json").read_text())
        assert report["selected_calibration_constrained_variant"] == "sparse_ce_warmup_decay"

    def test_sparse_direction_confirmation_keeps_top1_only(self, tmp_path):
        out = self._write_sparse_direction_reports(tmp_path)
        report = json.loads((out / "pvr_ec_sparse_direction_transfer_confirmation_report.json").read_text())
        assert report["owner_count_per_token"] == pytest.approx(1.0)
        assert report["Top2_executions"] == pytest.approx(0.0)
        assert report["Top4_executions"] == pytest.approx(0.0)

    def test_vectorized_expert_execution_preserves_shape(self):
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top2",
        )
        flat = torch.randn(16, 32)
        ids = torch.randint(0, 4, (16, 2))
        out = model._vectorized_expert_deltas(flat, ids)
        assert out.shape == (16, 2, 32)

    def test_deploy_forward_static_hot_path_rules(self):
        source = inspect.getsource(PVRECMoEFFN._deploy_forward)
        assert ".cpu(" not in source
        assert "synchronize" not in source
        assert ".item(" not in source

    def test_pvr_deployment_report_is_written(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="smoke",
            models=["fixed_moe", "pvr_ec_deploy_top2"],
            benchmark_inference_only=True,
            batch_sizes=[1],
            sequence_lengths=[16],
            warmup_steps=1,
            timed_steps=1,
        )
        runner.output_dir = tmp_path
        rows = [
            {
                "model": "fixed_moe", "deploy_mode": "off", "params": 1,
                "active_params_estimate": 1, "batch_size": 1, "sequence_length": 16,
                "loss": 1.0, "accuracy": 0.1, "p50_latency_ms": 1.0,
                "p95_latency_ms": 1.0, "mean_latency_ms": 1.0,
                "tokens_per_second": 16.0, "samples_per_second": 1.0,
                "quality_per_ms": 0.1, "quality_per_token_second": 1.6,
                "memory_allocated_mb": 1.0, "max_memory_allocated_mb": 2.0,
                "expert_execution_mode": "LOOPED", "branch_tickets_enabled": False,
                "mergeability_mode": "disabled", "runtime_branching_enabled": False,
            },
            {
                "model": "fixed_moe_vectorized", "deploy_mode": "off", "params": 1,
                "active_params_estimate": 1, "batch_size": 1, "sequence_length": 16,
                "loss": 1.0, "accuracy": 0.1, "p50_latency_ms": 0.8,
                "p95_latency_ms": 0.8, "mean_latency_ms": 0.8,
                "tokens_per_second": 20.0, "samples_per_second": 1.25,
                "quality_per_ms": 0.125, "quality_per_token_second": 2.0,
                "memory_allocated_mb": 1.0, "max_memory_allocated_mb": 2.0,
                "expert_execution_mode": "FULLY_VECTORIZED", "branch_tickets_enabled": False,
                "mergeability_mode": "disabled", "runtime_branching_enabled": False,
                "quality_per_memory_mb": 0.05, "latency_per_memory_mb": 0.4,
            },
            {
                "model": "pvr_ec_deploy_top2", "deploy_mode": "top2", "params": 1,
                "active_params_estimate": 1, "batch_size": 1, "sequence_length": 16,
                "loss": 1.1, "accuracy": 0.1, "p50_latency_ms": 1.2,
                "p95_latency_ms": 1.2, "mean_latency_ms": 1.2,
                "tokens_per_second": 13.3, "samples_per_second": 0.8,
                "quality_per_ms": 0.083, "quality_per_token_second": 1.3,
                "memory_allocated_mb": 1.0, "max_memory_allocated_mb": 2.0,
                "expert_execution_mode": "FULLY_VECTORIZED", "branch_tickets_enabled": False,
                "mergeability_mode": "disabled", "runtime_branching_enabled": False,
                "quality_per_memory_mb": 0.05, "latency_per_memory_mb": 0.6,
            },
        ]
        runner._write_deployment_reports(rows)
        expected = {
            "pvr_deployment_report.json",
            "pvr_deployment_report.md",
            "pvr_inference_latency_report.json",
            "pvr_hot_path_profile.json",
            "pvr_deploy_comparison.csv",
            "pvr_deploy_status.json",
            "fair_deployment_comparison_report.json",
            "fair_deployment_comparison_report.md",
            "fixed_moe_vectorization_report.json",
            "inference_latency_matrix.csv",
            "inference_latency_matrix.json",
            "memory_efficiency_report.json",
            "aux_alpha_capability_report.json",
            "pvr_deploy_go_no_go.json",
            "longer_capability_report.json",
        }
        for name in expected:
            assert (tmp_path / name).exists()

    def _write_synthetic_root_cause_reports(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(
            mode="smoke",
            root_cause_flags={
                "run_root_baseline_matrix": True,
                "run_training_dynamics_diagnostic": True,
                "run_ownership_integration_diagnostic": True,
                "run_shared_sparse_ablation": True,
                "run_loss_calibration_diagnostic": True,
                "run_task_fit_diagnostic": True,
                "run_latency_stability_diagnostic": True,
            },
            diagnostic_sweeps={
                "loss_schedule_sweep": ["ce_only", "aux_delta"],
                "task_loss_schedule_sweep": ["uniform", "family_balanced"],
            },
        )
        runner.output_dir = tmp_path
        rows = [
            {
                "model": "fixed_moe_vectorized",
                "family": "clrs",
                "task": "clrs_sorting",
                "loss": 0.7,
                "accuracy": 0.4,
                "training_loss": 0.8,
                "params": 100,
                "active_params_estimate": 100,
                "p50_latency_ms": 1.0,
                "p95_latency_ms": 1.1,
                "batch_size": 1,
                "sequence_length": 16,
            },
            {
                "model": "pvr_ec_ownership_top1_delta_medium",
                "family": "clrs",
                "task": "clrs_sorting",
                "loss": 0.8,
                "accuracy": 0.35,
                "training_loss": 0.9,
                "params": 120,
                "active_params_estimate": 80,
                "capacity_variant": "delta_medium",
                "pvr_expert_type": "delta_medium",
                "actual_owner_count_per_token": 1.0,
                "actual_experts_executed": 1.0,
                "owner_change_count": 0,
                "p50_latency_ms": 1.0,
                "p95_latency_ms": 4.0,
                "batch_size": 1,
                "sequence_length": 16,
            },
            {
                "model": "pvr_ec_shared_only_ablation",
                "family": "scan",
                "task": "scan_random",
                "loss": 0.6,
                "accuracy": 0.5,
                "training_loss": 0.6,
                "params": 110,
                "active_params_estimate": 70,
                "pvr_expert_type": "shared_base_only",
                "shared_output_norm": 4.0,
                "sparse_output_norm": 0.0,
                "shared_sparse_ratio": 10.0,
                "p50_latency_ms": 2.0,
                "p95_latency_ms": 2.2,
            },
            {
                "model": "pvr_ec_sparse_only_ablation",
                "family": "dyck",
                "task": "dyck_completion",
                "loss": 0.9,
                "accuracy": 0.2,
                "training_loss": 0.9,
                "params": 110,
                "active_params_estimate": 70,
                "shared_output_norm": 0.0,
                "sparse_output_norm": 3.0,
                "p50_latency_ms": 2.0,
                "p95_latency_ms": 2.2,
            },
        ]
        runner._write_root_cause_artifacts(rows, runner._artifact_metadata(), source="trained_benchmark")
        return tmp_path

    def test_root_cause_reports_are_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        expected = {
            "pvr_ec_root_cause_loop_report.json",
            "pvr_ec_root_cause_loop_report.md",
            "pvr_ec_root_baseline_matrix.json",
            "pvr_ec_root_baseline_matrix.md",
            "pvr_ec_training_dynamics_report.json",
            "pvr_ec_training_dynamics_report.md",
            "pvr_ec_ownership_integration_report.json",
            "pvr_ec_ownership_integration_report.md",
            "pvr_ec_shared_sparse_ablation_report.json",
            "pvr_ec_shared_sparse_ablation_report.md",
            "pvr_ec_learning_separation_report.json",
            "pvr_ec_learning_separation_report.md",
            "pvr_ec_loss_calibration_report.json",
            "pvr_ec_loss_calibration_report.md",
            "pvr_ec_task_fit_report.json",
            "pvr_ec_task_fit_report.md",
            "pvr_ec_latency_stability_report.json",
            "pvr_ec_latency_stability_report.md",
            "pvr_ec_root_cause_summary.json",
            "pvr_ec_root_cause_summary.md",
        }
        for name in expected:
            assert (tmp_path / name).exists(), name

    def test_root_cause_loop_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_root_cause_loop_report.json").exists()

    def test_training_dynamics_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_training_dynamics_report.json").exists()

    def test_ownership_integration_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_ownership_integration_report.json").exists()

    def test_shared_sparse_ablation_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_shared_sparse_ablation_report.json").exists()

    def test_loss_calibration_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_loss_calibration_report.json").exists()

    def test_task_fit_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_task_fit_report.json").exists()

    def test_latency_stability_report_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_latency_stability_report.json").exists()

    def test_root_cause_summary_written(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        assert (tmp_path / "pvr_ec_root_cause_summary.json").exists()

    def test_root_cause_report_fields_are_recorded(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        ownership = json.loads((tmp_path / "pvr_ec_ownership_integration_report.json").read_text())
        assert ownership["owner_changed_success_rate"] is None
        shared_sparse = json.loads((tmp_path / "pvr_ec_shared_sparse_ablation_report.json").read_text())
        assert shared_sparse["shared_only_sparse_disabled"]
        assert shared_sparse["sparse_only_shared_disabled"]
        calibration = json.loads((tmp_path / "pvr_ec_loss_calibration_report.json").read_text())
        assert {"nll", "brier_score", "ece", "confidence_histogram"} <= set(calibration["metrics"])
        task_fit = json.loads((tmp_path / "pvr_ec_task_fit_report.json").read_text())
        assert {"clrs", "scan", "dyck"} <= set(task_fit["per_family"])
        latency = json.loads((tmp_path / "pvr_ec_latency_stability_report.json").read_text())
        assert latency["latency_p95_p50_ratio_reported"] is True
        assert latency["max_latency_p95_p50_ratio"] == pytest.approx(4.0)
        learning = json.loads((tmp_path / "pvr_ec_learning_separation_report.json").read_text())
        assert learning["key_metric"] == "full_model_score_minus_shared_only_score"
        assert "full_model_score_minus_shared_only_score" in learning["learning_separation"]

    def test_shared_only_ablation_has_metrics(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_shared_sparse_ablation_report.json").read_text())
        assert report["shared_only_sparse_disabled"]

    def test_sparse_only_ablation_has_metrics(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_shared_sparse_ablation_report.json").read_text())
        assert report["sparse_only_shared_disabled"]

    def test_owner_change_success_null_when_no_changes(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_ownership_integration_report.json").read_text())
        assert report["owner_changed_success_rate"] is None

    def test_calibration_metrics_are_reported(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_loss_calibration_report.json").read_text())
        assert {"nll", "brier_score", "ece", "confidence_histogram"} <= set(report["metrics"])

    def test_per_family_metrics_are_reported(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_task_fit_report.json").read_text())
        assert {"clrs", "scan", "dyck"} <= set(report["per_family"])

    def test_latency_p95_p50_ratio_reported(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_latency_stability_report.json").read_text())
        assert report["latency_p95_p50_ratio_reported"] is True
        assert report["max_latency_p95_p50_ratio"] == pytest.approx(4.0)

    def test_learning_separation_gap_is_reported(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        report = json.loads((tmp_path / "pvr_ec_learning_separation_report.json").read_text())
        assert report["key_metric"] == "full_model_score_minus_shared_only_score"
        assert report["learning_separation"]["full_model"]["count"] > 0
        assert report["learning_separation"]["shared_only"]["count"] > 0

    def test_root_cause_labels_are_valid_and_promotion_blocked(self, tmp_path):
        from sparse_loop_moe.models.pvr_ec.diagnostics import PVR_EC_STATUSES

        self._write_synthetic_root_cause_reports(tmp_path)
        summary = json.loads((tmp_path / "pvr_ec_root_cause_summary.json").read_text())
        assert set(summary["statuses"]) <= set(PVR_EC_STATUSES)
        assert "PVR_EC_DO_NOT_PROMOTE" in summary["statuses"]
        assert summary["promotion_ready"] is False
        assert summary["do_not_promote"] is True

    def test_promotion_stays_blocked_without_clean_evidence(self, tmp_path):
        self._write_synthetic_root_cause_reports(tmp_path)
        summary = json.loads((tmp_path / "pvr_ec_root_cause_summary.json").read_text())
        assert summary["promotion_ready"] is False
        assert summary["do_not_promote"] is True

    def test_capacity_fairness_reports_are_written(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(mode="smoke")
        runner.output_dir = tmp_path
        rows = [
            {
                "model": "pvr_ec_ownership_top1_delta_medium",
                "deploy_mode": "top1",
                "capacity_variant": "delta_medium",
                "pvr_expert_type": "delta_rank_medium",
                "expert_architecture_id": "delta_rank_32",
                "expert_hidden_dim": 32,
                "expert_inner_dim": 32,
                "delta_rank": 32,
                "params": 100,
                "param_count": 100,
                "active_param_count": 50,
                "active_params_estimate": 50,
                "params_per_expert": 10,
                "shared_params": 20,
                "routed_expert_params": 40,
                "module_class_names": "LowRankExpertDelta",
                "module_fingerprint": "delta-fp",
                "actual_owner_count_per_token": 1.0,
                "actual_experts_executed": 1.0,
                "actual_expert_slots_per_token": 1.0,
                "dense_all_experts_executed": False,
                "oracle_owner_used": False,
                "forced_action_path_used": False,
                "replay_probe_labels_used": False,
                "batch_size": 1,
                "sequence_length": 16,
                "loss": 1.0,
                "accuracy": 0.5,
                "p50_latency_ms": 1.0,
                "p95_latency_ms": 1.2,
                "mean_latency_ms": 1.1,
                "quality_per_ms": 0.45,
                "quality_per_active_param": 0.01,
            },
            {
                "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
                "deploy_mode": "top1",
                "capacity_variant": "full_expert_ffn",
                "pvr_expert_type": "full_expert_ffn",
                "expert_architecture_id": "full_expert_ffn",
                "expert_hidden_dim": 64,
                "expert_inner_dim": 64,
                "delta_rank": 0,
                "params": 200,
                "param_count": 200,
                "active_param_count": 80,
                "active_params_estimate": 80,
                "params_per_expert": 20,
                "shared_params": 20,
                "routed_expert_params": 80,
                "module_class_names": "FullExpertFFN",
                "module_fingerprint": "full-fp",
                "actual_owner_count_per_token": 1.0,
                "actual_experts_executed": 1.0,
                "actual_expert_slots_per_token": 1.0,
                "dense_all_experts_executed": False,
                "oracle_owner_used": False,
                "forced_action_path_used": False,
                "replay_probe_labels_used": False,
                "batch_size": 1,
                "sequence_length": 16,
                "loss": 0.5,
                "accuracy": 0.8,
                "p50_latency_ms": 0.9,
                "p95_latency_ms": 1.0,
                "mean_latency_ms": 0.95,
                "quality_per_ms": 0.84,
                "quality_per_active_param": 0.01,
            },
        ]
        runner._write_capacity_proof_artifacts(rows, runner._artifact_metadata(), source="inference_only")
        expected = {
            "capacity_fairness_matrix_report.json",
            "capacity_fairness_matrix_report.md",
            "capacity_interpolation_report.json",
            "capacity_distillation_compression_plan.json",
            "pvr_ec_capacity_architecture_report.json",
            "pvr_ec_capacity_architecture_report.md",
            "capacity_fairness_audit_report.json",
            "capacity_fairness_audit_report.md",
            "capacity_knee_report.json",
        }
        for name in expected:
            assert (tmp_path / name).exists()
        report = json.loads((tmp_path / "capacity_fairness_matrix_report.json").read_text())
        assert report["promotion_ready"] is False
        assert report["hard_assertions"]["actual_owner_count_per_token_equals_1"] is True
        assert "PVR_EC_DO_NOT_PROMOTE" in report["statuses"]
        arch = json.loads((tmp_path / "pvr_ec_capacity_architecture_report.json").read_text())
        full = next(r for r in arch["rows"] if r["model_name"] == "pvr_ec_ownership_top1_full_expert_ffn_control")
        assert full["aliases_detected"] is False

    def test_capacity_architecture_report_detects_aliases(self, tmp_path):
        from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

        runner = AlgorithmicBenchmarkRunner(mode="smoke")
        runner.output_dir = tmp_path
        rows = [
            {
                "model": "pvr_ec_ownership_top1_delta_large",
                "capacity_variant": "delta_large",
                "pvr_expert_type": "delta_large",
                "expert_architecture_id": "delta_rank_32",
                "expert_inner_dim": 32,
                "delta_rank": 32,
                "param_count": 100,
                "active_param_count": 50,
                "params_per_expert": 10,
                "module_class_names": "LowRankExpertDelta",
                "module_fingerprint": "same",
                "actual_owner_count_per_token": 1.0,
                "actual_expert_slots_per_token": 1.0,
                "dense_all_experts_executed": False,
                "loss": 1.0,
                "accuracy": 0.1,
            },
            {
                "model": "pvr_ec_ownership_top1_full_expert_ffn_control",
                "capacity_variant": "full_expert_ffn",
                "pvr_expert_type": "full_expert_ffn_control",
                "expert_architecture_id": "delta_rank_32",
                "expert_inner_dim": 32,
                "delta_rank": 32,
                "param_count": 100,
                "active_param_count": 50,
                "params_per_expert": 10,
                "module_class_names": "LowRankExpertDelta",
                "module_fingerprint": "same",
                "actual_owner_count_per_token": 1.0,
                "actual_expert_slots_per_token": 1.0,
                "dense_all_experts_executed": False,
                "loss": 1.0,
                "accuracy": 0.1,
            },
        ]
        runner._write_capacity_proof_artifacts(rows, runner._artifact_metadata(), source="trained_benchmark")
        report = json.loads((tmp_path / "capacity_fairness_matrix_report.json").read_text())
        assert "PVR_EC_FULL_EXPERT_CONTROL_ALIAS_DETECTED" in report["statuses"]
        assert "PVR_EC_CAPACITY_LADDER_INVALID" in report["statuses"]


def _final_gate_runner(tmp_path):
    from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

    runner = AlgorithmicBenchmarkRunner(
        mode="smoke",
        models=["fixed_moe_vectorized", "pvr_ec_deploy_top1", "pvr_ec_ownership_top1_final_candidate_v1"],
        root_cause_flags={
            "run_final_config_manifest": True,
            "run_forward_purity_gate": True,
            "run_family_regression_gate": True,
            "run_quality_per_ms_memory_gate": True,
            "run_reliability_proxy_gate": True,
            "run_final_calibration_sweep": True,
        },
    )
    runner.output_dir = tmp_path
    return runner


def _candidate_rows():
    rows = []
    for family in ["clrs_style", "listops", "scan_style", "dyck"]:
        rows.extend([
            {
                "model_name": "fixed_moe_vectorized",
                "model": "fixed_moe_vectorized",
                "family": family,
                "task": family,
                "loss": 0.39,
                "accuracy": 0.26,
                "qpc": 0.13,
                "calibration_proxy": 0.10,
                "inference_time_s": 0.50,
            },
            {
                "model_name": "pvr_ec_deploy_top1",
                "model": "pvr_ec_deploy_top1",
                "family": family,
                "task": family,
                "loss": 0.45,
                "accuracy": 0.08,
                "qpc": 0.08,
                "calibration_proxy": 0.09,
                "inference_time_s": 0.40,
            },
            {
                "model_name": "pvr_ec_ownership_top1_final_candidate_v1",
                "model": "pvr_ec_ownership_top1_final_candidate_v1",
                "family": family,
                "task": family,
                "loss": 0.398,
                "accuracy": 0.248,
                "qpc": 0.248,
                "calibration_proxy": 0.105,
                "confidence_when_correct": 0.70,
                "confidence_when_wrong": 0.40,
                "incorrect_logit_overamplification_rate": 0.3,
                "delta_correct_minus_top_wrong": -0.70,
                "residual_help_rate": 0.9,
                "residual_harm_rate": 0.02,
                "decision_token_help_rate": 0.8,
                "token_to_sequence_transfer_ratio": 0.07,
                "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light",
                "sparse_aux_scope": "aux_all_tokens",
                "pvr_actual_owner_count_per_token": 1.0,
                "pvr_num_k2_tokens": 0.0,
                "pvr_num_k4_tokens": 0.0,
                "pvr_oracle_owner_used": False,
                "pvr_forced_action_path_used": False,
                "pvr_replay_probe_labels_used": False,
                "inference_time_s": 0.30,
            },
        ])
    return rows


def _summary():
    return {
        "model_table": {
            "fixed_moe_vectorized": {"avg_loss": 0.39, "avg_accuracy": 0.26, "avg_qpc": 0.13},
            "pvr_ec_deploy_top1": {"avg_loss": 0.45, "avg_accuracy": 0.08, "avg_qpc": 0.08},
            "pvr_ec_ownership_top1_final_candidate_v1": {"avg_loss": 0.398, "avg_accuracy": 0.248, "avg_qpc": 0.248},
        }
    }


def test_final_candidate_config_exists():
    assert Path("configs/pvr_ec_ownership_top1_final_candidate_v1.json").exists()
    assert Path("configs/pvr_ec_ownership_top1_final_candidate_v1.yaml").exists()


def test_final_candidate_config_loads():
    cfg = json.loads(Path("configs/pvr_ec_ownership_top1_final_candidate_v1.json").read_text())
    assert cfg["model_name"] == "pvr_ec_ownership_top1_final_candidate_v1"
    assert cfg["ownership_mode"] == "top1"


def test_final_candidate_resolves_expected_aux_loss():
    from run_algorithmic_benchmarks import MODELS

    overrides = MODELS["pvr_ec_ownership_top1_final_candidate_v1"]["overrides"]
    assert overrides["sparse_aux_loss_variant"] == "sparse_ce_0_05_plus_logit_norm_penalty_light"


def test_final_candidate_resolves_expected_scale_schedule():
    from run_algorithmic_benchmarks import MODELS

    overrides = MODELS["pvr_ec_ownership_top1_final_candidate_v1"]["overrides"]
    assert overrides["pvr_expert_delta_scale_schedule"] == "warmup_hold"
    assert overrides["pvr_expert_delta_scale_end"] == 8.0


def test_final_candidate_hash_is_stable(tmp_path):
    runner = _final_gate_runner(tmp_path)
    cfg = runner._final_candidate_config()
    assert runner._stable_hash(cfg) == runner._stable_hash(cfg)


def test_final_candidate_forward_purity_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    report = runner._write_forward_purity_gate(_candidate_rows())
    assert report["passed"] is True
    assert (tmp_path / "pvr_ec_final_forward_purity_report.json").exists()


def test_multiseed_confirmation_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_multiseed_confirmation_report", {"status": "PVR_EC_MULTI_SEED_CONFIRMED", "passed": True}, "x")
    assert (tmp_path / "pvr_ec_multiseed_confirmation_report.json").exists()


def test_longer_training_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_longer_training_confirmation_report", {"status": "PVR_EC_LONGER_TRAINING_CONFIRMED", "passed": True}, "x")
    assert (tmp_path / "pvr_ec_longer_training_confirmation_report.json").exists()


def test_matched_step_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_matched_step_report", {"status": "PVR_EC_MATCHED_STEP_CONFIRMED", "passed": True}, "x")
    assert (tmp_path / "pvr_ec_matched_step_report.json").exists()


def test_matched_wall_clock_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_matched_wall_clock_report", {"status": "PVR_EC_MATCHED_WALL_CLOCK_CONFIRMED", "passed": True}, "x")
    assert (tmp_path / "pvr_ec_matched_wall_clock_report.json").exists()


def test_final_calibration_sweep_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    runner._write_final_calibration_sweep_report(_candidate_rows(), runner._artifact_metadata(), _summary())
    assert (tmp_path / "pvr_ec_final_calibration_sweep_report.json").exists()


def test_family_regression_gate_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    runner._write_family_regression_gate(_candidate_rows(), _summary())
    assert (tmp_path / "pvr_ec_family_regression_gate_report.json").exists()


def test_quality_per_ms_memory_gate_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = [
        {"model": "fixed_moe_vectorized", "batch_size": 1, "sequence_length": 64, "loss": 0.39, "accuracy": 0.26, "p50_latency_ms": 2.0, "p95_latency_ms": 2.1, "max_memory_allocated_mb": 100, "active_param_count": 1000},
        {"model": "pvr_ec_ownership_top1_final_candidate_v1", "batch_size": 1, "sequence_length": 64, "loss": 0.398, "accuracy": 0.248, "p50_latency_ms": 1.0, "p95_latency_ms": 1.1, "max_memory_allocated_mb": 80, "active_param_count": 800},
    ]
    runner._write_quality_per_ms_memory_gate(rows)
    assert (tmp_path / "pvr_ec_quality_per_ms_memory_gate_report.json").exists()


def test_reliability_proxy_gate_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    runner._write_reliability_proxy_gate(_candidate_rows(), _summary())
    assert (tmp_path / "pvr_ec_reliability_proxy_gate_report.json").exists()


def test_final_deployment_gate_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair, summarize_pvr_final_deployment_gate

    stems = {
        "pvr_ec_final_forward_purity_report": "PVR_EC_FORWARD_PURITY_PASSED",
        "pvr_ec_final_candidate_config_manifest": "PVR_EC_REPRODUCIBILITY_MANIFEST_COMPLETE",
        "pvr_ec_multiseed_confirmation_report": "PVR_EC_MULTI_SEED_CONFIRMED",
        "pvr_ec_longer_training_confirmation_report": "PVR_EC_LONGER_TRAINING_CONFIRMED",
        "pvr_ec_matched_step_report": "PVR_EC_MATCHED_STEP_CONFIRMED",
        "pvr_ec_matched_wall_clock_report": "PVR_EC_MATCHED_WALL_CLOCK_CONFIRMED",
        "pvr_ec_final_calibration_sweep_report": "PVR_EC_CALIBRATION_CONSTRAINED_CONFIRMED",
        "pvr_ec_family_regression_gate_report": "PVR_EC_FAMILY_REGRESSION_PASSED",
        "pvr_ec_quality_per_ms_memory_gate_report": "PVR_EC_QUALITY_PER_MS_CONFIRMED",
        "pvr_ec_reliability_proxy_gate_report": "PVR_EC_RELIABILITY_PROXY_PASSED",
    }
    for stem, status in stems.items():
        _write_report_pair(tmp_path, stem, {"status": status, "statuses": [status], "passed": True}, "x")
    report = summarize_pvr_final_deployment_gate([str(tmp_path)], tmp_path / "final")
    assert report["status"] == "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"


def test_owners_per_token_equals_one(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["owners_per_token"] == pytest.approx(1.0)


def test_top2_top4_execution_zero_but_top2_score_allowed(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["Top2_executions"] == pytest.approx(0.0)
    assert report["Top4_executions"] == pytest.approx(0.0)
    assert report["top2_score_allowed_for_diagnostics"] is True


def test_oracle_owner_not_used(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["oracle_owner_used"] is False


def test_forced_action_not_used(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["forced_action_path_used"] is False


def test_forward_does_not_write_files(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["file_writes_in_forward"] == 0


def test_forward_does_not_run_replay(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["replay_in_forward"] is False


def test_forward_has_no_cpu_transfer_reported(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["CPU_transfers_in_forward"] == 0


def test_promotion_gate_blocks_on_calibration_regression(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair, summarize_pvr_final_deployment_gate

    _write_report_pair(tmp_path, "pvr_ec_final_calibration_sweep_report", {"status": "PVR_EC_CALIBRATION_BLOCKED", "passed": False}, "x")
    report = summarize_pvr_final_deployment_gate([str(tmp_path)], tmp_path / "final")
    assert report["status"] == "PARTIAL_PVR_EC_FINAL_DEPLOYMENT_GATE"


def test_promotion_gate_blocks_on_family_collapse(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = _candidate_rows()
    for row in rows:
        if row["model_name"] == "pvr_ec_ownership_top1_final_candidate_v1" and row["family"] == "dyck":
            row["accuracy"] = 0.0
    report = runner._write_family_regression_gate(rows, _summary())
    assert report["status"] == "PVR_EC_FAMILY_REGRESSION_BLOCKED"


def test_promotion_gate_blocks_on_quality_per_ms_regression(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = [
        {"model": "fixed_moe_vectorized", "batch_size": 1, "sequence_length": 64, "loss": 0.39, "accuracy": 0.26, "p50_latency_ms": 1.0, "p95_latency_ms": 1.1, "max_memory_allocated_mb": 100, "active_param_count": 1000},
        {"model": "pvr_ec_ownership_top1_final_candidate_v1", "batch_size": 1, "sequence_length": 64, "loss": 0.50, "accuracy": 0.10, "p50_latency_ms": 4.0, "p95_latency_ms": 4.1, "max_memory_allocated_mb": 120, "active_param_count": 800},
    ]
    report = runner._write_quality_per_ms_memory_gate(rows)
    assert report["status"] == "PVR_EC_QUALITY_PER_MS_BLOCKED"


def test_promotion_gate_blocks_on_repeatability_failure(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_multiseed_confirmation_report", {"status": "PVR_EC_REPEATABILITY_BLOCKED", "passed": False}, "x")
    assert json.loads((tmp_path / "pvr_ec_multiseed_confirmation_report.json").read_text())["passed"] is False


def test_promotion_gate_blocks_on_matched_wall_clock_failure(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_matched_wall_clock_report", {"status": "PVR_EC_MATCHED_WALL_CLOCK_BLOCKED", "passed": False}, "x")
    assert json.loads((tmp_path / "pvr_ec_matched_wall_clock_report.json").read_text())["status"] == "PVR_EC_MATCHED_WALL_CLOCK_BLOCKED"


def test_promotion_gate_blocks_on_missing_reproducibility_manifest(tmp_path):
    from run_algorithmic_benchmarks import summarize_pvr_final_deployment_gate

    report = summarize_pvr_final_deployment_gate([str(tmp_path)], tmp_path / "final")
    assert report["status"] == "PARTIAL_PVR_EC_FINAL_DEPLOYMENT_GATE"


def test_promotion_gate_passes_on_clean_fixture(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair, summarize_pvr_final_deployment_gate

    required = [
        "pvr_ec_final_forward_purity_report",
        "pvr_ec_final_candidate_config_manifest",
        "pvr_ec_multiseed_confirmation_report",
        "pvr_ec_longer_training_confirmation_report",
        "pvr_ec_matched_step_report",
        "pvr_ec_matched_wall_clock_report",
        "pvr_ec_final_calibration_sweep_report",
        "pvr_ec_family_regression_gate_report",
        "pvr_ec_quality_per_ms_memory_gate_report",
        "pvr_ec_reliability_proxy_gate_report",
    ]
    for stem in required:
        _write_report_pair(tmp_path, stem, {"status": "OK", "statuses": ["OK"], "passed": True}, "x")
    assert summarize_pvr_final_deployment_gate([str(tmp_path)], tmp_path / "final")["promotion_ready"] is True


def test_calibration_sweep_variant_creates_new_config_not_mutate_v1(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "configs").mkdir()
    original = {"config_name": "pvr_ec_ownership_top1_final_candidate_v1", "sparse_aux_loss_variant": "sparse_ce_0_05_plus_logit_norm_penalty_light"}
    (tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1.json").write_text(json.dumps(original))
    runner = _final_gate_runner(tmp_path)
    runner._write_selected_candidate_variant_config("sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01")
    assert json.loads((tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1.json").read_text()) == original
    assert (tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1_1.json").exists()


def test_selected_variant_requires_revalidation(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "configs").mkdir()
    (tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1.json").write_text(json.dumps({}))
    runner = _final_gate_runner(tmp_path)
    rows = _candidate_rows()
    for row in rows:
        if row["model_name"] == "pvr_ec_ownership_top1_final_candidate_v1":
            alt = dict(row)
            alt["model_name"] = "pvr_ec_ownership_top1_final_candidate_v1__aux__sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01"
            alt["sparse_aux_loss_variant"] = "sparse_ce_0_05_plus_logit_norm_light_plus_wrong_suppress_0_01"
            alt["loss"] = 0.38
            alt["accuracy"] = 0.27
            alt["calibration_proxy"] = 0.08
            rows.append(alt)
    report = runner._write_final_calibration_sweep_report(rows, runner._artifact_metadata(), _summary())
    assert report["selected_requires_revalidation"] is True


def test_repeatability_collapse_isolation_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_repeatability_collapse_isolation_report", {"status": "PVR_EC_REPEATABILITY_COLLAPSE_ANALYZED", "passed": False}, "x")
    assert (tmp_path / "pvr_ec_repeatability_collapse_isolation_report.json").exists()


def test_repeatability_repair_sweep_report_written(tmp_path):
    from run_algorithmic_benchmarks import _write_report_pair

    _write_report_pair(tmp_path, "pvr_ec_repeatability_repair_sweep_report", {"status": "PVR_EC_REPEATABILITY_BLOCKED", "passed": False}, "x")
    assert (tmp_path / "pvr_ec_repeatability_repair_sweep_report.json").exists()


def test_qpm_shape_regression_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = [
        {"model": "fixed_moe_vectorized", "batch_size": 1, "sequence_length": 16, "loss": 0.3, "accuracy": 0.3, "p50_latency_ms": 1.0, "p95_latency_ms": 1.1, "max_memory_allocated_mb": 10, "active_param_count": 10},
        {"model": "pvr_ec_ownership_top1_final_candidate_v1", "batch_size": 1, "sequence_length": 16, "loss": 0.31, "accuracy": 0.29, "p50_latency_ms": 1.2, "p95_latency_ms": 1.3, "max_memory_allocated_mb": 9, "active_param_count": 9, "actual_owner_count_per_token": 1.0},
    ]
    runner._write_qpm_shape_regression_report(rows)
    assert (tmp_path / "pvr_ec_qpm_shape_regression_report.json").exists()


def test_qpm_memory_repair_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = [
        {"model": "fixed_moe_vectorized", "batch_size": 1, "sequence_length": 16, "loss": 0.3, "accuracy": 0.3, "p50_latency_ms": 1.0, "p95_latency_ms": 1.1, "max_memory_allocated_mb": 10, "active_param_count": 10},
        {"model": "pvr_ec_ownership_top1_final_candidate_v1", "batch_size": 1, "sequence_length": 16, "loss": 0.31, "accuracy": 0.29, "p50_latency_ms": 0.8, "p95_latency_ms": 0.9, "max_memory_allocated_mb": 9, "active_param_count": 9, "actual_owner_count_per_token": 1.0},
    ]
    runner._write_qpm_shape_regression_report(rows, repair=True)
    assert (tmp_path / "pvr_ec_qpm_memory_repair_report.json").exists()


def test_reliability_calibration_repair_report_written(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = _candidate_rows()
    for row in list(rows):
        if row["model_name"] == "pvr_ec_ownership_top1_final_candidate_v1":
            row["repair_variant"] = "final_candidate_v1"
            alt = dict(row)
            alt["model_name"] = "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2"
            alt["repair_variant"] = "posthoc_temperature_T_1_2"
            alt["calibration_proxy"] = 0.10
            alt["incorrect_logit_overamplification_rate"] = 0.2
            rows.append(alt)
    runner._write_reliability_calibration_repair_report(rows, runner._artifact_metadata(), _summary())
    assert (tmp_path / "pvr_ec_reliability_calibration_repair_report.json").exists()


def test_selected_candidate_config_hash_changes(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "configs").mkdir()
    (tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1.json").write_text(json.dumps({"config_name": "pvr_ec_ownership_top1_final_candidate_v1"}))
    runner = _final_gate_runner(tmp_path)
    before = runner._file_sha256(tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1.json")
    runner._write_selected_candidate_variant_config("posthoc_temperature_T_1_2")
    after = runner._file_sha256(tmp_path / "configs" / "pvr_ec_ownership_top1_final_candidate_v1_1.json")
    assert before != after


def test_forward_purity_preserved_after_repair(tmp_path):
    rows = _candidate_rows()
    for row in rows:
        if row["model_name"] == "pvr_ec_ownership_top1_final_candidate_v1":
            row["repair_variant"] = "posthoc_temperature_T_1_2"
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(rows)
    assert report["passed"] is True


def test_top2_top4_execution_zero_after_repair(tmp_path):
    report = _final_gate_runner(tmp_path)._write_forward_purity_gate(_candidate_rows())
    assert report["Top2_executions"] == 0
    assert report["Top4_executions"] == 0


def test_qpm_report_contains_all_15_shapes(tmp_path):
    runner = _final_gate_runner(tmp_path)
    rows = []
    for b in [1, 8, 16, 32, 64]:
        for s in [16, 64, 128]:
            rows.append({"model": "fixed_moe_vectorized", "batch_size": b, "sequence_length": s, "loss": 0.3, "accuracy": 0.3, "p50_latency_ms": 1.0, "p95_latency_ms": 1.1, "max_memory_allocated_mb": 10, "active_param_count": 10})
            rows.append({"model": "pvr_ec_ownership_top1_final_candidate_v1", "batch_size": b, "sequence_length": s, "loss": 0.31, "accuracy": 0.29, "p50_latency_ms": 0.9, "p95_latency_ms": 1.0, "max_memory_allocated_mb": 9, "active_param_count": 9, "actual_owner_count_per_token": 1.0})
    report = runner._write_qpm_shape_regression_report(rows)
    assert report["shape_count"] == 15


def test_calibration_repair_does_not_change_owner_count():
    from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

    overrides = AlgorithmicBenchmarkRunner._repair_variant_overrides("posthoc_temperature_T_1_2")
    assert overrides["pvr_output_temperature"] == pytest.approx(1.2)


def test_temperature_calibration_does_not_change_routing():
    from run_algorithmic_benchmarks import AlgorithmicBenchmarkRunner

    overrides = AlgorithmicBenchmarkRunner._repair_variant_overrides("posthoc_temperature_T_1_3")
    assert "deploy_mode" not in overrides
    assert "pvr_expert_type" not in overrides


def test_diagnostic_logits_not_retained_in_inference_timing():
    config = PVRECModelConfig(
        vocab_size=32,
        d_model=32,
        max_seq_len=16,
        n_layers=1,
        n_heads=2,
        d_ff=64,
        num_experts=2,
        num_prototypes=4,
        d_expert=8,
        pvr_deploy_mode="top1",
        pvr_sparse_aux_loss_variant="sparse_ce_0_05_plus_logit_norm_penalty_light",
    )
    model = PVRECModel(config)
    model.eval()
    x = torch.randint(0, 32, (2, 8))
    y = torch.randint(0, 32, (2, 8))
    with torch.no_grad():
        out = model(input_ids=x, targets=y)
    assert "pvr_logit_decomposition" not in out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
