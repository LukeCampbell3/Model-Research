"""BranchIR schema - intermediate representation for a branch execution."""

import dataclasses
from typing import List, Dict, Any, Optional

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class BranchIR(BaseSchema):
    """Intermediate representation of a branch's planned execution."""

    ir_id: str = ""
    ticket_id: str = ""
    steps: List[Dict[str, Any]] = dataclasses.field(default_factory=list)
    dependencies: List[str] = dataclasses.field(default_factory=list)
    estimated_tokens: int = 0
    optimization_hints: Dict[str, Any] = dataclasses.field(default_factory=dict)
    status: str = "pending"  # pending, executing, completed, failed
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.ir_id:
            errors.append("ir_id must not be empty")
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        if not self.steps:
            errors.append("steps must contain at least one step")
        allowed_statuses = {"pending", "executing", "completed", "failed", "cancelled"}
        if self.status not in allowed_statuses:
            errors.append(f"status must be one of {allowed_statuses}")
        return errors
