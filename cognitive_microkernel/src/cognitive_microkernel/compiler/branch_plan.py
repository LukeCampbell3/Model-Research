"""BranchPlan: the output of the compiler pipeline.

A BranchPlan contains:
- The admitted branch set (workspace-ready)
- Admission scores and reasons
- Rejected branches with rejection reasons
- Conflict annotations
- Resource estimates for the admitted workspace
- Workspace creation gate (only admitted branches get a workspace)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from cognitive_microkernel.schemas import BranchProcess
from .pass_manager import PassResult
from .admission_scoring import AdmissionScore


class AdmissionStatus(Enum):
    ADMITTED = "admitted"
    REJECTED_BELOW_THRESHOLD = "rejected_below_threshold"
    REJECTED_CAPACITY = "rejected_capacity"
    ELIMINATED_DEAD = "eliminated_dead"
    ELIMINATED_DUPLICATE = "eliminated_duplicate"


@dataclass
class BranchPlanEntry:
    """A single entry in the branch plan."""
    branch: BranchProcess
    status: AdmissionStatus
    score: float
    rejection_reason: str | None = None
    merged_into: str | None = None  # branch_id it was merged into


@dataclass
class BranchPlan:
    """Complete branch plan produced by the compiler.

    Only branches with status=ADMITTED are given workspaces.
    """
    entries: list[BranchPlanEntry] = field(default_factory=list)
    pass_results: list[PassResult] = field(default_factory=list)
    total_input_branches: int = 0
    compiler_annotations: dict[str, Any] = field(default_factory=dict)

    @property
    def admitted(self) -> list[BranchProcess]:
        """Branches admitted to workspace."""
        return [e.branch for e in self.entries if e.status == AdmissionStatus.ADMITTED]

    @property
    def rejected(self) -> list[BranchPlanEntry]:
        """Entries that were not admitted."""
        return [e for e in self.entries if e.status != AdmissionStatus.ADMITTED]

    @property
    def admitted_count(self) -> int:
        return len(self.admitted)

    @property
    def rejected_count(self) -> int:
        return len(self.rejected)

    @property
    def workspace_budget(self) -> float:
        """Estimated total budget needed for admitted branches."""
        return sum(
            b.estimated_token_cost + b.estimated_tool_cost
            for b in self.admitted
        )

    @property
    def can_create_workspace(self) -> bool:
        """Whether the plan has any admitted branches worth a workspace."""
        return self.admitted_count > 0

    def get_entry(self, branch_id: str) -> BranchPlanEntry | None:
        """Get entry by branch ID."""
        for e in self.entries:
            if e.branch.branch_id == branch_id:
                return e
        return None

    def summary(self) -> dict[str, Any]:
        """Human-readable summary of the plan."""
        status_counts: dict[str, int] = {}
        for e in self.entries:
            status_counts[e.status.value] = status_counts.get(e.status.value, 0) + 1

        return {
            "total_input": self.total_input_branches,
            "admitted": self.admitted_count,
            "rejected": self.rejected_count,
            "workspace_budget": self.workspace_budget,
            "can_create_workspace": self.can_create_workspace,
            "status_distribution": status_counts,
            "passes_run": len(self.pass_results),
        }


def compile_branch_plan(
    branches: list[BranchProcess],
    pass_results: list[PassResult],
    admitted_branches: list[BranchProcess],
    annotations: dict[str, Any],
) -> BranchPlan:
    """Assemble a BranchPlan from compiler outputs.

    Args:
        branches: Original input branches
        pass_results: Results from all passes
        admitted_branches: Branches that passed admission
        annotations: Full annotation dict from PassManager
    """
    admitted_ids = {b.branch_id for b in admitted_branches}
    dead_reasons = annotations.get("dead_branch_reasons", {})
    merge_pairs = annotations.get("merge_pairs", [])
    merged_ids = {pair[1] for pair in merge_pairs}  # Second in pair was eliminated

    entries: list[BranchPlanEntry] = []

    for branch in branches:
        if branch.branch_id in admitted_ids:
            score_val = 0.5  # Default
            scores = annotations.get("admission_scores", [])
            for s in scores:
                if s.branch_id == branch.branch_id:
                    score_val = s.final_score
                    break
            entries.append(BranchPlanEntry(
                branch=branch, status=AdmissionStatus.ADMITTED, score=score_val,
            ))
        elif branch.branch_id in merged_ids:
            entries.append(BranchPlanEntry(
                branch=branch, status=AdmissionStatus.ELIMINATED_DUPLICATE,
                score=0.0, rejection_reason="Merged into duplicate",
            ))
        elif any(branch.branch_id in ids for ids in dead_reasons.values()):
            reason = next(
                (k for k, ids in dead_reasons.items() if branch.branch_id in ids), "dead"
            )
            entries.append(BranchPlanEntry(
                branch=branch, status=AdmissionStatus.ELIMINATED_DEAD,
                score=0.0, rejection_reason=reason,
            ))
        else:
            entries.append(BranchPlanEntry(
                branch=branch, status=AdmissionStatus.REJECTED_BELOW_THRESHOLD,
                score=0.0, rejection_reason="Below admission threshold",
            ))

    return BranchPlan(
        entries=entries,
        pass_results=pass_results,
        total_input_branches=len(branches),
        compiler_annotations=annotations,
    )
