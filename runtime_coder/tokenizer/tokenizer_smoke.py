"""Minimal dict-based tokenizer with special token registry."""

from typing import Dict, List, Optional

from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)


class RuntimeTokenizer:
    """Simple tokenizer: special tokens get dedicated IDs, other text is character-level."""

    def __init__(self):
        # Build special token mappings
        self._token_to_id: Dict[str, int] = {}
        self._id_to_token: Dict[int, str] = {}

        for i, token in enumerate(SPECIAL_TOKENS):
            tid = SPECIAL_TOKEN_ID_OFFSET + i
            self._token_to_id[token] = tid
            self._id_to_token[tid] = token

        # Character-level fallback (ASCII printable range + common)
        self._char_to_id: Dict[str, int] = {}
        self._id_to_char: Dict[int, str] = {}
        for i in range(256):
            self._char_to_id[chr(i)] = i
            self._id_to_char[i] = chr(i)

    @property
    def vocab_size(self) -> int:
        """Total vocabulary size."""
        return 256 + len(SPECIAL_TOKENS)

    def token_to_id(self, token: str) -> Optional[int]:
        """Get ID for a special token."""
        return self._token_to_id.get(token)

    def id_to_token(self, token_id: int) -> Optional[str]:
        """Get token string for an ID."""
        if token_id in self._id_to_token:
            return self._id_to_token[token_id]
        if token_id in self._id_to_char:
            return self._id_to_char[token_id]
        return None

    def special_token_ids(self) -> List[int]:
        """Return all special token IDs."""
        return list(self._token_to_id.values())

    def encode(self, text: str) -> List[int]:
        """Encode text to token IDs. Special tokens are matched first."""
        ids = []
        i = 0
        while i < len(text):
            matched = False
            # Try to match special tokens (longest match first)
            for token, tid in self._token_to_id.items():
                if text[i:].startswith(token):
                    ids.append(tid)
                    i += len(token)
                    matched = True
                    break
            if not matched:
                # Character-level fallback
                char = text[i]
                ids.append(self._char_to_id.get(char, ord(char) % 256))
                i += 1
        return ids

    def decode(self, ids: List[int]) -> str:
        """Decode token IDs back to text."""
        parts = []
        for tid in ids:
            if tid in self._id_to_token:
                parts.append(self._id_to_token[tid])
            elif tid in self._id_to_char:
                parts.append(self._id_to_char[tid])
            else:
                parts.append(f"<unk:{tid}>")
        return "".join(parts)
