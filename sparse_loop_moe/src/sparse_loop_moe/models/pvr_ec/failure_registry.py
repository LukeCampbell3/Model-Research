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
