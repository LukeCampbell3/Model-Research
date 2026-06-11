"""BranchTicket schema - represents a branch execution ticket with validation."""

import dataclasses
from typing import List, Optional, Dict, Any

from runtime_coder.schemas.base import BaseSchema

ALLOWED_BRANCH_TYPES = {"patch", "refactor", "test", "documentation", "exploration", "fix"}
ALLOWED_PRIVILEGE_LEVELS = {"read_only", "read_write", "admin", "sandboxed"}


@dataclasses.dataclass
class BranchTicket(BaseSchema):
    """A ticket authorizing a branch of execution."""

    ticket_id: str = ""
    branch_type: str = "patch"
    privilege_level: str = "read_write"
    description: str = ""
    read_set: List[str] = dataclasses.field(default_factory=list)
    write_set: List[str] = dataclasses.field(default_factory=list)
    verifier_targets: List[str] = dataclasses.field(default_factory=list)
    constraints: List[str] = dataclasses.field(default_factory=list)
    parent_ticket_id: Optional[str] = None
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        if self.branch_type not in ALLOWED_BRANCH_TYPES:
            errors.append(
                f"branch_type '{self.branch_type}' not in allowed set: {ALLOWED_BRANCH_TYPES}"
            )
        if self.privilege_level not in ALLOWED_PRIVILEGE_LEVELS:
            errors.append(
                f"privilege_level '{self.privilege_level}' not in allowed set: {ALLOWED_PRIVILEGE_LEVELS}"
            )
        # Patch-specific validations
        if self.branch_type == "patch":
            if not self.read_set:
                errors.append("read_set must be non-empty for patch branches")
            if not self.write_set:
                errors.append("write_set must be present for patch branches")
            if not self.verifier_targets:
                errors.append("verifier_targets must be present for patch branches")
        return errors
