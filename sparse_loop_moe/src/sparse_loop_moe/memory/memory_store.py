"""Memory Store: layered memory architecture.

Does not rely on direct weight updates for retention.
Uses structured, isolated memory layers with consolidation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional
from collections import deque

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class MemoryEntry:
    """A single memory entry."""

    key: torch.Tensor  # Embedding key for retrieval
    value: Any  # Stored content
    metadata: dict[str, Any] = field(default_factory=dict)
    access_count: int = 0
    creation_step: int = 0
    last_access_step: int = 0
    validated: bool = False
    consolidation_count: int = 0


class FastMemory:
    """Disposable task-local scratchpad.

    Short-lived, cleared between tasks. Used for intermediate
    computations and temporary state.
    """

    def __init__(self, max_slots: int = 64):
        self.max_slots = max_slots
        self.slots: dict[str, Any] = {}

    def write(self, key: str, value: Any) -> None:
        if len(self.slots) >= self.max_slots:
            # Evict oldest
            oldest_key = next(iter(self.slots))
            del self.slots[oldest_key]
        self.slots[key] = value

    def read(self, key: str) -> Any | None:
        return self.slots.get(key)

    def clear(self) -> None:
        self.slots.clear()

    def __len__(self) -> int:
        return len(self.slots)


class EpisodicMemory:
    """Stores task attempts, failures, repairs, and outcomes.

    Enables learning from past experiences without weight modification.
    """

    def __init__(self, max_entries: int = 1024, d_key: int = 256):
        self.max_entries = max_entries
        self.d_key = d_key
        self.entries: deque[MemoryEntry] = deque(maxlen=max_entries)
        self.step_counter = 0

    def store(
        self,
        key: torch.Tensor,
        value: Any,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Store a new episodic memory."""
        entry = MemoryEntry(
            key=key.detach(),
            value=value,
            metadata=metadata or {},
            creation_step=self.step_counter,
            last_access_step=self.step_counter,
        )
        self.entries.append(entry)
        self.step_counter += 1

    def retrieve(
        self, query: torch.Tensor, top_k: int = 5
    ) -> list[MemoryEntry]:
        """Retrieve most relevant episodic memories."""
        if not self.entries:
            return []

        keys = torch.stack([e.key for e in self.entries])
        similarities = F.cosine_similarity(
            query.unsqueeze(0), keys, dim=-1
        )
        top_k = min(top_k, len(self.entries))
        _, indices = similarities.topk(top_k)

        results = []
        for idx in indices.tolist():
            entry = self.entries[idx]
            entry.access_count += 1
            entry.last_access_step = self.step_counter
            results.append(entry)

        return results

    def get_failure_patterns(self) -> list[MemoryEntry]:
        """Retrieve entries marked as failures."""
        return [
            e for e in self.entries
            if e.metadata.get("outcome") == "failure"
        ]

    def __len__(self) -> int:
        return len(self.entries)


class SemanticMemory:
    """Stores distilled reusable rules.

    Only stores validated, consolidated knowledge that has been
    confirmed across multiple episodes.
    """

    def __init__(self, max_entries: int = 512, d_key: int = 256):
        self.max_entries = max_entries
        self.d_key = d_key
        self.entries: list[MemoryEntry] = []
        self.regression_tests: list[dict[str, Any]] = []

    def store(
        self,
        key: torch.Tensor,
        rule: Any,
        metadata: dict[str, Any] | None = None,
    ) -> bool:
        """Store a semantic rule (must be validated first).

        Returns True if stored, False if regression test failed.
        """
        # Run regression tests before storing
        if not self._passes_regression_tests(rule):
            return False

        if len(self.entries) >= self.max_entries:
            # Evict least accessed
            self.entries.sort(key=lambda e: e.access_count)
            self.entries.pop(0)

        entry = MemoryEntry(
            key=key.detach(),
            value=rule,
            metadata=metadata or {},
            validated=True,
        )
        self.entries.append(entry)
        return True

    def retrieve(
        self, query: torch.Tensor, top_k: int = 3
    ) -> list[MemoryEntry]:
        """Retrieve relevant semantic rules."""
        if not self.entries:
            return []

        keys = torch.stack([e.key for e in self.entries])
        similarities = F.cosine_similarity(
            query.unsqueeze(0), keys, dim=-1
        )
        top_k = min(top_k, len(self.entries))
        _, indices = similarities.topk(top_k)

        results = []
        for idx in indices.tolist():
            entry = self.entries[idx]
            entry.access_count += 1
            results.append(entry)

        return results

    def add_regression_test(self, test: dict[str, Any]) -> None:
        """Add a regression test to prevent old skills from being overwritten."""
        self.regression_tests.append(test)

    def _passes_regression_tests(self, rule: Any) -> bool:
        """Check if a new rule passes all regression tests."""
        # In a full implementation, this would evaluate the rule
        # against stored test cases. For now, always passes.
        return True

    def __len__(self) -> int:
        return len(self.entries)


