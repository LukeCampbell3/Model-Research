"""Tests for OOM-safe batching."""

import pytest
import torch
import torch.nn as nn

from runtime_coder.training.oom_safe_batching import OOMSafeBatcher


class FakeOOMModel(nn.Module):
    """A model that raises OOM on first N calls then succeeds."""

    def __init__(self, fail_count=2):
        super().__init__()
        self.linear = nn.Linear(32, 32)
        self.call_count = 0
        self.fail_count = fail_count

    def forward(self, x, labels=None):
        self.call_count += 1
        if self.call_count <= self.fail_count:
            raise RuntimeError("CUDA out of memory. Tried to allocate 2.00 GiB")
        logits = self.linear(x.float()[:, :32])
        loss = logits.mean()
        return {"loss": loss, "logits": logits}


class SimpleModel(nn.Module):
    """A simple model that always works."""

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(32, 32)

    def forward(self, x, labels=None):
        logits = self.linear(x.float()[:, :32])
        loss = logits.mean()
        return {"loss": loss, "logits": logits}


class TestOOMSafeBatcher:
    """Tests for OOM recovery behavior."""

    def test_normal_step_succeeds(self):
        """Normal step without OOM succeeds."""
        model = SimpleModel()
        optimizer = torch.optim.Adam(model.parameters())
        batcher = OOMSafeBatcher(initial_batch_size=4)

        batch = torch.randint(0, 100, (4, 32))
        result = batcher.try_step(model, batch, optimizer)
        assert result["success"]
        assert result["loss"] is not None

    def test_oom_halves_batch_size(self):
        """OOM triggers batch size reduction."""
        model = FakeOOMModel(fail_count=1)
        optimizer = torch.optim.Adam(model.parameters())
        batcher = OOMSafeBatcher(initial_batch_size=8)

        batch = torch.randint(0, 100, (8, 32))
        result = batcher.try_step(model, batch, optimizer)

        # Should have reduced batch size
        assert batcher.batch_size < 8

    def test_oom_increases_grad_accum(self):
        """OOM increases gradient accumulation."""
        model = FakeOOMModel(fail_count=1)
        optimizer = torch.optim.Adam(model.parameters())
        batcher = OOMSafeBatcher(initial_batch_size=8, grad_accum_steps=1)

        batch = torch.randint(0, 100, (8, 32))
        batcher.try_step(model, batch, optimizer)

        assert batcher.grad_accum_steps > 1

    def test_oom_recovery_succeeds(self):
        """After OOM recovery, next step succeeds."""
        model = FakeOOMModel(fail_count=1)  # Fail once then succeed
        optimizer = torch.optim.Adam(model.parameters())
        batcher = OOMSafeBatcher(initial_batch_size=8, max_retries=3)

        batch = torch.randint(0, 100, (8, 32))
        result = batcher.try_step(model, batch, optimizer)

        # After retry with smaller batch, should succeed
        assert result["success"]

    def test_min_batch_size_respected(self):
        """Batch size doesn't go below minimum."""
        batcher = OOMSafeBatcher(initial_batch_size=2, min_batch_size=1)
        batcher._handle_oom()
        assert batcher.batch_size >= 1

    def test_stats_tracking(self):
        """OOM stats are properly tracked."""
        model = SimpleModel()
        optimizer = torch.optim.Adam(model.parameters())
        batcher = OOMSafeBatcher(initial_batch_size=4)

        batch = torch.randint(0, 100, (4, 32))
        batcher.try_step(model, batch, optimizer)

        stats = batcher.get_stats()
        assert stats["total_steps"] == 1
        assert stats["successful_steps"] == 1
        assert stats["oom_count"] == 0

    def test_get_batch_from_dataset(self):
        """get_batch returns correct size from dataset."""
        batcher = OOMSafeBatcher(initial_batch_size=4)
        dataset = torch.randint(0, 100, (20, 64))
        batch = batcher.get_batch(dataset)
        assert batch.shape[0] == 4
        assert batch.shape[1] == 64
