"""Tests for JSON validity evaluation."""

import json
import pytest

from runtime_coder.evals.eval_json_validity import eval_json_validity


class TestJsonValidityEval:
    """Tests for JSON validity detection."""

    def test_valid_json_detected(self):
        """Valid JSON texts score 1.0."""
        texts = [
            json.dumps({"ticket_id": "t1", "branch_type": "fix"}),
            json.dumps({"ticket_id": "t2", "branch_type": "test"}),
        ]
        result = eval_json_validity(texts)
        assert result["valid_json_rate"] == 1.0
        assert result["parse_error_rate"] == 0.0

    def test_invalid_json_detected(self):
        """Invalid JSON texts score 0.0 valid."""
        texts = [
            "this is not json at all",
            "neither is this {broken",
        ]
        result = eval_json_validity(texts)
        assert result["valid_json_rate"] == 0.0

    def test_truncated_json_detected(self):
        """Truncated JSON is classified as truncated."""
        texts = [
            '{"ticket_id": "t1", "branch_type": "fix", "read_set": ["src/',
        ]
        result = eval_json_validity(texts)
        assert result["truncated_rate"] > 0.0

    def test_mixed_results(self):
        """Mix of valid, invalid, truncated produces correct rates."""
        texts = [
            json.dumps({"valid": True}),         # valid
            "not json",                           # invalid
            '{"truncated": "yes',                 # truncated
            json.dumps({"also": "valid"}),        # valid
        ]
        result = eval_json_validity(texts)
        assert result["valid_json_rate"] == 0.5
        assert result["truncated_rate"] > 0.0

    def test_empty_input(self):
        """Empty list returns zeros."""
        result = eval_json_validity([])
        assert result["valid_json_rate"] == 0.0

    def test_json_embedded_in_text(self):
        """JSON embedded in surrounding text is still detected."""
        text = 'Here is the ticket: {"ticket_id": "t1"} done.'
        result = eval_json_validity([text])
        assert result["valid_json_rate"] == 1.0
