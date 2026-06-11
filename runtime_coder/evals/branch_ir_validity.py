"""Evaluate BranchIR generation quality (Phase 2).

Metrics:
- schema_valid_rate: fraction that pass BranchIR.validate()
- action_consistency: actions match the expected action_type
- claims_have_evidence: claims in optimization_hints have evidence_required
- rollback_present: fraction with rollback checkpoint steps
"""

import json
from typing import Any, Dict, List

from runtime_coder.schemas.branch_ir import BranchIR


def _try_parse_ir(text: str) -> tuple:
    """Try to parse text as a BranchIR JSON.

    Returns (ir_or_None, parse_errors)
    """
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
        ir = BranchIR.from_dict(data)
        return ir, []
    except (TypeError, KeyError) as e:
        return None, [f"BranchIR construction error: {str(e)}"]


def eval_branch_ir_generation(
    model,
    test_examples: List,
    max_gen_tokens: int = 256,
    max_seq_len: int = 512,
    device: str = "cpu",
) -> Dict[str, float]:
    """Evaluate BranchIR generation quality on held-out examples.

    Args:
        model: TinyRuntimeCoder model
        test_examples: List of BranchIRSFTExample instances
        max_gen_tokens: Max tokens to generate
        max_seq_len: Max sequence length
        device: Device string

    Returns:
        Dictionary of metrics:
        - schema_valid_rate: fraction passing BranchIR.validate()
        - action_consistency: fraction with correct action types in steps
        - claims_have_evidence: fraction with evidence_required claims
        - rollback_present: fraction with rollback checkpoint steps
    """
    from runtime_coder.training.train_branch_sft import generate_from_model

    if not test_examples:
        return {
            "schema_valid_rate": 0.0,
            "action_consistency": 0.0,
            "claims_have_evidence": 0.0,
            "rollback_present": 0.0,
            "total_evaluated": 0,
        }

    vocab_size = model.config.vocab_size
    total = len(test_examples)

    schema_valid_count = 0
    action_consistent_count = 0
    claims_evidence_count = 0
    rollback_count = 0

    for ex in test_examples:
        input_text = ex.format_input()
        generated = generate_from_model(
            model, input_text, vocab_size, max_gen_tokens, max_seq_len, device
        )

        ir, parse_errors = _try_parse_ir(generated)

        if ir is not None:
            # Schema validation
            errors = ir.validate()
            if not errors:
                schema_valid_count += 1

            # Action consistency - check that steps have valid actions
            valid_actions = {"read", "edit", "generate", "verify", "inspect",
                           "analyze", "summarize", "extract", "plan", "execute",
                           "validate", "rollback_checkpoint"}
            if ir.steps:
                actions_valid = all(
                    s.get("action", "") in valid_actions
                    for s in ir.steps
                )
                if actions_valid:
                    action_consistent_count += 1

            # Claims have evidence
            hints = ir.optimization_hints or {}
            claims = hints.get("claims", [])
            if claims:
                all_have_evidence = all(
                    c.get("evidence_required", False) for c in claims
                    if isinstance(c, dict)
                )
                if all_have_evidence:
                    claims_evidence_count += 1
            else:
                # No claims is acceptable
                claims_evidence_count += 1

            # Rollback present
            if ir.steps:
                has_rollback = any(
                    s.get("action") == "rollback_checkpoint"
                    for s in ir.steps
                )
                if has_rollback:
                    rollback_count += 1

    return {
        "schema_valid_rate": schema_valid_count / total,
        "action_consistency": action_consistent_count / total,
        "claims_have_evidence": claims_evidence_count / total,
        "rollback_present": rollback_count / total,
        "total_evaluated": total,
    }


def validate_branch_irs(irs: List[BranchIR]) -> Dict[str, Any]:
    """Validate a list of BranchIRs and return summary metrics.

    Args:
        irs: List of BranchIR instances to validate

    Returns:
        Dict with validation statistics
    """
    results = {
        "total": len(irs),
        "valid": 0,
        "invalid": 0,
        "error_details": [],
    }

    for ir in irs:
        errors = ir.validate()
        if not errors:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["error_details"].append({
                "ir_id": ir.ir_id,
                "errors": errors,
            })

    results["validity_rate"] = results["valid"] / max(results["total"], 1)
    return results
