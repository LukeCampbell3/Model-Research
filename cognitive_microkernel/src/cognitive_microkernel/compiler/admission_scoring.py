"""AdmissionScoring: scores branches for workspace admission.

Computes a composite admission score based on:
- Expected upside (from branch)
- Priority score (from branch)
- Cost efficiency (upside / cost)
- Conflict penalty (from ConflictAnalysis annotations)
- Novelty bonus (dissimilarity from already-admitted branches)
- Evidence readiness (how much evidence is already available)

Branches below the admission threshold are rejected.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from cognitive_microkernel.schemas import BranchProcess
from .pass_manager import CompilerPass, PassResult


@dataclass
class AdmissionScore:
    """Detailed admission score for a branch."""
    branch_id: str
    raw_score: float
    upside_component: float
    priority_component: float
    efficiency_component: float
    conflict_penalty: float
    novelty_bonus: float
    evidence_readiness: float
    final_score: float
    admitted: bool


class AdmissionScoring(CompilerPass):
    """Score and filter branches for workspace admission."""

    @property
    def name(self) -> str:
        return "AdmissionScoring"

    def __init__(self, admission_threshold: float = 0.25, max_admitted: int = 10):
        self._threshold = admission_threshold
        self._max_admitted = max_admitted

    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        conflict_ids = annotations.get("conflict_branch_ids", set())
        scores: list[AdmissionScore] = []

        for branch in branches:
            score = self._score_branch(branch, conflict_ids)
            scores.append(score)

        # Sort by final_score descending, admit top N above threshold
        scores.sort(key=lambda s: s.final_score, reverse=True)
        admitted: list[BranchProcess] = []
        rejected: list[BranchProcess] = []
        score_map: dict[str, AdmissionScore] = {s.branch_id: s for s in scores}

        for branch in branches:
            s = score_map[branch.branch_id]
            if s.final_score >= self._threshold and len(admitted) < self._max_admitted:
                s.admitted = True
                admitted.append(branch)
            else:
                s.admitted = False
                rejected.append(branch)

        annotations["admission_scores"] = scores
        annotations["admitted_branch_ids"] = {b.branch_id for b in admitted}
        annotations["rejected_branch_ids"] = {b.branch_id for b in rejected}

        return admitted, PassResult(
            pass_name=self.name,
            branches_in=len(branches),
            branches_out=len(admitted),
            branches_eliminated=len(rejected),
            diagnostics={
                "threshold": self._threshold,
                "max_admitted": self._max_admitted,
                "scores_above_threshold": sum(1 for s in scores if s.final_score >= self._threshold),
                "avg_final_score": sum(s.final_score for s in scores) / max(len(scores), 1),
                "min_admitted_score": min((s.final_score for s in scores if s.admitted), default=0),
            },
        )

    def _score_branch(self, branch: BranchProcess, conflict_ids: set[str]) -> AdmissionScore:
        """Compute admission score for a single branch."""

        # Components (each 0-1)
        upside = min(branch.expected_upside, 1.0)
        priority = min(branch.priority_score, 1.0)

        # Efficiency: upside per unit cost
        total_cost = branch.estimated_token_cost + branch.estimated_tool_cost + 1
        efficiency = min(upside / (total_cost / 1000.0), 1.0)

        # Conflict penalty
        conflict_penalty = 0.2 if branch.branch_id in conflict_ids else 0.0

        # Evidence readiness: what fraction of needed evidence is implied available
        evidence_needed = len(branch.evidence_needed)
        evidence_readiness = 1.0 if evidence_needed == 0 else max(0.3, 1.0 - evidence_needed * 0.1)

        # Novelty bonus (placeholder — full impl would check similarity to admitted set)
        novelty = 0.1

        # Weighted composite
        raw = (
            0.30 * upside +
            0.20 * priority +
            0.20 * efficiency +
            0.15 * evidence_readiness +
            0.15 * novelty
        )
        final = max(0.0, raw - conflict_penalty)

        return AdmissionScore(
            branch_id=branch.branch_id,
            raw_score=raw,
            upside_component=upside,
            priority_component=priority,
            efficiency_component=efficiency,
            conflict_penalty=conflict_penalty,
            novelty_bonus=novelty,
            evidence_readiness=evidence_readiness,
            final_score=final,
            admitted=False,  # Set later
        )
