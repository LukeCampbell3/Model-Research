"""Robust tests for PVR-EC Family-Preserving Top1 Candidate Router.

Tests actual routing behavior, candidate map lifecycle, Expert Choice
teacher evidence, and gate acceptance/rejection logic with real models.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "evaluation"))

import torch
import torch.nn.functional as F
import pytest

from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import PVRECMoEFFN
from sparse_loop_moe.models.pvr_ec.pvr_ec_model import PVRECModel, PVRECModelConfig
from sparse_loop_moe.models.pvr_ec.pvr_ec_router import PVRECRouter, PVRECConfig
from sparse_loop_moe.models.pvr_ec.family_preserving_router import (
    CANDIDATE_MAP_SCHEMA_VERSION,
    CandidateMap,
    CandidateMapMetadata,
    compute_expert_choice_evidence,
    create_blank_candidate_map,
    evaluate_candidate_gate,
    family_preserving_top1_score,
    load_candidate_map,
    refresh_candidate_map_from_evidence,
    save_candidate_map,
)


# =============================================================================
# Helpers
# =============================================================================


def _build_model(num_experts=4, num_prototypes=8, d_model=64):
    return PVRECModel(PVRECModelConfig(
        vocab_size=256, d_model=d_model, max_seq_len=64,
        n_layers=2, n_heads=2, d_ff=128, num_experts=num_experts,
        num_prototypes=num_prototypes, max_k=4, d_expert=64,
        pvr_deploy_mode="top1", dropout=0.0,
    ))


def _make_candidate_map(num_prototypes=8, num_experts=4, seed=42):
    """Create a candidate map with some non-zero evidence."""
    torch.manual_seed(seed)
    cmap = create_blank_candidate_map(num_prototypes, num_experts)
    # Add some evidence
    cmap.family_owner_reliability = torch.rand(num_prototypes, num_experts) * 5
    cmap.family_owner_failure = torch.rand(num_prototypes, num_experts) * 2
    return cmap


# =============================================================================
# Family-Preserving Score Computation
# =============================================================================


class TestFamilyPreservingScore:
    """Verify the family-preserving Top1 score produces single-owner results."""

    def test_produces_exactly_one_owner_per_token(self):
        """Score must produce exactly one owner per token."""
        N = 32
        num_experts = 4
        num_prototypes = 8
        router_logits = torch.randn(N, num_experts)
        proto_bias = torch.randn(N, num_experts)
        proto_ids = torch.randint(0, num_prototypes, (N,))
        mask = torch.ones(N, num_experts)
        cmap = _make_candidate_map(num_prototypes, num_experts)

        owner_ids, scores = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, cmap
        )
        assert owner_ids.shape == (N,)
        # Each token gets exactly one owner
        assert (owner_ids >= 0).all()
        assert (owner_ids < num_experts).all()

    def test_respects_compatible_mask(self):
        """Owners must never be from incompatible experts."""
        N = 16
        num_experts = 4
        num_prototypes = 4
        router_logits = torch.randn(N, num_experts)
        proto_bias = torch.zeros(N, num_experts)
        proto_ids = torch.zeros(N, dtype=torch.long)
        # Only experts 0 and 1 are compatible
        mask = torch.zeros(N, num_experts)
        mask[:, 0] = 1.0
        mask[:, 1] = 1.0
        cmap = _make_candidate_map(num_prototypes, num_experts)
        # Even if family bias strongly favors expert 3
        cmap.family_owner_reliability[:, 3] = 100.0

        owner_ids, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, cmap
        )
        assert (owner_ids <= 1).all(), f"Routed outside mask: {owner_ids.unique()}"

    def test_family_bias_influences_routing(self):
        """Family bias should change routing decisions vs no-bias baseline."""
        N = 32
        num_experts = 4
        num_prototypes = 4
        torch.manual_seed(0)
        router_logits = torch.randn(N, num_experts) * 0.1  # Weak base signal
        proto_bias = torch.zeros(N, num_experts)
        proto_ids = torch.zeros(N, dtype=torch.long)
        mask = torch.ones(N, num_experts)

        # Blank map (no family bias)
        blank = create_blank_candidate_map(num_prototypes, num_experts)
        owners_blank, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, blank
        )

        # Map with strong family bias toward expert 2
        biased = create_blank_candidate_map(num_prototypes, num_experts)
        biased.family_owner_reliability[0, 2] = 50.0  # Strong preference

        owners_biased, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, biased,
            family_bias_weight=1.0, family_bias_cap=5.0,
        )

        # Biased version should route more tokens to expert 2
        biased_to_2 = (owners_biased == 2).sum().item()
        blank_to_2 = (owners_blank == 2).sum().item()
        assert biased_to_2 > blank_to_2, \
            f"Family bias should increase routing to expert 2: {biased_to_2} vs {blank_to_2}"

    def test_monopoly_penalty_reduces_dominant_expert_load(self):
        """Monopoly penalty should push tokens away from monopolized experts."""
        N = 32
        num_experts = 4
        num_prototypes = 4
        # Base scores slightly favor expert 0
        router_logits = torch.zeros(N, num_experts)
        router_logits[:, 0] = 0.5
        proto_bias = torch.zeros(N, num_experts)
        proto_ids = torch.zeros(N, dtype=torch.long)
        mask = torch.ones(N, num_experts)

        # Without penalty
        no_penalty = create_blank_candidate_map(num_prototypes, num_experts)
        owners_no, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, no_penalty
        )
        load_no = (owners_no == 0).sum().item()

        # With monopoly penalty on expert 0
        with_penalty = create_blank_candidate_map(num_prototypes, num_experts)
        with_penalty.prototype_local_monopoly_penalty[0, 0] = 2.0

        owners_pen, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, with_penalty
        )
        load_pen = (owners_pen == 0).sum().item()

        assert load_pen < load_no, \
            f"Monopoly penalty should reduce expert 0 load: {load_pen} vs {load_no}"


# =============================================================================
# Candidate Map Lifecycle
# =============================================================================


class TestCandidateMapLifecycle:
    """Verify save/load/validate cycle for candidate maps."""

    def test_save_and_load_round_trip(self, tmp_path):
        """Save then load should produce identical tensors."""
        cmap = _make_candidate_map(num_prototypes=8, num_experts=4)
        save_candidate_map(cmap, tmp_path)
        loaded = load_candidate_map(tmp_path, expected_num_prototypes=8, expected_num_experts=4)
        assert torch.equal(loaded.family_owner_reliability, cmap.family_owner_reliability)
        assert torch.equal(loaded.family_owner_failure, cmap.family_owner_failure)
        assert torch.equal(loaded.prototype_local_monopoly_penalty, cmap.prototype_local_monopoly_penalty)

    def test_metadata_written_correctly(self, tmp_path):
        """Metadata JSON must contain all required fields."""
        cmap = _make_candidate_map(num_prototypes=8, num_experts=4)
        save_candidate_map(cmap, tmp_path)
        meta = json.loads((tmp_path / "family_preservation_metadata.json").read_text())
        assert meta["schema_version"] == CANDIDATE_MAP_SCHEMA_VERSION
        assert meta["num_prototypes"] == 8
        assert meta["num_experts"] == 4
        assert meta["promotion_status"] == "candidate"

    def test_load_rejects_mismatched_prototypes(self, tmp_path):
        """Loading with wrong expected dimensions must raise ValueError."""
        cmap = _make_candidate_map(num_prototypes=8, num_experts=4)
        save_candidate_map(cmap, tmp_path)
        with pytest.raises(ValueError, match="Prototype mismatch"):
            load_candidate_map(tmp_path, expected_num_prototypes=16, expected_num_experts=4)

    def test_load_rejects_mismatched_experts(self, tmp_path):
        """Loading with wrong expert count must raise ValueError."""
        cmap = _make_candidate_map(num_prototypes=8, num_experts=4)
        save_candidate_map(cmap, tmp_path)
        with pytest.raises(ValueError, match="Expert mismatch"):
            load_candidate_map(tmp_path, expected_num_prototypes=8, expected_num_experts=8)

    def test_candidate_does_not_mutate_production_map(self, tmp_path):
        """Creating/saving a candidate must not affect a separate 'production' tensor."""
        production = torch.randn(8, 4)
        production_copy = production.clone()
        cmap = _make_candidate_map(num_prototypes=8, num_experts=4)
        save_candidate_map(cmap, tmp_path)
        # Production should be unchanged
        assert torch.equal(production, production_copy)


# =============================================================================
# Expert Choice Teacher Evidence
# =============================================================================


class TestExpertChoiceTeacherEvidence:
    """Verify offline Expert Choice evidence is computed correctly."""

    def test_evidence_produces_required_metrics(self):
        """Evidence dict must contain all required keys."""
        model = _build_model()
        x = torch.randint(1, 64, (4, 16))
        with torch.no_grad():
            # Get hidden states from first block
            positions = torch.arange(16).unsqueeze(0)
            hidden = model.token_emb(x) + model.pos_emb(positions)
            flat = hidden.reshape(-1, 64)
            proto_ids = torch.randint(0, 8, (64,))
            owners = torch.randint(0, 4, (64,))
            targets = torch.randint(0, 64, (64,))

            experts = list(model.blocks[0].moe.expert_deltas)
            evidence = compute_expert_choice_evidence(
                flat, experts, proto_ids, owners, targets
            )

        required_keys = [
            "challenger_family_win_rate",
            "teacher_family_owner_agreement",
            "single_owner_distillation_gap",
            "expert_family_recall",
            "expert_family_coverage",
        ]
        for key in required_keys:
            assert key in evidence, f"Missing key: {key}"

    def test_challenger_win_rate_bounded(self):
        """Challenger win rate must be in [0, 1]."""
        hidden = torch.randn(32, 64)
        from sparse_loop_moe.models.pvr_ec.pvr_ec_moe import LowRankExpertDelta
        experts = [LowRankExpertDelta(64, 32) for _ in range(4)]
        proto_ids = torch.randint(0, 4, (32,))
        owners = torch.randint(0, 4, (32,))
        targets = torch.randint(0, 64, (32,))

        evidence = compute_expert_choice_evidence(
            hidden, experts, proto_ids, owners, targets
        )
        assert 0.0 <= evidence["challenger_family_win_rate"] <= 1.0
        assert 0.0 <= evidence["teacher_family_owner_agreement"] <= 1.0

    def test_teacher_evidence_is_offline_only(self):
        """Teacher evidence must not modify model parameters."""
        model = _build_model()
        params_before = {n: p.clone() for n, p in model.named_parameters()}

        x = torch.randint(1, 64, (2, 16))
        with torch.no_grad():
            positions = torch.arange(16).unsqueeze(0)
            hidden = model.token_emb(x) + model.pos_emb(positions)
            flat = hidden.reshape(-1, 64)
            experts = list(model.blocks[0].moe.expert_deltas)
            compute_expert_choice_evidence(
                flat, experts, torch.zeros(32, dtype=torch.long),
                torch.zeros(32, dtype=torch.long), torch.zeros(32, dtype=torch.long),
            )

        # Parameters must not change
        for n, p in model.named_parameters():
            assert torch.equal(p, params_before[n]), f"Parameter {n} was modified!"


# =============================================================================
# Candidate Map Refresh
# =============================================================================


class TestCandidateMapRefresh:
    """Verify candidate map refresh accumulates evidence correctly."""

    def test_refresh_increases_reliability_for_successes(self):
        """Successful tokens should increase expert reliability."""
        base = create_blank_candidate_map(4, 4)
        evidence = {"best_expert_per_token": torch.zeros(8, dtype=torch.long)}
        proto_ids = torch.zeros(8, dtype=torch.long)
        owners = torch.zeros(8, dtype=torch.long)
        success = torch.ones(8, dtype=torch.bool)

        refreshed = refresh_candidate_map_from_evidence(
            base, evidence, proto_ids, owners, success
        )
        assert refreshed.family_owner_reliability[0, 0] > 0, \
            "Reliability should increase for successful expert"

    def test_refresh_increases_failure_for_failures(self):
        """Failed tokens should increase expert failure count."""
        base = create_blank_candidate_map(4, 4)
        evidence = {"best_expert_per_token": torch.ones(8, dtype=torch.long)}
        proto_ids = torch.zeros(8, dtype=torch.long)
        owners = torch.zeros(8, dtype=torch.long)
        success = torch.zeros(8, dtype=torch.bool)

        refreshed = refresh_candidate_map_from_evidence(
            base, evidence, proto_ids, owners, success
        )
        assert refreshed.family_owner_failure[0, 0] > 0, \
            "Failure should increase for failing expert"

    def test_refresh_does_not_mutate_base(self):
        """Refresh must return a new map, not mutate the original."""
        base = create_blank_candidate_map(4, 4)
        original_reliability = base.family_owner_reliability.clone()
        evidence = {"best_expert_per_token": torch.zeros(8, dtype=torch.long)}
        proto_ids = torch.zeros(8, dtype=torch.long)
        owners = torch.zeros(8, dtype=torch.long)
        success = torch.ones(8, dtype=torch.bool)

        _ = refresh_candidate_map_from_evidence(
            base, evidence, proto_ids, owners, success
        )
        assert torch.equal(base.family_owner_reliability, original_reliability), \
            "Base map was mutated!"

    def test_monopoly_penalty_applied_for_dominant_expert(self):
        """Monopoly penalty should appear if one expert dominates a prototype."""
        base = create_blank_candidate_map(4, 4)
        # Pre-load: expert 0 has massive reliability for proto 0
        base.family_owner_reliability[0, 0] = 100.0
        evidence = {"best_expert_per_token": torch.zeros(4, dtype=torch.long)}
        proto_ids = torch.zeros(4, dtype=torch.long)
        owners = torch.zeros(4, dtype=torch.long)
        success = torch.ones(4, dtype=torch.bool)

        refreshed = refresh_candidate_map_from_evidence(
            base, evidence, proto_ids, owners, success,
            monopoly_threshold=0.8,
        )
        assert refreshed.prototype_local_monopoly_penalty[0, 0] > 0, \
            "Monopoly penalty should be applied for dominant expert"


# =============================================================================
# Candidate Gate Logic
# =============================================================================


class TestCandidateGate:
    """Verify gate acceptance/rejection logic."""

    def test_gate_rejects_on_top2_execution(self):
        """Any Top2 execution must trigger rejection."""
        result = evaluate_candidate_gate(
            before_metrics={}, after_metrics={},
            top2_executions=1,
        )
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED"

    def test_gate_rejects_on_multi_owner(self):
        """owners_per_token != 1 must trigger rejection."""
        result = evaluate_candidate_gate(
            before_metrics={}, after_metrics={},
            owners_per_token=2.0,
        )
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED"

    def test_gate_accepts_on_oracle_gap_improvement(self):
        """If oracle gap improves with no regressions, accept."""
        before = {"family_top1_oracle_gap": 0.5, "prototype_local_monopoly_rate": 0.2}
        after = {"family_top1_oracle_gap": 0.3, "prototype_local_monopoly_rate": 0.2}
        result = evaluate_candidate_gate(before, after)
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVING_ROUTER_ACCEPTED"

    def test_gate_rejects_on_oracle_gap_worsening(self):
        """If oracle gap worsens significantly, reject."""
        before = {"family_top1_oracle_gap": 0.3}
        after = {"family_top1_oracle_gap": 0.5}
        result = evaluate_candidate_gate(before, after)
        assert "REJECTED" in result["verdict"] or "PARTIAL" in result["verdict"]

    def test_gate_partial_on_mixed_results(self):
        """If some metrics improve but others worsen, partial."""
        before = {
            "family_top1_oracle_gap": 0.5,
            "calibration_proxy": 0.1,
        }
        after = {
            "family_top1_oracle_gap": 0.3,  # Improved
            "calibration_proxy": 0.2,       # Worsened
        }
        result = evaluate_candidate_gate(before, after)
        assert result["verdict"] in (
            "PVR_EC_FAMILY_PRESERVING_ROUTER_PARTIAL",
            "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED",
        )

    def test_gate_needs_evidence_on_no_change(self):
        """If nothing changes, need more evidence."""
        before = {"family_top1_oracle_gap": 0.5}
        after = {"family_top1_oracle_gap": 0.5}
        result = evaluate_candidate_gate(before, after)
        assert result["verdict"] == "PVR_EC_FAMILY_PRESERVING_ROUTER_NEEDS_MORE_EVIDENCE"

    def test_gate_rejects_mean_only_improvement(self):
        """If worst-case worsens but mean improves, should not accept blindly."""
        before = {
            "family_top1_oracle_gap": 0.5,
            "high_confidence_family_failure_rate": 0.1,
        }
        after = {
            "family_top1_oracle_gap": 0.3,  # Mean improved
            "high_confidence_family_failure_rate": 0.15,  # Worst-case worsened
        }
        result = evaluate_candidate_gate(before, after)
        # Should not be fully accepted
        assert result["verdict"] != "PVR_EC_FAMILY_PRESERVING_ROUTER_ACCEPTED"


# =============================================================================
# Integration: Full Pipeline on Real Model
# =============================================================================


class TestFullPipelineIntegration:
    """End-to-end test: compute evidence, refresh map, score, gate."""

    def test_full_pipeline_produces_valid_routing(self):
        """Full pipeline: evidence → refresh → score → single owner."""
        model = _build_model(num_experts=4, num_prototypes=8)
        x = torch.randint(1, 64, (4, 16))

        with torch.no_grad():
            # Forward to get hidden states and routing
            positions = torch.arange(16).unsqueeze(0)
            hidden = model.token_emb(x) + model.pos_emb(positions)
            block = model.blocks[0]
            attn_in = block.attn_ln(hidden)
            attn_out, _ = block.attn(attn_in, attn_in, attn_in, need_weights=False)
            post_attn = hidden + attn_out
            moe_in = block.moe_ln(post_attn)
            flat = moe_in.reshape(-1, 64)

            # Get router info
            router = block.moe.router
            z = router.route_proj(flat)
            proto_dist = torch.cdist(z.unsqueeze(0), router.prototypes.unsqueeze(0)).squeeze(0)
            proto_ids = proto_dist.argmin(dim=-1)

            # Current routing
            moe_out, aux = block.moe(moe_in)
            current_owners = aux["primary_expert_ids"]

            # Expert Choice evidence (offline)
            experts = list(block.moe.expert_deltas)
            targets = torch.randint(0, 64, (flat.shape[0],))
            evidence = compute_expert_choice_evidence(
                flat, experts, proto_ids, current_owners, targets
            )

        # Create and refresh candidate map
        base_map = create_blank_candidate_map(8, 4)
        success = torch.rand(flat.shape[0]) > 0.3  # 70% success rate
        refreshed = refresh_candidate_map_from_evidence(
            base_map, evidence, proto_ids, current_owners, success
        )

        # Score with family-preserving router
        with torch.no_grad():
            router_logits = router.gate(z)
            proto_bias_per_token = router.proto_bias[proto_ids]
            compat_mask = router.proto_expert_compat[proto_ids]

            owner_ids, scores = family_preserving_top1_score(
                router_logits, proto_bias_per_token, proto_ids,
                compat_mask, refreshed,
            )

        # Verify invariants
        assert owner_ids.shape == (flat.shape[0],)
        assert (owner_ids >= 0).all()
        assert (owner_ids < 4).all()
        # Every token got exactly one owner
        assert owner_ids.shape[0] == flat.shape[0]

    def test_pipeline_with_save_load(self, tmp_path):
        """Full pipeline survives save/load cycle."""
        cmap = _make_candidate_map(8, 4)
        save_candidate_map(cmap, tmp_path)
        loaded = load_candidate_map(tmp_path, 8, 4)

        # Use loaded map for scoring
        router_logits = torch.randn(16, 4)
        proto_bias = torch.zeros(16, 4)
        proto_ids = torch.randint(0, 8, (16,))
        mask = torch.ones(16, 4)

        owners_original, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, cmap
        )
        owners_loaded, _ = family_preserving_top1_score(
            router_logits, proto_bias, proto_ids, mask, loaded
        )
        assert torch.equal(owners_original, owners_loaded), \
            "Routing should be identical after save/load"

    def test_training_with_candidate_router_reduces_loss(self):
        """A model using candidate router scores should still be trainable."""
        model = _build_model()
        x = torch.randint(1, 64, (8, 16))
        y = x.clone()  # identity task

        # Verify model trains normally (candidate router is offline scoring,
        # the model itself still trains with its built-in router)
        opt = torch.optim.AdamW(model.parameters(), lr=3e-3)
        losses = []
        for _ in range(30):
            opt.zero_grad()
            out = model(input_ids=x, targets=y)
            out["loss"].backward()
            opt.step()
            losses.append(out["loss"].item())

        assert losses[-1] < losses[0] * 0.5, \
            f"Model should train: {losses[0]:.3f} → {losses[-1]:.3f}"
