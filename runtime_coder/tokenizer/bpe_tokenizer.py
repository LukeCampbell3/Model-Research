"""BPE Tokenizer scaffold for RuntimeCoder Phase 1.

RUNTIME_CODER_BPE_SCAFFOLD - This is a pre-built vocabulary tokenizer,
not a full 100K-merge trained BPE. It uses Python keywords, common code
patterns, and byte-level fallback to simulate a 32K base vocab with
reserved IDs 50000-50074 for runtime special tokens.
"""

import re
from typing import Dict, List, Optional, Tuple

from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)

# Python keywords and builtins for the base vocabulary
_PYTHON_KEYWORDS = [
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield",
]

_PYTHON_BUILTINS = [
    "print", "len", "range", "int", "str", "float", "list", "dict",
    "tuple", "set", "bool", "type", "isinstance", "getattr", "setattr",
    "hasattr", "enumerate", "zip", "map", "filter", "sorted", "reversed",
    "sum", "min", "max", "abs", "all", "any", "open", "super", "object",
    "Exception", "ValueError", "TypeError", "KeyError", "IndexError",
    "AttributeError", "RuntimeError", "StopIteration", "NotImplementedError",
]

_COMMON_CODE_PATTERNS = [
    "self", "cls", "args", "kwargs", "init", "__init__", "__main__",
    "    ", "        ", "            ",  # indentation patterns
    "def ", "class ", "import ", "from ", "return ", "yield ",
    "if __name__", "== '__main__'",
    "-> ", "Optional[", "List[", "Dict[", "Tuple[", "Set[",
    "torch", "nn", "Module", "forward", "tensor", "Tensor",
    "numpy", "np", "os", "sys", "json", "math", "typing",
    "dataclass", "field", "dataclasses",
    "pytest", "test_", "assert ",
    ".py", ".json", ".yaml", ".toml",
    "# ", "\"\"\"", "'''",
    "\\n", "\\t", "  ",
    "(self)", "(self, ", "(**kwargs)",
    "-> None", "-> bool", "-> int", "-> str", "-> float",
    "-> List", "-> Dict", "-> Optional",
]


