"""Adjudicator: resolve conflicts between branch outcomes.

When multiple branches produce conflicting claims or evidence,
the Adjudicator decides which to prefer based on evidence strength,
provenance, and confidence.

The Adjudicator is advisory — it recommends resolution but the
CommitManager still gates state changes.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from enum import Enum


class ConflictResolution(Enum):
    PREFER_A = "prefer_a"
    PREFER_B = "prefer_b"
    BOTH_VALID = "both_valid"
    NEITHER_VALID = "neither_valid"
    NEEDS_MORE_EVIDENCE = "needs_more_evidence"


@dataclass
class AdjudicationResult:
    """Result of adjudicating between conflicting branches."""
    conflict_id: str
    branch_a_id: str
    branch_b_id: str
    resolution: ConflictResolution
    confidence: float = 0.0
    reasoning: str = ""
    evidence_basis: list[str] = field(default_factory=list)


class Adjudicator:
    """Resolve conflicts between branch outcomes.

    Does NOT commit state. Produces AdjudicationResults that inform
    the CommitManager's decision.
    """

    def adjudicate(self, branch_a_evidence: dict[str, float],
                   branch_b_evidence: dict[str, float],
                   branch_a_id: str, branch_b_id: str,
                   conflict_id: str = "") -> AdjudicationResult:
        """Adjudicate between two conflicting branches.

        Args:
            branch_a_evidence: {evidence_id: confidence_score} for branch A
            branch_b_evidence: {evidence_id: confidence_score} for branch B
        """
        # Compute strength for each side
        strength_a = sum(branch_a_evidence.values()) if branch_a_evidence else 0.0
        strength_b = sum(branch_b_evidence.values()) if branch_b_evidence else 0.0
        count_a = len(branch_a_evidence)
        count_b = len(branch_b_evidence)

        # Decision logic
        if strength_a == 0 and strength_b == 0:
            resolution = ConflictResolution.NEEDS_MORE_EVIDENCE
            confidence = 0.0
            reasoning = "Neither side has evidence"
        elif strength_a > strength_b * 1.5:
            resolution = ConflictResolution.PREFER_A
            confidence = min(strength_a / (strength_a + strength_b + 1e-8), 0.95)
            reasoning = f"Branch A has stronger evidence ({strength_a:.2f} vs {strength_b:.2f})"
        elif strength_b > strength_a * 1.5:
            resolution = ConflictResolution.PREFER_B
            confidence = min(strength_b / (strength_a + strength_b + 1e-8), 0.95)
            reasoning = f"Branch B has stronger evidence ({strength_b:.2f} vs {strength_a:.2f})"
        elif abs(strength_a - strength_b) < 0.1:
            resolution = ConflictResolution.BOTH_VALID
            confidence = 0.5
            reasoning = "Both branches have similar evidence strength"
        else:
            resolution = ConflictResolution.NEEDS_MORE_EVIDENCE
            confidence = 0.3
            reasoning = "Evidence is inconclusive"

        return AdjudicationResult(
            conflict_id=conflict_id or f"conflict_{branch_a_id}_{branch_b_id}",
            branch_a_id=branch_a_id,
            branch_b_id=branch_b_id,
            resolution=resolution,
            confidence=confidence,
            reasoning=reasoning,
            evidence_basis=list(branch_a_evidence.keys()) + list(branch_b_evidence.keys()),
        )
