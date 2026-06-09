"""Failure mode registry for PVR-EC-O observability."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


REQUIRED_FAILURE_MODE_FIELDS = (
    "id",
    "name",
    "description",
    "trigger_conditions",
    "required_evidence",
    "severity",
    "repeatability_requirement",
    "primary_metrics",
    "secondary_metrics",
    "allowed_repairs",
    "disallowed_repairs",
    "promotion_impact",
    "research_impact",
)


FAILURE_MODE_IDS = (
    "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
    "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL",
    "PVR_EC_FAILURE_SPARSE_LOGIT_MISDIRECTION",
    "PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP",
    "PVR_EC_FAILURE_CALIBRATION_COLLAPSE",
    "PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER",
    "PVR_EC_FAILURE_SEQUENCE_LENGTH_GENERALIZATION",
    "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
    "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION",
    "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION",
    "PVR_EC_FAILURE_SHARED_SPARSE_IMBALANCE",
    "PVR_EC_FAILURE_EXPERT_DEAD_OR_MONOPOLIZED",
    "PVR_EC_FAILURE_HIGH_CONFIDENCE_WRONG",
    "PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC",
    "PVR_EC_FAILURE_OWNERSHIP_MAP_STALENESS",
    "PVR_EC_FAILURE_PROTOTYPE_DRIFT",
    "PVR_EC_FAILURE_REPAIR_OVERFITS_COLLAPSE_CASE",
    "PVR_EC_FAILURE_UNKNOWN",
    # Family preservation failure modes
    "PVR_EC_FAILURE_FAMILY_PRESERVATION_LOSS",
    "PVR_EC_FAILURE_OVERLAP_BOUNDARY_MISROUTE",
    "PVR_EC_FAILURE_NOISY_REGION_OWNERSHIP",
    "PVR_EC_FAILURE_FAMILY_OWNER_CHURN",
    "PVR_EC_FAILURE_PROTOTYPE_FAMILY_COLLAPSE",
    "PVR_EC_FAILURE_BALANCE_BIAS_FAMILY_OVERRIDE",
    "PVR_EC_FAILURE_FAMILY_AWARE_ORACLE_GAP_HIGH",
    "PVR_EC_FAILURE_SOFT_FAMILY_EVIDENCE_DROPPED",
    "PVR_EC_FAILURE_FAMILY_LABEL_PROXY_DISAGREEMENT",
    "PVR_EC_FAILURE_NLP_AMBIGUOUS_TOKEN_OWNERSHIP",
    "PVR_EC_FAILURE_NLP_CONTEXT_INSENSITIVE_ROUTING",
    "PVR_EC_FAILURE_NLP_LENGTH_GENERALIZATION_COLLAPSE",
    "PVR_EC_FAILURE_NLP_OBSERVATORY_TAXONOMY_GAP",
)


PLAYBOOKS: dict[str, dict[str, list[str]]] = {
    "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE": {
        "inspect": ["owner_entropy", "prototype_entropy", "dead_expert_count", "expert_monopoly_rate", "prototype_local_monopoly_rate"],
        "allowed_repairs": ["family_balanced_sampling", "family_balanced_loss_light", "ownership_bias_clip_adjustment", "prototype_entropy_regularization_light", "owner_entropy_floor_diagnostic_only"],
        "disallowed_repairs": ["Top2/Top4 execution", "new router architecture", "larger experts", "distillation"],
    },
    "PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL": {
        "inspect": ["residual_help_rate", "residual_harm_rate", "expert_delta_contribution_pct", "expert_grad_norm", "shared_sparse_ratio"],
        "allowed_repairs": ["expert_delta_scale_schedule adjustment", "sparse_ce_weight adjustment", "decision-token sparse CE", "gradient clipping", "shared/sparse scale balancing"],
        "disallowed_repairs": ["ownership map changes", "Top2/Top4", "larger experts unless capacity has been proven blocker"],
    },
    "PVR_EC_FAILURE_SPARSE_LOGIT_MISDIRECTION": {
        "inspect": ["correct_class_logit_delta", "incorrect_class_logit_delta_max", "delta_correct_minus_top_wrong", "incorrect_overamp_rate", "logit_norm"],
        "allowed_repairs": ["sparse_ce", "margin alignment", "wrong suppress", "logit norm penalty", "sparse_ce decay", "temperature calibration"],
        "disallowed_repairs": ["routing changes", "expert capacity changes", "Top2/Top4 execution"],
    },
    "PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP": {
        "inspect": ["correct_class_logit_delta", "incorrect_class_logit_delta_max", "delta_correct_minus_top_wrong", "incorrect_overamp_rate", "logit_norm"],
        "allowed_repairs": ["sparse_ce", "margin alignment", "wrong suppress", "logit norm penalty", "sparse_ce decay", "temperature calibration"],
        "disallowed_repairs": ["routing changes", "expert capacity changes", "Top2/Top4 execution"],
    },
    "PVR_EC_FAILURE_CALIBRATION_COLLAPSE": {
        "inspect": ["ECE_proxy", "calibration_proxy", "confidence_when_correct", "confidence_when_wrong", "high_confidence_failure_rate"],
        "allowed_repairs": ["posthoc temperature scaling", "logit norm medium", "sparse_ce decay", "entropy-based temperature diagnostic", "wrong suppress light"],
        "disallowed_repairs": ["capacity increase", "routing changes", "deployment promotion"],
    },
    "PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER": {
        "inspect": ["token_accuracy", "sequence_accuracy", "exact_match", "decision_token_help_rate", "final_token_loss_delta", "token_to_sequence_transfer_ratio"],
        "allowed_repairs": ["decision-token weighting", "final-token weighting", "sequence-level diagnostic loss", "readout diagnostic only"],
        "disallowed_repairs": ["assuming residual is useless", "adding Top2/Top4", "changing ownership map first"],
    },
    "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION": {
        "inspect": ["latency_p50", "latency_p95", "p95_p50_ratio", "memory_peak", "diagnostic_tensor_retention", "cuda_sync_count", "cpu_transfer_count", "temporary_tensor_alloc_estimate"],
        "allowed_repairs": ["separate diagnostic and inference paths", "disable sparse logit decomposition in inference timing", "preallocate tensors", "cache masks and ownership bias", "remove Python objects from measured forward", "CUDA events instead of global sync", "warmup per shape"],
        "disallowed_repairs": ["changing model math", "removing required expert execution", "changing output", "Top2/Top4"],
    },
    # Family preservation playbooks
    "PVR_EC_FAILURE_FAMILY_PRESERVATION_LOSS": {
        "inspect": ["family_preservation_score", "family_top1_oracle_gap", "expert_family_purity", "expert_family_coverage", "prototype_family_owner_consistency"],
        "allowed_repairs": ["family_preservation_bias_shadow_to_active", "family_overlap_replay_refresh", "compatible_mask_refinement", "ownership_map_refresh"],
        "disallowed_repairs": ["Top2/Top4 execution", "new router architecture", "runtime dynamic-K"],
    },
    "PVR_EC_FAILURE_OVERLAP_BOUNDARY_MISROUTE": {
        "inspect": ["overlap_preservation_score", "boundary_failure_rate", "family_margin", "family_membership_entropy"],
        "allowed_repairs": ["family_preservation_bias_shadow_to_active", "compatible_mask_refinement", "boundary_state_replay"],
        "disallowed_repairs": ["Top2/Top4 execution", "multi-expert execution"],
    },
    "PVR_EC_FAILURE_NOISY_REGION_OWNERSHIP": {
        "inspect": ["noisy_region_failure_rate", "owner_churn_by_prototype", "oracle_gap_noisy_region"],
        "allowed_repairs": ["ownership_map_refresh", "oracle_gap_replay", "owner_reliability_recalibration"],
        "disallowed_repairs": ["Top2/Top4 execution", "runtime dynamic-K"],
    },
    "PVR_EC_FAILURE_FAMILY_OWNER_CHURN": {
        "inspect": ["owner_churn_by_family", "owner_churn_by_prototype", "owner_churn_by_seed", "family_owner_stability_score"],
        "allowed_repairs": ["route_consistency_loss", "prototype_stabilization", "family_consistency_replay_labels"],
        "disallowed_repairs": ["Top2/Top4 execution", "forced owner freezing without evidence"],
    },
    "PVR_EC_FAILURE_PROTOTYPE_FAMILY_COLLAPSE": {
        "inspect": ["prototype_family_owner_consistency", "prototype_local_monopoly_rate", "expert_family_entropy", "family_top1_oracle_gap"],
        "allowed_repairs": ["family_balanced_sampling", "family_balanced_loss_light", "anti_monopoly_penalty"],
        "disallowed_repairs": ["Top2/Top4 execution", "forced diversity without evidence"],
    },
    "PVR_EC_FAILURE_BALANCE_BIAS_FAMILY_OVERRIDE": {
        "inspect": ["balance_bias_changed_owner_rate", "balance_bias_changed_family_score_delta", "semantic_family_margin_when_balance_flipped"],
        "allowed_repairs": ["semantic_family_margin_guard", "balance_bias_cap_reduction", "family_aware_balance_constraint"],
        "disallowed_repairs": ["disabling balance entirely", "Top2/Top4 execution"],
    },
    "PVR_EC_FAILURE_FAMILY_AWARE_ORACLE_GAP_HIGH": {
        "inspect": ["prototype_family_oracle_gap", "family_top1_oracle_gap", "challenger_family_win_rate"],
        "allowed_repairs": ["ownership_map_refresh", "family_preservation_bias", "challenger_evidence_distillation"],
        "disallowed_repairs": ["Top2/Top4 execution", "runtime oracle"],
    },
    "PVR_EC_FAILURE_NLP_CONTEXT_INSENSITIVE_ROUTING": {
        "inspect": ["same_token_different_context_owner_rate", "context_conditioned_loss_gap", "contextual_owner_stability"],
        "allowed_repairs": ["context_conditioned_prototype_features", "context_role_tags", "context_aware_owner_reliability"],
        "disallowed_repairs": ["Top2/Top4 execution", "new router architecture"],
    },
    "PVR_EC_FAILURE_NLP_LENGTH_GENERALIZATION_COLLAPSE": {
        "inspect": ["loss_by_seq_len", "owner_entropy_by_seq_len", "prototype_entropy_by_seq_len", "family_preservation_score_by_seq_len"],
        "allowed_repairs": ["length_balanced_training", "prototype_drift_control_by_length", "length_conditioned_family_preservation"],
        "disallowed_repairs": ["Top2/Top4 execution", "length-specific routing"],
    },
}


def _default_playbook(mode_id: str) -> dict[str, list[str]]:
    return {
        "inspect": ["loss_gap_vs_fixed", "accuracy_gap_vs_fixed", "calibration_gap", "runtime_purity_passed"],
        "allowed_repairs": ["bounded diagnostic-only repair", "repeatability replay", "slice-specific validation"],
        "disallowed_repairs": ["Top2/Top4 execution", "new routing architecture", "distillation", "quantization", "model size increase"],
    }


def failure_mode_registry() -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for mode_id in FAILURE_MODE_IDS:
        playbook = PLAYBOOKS.get(mode_id, _default_playbook(mode_id))
        name = mode_id.replace("PVR_EC_FAILURE_", "").replace("_", " ").title()
        registry[mode_id] = {
            "id": mode_id,
            "name": name,
            "description": f"PVR-EC-O failure mode: {name}.",
            "trigger_conditions": playbook["inspect"],
            "required_evidence": playbook["inspect"],
            "severity": "high" if mode_id != "PVR_EC_FAILURE_UNKNOWN" else "blocking",
            "repeatability_requirement": "replay known seed/family/shape before promotion or research expansion",
            "primary_metrics": playbook["inspect"][:3],
            "secondary_metrics": playbook["inspect"][3:],
            "allowed_repairs": playbook["allowed_repairs"],
            "disallowed_repairs": playbook["disallowed_repairs"],
            "promotion_impact": "blocks deployment until repaired or explicitly waived by deployment gate",
            "research_impact": "blocks research only if unknown, unreplayable, or forward purity is violated",
        }
    return registry


def repair_playbooks() -> dict[str, dict[str, list[str]]]:
    registry = failure_mode_registry()
    return {
        mode_id: {
            "inspect": list(mode["required_evidence"]),
            "allowed_repairs": list(mode["allowed_repairs"]),
            "disallowed_repairs": list(mode["disallowed_repairs"]),
        }
        for mode_id, mode in registry.items()
    }


def registry_report_payload() -> dict[str, Any]:
    registry = failure_mode_registry()
    return {
        "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
        "mode_count": len(registry),
        "required_fields": list(REQUIRED_FAILURE_MODE_FIELDS),
        "modes": deepcopy(registry),
    }
