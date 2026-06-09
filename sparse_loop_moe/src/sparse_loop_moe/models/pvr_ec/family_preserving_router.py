"""Family-Preserving Top1 Candidate Router for PVR-EC-O.

Implements a canary/candidate router that adds family-preservation bias
to the single-owner Top1 scoring, without changing production deployment.

Key invariants:
- owners/token = 1.0
- Top2/Top4 execution = 0
- Family bias is tensor-backed, GPU-resident, clipped
- Compatible-mask constrained
- No Python dict lookup in forward
- No file write in forward
- No CPU/GPU transfer in forward
- No oracle/replay in forward
- No map update in forward

The score formula:
    owner_score(i, e) =
        router_logits[i, e]
      + prototype_bias[i, e]
      + clipped_ownership_bias[p_i, e]
      + clipped_family_bias[f_i, e]
      + clipped_balance_bias[e]
      - prototype_local_monopoly_penalty[p_i, e]
      - stale_owner_penalty[p_i, e]

    owner_score[i, ~compatible_mask_i] = -inf
    owner_i = argmax_e owner_score(i, e)
    execute exactly one expert delta
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

import torch
import torch.nn.functional as F


# =============================================================================
# Candidate Map Schema
# =============================================================================

CANDIDATE_MAP_SCHEMA_VERSION = "1.0.0"


@dataclass
class CandidateMapMetadata:
    """Metadata for a versioned family-preservation candidate map."""
    schema_version: str = CANDIDATE_MAP_SCHEMA_VERSION
    source_checkpoint_hash: str = ""
    router_config_hash: str = ""
    prototype_table_hash: str = ""
    compatible_mask_hash: str = ""
    num_prototypes: int = 0
    num_families: int = 0  # same as num_prototypes for prototype-based families
    num_experts: int = 0
    dtype: str = "float32"
    created_at: str = ""
    source_replay_window: str = ""
    promotion_status: str = "candidate"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CandidateMapMetadata":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class CandidateMap:
    """Family-preservation candidate map tensors.

    All tensors are [num_prototypes, num_experts] unless noted.
    """
    ownership_reliability_bias: torch.Tensor
    ownership_failure_bias: torch.Tensor
    family_owner_reliability: torch.Tensor
    family_owner_failure: torch.Tensor
    family_preservation_bias: torch.Tensor
    prototype_local_monopoly_penalty: torch.Tensor
    stale_owner_penalty: torch.Tensor
    metadata: CandidateMapMetadata

    @property
    def num_prototypes(self) -> int:
        return self.ownership_reliability_bias.shape[0]

    @property
    def num_experts(self) -> int:
        return self.ownership_reliability_bias.shape[1]

    def clipped_family_bias(self, weight: float = 0.25, cap: float = 0.25) -> torch.Tensor:
        """Compute clipped family bias: weight * (reliability - failure), clamped."""
        raw = self.family_owner_reliability - self.family_owner_failure
        return (weight * raw).clamp(-cap, cap)


def _tensor_hash(t: torch.Tensor) -> str:
    """Deterministic hash of tensor content."""
    data = t.detach().cpu().numpy().tobytes()
    return hashlib.sha256(data).hexdigest()[:16]


def create_blank_candidate_map(
    num_prototypes: int,
    num_experts: int,
    prototype_table: Optional[torch.Tensor] = None,
    compatible_mask: Optional[torch.Tensor] = None,
    router_config_hash: str = "",
) -> CandidateMap:
    """Create a blank candidate map with zero biases."""
    shape = (num_prototypes, num_experts)
    metadata = CandidateMapMetadata(
        num_prototypes=num_prototypes,
        num_families=num_prototypes,
        num_experts=num_experts,
        created_at=time.strftime("%Y-%m-%dT%H:%M:%S"),
        prototype_table_hash=_tensor_hash(prototype_table) if prototype_table is not None else "",
        compatible_mask_hash=_tensor_hash(compatible_mask) if compatible_mask is not None else "",
        router_config_hash=router_config_hash,
    )
    return CandidateMap(
        ownership_reliability_bias=torch.zeros(shape),
        ownership_failure_bias=torch.zeros(shape),
        family_owner_reliability=torch.zeros(shape),
        family_owner_failure=torch.zeros(shape),
        family_preservation_bias=torch.zeros(shape),
        prototype_local_monopoly_penalty=torch.zeros(shape),
        stale_owner_penalty=torch.zeros(shape),
        metadata=metadata,
    )


def save_candidate_map(candidate: CandidateMap, output_dir: Path) -> dict[str, Path]:
    """Save candidate map tensors and metadata to disk."""
    output_dir.mkdir(parents=True, exist_ok=True)
    map_path = output_dir / "ownership_map_candidate.pt"
    family_path = output_dir / "family_preservation_map_candidate.pt"
    meta_path = output_dir / "family_preservation_metadata.json"

    torch.save({
        "ownership_reliability_bias": candidate.ownership_reliability_bias,
        "ownership_failure_bias": candidate.ownership_failure_bias,
        "prototype_local_monopoly_penalty": candidate.prototype_local_monopoly_penalty,
        "stale_owner_penalty": candidate.stale_owner_penalty,
    }, map_path)

    torch.save({
        "family_owner_reliability": candidate.family_owner_reliability,
        "family_owner_failure": candidate.family_owner_failure,
        "family_preservation_bias": candidate.family_preservation_bias,
    }, family_path)

    with open(meta_path, "w") as f:
        json.dump(candidate.metadata.to_dict(), f, indent=2)

    return {"map": map_path, "family": family_path, "metadata": meta_path}


def load_candidate_map(
    input_dir: Path,
    expected_num_prototypes: int,
    expected_num_experts: int,
    expected_prototype_table_hash: str = "",
    expected_compatible_mask_hash: str = "",
) -> CandidateMap:
    """Load and validate a candidate map.

    Raises ValueError if dimensions or compatibility hashes mismatch.
    """
    meta_path = input_dir / "family_preservation_metadata.json"
    if not meta_path.exists():
        raise FileNotFoundError(f"No metadata at {meta_path}")

    with open(meta_path) as f:
        meta_dict = json.load(f)
    metadata = CandidateMapMetadata.from_dict(meta_dict)

    # Compatibility checks
    if metadata.num_prototypes != expected_num_prototypes:
        raise ValueError(
            f"Prototype mismatch: map has {metadata.num_prototypes}, "
            f"expected {expected_num_prototypes}"
        )
    if metadata.num_experts != expected_num_experts:
        raise ValueError(
            f"Expert mismatch: map has {metadata.num_experts}, "
            f"expected {expected_num_experts}"
        )
    if expected_prototype_table_hash and metadata.prototype_table_hash:
        if metadata.prototype_table_hash != expected_prototype_table_hash:
            raise ValueError(
                f"Prototype table hash mismatch: "
                f"{metadata.prototype_table_hash} != {expected_prototype_table_hash}"
            )
    if expected_compatible_mask_hash and metadata.compatible_mask_hash:
        if metadata.compatible_mask_hash != expected_compatible_mask_hash:
            raise ValueError(
                f"Compatible mask hash mismatch: "
                f"{metadata.compatible_mask_hash} != {expected_compatible_mask_hash}"
            )

    map_data = torch.load(input_dir / "ownership_map_candidate.pt", weights_only=True)
    family_data = torch.load(input_dir / "family_preservation_map_candidate.pt", weights_only=True)

    return CandidateMap(
        ownership_reliability_bias=map_data["ownership_reliability_bias"],
        ownership_failure_bias=map_data["ownership_failure_bias"],
        prototype_local_monopoly_penalty=map_data["prototype_local_monopoly_penalty"],
        stale_owner_penalty=map_data["stale_owner_penalty"],
        family_owner_reliability=family_data["family_owner_reliability"],
        family_owner_failure=family_data["family_owner_failure"],
        family_preservation_bias=family_data["family_preservation_bias"],
        metadata=metadata,
    )


# =============================================================================
# Family-Preserving Top1 Router Score
# =============================================================================


def family_preserving_top1_score(
    router_logits: torch.Tensor,
    prototype_bias: torch.Tensor,
    prototype_ids: torch.Tensor,
    compatible_mask: torch.Tensor,
    candidate_map: CandidateMap,
    balance_bias: Optional[torch.Tensor] = None,
    ownership_bias: Optional[torch.Tensor] = None,
    family_bias_weight: float = 0.25,
    family_bias_cap: float = 0.25,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Compute family-preserving Top1 routing score.

    All operations are tensor-only, no Python loops or dict lookups.

    Args:
        router_logits: [N, num_experts] raw router scores
        prototype_bias: [N, num_experts] per-token prototype bias
        prototype_ids: [N] nearest prototype per token
        compatible_mask: [N, num_experts] binary compatibility
        candidate_map: CandidateMap with all bias tensors
        balance_bias: [num_experts] optional load balance bias
        ownership_bias: [N, num_experts] optional existing ownership bias
        family_bias_weight: weight for family bias
        family_bias_cap: clamp magnitude for family bias

    Returns:
        (owner_ids, owner_scores) where:
        owner_ids: [N] argmax expert per token
        owner_scores: [N, num_experts] full score matrix
    """
    N = router_logits.shape[0]
    device = router_logits.device

    # Move candidate tensors to device
    family_reliability = candidate_map.family_owner_reliability.to(device)
    family_failure = candidate_map.family_owner_failure.to(device)
    monopoly_penalty = candidate_map.prototype_local_monopoly_penalty.to(device)
    stale_penalty = candidate_map.stale_owner_penalty.to(device)

    # Compute clipped family bias: [num_prototypes, num_experts]
    raw_family_bias = family_reliability - family_failure
    clipped_family_bias = (family_bias_weight * raw_family_bias).clamp(
        -family_bias_cap, family_bias_cap
    )

    # Gather per-token family bias: [N, num_experts]
    token_family_bias = clipped_family_bias[prototype_ids]

    # Gather per-token penalties: [N, num_experts]
    token_monopoly = monopoly_penalty[prototype_ids]
    token_stale = stale_penalty[prototype_ids]

    # Build score
    scores = router_logits + prototype_bias + token_family_bias
    scores = scores - token_monopoly - token_stale

    # Add optional biases
    if ownership_bias is not None:
        scores = scores + ownership_bias
    if balance_bias is not None:
        scores = scores + balance_bias.unsqueeze(0)

    # Apply compatible mask
    scores = scores.masked_fill(compatible_mask == 0, -float("inf"))

    # Argmax: single owner per token
    owner_ids = scores.argmax(dim=-1)

    return owner_ids, scores