class BPETokenizer:
    """Pre-built BPE tokenizer scaffold for code pretraining.

    RUNTIME_CODER_BPE_SCAFFOLD:
    - Base vocabulary: ~32000 tokens (byte-level + common code patterns)
    - Special token IDs: 50000-50074 reserved for runtime protocol tokens
    - Supports train_from_texts (builds merge table from corpus)
    - Encode/decode with special token awareness
    """

    def __init__(self, vocab_size: int = 32000):
        self._target_vocab_size = vocab_size
        self._token_to_id: Dict[str, int] = {}
        self._id_to_token: Dict[int, str] = {}
        self._merges: List[Tuple[str, str]] = []

        # Build the base vocabulary
        self._build_base_vocab()

        # Register special tokens at reserved offsets
        self._register_special_tokens()

    def _build_base_vocab(self):
        """Build base vocabulary from byte-level + code patterns."""
        idx = 0

        # Byte-level tokens (0-255)
        for i in range(256):
            token = bytes([i]).decode("latin-1")
            self._token_to_id[f"<byte_{i}>"] = idx
            self._id_to_token[idx] = f"<byte_{i}>"
            idx += 1

        # Python keywords
        for kw in _PYTHON_KEYWORDS:
            if kw not in self._token_to_id:
                self._token_to_id[kw] = idx
                self._id_to_token[idx] = kw
                idx += 1

        # Python builtins
        for builtin in _PYTHON_BUILTINS:
            if builtin not in self._token_to_id:
                self._token_to_id[builtin] = idx
                self._id_to_token[idx] = builtin
                idx += 1

        # Common code patterns
        for pattern in _COMMON_CODE_PATTERNS:
            if pattern not in self._token_to_id:
                self._token_to_id[pattern] = idx
                self._id_to_token[idx] = pattern
                idx += 1

        # Fill remaining slots with common character pairs
        common_pairs = []
        chars = "abcdefghijklmnopqrstuvwxyz_0123456789"
        for c1 in chars:
            for c2 in chars:
                common_pairs.append(c1 + c2)

        for pair in common_pairs:
            if idx >= self._target_vocab_size:
                break
            if pair not in self._token_to_id:
                self._token_to_id[pair] = idx
                self._id_to_token[idx] = pair
                idx += 1

        self._base_vocab_size = idx

    def _register_special_tokens(self):
        """Register runtime special tokens at reserved IDs 50000+."""
        for i, token in enumerate(SPECIAL_TOKENS):
            tid = SPECIAL_TOKEN_ID_OFFSET + i
            self._token_to_id[token] = tid
            self._id_to_token[tid] = token

    @property
    def vocab_size(self) -> int:
        """Total effective vocab size (base + special token range)."""
        return max(self._base_vocab_size, SPECIAL_TOKEN_ID_OFFSET + len(SPECIAL_TOKENS))

    @property
    def base_vocab_size(self) -> int:
        """Base vocab size (without special tokens)."""
        return self._base_vocab_size

    @property
    def special_token_count(self) -> int:
        """Number of registered special tokens."""
        return len(SPECIAL_TOKENS)

    def special_token_ids(self) -> List[int]:
        """Return all special token IDs."""
        return [SPECIAL_TOKEN_ID_OFFSET + i for i in range(len(SPECIAL_TOKENS))]

    def train_from_texts(self, texts: List[str], vocab_size: int = 32000) -> None:
        """Train BPE merges from a corpus of texts.

        SCAFFOLD: This performs simplified pair-frequency merges on the provided
        texts to build a merge table. Not a production-grade BPE trainer.
        """
        self._target_vocab_size = vocab_size
        # Tokenize texts into characters
        word_freqs: Dict[str, int] = {}
        for text in texts:
            words = text.split()
            for word in words:
                word_freqs[word] = word_freqs.get(word, 0) + 1

        # Build initial split (character-level)
        splits: Dict[str, List[str]] = {}
        for word in word_freqs:
            splits[word] = list(word)

        # Iterative merging
        num_merges = min(500, vocab_size - self._base_vocab_size)
        for _ in range(num_merges):
            # Count pair frequencies
            pair_freqs: Dict[Tuple[str, str], int] = {}
            for word, freq in word_freqs.items():
                split = splits[word]
                for i in range(len(split) - 1):
                    pair = (split[i], split[i + 1])
                    pair_freqs[pair] = pair_freqs.get(pair, 0) + freq

            if not pair_freqs:
                break

            # Find most frequent pair
            best_pair = max(pair_freqs, key=pair_freqs.get)
            self._merges.append(best_pair)

            # Merge the best pair in all splits
            merged_token = best_pair[0] + best_pair[1]
            if merged_token not in self._token_to_id:
                new_id = self._base_vocab_size + len(self._merges) - 1
                self._token_to_id[merged_token] = new_id
                self._id_to_token[new_id] = merged_token

            for word in splits:
                split = splits[word]
                new_split = []
                i = 0
                while i < len(split):
                    if i < len(split) - 1 and (split[i], split[i + 1]) == best_pair:
                        new_split.append(merged_token)
                        i += 2
                    else:
                        new_split.append(split[i])
                        i += 1
                splits[word] = new_split

    def encode(self, text: str) -> List[int]:
        """Encode text to token IDs.

        Special tokens are matched first via regex, then remaining text
        is tokenized using the BPE vocabulary with byte-level fallback.
        """
        ids = []
        # Build regex for special tokens
        special_pattern = "|".join(re.escape(t) for t in SPECIAL_TOKENS)
        pattern = f"({special_pattern})"

        parts = re.split(pattern, text)

        for part in parts:
            if not part:
                continue
            if part in self._token_to_id and part in SPECIAL_TOKENS:
                ids.append(self._token_to_id[part])
            else:
                # Tokenize using vocabulary lookup with greedy matching
                ids.extend(self._encode_chunk(part))

        return ids

    def _encode_chunk(self, text: str) -> List[int]:
        """Encode a chunk of text (no special tokens) using BPE vocab."""
        ids = []
        i = 0
        while i < len(text):
            # Try longest match from vocabulary (up to 20 chars)
            best_match = None
            best_len = 0
            for length in range(min(20, len(text) - i), 0, -1):
                candidate = text[i:i + length]
                if candidate in self._token_to_id:
                    tid = self._token_to_id[candidate]
                    # Skip special tokens in chunk encoding
                    if tid < SPECIAL_TOKEN_ID_OFFSET:
                        best_match = tid
                        best_len = length
                        break

            if best_match is not None:
                ids.append(best_match)
                i += best_len
            else:
                # Byte-level fallback
                byte_val = ord(text[i]) % 256
                ids.append(byte_val)  # maps to <byte_N>
                i += 1

        return ids

    def decode(self, ids: List[int]) -> str:
        """Decode token IDs back to text."""
        parts = []
        for tid in ids:
            if tid in self._id_to_token:
                token = self._id_to_token[tid]
                if token.startswith("<byte_") and token.endswith(">"):
                    # Byte-level token
                    byte_val = int(token[6:-1])
                    parts.append(chr(byte_val))
                else:
                    parts.append(token)
            else:
                parts.append(f"<unk:{tid}>")
        return "".join(parts)

    def token_to_id(self, token: str) -> Optional[int]:
        """Get ID for a token."""
        return self._token_to_id.get(token)

    def id_to_token(self, token_id: int) -> Optional[str]:
        """Get token string for an ID."""
        return self._id_to_token.get(token_id)
