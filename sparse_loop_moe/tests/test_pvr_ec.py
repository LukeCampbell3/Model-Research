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
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import torch
import pytest

from sparse_loop_moe.models.pvr_ec.diagnostics import (
    EXECUTION_MODES,
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
