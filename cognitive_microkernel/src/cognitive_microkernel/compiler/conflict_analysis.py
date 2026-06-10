"""BasicConflictAnalysis: detects branches that conflict with each other.

Conflicts arise when:
- Two branches target the same state region with incompatible changes
- A branch contradicts existing evidence
- Two branches have mutually exclusive validation conditions
- A branch's hypothesis contradicts another's established claim

Detected conflicts are annotated but do NOT eliminate branches.
The admission scorer uses conflict info to downgrade priorities.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from cognitive_microkernel.schemas import BranchProcess, BranchType
from .pass_manager import CompilerPass, PassResult


@dataclass
class ConflictRecord:
    """A detected conflict between two branches."""
    branch_a_id: str
    branch_b_id: str
    conflict_type: str  # "mutual_exclusion", "state_region_overlap", "hypothesis_contradiction"
    severity: float  # 0.0 - 1.0
    description: str


class BasicConflictAnalysis(CompilerPass):
    """Detect conflicts between branches without eliminating them."""

    @property
    def name(self) -> str:
        return "BasicConflictAnalysis"

    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        conflicts: list[ConflictRecord] = []

        for i in range(len(branches)):
            for j in range(i + 1, len(branches)):
                conflict = self._detect_conflict(branches[i], branches[j])
                if conflict:
                    conflicts.append(conflict)

        # Store conflicts in annotations for downstream passes
        annotations["conflicts"] = conflicts
        annotations["conflict_branch_ids"] = set()
        for c in conflicts:
            annotations["conflict_branch_ids"].add(c.branch_a_id)
            annotations["conflict_branch_ids"].add(c.branch_b_id)

        return branches, PassResult(
            pass_name=self.name,
            branches_in=len(branches),
            branches_out=len(branches),  # No elimination
            conflicts_detected=len(conflicts),
            diagnostics={
                "conflict_types": self._count_types(conflicts),
                "avg_severity": sum(c.severity for c in conflicts) / max(len(conflicts), 1),
            },
        )

    def _detect_conflict(self, a: BranchProcess, b: BranchProcess) -> ConflictRecord | None:
        """Detect if two branches conflict."""

        # Same parent, both commit candidates → potential state region overlap
        if (a.parent_state_hash == b.parent_state_hash and
            a.branch_type == BranchType.COMMIT_CANDIDATE and
            b.branch_type == BranchType.COMMIT_CANDIDATE):
            return ConflictRecord(
                branch_a_id=a.branch_id,
                branch_b_id=b.branch_id,
                conflict_type="state_region_overlap",
                severity=0.7,
                description="Two commit candidates target same parent state",
            )

        # Check hypothesis contradiction via negation keywords
        neg_keywords = {"not", "don't", "won't", "cannot", "never", "opposite", "instead"}
        words_a = set(a.hypothesis.lower().split())
        words_b = set(b.hypothesis.lower().split())
        shared_content = words_a & words_b - neg_keywords
        a_negated = bool(words_a & neg_keywords)
        b_negated = bool(words_b & neg_keywords)

        if shared_content and (a_negated != b_negated):
            return ConflictRecord(
                branch_a_id=a.branch_id,
                branch_b_id=b.branch_id,
                conflict_type="hypothesis_contradiction",
                severity=0.5,
                description=f"Contradictory hypotheses on: {shared_content}",
            )

        # Mutually exclusive validation conditions
        if (a.validation_condition and b.validation_condition and
            a.validation_condition == f"NOT({b.validation_condition})"):
            return ConflictRecord(
                branch_a_id=a.branch_id,
                branch_b_id=b.branch_id,
                conflict_type="mutual_exclusion",
                severity=0.9,
                description="Mutually exclusive validation conditions",
            )

        return None

    def _count_types(self, conflicts: list[ConflictRecord]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for c in conflicts:
            counts[c.conflict_type] = counts.get(c.conflict_type, 0) + 1
        return counts
