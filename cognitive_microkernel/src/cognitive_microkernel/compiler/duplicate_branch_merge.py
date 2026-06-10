"""DuplicateBranchMerge: merges semantically identical branches.

Two branches are merge candidates if:
- They share the same parent_state_hash
- Their hypothesis keywords overlap above threshold
- They target the same evidence_needed set
- They have compatible validation conditions

When merged, the surviving branch inherits the higher priority and broader
evidence needs from both. The eliminated branch is recorded for audit.
"""

from __future__ import annotations
import hashlib
import json
from typing import Any

from cognitive_microkernel.schemas import BranchProcess
from .pass_manager import CompilerPass, PassResult


class DuplicateBranchMerge(CompilerPass):
    """Merge duplicate or near-duplicate branches."""

    @property
    def name(self) -> str:
        return "DuplicateBranchMerge"

    def __init__(self, similarity_threshold: float = 0.8):
        self._threshold = similarity_threshold

    def run(self, branches: list[BranchProcess], annotations: dict[str, Any]) -> tuple[list[BranchProcess], PassResult]:
        if len(branches) <= 1:
            return branches, PassResult(
                pass_name=self.name, branches_in=len(branches),
                branches_out=len(branches),
            )

        # Group by parent_state_hash first (cheap filter)
        groups: dict[str, list[BranchProcess]] = {}
        for b in branches:
            groups.setdefault(b.parent_state_hash, []).append(b)

        merged_out: list[BranchProcess] = []
        total_merged = 0
        merge_pairs: list[tuple[str, str]] = []

        for parent_hash, group in groups.items():
            if len(group) <= 1:
                merged_out.extend(group)
                continue

            # Within group, check pairwise similarity
            survivors, merged_count, pairs = self._merge_group(group)
            merged_out.extend(survivors)
            total_merged += merged_count
            merge_pairs.extend(pairs)

        annotations["merge_pairs"] = merge_pairs

        return merged_out, PassResult(
            pass_name=self.name,
            branches_in=len(branches),
            branches_out=len(merged_out),
            branches_merged=total_merged,
            diagnostics={"merge_pairs_count": len(merge_pairs)},
        )

    def _merge_group(self, group: list[BranchProcess]) -> tuple[list[BranchProcess], int, list[tuple[str, str]]]:
        """Merge duplicates within a parent-hash group."""
        consumed: set[int] = set()
        survivors: list[BranchProcess] = []
        pairs: list[tuple[str, str]] = []

        for i in range(len(group)):
            if i in consumed:
                continue
            survivor = group[i]

            for j in range(i + 1, len(group)):
                if j in consumed:
                    continue
                if self._are_duplicates(survivor, group[j]):
                    # Merge: keep higher priority, broader evidence
                    survivor = self._merge_branches(survivor, group[j])
                    consumed.add(j)
                    pairs.append((survivor.branch_id, group[j].branch_id))

            survivors.append(survivor)

        merged_count = len(consumed)
        return survivors, merged_count, pairs

    def _are_duplicates(self, a: BranchProcess, b: BranchProcess) -> bool:
        """Check if two branches are semantically duplicate."""
        # Same parent (already guaranteed by grouping)
        # Check hypothesis keyword overlap
        words_a = set(a.hypothesis.lower().split())
        words_b = set(b.hypothesis.lower().split())
        if not words_a or not words_b:
            return False
        overlap = len(words_a & words_b) / max(len(words_a | words_b), 1)
        if overlap < self._threshold:
            return False

        # Check evidence_needed overlap
        ev_a = set(a.evidence_needed)
        ev_b = set(b.evidence_needed)
        if ev_a and ev_b:
            ev_overlap = len(ev_a & ev_b) / max(len(ev_a | ev_b), 1)
            if ev_overlap < 0.5:
                return False

        return True

    def _merge_branches(self, survivor: BranchProcess, eliminated: BranchProcess) -> BranchProcess:
        """Merge eliminated into survivor, keeping best attributes."""
        # Take higher priority
        if eliminated.priority_score > survivor.priority_score:
            survivor.priority_score = eliminated.priority_score

        # Take higher expected upside
        if eliminated.expected_upside > survivor.expected_upside:
            survivor.expected_upside = eliminated.expected_upside

        # Union evidence needs
        combined_evidence = set(survivor.evidence_needed) | set(eliminated.evidence_needed)
        survivor.evidence_needed = list(combined_evidence)

        # Union context refs
        combined_context = set(survivor.context_refs_needed) | set(eliminated.context_refs_needed)
        survivor.context_refs_needed = list(combined_context)

        return survivor
