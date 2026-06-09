"""Robust tests for PVR-EC Family Preservation Observatory.

Tests actual training behavior, metrics correctness, gate logic, and
failure mode classification. Not shape-checking — real verification.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "evaluation"))

import torch
import torch.nn.functional as F
import pytest
import numpy as np

from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.pvr_ec_router import PVRECRouter, PVRECConfig
from sparse_loop_moe.models.pvr_ec.family_preservation import (
    FAMILY_PRESERVATION_FAILURE_MODES,
    FAMILY_PRESERVATION_VERDICTS,
    NLP_STAGE1_VERDICTS,
    FamilyMembership,
    FamilyPreservationBiasConfig,
    OwnerChurnState,
    ShadowFamilyPreservationBias,
    compute_family_membership,
    compute_family_metrics,
    compute_family_oracle_gap,
    compute_family_preservation_score,
    family_preservation_gate,
)
from sparse_loop_moe.models.pvr_ec.failure_registry import (
    FAILURE_MODE_IDS,
    failure_mode_registry,
)


# =============================================================================
# Family Membership Computation
# =============================================================================


class TestFamilyMembershipComputation:
    """Verify soft family membership is computed correctly from prototype distances."""

    def test_membership_sums_to_one(self):
        """Soft membership must sum to 1 across prototypes (valid distribution)."""
        embeddings = torch.randn(32, 64)
        prototypes = torch.randn(8, 64)
        fm = compute_family_membership(embeddings, prototypes)
        sums = fm.soft_membership.sum(dim=-1)
        assert torch.allclose(sums, torch.ones_like(sums), atol=1e-5), \
            f"Membership doesn't sum to 1: {sums}"

    def test_membership_is_peaked_near_closest_prototype(self):
        """States near a prototype should have high membership in that prototype."""
        prototypes = torch.eye(4, 64)  # 4 prototypes in 64-dim, orthogonal
        # State very close to prototype 0
        embeddings = prototypes[0:1] + 0.01 * torch.randn(1, 64)
        fm = compute_family_membership(embeddings, prototypes, temperature=0.5)
        assert fm.soft_membership[0, 0] > 0.8, \
            f"State near proto 0 should have high membership: {fm.soft_membership[0]}"

    def test_boundary_detection_works(self):
        """States equidistant from two prototypes should be flagged as boundary."""
        prototypes = torch.zeros(2, 4)
        prototypes[0, 0] = 1.0  # proto 0 at [1,0,0,0]
        prototypes[1, 0] = -1.0  # proto 1 at [-1,0,0,0]
        # Midpoint between them
        midpoint = torch.zeros(1, 4)
        fm = compute_family_membership(midpoint, prototypes, boundary_threshold=0.3)
        assert fm.is_boundary[0].item(), "Midpoint should be boundary"
        # Point clearly near proto 0
        near_0 = torch.tensor([[0.9, 0.0, 0.0, 0.0]])
        fm2 = compute_family_membership(near_0, prototypes, boundary_threshold=0.3)
        assert not fm2.is_boundary[0].item(), "Point near proto 0 should not be boundary"

    def test_entropy_is_high_for_uniform_membership(self):
        """States equidistant from all prototypes should have high entropy."""
        # All prototypes at same distance
        prototypes = torch.eye(4, 4)
        # Point at origin — equidistant from all
        origin = torch.zeros(1, 4)
        fm = compute_family_membership(origin, prototypes)
        max_entropy = np.log(4)
        assert fm.membership_entropy[0].item() > max_entropy * 0.8, \
            f"Entropy should be near max ({max_entropy}), got {fm.membership_entropy[0].item()}"

    def test_margin_is_large_for_clear_assignments(self):
        """States clearly near one prototype should have large margin."""
        prototypes = torch.randn(8, 32)
        # State exactly equal to proto 3
        state = prototypes[3:4].clone()
        fm = compute_family_membership(state, prototypes)
        assert fm.membership_margin[0].item() > 0.1, \
            f"Clear assignment should have large margin: {fm.membership_margin[0].item()}"
        assert fm.nearest_prototype[0].item() == 3


# =============================================================================
# Family Preservation Score
# =============================================================================


class TestFamilyPreservationScore:
    """Verify preservation score measures owner-family compatibility."""

    def test_perfect_owner_gets_high_score(self):
        """If owner has high affinity for state's dominant family, score is high."""
        soft_membership = torch.tensor([[0.8, 0.1, 0.1]])  # strong in proto 0
        owner_ids = torch.tensor([0])
        # Expert 0 has high affinity for proto 0
        affinity = torch.zeros(4, 3)
        affinity[0, 0] = 5.0  # expert 0 strong for proto 0
        score = compute_family_preservation_score(soft_membership, owner_ids, affinity)
        assert score[0].item() > 0.7, f"Perfect owner should score high: {score[0].item()}"

    def test_bad_owner_gets_low_score(self):
        """If owner has no affinity for state's family, score is low."""
        soft_membership = torch.tensor([[0.8, 0.1, 0.1]])  # strong in proto 0
        owner_ids = torch.tensor([1])  # Expert 1 is the owner
        affinity = torch.zeros(4, 3)
        affinity[0, 0] = 5.0   # expert 0 strong for proto 0
        affinity[1, 2] = 5.0   # expert 1 strong for proto 2 (wrong)
        score = compute_family_preservation_score(soft_membership, owner_ids, affinity)
        # Expert 1 has no affinity for proto 0 where the state lives
        assert score[0].item() < 0.6, f"Bad owner should score low: {score[0].item()}"

    def test_score_between_zero_and_one(self):
        """Preservation score must always be in [0, 1]."""
        soft_membership = torch.rand(100, 8)
        soft_membership = soft_membership / soft_membership.sum(dim=-1, keepdim=True)
        owner_ids = torch.randint(0, 4, (100,))
        affinity = torch.randn(4, 8)
        scores = compute_family_preservation_score(soft_membership, owner_ids, affinity)
        assert (scores >= 0).all() and (scores <= 1).all()


