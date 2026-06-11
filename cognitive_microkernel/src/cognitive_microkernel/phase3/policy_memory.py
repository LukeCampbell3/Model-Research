"""PolicyMemory: time-decayed learned heuristics.

Stores policy decisions with exponential decay — old policies
fade unless reinforced by new evidence. This prevents stale
heuristics from dominating current decisions.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime, timedelta
from enum import Enum
import math


class DecaySchedule(Enum):
    FAST = "fast"        # Half-life: 1 hour
    NORMAL = "normal"    # Half-life: 24 hours
    SLOW = "slow"        # Half-life: 7 days
    PERMANENT = "permanent"  # No decay


DECAY_HALF_LIVES = {
    DecaySchedule.FAST: timedelta(hours=1),
    DecaySchedule.NORMAL: timedelta(hours=24),
    DecaySchedule.SLOW: timedelta(days=7),
    DecaySchedule.PERMANENT: timedelta(days=36500),  # ~100 years
}


@dataclass
class PolicyEntry:
    """A single policy entry with decay."""
    policy_id: str
    policy_type: str  # "routing", "scoring", "depth", "context"
    decision: str
    confidence: float = 1.0
    decay_schedule: DecaySchedule = DecaySchedule.NORMAL
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_reinforced: datetime = field(default_factory=datetime.utcnow)
    reinforcement_count: int = 1
    context_hash: str = ""  # What context this policy applies to

    @property
    def current_strength(self) -> float:
        """Compute current strength after decay."""
        half_life = DECAY_HALF_LIVES[self.decay_schedule]
        elapsed = datetime.utcnow() - self.last_reinforced
        decay_factor = math.exp(-0.693 * elapsed.total_seconds() / half_life.total_seconds())
        return self.confidence * decay_factor

    @property
    def is_expired(self) -> bool:
        """Policy is expired if strength < 0.1."""
        return self.current_strength < 0.1

    def reinforce(self, new_confidence: float = None) -> None:
        """Reinforce this policy (resets decay timer)."""
        self.last_reinforced = datetime.utcnow()
        self.reinforcement_count += 1
        if new_confidence is not None:
            self.confidence = new_confidence


class PolicyMemory:
    """Time-decayed policy memory.

    Policies fade over time unless reinforced by new evidence.
    This is ADVISORY — policies inform decisions but cannot override
    verification or commit gates.
    """

    def __init__(self, max_entries: int = 500, min_strength: float = 0.1):
        self._entries: dict[str, PolicyEntry] = {}
        self._max_entries = max_entries
        self._min_strength = min_strength

    @property
    def active_count(self) -> int:
        """Count of non-expired entries."""
        return sum(1 for e in self._entries.values() if not e.is_expired)

    def store(self, entry: PolicyEntry) -> None:
        """Store or update a policy entry."""
        existing = self._entries.get(entry.policy_id)
        if existing:
            existing.reinforce(entry.confidence)
        else:
            if len(self._entries) >= self._max_entries:
                self._evict_weakest()
            self._entries[entry.policy_id] = entry

    def query(self, policy_type: str, context_hash: str = "") -> list[PolicyEntry]:
        """Query active policies by type and optional context."""
        results = []
        for entry in self._entries.values():
            if entry.is_expired:
                continue
            if entry.policy_type != policy_type:
                continue
            if context_hash and entry.context_hash != context_hash:
                continue
            results.append(entry)
        results.sort(key=lambda e: e.current_strength, reverse=True)
        return results

    def get_strongest(self, policy_type: str, context_hash: str = "") -> PolicyEntry | None:
        """Get strongest active policy for a given type/context."""
        entries = self.query(policy_type, context_hash)
        return entries[0] if entries else None

    def decay_sweep(self) -> int:
        """Remove expired entries. Returns count removed."""
        expired = [k for k, v in self._entries.items() if v.is_expired]
        for k in expired:
            del self._entries[k]
        return len(expired)

    def _evict_weakest(self) -> None:
        if not self._entries:
            return
        weakest = min(self._entries, key=lambda k: self._entries[k].current_strength)
        del self._entries[weakest]
