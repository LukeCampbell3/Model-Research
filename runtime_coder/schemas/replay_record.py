"""ReplayRecord schema - a record for deterministic replay of execution."""

import dataclasses
from typing import List, Dict, Any

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class ReplayRecord(BaseSchema):
    """Record enabling deterministic replay of branch execution."""

    record_id: str = ""
    ticket_id: str = ""
    sequence_number: int = 0
    action_type: str = "generate"  # generate, verify, commit, rollback
    inputs: Dict[str, Any] = dataclasses.field(default_factory=dict)
    outputs: Dict[str, Any] = dataclasses.field(default_factory=dict)
    token_budget_used: int = 0
    timestamp: str = ""
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.record_id:
            errors.append("record_id must not be empty")
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        if self.sequence_number < 0:
            errors.append("sequence_number must be non-negative")
        allowed_actions = {"generate", "verify", "commit", "rollback", "branch", "merge"}
        if self.action_type not in allowed_actions:
            errors.append(f"action_type must be one of {allowed_actions}")
        return errors