# =============================================================================
# Family-Aware Oracle Gap
# =============================================================================


class TestFamilyOracleGap:
    """Verify oracle gap correctly identifies suboptimal owners."""

    def test_optimal_owner_has_zero_gap(self):
        """If current owner is already best, gap should be 0."""
        losses = torch.tensor([[0.1, 0.5, 0.8, 0.3]])  # Expert 0 is best
        owner_ids = torch.tensor([0])
        gap, best = compute_family_oracle_gap(losses, owner_ids)
        assert gap[0].item() == 0.0, f"Optimal owner gap should be 0, got {gap[0].item()}"
        assert best[0].item() == 0

    def test_suboptimal_owner_has_positive_gap(self):
        """If current owner is not best, gap should be positive."""
        losses = torch.tensor([[0.1, 0.5, 0.8, 0.3]])  # Expert 0 is best
        owner_ids = torch.tensor([2])  # But expert 2 is assigned (loss=0.8)
        gap, best = compute_family_oracle_gap(losses, owner_ids)
        expected_gap = 0.8 - 0.1
        assert abs(gap[0].item() - expected_gap) < 1e-5, \
            f"Gap should be {expected_gap}, got {gap[0].item()}"
        assert best[0].item() == 0

    def test_gap_is_nonnegative(self):
        """Oracle gap must always be >= 0."""
        losses = torch.rand(50, 4)
        owner_ids = torch.randint(0, 4, (50,))
        gap, _ = compute_family_oracle_gap(losses, owner_ids)
        assert (gap >= -1e-6).all(), f"Gap should be non-negative: min={gap.min().item()}"


# =============================================================================
# Owner Churn Tracking
# =============================================================================


class TestOwnerChurn:
    """Verify churn tracking correctly identifies unstable ownership."""

    def test_stable_ownership_has_low_churn(self):
        """If same owner every snapshot, churn should be 0."""
        state = OwnerChurnState(
            ownership_counts=torch.zeros(4, 4),
            num_snapshots=0,
        )
        # Record 5 snapshots with same ownership
        for _ in range(5):
            state.record_snapshot(
                owner_ids=torch.tensor([0, 1, 2, 3]),
                prototype_ids=torch.tensor([0, 1, 2, 3]),
            )
        churn = state.churn_rate()
        assert churn.max().item() == 0.0, f"Stable ownership should have 0 churn: {churn}"

    def test_unstable_ownership_has_high_churn(self):
        """If owner changes every snapshot, churn should be high."""
        state = OwnerChurnState(
            ownership_counts=torch.zeros(4, 4),
            num_snapshots=0,
        )
        # Record snapshots with rotating ownership for proto 0
        for i in range(4):
            state.record_snapshot(
                owner_ids=torch.tensor([i % 4]),
                prototype_ids=torch.tensor([0]),
            )
        churn = state.churn_rate()
        # Proto 0 has seen all 4 experts equally → churn = 1 - 0.25 = 0.75
        assert churn[0].item() == 0.75, f"Rotating ownership churn wrong: {churn[0].item()}"


