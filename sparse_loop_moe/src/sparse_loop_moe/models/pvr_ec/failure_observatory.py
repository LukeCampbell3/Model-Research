"""Failure observatory event schema, assertions, and report helpers."""

from __future__ import annotations

import csv
import json
import platform
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from .failure_attribution import attribute_events, attribution_for_event
from .failure_registry import registry_report_payload
from .failure_repairs import repair_candidates_for_modes, validate_repair_result


FAILURE_EVENT_SCHEMA = (
    "run_id", "timestamp", "git_commit_if_available", "docker_image", "device", "seed", "family", "task", "shape",
    "batch_size", "seq_len", "model", "candidate_config", "ownership_map_version",
    "fixed_loss", "candidate_loss", "loss_gap_vs_fixed", "fixed_accuracy", "candidate_accuracy", "accuracy_gap_vs_fixed",
    "fixed_quality_per_ms", "candidate_quality_per_ms", "qpm_gap", "fixed_calibration", "candidate_calibration", "calibration_gap",
    "collapse_detected", "collapse_severity", "failure_mode_primary", "failure_mode_secondary", "failure_mode_confidence",
    "failure_is_repeatable", "failure_is_explained", "failure_is_repaired",
    "owner_entropy", "prototype_entropy", "owner_distribution", "prototype_distribution", "dead_expert_count",
    "expert_monopoly_rate", "prototype_local_monopoly_rate",
    "residual_help_rate", "residual_harm_rate", "decision_token_help_rate", "final_token_loss_delta", "token_to_sequence_transfer_ratio",
    "correct_class_logit_delta", "incorrect_class_logit_delta_max", "delta_correct_minus_top_wrong", "incorrect_overamp_rate",
    "logit_norm", "high_confidence_failure_rate",
    "shared_output_norm", "sparse_output_norm", "shared_sparse_ratio", "expert_delta_contribution_pct",
    "expert_grad_norm", "shared_grad_norm", "expert_grad_to_shared_grad_ratio",
    "owners_per_token", "Top2_executions", "Top4_executions", "oracle_owner_used", "forced_action_used",
    "replay_in_forward", "runtime_purity_passed",
    "latency_p50", "latency_p95", "latency_p99", "p95_p50_ratio", "memory_peak", "cuda_sync_count",
    "cpu_transfer_count", "file_write_count", "diagnostic_tensor_retention",
    "repair_candidate", "repair_allowed", "repair_result", "repair_validation_status", "notes",
    "tokenization_type", "vocab_size", "context_length", "sequence_length", "language_task_type", "exact_match",
    "token_accuracy", "sequence_accuracy", "calibration_by_length", "owner_entropy_by_length", "failure_mode_by_length",
)


def git_commit_if_available() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def blank_failure_event(**overrides: Any) -> dict[str, Any]:
    event = {field: "" for field in FAILURE_EVENT_SCHEMA}
    event.update({
        "timestamp": datetime.utcnow().isoformat(),
        "git_commit_if_available": git_commit_if_available(),
        "docker_image": "sparse-loop-moe-gpu",
        "device": "cuda" if "cuda" in str(overrides.get("device", "")) else overrides.get("device", ""),
        "owners_per_token": 1.0,
        "Top2_executions": 0.0,
        "Top4_executions": 0.0,
        "oracle_owner_used": False,
        "forced_action_used": False,
        "replay_in_forward": False,
        "runtime_purity_passed": True,
        "failure_is_repeatable": True,
        "failure_is_repaired": False,
        "tokenization_type": "symbolic",
        "language_task_type": "algorithmic",
    })
    event.update(overrides)
    return event


