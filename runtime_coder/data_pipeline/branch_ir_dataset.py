"""BranchIR SFT dataset generation for Phase 2.

Generates BranchIR training examples: BranchTicket input -> BranchIR output.
Covers different action types (edit, test, inspect, summarize).
"""

import dataclasses
import random
from typing import Dict, Any, List

from runtime_coder.schemas.branch_ir import BranchIR
from runtime_coder.schemas.branch_ticket import BranchTicket
from runtime_coder.tokenizer.runtime_special_tokens import BRANCH_TOKENS


# Action type templates for IR steps
ACTION_TEMPLATES = {
    "edit": [
        {"action": "read", "target": "{read_file}", "description": "Read current implementation"},
        {"action": "edit", "target": "{write_file}", "description": "Apply changes"},
        {"action": "verify", "target": "{verifier}", "description": "Run verification"},
    ],
    "test": [
        {"action": "inspect", "target": "{read_file}", "description": "Inspect code under test"},
        {"action": "generate", "target": "{write_file}", "description": "Generate test cases"},
        {"action": "execute", "target": "{verifier}", "description": "Execute tests"},
        {"action": "validate", "target": "{verifier}", "description": "Validate coverage"},
    ],
    "inspect": [
        {"action": "read", "target": "{read_file}", "description": "Read target file"},
        {"action": "analyze", "target": "{read_file}", "description": "Analyze code structure"},
        {"action": "summarize", "target": "report", "description": "Generate summary"},
    ],
    "summarize": [
        {"action": "read", "target": "{read_file}", "description": "Read source"},
        {"action": "extract", "target": "{read_file}", "description": "Extract key info"},
        {"action": "summarize", "target": "summary.md", "description": "Produce summary document"},
    ],
    "refactor": [
        {"action": "read", "target": "{read_file}", "description": "Read current code"},
        {"action": "plan", "target": "{write_file}", "description": "Plan refactoring"},
        {"action": "edit", "target": "{write_file}", "description": "Apply refactoring"},
        {"action": "verify", "target": "{verifier}", "description": "Verify behavior unchanged"},
    ],
    "multi_file": [
        {"action": "read", "target": "{read_file}", "description": "Read primary file"},
        {"action": "read", "target": "{secondary_file}", "description": "Read dependency"},
        {"action": "edit", "target": "{write_file}", "description": "Edit primary"},
        {"action": "edit", "target": "{secondary_file}", "description": "Edit dependency"},
        {"action": "verify", "target": "{verifier}", "description": "Run all tests"},
    ],
}

# File path templates for different scenarios
FILE_SCENARIOS = [
    {
        "read_file": "src/auth/handler.py",
        "write_file": "src/auth/handler.py",
        "secondary_file": "src/auth/models.py",
        "verifier": "tests/test_auth.py::test_handler",
    },
    {
        "read_file": "src/api/routes.py",
        "write_file": "src/api/routes.py",
        "secondary_file": "src/api/middleware.py",
        "verifier": "tests/test_api.py::test_routes",
    },
    {
        "read_file": "src/data/processor.py",
        "write_file": "src/data/processor.py",
        "secondary_file": "src/data/schemas.py",
        "verifier": "tests/test_data.py::test_processor",
    },
    {
        "read_file": "src/utils/cache.py",
        "write_file": "src/utils/cache.py",
        "secondary_file": "src/utils/config.py",
        "verifier": "tests/test_utils.py::test_cache",
    },
    {
        "read_file": "src/models/user.py",
        "write_file": "tests/test_user.py",
        "secondary_file": "src/models/base.py",
        "verifier": "tests/test_user.py::test_model",
    },
]


