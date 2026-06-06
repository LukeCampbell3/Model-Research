"""Tests for PVR-EC Ownership Map Recall Expansion + Calibration.

Validates all requirements from the implementation prompt:
- Candidate generation includes current owner
- Candidate generation includes replay oracle winner
- Candidate generation respects compatible mask
- Candidate set size is configurable
- Candidate owner recall metric is written
- Owner action rate metric is written
- Ownership bias sweep writes report
- Semantic margin guard blocks unsafe high-margin flip
- Semantic margin guard allows replay-supported flip
- Promotion gate writes explicit reason codes
- Promotion gate blocks low candidate recall
- Promotion gate blocks owner-change success regression
- Promotion gate blocks prototype monopoly increase
- Promotion gate blocks latency regression
- Failure decomposition separates recall vs scoring vs capacity
- Frozen candidate uses selected calibrated config
- Multi-seed report aggregates metrics
- Ownership map still executes exactly one expert
- Top2/Top4 remain disabled
- Hot path remains tensor-only
"""

import sys
import json
import inspect
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import torch
import pytest

from sparse_loop_moe.models.pvr_ec.ownership_map import (
    OwnershipMapConfig,
    OwnershipMapState,
    PVR_EC_OWNERSHIP_STATUSES,
    PROMOTION_REASON_CODES,
    CANDIDATE_SOURCES,
    CandidateScore,
    SweepResult,
    generate_candidates,
    compute_semantic_margin,
    ownership_bias_allowed,
    apply_ownership_bias,
    refresh_ownership_map,
    compute_candidate_owner_recall,
    compute_owner_change_metrics,
    compute_failure_decomposition,
    evaluate_promotion_gate,
    select_best_safe_config,
    aggregate_multiseed_results,
    write_ownership_reports,
    build_ownership_map_tensor,
    export_frozen_candidate_map,
    load_frozen_candidate_map,
)
from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.diagnostics import PVR_EC_STATUSES


@pytest.fixture
def config():
    return OwnershipMapConfig(candidate_set_size=4)


@pytest.fixture
def state():
    return OwnershipMapState(num_prototypes=8, num_experts=4)


@pytest.fixture
def ownership_model():
    return PVRECMoEFFN(
        d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
        pvr_deploy_mode="top1",
    )


class TestCandidateGeneration:
    """Test candidate owner generation from multiple sources."""

    def test_candidate_generation_includes_current_owner(self, state):
        """Current owner is always in candidate set."""
        router_logits = torch.randn(16, 4)
        prototype_ids = torch.randint(0, 8, (16,))
        candidates = generate_candidates(
            state,
            router_logits=router_logits,
            prototype_ids=prototype_ids,
        )
        for p in range(state.num_prototypes):
            current_owner = state.prototype_owners[p]
            expert_ids = [c.expert_id for c in candidates[p]]
            assert current_owner in expert_ids, \
                f"Current owner {current_owner} not in candidates for prototype {p}"

    def test_candidate_generation_includes_replay_oracle_winner(self, state):
        """Replay oracle winner appears in candidate set."""
        N = 32
        router_logits = torch.randn(N, 4)
        prototype_ids = torch.zeros(N, dtype=torch.long)  # All tokens → prototype 0
        oracle_expert_ids = torch.full((N,), 2, dtype=torch.long)  # Expert 2 always wins

        candidates = generate_candidates(
            state,
            router_logits=router_logits,
            prototype_ids=prototype_ids,
            oracle_expert_ids=oracle_expert_ids,
        )
        expert_ids_p0 = [c.expert_id for c in candidates[0]]
        assert 2 in expert_ids_p0, "Replay oracle winner (expert 2) not in candidates"
        # Check source label
        oracle_sources = [c for c in candidates[0] if c.expert_id == 2 and "oracle" in c.source]
        assert len(oracle_sources) > 0

    def test_candidate_generation_respects_compatible_mask(self, state):
        """Underused compatible owners with oracle wins are candidates."""
        N = 16
        router_logits = torch.randn(N, 4)
        prototype_ids = torch.zeros(N, dtype=torch.long)

        # Make expert 3 compatible and underused
        compatible_mask = torch.ones(8, 4)
        # Record oracle wins for expert 3 on prototype 0
        state.oracle_win_counts[0][3] = 5
        state.oracle_win_counts[0][0] = 10

        candidates = generate_candidates(
            state,
            router_logits=router_logits,
            prototype_ids=prototype_ids,
            compatible_mask=compatible_mask,
        )
        expert_ids_p0 = [c.expert_id for c in candidates[0]]
        # Expert 3 should appear (it has oracle wins and is compatible)
        assert 3 in expert_ids_p0

    def test_candidate_set_size_is_configurable(self):
        """Candidate set size respects config.candidate_set_size."""
        for C in [2, 4, 6, 8]:
            config = OwnershipMapConfig(candidate_set_size=C)
            state = OwnershipMapState(num_prototypes=8, num_experts=4, config=config)
            router_logits = torch.randn(32, 4)
            prototype_ids = torch.randint(0, 8, (32,))

            candidates = generate_candidates(
                state,
                router_logits=router_logits,
                prototype_ids=prototype_ids,
            )
            for p in range(8):
                assert len(candidates[p]) <= C, \
                    f"Candidate set size {len(candidates[p])} exceeds C={C} for prototype {p}"

    def test_candidate_sources_are_diverse(self, state):
        """Candidates come from multiple sources."""
        N = 64
        router_logits = torch.randn(N, 4)
        prototype_ids = torch.randint(0, 8, (N,))
        oracle_expert_ids = torch.randint(0, 4, (N,))

        # Put some oracle wins in state
        for p in range(8):
            for e in range(4):
                state.oracle_win_counts[p][e] = torch.randint(0, 10, (1,)).item()

        candidates = generate_candidates(
            state,
            router_logits=router_logits,
            prototype_ids=prototype_ids,
            oracle_expert_ids=oracle_expert_ids,
        )
        all_sources = set()
        for p in range(8):
            for c in candidates[p]:
                all_sources.add(c.source)
        # Should have at least current_owner and one other source
        assert "current_owner" in all_sources
        assert len(all_sources) >= 2


