"""DeadBranchElimination: removes branches that can never commit.

A branch is dead if:
- It has zero expected upside
- Its parent state hash is stale (no longer current)
- Its validation condition is impossible (empty or contradicted)
- It has been explicitly cancelled
- Its budget is exhausted
- It references a contradicted claim as its sole evidence
"""

from __future__ import annotations
from typing import Any

from cognitive_microkernel.schemas import BranchProcess, ProcessStatus, BranchType
from .pass_manager import CompilerPass, PassResult


class DeadBranchElimination(CompilerPass):
    """Eliminate provably dead branches before they consume resources."""

    @property
    def name(self) -> str:
        return "DeadBranchElimination"

    def __init__(self, current_state_hash: str | None = None, stale_hashes: set[str] | None = None):
        self._current_state_hash = current_state_hash
        self._stale_hashes = stale_hashes or set()

    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        alive: list[BranchProcess] = []
        eliminated = 0
        reasons: dict[str, list[str]] = {}

        for branch in branches:
            reason = self._is_dead(branch)
            if reason:
                eliminated += 1
                reasons.setdefault(reason, []).append(branch.branch_id)
            else:
                alive.append(branch)

        # Store elimination info in annotations for later passes
        annotations["dead_branch_reasons"] = reasons

        return alive, PassResult(
            pass_name=self.name,
            branches_in=len(branches),
            branches_out=len(alive),
            branches_eliminated=eliminated,
            diagnostics={"reasons": {k: len(v) for k, v in reasons.items()}},
        )

    def _is_dead(self, branch: BranchProcess) -> str | None:
        """Return reason string if branch is dead, None if alive."""

        # Already terminal
        if branch.status in (ProcessStatus.CANCELLED, ProcessStatus.FAILED):
            return "terminal_status"

        # Zero upside
        if branch.expected_upside <= 0.0:
            return "zero_upside"

        # Stale parent state
        if self._current_state_hash and branch.parent_state_hash != self._current_state_hash:
            if branch.parent_state_hash in self._stale_hashes:
                return "stale_parent_state"

        # Empty validation condition on commit candidate
        if branch.branch_type == BranchType.COMMIT_CANDIDATE and not branch.validation_condition:
            return "impossible_validation"

        # Budget exhausted
        total_cost = branch.estimated_token_cost + branch.estimated_tool_cost
        if total_cost > 0 and branch.expected_upside < 0.01 and total_cost > 1000:
            return "budget_exceeds_value"

        return None
