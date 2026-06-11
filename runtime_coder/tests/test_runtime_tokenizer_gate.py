"""Tests for the runtime tokenizer gate (Gate 0)."""

import pytest

from runtime_coder.tokenizer.runtime_tokenizer_gate import validate_runtime_tokenizer


class TestRuntimeTokenizerGate:
    """Gate 0 validation tests."""

    def test_gate_returns_confirmed(self):
        """Gate 0 should return CONFIRMED status."""
        result = validate_runtime_tokenizer()
        assert result["status"] == "CONFIRMED", f"Gate blocked: {result['errors']}"

    def test_all_checks_pass(self):
        """All individual checks should pass."""
        result = validate_runtime_tokenizer()
        for check_name, passed in result["checks"].items():
            assert passed, f"Check failed: {check_name}"

    def test_special_tokens_check(self):
        """Special tokens exist and have unique IDs."""
        result = validate_runtime_tokenizer()
        assert result["checks"]["special_tokens_exist_unique"]

    def test_json_roundtrip_check(self):
        """JSON round-trip through tokenizer works."""
        result = validate_runtime_tokenizer()
        assert result["checks"]["json_roundtrip"]

    def test_python_indentation_check(self):
        """Python indentation survives tokenizer round-trip."""
        result = validate_runtime_tokenizer()
        assert result["checks"]["python_indentation_roundtrip"]

    def test_diff_hunk_check(self):
        """Diff hunks survive tokenizer round-trip."""
        result = validate_runtime_tokenizer()
        assert result["checks"]["diff_hunk_roundtrip"]

    def test_traceback_check(self):
        """Python tracebacks survive tokenizer round-trip."""
        result = validate_runtime_tokenizer()
        assert result["checks"]["traceback_roundtrip"]

    def test_no_errors(self):
        """No errors in gate validation."""
        result = validate_runtime_tokenizer()
        assert result["errors"] == []

    def test_vocab_size_reported(self):
        """Tokenizer vocab size is reported."""
        result = validate_runtime_tokenizer()
        assert result["tokenizer_vocab_size"] > 0

    def test_special_token_count_reported(self):
        """Special token count is reported."""
        result = validate_runtime_tokenizer()
        assert result["special_token_count"] > 60  # We have ~75 tokens