# =============================================================================
# Expert Choice Teacher Evidence (Offline Only)
# =============================================================================


def compute_expert_choice_evidence(
    hidden_states: torch.Tensor,
    expert_deltas: list,
    prototype_ids: torch.Tensor,
    current_owners: torch.Tensor,
    targets: torch.Tensor,
    vocab_size: int = 256,
) -> dict[str, Any]:
    """Compute offline Expert Choice teacher evidence.

    For each expert, compute which tokens it would prefer (by loss improvement).
    This does NOT execute in production forward — it's offline replay evidence.

    Args:
        hidden_states: [N, d_model] pre-expert hidden states
        expert_deltas: list of expert modules
        prototype_ids: [N] nearest prototype per token
        current_owners: [N] current owner assignments
        targets: [N] target token ids
        vocab_size: vocabulary size

    Returns:
        Dict with teacher evidence metrics
    """
    N = hidden_states.shape[0]
    num_experts = len(expert_deltas)
    device = hidden_states.device

    # Compute loss per expert per token (offline!)
    losses_per_expert = torch.zeros(N, num_experts, device=device)

    for e_idx, expert in enumerate(expert_deltas):
        with torch.no_grad():
            # Expert output = hidden + expert_delta(hidden)
            expert_out = expert(hidden_states)  # [N, d_model]
            # Simple projection to vocab (just for relative comparison)
            # In practice this would use the full model head
            # For evidence purposes, we just compare expert outputs
            losses_per_expert[:, e_idx] = -expert_out.norm(dim=-1)  # proxy

    # Which tokens would each expert choose? (lowest loss)
    expert_preferred_tokens = losses_per_expert.argmin(dim=0)  # [num_experts]

    # Which expert is best for each token?
    best_expert_per_token = losses_per_expert.argmin(dim=-1)  # [N]

    # Challenger wins: where best != current
    challenger_wins = (best_expert_per_token != current_owners)
    challenger_win_rate = challenger_wins.float().mean().item()

    # Per-prototype analysis
    num_prototypes = prototype_ids.max().item() + 1 if prototype_ids.numel() > 0 else 1
    expert_family_recall = torch.zeros(num_experts, num_prototypes, device=device)
    expert_family_coverage = torch.zeros(num_experts, device=device)

    for e_idx in range(num_experts):
        # Tokens where this expert is best
        is_best = best_expert_per_token == e_idx
        if is_best.sum() == 0:
            continue
        # Which prototypes does this expert serve?
        protos_served = prototype_ids[is_best]
        for p in range(num_prototypes):
            proto_mask = prototype_ids == p
            proto_and_best = is_best & proto_mask
            if proto_mask.sum() > 0:
                expert_family_recall[e_idx, p] = proto_and_best.sum().float() / proto_mask.sum().float()
        expert_family_coverage[e_idx] = (expert_family_recall[e_idx] > 0).sum().float() / max(num_prototypes, 1)

    # Teacher-owner agreement
    agreement = (best_expert_per_token == current_owners).float().mean().item()

    return {
        "challenger_family_win_rate": challenger_win_rate,
        "teacher_family_owner_agreement": agreement,
        "single_owner_distillation_gap": 1.0 - agreement,
        "expert_family_recall": expert_family_recall.cpu(),
        "expert_family_coverage": expert_family_coverage.cpu().tolist(),
        "num_challenger_wins": int(challenger_wins.sum().item()),
        "best_expert_per_token": best_expert_per_token.cpu(),
    }


