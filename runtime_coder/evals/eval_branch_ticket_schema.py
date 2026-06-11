"""BranchTicket schema validity evaluation.

Evaluates generated text against the BranchTicket schema for:
- schema_valid_rate: fraction that fully validate
- field_completeness: fraction of required fields present
- required_key_accuracy: accuracy on required keys
- enum_accuracy: accuracy on enum fields (branch_type, privilege_level)
"""

import json
from typing import Dict, List

from runtime_coder.schema.canonical_schema_loader import load_branch_ticket_schema


def eval_branch_ticket_schema(generated_texts: List[str]) -> Dict[str, float]:
    """Evaluate generated texts against BranchTicket schema.

    Args:
        generated_texts: List of model-generated text strings.

    Returns:
        Dict with schema_valid_rate, field_completeness,
        required_key_accuracy, enum_accuracy.
    """
    schema = load_branch_ticket_schema()
    required_fields = schema["required_fields"]
    allowed_branch_types = set(schema["allowed_branch_types"])
    allowed_privilege_levels = set(schema["allowed_privilege_levels"])

    total = len(generated_texts)
    if total == 0:
        return {
            "schema_valid_rate": 0.0,
            "field_completeness": 0.0,
            "required_key_accuracy": 0.0,
            "enum_accuracy": 0.0,
        }

    valid_count = 0
    field_completeness_sum = 0.0
    required_key_sum = 0.0
    enum_accuracy_sum = 0.0

    for text in generated_texts:
        data = _parse_json_from_text(text)
        if data is None:
            continue

        # Check required fields
        present_required = sum(1 for f in required_fields if f in data and data[f])
        completeness = present_required / len(required_fields)
        field_completeness_sum += completeness
        required_key_sum += present_required / len(required_fields)

        # Check enums
        enum_correct = 0
        enum_total = 0
        if "branch_type" in data:
            enum_total += 1
            if data["branch_type"] in allowed_branch_types:
                enum_correct += 1
        if "privilege_level" in data:
            enum_total += 1
            if data["privilege_level"] in allowed_privilege_levels:
                enum_correct += 1
        if enum_total > 0:
            enum_accuracy_sum += enum_correct / enum_total

        # Full schema validity
        is_valid = (
            completeness == 1.0
            and data.get("branch_type") in allowed_branch_types
            and data.get("privilege_level") in allowed_privilege_levels
        )
        if is_valid:
            valid_count += 1

    parsed_count = sum(1 for t in generated_texts if _parse_json_from_text(t) is not None)
    denom = max(parsed_count, 1)

    return {
        "schema_valid_rate": valid_count / total,
        "field_completeness": field_completeness_sum / denom,
        "required_key_accuracy": required_key_sum / denom,
        "enum_accuracy": enum_accuracy_sum / denom,
    }


def _parse_json_from_text(text: str) -> dict:
    """Try to parse a JSON object from text."""
    start = text.find("{")
    if start == -1:
        return None

    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start: i + 1])
                except json.JSONDecodeError:
                    return None
    return None