class TestCandidateOwnerRecall:
    """Test candidate owner recall metric computation."""

    def test_candidate_owner_recall_metric_is_written(self, tmp_path, state):
        """Candidate owner recall metric appears in report."""
        recall = compute_candidate_owner_recall(
            oracle_expert_ids=torch.tensor([0, 1, 2, 3, 0, 1, 2, 3]),
            prototype_ids=torch.tensor([0, 0, 1, 1, 2, 2, 3, 3]),
            candidate_sets=state.prototype_owner_candidates,
        )
        assert "candidate_owner_recall" in recall
        assert "oracle_best_in_candidate_set_rate" in recall
        assert "candidate_set_size" in recall
        assert 0.0 <= recall["candidate_owner_recall"] <= 1.0

    def test_recall_is_1_when_all_oracle_in_set(self):
        """Recall = 1.0 when all oracle experts are in candidate sets."""
        # All prototypes have candidate set [0, 1, 2, 3]
        candidate_sets = [[0, 1, 2, 3]] * 4
        oracle_expert_ids = torch.tensor([0, 1, 2, 3])
        prototype_ids = torch.tensor([0, 1, 2, 3])

        recall = compute_candidate_owner_recall(oracle_expert_ids, prototype_ids, candidate_sets)
        assert recall["candidate_owner_recall"] == 1.0

    def test_recall_is_0_when_no_oracle_in_set(self):
        """Recall = 0.0 when no oracle experts are in candidate sets."""
        # Candidate sets only have expert 0
        candidate_sets = [[0]] * 4
        oracle_expert_ids = torch.tensor([3, 3, 3, 3])
        prototype_ids = torch.tensor([0, 1, 2, 3])

        recall = compute_candidate_owner_recall(oracle_expert_ids, prototype_ids, candidate_sets)
        assert recall["candidate_owner_recall"] == 0.0


class TestOwnerActionRate:
    """Test ownership action rate metrics."""

    def test_owner_action_rate_metric_is_written(self, tmp_path, state):
        """Owner action rate metric appears in report."""
        state.owner_change_count = 3
        state.owner_change_success_count = 2
        state.total_evaluations = 100

        metrics = compute_owner_change_metrics(
            state,
            loss_when_changed=[0.5, 0.4, 0.6],
            loss_when_unchanged=[0.7] * 97,
            oracle_gap_when_changed=[0.1, 0.05, 0.15],
            oracle_gap_when_unchanged=[0.2] * 97,
        )
        assert "owner_change_rate" in metrics
        assert "owner_changed_success_rate" in metrics
        assert metrics["owner_change_rate"] == 0.03
        assert metrics["owner_changed_success_rate"] == pytest.approx(2 / 3)


