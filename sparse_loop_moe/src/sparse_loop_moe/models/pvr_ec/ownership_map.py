"""PVR-EC Ownership Map: Candidate Recall Expansion + Calibration.

Core thesis: Better ownership surfaces make greedy Top-1 better.
The ownership map should act more often when it is likely correct.

This module implements:
- Candidate owner generation from multiple sources
- Candidate scoring with oracle/replay evidence
- Ownership bias calibration sweeps
- Semantic-margin guarded ownership bias
- Candidate map refresh (offline-only)
- Promotion gate with explicit reason codes
- Failure decomposition (recall vs scoring vs capacity)
- Multi-seed confirmation aggregation

Non-negotiable rules:
- Deployment executes exactly one owner (Top-1)
- Top2/Top4 are NOT production execution paths
- No Python loops, .item(), .cpu(), .numpy(), CUDA sync on hot path
- Ownership bias must not overpower semantic routing (margin guard)
- Promotion requires repeated multi-seed evidence
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

import torch
import torch.nn.functional as F


# =============================================================================
# Configuration
# =============================================================================


@dataclass
class OwnershipMapConfig:
    """Configuration for ownership map candidate expansion and calibration."""

    # Candidate set size: C ∈ {2, 4, 6, 8}
    candidate_set_size: int = 4

    # Ownership bias parameters
    ownership_weight: float = 0.25
    ownership_bias_cap: float = 0.25
    failure_bias_weight: float = 1.0
    stale_penalty_weight: float = 0.5
    balance_weight: float = 0.0  # Start at 0 to isolate ownership effects

    # Semantic margin guard
    semantic_margin_guard: float = 0.10

    # Owner-change target bands
    early_calibration_owner_change_rate_min: float = 0.02
    early_calibration_owner_change_rate_max: float = 0.08
    candidate_exploration_owner_change_rate_min: float = 0.05
    candidate_exploration_owner_change_rate_max: float = 0.12

    # Minimum sample protection
    min_ownership_samples: int = 32

    # Promotion gate thresholds
    min_loss_improvement: float = 0.01
    min_oracle_gap_improvement: float = 0.005
    owner_changed_success_threshold: float = 0.70
    high_confidence_failure_tolerance: float = 0.02
    prototype_monopoly_tolerance: float = 0.05
    latency_multiplier_limit: float = 1.25

    # Sweep ranges
    ownership_weight_sweep: tuple[float, ...] = (0.1, 0.25, 0.5, 0.75, 1.0)
    ownership_bias_cap_sweep: tuple[float, ...] = (0.1, 0.25, 0.5, 0.75)
    failure_bias_weight_sweep: tuple[float, ...] = (0.5, 1.0, 1.5)
    semantic_margin_guard_sweep: tuple[float, ...] = (0.05, 0.10, 0.20, 0.35)
    candidate_set_size_sweep: tuple[int, ...] = (2, 4, 6, 8)


# =============================================================================
# Statuses
# =============================================================================

PVR_EC_OWNERSHIP_STATUSES = (
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


# =============================================================================
# Promotion Gate Reason Codes
# =============================================================================

PROMOTION_REASON_CODES = (
    "LOSS_REGRESSION",
    "ORACLE_GAP_REGRESSION",
    "QUALITY_PER_MS_REGRESSION",
    "LATENCY_REGRESSION",
    "OWNER_CHANGE_SUCCESS_TOO_LOW",
    "CANDIDATE_RECALL_TOO_LOW",
    "HIGH_CONFIDENCE_FAILURE_INCREASE",
    "PROTOTYPE_MONOPOLY_INCREASE",
    "CANARY_NOT_REPRODUCED",
    "FROZEN_CANDIDATE_NOT_REPRODUCED",
    "SEED_REPEATABILITY_FAILED",
    "MAP_COMPATIBILITY_FAILED",
    "OWNER_CHANGE_TOO_RARE",
    "OWNERSHIP_BIAS_TOO_AGGRESSIVE",
    "OWNERSHIP_BIAS_TOO_WEAK",
)


# =============================================================================
# Candidate Generation Sources
# =============================================================================

CANDIDATE_SOURCES = (
    "current_owner",
    "score_challenger",
    "nearest_prototype_primary_owners",
    "nearest_prototype_backup_owners",
    "replay_oracle_winners",
    "replay_oracle_runners_up",
    "underused_compatible_owners_with_oracle_wins",
    "rare_expert_unique_utility_owners",
    "historically_successful_low_confidence_owners",
    "prototype_local_auxiliary_winners",
)


# =============================================================================
# Candidate Owner Scoring
# =============================================================================


@dataclass
class CandidateScore:
    """Score components for a candidate owner of a prototype."""

    prototype_id: int
    expert_id: int
    oracle_win_rate: float = 0.0
    replay_loss_improvement: float = 0.0
    reliability_bias: float = 0.0
    failure_rate: float = 0.0
    rare_utility_bonus: float = 0.0
    underused_compatible_bonus: float = 0.0
    monopoly_penalty: float = 0.0
    stale_owner_penalty: float = 0.0
    source: str = "current_owner"

    @property
    def total_score(self) -> float:
        return (
            self.oracle_win_rate
            + self.replay_loss_improvement
            + self.reliability_bias
            - self.failure_rate
            + self.rare_utility_bonus
            + self.underused_compatible_bonus
            - self.monopoly_penalty
            - self.stale_owner_penalty
        )


# =============================================================================
# Ownership Map State
# =============================================================================


@dataclass
class OwnershipMapState:
    """Persistent ownership map state for offline refresh."""

    num_prototypes: int = 16
    num_experts: int = 4
    config: OwnershipMapConfig = field(default_factory=OwnershipMapConfig)

    # Per-prototype owner assignments (the "map")
    # prototype_owners[p] = expert_id that owns prototype p
    prototype_owners: list[int] = field(default_factory=list)

    # Per-prototype candidate sets
    # prototype_owner_candidates[p] = top C candidates by score
    prototype_owner_candidates: list[list[int]] = field(default_factory=list)

    # Per-prototype candidate scores
    prototype_candidate_scores: list[list[float]] = field(default_factory=list)

    # Tracking
    oracle_win_counts: list[list[int]] = field(default_factory=list)
    failure_counts: list[list[int]] = field(default_factory=list)
    sample_counts: list[list[int]] = field(default_factory=list)
    owner_change_history: list[dict] = field(default_factory=list)

    # Metrics
    owner_change_count: int = 0
    owner_change_success_count: int = 0
    total_evaluations: int = 0

    def __post_init__(self):
        if not self.prototype_owners:
            self.prototype_owners = [i % self.num_experts for i in range(self.num_prototypes)]
        if not self.prototype_owner_candidates:
            self.prototype_owner_candidates = [
                list(range(min(self.config.candidate_set_size, self.num_experts)))
                for _ in range(self.num_prototypes)
            ]
        if not self.prototype_candidate_scores:
            self.prototype_candidate_scores = [
                [0.0] * min(self.config.candidate_set_size, self.num_experts)
                for _ in range(self.num_prototypes)
            ]
        if not self.oracle_win_counts:
            self.oracle_win_counts = [
                [0] * self.num_experts for _ in range(self.num_prototypes)
            ]
        if not self.failure_counts:
            self.failure_counts = [
                [0] * self.num_experts for _ in range(self.num_prototypes)
            ]
        if not self.sample_counts:
            self.sample_counts = [
                [0] * self.num_experts for _ in range(self.num_prototypes)
            ]


# =============================================================================
# Candidate Generation
# =============================================================================


def generate_candidates(
    state: OwnershipMapState,
    *,
    router_logits: torch.Tensor,
    prototype_ids: torch.Tensor,
    oracle_expert_ids: Optional[torch.Tensor] = None,
    replay_results: Optional[dict] = None,
    compatible_mask: Optional[torch.Tensor] = None,
) -> dict[int, list[CandidateScore]]:
    """Generate candidate owners for each prototype from multiple sources.

    Args:
        state: Current ownership map state
        router_logits: [N, num_experts] raw router scores
        prototype_ids: [N] nearest prototype per token
        oracle_expert_ids: [N] best expert per token from oracle sweep (offline)
        replay_results: dict with replay oracle data per prototype
        compatible_mask: [num_prototypes, num_experts] compatibility

    Returns:
        Dict mapping prototype_id -> list of CandidateScore
    """
    config = state.config
    C = config.candidate_set_size
    num_prototypes = state.num_prototypes
    num_experts = state.num_experts

    candidates: dict[int, list[CandidateScore]] = {p: [] for p in range(num_prototypes)}

    # Source 1: current_owner (always included)
    for p in range(num_prototypes):
        current = state.prototype_owners[p]
        candidates[p].append(CandidateScore(
            prototype_id=p,
            expert_id=current,
            reliability_bias=0.1,  # Incumbency bonus
            source="current_owner",
        ))

    # Source 2: score_challenger (highest router logit for this prototype)
    if router_logits is not None and prototype_ids is not None:
        for p in range(num_prototypes):
            mask = prototype_ids == p
            if not mask.any():
                continue
            avg_logits = router_logits[mask].mean(dim=0)
            # Top challengers excluding current owner
            current = state.prototype_owners[p]
            challenger_scores = avg_logits.clone()
            challenger_scores[current] = -float("inf")
            top_challengers = challenger_scores.topk(min(2, num_experts - 1)).indices.tolist()
            for e in top_challengers:
                candidates[p].append(CandidateScore(
                    prototype_id=p,
                    expert_id=e,
                    source="score_challenger",
                ))

    # Source 3+4: nearest_prototype_primary/backup_owners
    for p in range(num_prototypes):
        # Primary owners of nearby prototypes are candidates
        # Use simple neighbor heuristic: prototypes p-1, p+1
        neighbors = [(p - 1) % num_prototypes, (p + 1) % num_prototypes]
        for np_id in neighbors:
            primary_owner = state.prototype_owners[np_id]
            if primary_owner != state.prototype_owners[p]:
                candidates[p].append(CandidateScore(
                    prototype_id=p,
                    expert_id=primary_owner,
                    source="nearest_prototype_primary_owners",
                ))
            # Backup owners (from candidate set of neighbors)
            for backup in state.prototype_owner_candidates[np_id]:
                if backup != state.prototype_owners[p] and backup != primary_owner:
                    candidates[p].append(CandidateScore(
                        prototype_id=p,
                        expert_id=backup,
                        source="nearest_prototype_backup_owners",
                    ))

    # Source 5+6: replay_oracle_winners and runners_up
    if oracle_expert_ids is not None and prototype_ids is not None:
        for p in range(num_prototypes):
            mask = prototype_ids == p
            if not mask.any():
                continue
            oracle_for_p = oracle_expert_ids[mask]
            # Count oracle wins per expert
            expert_wins = torch.zeros(num_experts, dtype=torch.long)
            for e_id in oracle_for_p:
                expert_wins[e_id.item()] += 1
            total = mask.sum().item()
            # Winner
            winner = expert_wins.argmax().item()
            win_rate = expert_wins[winner].item() / max(total, 1)
            candidates[p].append(CandidateScore(
                prototype_id=p,
                expert_id=winner,
                oracle_win_rate=win_rate,
                source="replay_oracle_winners",
            ))
            # Runner-up
            expert_wins[winner] = -1
            runner_up = expert_wins.argmax().item()
            if expert_wins[runner_up].item() > 0:
                ru_rate = expert_wins[runner_up].item() / max(total, 1)
                candidates[p].append(CandidateScore(
                    prototype_id=p,
                    expert_id=runner_up,
                    oracle_win_rate=ru_rate,
                    source="replay_oracle_runners_up",
                ))

    # Source 7: underused_compatible_owners_with_oracle_wins
    if compatible_mask is not None:
        expert_usage = torch.zeros(num_experts)
        for p in range(num_prototypes):
            expert_usage[state.prototype_owners[p]] += 1
        mean_usage = expert_usage.mean().item()
        for p in range(num_prototypes):
            compat = compatible_mask[p] if compatible_mask.dim() == 2 else compatible_mask
            for e in range(num_experts):
                if compat[e].item() > 0 and expert_usage[e].item() < mean_usage * 0.5:
                    oracle_wins = state.oracle_win_counts[p][e]
                    if oracle_wins > 0:
                        candidates[p].append(CandidateScore(
                            prototype_id=p,
                            expert_id=e,
                            underused_compatible_bonus=0.1,
                            oracle_win_rate=oracle_wins / max(sum(state.oracle_win_counts[p]), 1),
                            source="underused_compatible_owners_with_oracle_wins",
                        ))

    # Source 8: rare_expert_unique_utility_owners
    expert_total_wins = [sum(state.oracle_win_counts[p][e] for p in range(num_prototypes))
                         for e in range(num_experts)]
    mean_wins = sum(expert_total_wins) / max(num_experts, 1)
    for p in range(num_prototypes):
        for e in range(num_experts):
            if expert_total_wins[e] < mean_wins * 0.3 and state.oracle_win_counts[p][e] > 0:
                candidates[p].append(CandidateScore(
                    prototype_id=p,
                    expert_id=e,
                    rare_utility_bonus=0.15,
                    source="rare_expert_unique_utility_owners",
                ))

    # Deduplicate and score
    for p in range(num_prototypes):
        # Merge duplicate expert entries (keep best source)
        by_expert: dict[int, CandidateScore] = {}
        for c_score in candidates[p]:
            e = c_score.expert_id
            if e not in by_expert or c_score.total_score > by_expert[e].total_score:
                by_expert[e] = c_score
            else:
                # Accumulate useful signals
                by_expert[e].oracle_win_rate = max(
                    by_expert[e].oracle_win_rate, c_score.oracle_win_rate
                )
                by_expert[e].rare_utility_bonus = max(
                    by_expert[e].rare_utility_bonus, c_score.rare_utility_bonus
                )
                by_expert[e].underused_compatible_bonus = max(
                    by_expert[e].underused_compatible_bonus, c_score.underused_compatible_bonus
                )

        # Apply failure/monopoly penalties from state
        for e, cs in by_expert.items():
            total_samples = max(state.sample_counts[p][e], 1)
            cs.failure_rate = state.failure_counts[p][e] / total_samples
            # Monopoly: if this expert owns too many prototypes
            expert_owned = sum(1 for owner in state.prototype_owners if owner == e)
            if expert_owned > num_prototypes / num_experts * 1.5:
                cs.monopoly_penalty = 0.1 * (expert_owned / num_prototypes)
            # Stale penalty: if current owner hasn't won oracle recently
            if e == state.prototype_owners[p]:
                recent_wins = state.oracle_win_counts[p][e]
                total_wins = sum(state.oracle_win_counts[p])
                if total_wins > 0 and recent_wins / total_wins < 0.3:
                    cs.stale_owner_penalty = 0.1

        # Sort by total score, take top C
        sorted_candidates = sorted(by_expert.values(), key=lambda x: x.total_score, reverse=True)
        candidates[p] = sorted_candidates[:C]

    return candidates


# =============================================================================
# Semantic Margin Guard
# =============================================================================


def compute_semantic_margin(
    router_logits: torch.Tensor,
    prototype_bias: torch.Tensor,
    monopoly_penalty: Optional[torch.Tensor] = None,
    stale_penalty: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    """Compute semantic score without ownership bias.

    semantic_score = router_logits + prototype_bias - monopoly_penalty - stale_penalty
    semantic_margin = semantic_top1_score - semantic_top2_score

    Returns:
        semantic_margin: [N] margin between top1 and top2 semantic scores
    """
    semantic_score = router_logits + prototype_bias
    if monopoly_penalty is not None:
        semantic_score = semantic_score - monopoly_penalty
    if stale_penalty is not None:
        semantic_score = semantic_score - stale_penalty

    top2_vals = semantic_score.topk(min(2, semantic_score.shape[-1]), dim=-1).values
    if top2_vals.shape[-1] < 2:
        return top2_vals[:, 0]
    return top2_vals[:, 0] - top2_vals[:, 1]


def ownership_bias_allowed(
    semantic_margin: torch.Tensor,
    margin_guard: float,
    failure_bias_current: Optional[torch.Tensor] = None,
    replay_evidence_strong: Optional[torch.Tensor] = None,
    current_owner_stale: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    """Determine if ownership bias may flip owner per token.

    Guard rule: If semantic_margin > semantic_margin_guard,
    ownership bias may flip owner only if:
        - failure_bias[current_owner] is high
        - or replay oracle evidence strongly favors challenger
        - or current owner is marked stale for prototype

    Args:
        semantic_margin: [N]
        margin_guard: scalar threshold
        failure_bias_current: [N] failure rate of current owner (optional)
        replay_evidence_strong: [N] bool, replay strongly favors flip (optional)
        current_owner_stale: [N] bool, current owner is stale (optional)

    Returns:
        allowed: [N] bool, whether ownership flip is permitted
    """
    N = semantic_margin.shape[0]
    device = semantic_margin.device

    # Low margin: always allow ownership bias
    low_margin = semantic_margin <= margin_guard
    allowed = low_margin.clone()

    # High margin: only if override conditions met
    high_margin = ~low_margin
    if high_margin.any():
        override = torch.zeros(N, device=device, dtype=torch.bool)

        if failure_bias_current is not None:
            override = override | (failure_bias_current > 0.5)

        if replay_evidence_strong is not None:
            override = override | replay_evidence_strong

        if current_owner_stale is not None:
            override = override | current_owner_stale

        allowed = allowed | (high_margin & override)

    return allowed


# =============================================================================
# Ownership Bias Application (tensor-only, hot-path safe)
# =============================================================================


def apply_ownership_bias(
    router_logits: torch.Tensor,
    prototype_ids: torch.Tensor,
    ownership_map_tensor: torch.Tensor,
    ownership_weight: float = 0.25,
    ownership_bias_cap: float = 0.25,
    semantic_margin: Optional[torch.Tensor] = None,
    margin_guard: float = 0.10,
) -> torch.Tensor:
    """Apply ownership bias to router logits (tensor-only, no Python loops).

    This is safe for the hot path. All operations are vectorized.

    Args:
        router_logits: [N, num_experts]
        prototype_ids: [N] nearest prototype per token
        ownership_map_tensor: [num_prototypes, num_experts] ownership scores
        ownership_weight: scalar weight for ownership contribution
        ownership_bias_cap: cap on ownership bias magnitude
        semantic_margin: [N] optional, for margin guard
        margin_guard: threshold for semantic margin guard

    Returns:
        biased_logits: [N, num_experts] logits with ownership bias applied
    """
    # Gather ownership scores for each token's prototype
    ownership_scores = ownership_map_tensor[prototype_ids]  # [N, num_experts]

    # Cap and scale
    ownership_bias = (ownership_scores * ownership_weight).clamp(
        -ownership_bias_cap, ownership_bias_cap
    )

    # Apply semantic margin guard if provided
    if semantic_margin is not None:
        # Zero out bias where margin is high (guard protects strong semantic signals)
        high_margin_mask = semantic_margin > margin_guard  # [N]
        ownership_bias = ownership_bias * (~high_margin_mask).unsqueeze(-1).float()

    return router_logits + ownership_bias


# =============================================================================
# Candidate Map Refresh (offline-only)
# =============================================================================


def refresh_ownership_map(
    state: OwnershipMapState,
    candidates: dict[int, list[CandidateScore]],
) -> tuple[OwnershipMapState, dict]:
    """Refresh ownership map from candidate scores (offline-only).

    Flow:
    - For each prototype, select best candidate as new owner
    - Apply minimum sample protection
    - Track owner changes

    Returns:
        Updated state, change_report dict
    """
    config = state.config
    changes = []
    unchanged = []

    for p in range(state.num_prototypes):
        if not candidates.get(p):
            unchanged.append(p)
            continue

        best = candidates[p][0]
        current_owner = state.prototype_owners[p]

        # Minimum sample protection
        samples = state.sample_counts[p][best.expert_id]
        if samples < config.min_ownership_samples and best.expert_id != current_owner:
            unchanged.append(p)
            continue

        if best.expert_id != current_owner and best.total_score > 0:
            # Check if improvement over current owner
            current_score = next(
                (c.total_score for c in candidates[p] if c.expert_id == current_owner),
                0.0,
            )
            if best.total_score > current_score:
                old_owner = current_owner
                state.prototype_owners[p] = best.expert_id
                state.owner_change_count += 1
                changes.append({
                    "prototype_id": p,
                    "old_owner": old_owner,
                    "new_owner": best.expert_id,
                    "score_improvement": best.total_score - current_score,
                    "source": best.source,
                })
            else:
                unchanged.append(p)
        else:
            unchanged.append(p)

    # Update candidate sets
    for p in range(state.num_prototypes):
        if candidates.get(p):
            state.prototype_owner_candidates[p] = [c.expert_id for c in candidates[p]]
            state.prototype_candidate_scores[p] = [c.total_score for c in candidates[p]]

    report = {
        "owner_changes": changes,
        "unchanged_prototypes": len(unchanged),
        "total_changes": len(changes),
        "owner_change_rate": len(changes) / max(state.num_prototypes, 1),
    }
    return state, report


# =============================================================================
# Ownership Metrics
# =============================================================================


def compute_candidate_owner_recall(
    oracle_expert_ids: torch.Tensor,
    prototype_ids: torch.Tensor,
    candidate_sets: list[list[int]],
) -> dict[str, float]:
    """Compute candidate owner recall: is oracle-best in candidate set?

    Args:
        oracle_expert_ids: [N] best expert per token from oracle
        prototype_ids: [N] prototype assignments
        candidate_sets: per-prototype candidate expert lists

    Returns:
        Dict with recall metrics
    """
    N = oracle_expert_ids.shape[0]
    in_set = 0
    by_prototype: dict[int, list[bool]] = {}

    for i in range(N):
        p = prototype_ids[i].item()
        oracle_e = oracle_expert_ids[i].item()
        is_in = oracle_e in candidate_sets[p]
        in_set += int(is_in)
        by_prototype.setdefault(p, []).append(is_in)

    recall = in_set / max(N, 1)
    recall_by_proto = {
        p: sum(hits) / max(len(hits), 1)
        for p, hits in by_prototype.items()
    }

    return {
        "candidate_owner_recall": recall,
        "oracle_best_in_candidate_set_rate": recall,
        "candidate_set_size": len(candidate_sets[0]) if candidate_sets else 0,
        "candidate_recall_by_prototype": recall_by_proto,
        "total_tokens": N,
        "tokens_with_oracle_in_set": in_set,
    }


def compute_owner_change_metrics(
    state: OwnershipMapState,
    loss_when_changed: list[float],
    loss_when_unchanged: list[float],
    oracle_gap_when_changed: list[float],
    oracle_gap_when_unchanged: list[float],
) -> dict[str, float]:
    """Compute owner-change effectiveness metrics."""
    total_eval = state.total_evaluations
    change_rate = state.owner_change_count / max(total_eval, 1)
    success_rate = state.owner_change_success_count / max(state.owner_change_count, 1)

    return {
        "owner_change_rate": change_rate,
        "owner_changed_success_rate": success_rate,
        "owner_change_count": state.owner_change_count,
        "total_evaluations": total_eval,
        "loss_when_owner_changed": sum(loss_when_changed) / max(len(loss_when_changed), 1),
        "loss_when_owner_unchanged": sum(loss_when_unchanged) / max(len(loss_when_unchanged), 1),
        "oracle_gap_when_owner_changed": sum(oracle_gap_when_changed) / max(len(oracle_gap_when_changed), 1),
        "oracle_gap_when_owner_unchanged": sum(oracle_gap_when_unchanged) / max(len(oracle_gap_when_unchanged), 1),
    }


# =============================================================================
# Failure Decomposition
# =============================================================================


def compute_failure_decomposition(
    oracle_expert_ids: torch.Tensor,
    selected_expert_ids: torch.Tensor,
    prototype_ids: torch.Tensor,
    candidate_sets: list[list[int]],
    loss_per_token: torch.Tensor,
    oracle_loss_per_token: torch.Tensor,
) -> dict[str, Any]:
    """Decompose failures into recall vs scoring vs capacity.

    - candidate_recall_failure: oracle-best not in candidate set
    - scoring_failure: oracle-best in candidate set but not selected
    - expert_capacity_failure: oracle-best selected but loss still bad

    Returns:
        Failure decomposition report dict
    """
    N = oracle_expert_ids.shape[0]
    recall_failures = 0
    scoring_failures = 0
    capacity_failures = 0
    by_prototype: dict[int, dict[str, int]] = {}

    for i in range(N):
        p = prototype_ids[i].item()
        oracle_e = oracle_expert_ids[i].item()
        selected_e = selected_expert_ids[i].item()
        candidates = candidate_sets[p]

        by_prototype.setdefault(p, {"recall": 0, "scoring": 0, "capacity": 0, "total": 0})
        by_prototype[p]["total"] += 1

        if oracle_e not in candidates:
            recall_failures += 1
            by_prototype[p]["recall"] += 1
        elif oracle_e != selected_e:
            scoring_failures += 1
            by_prototype[p]["scoring"] += 1
        elif loss_per_token[i].item() > oracle_loss_per_token[i].item() * 1.5:
            capacity_failures += 1
            by_prototype[p]["capacity"] += 1

    total_failures = recall_failures + scoring_failures + capacity_failures

    # Find top failed prototypes
    proto_failure_rates = {
        p: (d["recall"] + d["scoring"] + d["capacity"]) / max(d["total"], 1)
        for p, d in by_prototype.items()
    }
    top_failed = sorted(proto_failure_rates.items(), key=lambda x: x[1], reverse=True)[:5]

    # Recommended action
    if recall_failures > scoring_failures and recall_failures > capacity_failures:
        recommended = "expand_candidate_generation_and_replay_sampling"
    elif scoring_failures > recall_failures and scoring_failures > capacity_failures:
        recommended = "recalibrate_ownership_bias_and_failure_penalties"
    else:
        recommended = "ownership_routing_correct_expert_capacity_insufficient"

    return {
        "candidate_recall_failure_rate": recall_failures / max(N, 1),
        "scoring_failure_rate": scoring_failures / max(N, 1),
        "expert_capacity_failure_rate": capacity_failures / max(N, 1),
        "total_failure_count": total_failures,
        "total_tokens": N,
        "prototype_distribution": by_prototype,
        "top_failed_prototypes": [{"prototype": p, "failure_rate": r} for p, r in top_failed],
        "recommended_action": recommended,
    }


# =============================================================================
# Promotion Gate
# =============================================================================


def evaluate_promotion_gate(
    *,
    config: OwnershipMapConfig,
    deploy_top1_loss: float,
    deploy_top1_oracle_gap: float,
    deploy_top1_latency_ms: float,
    deploy_top1_high_confidence_failure_rate: float,
    deploy_top1_monopoly_rate: float,
    candidate_loss: float,
    candidate_oracle_gap: float,
    candidate_latency_ms: float,
    candidate_quality_per_ms: float,
    owner_changed_success_rate: float,
    candidate_owner_recall: float,
    high_confidence_failure_rate: float,
    prototype_monopoly_rate: float,
    seed_repeatability_passed: bool,
    canary_reproduced: bool,
    frozen_candidate_reproduced: bool,
    owner_change_rate: float,
    deploy_top1_quality_per_ms: float = 0.0,
) -> dict[str, Any]:
    """Evaluate promotion gate with explicit reason codes.

    Returns report with decision and all gate results.
    """
    blocked_reasons = []

    # Loss gate
    loss_passed = candidate_loss <= deploy_top1_loss - config.min_loss_improvement
    if not loss_passed:
        blocked_reasons.append("LOSS_REGRESSION")

    # Oracle gap gate
    oracle_gap_passed = candidate_oracle_gap <= deploy_top1_oracle_gap - config.min_oracle_gap_improvement
    if not oracle_gap_passed:
        blocked_reasons.append("ORACLE_GAP_REGRESSION")

    # Quality per ms gate
    qpm_passed = candidate_quality_per_ms >= deploy_top1_quality_per_ms
    if not qpm_passed:
        blocked_reasons.append("QUALITY_PER_MS_REGRESSION")

    # Latency gate
    latency_passed = candidate_latency_ms <= deploy_top1_latency_ms * config.latency_multiplier_limit
    if not latency_passed:
        blocked_reasons.append("LATENCY_REGRESSION")

    # Owner change success gate
    owner_success_passed = owner_changed_success_rate >= config.owner_changed_success_threshold
    if not owner_success_passed:
        blocked_reasons.append("OWNER_CHANGE_SUCCESS_TOO_LOW")

    # Candidate recall gate
    recall_passed = candidate_owner_recall >= 0.5
    if not recall_passed:
        blocked_reasons.append("CANDIDATE_RECALL_TOO_LOW")

    # High confidence failure gate
    confidence_passed = (
        high_confidence_failure_rate
        <= deploy_top1_high_confidence_failure_rate + config.high_confidence_failure_tolerance
    )
    if not confidence_passed:
        blocked_reasons.append("HIGH_CONFIDENCE_FAILURE_INCREASE")

    # Prototype monopoly gate
    monopoly_passed = (
        prototype_monopoly_rate
        <= deploy_top1_monopoly_rate + config.prototype_monopoly_tolerance
    )
    if not monopoly_passed:
        blocked_reasons.append("PROTOTYPE_MONOPOLY_INCREASE")

    # Reproduction gates
    if not canary_reproduced:
        blocked_reasons.append("CANARY_NOT_REPRODUCED")
    if not frozen_candidate_reproduced:
        blocked_reasons.append("FROZEN_CANDIDATE_NOT_REPRODUCED")

    # Seed repeatability
    if not seed_repeatability_passed:
        blocked_reasons.append("SEED_REPEATABILITY_FAILED")

    # Owner change rate (not too rare)
    if owner_change_rate < config.early_calibration_owner_change_rate_min:
        blocked_reasons.append("OWNER_CHANGE_TOO_RARE")

    promotion_decision = len(blocked_reasons) == 0

    return {
        "promotion_decision": promotion_decision,
        "promotion_blocked_reasons": blocked_reasons,
        "loss_gate_passed": loss_passed,
        "oracle_gap_gate_passed": oracle_gap_passed,
        "quality_per_ms_gate_passed": qpm_passed,
        "latency_gate_passed": latency_passed,
        "owner_change_success_gate_passed": owner_success_passed,
        "candidate_recall_gate_passed": recall_passed,
        "confidence_calibration_gate_passed": confidence_passed,
        "prototype_monopoly_gate_passed": monopoly_passed,
        "reproduction_gate_passed": canary_reproduced and frozen_candidate_reproduced,
        "seed_repeatability_gate_passed": seed_repeatability_passed,
        "status": (
            "PVR_EC_OWNERSHIP_PROMOTION_GATE_CLEAN"
            if promotion_decision
            else "PVR_EC_OWNERSHIP_PROMOTION_GATE_NOT_CLEAN"
        ),
    }


# =============================================================================
# Bias Calibration Sweep
# =============================================================================


@dataclass
class SweepResult:
    """Result of one ownership bias configuration."""

    ownership_weight: float
    ownership_bias_cap: float
    failure_bias_weight: float
    semantic_margin_guard: float
    candidate_set_size: int
    loss: float = 0.0
    oracle_gap: float = 0.0
    quality_per_ms: float = 0.0
    owner_change_rate: float = 0.0
    owner_changed_success_rate: float = 0.0
    latency_ms: float = 0.0
    high_confidence_failure_rate: float = 0.0
    prototype_monopoly_rate: float = 0.0
    is_safe: bool = False


def select_best_safe_config(
    sweep_results: list[SweepResult],
    deploy_top1_loss: float,
    deploy_top1_oracle_gap: float,
    deploy_top1_latency_ms: float,
    config: OwnershipMapConfig,
) -> Optional[SweepResult]:
    """Select best safe configuration from sweep results.

    Safe config must satisfy all constraints from section 8.
    """
    safe_configs = []
    for r in sweep_results:
        # Check all safety constraints
        if r.loss > deploy_top1_loss - config.min_loss_improvement:
            continue
        if r.oracle_gap > deploy_top1_oracle_gap - config.min_oracle_gap_improvement:
            continue
        if r.owner_changed_success_rate < config.owner_changed_success_threshold:
            continue
        if r.latency_ms > deploy_top1_latency_ms * config.latency_multiplier_limit:
            continue
        if r.high_confidence_failure_rate > config.high_confidence_failure_tolerance:
            continue
        if r.prototype_monopoly_rate > config.prototype_monopoly_tolerance:
            continue
        r.is_safe = True
        safe_configs.append(r)

    if not safe_configs:
        return None

    # Primary objective: lower loss and lower oracle gap
    safe_configs.sort(key=lambda r: (r.loss, r.oracle_gap))
    return safe_configs[0]


# =============================================================================
# Multi-Seed Confirmation
# =============================================================================


def aggregate_multiseed_results(
    results_by_seed: dict[int, dict[str, float]],
) -> dict[str, Any]:
    """Aggregate metrics across seeds for confirmation.

    Args:
        results_by_seed: {seed: {metric_name: value}}

    Returns:
        Aggregated report with mean/std for each metric
    """
    if not results_by_seed:
        return {"status": "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_FAILED", "reason": "no_results"}

    all_metrics: dict[str, list[float]] = {}
    for seed_results in results_by_seed.values():
        for key, value in seed_results.items():
            if isinstance(value, (int, float)):
                all_metrics.setdefault(key, []).append(float(value))

    aggregated = {}
    for key, values in all_metrics.items():
        if values:
            aggregated[f"{key}_mean"] = sum(values) / len(values)
            n = len(values)
            if n > 1:
                mean = sum(values) / n
                aggregated[f"{key}_std"] = math.sqrt(sum((v - mean) ** 2 for v in values) / (n - 1))
            else:
                aggregated[f"{key}_std"] = 0.0

    # Decision: improvement must occur across seeds
    loss_values = all_metrics.get("loss_improvement", [])
    if loss_values and all(v > 0 for v in loss_values):
        aggregated["status"] = "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_CONFIRMED"
    elif loss_values and any(v > 0 for v in loss_values):
        aggregated["status"] = "PVR_EC_DO_NOT_PROMOTE"
        aggregated["reason"] = "improvement_only_on_some_seeds"
    else:
        aggregated["status"] = "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_FAILED"

    aggregated["seeds"] = list(results_by_seed.keys())
    aggregated["seed_count"] = len(results_by_seed)

    return aggregated


# =============================================================================
# Report Writers
# =============================================================================


def write_ownership_reports(
    output_dir: str | Path,
    *,
    candidate_recall: Optional[dict] = None,
    owner_change_metrics: Optional[dict] = None,
    bias_sweep_results: Optional[list[SweepResult]] = None,
    best_config: Optional[SweepResult] = None,
    promotion_gate: Optional[dict] = None,
    failure_decomposition: Optional[dict] = None,
    multiseed_results: Optional[dict] = None,
    ownership_state: Optional[OwnershipMapState] = None,
    action_rate_metrics: Optional[dict] = None,
) -> dict[str, Path]:
    """Write all ownership-related reports."""

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}

    # 1. Candidate Recall Report
    recall_data = candidate_recall or {
        "candidate_owner_recall": 0.0,
        "status": "PVR_EC_CANDIDATE_OWNER_RECALL_LOW",
    }
    _write_json(out / "ownership_candidate_recall_report.json", recall_data, paths)
    _write_md(out / "ownership_candidate_recall_report.md",
              "Ownership Candidate Recall Report", recall_data, paths)

    # 2. Action Rate Report
    action_data = action_rate_metrics or owner_change_metrics or {
        "owner_change_rate": 0.0,
        "status": "PVR_EC_OWNERSHIP_MAP_ACTS_TOO_RARELY",
    }
    if "target_owner_change_band" not in action_data:
        action_data["target_owner_change_band"] = "2%-8% (early calibration)"
    if "recommended_bias_adjustment" not in action_data:
        rate = action_data.get("owner_change_rate", 0.0)
        if rate < 0.02:
            action_data["recommended_bias_adjustment"] = "increase_ownership_weight"
        elif rate > 0.12:
            action_data["recommended_bias_adjustment"] = "decrease_ownership_weight"
        else:
            action_data["recommended_bias_adjustment"] = "none"
    _write_json(out / "ownership_action_rate_report.json", action_data, paths)

    # 3. Bias Calibration Report
    bias_data: dict[str, Any] = {}
    if best_config:
        bias_data = {
            "best_ownership_weight": best_config.ownership_weight,
            "best_ownership_bias_cap": best_config.ownership_bias_cap,
            "best_failure_bias_weight": best_config.failure_bias_weight,
            "best_semantic_margin_guard": best_config.semantic_margin_guard,
            "best_candidate_set_size": best_config.candidate_set_size,
            "best_loss": best_config.loss,
            "best_oracle_gap": best_config.oracle_gap,
            "is_safe": best_config.is_safe,
            "status": "PVR_EC_OWNERSHIP_BIAS_CALIBRATED" if best_config.is_safe
                      else "PVR_EC_OWNERSHIP_BIAS_UNDERCALIBRATED",
        }
    else:
        bias_data = {"status": "PVR_EC_OWNERSHIP_BIAS_UNDERCALIBRATED"}
    _write_json(out / "ownership_bias_calibration_report.json", bias_data, paths)

    # 4. Bias Sweep Report
    sweep_data: dict[str, Any] = {"configs_tested": 0}
    if bias_sweep_results:
        sweep_data = {
            "configs_tested": len(bias_sweep_results),
            "safe_configs": sum(1 for r in bias_sweep_results if r.is_safe),
            "results": [asdict(r) for r in bias_sweep_results],
        }
    _write_json(out / "ownership_bias_sweep_report.json", sweep_data, paths)

    # 5. Promotion Gate Report
    gate_data = promotion_gate or {
        "promotion_decision": False,
        "promotion_blocked_reasons": ["CANDIDATE_RECALL_TOO_LOW"],
        "status": "PVR_EC_OWNERSHIP_PROMOTION_GATE_NOT_CLEAN",
    }
    _write_json(out / "ownership_promotion_gate_report.json", gate_data, paths)
    _write_md(out / "ownership_promotion_gate_report.md",
              "Ownership Promotion Gate Report", gate_data, paths)

    # 6. Failure Decomposition Report
    decomp_data = failure_decomposition or {
        "candidate_recall_failure_rate": 0.0,
        "scoring_failure_rate": 0.0,
        "expert_capacity_failure_rate": 0.0,
        "recommended_action": "expand_candidate_generation_and_replay_sampling",
    }
    _write_json(out / "ownership_failure_decomposition_report.json", decomp_data, paths)

    # 7. Multi-Seed Repeatability Report
    seed_data = multiseed_results or {
        "status": "PVR_EC_OWNERSHIP_REPEATED_SIGNAL_FAILED",
        "reason": "not_yet_run",
    }
    _write_json(out / "ownership_repeatability_report.json", seed_data, paths)
    _write_md(out / "ownership_repeatability_report.md",
              "Ownership Repeatability Report", seed_data, paths)

    # 8. Map Refresh Report
    refresh_data: dict[str, Any] = {"status": "PVR_EC_OWNERSHIP_MAP_REFRESH_READY"}
    if ownership_state:
        refresh_data.update({
            "prototype_owners": ownership_state.prototype_owners,
            "owner_change_count": ownership_state.owner_change_count,
            "total_evaluations": ownership_state.total_evaluations,
        })
    _write_json(out / "ownership_map_refresh_report.json", refresh_data, paths)

    # 9. Owner Change Report
    change_data = owner_change_metrics or {"owner_change_rate": 0.0}
    _write_json(out / "ownership_owner_change_report.json", change_data, paths)

    # 10. Oracle Gap Report
    oracle_data: dict[str, Any] = {
        "oracle_gap_when_owner_changed": (owner_change_metrics or {}).get(
            "oracle_gap_when_owner_changed", 0.0
        ),
        "oracle_gap_when_owner_unchanged": (owner_change_metrics or {}).get(
            "oracle_gap_when_owner_unchanged", 0.0
        ),
    }
    _write_json(out / "ownership_oracle_gap_report.json", oracle_data, paths)

    return paths


def _write_json(path: Path, data: dict, paths: dict[str, Path]):
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    paths[path.name] = path


def _write_md(path: Path, title: str, data: dict, paths: dict[str, Path]):
    lines = [f"# {title}", "", f"**Status:** {data.get('status', 'unknown')}", ""]
    if "promotion_blocked_reasons" in data:
        lines.append("## Blocked Reasons")
        for reason in data["promotion_blocked_reasons"]:
            lines.append(f"- {reason}")
        lines.append("")
    lines.append("## Data")
    lines.append("```json")
    lines.append(json.dumps(data, indent=2, default=str))
    lines.append("```")
    path.write_text("\n".join(lines), encoding="utf-8")
    paths[path.name] = path


# =============================================================================
# Frozen Candidate Map (for deployment eval)
# =============================================================================


def build_ownership_map_tensor(
    state: OwnershipMapState,
) -> torch.Tensor:
    """Build a [num_prototypes, num_experts] ownership score tensor.

    The tensor encodes ownership as a one-hot-like bias: the owner gets +1,
    candidates get fractional scores, non-candidates get 0.
    """
    num_p = state.num_prototypes
    num_e = state.num_experts
    tensor = torch.zeros(num_p, num_e)

    for p in range(num_p):
        owner = state.prototype_owners[p]
        tensor[p, owner] = 1.0

        # Candidates get scaled score
        for i, e in enumerate(state.prototype_owner_candidates[p]):
            if e != owner:
                score = state.prototype_candidate_scores[p][i] if i < len(state.prototype_candidate_scores[p]) else 0.0
                tensor[p, e] = max(0.0, min(score, 0.5))

    return tensor


def export_frozen_candidate_map(
    state: OwnershipMapState,
    output_path: str | Path,
) -> Path:
    """Export frozen candidate map for canary/evaluation."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "prototype_owners": state.prototype_owners,
        "prototype_owner_candidates": state.prototype_owner_candidates,
        "prototype_candidate_scores": state.prototype_candidate_scores,
        "config": asdict(state.config),
        "num_prototypes": state.num_prototypes,
        "num_experts": state.num_experts,
    }
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def load_frozen_candidate_map(path: str | Path) -> OwnershipMapState:
    """Load frozen candidate map."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    config = OwnershipMapConfig(**data.get("config", {}))
    state = OwnershipMapState(
        num_prototypes=data["num_prototypes"],
        num_experts=data["num_experts"],
        config=config,
    )
    state.prototype_owners = data["prototype_owners"]
    state.prototype_owner_candidates = data["prototype_owner_candidates"]
    state.prototype_candidate_scores = data["prototype_candidate_scores"]
    return state
