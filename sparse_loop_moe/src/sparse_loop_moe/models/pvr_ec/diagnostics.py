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
        "expert_types": sorted(EXPERT_TYPES),
        "hard_runtime_branching": "disabled",
        "branch_tickets": "shadow_only",
    }


def write_diagnostic_reports(output_dir: str | Path, payload: dict[str, Any] | None = None) -> dict[str, Path]:
    """Write required MVP report files with explicit partial/complete status."""

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    base = empty_report()
    if payload:
        base.update(payload)

    reports = {
        "pvr_ec_sparse_dispatch_ablation_report.json": base,
        "dispatch_timing_report.json": base,
        "expert_type_ablation_report.json": base,
        "hybrid_router_report.json": base,
        "mergeability_formula_report.json": {
            **base,
            "current_weights": asdict(MergeabilityWeights()),
            "initial_weights": asdict(MergeabilityWeights()),
            "number_of_replay_updates": 0,
            "learning_rate": 0.01,
            "mergeability_score_distribution": {},
            "merge_success_by_bucket": {},
            "merge_failure_by_bucket": {},
            "calibration_error": None,
            "weight_update_history": [],
            "active_or_shadow_mode": "shadow",
        },
        "soft_vs_hard_speculation_report.json": base,
        "branch_ticket_shadow_report.json": base,
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
                "",
                "Hard runtime branching is disabled. Branch tickets are shadow-only.",
            ]
        ),
        encoding="utf-8",
    )
    paths[md_path.name] = md_path
    return paths
