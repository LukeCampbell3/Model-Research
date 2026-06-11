"""Tests for checkpoint save/load round-trip."""

import os
import pytest
import torch
import torch.nn as nn

from runtime_coder.training.checkpointing import (
    save_checkpoint,
    load_checkpoint,
    find_latest_checkpoint,
)


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(32, 16)
        self.out = nn.Linear(16, 8)

    def forward(self, x):
        return self.out(torch.relu(self.linear(x)))


class TestCheckpointResume:
    """Tests for checkpoint save/load functionality."""

    @pytest.fixture
    def model_and_optimizer(self):
        model = SimpleModel()
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
        return model, optimizer

    def test_save_creates_file(self, tmp_path, model_and_optimizer):
        """Save creates a checkpoint file."""
        model, optimizer = model_and_optimizer
        path = save_checkpoint(model, optimizer, step=10, path=str(tmp_path))
        assert os.path.exists(path)

    def test_load_restores_state(self, tmp_path, model_and_optimizer):
        """Load restores model and optimizer state."""
        model, optimizer = model_and_optimizer

        # Run a forward/backward to modify state
        x = torch.randn(2, 32)
        loss = model(x).sum()
        loss.backward()
        optimizer.step()

        # Save
        path = save_checkpoint(model, optimizer, step=5, path=str(tmp_path))

        # Create fresh model
        model2 = SimpleModel()
        optimizer2 = torch.optim.Adam(model2.parameters(), lr=1e-3)

        # Load
        result = load_checkpoint(path, model2, optimizer2)
        assert result["step"] == 5

        # Verify weights match
        for p1, p2 in zip(model.parameters(), model2.parameters()):
            assert torch.allclose(p1, p2)

    def test_extra_state_saved(self, tmp_path, model_and_optimizer):
        """Extra state is preserved through save/load."""
        model, optimizer = model_and_optimizer
        extra = {"loss": 0.5, "eval_metric": 0.8}

        path = save_checkpoint(model, optimizer, step=3, path=str(tmp_path), extra_state=extra)

        model2 = SimpleModel()
        result = load_checkpoint(path, model2)
        assert result["extra_state"]["loss"] == 0.5
        assert result["extra_state"]["eval_metric"] == 0.8

    def test_find_latest_checkpoint(self, tmp_path, model_and_optimizer):
        """find_latest_checkpoint returns highest step."""
        model, optimizer = model_and_optimizer

        save_checkpoint(model, optimizer, step=5, path=str(tmp_path))
        save_checkpoint(model, optimizer, step=10, path=str(tmp_path))
        save_checkpoint(model, optimizer, step=15, path=str(tmp_path))

        latest = find_latest_checkpoint(str(tmp_path))
        assert latest is not None
        assert "step_15" in latest

    def test_find_latest_returns_none_for_empty_dir(self, tmp_path):
        """find_latest_checkpoint returns None for empty directory."""
        result = find_latest_checkpoint(str(tmp_path))
        assert result is None

    def test_load_missing_file_raises(self, model_and_optimizer):
        """Loading non-existent checkpoint raises FileNotFoundError."""
        model, _ = model_and_optimizer
        with pytest.raises(FileNotFoundError):
            load_checkpoint("/nonexistent/path.pt", model)

    def test_round_trip_preserves_step(self, tmp_path, model_and_optimizer):
        """Step number survives save/load round-trip."""
        model, optimizer = model_and_optimizer
        path = save_checkpoint(model, optimizer, step=42, path=str(tmp_path))

        model2 = SimpleModel()
        result = load_checkpoint(path, model2)
        assert result["step"] == 42
