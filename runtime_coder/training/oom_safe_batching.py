"""OOM-safe batching for GPU training.

OOMSafeBatcher catches CUDA OOM errors, halves the effective batch size,
increases gradient accumulation steps to compensate, and retries.
"""

import torch
from typing import Optional, Dict, Any


class OOMSafeBatcher:
    """Handles CUDA OOM by reducing batch size and increasing grad accumulation.

    Usage:
        batcher = OOMSafeBatcher(initial_batch_size=16, grad_accum_steps=1)
        for step in range(max_steps):
            batch = batcher.get_batch(dataset)
            success = batcher.try_step(model, batch, optimizer)
            if not success:
                continue  # batch was halved, retry on next iteration
    """

    def __init__(
        self,
        initial_batch_size: int = 16,
        grad_accum_steps: int = 1,
        min_batch_size: int = 1,
        max_retries: int = 3,
    ):
        self.batch_size = initial_batch_size
        self.grad_accum_steps = grad_accum_steps
        self.min_batch_size = min_batch_size
        self.max_retries = max_retries
        self.oom_count = 0
        self.total_steps = 0
        self.successful_steps = 0
        self._effective_batch_size = initial_batch_size * grad_accum_steps

    @property
    def effective_batch_size(self) -> int:
        """Total effective batch size (batch_size * grad_accum_steps)."""
        return self.batch_size * self.grad_accum_steps

    def get_batch(self, dataset: torch.Tensor, step: int = 0) -> torch.Tensor:
        """Sample a batch from the dataset.

        Args:
            dataset: Full dataset tensor [N, seq_len].
            step: Current step (for deterministic sampling).

        Returns:
            Batch tensor [batch_size, seq_len].
        """
        n = dataset.shape[0]
        indices = torch.randint(0, n, (self.batch_size,))
        return dataset[indices]

    def try_step(
        self,
        model: torch.nn.Module,
        batch: torch.Tensor,
        optimizer: torch.optim.Optimizer,
        accumulation_step: int = 0,
    ) -> Dict[str, Any]:
        """Try a forward/backward step, handling OOM.

        Args:
            model: The model to train.
            batch: Input batch tensor.
            optimizer: The optimizer.
            accumulation_step: Current accumulation step (0-indexed).

        Returns:
            Dict with 'success', 'loss', and optionally 'oom_recovered'.
        """
        self.total_steps += 1

        for retry in range(self.max_retries):
            try:
                # Forward pass
                output = model(batch, labels=batch)
                loss = output["loss"] / self.grad_accum_steps

                # Backward pass
                loss.backward()

                # Only step optimizer on last accumulation step
                if (accumulation_step + 1) % self.grad_accum_steps == 0:
                    optimizer.step()
                    optimizer.zero_grad()

                self.successful_steps += 1
                return {
                    "success": True,
                    "loss": loss.item() * self.grad_accum_steps,
                    "batch_size": self.batch_size,
                    "grad_accum_steps": self.grad_accum_steps,
                }

            except RuntimeError as e:
                if "out of memory" in str(e).lower() or "CUDA" in str(e):
                    self.oom_count += 1
                    self._handle_oom()

                    # Clear memory
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()

                    # Re-slice batch to new size
                    batch = batch[: self.batch_size]

                    if retry < self.max_retries - 1:
                        continue
                    else:
                        return {
                            "success": False,
                            "loss": None,
                            "oom_recovered": False,
                            "error": str(e),
                        }
                else:
                    raise

        return {"success": False, "loss": None, "oom_recovered": False}

    def _handle_oom(self):
        """Handle OOM by halving batch size and doubling grad accum."""
        old_batch = self.batch_size
        new_batch = max(self.min_batch_size, self.batch_size // 2)

        if new_batch < old_batch:
            # Increase grad_accum to maintain effective batch size
            self.grad_accum_steps *= 2
            self.batch_size = new_batch

    def get_stats(self) -> Dict[str, Any]:
        """Get batching statistics."""
        return {
            "current_batch_size": self.batch_size,
            "current_grad_accum_steps": self.grad_accum_steps,
            "effective_batch_size": self.effective_batch_size,
            "oom_count": self.oom_count,
            "total_steps": self.total_steps,
            "successful_steps": self.successful_steps,
            "success_rate": (
                self.successful_steps / max(1, self.total_steps)
            ),
        }
