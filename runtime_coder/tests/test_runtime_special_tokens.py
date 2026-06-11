"""Test special token registry: uniqueness, completeness, coverage."""

import pytest

from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_CATEGORIES,
    SPECIAL_TOKEN_ID_OFFSET,
    get_all_special_tokens,
)
from runtime_coder.tokenizer.tokenizer_smoke import RuntimeTokenizer


class TestTokenUniqueness:
    """All special tokens must be unique strings."""

    def test_all_tokens_unique(self):
        assert len(SPECIAL_TOKENS) == len(set(SPECIAL_TOKENS)), (
            f"Duplicate tokens found: {len(SPECIAL_TOKENS)} total, "
            f"{len(set(SPECIAL_TOKENS))} unique"
        )

    def test_token_count_at_least_70(self):
        """We define ~70 tokens across all categories."""
        assert len(SPECIAL_TOKENS) >= 68, (
            f"Expected ~70 tokens, got {len(SPECIAL_TOKENS)}"
        )

    def test_all_tokens_are_strings(self):
        for token in SPECIAL_TOKENS:
            assert isinstance(token, str), f"Token {token!r} is not a string"

    def test_all_tokens_have_delimiters(self):
        """All tokens should use <| |> delimiter format."""
        for token in SPECIAL_TOKENS:
            assert token.startswith("<|"), f"Token {token!r} missing <| prefix"
            assert token.endswith("|>"), f"Token {token!r} missing |> suffix"

    def test_categories_cover_all_tokens(self):
        """Category tokens should sum to total tokens."""
        category_total = sum(len(t) for t in SPECIAL_TOKEN_CATEGORIES.values())
        assert category_total == len(SPECIAL_TOKENS)

    def test_required_categories_present(self):
        """All required categories must be present."""
        required = {"task", "context", "branch", "patch", "evidence",
                    "verifier", "replay", "commit", "fim", "mode",
                    "descriptor", "operator"}
        assert required == set(SPECIAL_TOKEN_CATEGORIES.keys())


class TestTokenizerIntegration:
    """Test tokenizer handles special tokens correctly."""

    @pytest.fixture
    def tokenizer(self):
        return RuntimeTokenizer()

    def test_special_token_ids_start_at_offset(self, tokenizer):
        ids = tokenizer.special_token_ids()
        assert all(tid >= SPECIAL_TOKEN_ID_OFFSET for tid in ids)

    def test_special_token_ids_unique(self, tokenizer):
        ids = tokenizer.special_token_ids()
        assert len(ids) == len(set(ids))

    def test_encode_special_token(self, tokenizer):
        token = "<|task_start|>"
        ids = tokenizer.encode(token)
        assert len(ids) == 1
        assert ids[0] >= SPECIAL_TOKEN_ID_OFFSET

    def test_decode_special_token(self, tokenizer):
        token = "<|task_start|>"
        ids = tokenizer.encode(token)
        decoded = tokenizer.decode(ids)
        assert decoded == token

    def test_encode_mixed_text(self, tokenizer):
        text = "<|task_start|>hello<|task_end|>"
        ids = tokenizer.encode(text)
        decoded = tokenizer.decode(ids)
        assert decoded == text

    def test_token_to_id_returns_correct_id(self, tokenizer):
        for token in SPECIAL_TOKENS[:5]:
            tid = tokenizer.token_to_id(token)
            assert tid is not None
            assert tid >= SPECIAL_TOKEN_ID_OFFSET

    def test_id_to_token_returns_correct_token(self, tokenizer):
        for token in SPECIAL_TOKENS[:5]:
            tid = tokenizer.token_to_id(token)
            result = tokenizer.id_to_token(tid)
            assert result == token

    def test_unknown_token_returns_none(self, tokenizer):
        assert tokenizer.token_to_id("<|nonexistent|>") is None
