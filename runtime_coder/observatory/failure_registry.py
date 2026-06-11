"""Failure registry for tracking and categorizing failure modes."""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class FailureEntry:
    """A single failure mode entry."""
    failure_id: str = ""
    category: str = "unknown"  # validation, runtime, verifier, compliance, model
    description: str = ""
    severity: str = "medium"  # low, medium, high, critical
    ticket_id: Optional[str] = None
    context: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = ""
    resolved: bool = False


class FailureRegistry:
    """Registry for tracking failure modes during execution."""

    ALLOWED_CATEGORIES = {"validation", "runtime", "verifier", "compliance", "model", "unknown"}
    ALLOWED_SEVERITIES = {"low", "medium", "high", "critical"}

    def __init__(self):
        self._failures: List[FailureEntry] = []

    def register(
        self,
        failure_id: str,
        category: str = "unknown",
        description: str = "",
        severity: str = "medium",
        ticket_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        timestamp: str = "",
    ) -> FailureEntry:
        """Register a new failure mode."""
        entry = FailureEntry(
            failure_id=failure_id,
            category=category if category in self.ALLOWED_CATEGORIES else "unknown",
            description=description,
            severity=severity if severity in self.ALLOWED_SEVERITIES else "medium",
            ticket_id=ticket_id,
            context=context or {},
            timestamp=timestamp,
        )
        self._failures.append(entry)
        return entry

    def resolve(self, failure_id: str) -> bool:
        """Mark a failure as resolved."""
        for entry in self._failures:
            if entry.failure_id == failure_id:
                entry.resolved = True
                return True
        return False

    def get_unresolved(self) -> List[FailureEntry]:
        """Get all unresolved failures."""
        return [f for f in self._failures if not f.resolved]

    def get_by_category(self, category: str) -> List[FailureEntry]:
        """Get failures filtered by category."""
        return [f for f in self._failures if f.category == category]

    def get_by_severity(self, severity: str) -> List[FailureEntry]:
        """Get failures filtered by severity."""
        return [f for f in self._failures if f.severity == severity]

    def summary(self) -> Dict[str, Any]:
        """Get summary statistics."""
        total = len(self._failures)
        unresolved = len(self.get_unresolved())
        by_category = {}
        for cat in self.ALLOWED_CATEGORIES:
            count = len(self.get_by_category(cat))
            if count > 0:
                by_category[cat] = count
        by_severity = {}
        for sev in self.ALLOWED_SEVERITIES:
            count = len(self.get_by_severity(sev))
            if count > 0:
                by_severity[sev] = count
        return {
            "total": total,
            "unresolved": unresolved,
            "resolved": total - unresolved,
            "by_category": by_category,
            "by_severity": by_severity,
        }

    def clear(self):
        """Clear all entries."""
        self._failures.clear()
