"""Branch SFT (Supervised Fine-Tuning) scaffold for RuntimeCoder Phase 1.

Runs a smoke test: 3 gradient steps on fixture BranchTicket examples,
validating that runtime special tokens appear in training data.
"""

import dataclasses
import json
import os
import time
from typing import Dict, List, Optional

import torch
import torch.optim as optim

from runtime_coder.data_pipeline.fixtures import generate_all_fixtures
from runtime_coder.model.runtime_coder_micro import (
    RuntimeCoderMicroConfig,
    build_micro_model,
    count_parameters,
)
from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)


@dataclasses.dataclass
class BranchSFTConfig:
    """Configuration for Branch SFT training."""

    model_config: Optional[RuntimeCoderMicroConfig] = None
    batch_size: int = 2
    lr: float = 1e-4
    max_steps: int = 3
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    max_seq_len: int = 256
    report_path: str = "evaluation/runtime_coder_phase1/branch_sft_smoke_report.json"

    def __post_init__(self):
        if self.model_config is None:
            self.model_config = RuntimeCoderMicroConfig()


def _build_branch_sft_examples() -> List[str]:
    """Build SFT training examples from BranchTicket fixtures.

    Each example uses runtime special tokens to structure the training data.
    """
    fixtures = generate_all_fixtures()
    ticket = fixtures["branch_ticket"]
    ir = fixtures["branch_ir"]
    evidence = fixtures["evidence_packet"]
    verifier = fixtures["verifier_result"]

    examples = []

    # Example 1: Branch ticket creation
    ex1 = (
        f"<|branch_start|>"
        f"<|branch_ticket|>{ticket.ticket_id}\n"
        f"<|branch_type|>{ticket.branch_type}\n"
        f"<|branch_privilege|>{ticket.privilege_level}\n"
        f"<|branch_read_set|>{', '.join(ticket.read_set)}\n"
        f"<|branch_write_set|>{', '.join(ticket.write_set)}\n"
        f"<|branch_end|>"
    )
    examples.append(ex1)

    # Example 2: Branch IR execution
    ex2 = (
        f"<|branch_start|>"
        f"<|branch_ticket|>{ir.ticket_id}\n"
        f"<|branch_ir|>\n"
    )
    for step in ir.steps:
        ex2 += f"<|branch_step|>{step['action']}: {step['target']}\n"
    ex2 += "<|branch_end|>"
    examples.append(ex2)

    # Example 3: Evidence + Verification flow
    ex3 = (
        f"<|evidence_start|>"
        f"<|evidence_type|>{evidence.evidence_type}\n"
        f"<|evidence_confidence|>{evidence.confidence}\n"
        f"<|evidence_data|>{evidence.content}\n"
        f"<|evidence_end|>"
        f"<|verifier_start|>"
        f"<|verifier_pass|>\n"
        f"<|verifier_score|>{verifier.score}\n"
        f"<|verifier_end|>"
    )
    examples.append(ex3)

    # Example 4: Full commit flow
    commit = fixtures["commit_result"]
    ex4 = (
        f"<|commit_start|>"
        f"<|commit_accept|>\n"
        f"<|commit_files|>{', '.join(commit.files_created)}\n"
        f"<|commit_end|>"
    )
    examples.append(ex4)

    return examples


def _text_to_ids(text: str, vocab_size: int, max_len: int) -> torch.Tensor:
    """Convert text to token IDs, mapping special tokens to their reserved IDs."""
    ids = []
    i = 0
    while i < len(text) and len(ids) < max_len:
        matched = False
        # Try to match special tokens
        for token in SPECIAL_TOKENS:
            if text[i:].startswith(token):
                token_id = SPECIAL_TOKEN_ID_OFFSET + SPECIAL_TOKENS.index(token)
                # Only use special token ID if within vocab range
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

    # Pad
    while len(ids) < max_len:
        ids.append(0)

    return torch.tensor(ids[:max_len], dtype=torch.long)


def _validate_special_tokens_in_data(examples: List[str]) -> Dict[str, bool]:
    """Validate that runtime special tokens appear in training data."""
    all_text = " ".join(examples)
    found_tokens = {}
    for token in SPECIAL_TOKENS:
        found_tokens[token] = token in all_text

    return {
        "total_special_tokens": len(SPECIAL_TOKENS),
        "tokens_found_in_data": sum(1 for v in found_tokens.values() if v),
        "branch_tokens_present": all(
            t in all_text for t in ["<|branch_start|>", "<|branch_end|>", "<|branch_ticket|>"]
        ),
        "evidence_tokens_present": all(
            t in all_text for t in ["<|evidence_start|>", "<|evidence_end|>"]
        ),
        "verifier_tokens_present": all(
            t in all_text for t in ["<|verifier_start|>", "<|verifier_end|>"]
        ),
    }


def run_branch_sft_smoke(config: Optional[BranchSFTConfig] = None) -> Dict:
    """Run Branch SFT smoke test: 3 gradient steps on fixture examples.

    Args:
        config: SFT configuration. Uses defaults if None.

    Returns:
        Dictionary with metrics.
    """
    if config is None:
        config = BranchSFTConfig()

    device = config.device
    print(f"  Device: {device}")

    # Build model
    model = build_micro_model(config.model_config, device=device)
    param_info = count_parameters(model)
    print(f"  Model parameters: {param_info['total']:,}")

    # Build training data
    examples = _build_branch_sft_examples()
    print(f"  Training examples: {len(examples)}")

    # Validate special tokens
    token_validation = _validate_special_tokens_in_data(examples)
    print(f"  Special tokens in data: {token_validation['tokens_found_in_data']}/{token_validation['total_special_tokens']}")
    print(f"  Branch tokens present: {token_validation['branch_tokens_present']}")

    # Convert to token IDs
    vocab_size = config.model_config.vocab_size
    max_len = config.max_seq_len

    all_input_ids = []
    for text in examples:
        ids = _text_to_ids(text, vocab_size, max_len)
        all_input_ids.append(ids)

    dataset = torch.stack(all_input_ids).to(device)

    # Optimizer
    optimizer = optim.AdamW(model.parameters(), lr=config.lr)

    # Training loop
    model.train()
    metrics = {
        "losses": [],
        "steps": config.max_steps,
        "param_count": param_info["total"],
        "device": device,
        "special_token_validation": token_validation,
    }

    for step in range(config.max_steps):
        # Sample batch
        batch_indices = torch.randint(0, len(dataset), (config.batch_size,))
        batch = dataset[batch_indices]

        # Forward pass
        output = model(batch, labels=batch)
        loss = output["loss"]

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        metrics["losses"].append(loss.item())
        print(f"    Step {step + 1}/{config.max_steps}: loss={loss.item():.4f}")

    # Verify purity counters
    model.eval()
    with torch.no_grad():
        test_input = torch.randint(0, vocab_size, (1, 32), device=device)
        test_output = model(test_input)
        metrics["purity_counters"] = test_output["purity_counters"]

    # Save report
    report_dir = os.path.dirname(config.report_path)
    if report_dir:
        os.makedirs(report_dir, exist_ok=True)
    with open(config.report_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"  Report saved: {config.report_path}")

    return metrics
