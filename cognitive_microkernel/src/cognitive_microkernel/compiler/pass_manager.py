"""PassManager: orchestrates compiler passes over branch sets.

Each pass receives the current branch set and annotations, transforms them,
and returns a PassResult. The PassManager runs passes in registered order
and accumulates diagnostics.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from cognitive_microkernel.schemas import BranchProcess


@dataclass
class PassResult:
    """Result from a single compiler pass."""
    pass_name: str
    branches_in: int
    branches_out: int
    branches_eliminated: int = 0
    branches_merged: int = 0
    branches_modified: int = 0
    conflicts_detected: int = 0
    diagnostics: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class CompilerPass(ABC):
    """Base class for branch compiler passes."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique pass name."""
        ...

    @abstractmethod
    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        """Execute the pass.

        Args:
            branches: Current branch set.
            annotations: Mutable annotations dict shared across passes.

        Returns:
            (transformed_branches, result)
        """
        ...


class PassManager:
    """Runs a sequence of compiler passes over a branch set.

    Passes execute in registration order. Each pass receives the output
    of the previous pass. The manager collects all PassResults and can
    short-circuit on fatal errors.
    """

    def __init__(self):
        self._passes: list[CompilerPass] = []
        self._results: list[PassResult] = []

    def register(self, compiler_pass: CompilerPass) -> "PassManager":
        """Register a pass. Returns self for chaining."""
        self._passes.append(compiler_pass)
        return self

    @property
    def passes(self) -> list[CompilerPass]:
        return list(self._passes)

    @property
    def results(self) -> list[PassResult]:
        return list(self._results)

    def run(self, branches: list[BranchProcess]) -> tuple[list[BranchProcess], list[PassResult]]:
        """Run all registered passes in order.

        Returns:
            (final_branches, all_pass_results)
        """
        self._results = []
        annotations: dict[str, Any] = {}
        current = branches

        for compiler_pass in self._passes:
            current, result = compiler_pass.run(current, annotations)
            self._results.append(result)

            if result.error:
                # Fatal error — stop pipeline
                break

        return current, self._results

    def summary(self) -> dict[str, Any]:
        """Produce a summary of the full compilation."""
        if not self._results:
            return {"status": "NOT_RUN", "passes": 0}

        total_eliminated = sum(r.branches_eliminated for r in self._results)
        total_merged = sum(r.branches_merged for r in self._results)
        total_conflicts = sum(r.conflicts_detected for r in self._results)
        errors = [r for r in self._results if r.error]

        return {
            "status": "ERROR" if errors else "COMPLETE",
            "passes_run": len(self._results),
            "branches_in": self._results[0].branches_in if self._results else 0,
            "branches_out": self._results[-1].branches_out if self._results else 0,
            "total_eliminated": total_eliminated,
            "total_merged": total_merged,
            "total_conflicts": total_conflicts,
            "errors": [r.error for r in errors],
        }
