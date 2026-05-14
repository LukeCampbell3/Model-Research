"""Training loop for Sparse Loop-MoE experiments.

Supports staged training across all phases and model configurations.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

from sparse_loop_moe.core.cognitive_state import CognitiveState
from sparse_loop_moe.core.types import LoopStats
from sparse_loop_moe.training.losses import CombinedLoss, LossWeights
from sparse_loop_moe.training.data_generation import TaskSample, SyntheticTaskGenerator


@dataclass
class TrainerConfig:
    """Training configuration."""

    # Optimization
    learning_rate: float = 3e-4
    weight_decay: float = 0.01
    max_grad_norm: float = 1.0
    warmup_steps: int = 100
    max_steps: int = 10000
    batch_size: int = 32

    # Logging
    log_interval: int = 50
    eval_interval: int = 500
    save_interval: int = 1000

    # Loss weights
    loss_weights: LossWeights = field(default_factory=LossWeights)

    # Device
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


class SyntheticDataset(Dataset):
    """Dataset wrapper for synthetic task samples."""

    def __init__(self, samples: list[TaskSample]):
        self.samples = samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor | dict]:
        sample = self.samples[idx]
        return {
            "input_ids": sample.input_ids,
            "target_ids": sample.target_ids,
            "metadata": sample.metadata,
        }


def collate_fn(batch: list[dict]) -> dict[str, Any]:
    """Collate function for DataLoader."""
    input_ids = torch.stack([item["input_ids"] for item in batch])
    target_ids = torch.stack([item["target_ids"] for item in batch])
    metadata = [item["metadata"] for item in batch]
    return {
        "input_ids": input_ids,
        "target_ids": target_ids,
        "metadata": metadata,
    }


class Trainer:
    """Training loop for Sparse Loop-MoE models.

    Handles:
    - Staged training across phases
    - Combined loss computation
    - Metric tracking
    - Gradient clipping
    - Learning rate scheduling
    """

    def __init__(
        self,
        model: nn.Module,
        config: TrainerConfig | None = None,
        task_generator: SyntheticTaskGenerator | None = None,
    ):
        self.model = model
        self.config = config or TrainerConfig()
        self.task_generator = task_generator or SyntheticTaskGenerator()
        self.loss_fn = CombinedLoss(self.config.loss_weights)

        # Move model to device
        self.device = torch.device(self.config.device)
        self.model = self.model.to(self.device)

        # Optimizer
        self.optimizer = optim.AdamW(
            self.model.parameters(),
            lr=self.config.learning_rate,
            weight_decay=self.config.weight_decay,
        )

        # LR scheduler with warmup
        self.scheduler = optim.lr_scheduler.OneCycleLR(
            self.optimizer,
            max_lr=self.config.learning_rate,
            total_steps=self.config.max_steps,
            pct_start=self.config.warmup_steps / self.config.max_steps,
        )

        # Metrics
        self.step = 0
        self.metrics_history: list[dict[str, float]] = []

    def train_step(self, batch: dict[str, Any]) -> dict[str, float]:
        """Execute a single training step.

        Returns dictionary of metrics for this step.
        """
        self.model.train()
        self.optimizer.zero_grad()

        input_ids = batch["input_ids"].to(self.device)
        target_ids = batch["target_ids"].to(self.device)

        # Forward pass
        output = self.model(input_ids=input_ids, targets=target_ids)

        # Get task loss
        task_loss = output["loss"]

        # Get auxiliary losses
        aux_losses = output.get("aux_losses", {})
        loop_stats = output.get("loop_stats", [])

        # Compute combined loss
        total_loss, loss_components = self.loss_fn(
            task_loss=task_loss,
            aux_losses=aux_losses,
            loop_stats=loop_stats if isinstance(loop_stats, list) else [],
        )

        # Backward pass
        total_loss.backward()

        # Gradient clipping
        grad_norm = nn.utils.clip_grad_norm_(
            self.model.parameters(), self.config.max_grad_norm
        )

        # Optimizer step
        self.optimizer.step()
        self.scheduler.step()

        self.step += 1

        # Collect metrics
        metrics = {
            "step": self.step,
            "total_loss": total_loss.item(),
            "task_loss": task_loss.item(),
            "grad_norm": grad_norm.item() if isinstance(grad_norm, torch.Tensor) else grad_norm,
            "lr": self.scheduler.get_last_lr()[0],
        }

        # Add loss components
        for key, val in loss_components.items():
            if key != "total_loss" and isinstance(val, torch.Tensor):
                metrics[f"loss/{key}"] = val.item()

        # Add loop metrics if available
        if loop_stats and isinstance(loop_stats, list) and len(loop_stats) > 0:
            total_loops = sum(
                s.loops_used for s in loop_stats if isinstance(s, LoopStats)
            )
            metrics["loops/total"] = total_loops
            metrics["loops/avg_per_block"] = total_loops / max(len(loop_stats), 1)

            halt_count = sum(
                1 for s in loop_stats
                if isinstance(s, LoopStats) and s.halted_early
            )
            metrics["loops/halt_rate"] = halt_count / max(len(loop_stats), 1)

        self.metrics_history.append(metrics)
        return metrics

    def evaluate(
        self, eval_samples: list[TaskSample], max_samples: int = 256
    ) -> dict[str, float]:
        """Evaluate model on a set of samples.

        Returns dictionary of evaluation metrics.
        """
        self.model.eval()
        eval_samples = eval_samples[:max_samples]

        total_loss = 0.0
        total_correct = 0
        total_tokens = 0
        total_loops = 0
        total_experts = 0
        num_batches = 0

        with torch.no_grad():
            for i in range(0, len(eval_samples), self.config.batch_size):
                batch_samples = eval_samples[i: i + self.config.batch_size]
                input_ids = torch.stack([s.input_ids for s in batch_samples]).to(
                    self.device
                )
                target_ids = torch.stack([s.target_ids for s in batch_samples]).to(
                    self.device
                )

                output = self.model(input_ids=input_ids, targets=target_ids)

                total_loss += output["loss"].item()

                # Accuracy (non-padding tokens)
                logits = output["logits"]
                preds = logits.argmax(dim=-1)
                mask = target_ids != 0  # Non-padding
                correct = (preds == target_ids) & mask
                total_correct += correct.sum().item()
                total_tokens += mask.sum().item()

                # Loop stats
                loop_stats = output.get("loop_stats", [])
                if loop_stats and isinstance(loop_stats[0], LoopStats):
                    total_loops += sum(s.loops_used for s in loop_stats)
                    for s in loop_stats:
                        total_experts += sum(s.experts_used_per_loop)

                num_batches += 1

        accuracy = total_correct / max(total_tokens, 1)
        avg_loss = total_loss / max(num_batches, 1)
        avg_loops = total_loops / max(num_batches * len(self.model.blocks) if hasattr(self.model, 'blocks') else 1, 1)

        return {
            "eval/loss": avg_loss,
            "eval/accuracy": accuracy,
            "eval/avg_loops": avg_loops,
            "eval/total_experts": total_experts,
        }

    def train(
        self,
        num_steps: int | None = None,
        eval_samples: list[TaskSample] | None = None,
    ) -> list[dict[str, float]]:
        """Run training loop.

        Args:
            num_steps: Number of steps (defaults to config.max_steps)
            eval_samples: Optional evaluation samples

        Returns:
            List of metric dictionaries
        """
        steps = num_steps or self.config.max_steps
        all_metrics = []

        for step_idx in range(steps):
            # Generate batch
            batch_samples = self.task_generator.generate_batch(
                batch_size=self.config.batch_size
            )
            input_ids = torch.stack([s.input_ids for s in batch_samples])
            target_ids = torch.stack([s.target_ids for s in batch_samples])
            batch = {
                "input_ids": input_ids,
                "target_ids": target_ids,
                "metadata": [s.metadata for s in batch_samples],
            }

            # Train step
            metrics = self.train_step(batch)
            all_metrics.append(metrics)

            # Logging
            if self.step % self.config.log_interval == 0:
                self._log_metrics(metrics)

            # Evaluation
            if eval_samples and self.step % self.config.eval_interval == 0:
                eval_metrics = self.evaluate(eval_samples)
                all_metrics.append(eval_metrics)
                self._log_metrics(eval_metrics, prefix="EVAL")

        return all_metrics

    def _log_metrics(self, metrics: dict[str, float], prefix: str = "TRAIN") -> None:
        """Log metrics to console."""
        parts = [f"[{prefix}] step={self.step}"]
        for key, val in metrics.items():
            if key == "step":
                continue
            if isinstance(val, float):
                parts.append(f"{key}={val:.4f}")
        print(" | ".join(parts))
