"""File boundary dataset for multi-file context pretraining.

Creates training examples that teach the model about file boundaries using
<|file_sep|> and <|path|> special tokens from the RuntimeCoder protocol.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class FileBoundaryExample:
    """A multi-file context training example.

    Contains multiple files concatenated with boundary tokens so the model
    learns to understand file separations and path associations.
    """

    files: List[dict] = field(default_factory=list)
    """List of dicts with 'path' and 'content' keys."""

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {"files": self.files}


def create_file_boundary_example(file_list: List[Tuple[str, str]]) -> str:
    """Create a formatted string with file boundary tokens.

    Format:
        <|file_sep|><|path|>path/to/file1.py
        content of file 1
        <|file_sep|><|path|>path/to/file2.py
        content of file 2

    Args:
        file_list: List of (path, content) tuples

    Returns:
        Formatted string with boundary tokens.
    """
    parts = []
    for path, content in file_list:
        parts.append(f"<|file_sep|><|path|>{path}\n{content}")

    return "\n".join(parts)


def build_file_boundary_dataset(
    repo_files: List[Tuple[str, str]],
    examples_per_window: int = 5,
    max_examples: Optional[int] = None,
    seed: Optional[int] = None,
) -> List[FileBoundaryExample]:
    """Build a file boundary dataset from repository files.

    Creates examples by grouping files into windows and formatting them
    with boundary tokens.

    Args:
        repo_files: List of (path, content) tuples from a repository
        examples_per_window: Number of files per training example
        max_examples: Maximum number of examples to generate (None = all possible)
        seed: Random seed for reproducibility

    Returns:
        List of FileBoundaryExample instances.
    """
    if seed is not None:
        random.seed(seed)

    if not repo_files:
        return []

    examples = []

    # Shuffle files for variety
    shuffled = list(repo_files)
    random.shuffle(shuffled)

    # Create windows of files
    i = 0
    while i < len(shuffled):
        window = shuffled[i:i + examples_per_window]
        if len(window) < 2:
            # Need at least 2 files for a boundary example
            break

        example = FileBoundaryExample(
            files=[{"path": path, "content": content} for path, content in window]
        )
        examples.append(example)

        i += examples_per_window

        if max_examples is not None and len(examples) >= max_examples:
            break

    return examples
