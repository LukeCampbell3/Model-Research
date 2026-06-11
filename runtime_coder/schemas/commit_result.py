"""CommitResult schema - result from committing a branch's output."""

import dataclasses
from typing import List, Dict, Any

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class CommitResult(BaseSchema):
    """Result of committing a completed branch execution."""

    commit_id: str = ""
    ticket_id: str = ""
    committed: bool = False
    files_modified: List[str] = dataclasses.field(default_factory=list)
    files_created: List[str] = dataclasses.field(default_factory=list)
    files_deleted: List[str] = dataclasses.field(default_factory=list)
    rollback_available: bool = True
    verifier_summary: Dict[str, Any] = dataclasses.field(default_factory=dict)
    metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.commit_id:
            errors.append("commit_id must not be empty")
        if not self.ticket_id:
            errors.append("ticket_id must not be empty")
        return errors
