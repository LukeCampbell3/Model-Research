"""Evaluate BranchTicket validity and generation quality (Phase 0 + Phase 2).

Phase 0: Basic validation of BranchTicket lists.
Phase 2: Full generation evaluation with schema validity, field completeness,
          branch type accuracy, and other metrics.
"""

import json
from typing import Any, Dict, List, Optional

from runtime_coder.schemas.branch_ticket import (
    ALLOWED_BRANCH_TYPES,
    ALLOWED_PRIVILEGE_LEVELS,
    BranchTicket,
)


def validate_branch_tickets(tickets: List[BranchTicket]) -> Dict[str, Any]:
    """Validate a list of BranchTickets and return summary metrics.

    Returns:
        Dict with keys: total, valid, invalid, error_details
    """
    results = {
        "total": len(tickets),
        "valid": 0,
        "invalid": 0,
        "error_details": [],
    }

    for ticket in tickets:
        errors = ticket.validate()
        if not errors:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["error_details"].append({
                "ticket_id": ticket.ticket_id,
                "errors": errors,
            })

    results["validity_rate"] = results["valid"] / max(results["total"], 1)
    return results


# ============================================================
# Phase 2: Full Generation Evaluation
# ============================================================


def _try_parse_ticket(text: str) -> tuple:
    """Try to parse text as a BranchTicket JSON.

    Returns (ticket_or_None, parse_errors)
    """
    # Try to extract JSON
    start = text.find("{")
    if start == -1:
        return None, ["no JSON object found"]

    depth = 0
    end = -1
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    if end == -1:
        return None, ["unclosed JSON object"]

    json_str = text[start:end]
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, [f"JSON parse error: {str(e)}"]

    try:
        ticket = BranchTicket.from_dict(data)
        return ticket, []
    except (TypeError, KeyError) as e:
        return None, [f"BranchTicket construction error: {str(e)}"]


def eval_branch_ticket_generation(
    model,
    test_examples: List,
    tokenizer=None,
    max_gen_tokens: int = 256,
    max_seq_len: int = 512,
    device: str = "cpu",
) -> Dict[str, float]:
    """Evaluate BranchTicket generation quality on held-out examples.

    Runs the model on each test example's input and evaluates the output.

    Args:
        model: TinyRuntimeCoder model (or compatible)
        test_examples: List of BranchTicketSFTExample instances
        tokenizer: Optional tokenizer (uses char-level if None)
        max_gen_tokens: Max tokens to generate per example
        max_seq_len: Max sequence length
        device: Device string

    Returns:
        Dictionary of evaluation metrics:
        - valid_json_rate: fraction that parse as valid JSON
        - schema_valid_rate: fraction that pass BranchTicket.validate()
        - field_completeness: avg fraction of required fields present
        - branch_type_accuracy: fraction with correct branch_type
        - write_set_present: fraction with non-empty write_set
        - verifier_declared: fraction with non-empty verifier_targets
        - evidence_declared: fraction with metadata present
    """
    from runtime_coder.training.train_branch_sft import generate_from_model

    if not test_examples:
        return {
            "valid_json_rate": 0.0,
            "schema_valid_rate": 0.0,
            "field_completeness": 0.0,
            "branch_type_accuracy": 0.0,
            "write_set_present": 0.0,
            "verifier_declared": 0.0,
            "evidence_declared": 0.0,
            "total_evaluated": 0,
        }

    vocab_size = model.config.vocab_size
    total = len(test_examples)

    valid_json_count = 0
    schema_valid_count = 0
    field_completeness_scores = []
    branch_type_correct = 0
    write_set_count = 0
    verifier_count = 0
    evidence_count = 0

    required_fields = [
        "ticket_id", "branch_type", "privilege_level",
        "read_set", "write_set", "verifier_targets", "description",
    ]

    for ex in test_examples:
        input_text = ex.format_input()
        generated = generate_from_model(
            model, input_text, vocab_size, max_gen_tokens, max_seq_len, device
        )

        ticket, parse_errors = _try_parse_ticket(generated)

        if ticket is not None or not parse_errors:
            valid_json_count += 1

        if ticket is not None:
            # Schema validation
            errors = ticket.validate()
            if not errors:
                schema_valid_count += 1

            # Field completeness
            ticket_dict = ticket.to_dict()
            present = sum(
                1 for f in required_fields
                if f in ticket_dict and ticket_dict[f]
            )
            field_completeness_scores.append(present / len(required_fields))

            # Branch type accuracy
            expected_type = ex.target_branch_ticket.branch_type
            if ticket.branch_type == expected_type:
                branch_type_correct += 1

            # Write set present
            if ticket.write_set:
                write_set_count += 1

            # Verifier declared
            if ticket.verifier_targets:
                verifier_count += 1

            # Evidence (metadata present)
            if ticket.metadata:
                evidence_count += 1
        else:
            field_completeness_scores.append(0.0)

    return {
        "valid_json_rate": valid_json_count / total,
        "schema_valid_rate": schema_valid_count / total,
        "field_completeness": sum(field_completeness_scores) / total,
        "branch_type_accuracy": branch_type_correct / total,
        "write_set_present": write_set_count / total,
        "verifier_declared": verifier_count / total,
        "evidence_declared": evidence_count / total,
        "total_evaluated": total,
    }