@dataclasses.dataclass
class BranchIRSFTExample:
    """A single SFT training example for BranchIR generation."""

    branch_ticket: BranchTicket
    target_branch_ir: BranchIR
    action_type: str  # Key from ACTION_TEMPLATES
    has_rollback: bool = True
    has_claims: bool = True

    def format_input(self) -> str:
        """Format BranchTicket as model input."""
        parts = []
        parts.append(BRANCH_TOKENS[0])  # <|branch_start|>
        parts.append(f"{BRANCH_TOKENS[2]}{self.branch_ticket.ticket_id}")
        parts.append(f"{BRANCH_TOKENS[3]}{self.branch_ticket.branch_type}")
        parts.append(f"{BRANCH_TOKENS[4]}{self.branch_ticket.privilege_level}")
        parts.append(f"{BRANCH_TOKENS[5]}{', '.join(self.branch_ticket.read_set)}")
        parts.append(f"{BRANCH_TOKENS[6]}{', '.join(self.branch_ticket.write_set)}")
        parts.append(f"Description: {self.branch_ticket.description}")
        parts.append(BRANCH_TOKENS[1])  # <|branch_end|>
        parts.append(f"{BRANCH_TOKENS[7]}")  # <|branch_ir|>
        return "\n".join(parts)

    def format_target(self) -> str:
        """Format target BranchIR as JSON output."""
        return self.target_branch_ir.to_json()

    def format_full(self) -> str:
        """Format complete input->output example."""
        return f"{self.format_input()}\n{self.format_target()}"


def _fill_step_template(step: Dict[str, str], scenario: Dict[str, str]) -> Dict[str, Any]:
    """Fill in a step template with scenario file paths."""
    filled = {}
    for key, val in step.items():
        if isinstance(val, str):
            for placeholder, replacement in scenario.items():
                val = val.replace(f"{{{placeholder}}}", replacement)
        filled[key] = val
    return filled


def generate_ir_examples(count: int = 50, seed: int = 99) -> List[BranchIRSFTExample]:
    """Generate BranchIR SFT training examples.

    Each example maps a BranchTicket to a BranchIR execution plan.

    Args:
        count: Number of examples to generate
        seed: Random seed for reproducibility

    Returns:
        List of BranchIRSFTExample instances
    """
    rng = random.Random(seed)
    examples = []
    action_types = sorted(ACTION_TEMPLATES.keys())
    branch_types = ["patch", "refactor", "test", "fix", "exploration", "documentation"]
    privilege_levels = ["read_only", "read_write", "admin", "sandboxed"]

    for i in range(count):
        action_type = action_types[i % len(action_types)]
        scenario = FILE_SCENARIOS[i % len(FILE_SCENARIOS)]
        branch_type = branch_types[i % len(branch_types)]
        privilege = privilege_levels[i % len(privilege_levels)]

        # Build source BranchTicket
        ticket = BranchTicket(
            ticket_id=f"ir_ticket_{i:04d}",
            branch_type=branch_type,
            privilege_level=privilege,
            description=f"Execute {action_type} operation on {scenario['write_file']}",
            read_set=[scenario["read_file"]],
            write_set=[scenario["write_file"]],
            verifier_targets=[scenario["verifier"]],
            constraints=["maintain correctness"],
            metadata={"action_type": action_type},
        )

        # Build target BranchIR
        step_templates = ACTION_TEMPLATES[action_type]
        steps = [_fill_step_template(s, scenario) for s in step_templates]

        # Add rollback step for some examples
        has_rollback = i % 3 != 0
        if has_rollback:
            steps.append({
                "action": "rollback_checkpoint",
                "target": "auto",
                "description": "Create rollback point",
            })

        # Add claims for some examples
        has_claims = i % 4 != 0
        optimization_hints = {"cache_context": True}
        if has_claims:
            optimization_hints["claims"] = [
                {"claim": "operation is safe", "evidence_required": True},
                {"claim": "no side effects beyond write_set", "evidence_required": True},
            ]

        ir = BranchIR(
            ir_id=f"ir_{i:04d}",
            ticket_id=ticket.ticket_id,
            steps=steps,
            dependencies=[f"ctx_{i:04d}"],
            estimated_tokens=rng.randint(100, 2000),
            optimization_hints=optimization_hints,
            status="pending",
            metadata={"action_type": action_type, "has_rollback": has_rollback},
        )

        example = BranchIRSFTExample(
            branch_ticket=ticket,
            target_branch_ir=ir,
            action_type=action_type,
            has_rollback=has_rollback,
            has_claims=has_claims,
        )
        examples.append(example)

    return examples