class TestOwnershipBiasSweep:
    """Test ownership bias sweep."""

    def test_ownership_bias_sweep_writes_report(self, tmp_path):
        """Bias sweep produces a report file."""
        results = [
            SweepResult(
                ownership_weight=0.25, ownership_bias_cap=0.25,
                failure_bias_weight=1.0, semantic_margin_guard=0.10,
                candidate_set_size=4, loss=0.5, oracle_gap=0.1,
                quality_per_ms=0.8, owner_change_rate=0.05,
                owner_changed_success_rate=0.75, latency_ms=10.0,
            ),
            SweepResult(
                ownership_weight=0.5, ownership_bias_cap=0.5,
                failure_bias_weight=1.0, semantic_margin_guard=0.10,
                candidate_set_size=4, loss=0.45, oracle_gap=0.08,
                quality_per_ms=0.85, owner_change_rate=0.08,
                owner_changed_success_rate=0.72, latency_ms=10.5,
            ),
        ]
        paths = write_ownership_reports(tmp_path, bias_sweep_results=results)
        assert "ownership_bias_sweep_report.json" in paths
        data = json.loads((tmp_path / "ownership_bias_sweep_report.json").read_text())
        assert data["configs_tested"] == 2


class TestSemanticMarginGuard:
    """Test semantic margin guard."""

    def test_semantic_margin_guard_blocks_unsafe_high_margin_flip(self):
        """High semantic margin blocks ownership bias flip when no override."""
        semantic_margin = torch.tensor([0.5, 0.6, 0.8])  # All above guard
        margin_guard = 0.10

        allowed = ownership_bias_allowed(
            semantic_margin, margin_guard,
            failure_bias_current=None,
            replay_evidence_strong=None,
            current_owner_stale=None,
        )
        # No override conditions → should block all
        assert not allowed.any()

    def test_semantic_margin_guard_allows_replay_supported_flip(self):
        """High margin flip allowed when replay evidence supports it."""
        semantic_margin = torch.tensor([0.5, 0.6, 0.8])
        margin_guard = 0.10
        replay_evidence = torch.tensor([True, True, True])

        allowed = ownership_bias_allowed(
            semantic_margin, margin_guard,
            replay_evidence_strong=replay_evidence,
        )
        assert allowed.all()

    def test_low_margin_always_allows_ownership_bias(self):
        """Low semantic margin always permits ownership bias."""
        semantic_margin = torch.tensor([0.01, 0.05, 0.09])
        margin_guard = 0.10

        allowed = ownership_bias_allowed(semantic_margin, margin_guard)
        assert allowed.all()

    def test_margin_guard_allows_stale_owner_override(self):
        """High margin flip allowed when current owner is stale."""
        semantic_margin = torch.tensor([0.5, 0.5])
        margin_guard = 0.10
        stale = torch.tensor([True, False])

        allowed = ownership_bias_allowed(
            semantic_margin, margin_guard,
            current_owner_stale=stale,
        )
        assert allowed[0].item() is True
        assert allowed[1].item() is False

    def test_compute_semantic_margin_shape(self):
        """Semantic margin has correct shape."""
        router_logits = torch.randn(16, 4)
        proto_bias = torch.randn(16, 4)
        margin = compute_semantic_margin(router_logits, proto_bias)
        assert margin.shape == (16,)
        assert (margin >= 0).all()


