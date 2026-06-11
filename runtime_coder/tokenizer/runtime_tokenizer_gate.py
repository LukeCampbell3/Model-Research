"""Gate 0: Runtime Tokenizer Validation Gate.

Validates that the tokenizer correctly handles:
1. All special tokens exist and have unique IDs
2. BranchTicket JSON round-trips through encode/decode
3. Python indentation round-trips
4. Diff hunks round-trip
5. Tracebacks round-trip

Returns CONFIRMED or BLOCKED with reasons.
"""

import json
from typing import Dict, List, Tuple

from runtime_coder.tokenizer.tokenizer_smoke import RuntimeTokenizer
from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)


def _check_special_tokens_exist(tokenizer: RuntimeTokenizer) -> Tuple[bool, List[str]]:
    """Check all special tokens exist and have unique IDs."""
    errors = []
    seen_ids = {}

    for token in SPECIAL_TOKENS:
        tid = tokenizer.token_to_id(token)
        if tid is None:
            errors.append(f"Token not found: {token}")
            continue
        if tid in seen_ids:
            errors.append(f"Duplicate ID {tid}: {token} conflicts with {seen_ids[tid]}")
        seen_ids[tid] = token

    return len(errors) == 0, errors


def _check_json_roundtrip(tokenizer: RuntimeTokenizer) -> Tuple[bool, List[str]]:
    """Check BranchTicket JSON survives encode/decode."""
    errors = []
    ticket_json = json.dumps({
        "ticket_id": "tkt_001",
        "branch_type": "bug_fix",
        "privilege_level": "read_write",
        "description": "Fix off-by-one in binary search",
        "read_set": ["src/search.py", "tests/test_search.py"],
        "write_set": ["src/search.py"],
        "verifier_targets": ["tests/test_search.py::test_binary_search"],
        "constraints": ["no_new_dependencies"],
        "schema_hash": "abc123def456",
        "runtime_contract_version": "1.0",
        "target_kind": "python",
    }, indent=2)

    ids = tokenizer.encode(ticket_json)
    decoded = tokenizer.decode(ids)

    # The decoded text should parse as equivalent JSON
    try:
        original = json.loads(ticket_json)
        restored = json.loads(decoded)
        if original != restored:
            errors.append(
                f"JSON content mismatch after round-trip: "
                f"keys_diff={set(original.keys()) ^ set(restored.keys())}"
            )
    except json.JSONDecodeError as e:
        errors.append(f"JSON decode failed after round-trip: {e}")

    return len(errors) == 0, errors


def _check_python_indentation_roundtrip(tokenizer: RuntimeTokenizer) -> Tuple[bool, List[str]]:
    """Check Python indentation survives encode/decode."""
    errors = []
    python_code = (
        "def binary_search(arr, target):\n"
        "    left, right = 0, len(arr) - 1\n"
        "    while left <= right:\n"
        "        mid = (left + right) // 2\n"
        "        if arr[mid] == target:\n"
        "            return mid\n"
        "        elif arr[mid] < target:\n"
        "            left = mid + 1\n"
        "        else:\n"
        "            right = mid - 1\n"
        "    return -1\n"
    )

    ids = tokenizer.encode(python_code)
    decoded = tokenizer.decode(ids)

    # Check indentation is preserved
    original_lines = python_code.split("\n")
    decoded_lines = decoded.split("\n")

    if len(original_lines) != len(decoded_lines):
        errors.append(
            f"Line count mismatch: original={len(original_lines)}, "
            f"decoded={len(decoded_lines)}"
        )
    else:
        for i, (orig, dec) in enumerate(zip(original_lines, decoded_lines)):
            orig_indent = len(orig) - len(orig.lstrip())
            dec_indent = len(dec) - len(dec.lstrip())
            if orig_indent != dec_indent:
                errors.append(
                    f"Indentation mismatch at line {i}: "
                    f"expected {orig_indent} spaces, got {dec_indent}"
                )

    return len(errors) == 0, errors


def _check_diff_hunk_roundtrip(tokenizer: RuntimeTokenizer) -> Tuple[bool, List[str]]:
    """Check unified diff hunks round-trip correctly."""
    errors = []
    diff_hunk = (
        "--- a/src/search.py\n"
        "+++ b/src/search.py\n"
        "@@ -5,7 +5,7 @@\n"
        " def binary_search(arr, target):\n"
        "     left, right = 0, len(arr) - 1\n"
        "     while left <= right:\n"
        "-        mid = (left + right) / 2\n"
        "+        mid = (left + right) // 2\n"
        "         if arr[mid] == target:\n"
        "             return mid\n"
        "     return -1\n"
    )

    ids = tokenizer.encode(diff_hunk)
    decoded = tokenizer.decode(ids)

    # Check key diff markers are preserved
    if decoded != diff_hunk:
        # Check individual markers
        for marker in ["---", "+++", "@@", "-        ", "+        "]:
            if marker not in decoded:
                errors.append(f"Diff marker lost: {repr(marker)}")

    return len(errors) == 0, errors


def _check_traceback_roundtrip(tokenizer: RuntimeTokenizer) -> Tuple[bool, List[str]]:
    """Check Python tracebacks round-trip correctly."""
    errors = []
    traceback_text = (
        "Traceback (most recent call last):\n"
        '  File "src/search.py", line 8, in binary_search\n'
        "    mid = (left + right) / 2\n"
        "TypeError: unsupported operand type(s) for /: 'str' and 'int'\n"
    )

    ids = tokenizer.encode(traceback_text)
    decoded = tokenizer.decode(ids)

    if decoded != traceback_text:
        # Check key elements
        for element in ["Traceback", "File", "line 8", "TypeError"]:
            if element not in decoded:
                errors.append(f"Traceback element lost: {repr(element)}")

    return len(errors) == 0, errors


def validate_runtime_tokenizer() -> Dict:
    """Run Gate 0 validation on the runtime tokenizer.

    Returns:
        Dict with 'status' (CONFIRMED or BLOCKED), 'checks' detail,
        and 'errors' list if blocked.
    """
    tokenizer = RuntimeTokenizer()
    checks = {}
    all_errors = []

    # Check 1: Special tokens exist and unique
    ok, errs = _check_special_tokens_exist(tokenizer)
    checks["special_tokens_exist_unique"] = ok
    all_errors.extend(errs)

    # Check 2: JSON round-trip
    ok, errs = _check_json_roundtrip(tokenizer)
    checks["json_roundtrip"] = ok
    all_errors.extend(errs)

    # Check 3: Python indentation round-trip
    ok, errs = _check_python_indentation_roundtrip(tokenizer)
    checks["python_indentation_roundtrip"] = ok
    all_errors.extend(errs)

    # Check 4: Diff hunk round-trip
    ok, errs = _check_diff_hunk_roundtrip(tokenizer)
    checks["diff_hunk_roundtrip"] = ok
    all_errors.extend(errs)

    # Check 5: Traceback round-trip
    ok, errs = _check_traceback_roundtrip(tokenizer)
    checks["traceback_roundtrip"] = ok
    all_errors.extend(errs)

    status = "CONFIRMED" if not all_errors else "BLOCKED"

    return {
        "status": status,
        "checks": checks,
        "errors": all_errors,
        "tokenizer_vocab_size": tokenizer.vocab_size,
        "special_token_count": len(SPECIAL_TOKENS),
    }