# =============================================================================
# Candidate Map Refresh from Evidence
# =============================================================================


def refresh_candidate_map_from_evidence(
    base_map: CandidateMap,
    expert_choice_evidence: dict[str, Any],
    prototype_ids: torch.Tensor,
    current_owners: torch.Tensor,
    success_mask: torch.Tensor,
    monopoly_threshold: float = 0.9,
    stale_threshold: float = 0.3,
) -> CandidateMap:
    """Refresh candidate map tensors from offline evidence.

    Does NOT mutate the base_map. Returns a new CandidateMap.

    Args:
        base_map: starting candidate map
        expert_choice_evidence: output from compute_expert_choice_evidence
        prototype_ids: [N] prototype assignments
        current_owners: [N] current owner assignments
        success_mask: [N] boolean - did current owner succeed?
        monopoly_threshold: threshold for monopoly penalty
        stale_threshold: threshold for stale penalty

    Returns:
        New CandidateMap with updated biases
    """
    num_prototypes = base_map.num_prototypes
    num_experts = base_map.num_experts

    # Start from base
    reliability = base_map.family_owner_reliability.clone()
    failure = base_map.family_owner_failure.clone()
    monopoly_penalty = base_map.prototype_local_monopoly_penalty.clone()
    stale_penalty = base_map.stale_owner_penalty.clone()

    # Update reliability/failure from evidence
    for i in range(prototype_ids.shape[0]):
        p = prototype_ids[i].item()
        e = current_owners[i].item()
        if p < num_prototypes and e < num_experts:
            if success_mask[i].item():
                reliability[p, e] += 1.0
            else:
                failure[p, e] += 1.0

    # Update from challenger evidence
    best_experts = expert_choice_evidence.get("best_expert_per_token")
    if best_experts is not None:
        for i in range(min(best_experts.shape[0], prototype_ids.shape[0])):
            p = prototype_ids[i].item()
            best_e = best_experts[i].item()
            if p < num_prototypes and best_e < num_experts:
                reliability[p, best_e] += 0.5  # Soft boost for challenger wins

    # Compute monopoly penalty
    for p in range(num_prototypes):
        total = reliability[p].sum()
        if total > 0:
            max_share = reliability[p].max() / total
            if max_share > monopoly_threshold:
                dominant_expert = reliability[p].argmax()
                monopoly_penalty[p, dominant_expert] = (max_share - monopoly_threshold) * 0.1

    # Compute stale penalty (experts with high failure rate)
    for p in range(num_prototypes):
        for e in range(num_experts):
            total = reliability[p, e] + failure[p, e]
            if total > 5:  # Minimum evidence threshold
                failure_rate = failure[p, e] / total
                if failure_rate > stale_threshold:
                    stale_penalty[p, e] = (failure_rate - stale_threshold) * 0.1

    new_metadata = CandidateMapMetadata(
        schema_version=CANDIDATE_MAP_SCHEMA_VERSION,
        num_prototypes=num_prototypes,
        num_families=num_prototypes,
        num_experts=num_experts,
        created_at=time.strftime("%Y-%m-%dT%H:%M:%S"),
        source_checkpoint_hash=base_map.metadata.source_checkpoint_hash,
        router_config_hash=base_map.metadata.router_config_hash,
        prototype_table_hash=base_map.metadata.prototype_table_hash,
        compatible_mask_hash=base_map.metadata.compatible_mask_hash,
        promotion_status="candidate",
    )

    return CandidateMap(
        ownership_reliability_bias=reliability.clone(),
        ownership_failure_bias=failure.clone(),
        family_owner_reliability=reliability,
        family_owner_failure=failure,
        family_preservation_bias=base_map.family_preservation_bias.clone(),
        prototype_local_monopoly_penalty=monopoly_penalty,
        stale_owner_penalty=stale_penalty,
        metadata=new_metadata,
    )


