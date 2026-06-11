"""Python context grounding evaluation.

Evaluates whether generated BranchTickets correctly reference files and
symbols from the provided ContextPacket, detecting hallucinated references.
"""

import json
from typing import Dict, List, Any


def eval_python_grounding(
    generated_texts: List[str],
    context_packets: List[Dict[str, Any]],
) -> Dict[str, float]:
    """Evaluate grounding of generated tickets against context.

    Args:
        generated_texts: List of generated text strings.
        context_packets: List of corresponding ContextPacket dicts.

    Returns:
        Dict with read_set_accuracy, write_set_accuracy,
        path_accuracy, hallucinated_file_rate.
    """
    total = len(generated_texts)
    if total == 0:
        return {
            "read_set_accuracy": 0.0,
            "write_set_accuracy": 0.0,
            "path_accuracy": 0.0,
            "hallucinated_file_rate": 0.0,
        }

    read_set_scores = []
    write_set_scores = []
    path_scores = []
    hallucination_count = 0

    for text, ctx in zip(generated_texts, context_packets):
        ticket = _parse_ticket(text)
        if ticket is None:
            continue

        # Get valid paths from context
        valid_paths = _get_valid_paths(ctx)

        # Evaluate read_set
        read_set = ticket.get("read_set", [])
        if read_set:
            read_correct = sum(1 for p in read_set if _path_in_context(p, valid_paths))
            read_set_scores.append(read_correct / len(read_set))

            # Check for hallucinated paths
            hallucinated = [p for p in read_set if not _path_in_context(p, valid_paths)]
            if hallucinated:
                hallucination_count += 1
        else:
            read_set_scores.append(0.0)

        # Evaluate write_set
        write_set = ticket.get("write_set", [])
        if write_set:
            write_correct = sum(1 for p in write_set if _path_in_context(p, valid_paths))
            write_set_scores.append(write_correct / len(write_set))

            hallucinated = [p for p in write_set if not _path_in_context(p, valid_paths)]
            if hallucinated:
                hallucination_count += 1
        else:
            write_set_scores.append(0.0)

        # Overall path accuracy
        all_paths = read_set + write_set
        if all_paths:
            correct = sum(1 for p in all_paths if _path_in_context(p, valid_paths))
            path_scores.append(correct / len(all_paths))

    n = max(len(read_set_scores), 1)
    return {
        "read_set_accuracy": sum(read_set_scores) / n if read_set_scores else 0.0,
        "write_set_accuracy": sum(write_set_scores) / n if write_set_scores else 0.0,
        "path_accuracy": sum(path_scores) / max(len(path_scores), 1) if path_scores else 0.0,
        "hallucinated_file_rate": hallucination_count / total,
    }


def _parse_ticket(text: str) -> dict:
    """Parse JSON ticket from text."""
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


def _get_valid_paths(ctx: Dict[str, Any]) -> List[str]:
    """Extract all valid file paths from context."""
    paths = []
    if "file_path" in ctx and ctx["file_path"]:
        paths.append(ctx["file_path"])
    # Also include test file paths derived from source
    file_path = ctx.get("file_path", "")
    if file_path.startswith("src/"):
        test_path = file_path.replace("src/", "tests/test_")
        paths.append(test_path)
    # Include directory paths
    if "/" in file_path:
        paths.append(file_path.rsplit("/", 1)[0] + "/")
    return paths


def _path_in_context(path: str, valid_paths: List[str]) -> bool:
    """Check if a path is valid given the context."""
    if path in valid_paths:
        return True
    # Prefix match (e.g., "tests/" matches "tests/test_foo.py")
    for vp in valid_paths:
        if path.startswith(vp) or vp.startswith(path):
            return True
    return False
