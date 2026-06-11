"""Fill-in-the-Middle (FIM) dataset for code pretraining.

Creates FIM examples using the <|fim_prefix|>, <|fim_middle|>, <|fim_suffix|>
special tokens from the RuntimeCoder protocol.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FIMExample:
    """A fill-in-the-middle training example.

    The model sees: <|fim_prefix|>{prefix}<|fim_suffix|>{suffix}<|fim_middle|>{middle}
    And learns to predict the middle portion.
    """

    prefix: str
    middle: str
    suffix: str
    full_text: str

    def to_training_format(self) -> str:
        """Convert to the PSM (prefix-suffix-middle) training format."""
        return (
            f"<|fim_prefix|>{self.prefix}"
            f"<|fim_suffix|>{self.suffix}"
            f"<|fim_middle|>{self.middle}"
        )

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "prefix": self.prefix,
            "middle": self.middle,
            "suffix": self.suffix,
            "full_text": self.full_text,
        }


def create_fim_example(
    text: str,
    fim_rate: float = 0.5,
    min_middle_chars: int = 10,
    max_middle_ratio: float = 0.5,
) -> Optional[FIMExample]:
    """Create a FIM example from a text by randomly splitting into prefix/middle/suffix.

    Args:
        text: Source text to create FIM example from
        fim_rate: Probability of actually creating a FIM example (vs returning None)
        min_middle_chars: Minimum characters in the middle portion
        max_middle_ratio: Maximum ratio of text that can be the middle

    Returns:
        FIMExample if created, None if skipped by fim_rate or text too short.
    """
    if random.random() > fim_rate:
        return None

    if len(text) < min_middle_chars * 3:
        return None

    # Choose split points
    max_middle_len = int(len(text) * max_middle_ratio)
    middle_len = random.randint(min_middle_chars, max(min_middle_chars, max_middle_len))

    # Ensure we have room for prefix and suffix
    max_start = len(text) - middle_len - 1
    if max_start < 1:
        return None

    start = random.randint(1, max_start)
    end = start + middle_len

    prefix = text[:start]
    middle = text[start:end]
    suffix = text[end:]

    return FIMExample(
        prefix=prefix,
        middle=middle,
        suffix=suffix,
        full_text=text,
    )


def build_fim_dataset(
    texts: List[str],
    count: int,
    fim_rate: float = 0.5,
    seed: Optional[int] = None,
) -> List[FIMExample]:
    """Build a FIM dataset from a collection of texts.

    Args:
        texts: Source texts to create FIM examples from
        count: Target number of examples to generate
        fim_rate: Probability of creating FIM from each text
        seed: Random seed for reproducibility

    Returns:
        List of FIMExample instances (may be fewer than count if texts are limited).
    """
    if seed is not None:
        random.seed(seed)

    examples = []
    attempts = 0
    max_attempts = count * 10  # Avoid infinite loop

    while len(examples) < count and attempts < max_attempts:
        text = random.choice(texts)
        example = create_fim_example(text, fim_rate=fim_rate)
        if example is not None:
            examples.append(example)
        attempts += 1

    return examples
