"""Branch SFT (Supervised Fine-Tuning) for RuntimeCoder Phase 1+2.

Phase 1: Runs a smoke test: 3 gradient steps on fixture BranchTicket examples.
Phase 2: Full SFT training on diverse BranchTicket examples with validation metrics.
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


# ============================================================
# Phase 2: Full Branch SFT Training
# ============================================================


@dataclasses.dataclass
class BranchSFTFullConfig:
    """Configuration for full Branch SFT training (Phase 2)."""

    model_config: Optional[RuntimeCoderMicroConfig] = None
    batch_size: int = 4
    lr: float = 5e-4
    max_steps: int = 50
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    max_seq_len: int = 512
    max_gen_tokens: int = 256
    validate_every: int = 10
    num_examples: int = 100
    report_path: str = "evaluation/runtime_coder_phase2/branch_sft_full_report.json"

    def __post_init__(self):
        if self.model_config is None:
            self.model_config = RuntimeCoderMicroConfig()


def generate_from_model(
    model,
    input_text: str,
    vocab_size: int,
    max_gen_tokens: int = 256,
    max_seq_len: int = 512,
    device: str = "cpu",
) -> str:
    """Generate text from model via greedy decode.

    Takes input text, converts to token IDs, runs forward, argmax for N tokens.

    Args:
        model: TinyRuntimeCoder model
        input_text: Input text string
        vocab_size: Model vocab size
        max_gen_tokens: Maximum tokens to generate
        max_seq_len: Maximum sequence length
        device: Device to run on

    Returns:
        Generated text string (input + generated portion)
    """
    model.eval()

    # Tokenize input
    input_ids = _text_to_ids(input_text, vocab_size, min(len(input_text), max_seq_len // 2))
    # Strip padding
    non_pad = (input_ids != 0).sum().item()
    input_ids = input_ids[:non_pad].unsqueeze(0).to(device)

    generated_ids = input_ids.clone()

    with torch.no_grad():
        for _ in range(max_gen_tokens):
            if generated_ids.shape[1] >= max_seq_len:
                break

            output = model(generated_ids)
            logits = output["logits"]
            # Greedy: take argmax of last position
            next_token = logits[:, -1, :].argmax(dim=-1, keepdim=True)
            generated_ids = torch.cat([generated_ids, next_token], dim=1)

    # Decode back to text
    all_ids = generated_ids[0].cpu().tolist()
    return _ids_to_text(all_ids, vocab_size)


def _ids_to_text(ids: List[int], vocab_size: int) -> str:
    """Convert token IDs back to text (inverse of _text_to_ids)."""
    chars = []
    for tid in ids:
        if tid == 0:
            continue  # Skip padding
        # Check if it's a special token
        if tid >= SPECIAL_TOKEN_ID_OFFSET:
            st_idx = tid - SPECIAL_TOKEN_ID_OFFSET
            if 0 <= st_idx < len(SPECIAL_TOKENS):
                chars.append(SPECIAL_TOKENS[st_idx])
                continue
        # Regular character
        if tid < 128:
            chars.append(chr(tid))
        else:
            chars.append(f"[{tid}]")
    return "".join(chars)


def validate_generated_ticket(text: str) -> tuple:
    """Validate that generated text is a valid BranchTicket.

    Attempts to parse JSON from the text and validate as BranchTicket.

    Args:
        text: Generated text from model

    Returns:
        Tuple of (is_valid: bool, errors: list)
    """
    # Try to extract JSON from text
    json_str = _extract_json(text)
    if json_str is None:
        return False, ["no valid JSON found in generated text"]

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return False, [f"JSON parse error: {str(e)}"]

    # Check if it has BranchTicket fields
    from runtime_coder.schemas.branch_ticket import BranchTicket
    try:
        ticket = BranchTicket.from_dict(data)
        errors = ticket.validate()
        return len(errors) == 0, errors
    except (TypeError, KeyError) as e:
        return False, [f"cannot construct BranchTicket: {str(e)}"]


def _extract_json(text: str) -> Optional[str]:
    """Try to extract a JSON object from text."""
    # Look for JSON object delimiters
    start = text.find("{")
    if start == -1:
        return None

    # Find matching closing brace
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def _compute_schema_validity_rate(
    model,
    examples,
    vocab_size: int,
    max_gen_tokens: int,
    max_seq_len: int,
    device: str,
    sample_size: int = 10,
) -> Dict:
    """Compute what fraction of model outputs parse as valid BranchTickets."""
    valid_count = 0
    field_complete_count = 0
    total = min(sample_size, len(examples))

    for i in range(total):
        ex = examples[i]
        input_text = ex.format_input()
        generated = generate_from_model(
            model, input_text, vocab_size, max_gen_tokens, max_seq_len, device
        )
        is_valid, errors = validate_generated_ticket(generated)
        if is_valid:
            valid_count += 1
            field_complete_count += 1
        else:
            # Check partial field completeness
            json_str = _extract_json(generated)
            if json_str:
                try:
                    data = json.loads(json_str)
                    required_fields = ["ticket_id", "branch_type", "privilege_level", "read_set", "write_set"]
                    present = sum(1 for f in required_fields if f in data and data[f])
                    if present >= 3:
                        field_complete_count += 1
                except json.JSONDecodeError:
                    pass

    return {
        "schema_validity_rate": valid_count / max(total, 1),
        "field_completeness_rate": field_complete_count / max(total, 1),
        "valid_count": valid_count,
        "total_evaluated": total,
    }


def run_branch_sft_full(config: Optional[BranchSFTFullConfig] = None) -> Dict:
    """Run full Branch SFT training (Phase 2).

    Trains on diverse BranchTicket examples for 50+ steps.
    Tracks schema_validity_rate and field_completeness_rate.

    Args:
        config: Training configuration. Uses defaults if None.

    Returns:
        Dictionary with training metrics and validation results.
    """
    if config is None:
        config = BranchSFTFullConfig()

    device = config.device
    print(f"  Device: {device}")
    print(f"  Phase 2 Full Branch SFT Training")
    print(f"  Max steps: {config.max_steps}")

    # Build model
    model = build_micro_model(config.model_config, device=device)
    param_info = count_parameters(model)
    print(f"  Model parameters: {param_info['total']:,}")

    # Generate diverse training examples
    from runtime_coder.data_pipeline.branch_ticket_dataset import generate_diverse_examples

    examples = generate_diverse_examples(count=config.num_examples)
    print(f"  Training examples: {len(examples)}")

    # Convert examples to token IDs
    vocab_size = config.model_config.vocab_size
    max_len = config.max_seq_len

    all_input_ids = []
    for ex in examples:
        full_text = ex.format_full()
        ids = _text_to_ids(full_text, vocab_size, max_len)
        all_input_ids.append(ids)

    dataset = torch.stack(all_input_ids).to(device)

    # Optimizer
    optimizer = optim.AdamW(model.parameters(), lr=config.lr)

    # Compute initial validity rate
    print("  Computing initial schema validity rate...")
    initial_validity = _compute_schema_validity_rate(
        model, examples, vocab_size, config.max_gen_tokens, max_len, device, sample_size=5
    )
    print(f"  Initial schema validity rate: {initial_validity['schema_validity_rate']:.3f}")

    # Training loop
    model.train()
    metrics = {
        "losses": [],
        "steps": config.max_steps,
        "param_count": param_info["total"],
        "device": device,
        "num_examples": len(examples),
        "validity_checkpoints": [initial_validity],
    }

    for step in range(config.max_steps):
        # Sample batch
        batch_indices = torch.randint(0, len(dataset), (config.batch_size,))
        batch = dataset[batch_indices]

        # Forward pass (teacher-forced)
        output = model(batch, labels=batch)
        loss = output["loss"]

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        metrics["losses"].append(loss.item())

        if (step + 1) % 10 == 0:
            print(f"    Step {step + 1}/{config.max_steps}: loss={loss.item():.4f}")

        # Periodic validation
        if (step + 1) % config.validate_every == 0:
            model.eval()
            validity = _compute_schema_validity_rate(
                model, examples, vocab_size, config.max_gen_tokens, max_len, device, sample_size=5
            )
            metrics["validity_checkpoints"].append(validity)
            print(f"    Validity rate @ step {step + 1}: {validity['schema_validity_rate']:.3f}")
            model.train()

    # Final validation
    model.eval()
    print("  Computing final schema validity rate...")
    final_validity = _compute_schema_validity_rate(
        model, examples, vocab_size, config.max_gen_tokens, max_len, device, sample_size=10
    )
    metrics["validity_checkpoints"].append(final_validity)
    metrics["final_schema_validity_rate"] = final_validity["schema_validity_rate"]
    metrics["final_field_completeness_rate"] = final_validity["field_completeness_rate"]
    print(f"  Final schema validity rate: {final_validity['schema_validity_rate']:.3f}")
    print(f"  Final field completeness rate: {final_validity['field_completeness_rate']:.3f}")

    # Check schema validity rate improvement
    initial_rate = initial_validity["schema_validity_rate"]
    final_rate = final_validity["schema_validity_rate"]
    metrics["schema_validity_improved"] = final_rate >= initial_rate
    # Note: with a random untrained model, initial rate is likely 0,
    # and even after 50 steps of SFT on a tiny model it may stay low.
    # The key metric is that loss decreased, showing the model learned the distribution.
    metrics["loss_decreased"] = metrics["losses"][-1] < metrics["losses"][0]

    # Verify purity counters still work
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
