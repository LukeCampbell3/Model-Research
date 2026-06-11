"""JSON validity evaluation for generated BranchTicket texts.

Computes valid_json_rate, truncated_rate, and parse_error_rate.
"""

import json
from typing import Dict, List


def eval_json_validity(generated_texts: List[str]) -> Dict[str, float]:
    """Evaluate JSON validity of generated texts.

    Args:
        generated_texts: List of model-generated text strings.

    Returns:
        Dict with valid_json_rate, truncated_rate, parse_error_rate.
    """
    total = len(generated_texts)
    if total == 0:
        return {"valid_json_rate": 0.0, "truncated_rate": 0.0, "parse_error_rate": 0.0}

    valid_count = 0
    truncated_count = 0
    parse_error_count = 0

    for text in generated_texts:
        json_str = _extract_json(text)

        if json_str is None:
            # No JSON found - check if truncated
            if _looks_truncated(text):
                truncated_count += 1
            else:
                parse_error_count += 1
            continue

        try:
            json.loads(json_str)
            valid_count += 1
        except json.JSONDecodeError:
            # Check if truncation caused the error
            if _looks_truncated(json_str):
                truncated_count += 1
            else:
                parse_error_count += 1

    return {
        "valid_json_rate": valid_count / total,
        "truncated_rate": truncated_count / total,
        "parse_error_rate": parse_error_count / total,
    }


def _extract_json(text: str) -> str:
    """Try to extract a JSON object from text."""
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
                return text[start: i + 1]

    # Unclosed - return partial
    return text[start:]


def _looks_truncated(text: str) -> bool:
    """Heuristic: does the text look like it was cut off mid-JSON?"""
    if not text:
        return False
    # Count braces
    open_braces = text.count("{")
    close_braces = text.count("}")
    open_brackets = text.count("[")
    close_brackets = text.count("]")

    # If more opens than closes, likely truncated
    return (open_braces > close_braces) or (open_brackets > close_brackets)