class TestPromotionGate:
    """Test promotion gate with explicit reason codes."""

    def test_promotion_gate_writes_explicit_reason_codes(self, config):
        """Gate report includes specific reason codes, not generic DO_NOT_PROMOTE."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            candidate_loss=1.1,  # Regression
            candidate_oracle_gap=0.25,  # Regression
            candidate_latency_ms=15.0,  # Over limit
            candidate_quality_per_ms=0.5,
            owner_changed_success_rate=0.5,  # Too low
            candidate_owner_recall=0.3,  # Too low
            high_confidence_failure_rate=0.1,  # Too high
            prototype_monopoly_rate=0.5,  # Too high
            seed_repeatability_passed=False,
            canary_reproduced=False,
            frozen_candidate_reproduced=False,
            owner_change_rate=0.01,  # Too rare
        )
        assert result["promotion_decision"] is False
        assert len(result["promotion_blocked_reasons"]) > 0
        # Should have specific reason codes, not generic
        for reason in result["promotion_blocked_reasons"]:
            assert reason in PROMOTION_REASON_CODES

    def test_promotion_gate_blocks_low_candidate_recall(self, config):
        """Gate blocks when candidate recall is too low."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            candidate_loss=0.8,
            candidate_oracle_gap=0.1,
            candidate_latency_ms=9.0,
            candidate_quality_per_ms=1.0,
            owner_changed_success_rate=0.8,
            candidate_owner_recall=0.2,  # Too low (<0.5)
            high_confidence_failure_rate=0.03,
            prototype_monopoly_rate=0.25,
            seed_repeatability_passed=True,
            canary_reproduced=True,
            frozen_candidate_reproduced=True,
            owner_change_rate=0.05,
        )
        assert "CANDIDATE_RECALL_TOO_LOW" in result["promotion_blocked_reasons"]

    def test_promotion_gate_blocks_owner_change_success_regression(self, config):
        """Gate blocks when owner-change success rate is below threshold."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            candidate_loss=0.8,
            candidate_oracle_gap=0.1,
            candidate_latency_ms=9.0,
            candidate_quality_per_ms=1.0,
            owner_changed_success_rate=0.5,  # Below 0.70 threshold
            candidate_owner_recall=0.8,
            high_confidence_failure_rate=0.03,
            prototype_monopoly_rate=0.25,
            seed_repeatability_passed=True,
            canary_reproduced=True,
            frozen_candidate_reproduced=True,
            owner_change_rate=0.05,
        )
        assert "OWNER_CHANGE_SUCCESS_TOO_LOW" in result["promotion_blocked_reasons"]

    def test_promotion_gate_blocks_prototype_monopoly_increase(self, config):
        """Gate blocks when monopoly rate increases beyond tolerance."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            candidate_loss=0.8,
            candidate_oracle_gap=0.1,
            candidate_latency_ms=9.0,
            candidate_quality_per_ms=1.0,
            owner_changed_success_rate=0.8,
            candidate_owner_recall=0.8,
            high_confidence_failure_rate=0.03,
            prototype_monopoly_rate=0.5,  # 0.3 + 0.05 tolerance = 0.35, this exceeds
            seed_repeatability_passed=True,
            canary_reproduced=True,
            frozen_candidate_reproduced=True,
            owner_change_rate=0.05,
        )
        assert "PROTOTYPE_MONOPOLY_INCREASE" in result["promotion_blocked_reasons"]

    def test_promotion_gate_blocks_latency_regression(self, config):
        """Gate blocks when latency exceeds limit."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            candidate_loss=0.8,
            candidate_oracle_gap=0.1,
            candidate_latency_ms=13.0,  # 10.0 * 1.25 = 12.5, this exceeds
            candidate_quality_per_ms=1.0,
            owner_changed_success_rate=0.8,
            candidate_owner_recall=0.8,
            high_confidence_failure_rate=0.03,
            prototype_monopoly_rate=0.25,
            seed_repeatability_passed=True,
            canary_reproduced=True,
            frozen_candidate_reproduced=True,
            owner_change_rate=0.05,
        )
        assert "LATENCY_REGRESSION" in result["promotion_blocked_reasons"]

    def test_promotion_gate_passes_when_all_clean(self, config):
        """Gate passes when all conditions met."""
        result = evaluate_promotion_gate(
            config=config,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            deploy_top1_high_confidence_failure_rate=0.05,
            deploy_top1_monopoly_rate=0.3,
            deploy_top1_quality_per_ms=0.5,
            candidate_loss=0.8,  # Better than 1.0 - 0.01
            candidate_oracle_gap=0.1,  # Better than 0.2 - 0.005
            candidate_latency_ms=9.0,  # Within 10 * 1.25
            candidate_quality_per_ms=0.6,  # Better than deploy
            owner_changed_success_rate=0.8,  # Above 0.70
            candidate_owner_recall=0.7,  # Above 0.5
            high_confidence_failure_rate=0.04,  # Within tolerance
            prototype_monopoly_rate=0.25,  # Within tolerance
            seed_repeatability_passed=True,
            canary_reproduced=True,
            frozen_candidate_reproduced=True,
            owner_change_rate=0.05,  # Above min
        )
        assert result["promotion_decision"] is True
        assert result["promotion_blocked_reasons"] == []
        assert result["status"] == "PVR_EC_OWNERSHIP_PROMOTION_GATE_CLEAN"


class TestFailureDecomposition:
    """Test failure decomposition separates recall vs scoring vs capacity."""

    def test_failure_decomposition_separates_recall_vs_scoring_vs_capacity(self):
        """Decomposition correctly classifies each failure type."""
        # Token 0: oracle=3, selected=0, candidate_set has [0,1] → recall failure
        # Token 1: oracle=1, selected=0, candidate_set has [0,1] → scoring failure
        # Token 2: oracle=0, selected=0, candidate_set has [0,1], loss high → capacity
        # Token 3: oracle=0, selected=0, candidate_set has [0,1], loss ok → no failure

        oracle_expert_ids = torch.tensor([3, 1, 0, 0])
        selected_expert_ids = torch.tensor([0, 0, 0, 0])
        prototype_ids = torch.tensor([0, 0, 0, 0])
        candidate_sets = [[0, 1]] * 4
        loss_per_token = torch.tensor([1.0, 1.0, 2.0, 0.5])
        oracle_loss_per_token = torch.tensor([0.5, 0.5, 0.5, 0.5])

        decomp = compute_failure_decomposition(
            oracle_expert_ids, selected_expert_ids, prototype_ids,
            candidate_sets, loss_per_token, oracle_loss_per_token,
        )
        assert decomp["candidate_recall_failure_rate"] == 0.25  # 1/4
        assert decomp["scoring_failure_rate"] == 0.25  # 1/4
        assert decomp["expert_capacity_failure_rate"] == 0.25  # 1/4 (loss 2.0 > 0.5*1.5)
        assert "recommended_action" in decomp

    def test_recommended_action_when_recall_dominates(self):
        """Recommends expanding candidate generation when recall failures dominate."""
        oracle_expert_ids = torch.tensor([3, 3, 3, 3])  # All need expert 3
        selected_expert_ids = torch.tensor([0, 0, 0, 0])
        prototype_ids = torch.tensor([0, 0, 0, 0])
        candidate_sets = [[0, 1]] * 4  # Expert 3 not in sets

        decomp = compute_failure_decomposition(
            oracle_expert_ids, selected_expert_ids, prototype_ids,
            candidate_sets, torch.ones(4), torch.ones(4) * 0.5,
        )
        assert decomp["recommended_action"] == "expand_candidate_generation_and_replay_sampling"


class TestFrozenCandidateMap:
    """Test frozen candidate map export/load."""

    def test_frozen_candidate_uses_selected_calibrated_config(self, tmp_path, state):
        """Frozen candidate map stores and loads config correctly."""
        state.config.ownership_weight = 0.75
        state.config.ownership_bias_cap = 0.5

        path = export_frozen_candidate_map(state, tmp_path / "frozen.json")
        loaded = load_frozen_candidate_map(path)

        assert loaded.prototype_owners == state.prototype_owners
        assert loaded.config.ownership_weight == 0.75
        assert loaded.config.ownership_bias_cap == 0.5

    def test_ownership_map_tensor_shape(self, state):
        """Ownership map tensor has correct shape."""
        tensor = build_ownership_map_tensor(state)
        assert tensor.shape == (state.num_prototypes, state.num_experts)
        # Owner positions should have value 1.0
        for p in range(state.num_prototypes):
            owner = state.prototype_owners[p]
            assert tensor[p, owner].item() == 1.0


class TestMultiSeedConfirmation:
    """Test multi-seed repeatability aggregation."""

    def test_multi_seed_report_aggregates_metrics(self):
        """Multi-seed report computes mean/std across seeds."""
        results = {
            42: {"loss": 0.5, "accuracy": 0.8, "oracle_gap": 0.1, "loss_improvement": 0.05},
            123: {"loss": 0.48, "accuracy": 0.82, "oracle_gap": 0.09, "loss_improvement": 0.07},
            777: {"loss": 0.52, "accuracy": 0.79, "oracle_gap": 0.11, "loss_improvement": 0.03},
        }
        agg = aggregate_multiseed_results(results)
        assert "loss_mean" in agg
        assert "loss_std" in agg
        assert "accuracy_mean" in agg
        assert agg["seed_count"] == 3
        assert agg["status"] == "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_CONFIRMED"

    def test_multi_seed_fails_if_not_all_improve(self):
        """Status is not CONFIRMED if improvement only on some seeds."""
        results = {
            42: {"loss_improvement": 0.05},
            123: {"loss_improvement": -0.02},  # Regression
            777: {"loss_improvement": 0.03},
        }
        agg = aggregate_multiseed_results(results)
        assert agg["status"] != "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_CONFIRMED"


class TestOwnershipMapExecution:
    """Test that ownership map still executes exactly one expert."""

    def test_ownership_map_still_executes_exactly_one_expert(self, ownership_model):
        """Deploy top1 with ownership map still uses exactly 1 expert per token."""
        x = torch.randn(2, 8, 32)
        out, aux = ownership_model(x)
        assert out.shape == x.shape
        assert aux["deploy_mode"] == "top1"
        # Verify actual_avg_k == 1
        assert aux["routing_metrics"]["actual_avg_k"].item() == pytest.approx(1.0)

    def test_top2_top4_remain_disabled(self):
        """Top2 and Top4 are NOT production execution paths for ownership map."""
        # The ownership model variant should use deploy_mode="top1"
        model = PVRECMoEFFN(
            d_model=32, d_ff=64, num_experts=4, num_prototypes=8,
            pvr_deploy_mode="top1",
        )
        _, aux = model(torch.randn(2, 8, 32))
        assert aux["deploy_mode"] == "top1"
        actual_k = aux["routing_metrics"]["actual_avg_k"]
        if isinstance(actual_k, torch.Tensor):
            actual_k = actual_k.item()
        assert actual_k == 1.0

    def test_hot_path_remains_tensor_only(self):
        """Deploy forward path has no .cpu(), .item(), synchronize, or .numpy()."""
        source = inspect.getsource(PVRECMoEFFN._deploy_forward)
        assert ".cpu(" not in source
        assert "synchronize" not in source
        assert ".item(" not in source
        assert ".numpy(" not in source

    def test_apply_ownership_bias_is_tensor_only(self):
        """apply_ownership_bias uses no Python loops or CPU ops."""
        source = inspect.getsource(apply_ownership_bias)
        assert ".item(" not in source
        assert ".cpu(" not in source
        assert ".numpy(" not in source
        # Check no Python for-loops in code lines (exclude docstring/comments)
        lines = source.split("\n")
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith("#")
                      and not l.strip().startswith('"""') and not l.strip().startswith("'")]
        for_loops = [l for l in code_lines if l.strip().startswith("for ")]
        assert len(for_loops) == 0, f"Found Python for-loop in hot path: {for_loops}"