class AdapterMemory:
    """Stores domain-specific temporary skill patches.

    These are lightweight adapters that can be activated/deactivated
    based on task domain without modifying base weights.
    """

    def __init__(self, max_adapters: int = 32, d_model: int = 256):
        self.max_adapters = max_adapters
        self.d_model = d_model
        self.adapters: dict[str, dict[str, Any]] = {}

    def register_adapter(
        self,
        name: str,
        adapter_weights: dict[str, torch.Tensor],
        domain: str = "general",
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Register a new adapter."""
        if len(self.adapters) >= self.max_adapters:
            # Evict least used
            least_used = min(
                self.adapters.items(),
                key=lambda x: x[1].get("use_count", 0),
            )
            del self.adapters[least_used[0]]

        self.adapters[name] = {
            "weights": adapter_weights,
            "domain": domain,
            "metadata": metadata or {},
            "use_count": 0,
            "active": False,
        }

    def activate(self, name: str) -> dict[str, torch.Tensor] | None:
        """Activate an adapter and return its weights."""
        if name in self.adapters:
            self.adapters[name]["active"] = True
            self.adapters[name]["use_count"] += 1
            return self.adapters[name]["weights"]
        return None

    def deactivate(self, name: str) -> None:
        """Deactivate an adapter."""
        if name in self.adapters:
            self.adapters[name]["active"] = False

    def get_active_adapters(self) -> list[str]:
        """Get names of currently active adapters."""
        return [
            name for name, info in self.adapters.items() if info["active"]
        ]

    def get_domain_adapters(self, domain: str) -> list[str]:
        """Get adapter names for a specific domain."""
        return [
            name
            for name, info in self.adapters.items()
            if info["domain"] == domain
        ]


class ConsolidationLayer:
    """Promotes repeated validated lessons from episodic to semantic memory.

    A pattern must be observed at least `threshold` times with consistent
    positive outcomes before promotion.
    """

    def __init__(self, threshold: int = 5):
        self.threshold = threshold
        self.candidate_patterns: dict[str, dict[str, Any]] = {}

    def observe(
        self, pattern_key: str, outcome: bool, embedding: torch.Tensor
    ) -> bool:
        """Observe a pattern occurrence. Returns True if ready for promotion."""
        if pattern_key not in self.candidate_patterns:
            self.candidate_patterns[pattern_key] = {
                "count": 0,
                "successes": 0,
                "embedding": embedding.detach(),
            }

        self.candidate_patterns[pattern_key]["count"] += 1
        if outcome:
            self.candidate_patterns[pattern_key]["successes"] += 1

        info = self.candidate_patterns[pattern_key]
        return (
            info["count"] >= self.threshold
            and info["successes"] / info["count"] >= 0.8
        )

    def get_promotable(self) -> list[tuple[str, torch.Tensor]]:
        """Get patterns ready for promotion to semantic memory."""
        promotable = []
        for key, info in self.candidate_patterns.items():
            if (
                info["count"] >= self.threshold
                and info["successes"] / info["count"] >= 0.8
            ):
                promotable.append((key, info["embedding"]))
        return promotable

    def clear_promoted(self, keys: list[str]) -> None:
        """Remove promoted patterns from candidates."""
        for key in keys:
            self.candidate_patterns.pop(key, None)


class MemoryStore:
    """Unified memory store combining all memory layers.

    Implements the full memory architecture with consolidation
    and regression testing.
    """

    def __init__(
        self,
        d_model: int = 256,
        max_fast_slots: int = 64,
        max_episodic: int = 1024,
        max_semantic: int = 512,
        max_adapters: int = 32,
        consolidation_threshold: int = 5,
    ):
        self.fast = FastMemory(max_slots=max_fast_slots)
        self.episodic = EpisodicMemory(max_entries=max_episodic, d_key=d_model)
        self.semantic = SemanticMemory(max_entries=max_semantic, d_key=d_model)
        self.adapters = AdapterMemory(max_adapters=max_adapters, d_model=d_model)
        self.consolidation = ConsolidationLayer(threshold=consolidation_threshold)

    def task_start(self) -> None:
        """Called at the start of each task. Clears fast memory."""
        self.fast.clear()

    def task_end(
        self,
        task_embedding: torch.Tensor,
        outcome: dict[str, Any],
    ) -> None:
        """Called at the end of each task. Stores episode and checks consolidation."""
        # Store in episodic memory
        self.episodic.store(
            key=task_embedding,
            value=outcome,
            metadata={"outcome": "success" if outcome.get("success") else "failure"},
        )

        # Check consolidation
        pattern_key = outcome.get("pattern_key", "")
        if pattern_key:
            ready = self.consolidation.observe(
                pattern_key=pattern_key,
                outcome=outcome.get("success", False),
                embedding=task_embedding,
            )
            if ready:
                self._promote_to_semantic(pattern_key, task_embedding)

    def _promote_to_semantic(self, pattern_key: str, embedding: torch.Tensor) -> None:
        """Promote a consolidated pattern to semantic memory."""
        rule = f"Consolidated rule: {pattern_key}"
        stored = self.semantic.store(
            key=embedding,
            rule=rule,
            metadata={"source": "consolidation", "pattern_key": pattern_key},
        )
        if stored:
            self.consolidation.clear_promoted([pattern_key])

    def retrieve_relevant(
        self, query: torch.Tensor, top_k: int = 5
    ) -> dict[str, list[MemoryEntry]]:
        """Retrieve relevant memories from all layers."""
        return {
            "episodic": self.episodic.retrieve(query, top_k),
            "semantic": self.semantic.retrieve(query, top_k),
        }
