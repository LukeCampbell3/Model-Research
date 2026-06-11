"""Main Python RuntimeCoder trainer.

Loads config, builds model, loads curriculum data, runs training loop
with eval checkpoints, OOM recovery, and generation logging.
"""

import json
import os
import time
from typing import Dict, Any, Optional

import torch
import torch.optim as optim

from runtime_coder.configs.python_configs import get_config
from runtime_coder.data_pipeline.python_branch_ticket_curriculum import (
    build_curriculum,
    build_mixed_curriculum,
)
from runtime_coder.data_pipeline.python_heldout_split_builder import build_heldout_split
from runtime_coder.model.runtime_coder_micro import (
    RuntimeCoderMicroConfig,
    build_micro_model,
    count_parameters,
)
from runtime_coder.tokenizer.runtime_special_tokens import (
    SPECIAL_TOKENS,
    SPECIAL_TOKEN_ID_OFFSET,
)
from runtime_coder.training.checkpointing import save_checkpoint, find_latest_checkpoint, load_checkpoint
from runtime_coder.training.oom_safe_batching import OOMSafeBatcher


def _text_to_ids(text: str, vocab_size: int, max_len: int) -> torch.Tensor:
    """Convert text to token IDs."""
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

    while len(ids) < max_len:
        ids.append(0)

    return torch.tensor(ids[:max_len], dtype=torch.long)


def _build_dataset(
    config: dict,
    max_seq_len: int,
    vocab_size: int,
) -> tuple:
    """Build train and eval datasets from curriculum.

    Returns:
        Tuple of (train_tensor, eval_tensor, train_examples, eval_examples)
    """
    data_cfg = config["data"]
    stage = data_cfg.get("curriculum_stage", "C")
    num_examples = data_cfg.get("num_examples", 200)

    # Build curriculum
    if stage == "mixed":
        examples = build_mixed_curriculum(size=num_examples, seed=42)
    else:
        examples = build_curriculum(stage=stage, size=num_examples, seed=42)

    # Split into train/eval
    eval_ratio = data_cfg.get("eval_split_ratio", 0.1)
    train_examples, eval_examples = build_heldout_split(examples, eval_ratio=eval_ratio)

    # Convert to tensors
    def examples_to_tensor(exs):
        all_ids = []
        for ex in exs:
            full_text = ex["input"] + "\n" + ex["target"]
            ids = _text_to_ids(full_text, vocab_size, max_seq_len)
            all_ids.append(ids)
        return torch.stack(all_ids) if all_ids else torch.zeros(1, max_seq_len, dtype=torch.long)

    train_tensor = examples_to_tensor(train_examples)
    eval_tensor = examples_to_tensor(eval_examples)

    return train_tensor, eval_tensor, train_examples, eval_examples


def _evaluate(
    model: torch.nn.Module,
    eval_data: torch.Tensor,
    device: str,
) -> Dict[str, float]:
    """Run evaluation and return metrics."""
    model.eval()
    total_loss = 0.0
    n_batches = min(10, eval_data.shape[0])

    with torch.no_grad():
        for i in range(n_batches):
            batch = eval_data[i : i + 1].to(device)
            output = model(batch, labels=batch)
            total_loss += output["loss"].item()

    model.train()
    avg_loss = total_loss / max(n_batches, 1)
    return {"eval_loss": avg_loss}


