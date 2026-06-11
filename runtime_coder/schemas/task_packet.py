"""TaskPacket schema - represents a coding task to be executed."""

import dataclasses
from typing import List, Optional

from runtime_coder.schemas.base import BaseSchema


@dataclasses.dataclass
class TaskPacket(BaseSchema):
    """A coding task dispatched to the runtime."""

    task_id: str = ""
    task_type: str = "code_generation"
    description: str = ""
    constraints: List[str] = dataclasses.field(default_factory=list)
    context_refs: List[str] = dataclasses.field(default_factory=list)
    priority: int = 0
    metadata: dict = dataclasses.field(default_factory=dict)

    def validate(self) -> list:
        errors = super().validate()
        if not self.task_id:
            errors.append("task_id must not be empty")
        if not self.task_type:
            errors.append("task_type must not be empty")
        return errors