def _f(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return float(default)


def _has(event: dict[str, Any], key: str) -> bool:
    return event.get(key) not in {"", None}


def assertions_for_event(event: dict[str, Any]) -> list[str]:
    modes = []
    if not event.get("runtime_purity_passed", True) or _f(event.get("owners_per_token"), 1.0) != 1.0 or _f(event.get("Top2_executions")) > 0 or _f(event.get("Top4_executions")) > 0 or event.get("oracle_owner_used") or event.get("forced_action_used") or event.get("replay_in_forward") or _f(event.get("file_write_count")) > 0 or _f(event.get("cpu_transfer_count")) > 0:
        modes.append("PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION")
    if _f(event.get("loss_gap_vs_fixed")) > 0.10 or _f(event.get("accuracy_gap_vs_fixed")) < -0.05:
        modes.append("PVR_EC_FAILURE_BENCHMARK_FAMILY_SPECIFIC")
    if _f(event.get("candidate_calibration")) > 0.12 or _f(event.get("calibration_gap")) > 0.03 or _f(event.get("high_confidence_failure_rate")) > 0.05:
        modes.append("PVR_EC_FAILURE_CALIBRATION_COLLAPSE")
    if _f(event.get("incorrect_overamp_rate")) > 0.50 or _f(event.get("delta_correct_minus_top_wrong")) < -1.0:
        modes.append("PVR_EC_FAILURE_INCORRECT_LOGIT_OVERAMP")
    if (
        (_has(event, "owner_entropy") and _f(event.get("owner_entropy")) <= 0.01)
        or (_has(event, "prototype_entropy") and _f(event.get("prototype_entropy")) <= 0.01)
        or (_has(event, "dead_expert_count") and _f(event.get("dead_expert_count")) > 0)
        or (_has(event, "expert_monopoly_rate") and _f(event.get("expert_monopoly_rate")) > 0.85)
    ):
        modes.append("PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE")
    if _f(event.get("residual_help_rate")) >= 0.05 and (_f(event.get("token_to_sequence_transfer_ratio")) < 0.25 or _f(event.get("sequence_accuracy")) < 0.10):
        modes.append("PVR_EC_FAILURE_LOCAL_TO_GLOBAL_TRANSFER")
    if (
        (_has(event, "residual_help_rate") and _f(event.get("residual_help_rate")) < 0.05)
        or (_has(event, "residual_harm_rate") and _f(event.get("residual_harm_rate")) > 0.50)
        or (_has(event, "expert_delta_contribution_pct") and _f(event.get("expert_delta_contribution_pct")) < 0.01)
        or (_has(event, "expert_grad_norm") and _f(event.get("expert_grad_norm")) < 1e-8)
    ):
        modes.append("PVR_EC_FAILURE_SPARSE_RESIDUAL_UNHELPFUL")
    if _f(event.get("qpm_gap")) < 0 or _f(event.get("p95_p50_ratio"), 1.0) > 2.0 or event.get("diagnostic_tensor_retention"):
        modes.append("PVR_EC_FAILURE_QPM_SHAPE_REGRESSION")
    return sorted(set(modes))


def finalize_event(event: dict[str, Any]) -> dict[str, Any]:
    modes = assertions_for_event(event)
    attribution = attribution_for_event(event)
    primary = attribution["primary_failure_mode"]
    secondary = sorted(set(modes + attribution["secondary_failure_modes"]))
    if primary in secondary:
        secondary.remove(primary)
    event = {**blank_failure_event(), **event}
    event.update({
        "failure_mode_primary": primary,
        "failure_mode_secondary": secondary,
        "failure_mode_confidence": attribution["confidence_score"],
        "failure_is_explained": primary != "PVR_EC_FAILURE_UNKNOWN",
        "collapse_detected": bool(_f(event.get("loss_gap_vs_fixed")) > 0.10 or _f(event.get("accuracy_gap_vs_fixed")) < -0.05),
        "collapse_severity": max(_f(event.get("loss_gap_vs_fixed")), -_f(event.get("accuracy_gap_vs_fixed"))),
        "runtime_purity_passed": "PVR_EC_FAILURE_RUNTIME_PATH_POLLUTION" not in modes,
        "repair_allowed": attribution["recommended_repair_family"],
    })
    return event


def events_from_rows(rows: list[dict[str, Any]], *, run_id: str = "", seed: int | None = None, device: str = "") -> list[dict[str, Any]]:
    fixed_by_key = {}
    for row in rows:
        model = row.get("model_name") or row.get("model")
        if model == "fixed_moe_vectorized":
            key = (row.get("family"), row.get("task"), row.get("batch_size"), row.get("sequence_length", row.get("seq_len")))
            fixed_by_key[key] = row
    events = []
    for row in rows:
        model = row.get("model_name") or row.get("model")
        if model == "fixed_moe_vectorized":
            continue
        model_text = str(model or "")
        candidate_config = row.get("final_candidate_config", row.get("config_name", ""))
        if not candidate_config:
            if model_text.endswith("final_candidate_v1_1") or "final_candidate_v1_1" in model_text:
                candidate_config = "final_candidate_v1_1"
            elif model_text.endswith("final_candidate_v1") or "final_candidate_v1" in model_text:
                candidate_config = "final_candidate_v1"
        key = (row.get("family"), row.get("task"), row.get("batch_size"), row.get("sequence_length", row.get("seq_len")))
        fixed = fixed_by_key.get(key, {})
        fixed_loss = _f(fixed.get("loss"))
        cand_loss = _f(row.get("loss"))
        fixed_acc = _f(fixed.get("accuracy"))
        cand_acc = _f(row.get("accuracy"))
        fixed_qpm = _f(fixed.get("quality_per_ms", fixed.get("qpc")))
        cand_qpm = _f(row.get("quality_per_ms", row.get("qpc")))
        latency_p50 = _f(row.get("p50_latency_ms", row.get("latency_p50")))
        latency_p95 = _f(row.get("p95_latency_ms", row.get("latency_p95", latency_p50)))
        event = blank_failure_event(
            run_id=run_id,
            device=device,
            seed=row.get("seed", seed if seed is not None else ""),
            family=row.get("family", ""),
            task=row.get("task", ""),
            shape=f"b{row.get('batch_size', '')}-s{row.get('sequence_length', row.get('seq_len', ''))}" if row.get("batch_size") else row.get("shape", ""),
            batch_size=row.get("batch_size", ""),
            seq_len=row.get("sequence_length", row.get("seq_len", "")),
            model=model,
            candidate_config=candidate_config,
            ownership_map_version=row.get("ownership_map_mode", "frozen"),
            fixed_loss=fixed_loss,
            candidate_loss=cand_loss,
            loss_gap_vs_fixed=cand_loss - fixed_loss if fixed else row.get("loss_gap", 0.0),
            fixed_accuracy=fixed_acc,
            candidate_accuracy=cand_acc,
            accuracy_gap_vs_fixed=cand_acc - fixed_acc if fixed else row.get("accuracy_gap", 0.0),
            fixed_quality_per_ms=fixed_qpm,
            candidate_quality_per_ms=cand_qpm,
            qpm_gap=cand_qpm - fixed_qpm if fixed_qpm or cand_qpm else row.get("qpm_gap", 0.0),
            fixed_calibration=fixed.get("calibration_proxy", 0.0),
            candidate_calibration=row.get("calibration_proxy", 0.0),
            calibration_gap=_f(row.get("calibration_proxy")) - _f(fixed.get("calibration_proxy")),
            owner_entropy=row.get("pvr_route_entropy", row.get("owner_entropy", "")),
            prototype_entropy=row.get("prototype_owner_entropy", row.get("prototype_entropy", "")),
            owner_distribution=row.get("owner_distribution", ""),
            prototype_distribution=row.get("prototype_distribution", ""),
            dead_expert_count=row.get("dead_expert_count", ""),
            expert_monopoly_rate=row.get("expert_monopoly_rate", ""),
            prototype_local_monopoly_rate=row.get("prototype_local_monopoly_rate", ""),
            residual_help_rate=row.get("residual_help_rate", ""),
            residual_harm_rate=row.get("residual_harm_rate", ""),
            decision_token_help_rate=row.get("decision_token_help_rate", ""),
            final_token_loss_delta=row.get("final_token_loss_delta", ""),
            token_to_sequence_transfer_ratio=row.get("token_to_sequence_transfer_ratio", ""),
            correct_class_logit_delta=row.get("correct_class_logit_delta", 0.0),
            incorrect_class_logit_delta_max=row.get("incorrect_class_logit_delta_max", 0.0),
            delta_correct_minus_top_wrong=row.get("delta_correct_minus_top_wrong", 0.0),
            incorrect_overamp_rate=row.get("incorrect_logit_overamplification_rate", row.get("incorrect_overamp_rate", 0.0)),
            logit_norm=row.get("logit_norm", 0.0),
            high_confidence_failure_rate=row.get("high_confidence_failure_rate", 0.0),
            shared_output_norm=row.get("shared_output_norm", ""),
            sparse_output_norm=row.get("sparse_output_norm", ""),
            shared_sparse_ratio=row.get("shared_sparse_ratio", ""),
            expert_delta_contribution_pct=row.get("expert_delta_contribution_pct", ""),
            expert_grad_norm=row.get("expert_grad_norm", ""),
            shared_grad_norm=row.get("shared_grad_norm", ""),
            expert_grad_to_shared_grad_ratio=row.get("expert_grad_to_shared_grad_ratio", ""),
            owners_per_token=row.get("pvr_actual_owner_count_per_token", row.get("actual_owner_count_per_token", row.get("owner_count_per_token", 1.0))),
            Top2_executions=row.get("pvr_num_k2_tokens", row.get("Top2_executions", 0.0)),
            Top4_executions=row.get("pvr_num_k4_tokens", row.get("Top4_executions", 0.0)),
            oracle_owner_used=row.get("pvr_oracle_owner_used", False),
            forced_action_used=row.get("pvr_forced_action_path_used", False),
            replay_in_forward=row.get("pvr_replay_probe_labels_used", False),
            latency_p50=latency_p50,
            latency_p95=latency_p95,
            latency_p99=max(latency_p50, latency_p95),
            p95_p50_ratio=latency_p95 / max(latency_p50, 1e-8) if latency_p95 else 1.0,
            memory_peak=row.get("max_memory_allocated_mb", row.get("memory_peak", 0.0)),
            cuda_sync_count=row.get("cuda_sync_count", 0),
            cpu_transfer_count=row.get("cpu_transfer_count", 0),
            file_write_count=row.get("file_write_count", 0),
            diagnostic_tensor_retention=row.get("diagnostic_tensor_retention", False),
            repair_candidate=row.get("repair_variant", ""),
            exact_match=row.get("exact_match", 0.0),
            token_accuracy=row.get("accuracy", 0.0),
            sequence_accuracy=row.get("exact_match", 0.0),
            sequence_length=row.get("sequence_length", row.get("seq_len", "")),
            vocab_size=row.get("vocab_size", ""),
            context_length=row.get("context_length", row.get("sequence_length", "")),
        )
        events.append(finalize_event(event))
    return events


def write_events(output_dir: str | Path, events: list[dict[str, Any]]) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    json_path = out / "failure_observatory_events.json"
    csv_path = out / "failure_observatory_events.csv"
    json_path.write_text(json.dumps(events, indent=2, default=str), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(FAILURE_EVENT_SCHEMA), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(events)
    latest = Path("evaluation/benchmark_results/latest")
    if out.resolve() != latest.resolve():
        latest.mkdir(parents=True, exist_ok=True)
        (latest / json_path.name).write_text(json_path.read_text(encoding="utf-8"), encoding="utf-8")
        (latest / csv_path.name).write_text(csv_path.read_text(encoding="utf-8"), encoding="utf-8")


def scoreboard_payload(events: list[dict[str, Any]]) -> dict[str, Any]:
    by_mode: dict[str, dict[str, Any]] = {}
    for event in events:
        mode = event.get("failure_mode_primary") or "PVR_EC_FAILURE_UNKNOWN"
        item = by_mode.setdefault(mode, {
            "failure_mode": mode, "count": 0, "repeatable_count": 0, "unexplained_count": 0,
            "repaired_count": 0, "partial_repair_count": 0, "blocked_count": 0,
            "affected_seeds": set(), "affected_families": set(), "affected_tasks": set(), "affected_shapes": set(),
            "most_common_primary_metric": "loss_gap_vs_fixed", "current_status": "blocked",
            "recommended_next_action": "run bounded repair validation",
        })
        item["count"] += 1
        item["repeatable_count"] += int(bool(event.get("failure_is_repeatable", True)))
        item["unexplained_count"] += int(mode == "PVR_EC_FAILURE_UNKNOWN")
        item["repaired_count"] += int(bool(event.get("failure_is_repaired")))
        item["blocked_count"] += int(not bool(event.get("failure_is_repaired")))
        for field, target in [("seed", "affected_seeds"), ("family", "affected_families"), ("task", "affected_tasks"), ("shape", "affected_shapes")]:
            value = event.get(field)
            if value not in {"", None}:
                item[target].add(str(value))
    rows = []
    for item in by_mode.values():
        row = dict(item)
        for key in ["affected_seeds", "affected_families", "affected_tasks", "affected_shapes"]:
            row[key] = sorted(row[key])
        rows.append(row)
    return {"status": "PVR_EC_FAILURE_OBSERVATORY_READY", "mode_count": len(rows), "scoreboard": rows}


def trend_payload(events: list[dict[str, Any]], previous: dict[str, Any] | None = None) -> dict[str, Any]:
    previous = previous or {}
    collapse_count = sum(1 for e in events if e.get("collapse_detected"))
    qpm_pass_count = sum(1 for e in events if _f(e.get("qpm_gap")) >= 0)
    calibration_values = [_f(e.get("candidate_calibration")) for e in events if e.get("candidate_calibration") not in {"", None}]
    return {
        "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
        "failure_count": len(events),
        "failure_count_change": len(events) - int(previous.get("failure_count", len(events))),
        "collapse_count": collapse_count,
        "collapse_count_change": collapse_count - int(previous.get("collapse_count", collapse_count)),
        "calibration_mean": sum(calibration_values) / max(len(calibration_values), 1),
        "calibration_change": 0.0,
        "QPM_shape_pass_count": qpm_pass_count,
        "QPM_shape_pass_count_change": 0,
        "overamp_change": 0.0,
        "forward_purity_change": 0.0,
        "platform": platform.platform(),
    }


def observatory_gate_payload(events: list[dict[str, Any]]) -> dict[str, Any]:
    unknown_active = any(e.get("failure_mode_primary") == "PVR_EC_FAILURE_UNKNOWN" for e in events)
    forward_purity = all(bool(e.get("runtime_purity_passed", True)) for e in events)
    classified = all(bool(e.get("failure_is_explained")) for e in events)
    qpm_classified = all(
        e.get("failure_mode_primary") != "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION" or e.get("failure_is_explained")
        for e in events
    )
    research_allowed = forward_purity and classified and qpm_classified and not unknown_active
    deployment_ready = research_allowed and not any(e.get("collapse_detected") for e in events) and all(_f(e.get("qpm_gap")) >= 0 for e in events)
    return {
        "status": "PVR_EC_FAILURE_OBSERVATORY_READY" if research_allowed else "PVR_EC_FAILURE_OBSERVATORY_INCOMPLETE",
        "deployment_verdict": "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" if deployment_ready else "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
        "research_verdict": "PVR_EC_RESEARCH_EXPANSION_ALLOWED" if research_allowed else "PVR_EC_RESEARCH_EXPANSION_BLOCKED",
        "statuses": [
            "PVR_EC_FAILURE_OBSERVATORY_READY" if research_allowed else "PVR_EC_FAILURE_OBSERVATORY_INCOMPLETE",
            "PVR_EC_RESEARCH_EXPANSION_ALLOWED" if research_allowed else "PVR_EC_RESEARCH_EXPANSION_BLOCKED",
            "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED" if deployment_ready else "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
            "PVR_EC_DO_NOT_PROMOTE" if not deployment_ready else "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
        ],
        "forward_purity_passed": forward_purity,
        "unknown_failure_active": unknown_active,
        "all_failures_classified": classified,
        "qpm_issues_classified": qpm_classified,
        "event_count": len(events),
    }


def repair_validation_payload(events: list[dict[str, Any]], repair_candidates: list[str]) -> dict[str, Any]:
    rows = []
    for candidate in repair_candidates:
        result = validate_repair_result({
            "collapse_count_before": sum(1 for e in events if e.get("collapse_detected")),
            "collapse_count_after": sum(1 for e in events if e.get("collapse_detected")),
            "qpm_failed_before": sum(1 for e in events if _f(e.get("qpm_gap")) < 0),
            "qpm_failed_after": sum(1 for e in events if _f(e.get("qpm_gap")) < 0),
            "needs_more_evidence": True,
        })
        rows.append({"repair_candidate": candidate, "repair_result": result, "repair_validation_status": result})
    return {
        "status": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "passed": False,
        "repair_results": rows,
    }
