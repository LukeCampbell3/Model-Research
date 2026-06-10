"""Branch Compiler: PassManager and optimization passes for branch processing.

Phase 2 introduces a compiler-style pass pipeline that optimizes branches
before they enter the workspace. This eliminates dead branches, merges
duplicates, detects conflicts, reduces strength, scores admission, and
produces a BranchPlan that gates workspace creation.

Only branches that pass the full compiler pipeline are admitted to the workspace.
"""

from .pass_manager import PassManager, CompilerPass, PassResult
from .dead_branch_elimination import DeadBranchElimination
from .duplicate_branch_merge import DuplicateBranchMerge
from .conflict_analysis import BasicConflictAnalysis
from .strength_reduction import StrengthReduction
from .admission_scoring import AdmissionScoring
from .branch_plan import BranchPlan, BranchPlanEntry, AdmissionStatus

__all__ = [
    "PassManager",
    "CompilerPass",
    "PassResult",
    "DeadBranchElimination",
    "DuplicateBranchMerge",
    "BasicConflictAnalysis",
    "StrengthReduction",
    "AdmissionScoring",
    "BranchPlan",
    "BranchPlanEntry",
    "AdmissionStatus",
]
