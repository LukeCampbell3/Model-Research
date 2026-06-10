"""StrengthReduction: simplifies over-specified branches.

Reduces complexity by:
- Collapsing redundant evidence_needed entries
- Reducing estimated costs for branches with simple hypotheses
- Downgrading branch_type from COMMIT_CANDIDATE to BRANCH_SKETCH if prerequisites missing
- Simplifying overly broad context_refs_needed
- Clamping unrealistic expected_upside values
"""

from __future__ import annotations
from typing import Any

from cognitive_microkernel.schemas import BranchProcess, BranchType
from .pass_manager import CompilerPass, PassResult


class StrengthReduction(CompilerPass):
    """Reduce branch complexity without changing semantics."""

    @property
    def name(self) -> str:
        return "StrengthReduction"

    def __init__(self, max_evidence_needed: int = 10, max_context_refs: int = 5,
                 max_upside: float = 0.95):
        self._max_evidence = max_evidence_needed
        self._max_context = max_context_refs
        self._max_upside = max_upside

    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        modified = 0
        reductions: dict[str, int] = {}

        for branch in branches:
            changes = self._reduce(branch)
            if changes:
                modified += 1
                for change in changes:
                    reductions[change] = reductions.get(change, 0) + 1

        annotations["strength_reductions"] = reductions

        return branches, PassResult(
            pass_name=self.name,
            branches_in=len(branches),
            branches_out=len(branches),
            branches_modified=modified,
            diagnostics={"reductions": reductions},
        )

    def _reduce(self, branch: BranchProcess) -> list[str]:
        """Apply strength reductions. Returns list of applied reduction names."""
        changes: list[str] = []

        # Deduplicate evidence_needed
        original_ev = len(branch.evidence_needed)
        branch.evidence_needed = list(set(branch.evidence_needed))
        if len(branch.evidence_needed) < original_ev:
            changes.append("dedup_evidence_needed")

        # Cap evidence_needed to max
        if len(branch.evidence_needed) > self._max_evidence:
            branch.evidence_needed = branch.evidence_needed[:self._max_evidence]
            changes.append("cap_evidence_needed")

        # Deduplicate and cap context_refs
        original_ctx = len(branch.context_refs_needed)
        branch.context_refs_needed = list(set(branch.context_refs_needed))
        if len(branch.context_refs_needed) > self._max_context:
            branch.context_refs_needed = branch.context_refs_needed[:self._max_context]
            changes.append("cap_context_refs")

        # Clamp unrealistic expected_upside
        if branch.expected_upside > self._max_upside:
            branch.expected_upside = self._max_upside
            changes.append("clamp_upside")

        # Downgrade commit candidate without validation condition to sketch
        if (branch.branch_type == BranchType.COMMIT_CANDIDATE and
            not branch.validation_condition):
            branch.branch_type = BranchType.BRANCH_SKETCH
            changes.append("downgrade_to_sketch")

        # Reduce cost estimate for trivial hypotheses
        words = branch.hypothesis.split()
        if len(words) <= 3 and branch.estimated_token_cost > 500:
            branch.estimated_token_cost = 200
            changes.append("reduce_trivial_cost")

        return changes