# =============================================================================
# Shadow Family-Preservation Bias
# =============================================================================


class TestShadowFamilyBias:
    """Verify shadow bias is tensor-backed, clipped, and never active in first pass."""

    def test_shadow_bias_is_always_shadow_in_first_pass(self):
        """Shadow bias must report shadow-only mode."""
        config = FamilyPreservationBiasConfig(num_prototypes=8, num_experts=4)
        bias = ShadowFamilyPreservationBias(config)
        assert bias.is_shadow_only, "Bias must be shadow-only in first pass"

    def test_bias_is_clipped(self):
        """Clipped bias must respect the cap."""
        config = FamilyPreservationBiasConfig(
            num_prototypes=4, num_experts=4,
            family_bias_weight=1.0, family_bias_cap=0.25,
        )
        bias = ShadowFamilyPreservationBias(config)
        # Set extreme reliability
        bias.family_owner_reliability = torch.ones(4, 4) * 100.0
        clipped = bias.clipped_bias()
        assert clipped.max().item() <= 0.25 + 1e-6
        assert clipped.min().item() >= -0.25 - 1e-6

    def test_shadow_scores_respect_compatible_mask(self):
        """Shadow routing must not route outside compatible mask."""
        config = FamilyPreservationBiasConfig(num_prototypes=4, num_experts=4)
        bias = ShadowFamilyPreservationBias(config)
        # Set bias to strongly prefer expert 3
        bias.family_owner_reliability[0, 3] = 10.0

        scores = torch.zeros(4, 4)
        prototype_ids = torch.zeros(4, dtype=torch.long)
        # Mask: only experts 0 and 1 are compatible
        mask = torch.zeros(4, 4)
        mask[:, 0] = 1.0
        mask[:, 1] = 1.0

        result = bias.compute_shadow_scores(scores, prototype_ids, mask)
        # Shadow owner should be 0 or 1, never 3 (masked out)
        assert (result["shadow_owner"] <= 1).all(), \
            f"Shadow routed outside mask: {result['shadow_owner']}"

    def test_shadow_logs_would_change_owner(self):
        """If bias would change owner, it must be logged."""
        config = FamilyPreservationBiasConfig(
            num_prototypes=4, num_experts=4,
            family_bias_weight=1.0, family_bias_cap=5.0,
        )
        bias = ShadowFamilyPreservationBias(config)
        # Strongly bias proto 0 toward expert 2
        bias.family_owner_reliability[0, 2] = 50.0

        # Current scores favor expert 0
        scores = torch.zeros(8, 4)
        scores[:, 0] = 1.0
        prototype_ids = torch.zeros(8, dtype=torch.long)
        mask = torch.ones(8, 4)

        result = bias.compute_shadow_scores(scores, prototype_ids, mask)
        # Bias should flip some/all tokens to expert 2
        assert result["would_change_owner"].any(), "Strong bias should change some owners"
        assert result["change_rate"] > 0.0

    def test_update_from_evidence_accumulates_correctly(self):
        """Evidence updates must accumulate reliability and failure counts."""
        config = FamilyPreservationBiasConfig(num_prototypes=4, num_experts=4)
        bias = ShadowFamilyPreservationBias(config)

        # 5 successes for expert 0 on prototype 0
        bias.update_from_evidence(
            prototype_ids=torch.zeros(5, dtype=torch.long),
            expert_ids=torch.zeros(5, dtype=torch.long),
            success=torch.ones(5, dtype=torch.bool),
        )
        assert bias.family_owner_reliability[0, 0].item() == 5.0

        # 3 failures for expert 1 on prototype 0
        bias.update_from_evidence(
            prototype_ids=torch.zeros(3, dtype=torch.long),
            expert_ids=torch.ones(3, dtype=torch.long),
            success=torch.zeros(3, dtype=torch.bool),
        )
        assert bias.family_owner_failure[0, 1].item() == 3.0


# =============================================================================
# Family Metrics Computation
# =============================================================================


