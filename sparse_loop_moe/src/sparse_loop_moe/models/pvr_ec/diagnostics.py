"""PVR-EC diagnostic utilities for sparse-dispatch and speculative routing.

This module intentionally stays lightweight: formulaic mergeability, shadow
branch-ticket packets, execution-mode constants, and report skeleton writers.
It does not launch hard runtime branches.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
import math
from pathlib import Path
from typing import Any

import torch


EXECUTION_MODES = {
    "dense_all_experts",
    "fixed_top2_all_experts_masked",
    "fixed_top2_pack_by_expert",
    "variable_k_pack_by_expert",
    "hybrid_expert_choice_bucketed",
}

DEPLOY_MODES = {
    "off",
    "top1",
    "top2",
    "bucketed",
    "dense_masked_control",
}

EXPERT_TYPES = {
    "shared_base_only",
    "delta_rank_small",
    "delta_rank_medium",
    "delta_rank_large",
    "full_expert_ffn",
}

K_ALLOWED = (1, 2, 4)

PVR_EC_STATUSES = (
    "PVR_EC_SPARSE_DISPATCH_BOTTLENECK",
    "PVR_EC_DENSE_ALL_EXPERTS_FASTER",
    "PVR_EC_FIXED_TOP2_FASTER_THAN_VARIABLE_K",
    "PVR_EC_DELTA_TOO_SMALL_TO_AMORTIZE_DISPATCH",
    "PVR_EC_SPARSE_DISPATCH_PREMATURE",
    "PVR_EC_DENSE_TRAINING_RECOMMENDED",
    "PVR_EC_READY_FOR_SPARSE_EFFICIENCY_PHASE",
    "PVR_EC_TRAINING_GRADIENT_SPARSITY_BOTTLENECK",
    "PVR_EC_FORWARD_DISPATCH_ACCEPTABLE_BACKWARD_EXPENSIVE",
    "PVR_EC_ASSIGNMENT_BUDGET_DRIFT",
    "PVR_EC_SPARSE_TRANSITION_NOT_SOLVED",
    "PVR_EC_SPECULATIVE_ROUTER_ENABLED",
    "PVR_EC_SOFT_SPECULATION_ONLY",
    "PVR_EC_BRANCH_TICKETS_SHADOW_ONLY",
    "PVR_EC_RUNTIME_BRANCHING_DISABLED",
    "PVR_EC_RUNTIME_BRANCHING_GATED",
    "PVR_EC_SPECULATION_OVERUSED",
    "PVR_EC_SPECULATION_UNDERUSED",
    "PVR_EC_HARD_BRANCHING_NOT_READY",
    "PVR_EC_FORMULAIC_MERGEABILITY_ENABLED",
    "PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE",
    "PVR_EC_MERGEABILITY_FORMULA_ACTIVE",
    "PVR_EC_MERGEABILITY_REPLAY_LEARNING_ENABLED",
    "PVR_EC_MERGEABILITY_CALIBRATION_POOR",
    "PVR_EC_MERGEABILITY_CALIBRATED",
    "PVR_EC_MERGEABILITY_TOO_PERMISSIVE",
    "PVR_EC_MERGEABILITY_TOO_CONSERVATIVE",
    # Ownership map statuses
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
)


@dataclass
class MergeabilityWeights:
    """Scalar weights for the formulaic mergeability score."""

    w_c: float = 1.4
    w_g: float = 1.0
    w_s: float = 0.8
    w_e: float = 0.8
    w_d: float = 1.2
    w_r: float = 1.5
    b: float = -1.0

    def update_from_replay(
        self,
        *,
        y: float,
        score: float,
        p1: float,
        p2: float,
        selected_mass: float,
        entropy: float,
        disagreement: float,
        risk: float,
        learning_rate: float = 0.01,
    ) -> dict[str, float]:
        """Apply one scalar replay update and return the deltas."""

        error = y - score
        deltas = {
            "w_c": learning_rate * error * p1,
            "w_g": learning_rate * error * (p1 - p2),
            "w_s": learning_rate * error * selected_mass,
            "w_e": learning_rate * error * (1.0 - entropy),
            "w_d": -learning_rate * error * disagreement,
            "w_r": -learning_rate * error * risk,
            "b": learning_rate * error,
        }
        self.w_c += deltas["w_c"]
        self.w_g += deltas["w_g"]
        self.w_s += deltas["w_s"]
        self.w_e += deltas["w_e"]
        self.w_d += deltas["w_d"]
        self.w_r += deltas["w_r"]
        self.b += deltas["b"]
        return deltas


@dataclass
class MergeabilityState:
    """Shadow-mode mergeability calibration state."""

    initial_weights: MergeabilityWeights = field(default_factory=MergeabilityWeights)
    current_weights: MergeabilityWeights = field(default_factory=MergeabilityWeights)
    number_of_replay_updates: int = 0
    learning_rate: float = 0.01
    weight_update_history: list[dict[str, float]] = field(default_factory=list)
    replay_labels: list[float] = field(default_factory=list)
    active_or_shadow_mode: str = "shadow"

    def record_replay_update(self, features: dict[str, float], y: float) -> dict[str, float]:
        deltas = self.current_weights.update_from_replay(
            y=y,
            learning_rate=self.learning_rate,
            **features,
        )
        self.number_of_replay_updates += 1
        self.replay_labels.append(float(y))
        self.weight_update_history.append(deltas)
        return deltas


def _second_top(probs: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    top_vals = probs.topk(min(2, probs.shape[-1]), dim=-1).values
    p1 = top_vals[:, 0]
    p2 = top_vals[:, 1] if top_vals.shape[1] > 1 else torch.zeros_like(p1)
    return p1, p2


def selected_mass(probs: torch.Tensor, selected_mask: torch.Tensor) -> torch.Tensor:
    return (probs * selected_mask.to(probs.dtype)).sum(dim=-1)


def normalized_entropy(probs: torch.Tensor) -> torch.Tensor:
    entropy = -(probs * torch.log(probs + 1e-8)).sum(dim=-1)
    max_entropy = math.log(max(probs.shape[-1], 2))
    return entropy / (max_entropy + 1e-8)


def pre_expert_mergeability(
    probs: torch.Tensor,
    selected_mask: torch.Tensor,
    risk: torch.Tensor | float = 0.0,
    weights: MergeabilityWeights | None = None,
) -> torch.Tensor:
    """Cheap pre-expert mergeability score in [0, 1]."""

    weights = weights or MergeabilityWeights()
    risk_t = torch.as_tensor(risk, device=probs.device, dtype=probs.dtype)
    if risk_t.ndim == 0:
        risk_t = risk_t.expand(probs.shape[0])
    p1, p2 = _second_top(probs)
    s_i = selected_mass(probs, selected_mask)
    h_i = normalized_entropy(probs)
    logits = (
        weights.w_c * p1
        + weights.w_g * (p1 - p2)
        + weights.w_s * s_i
        + weights.w_e * (1.0 - h_i)
        - weights.w_r * risk_t
        + weights.b
    )
    return torch.sigmoid(logits)


def expert_disagreement(expert_outputs: torch.Tensor, primary_index: int = 0) -> torch.Tensor:
    """Mean normalized disagreement from the primary output.

    Args:
        expert_outputs: [N, K, d_model]
    """

    if expert_outputs.shape[1] <= 1:
        return torch.zeros(expert_outputs.shape[0], device=expert_outputs.device)
    primary = expert_outputs[:, primary_index, :]
    diff = torch.linalg.norm(expert_outputs - primary.unsqueeze(1), dim=-1).mean(dim=-1)
    denom = torch.linalg.norm(primary, dim=-1) + 1e-8
    return diff / denom


def post_expert_mergeability(
    probs: torch.Tensor,
    selected_mask: torch.Tensor,
    disagreement: torch.Tensor,
    risk: torch.Tensor | float = 0.0,
    weights: MergeabilityWeights | None = None,
) -> torch.Tensor:
    """Full post-expert mergeability score in [0, 1]."""

    weights = weights or MergeabilityWeights()
    risk_t = torch.as_tensor(risk, device=probs.device, dtype=probs.dtype)
    if risk_t.ndim == 0:
        risk_t = risk_t.expand(probs.shape[0])
    p1, p2 = _second_top(probs)
    s_i = selected_mass(probs, selected_mask)
    h_i = normalized_entropy(probs)
    logits = (
        weights.w_c * p1
        + weights.w_g * (p1 - p2)
        + weights.w_s * s_i
        + weights.w_e * (1.0 - h_i)
        - weights.w_d * disagreement
        - weights.w_r * risk_t
        + weights.b
    )
    return torch.sigmoid(logits)


def choose_merge_type(score: float) -> str:
    if score >= 0.75:
        return "weighted_hidden_merge"
    if score >= 0.45:
        return "residual_merge"
    if score >= 0.25:
        return "delayed_merge"
    return "hard_branch_candidate"


def weighted_hidden_merge(expert_outputs: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
    """Weighted soft merge preserving [N, d_model] shape."""

    norm = weights / (weights.sum(dim=-1, keepdim=True) + 1e-8)
    return (expert_outputs * norm.unsqueeze(-1)).sum(dim=1)


def residual_merge(
    primary_output: torch.Tensor,
    auxiliary_delta: torch.Tensor,
    alpha: float | torch.Tensor = 0.25,
) -> torch.Tensor:
    """Residual merge that preserves primary owner contribution."""

    return primary_output + alpha * auxiliary_delta


REQUIRED_BRANCH_TICKET_FIELDS = (
    "state_id",
    "primary_expert",
    "selected_experts",
    "k",
    "uncertainty",
    "mergeability_score",
    "branch_value",
    "affinity",
    "state_impact",
    "prototype_ids",
    "prototype_distance",
    "difficulty_bucket",
    "speculation_mode",
    "merge_type",
    "budget_class",
    "runtime_branch_recommended",
    "reason_codes",
)


def make_branch_ticket(
    *,
    state_id: int,
    primary_expert: int,
    selected_experts: list[int],
    uncertainty: float,
    mergeability_score: float,
    branch_value: float,
    affinity: list[float],
    prototype_ids: list[int],
    prototype_distance: float,
    difficulty_bucket: str,
    merge_type: str,
    reason_codes: list[str] | None = None,
) -> dict[str, Any]:
    """Build a shadow-only branch ticket packet."""

    ticket = {
        "state_id": state_id,
        "primary_expert": primary_expert,
        "selected_experts": selected_experts,
        "k": len(selected_experts),
        "uncertainty": uncertainty,
        "mergeability_score": mergeability_score,
        "branch_value": branch_value,
        "affinity": affinity,
        "state_impact": 0.0,
        "prototype_ids": prototype_ids,
        "prototype_distance": prototype_distance,
        "difficulty_bucket": difficulty_bucket,
        "speculation_mode": "soft_shadow",
        "merge_type": merge_type,
        "budget_class": "bounded_k",
        "runtime_branch_recommended": False,
        "reason_codes": reason_codes or ["PVR_EC_BRANCH_TICKETS_SHADOW_ONLY"],
    }
    missing = set(REQUIRED_BRANCH_TICKET_FIELDS) - set(ticket)
    if missing:
        raise ValueError(f"Branch ticket missing fields: {sorted(missing)}")
    return ticket


def empty_report(status: str = "PARTIAL_PVR_EC_DIAGNOSTIC_IMPLEMENTATION") -> dict[str, Any]:
    return {
        "status": status,
        "statuses": list(PVR_EC_STATUSES),
        "execution_modes": sorted(EXECUTION_MODES),
        "deploy_modes": sorted(DEPLOY_MODES),
        "expert_types": sorted(EXPERT_TYPES),
        "hard_runtime_branching": "disabled",
        "branch_tickets": "shadow_only",
    }


def _numeric_mean(records: list[dict[str, Any]], key: str) -> float:
    values = [float(r[key]) for r in records if isinstance(r.get(key), (int, float))]
    return sum(values) / max(len(values), 1)


def _numeric_sum(records: list[dict[str, Any]], key: str) -> float:
    return sum(float(r[key]) for r in records if isinstance(r.get(key), (int, float)))


def _pvr_records(payload: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not payload:
        return []
    return [
        r for r in payload.get("pvr_eval_records", [])
        if r.get("model_name") == "pvr_ec" or r.get("pvr_execution_mode")
    ]


def _fixed_records(payload: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not payload:
        return []
    return [r for r in payload.get("pvr_eval_records", []) if r.get("model_name") == "fixed_moe"]


def _group_by(records: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        groups.setdefault(str(record.get(key, "")), []).append(record)
    return groups


def _quality_per_ms(record: dict[str, Any]) -> float:
    inference_ms = float(record.get("inference_time_s", 0.0)) * 1000.0
    return float(record.get("accuracy", 0.0)) / max(inference_ms, 1e-8)


def _derive_statuses(pvr_records: list[dict[str, Any]]) -> list[str]:
    statuses = [
        "PVR_EC_SOFT_SPECULATION_ONLY",
        "PVR_EC_BRANCH_TICKETS_SHADOW_ONLY",
        "PVR_EC_RUNTIME_BRANCHING_DISABLED",
        "PVR_EC_FORMULAIC_MERGEABILITY_ENABLED",
        "PVR_EC_MERGEABILITY_FORMULA_SHADOW_MODE",
    ]
    if not pvr_records:
        statuses.append("PVR_EC_SPARSE_TRANSITION_NOT_SOLVED")
        return statuses

    dispatch = _numeric_mean(pvr_records, "pvr_dispatch_overhead_ratio")
    compute_to_dispatch = _numeric_mean(pvr_records, "pvr_compute_to_dispatch_ratio")
    expert_compute = _numeric_mean(pvr_records, "pvr_expert_compute_time_ms")
    pack_scatter = _numeric_mean(pvr_records, "pvr_pack_time_ms") + _numeric_mean(
        pvr_records, "pvr_scatter_time_ms"
    )
    drift = abs(_numeric_mean(pvr_records, "pvr_assignment_budget_drift"))

    if dispatch > 0.30:
        statuses.append("PVR_EC_SPARSE_DISPATCH_BOTTLENECK")
    if compute_to_dispatch < 1.0 or expert_compute < pack_scatter:
        statuses.append("PVR_EC_SPARSE_DISPATCH_PREMATURE")
    if drift > 0.10:
        statuses.append("PVR_EC_ASSIGNMENT_BUDGET_DRIFT")
    if _numeric_mean(pvr_records, "pvr_backward_dispatch_overhead_ratio") > 0.30:
        statuses.append("PVR_EC_FORWARD_DISPATCH_ACCEPTABLE_BACKWARD_EXPENSIVE")
    if "hybrid_expert_choice_bucketed" in {
        str(r.get("pvr_execution_mode", "")) for r in pvr_records
    }:
        statuses.append("PVR_EC_SPECULATIVE_ROUTER_ENABLED")

    statuses.append("PVR_EC_SPARSE_TRANSITION_NOT_SOLVED")
    return list(dict.fromkeys(statuses))


def _sparse_dispatch_report(base: dict[str, Any], pvr_records: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        **base,
        "record_count": len(pvr_records),
        "metrics": {
            "total_step_time_ms": _numeric_mean(pvr_records, "pvr_total_step_time_ms"),
            "router_score_time_ms": _numeric_mean(pvr_records, "pvr_router_score_time_ms"),
            "assignment_build_time_ms": _numeric_mean(pvr_records, "pvr_assignment_build_time_ms"),
            "pack_time_ms": _numeric_mean(pvr_records, "pvr_pack_time_ms"),
            "expert_compute_time_ms": _numeric_mean(pvr_records, "pvr_expert_compute_time_ms"),
            "scatter_time_ms": _numeric_mean(pvr_records, "pvr_scatter_time_ms"),
            "tokens_per_second": _numeric_mean(pvr_records, "pvr_tokens_per_second"),
            "dispatch_overhead_ratio": _numeric_mean(pvr_records, "pvr_dispatch_overhead_ratio"),
            "compute_to_dispatch_ratio": _numeric_mean(pvr_records, "pvr_compute_to_dispatch_ratio"),
            "forward_dispatch_overhead_ratio": _numeric_mean(
                pvr_records, "pvr_forward_dispatch_overhead_ratio"
            ),
            "backward_dispatch_overhead_ratio": _numeric_mean(
                pvr_records, "pvr_backward_dispatch_overhead_ratio"
            ),
            "training_compute_to_dispatch_ratio": _numeric_mean(
                pvr_records, "pvr_training_compute_to_dispatch_ratio"
            ),
            "avg_tokens_per_active_expert": _numeric_mean(
                pvr_records, "pvr_avg_tokens_per_active_expert"
            ),
            "small_expert_batch_rate": _numeric_mean(pvr_records, "pvr_small_expert_batch_rate"),
            "actual_avg_k": _numeric_mean(pvr_records, "pvr_actual_avg_k"),
            "route_entropy": _numeric_mean(pvr_records, "pvr_route_entropy"),
            "expert_load_cv": _numeric_mean(pvr_records, "pvr_expert_load_cv"),
        },
    }


def _mode_report(pvr_records: list[dict[str, Any]], fixed_records: list[dict[str, Any]]) -> dict[str, Any]:
    fixed_by_task = {r.get("task"): r for r in fixed_records}
    by_mode = {}
    for mode, records in _group_by(pvr_records, "pvr_execution_mode").items():
        fixed_matches = [fixed_by_task[r.get("task")] for r in records if r.get("task") in fixed_by_task]
        avg_quality_per_ms = sum(_quality_per_ms(r) for r in records) / max(len(records), 1)
        fixed_quality_per_ms = sum(_quality_per_ms(r) for r in fixed_matches) / max(len(fixed_matches), 1)
        by_mode[mode] = {
            "record_count": len(records),
            "avg_accuracy": _numeric_mean(records, "accuracy"),
            "avg_loss": _numeric_mean(records, "loss"),
            "avg_qpc": _numeric_mean(records, "qpc"),
            "quality_per_ms": avg_quality_per_ms,
            "fixed_moe_quality_per_ms": fixed_quality_per_ms,
            "quality_per_ms_ratio_vs_fixed_moe": avg_quality_per_ms / max(fixed_quality_per_ms, 1e-8),
            "avg_training_time_s": _numeric_mean(records, "training_time_s"),
            "avg_inference_time_s": _numeric_mean(records, "inference_time_s"),
            "dispatch_overhead_ratio": _numeric_mean(records, "pvr_dispatch_overhead_ratio"),
            "compute_to_dispatch_ratio": _numeric_mean(records, "pvr_compute_to_dispatch_ratio"),
            "actual_avg_k": _numeric_mean(records, "pvr_actual_avg_k"),
            "assignment_budget_drift": _numeric_mean(records, "pvr_assignment_budget_drift"),
        }
    return by_mode


def _hybrid_report(base: dict[str, Any], pvr_records: list[dict[str, Any]]) -> dict[str, Any]:
    hybrid = [
        r for r in pvr_records
        if r.get("pvr_execution_mode") == "hybrid_expert_choice_bucketed"
    ]
    records = hybrid or pvr_records
    total_k = (
        _numeric_sum(records, "pvr_num_k1_tokens")
        + _numeric_sum(records, "pvr_num_k2_tokens")
        + _numeric_sum(records, "pvr_num_k4_tokens")
    )
    return {
        **base,
        "record_count": len(records),
        "K_distribution": {
            "k1": _numeric_sum(records, "pvr_num_k1_tokens"),
            "k2": _numeric_sum(records, "pvr_num_k2_tokens"),
            "k4": _numeric_sum(records, "pvr_num_k4_tokens"),
            "total_bucketed_tokens": total_k,
        },
        "avg_K": _numeric_mean(records, "pvr_actual_avg_k"),
        "target_avg_K": _numeric_mean(records, "pvr_target_avg_k"),
        "actual_avg_k": _numeric_mean(records, "pvr_actual_avg_k"),
        "assignment_budget_drift": _numeric_mean(records, "pvr_assignment_budget_drift"),
        "expert_utilization": _numeric_mean(records, "pvr_expert_utilization"),
        "expert_load_cv": _numeric_mean(records, "pvr_expert_load_cv"),
        "soft_branch_gain": None,
        "top2_gain_over_top1": None,
        "top4_gain_over_top1": None,
        "quality_per_branch_compute": None,
    }


def _mergeability_report(base: dict[str, Any], pvr_records: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        **base,
        "current_weights": asdict(MergeabilityWeights()),
        "initial_weights": asdict(MergeabilityWeights()),
        "number_of_replay_updates": 0,
        "learning_rate": 0.01,
        "mergeability_score_distribution": {
            "mean": _numeric_mean(pvr_records, "pvr_mergeability_score_mean"),
            "std": _numeric_mean(pvr_records, "pvr_mergeability_score_std"),
        },
        "merge_success_by_bucket": {},
        "merge_failure_by_bucket": {},
        "calibration_error": None,
        "weight_update_history": [],
        "active_or_shadow_mode": "shadow",
        "expert_disagreement_mean": _numeric_mean(pvr_records, "pvr_expert_disagreement_mean"),
    }


def write_diagnostic_reports(output_dir: str | Path, payload: dict[str, Any] | None = None) -> dict[str, Path]:
    """Write required MVP report files with explicit partial/complete status."""

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    base = empty_report()
    if payload:
        base.update(payload)
    pvr_eval_records = _pvr_records(payload)
    fixed_eval_records = _fixed_records(payload)
    base["statuses"] = _derive_statuses(pvr_eval_records)
    mode_summary = _mode_report(pvr_eval_records, fixed_eval_records)

    reports = {
        "pvr_ec_sparse_dispatch_ablation_report.json": {
            **_sparse_dispatch_report(base, pvr_eval_records),
            "mode_summary": mode_summary,
        },
        "dispatch_timing_report.json": _sparse_dispatch_report(base, pvr_eval_records),
        "expert_type_ablation_report.json": {
            **base,
            "by_expert_type": _group_by(pvr_eval_records, "pvr_expert_type"),
        },
        "hybrid_router_report.json": _hybrid_report(base, pvr_eval_records),
        "mergeability_formula_report.json": _mergeability_report(base, pvr_eval_records),
        "soft_vs_hard_speculation_report.json": {
            **base,
            "soft_speculation_only": True,
            "hard_runtime_branching_enabled": False,
            "branch_ticket_count": _numeric_sum(pvr_eval_records, "pvr_branch_ticket_count"),
            "runtime_branch_recommended_count": 0,
        },
        "branch_ticket_shadow_report.json": {
            **base,
            "branch_ticket_count": _numeric_sum(pvr_eval_records, "pvr_branch_ticket_count"),
            "runtime_branch_recommended_default": False,
            "shadow_only": True,
        },
    }
    paths: dict[str, Path] = {}
    for filename, data in reports.items():
        path = out / filename
        path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        paths[filename] = path

    md_path = out / "pvr_ec_sparse_dispatch_ablation_report.md"
    md_path.write_text(
        "\n".join(
            [
                "# PVR-EC Sparse Dispatch Ablation Report",
                "",
                f"**Status:** {base['status']}",
                f"**Statuses:** {', '.join(base['statuses'])}",
                "",
                "Hard runtime branching is disabled. Branch tickets are shadow-only.",
                "",
                "## Mode Summary",
                "",
                json.dumps(mode_summary, indent=2, default=str),
            ]
        ),
        encoding="utf-8",
    )
    paths[md_path.name] = md_path
    return paths