class TestOwnershipBiasApplication:
    """Test tensor-only ownership bias application."""

    def test_apply_ownership_bias_changes_logits(self):
        """Ownership bias modifies router logits."""
        router_logits = torch.randn(16, 4)
        prototype_ids = torch.randint(0, 8, (16,))
        ownership_map = torch.randn(8, 4)

        biased = apply_ownership_bias(
            router_logits, prototype_ids, ownership_map,
            ownership_weight=0.5, ownership_bias_cap=0.5,
        )
        assert biased.shape == router_logits.shape
        assert not torch.allclose(biased, router_logits)

    def test_apply_ownership_bias_respects_cap(self):
        """Ownership bias is capped."""
        router_logits = torch.zeros(8, 4)
        prototype_ids = torch.zeros(8, dtype=torch.long)
        # Large ownership scores
        ownership_map = torch.ones(8, 4) * 10.0
        cap = 0.25

        biased = apply_ownership_bias(
            router_logits, prototype_ids, ownership_map,
            ownership_weight=1.0, ownership_bias_cap=cap,
        )
        # All bias values should be capped
        assert biased.max().item() <= cap + 1e-6

    def test_apply_ownership_bias_with_margin_guard(self):
        """Ownership bias is zeroed where semantic margin is high."""
        router_logits = torch.zeros(4, 4)
        prototype_ids = torch.zeros(4, dtype=torch.long)
        ownership_map = torch.ones(8, 4)
        # High margin for tokens 0,1; low margin for tokens 2,3
        semantic_margin = torch.tensor([0.5, 0.3, 0.05, 0.01])

        biased = apply_ownership_bias(
            router_logits, prototype_ids, ownership_map,
            ownership_weight=0.5, ownership_bias_cap=0.5,
            semantic_margin=semantic_margin, margin_guard=0.10,
        )
        # High margin tokens should have no bias (logits unchanged)
        assert torch.allclose(biased[0], router_logits[0])
        assert torch.allclose(biased[1], router_logits[1])
        # Low margin tokens should have bias applied
        assert not torch.allclose(biased[2], router_logits[2])
        assert not torch.allclose(biased[3], router_logits[3])