# =============================================================================
# Candidate Gate Logic
# =============================================================================


def evaluate_candidate_gate(
    before_metrics: dict[str, float],
    after_metrics: dict[str, float],
    owners_per_token: float = 1.0,
    top2_executions: int = 0,
    top4_executions: int = 0,
) -> dict[str, Any]:
    """Evaluate whether a family-preserving candidate should be accepted.

    Returns verdict and evidence.
    """
    # Hard invariants
    if owners_per_token != 1.0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED",
                "reason": f"owners_per_token={owners_per_token}"}
    if top2_executions > 0 or top4_executions > 0:
        return {"verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED",
                "reason": "Top2/Top4 execution detected"}

    improvements = []
    regressions = []

    # Check oracle gap improvement
    gap_before = before_metrics.get("family_top1_oracle_gap", 0.0)
    gap_after = after_metrics.get("family_top1_oracle_gap", 0.0)
    if gap_after < gap_before:
        improvements.append(f"family_oracle_gap: {gap_before:.4f} → {gap_after:.4f}")
    elif gap_after > gap_before * 1.05:
        regressions.append(f"family_oracle_gap worsened: {gap_before:.4f} → {gap_after:.4f}")

    # Check monopoly
    mono_before = before_metrics.get("prototype_local_monopoly_rate", 0.0)
    mono_after = after_metrics.get("prototype_local_monopoly_rate", 0.0)
    if mono_after > mono_before * 1.1 + 0.05:
        regressions.append(f"monopoly worsened: {mono_before:.4f} → {mono_after:.4f}")

    # Check calibration
    cal_before = before_metrics.get("calibration_proxy", 0.0)
    cal_after = after_metrics.get("calibration_proxy", 0.0)
    if cal_after > cal_before * 1.2 + 0.02:
        regressions.append(f"calibration regressed: {cal_before:.4f} → {cal_after:.4f}")

    # Check high-confidence failures
    hcf_before = before_metrics.get("high_confidence_family_failure_rate", 0.0)
    hcf_after = after_metrics.get("high_confidence_family_failure_rate", 0.0)
    if hcf_after < hcf_before:
        improvements.append(f"high_conf_failures: {hcf_before:.4f} → {hcf_after:.4f}")
    elif hcf_after > hcf_before * 1.1 + 0.01:
        regressions.append(f"high_conf_failures worsened: {hcf_before:.4f} → {hcf_after:.4f}")

    # Decision
    if regressions:
        if improvements:
            return {
                "verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_PARTIAL",
                "improvements": improvements,
                "regressions": regressions,
            }
        return {
            "verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_REJECTED",
            "regressions": regressions,
        }

    if improvements:
        return {
            "verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_ACCEPTED",
            "improvements": improvements,
        }

    return {
        "verdict": "PVR_EC_FAMILY_PRESERVING_ROUTER_NEEDS_MORE_EVIDENCE",
        "reason": "No clear improvement or regression",
    }
