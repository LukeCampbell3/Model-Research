"""Tests for the heldout split builder."""

import pytest

from runtime_coder.data_pipeline.python_branch_ticket_curriculum import build_curriculum
from runtime_coder.data_pipeline.python_heldout_split_builder import (
    build_heldout_split,
    verify_no_leakage,
    compute_example_hash,
    extract_template_id,
)


class TestHeldoutSplitBuilder:
    """Tests for train/eval split with no leakage."""

    def test_split_produces_train_and_eval(self):
        """Split produces non-empty train and eval sets."""
        examples = build_curriculum("C", size=50)
        train, eval_ = build_heldout_split(examples, eval_ratio=0.2)
        assert len(train) > 0
        assert len(eval_) > 0
        assert len(train) + len(eval_) == len(examples)

    def test_no_template_leakage(self):
        """No template IDs shared between train and eval."""
        examples = build_curriculum("C", size=50)
        train, eval_ = build_heldout_split(examples, eval_ratio=0.2)
        result = verify_no_leakage(train, eval_)
        assert not result["leaked"], f"Leakage detected: {result}"

    def test_no_hash_leakage(self):
        """No content hashes shared between train and eval."""
        examples = build_curriculum("C", size=50)
        train, eval_ = build_heldout_split(examples, eval_ratio=0.2)
        result = verify_no_leakage(train, eval_)
        assert result["hash_overlap_count"] == 0

    def test_eval_ratio_approximately_correct(self):
        """Eval split is approximately the requested ratio."""
        examples = build_curriculum("C", size=100)
        train, eval_ = build_heldout_split(examples, eval_ratio=0.1)
        # Allow some flexibility since we split by template groups
        assert len(eval_) >= 1
        assert len(eval_) <= len(examples) * 0.5  # not more than half

    def test_deterministic_split(self):
        """Same seed produces same split."""
        examples = build_curriculum("C", size=50)
        train1, eval1 = build_heldout_split(examples, seed=42)
        train2, eval2 = build_heldout_split(examples, seed=42)
        assert train1 == train2
        assert eval1 == eval2

    def test_example_hash_deterministic(self):
        """Example hash is deterministic."""
        examples = build_curriculum("A", size=5)
        h1 = compute_example_hash(examples[0])
        h2 = compute_example_hash(examples[0])
        assert h1 == h2

    def test_template_id_extraction(self):
        """Template IDs are extractable from examples."""
        examples = build_curriculum("C", size=5)
        for ex in examples:
            tid = extract_template_id(ex)
            assert isinstance(tid, str)
            assert len(tid) > 0
