"""Heldout split builder for Python training data.

Ensures no template/hash leakage between train and eval splits.
Splits by template ID to prevent the model from memorizing specific examples.
"""

import hashlib
import random
from typing import Dict, List, Any, Tuple


def compute_example_hash(example: Dict[str, Any]) -> str:
    """Compute a deterministic hash for an example.

    Uses the target content to identify unique examples.
    """
    target = example.get("target", "")
    return hashlib.md5(target.encode()).hexdigest()[:12]


def extract_template_id(example: Dict[str, Any]) -> str:
    """Extract the template source ID from an example.

    Looks at curriculum_metadata or falls back to hashing the input pattern.
    """
    meta = example.get("curriculum_metadata", {})
    task_type = meta.get("task_type", "unknown")

    # Use input structure as template fingerprint
    input_text = example.get("input", "")
    # Strip variable content, keep structure
    structure = ""
    for token in ["<|task_start|>", "<|task_end|>", "<|context_start|>",
                  "<|context_end|>", "<|task_type|>", "<|task_id|>"]:
        if token in input_text:
            structure += token

    template_key = f"{task_type}:{structure}"
    return hashlib.md5(template_key.encode()).hexdigest()[:8]


def build_heldout_split(
    examples: List[Dict[str, Any]],
    eval_ratio: float = 0.1,
    seed: int = 42,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Split examples into train and eval with no template leakage.

    Groups examples by template ID, then assigns entire template groups
    to either train or eval. This ensures the eval set tests
    generalization, not memorization.

    Args:
        examples: Full list of curriculum examples.
        eval_ratio: Fraction of examples for eval (by template groups).
        seed: Random seed for reproducible splits.

    Returns:
        Tuple of (train_examples, eval_examples).
    """
    # Group by template ID
    template_groups: Dict[str, List[Dict[str, Any]]] = {}
    for ex in examples:
        tid = extract_template_id(ex)
        if tid not in template_groups:
            template_groups[tid] = []
        template_groups[tid].append(ex)

    # Shuffle template IDs
    rng = random.Random(seed)
    template_ids = list(template_groups.keys())
    rng.shuffle(template_ids)

    # Determine split point
    total_examples = len(examples)
    target_eval_count = max(1, int(total_examples * eval_ratio))

    eval_examples = []
    train_examples = []
    eval_template_ids = set()

    # Assign templates to eval until we reach target count
    for tid in template_ids:
        if len(eval_examples) < target_eval_count:
            eval_examples.extend(template_groups[tid])
            eval_template_ids.add(tid)
        else:
            train_examples.extend(template_groups[tid])

    return train_examples, eval_examples


def verify_no_leakage(
    train_examples: List[Dict[str, Any]],
    eval_examples: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Verify there's no template or hash leakage between splits.

    Args:
        train_examples: Training split.
        eval_examples: Evaluation split.

    Returns:
        Dict with leakage metrics. 'leaked' is True if leakage detected.
    """
    # Check template ID overlap
    train_templates = {extract_template_id(ex) for ex in train_examples}
    eval_templates = {extract_template_id(ex) for ex in eval_examples}
    template_overlap = train_templates & eval_templates

    # Check content hash overlap
    train_hashes = {compute_example_hash(ex) for ex in train_examples}
    eval_hashes = {compute_example_hash(ex) for ex in eval_examples}
    hash_overlap = train_hashes & eval_hashes

    return {
        "leaked": len(template_overlap) > 0 or len(hash_overlap) > 0,
        "template_overlap_count": len(template_overlap),
        "hash_overlap_count": len(hash_overlap),
        "train_templates": len(train_templates),
        "eval_templates": len(eval_templates),
        "train_examples": len(train_examples),
        "eval_examples": len(eval_examples),
    }