class TestFamilyMetrics:
    """Verify aggregate family metrics are computed correctly."""

    def test_metrics_have_required_keys(self):
        """All required metric keys must be present."""
        soft_membership = torch.rand(32, 8)
        soft_membership = soft_membership / soft_membership.sum(dim=-1, keepdim=True)
        owner_ids = torch.randint(0, 4, (32,))
        prototype_ids = torch.randint(0, 8, (32,))
        metrics = compute_family_metrics(soft_membership, owner_ids, prototype_ids, num_experts=4)
        required = [
            "expert_family_purity", "expert_family_coverage",
            "expert_family_entropy", "prototype_family_owner_consistency",
            "prototype_local_monopoly_rate", "owner_entropy",
            "family_label_proxy_disagreement_rate",
        ]
        for key in required:
            assert key in metrics, f"Missing metric: {key}"

    def test_monopoly_detected_when_one_expert_dominates(self):
        """If one expert owns all tokens in a prototype, monopoly should be flagged."""
        soft_membership = torch.rand(32, 4)
        # All tokens assigned to expert 0, all in prototype 0
        owner_ids = torch.zeros(32, dtype=torch.long)
        prototype_ids = torch.zeros(32, dtype=torch.long)
        metrics = compute_family_metrics(soft_membership, owner_ids, prototype_ids, num_experts=4)
        assert metrics["prototype_local_monopoly_rate"] > 0.5, \
            f"Should detect monopoly: {metrics['prototype_local_monopoly_rate']}"

    def test_balanced_ownership_has_low_monopoly(self):
        """Balanced ownership across prototypes should have low monopoly rate."""
        soft_membership = torch.rand(64, 8)
        # Each prototype has tokens from multiple experts
        # Proto 0: experts 0,1  Proto 1: experts 2,3  etc — but mixed within
        owner_ids = torch.zeros(64, dtype=torch.long)
        prototype_ids = torch.zeros(64, dtype=torch.long)
        for i in range(64):
            prototype_ids[i] = i % 8
            # Within each prototype, alternate between 2 experts
            owner_ids[i] = (i // 8) % 4  # Different expert groupings per prototype slot
        # Ensure at least 2 different owners per prototype
        for p in range(8):
            mask = prototype_ids == p
            indices = mask.nonzero(as_tuple=True)[0]
            if len(indices) >= 2:
                owner_ids[indices[0]] = 0
                owner_ids[indices[1]] = 1
        metrics = compute_family_metrics(soft_membership, owner_ids, prototype_ids, num_experts=4)
        assert metrics["prototype_local_monopoly_rate"] < 0.5, \
            f"Balanced should have low monopoly: {metrics['prototype_local_monopoly_rate']}"


# =============================================================================
# Family Preservation Gate
# =============================================================================


class TestFamilyPreservationGate:
    """Verify gate logic enforces hard invariants and detects blockers."""

    def test_gate_blocks_on_multiple_owners(self):
        """Gate must block if owners_per_token != 1."""
        result = family_preservation_gate(
            metrics={}, owners_per_token=2.0,
        )
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVATION_BLOCKED"

    def test_gate_blocks_on_top2_execution(self):
        """Gate must block if Top2 executions > 0."""
        result = family_preservation_gate(
            metrics={}, top2_executions=1,
        )
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVATION_BLOCKED"

    def test_gate_requires_expansion_on_unknown_failures(self):
        """Unknown failures require observatory expansion."""
        result = family_preservation_gate(
            metrics={}, unknown_failures=1,
        )
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVATION_OBSERVATORY_EXPANSION_REQUIRED"

    def test_gate_passes_with_good_metrics(self):
        """Good metrics with no invariant violations should pass."""
        metrics = {
            "expert_family_purity": 0.6,
            "expert_family_coverage": 0.4,
            "expert_family_entropy": 1.2,
            "prototype_family_owner_consistency": 0.7,
            "prototype_local_monopoly_rate": 0.1,
        }
        result = family_preservation_gate(metrics)
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVATION_PASSED"

    def test_gate_passes_with_blockers_on_high_monopoly(self):
        """High monopoly should pass with blockers, not block outright."""
        metrics = {
            "expert_family_purity": 0.6,
            "expert_family_entropy": 1.0,
            "prototype_local_monopoly_rate": 0.7,  # High
        }
        result = family_preservation_gate(metrics)
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVATION_PASSED_WITH_BLOCKERS"


# =============================================================================
# Failure Registry Extension
# =============================================================================


class TestFailureRegistryExtension:
    """Verify family preservation failure modes are registered correctly."""

    def test_all_family_modes_registered(self):
        """Every family preservation failure mode must be in the registry."""
        from sparse_loop_moe.models.pvr_ec.family_preservation import \
            FAMILY_PRESERVATION_FAILURE_MODES
        for mode in FAMILY_PRESERVATION_FAILURE_MODES:
            assert mode in FAILURE_MODE_IDS, f"{mode} not in FAILURE_MODE_IDS"

    def test_registry_has_playbooks_for_new_modes(self):
        """New modes must have valid playbooks in the registry."""
        registry = failure_mode_registry()
        family_modes = [m for m in FAILURE_MODE_IDS if "FAMILY" in m or "NLP_" in m]
        for mode in family_modes:
            assert mode in registry, f"{mode} not in registry"
            entry = registry[mode]
            assert "allowed_repairs" in entry
            assert "disallowed_repairs" in entry
            # No Top2/Top4 should be allowed
            for repair in entry["allowed_repairs"]:
                assert "Top2" not in repair and "Top4" not in repair, \
                    f"Top2/Top4 repair in allowed list for {mode}: {repair}"


# =============================================================================
# Integration: Family Metrics on Trained PVR Model
# =============================================================================


class TestFamilyMetricsOnTrainedModel:
    """Run real forward passes and verify family metrics are computable."""

    def _build_model(self):
        return PVRECModel(PVRECModelConfig(
            vocab_size=256, d_model=64, max_seq_len=64,
            n_layers=2, n_heads=2, d_ff=128, num_experts=4,
            num_prototypes=8, max_k=4, d_expert=64,
            pvr_deploy_mode="top1", dropout=0.0,
        ))

    def test_family_membership_from_router_embeddings(self):
        """Can compute family membership from a live model's routing space."""
        model = self._build_model()
        x = torch.randint(1, 64, (4, 16))

        # Get routing space embeddings through the model's router
        with torch.no_grad():
            # Access first block's router
            block = model.blocks[0]
            moe = block.moe
            router = moe.router

            # Get hidden states from token embeddings
            positions = torch.arange(16).unsqueeze(0)
            hidden = model.token_emb(x) + model.pos_emb(positions)
            flat_hidden = hidden.reshape(-1, 64)

            # Project to routing space
            z = router.route_proj(flat_hidden)
            prototypes = router.prototypes

            # Compute family membership
            fm = compute_family_membership(z, prototypes)

        assert fm.soft_membership.shape == (64, 8)  # 4*16 tokens, 8 prototypes
        assert (fm.soft_membership >= 0).all()
        assert torch.allclose(fm.soft_membership.sum(dim=-1), torch.ones(64), atol=1e-5)

    def test_family_metrics_after_training(self):
        """Family metrics should be computable after a few training steps."""
        model = self._build_model()
        g = torch.Generator().manual_seed(42)
        x = torch.randint(1, 64, (8, 16), generator=g)
        y = x.clone()  # identity task

        # Train a few steps
        opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
        for _ in range(10):
            opt.zero_grad()
            out = model(input_ids=x, targets=y)
            out["loss"].backward()
            opt.step()

        # Get routing info
        with torch.no_grad():
            out = model(input_ids=x)
            block = model.blocks[0]
            moe = block.moe
            router = moe.router

            hidden = model.token_emb(x) + model.pos_emb(torch.arange(16).unsqueeze(0))
            attn_in = block.attn_ln(hidden)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post_attn = hidden + attn_out
            moe_in = block.moe_ln(post_attn)
            flat = moe_in.reshape(-1, 64)

            z = router.route_proj(flat)
            fm = compute_family_membership(z, router.prototypes)

            # Get owner ids through deploy path
            moe_out, aux = moe(moe_in)
            owner_ids = aux["primary_expert_ids"]

        # Compute metrics
        metrics = compute_family_metrics(
            fm.soft_membership, owner_ids, fm.nearest_prototype, num_experts=4
        )
        assert "expert_family_purity" in metrics
        assert 0 <= metrics["expert_family_purity"] <= 1.0
        assert metrics["owner_entropy"] >= 0.0