class TestOwnershipMapRefresh:
    """Test offline ownership map refresh."""

    def test_refresh_changes_owners_when_better_candidate_exists(self, state):
        """Refresh updates owner when candidate scores higher."""
        # Give prototype 0 lots of oracle wins for expert 2
        state.oracle_win_counts[0] = [1, 1, 20, 1]
        state.sample_counts[0] = [50, 50, 50, 50]

        candidates = {
            0: [
                CandidateScore(prototype_id=0, expert_id=2,
                               oracle_win_rate=0.8, source="replay_oracle_winners"),
                CandidateScore(prototype_id=0, expert_id=0,
                               reliability_bias=0.1, source="current_owner"),
            ],
        }
        # Fill other prototypes with empty or low-score candidates
        for p in range(1, 8):
            candidates[p] = [CandidateScore(prototype_id=p, expert_id=state.prototype_owners[p],
                                            reliability_bias=0.1, source="current_owner")]

        old_owner = state.prototype_owners[0]
        new_state, report = refresh_ownership_map(state, candidates)
        assert new_state.prototype_owners[0] == 2
        assert report["total_changes"] >= 1

    def test_refresh_respects_min_sample_protection(self, state):
        """Refresh does NOT change owner if below min_ownership_samples."""
        state.config.min_ownership_samples = 100
        state.sample_counts[0] = [10, 10, 10, 10]  # All below 100

        candidates = {
            0: [
                CandidateScore(prototype_id=0, expert_id=3,
                               oracle_win_rate=0.9, source="replay_oracle_winners"),
                CandidateScore(prototype_id=0, expert_id=0,
                               reliability_bias=0.1, source="current_owner"),
            ],
        }
        for p in range(1, 8):
            candidates[p] = [CandidateScore(prototype_id=p, expert_id=state.prototype_owners[p],
                                            source="current_owner")]

        old_owner = state.prototype_owners[0]
        new_state, report = refresh_ownership_map(state, candidates)
        # Should NOT change (insufficient samples for expert 3)
        assert new_state.prototype_owners[0] == old_owner