def run_python_trainer(
    config_name: str = "debug",
    dataset_dir: Optional[str] = None,
    steps: Optional[int] = None,
    device: Optional[str] = None,
    output_dir: str = "artifacts/runtimecoder_python",
    resume: bool = False,
) -> Dict[str, Any]:
    """Run the Python RuntimeCoder trainer.

    Args:
        config_name: Config name ("debug", "mini", "micro").
        dataset_dir: Optional dataset directory (unused for now, uses curriculum).
        steps: Override max training steps.
        device: Device override ("cpu", "cuda").
        output_dir: Where to save checkpoints and logs.
        resume: Whether to resume from latest checkpoint.

    Returns:
        Training metrics dict.
    """
    config = get_config(config_name)
    model_cfg = config["model"]
    train_cfg = config["training"]

    # Override steps and device if provided
    max_steps = steps if steps is not None else train_cfg["max_steps"]
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")

    print(f"=" * 60)
    print(f"RuntimeCoder Python Trainer - {config['name']}")
    print(f"=" * 60)
    print(f"  Config: {config_name}")
    print(f"  Device: {device}")
    print(f"  Max steps: {max_steps}")

    # Build model
    micro_config = RuntimeCoderMicroConfig(
        vocab_size=model_cfg["vocab_size"],
        d_model=model_cfg["d_model"],
        n_layers=model_cfg["n_layers"],
        n_heads=model_cfg["n_heads"],
        d_ff=model_cfg["d_ff"],
        max_seq_len=model_cfg["max_seq_len"],
        dropout=model_cfg["dropout"],
    )
    model = build_micro_model(micro_config, device=device)
    param_info = count_parameters(model)
    print(f"  Parameters: {param_info['total']:,}")

    # Build dataset
    max_seq_len = config["data"]["max_seq_len"]
    vocab_size = model_cfg["vocab_size"]
    train_data, eval_data, train_exs, eval_exs = _build_dataset(config, max_seq_len, vocab_size)
    train_data = train_data.to(device)
    eval_data = eval_data.to(device)
    print(f"  Train examples: {len(train_exs)}")
    print(f"  Eval examples: {len(eval_exs)}")

    # Optimizer
    optimizer = optim.AdamW(
        model.parameters(),
        lr=train_cfg["lr"],
        weight_decay=train_cfg["weight_decay"],
    )

    # OOM-safe batcher
    batcher = OOMSafeBatcher(
        initial_batch_size=train_cfg["batch_size"],
        grad_accum_steps=train_cfg["grad_accum_steps"],
    )

    # Resume from checkpoint if requested
    start_step = 0
    if resume:
        latest = find_latest_checkpoint(output_dir)
        if latest:
            result = load_checkpoint(latest, model, optimizer, device=device)
            start_step = result["step"]
            print(f"  Resumed from step {start_step}")

    # Training loop
    os.makedirs(output_dir, exist_ok=True)
    model.train()
    metrics = {
        "config_name": config_name,
        "parameters": param_info["total"],
        "device": device,
        "max_steps": max_steps,
        "losses": [],
        "eval_losses": [],
        "timestamps": [],
    }

    start_time = time.time()

    for step in range(start_step, start_step + max_steps):
        batch = batcher.get_batch(train_data, step)
        result = batcher.try_step(model, batch, optimizer, step % batcher.grad_accum_steps)

        if result["success"]:
            metrics["losses"].append(result["loss"])
            metrics["timestamps"].append(time.time() - start_time)
        else:
            # OOM or failure - log and continue
            metrics["losses"].append(metrics["losses"][-1] if metrics["losses"] else 10.0)
            metrics["timestamps"].append(time.time() - start_time)

        # Logging
        if (step + 1) % train_cfg.get("log_every", 10) == 0:
            recent_loss = sum(metrics["losses"][-10:]) / min(10, len(metrics["losses"]))
            elapsed = time.time() - start_time
            print(f"    Step {step + 1}/{start_step + max_steps}: "
                  f"loss={recent_loss:.4f} elapsed={elapsed:.1f}s")

        # Evaluation
        if (step + 1) % train_cfg.get("eval_every", 50) == 0:
            eval_metrics = _evaluate(model, eval_data, device)
            metrics["eval_losses"].append(eval_metrics["eval_loss"])
            print(f"    Eval @ step {step + 1}: loss={eval_metrics['eval_loss']:.4f}")

        # Checkpointing
        if (step + 1) % train_cfg.get("save_every", 100) == 0:
            save_checkpoint(model, optimizer, step + 1, output_dir)

    # Final eval
    final_eval = _evaluate(model, eval_data, device)
    metrics["final_eval_loss"] = final_eval["eval_loss"]

    # Save final checkpoint
    save_checkpoint(model, optimizer, start_step + max_steps, output_dir)

    # Compute summary metrics
    metrics["loss_decreased"] = (
        len(metrics["losses"]) >= 2
        and metrics["losses"][-1] < metrics["losses"][0]
    )
    metrics["total_time_seconds"] = time.time() - start_time
    metrics["oom_stats"] = batcher.get_stats()
    metrics["final_loss"] = metrics["losses"][-1] if metrics["losses"] else None
    metrics["initial_loss"] = metrics["losses"][0] if metrics["losses"] else None

    # Save metrics
    metrics_path = os.path.join(output_dir, "training_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"\n  Metrics saved: {metrics_path}")
    print(f"  Final loss: {metrics['final_loss']:.4f}")
    print(f"  Loss decreased: {metrics['loss_decreased']}")
    print(f"  Total time: {metrics['total_time_seconds']:.1f}s")
    print(f"  OOM count: {metrics['oom_stats']['oom_count']}")

    return metrics
