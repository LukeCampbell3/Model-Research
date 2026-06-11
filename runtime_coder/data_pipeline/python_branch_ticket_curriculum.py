"""Staged curriculum builder for Python BranchTicket training.

Stage A: JSON warmup - simple JSON objects with runtime fields
Stage B: Minimal BranchTicket - required fields only
Stage C: Full BranchTicket - all fields with context and constraints

Each example includes schema_hash, runtime_contract_version, target_kind.
"""

import json
import random
from typing import Dict, List, Any

from runtime_coder.schema.canonical_schema_loader import compute_schema_hash
from runtime_coder.data_pipeline.python_task_bank import get_all_task_templates

_SCHEMA_HASH = compute_schema_hash()
_CONTRACT_VERSION = "1.0"
_TARGET_KIND = "python"


def _build_stage_a_example(seed_val: int) -> Dict[str, Any]:
    """Stage A: JSON warmup with runtime fields.

    Simple JSON objects that teach the model JSON syntax and
    the required runtime metadata fields.
    """
    rng = random.Random(seed_val)
    branch_types = ["bug_fix", "test_gen", "refactor", "type_fix", "import_fix"]
    privilege_levels = ["read_only", "read_write", "sandboxed"]

    example = {
        "input": "<|task_start|>Generate a valid JSON object with runtime fields<|task_end|>",
        "target": json.dumps({
            "schema_hash": _SCHEMA_HASH,
            "runtime_contract_version": _CONTRACT_VERSION,
            "target_kind": _TARGET_KIND,
            "branch_type": rng.choice(branch_types),
            "privilege_level": rng.choice(privilege_levels),
        }, indent=2),
        "stage": "A",
        "curriculum_metadata": {
            "focus": "json_syntax_and_runtime_fields",
            "difficulty": 1,
        },
    }
    return example


def _build_stage_b_example(seed_val: int) -> Dict[str, Any]:
    """Stage B: Minimal BranchTicket with required fields only."""
    rng = random.Random(seed_val)
    templates = get_all_task_templates()
    template = templates[seed_val % len(templates)]
    ticket = template["ticket"]

    # Minimal ticket: just required fields
    minimal_ticket = {
        "ticket_id": ticket["ticket_id"],
        "branch_type": ticket["branch_type"],
        "privilege_level": ticket["privilege_level"],
        "description": ticket["description"],
        "read_set": ticket["read_set"],
        "write_set": ticket["write_set"],
        "schema_hash": _SCHEMA_HASH,
        "runtime_contract_version": _CONTRACT_VERSION,
        "target_kind": _TARGET_KIND,
    }

    task = template["task"]
    input_text = (
        f"<|task_start|><|task_type|>{task['task_type']}\n"
        f"{task['description']}<|task_end|>"
    )

    example = {
        "input": input_text,
        "target": json.dumps(minimal_ticket, indent=2),
        "stage": "B",
        "curriculum_metadata": {
            "focus": "minimal_branch_ticket_structure",
            "difficulty": 2,
            "task_type": task["task_type"],
        },
    }
    return example


def _build_stage_c_example(seed_val: int) -> Dict[str, Any]:
    """Stage C: Full BranchTicket with context and constraints."""
    templates = get_all_task_templates()
    template = templates[seed_val % len(templates)]
    ticket = template["ticket"]
    task = template["task"]
    context = template["context"]

    # Build full input with context
    input_text = (
        f"<|task_start|><|task_type|>{task['task_type']}\n"
        f"<|task_id|>{task['task_id']}\n"
        f"{task['description']}<|task_end|>\n"
        f"<|context_start|><|context_file|>{context['file_path']}\n"
        f"<|context_language|>{context['language']}\n"
        f"<|context_snippet|>{context['content']}<|context_end|>"
    )

    # Full ticket with all fields
    full_ticket = {
        "ticket_id": ticket["ticket_id"],
        "branch_type": ticket["branch_type"],
        "privilege_level": ticket["privilege_level"],
        "description": ticket["description"],
        "read_set": ticket["read_set"],
        "write_set": ticket["write_set"],
        "verifier_targets": ticket.get("verifier_targets", []),
        "constraints": ticket.get("constraints", []),
        "schema_hash": _SCHEMA_HASH,
        "runtime_contract_version": _CONTRACT_VERSION,
        "target_kind": _TARGET_KIND,
    }

    example = {
        "input": input_text,
        "target": json.dumps(full_ticket, indent=2),
        "stage": "C",
        "curriculum_metadata": {
            "focus": "full_branch_ticket_with_context",
            "difficulty": 3,
            "task_type": task["task_type"],
            "has_context": True,
        },
    }
    return example


def build_curriculum(stage: str, size: int, seed: int = 42) -> List[Dict[str, Any]]:
    """Build curriculum examples for a given stage.

    Args:
        stage: "A" (JSON warmup), "B" (minimal ticket), or "C" (full ticket).
        size: Number of examples to generate.
        seed: Random seed for reproducibility.

    Returns:
        List of curriculum examples with input/target pairs.

    Raises:
        ValueError: If stage is not A, B, or C.
    """
    if stage not in ("A", "B", "C"):
        raise ValueError(f"stage must be 'A', 'B', or 'C', got '{stage}'")

    builders = {"A": _build_stage_a_example, "B": _build_stage_b_example, "C": _build_stage_c_example}
    builder = builders[stage]

    examples = []
    for i in range(size):
        example = builder(seed + i)
        examples.append(example)

    return examples


def build_mixed_curriculum(size: int, seed: int = 42) -> List[Dict[str, Any]]:
    """Build a mixed curriculum with progressive staging.

    First 20% is Stage A, next 30% is Stage B, final 50% is Stage C.

    Args:
        size: Total number of examples.
        seed: Random seed.

    Returns:
        List of mixed curriculum examples.
    """
    stage_a_size = max(1, int(size * 0.2))
    stage_b_size = max(1, int(size * 0.3))
    stage_c_size = size - stage_a_size - stage_b_size

    examples = []
    examples.extend(build_curriculum("A", stage_a_size, seed=seed))
    examples.extend(build_curriculum("B", stage_b_size, seed=seed + 1000))
    examples.extend(build_curriculum("C", stage_c_size, seed=seed + 2000))

    return examples