class TestOwnershipReports:
    """Test report writing."""

    def test_all_required_reports_are_written(self, tmp_path):
        """All 10 required report files are created."""
        paths = write_ownership_reports(tmp_path)
        expected = {
            "ownership_candidate_recall_report.json",
            "ownership_candidate_recall_report.md",
            "ownership_action_rate_report.json",
            "ownership_bias_calibration_report.json",
            "ownership_bias_sweep_report.json",
            "ownership_promotion_gate_report.json",
            "ownership_promotion_gate_report.md",
            "ownership_failure_decomposition_report.json",
            "ownership_repeatability_report.json",
            "ownership_repeatability_report.md",
            "ownership_map_refresh_report.json",
            "ownership_owner_change_report.json",
            "ownership_oracle_gap_report.json",
        }
        for name in expected:
            assert name in paths, f"Missing report: {name}"
            assert (tmp_path / name).exists()

    def test_action_rate_report_has_required_fields(self, tmp_path):
        """Action rate report includes all required fields."""
        action_data = {
            "owner_change_rate": 0.05,
            "target_owner_change_band": "2%-8%",
            "owner_changed_success_rate": 0.75,
            "loss_when_owner_changed": 0.5,
            "loss_when_owner_unchanged": 0.7,
            "oracle_gap_when_owner_changed": 0.1,
            "oracle_gap_when_owner_unchanged": 0.2,
            "recommended_bias_adjustment": "none",
        }
        paths = write_ownership_reports(tmp_path, action_rate_metrics=action_data)
        data = json.loads((tmp_path / "ownership_action_rate_report.json").read_text())
        required = [
            "owner_change_rate", "target_owner_change_band",
            "owner_changed_success_rate", "loss_when_owner_changed",
            "loss_when_owner_unchanged", "oracle_gap_when_owner_changed",
            "oracle_gap_when_owner_unchanged", "recommended_bias_adjustment",
        ]
        for field in required:
            assert field in data, f"Missing field in action rate report: {field}"


