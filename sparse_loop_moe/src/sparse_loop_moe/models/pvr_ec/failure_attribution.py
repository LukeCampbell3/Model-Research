"""Rule-based failure attribution for PVR-EC-O observatory rows."""

from __future__ import annotations

from typing import Any

from .failure_registry import failure_mode_registry


def _f(row: dict[str, Any], key: str, default: float = 0.0) -> float:
    value = row.get(key, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def _has(row: dict[str, Any], key: str) -> bool:
    return row.get(key) not in {"", None}


def attribution_for_event(row: dict[str, Any]) -> dict[str, Any]:
    modes: list[str] = []
    evidence: dict[str, Any] = {}

    runtime_bad = (
        abs(_f(row, "owners_per_token", 1.0) - 1.0) > 1e-6
        or _f(row, "Top2_executions") > 0
        or _f(row, "Top4_executions") > 0
        or bool(row.get("oracle_owner_used"))
        or bool(row.get("forced_action_used"))
        or bool(row.get("replay_in_forward"))
        or _f(row, "file_write_count") > 0
        or _f(row, "cpu_transfer_count") > 0
        or bool(row.get("diagnostic_tensor_retention"))
    )
    if runtime_bad:
        modes.append("PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION")
        evidence["runtime_purity"] = False

    if (
        (_has(row, "owner_entropy") and _f(row, "owner_entropy") <= 0.01)
        or (_has(row, "prototype_entropy") and _f(row, "prototype_entropy") <= 0.01)
        or (_has(row, "dead_expert_count") and _f(row, "dead_expert_count") > 0)
        or (_has(row, "expert_monopoly_rate") and _f(row, "expert_monopoly_rate") > 0.85)
        or (_has(row, "prototype_local_monopoly_rate") and _f(row, "prototype_local_monopoly_rate") > 0.85)
    ):
        modes.append("PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE")
        evidence["owner_entropy"] = row.get("owner_entropy")
        evidence["prototype_entropy"] = row.get("prototype_entropy")

    if _f(row, "candidate_calibration") > _f(row, "calibration_threshold", 0.12) or _f(row, "calibration_gap") > _f(row, "calibration_gap_threshold", 0.03) or _f(row, "high_confidence_failure_rate") > 0.05:
        modes.append("PVR_EC_FAILURE_CALIBRATION_COLLAPSE")
        evidence["candidate_calibration"] = row.get("candidate_calibration")
        evidence["calibration_gap"] = row.get("calibration_gap")

    if _f(row, "incorrect_overamp_rate") > 0.50 or _f(row, "delta_correct_minus_top_wrong") < -1.0:
        modes.append("PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP")
        evidence["incorrect_overamp_rate"] = row.get("incorrect_overamp_rate")
        evidence["delta_correct_minus_top_wrong"] = row.get("delta_correct_minus_top_wrong")

    if (
        (_has(row, "residual_help_rate") and _f(row, "residual_help_rate") < 0.05)
        or (_has(row, "residual_harm_rate") and _f(row, "residual_harm_rate") > 0.50)
        or (_has(row, "expert_delta_contribution_pct") and _f(row, "expert_delta_contribution_pct") < 0.01)
        or (_has(row, "expert_grad_norm") and _f(row, "expert_grad_norm") < 1e-8)
    ):
        modes.append("PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL")
        evidence["residual_help_rate"] = row.get("residual_help_rate")
        evidence["expert_delta_contribution_pct"] = row.get("expert_delta_contribution_pct")

    if _f(row, "residual_help_rate") >= 0.05 and (_f(row, "token_to_sequence_transfer_ratio") < 0.25 or _f(row, "accuracy_gap_vs_fixed") < -0.05):
        modes.append("PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER")
        evidence["token_to_sequence_transfer_ratio"] = row.get("token_to_sequence_transfer_ratio")

    if _f(row, "loss_gap_vs_fixed") > 0.10 or _f(row, "accuracy_gap_vs_fixed") < -0.05:
        modes.append("PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC")
        evidence["loss_gap_vs_fixed"] = row.get("loss_gap_vs_fixed")
        evidence["accuracy_gap_vs_fixed"] = row.get("accuracy_gap_vs_fixed")

    if (_has(row, "fixed_accuracy") and _f(row, "fixed_accuracy") < 0.10) or (_has(row, "fixed_loss") and _f(row, "fixed_loss") > 1.0):
        modes.append("PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY")
        evidence["fixed_loss"] = row.get("fixed_loss")
        evidence["fixed_accuracy"] = row.get("fixed_accuracy")

    qpm_failed = _f(row, "qpm_gap") < 0 or _f(row, "p95_p50_ratio", 1.0) > 2.0 or _f(row, "memory_peak") > _f(row, "fixed_memory_peak", 1e18)
    if qpm_failed:
        modes.append("PVR_EC_FAILURE_QPM_SHAPE_REGRESSION")
        evidence["qpm_gap"] = row.get("qpm_gap")
        evidence["p95_p50_ratio"] = row.get("p95_p50_ratio")

    if _f(row, "shared_sparse_ratio") > 10.0 or (0 < _f(row, "shared_sparse_ratio") < 0.10):
        modes.append("PVR_EC_FAILURE_SHARED_SPARSE_IMBALANCE")
        evidence["shared_sparse_ratio"] = row.get("shared_sparse_ratio")

    modes = sorted(set(modes))
    if not modes:
        modes = ["PVR_EC_FAILURE_UNKNOWN"]
    registry = failure_mode_registry()
    primary = modes[0]
    if "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION" in modes:
        primary = "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION"
    elif "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION" in modes:
        primary = "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
    elif "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY" in modes:
        primary = "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY"
    elif "PVR_EC_FAILURE_CALIBRATION_COLLAPSE" in modes and "PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP" in modes:
        primary = "PVR_EC_FAILURE_CALIBRATION_COLLAPSE"
    elif "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE" in modes:
        primary = "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE"
    secondary = [m for m in modes if m != primary]
    playbook = registry.get(primary, registry["PVR_EC_FAILURE_UNKNOWN"])
    return {
        "primary_failure_mode": primary,
        "secondary_failure_modes": secondary,
        "confidence_score": 0.85 if primary != "PVR_EC_FAILURE_UNKNOWN" else 0.25,
        "evidence_bundle": evidence,
        "recommended_repair_family": playbook.get("allowed_repairs", []),
        "disallowed_repair_family": playbook.get("disallowed_repairs", []),
        "research_expansion_allowed": primary != "PVR_EC_FAILURE_UNKNOWN" and primary != "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION",
    }


def attribute_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for event in events:
        attribution = attribution_for_event(event)
        item = dict(event)
        item.update({
            "failure_mode_primary": attribution["primary_failure_mode"],
            "failure_mode_secondary": attribution["secondary_failure_modes"],
            "failure_mode_confidence": attribution["confidence_score"],
            "failure_is_explained": attribution["primary_failure_mode"] != "PVR_EC_FAILURE_UNKNOWN",
        })
        item["attribution"] = attribution
        out.append(item)
    return out
