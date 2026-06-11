"""Pretraining loop scaffold for RuntimeCoder Phase 1.

Runs a smoke test: 5 gradient steps on synthetic FIM + file-boundary data
using the RuntimeCoder-Micro model.
"""

import dataclasses
import json
import os
import time
from typing import Dict, List, Optional

import torch
import torch.nn as nn
import torch.optim as optim

from runtime_coder.data_pipeline.fim_dataset import FIMExample, build_fim_dataset
from runtime_coder.data_pipeline.file_boundary_dataset import (
    FileBoundaryExample,
    create_file_boundary_example,
)
from runtime_coder.model.runtime_coder_micro import (
    RuntimeCoderMicroConfig,
    build_micro_model,
    count_parameters,
)


@dataclasses.dataclass
class PretrainConfig:
    """Configuration for pretraining."""

    model_config: Optional[RuntimeCoderMicroConfig] = None
    batch_size: int = 2
    lr: float = 3e-4
    max_steps: int = 5
    warmup_steps: int = 1
    eval_interval: int = 5
    checkpoint_dir: str = ""
    dataset_path: str = ""
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    max_seq_len: int = 256  # Shortened for smoke test
    report_path: str = "evaluation/runtime_coder_phase1/pretrain_smoke_report.json"

    def __post_init__(self):
        if self.model_config is None:
            self.model_config = RuntimeCoderMicroConfig()


def _generate_synthetic_texts() -> List[str]:
    """Generate synthetic Python code texts for smoke testing."""
    texts = [
        '''def binary_search(arr, target):
    """Search for target in sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
''',
        '''class DataProcessor:
    """Process and transform data."""

    def __init__(self, config):
        self.config = config
        self.cache = {}

    def process(self, data):
        if data in self.cache:
            return self.cache[data]
        result = self._transform(data)
        self.cache[data] = result
        return result

    def _transform(self, data):
        return data.strip().lower()
''',
        '''import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
''',
        '''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
''',
        '''from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Config:
    learning_rate: float = 0.001
    batch_size: int = 32
    epochs: int = 10
    hidden_dims: List[int] = field(default_factory=lambda: [128, 64])
    dropout: float = 0.1
    device: str = "cuda"

    def validate(self) -> bool:
        if self.learning_rate <= 0:
            return False
        if self.batch_size < 1:
            return False
        return True
''',
        '''import pytest

def test_binary_search_found():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 5) == 2

def test_binary_search_not_found():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 4) == -1

def test_binary_search_empty():
    assert binary_search([], 1) == -1

def test_binary_search_single():
    assert binary_search([5], 5) == 0
''',
    ]
    return texts


def _text_to_token_ids(text: str, vocab_size: int, max_len: int) -> torch.Tensor:
    """Convert text to pseudo-token IDs for smoke testing.

    Uses character-level encoding mapped to vocab range.
    Special token markers in text (FIM tokens) are mapped to their proper IDs.
    """
    from runtime_coder.tokenizer.runtime_special_tokens import (
        SPECIAL_TOKENS,
        SPECIAL_TOKEN_ID_OFFSET,
    )

    ids = []
    i = 0
    while i < len(text) and len(ids) < max_len:
        matched = False
        for token in SPECIAL_TOKENS:
            if text[i:].startswith(token):
                token_id = SPECIAL_TOKEN_ID_OFFSET + SPECIAL_TOKENS.index(token)
                if token_id < vocab_size:
                    ids.append(token_id)
                else:
                    ids.append(token_id % vocab_size)
                i += len(token)
                matched = True
                break
        if not matched:
            ids.append(ord(text[i]) % min(vocab_size, SPECIAL_TOKEN_ID_OFFSET))
            i += 1

    # Pad to max_len
    while len(ids) < max_len:
        ids.append(0)
    return torch.tensor(ids[:max_len], dtype=torch.long)


def run_pretrain_smoke(config: Optional[PretrainConfig] = None) -> Dict:
    """Run pretraining smoke test: 5 gradient steps on synthetic data.

    Args:
        config: Pretraining configuration. Uses defaults if None.

    Returns:
        Dictionary with metrics: losses, tokens_per_sec, memory_mb, param_count.
    """
    if config is None:
        config = PretrainConfig()

    device = config.device
    print(f"  Device: {device}")

    # Build model
    model = build_micro_model(config.model_config, device=device)
    param_info = count_parameters(model)
    print(f"  Model parameters: {param_info['total']:,}")

    # Generate synthetic data
    texts = _generate_synthetic_texts()
    fim_examples = build_fim_dataset(texts, count=20, fim_rate=1.0, seed=42)

    # Build training batch from FIM examples
    vocab_size = config.model_config.vocab_size
    max_len = config.max_seq_len

    training_texts = []
    for ex in fim_examples:
        training_texts.append(ex.to_training_format())

    # Also add file-boundary examples
    file_list = [(f"file_{i}.py", text) for i, text in enumerate(texts)]
    boundary_text = create_file_boundary_example(file_list[:3])
    training_texts.append(boundary_text)

    # Convert to token IDs
    all_input_ids = []
    for text in training_texts:
        ids = _text_to_token_ids(text, vocab_size, max_len)
        all_input_ids.append(ids)

    # Stack into batches
    dataset = torch.stack(all_input_ids).to(device)

    # Optimizer
    optimizer = optim.AdamW(model.parameters(), lr=config.lr)

    # Training loop
    model.train()
    metrics = {
        "losses": [],
        "tokens_per_sec": [],
        "steps": config.max_steps,
        "param_count": param_info["total"],
        "param_breakdown": {k: v for k, v in param_info["breakdown"].items()},
        "device": device,
    }

    total_tokens = 0
    start_time = time.time()

    for step in range(config.max_steps):
        step_start = time.time()

        # Sample batch
        batch_indices = torch.randint(0, len(dataset), (config.batch_size,))
        batch = dataset[batch_indices]

        # Forward pass (input = labels for causal LM)
        output = model(batch, labels=batch)
        loss = output["loss"]

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Metrics
        step_time = time.time() - step_start
        step_tokens = config.batch_size * max_len
        total_tokens += step_tokens
        tokens_per_sec = step_tokens / max(step_time, 1e-6)

        metrics["losses"].append(loss.item())
        metrics["tokens_per_sec"].append(tokens_per_sec)

        print(f"    Step {step + 1}/{config.max_steps}: "
              f"loss={loss.item():.4f}, "
              f"tok/s={tokens_per_sec:.0f}")

    elapsed = time.time() - start_time
    metrics["total_time_sec"] = elapsed
    metrics["avg_tokens_per_sec"] = total_tokens / max(elapsed, 1e-6)

    # Memory usage
    if device == "cuda" and torch.cuda.is_available():
        metrics["memory_mb"] = torch.cuda.max_memory_allocated() / (1024 * 1024)
    else:
        metrics["memory_mb"] = 0.0

    # Check purity counters still work
    model.eval()
    with torch.no_grad():
        test_input = torch.randint(0, vocab_size, (1, 32), device=device)
        test_output = model(test_input)
        metrics["purity_counters"] = test_output["purity_counters"]

    # Loss trend
    if len(metrics["losses"]) >= 2:
        metrics["loss_decreased"] = metrics["losses"][-1] < metrics["losses"][0]
    else:
        metrics["loss_decreased"] = False

    # Save report
    report_dir = os.path.dirname(config.report_path)
    if report_dir:
        os.makedirs(report_dir, exist_ok=True)
    with open(config.report_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"  Report saved: {config.report_path}")

    return metrics
