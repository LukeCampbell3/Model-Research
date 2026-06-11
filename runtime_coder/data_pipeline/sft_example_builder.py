"""Build SFT (Supervised Fine-Tuning) examples from fixtures."""

from typing import Dict, List, Any

from runtime_coder.data_pipeline.fixtures import generate_all_fixtures
from runtime_coder.tokenizer.runtime_special_tokens import (
    TASK_TOKENS,
    CONTEXT_TOKENS,
    BRANCH_TOKENS,
    PATCH_TOKENS,
    VERIFIER_TOKENS,
    COMMIT_TOKENS,
)


def build_sft_example(fixture_name: str, fixture: Any) -> Dict[str, Any]:
    """Build a single SFT training example from a fixture."""
    d = fixture.to_dict()

    # Construct prompt with special tokens
    prompt_parts = []
    completion_parts = []

    if fixture_name == "task_packet":
        prompt_parts.append(TASK_TOKENS[0])  # <|task_start|>
        prompt_parts.append(f"Task: {d['description']}")
        prompt_parts.append(TASK_TOKENS[1])  # <|task_end|>
        completion_parts.append(f"task_id: {d['task_id']}")
        completion_parts.append(f"type: {d['task_type']}")

    elif fixture_name == "branch_ticket":
        prompt_parts.append(BRANCH_TOKENS[0])  # <|branch_start|>
        prompt_parts.append(f"Branch: {d['description']}")
        prompt_parts.append(f"Type: {d['branch_type']}")
        prompt_parts.append(BRANCH_TOKENS[1])  # <|branch_end|>
        completion_parts.append(f"ticket_id: {d['ticket_id']}")
        completion_parts.append(f"write_set: {d['write_set']}")

    elif fixture_name == "context_packet":
        prompt_parts.append(CONTEXT_TOKENS[0])  # <|context_start|>
        prompt_parts.append(f"File: {d['file_path']}")
        prompt_parts.append(d['content'])
        prompt_parts.append(CONTEXT_TOKENS[1])  # <|context_end|>
        completion_parts.append(f"symbols: {d['symbols']}")

    elif fixture_name == "verifier_result":
        prompt_parts.append(VERIFIER_TOKENS[0])  # <|verifier_start|>
        prompt_parts.append(f"Verifier: {d['verifier_type']}")
        prompt_parts.append(VERIFIER_TOKENS[1])  # <|verifier_end|>
        if d['passed']:
            completion_parts.append(VERIFIER_TOKENS[2])  # <|verifier_pass|>
        else:
            completion_parts.append(VERIFIER_TOKENS[3])  # <|verifier_fail|>
        completion_parts.append(f"score: {d['score']}")

    elif fixture_name == "commit_result":
        prompt_parts.append(COMMIT_TOKENS[0])  # <|commit_start|>
        prompt_parts.append(f"Commit for: {d['ticket_id']}")
        prompt_parts.append(COMMIT_TOKENS[1])  # <|commit_end|>
        if d['committed']:
            completion_parts.append(COMMIT_TOKENS[2])  # <|commit_accept|>
        else:
            completion_parts.append(COMMIT_TOKENS[3])  # <|commit_reject|>

    else:
        # Generic handling for other schemas
        prompt_parts.append(f"Schema: {fixture_name}")
        prompt_parts.append(str(d))
        completion_parts.append("acknowledged")

    return {
        "fixture_name": fixture_name,
        "prompt": "\n".join(prompt_parts),
        "completion": "\n".join(completion_parts),
        "raw_data": d,
    }


def build_sft_examples() -> List[Dict[str, Any]]:
    """Build SFT examples from all fixtures."""
    fixtures = generate_all_fixtures()
    examples = []
    for name, fixture in fixtures.items():
        example = build_sft_example(name, fixture)
        examples.append(example)
    return examples