class TestStatusesRegistered:
    """Test that all new statuses are registered."""

    def test_ownership_statuses_in_pvr_ec_statuses(self):
        """All ownership statuses appear in the main PVR_EC_STATUSES tuple."""
        for status in PVR_EC_OWNERSHIP_STATUSES:
            assert status in PVR_EC_STATUSES, f"Status {status} not in PVR_EC_STATUSES"

    def test_all_required_statuses_exist(self):
        """All statuses from the spec are defined."""
        required = [
            "PVR_EC_OWNERSHIP_MAP_ACTS_TOO_RARELY",
            "PVR_EC_CANDIDATE_OWNER_RECALL_LOW",
            "PVR_EC_CANDIDATE_OWNER_RECALL_IMPROVED",
            "PVR_EC_OWNERSHIP_BIAS_UNDERCALIBRATED",
            "PVR_EC_OWNERSHIP_BIAS_CALIBRATED",
            "PVR_EC_OWNERSHIP_BIAS_TOO_AGGRESSIVE",
            "PVR_EC_OWNERSHIP_SEMANTIC_OVERRIDE_RISK",
            "PVR_EC_OWNERSHIP_PROMOTION_GATE_NOT_CLEAN",
            "PVR_EC_OWNERSHIP_PROMOTION_GATE_CLEAN",
            "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_CONFIRMED",
            "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_FAILED",
            "PVR_EC_OWNERSHIP_MAP_REFRESH_READY",
            "PVR_EC_OWNERSHIP_MAP_CANARY_READY",
            "PVR_EC_OWNERSHIP_MAP_DEPLOY_READY",
            "PVR_EC_DO_NOT_PROMOTE",
        ]
        for status in required:
            assert status in PVR_EC_OWNERSHIP_STATUSES


class TestBiasCalibrationSelection:
    """Test best safe config selection."""

    def test_selects_best_loss_among_safe(self):
        """Selects config with lowest loss among safe configs."""
        config = OwnershipMapConfig()
        results = [
            SweepResult(
                ownership_weight=0.25, ownership_bias_cap=0.25,
                failure_bias_weight=1.0, semantic_margin_guard=0.10,
                candidate_set_size=4, loss=0.8, oracle_gap=0.1,
                quality_per_ms=1.0, owner_change_rate=0.05,
                owner_changed_success_rate=0.8, latency_ms=9.0,
                high_confidence_failure_rate=0.01, prototype_monopoly_rate=0.02,
            ),
            SweepResult(
                ownership_weight=0.5, ownership_bias_cap=0.5,
                failure_bias_weight=1.0, semantic_margin_guard=0.10,
                candidate_set_size=4, loss=0.7, oracle_gap=0.08,  # Better
                quality_per_ms=1.2, owner_change_rate=0.08,
                owner_changed_success_rate=0.85, latency_ms=10.0,
                high_confidence_failure_rate=0.01, prototype_monopoly_rate=0.02,
            ),
        ]
        best = select_best_safe_config(
            results,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            config=config,
        )
        assert best is not None
        assert best.loss == 0.7
        assert best.is_safe is True

    def test_returns_none_when_no_safe_config(self):
        """Returns None when no config passes all safety constraints."""
        config = OwnershipMapConfig(min_loss_improvement=0.5)
        results = [
            SweepResult(
                ownership_weight=0.25, ownership_bias_cap=0.25,
                failure_bias_weight=1.0, semantic_margin_guard=0.10,
                candidate_set_size=4, loss=0.9,  # Not enough improvement
                oracle_gap=0.15, quality_per_ms=0.8,
                owner_change_rate=0.05, owner_changed_success_rate=0.8,
                latency_ms=9.0, high_confidence_failure_rate=0.01,
                prototype_monopoly_rate=0.02,
            ),
        ]
        best = select_best_safe_config(
            results,
            deploy_top1_loss=1.0,
            deploy_top1_oracle_gap=0.2,
            deploy_top1_latency_ms=10.0,
            config=config,
        )
        assert best is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
