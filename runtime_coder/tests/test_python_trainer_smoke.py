"""Smoke tests for the Python RuntimeCoder trainer."""

import os
import tempfile
import pytest
import torch

from runtime_coder.training.train_python_runtime_coder import run_python_trainer


class TestPythonTrainerSmoke:
    """Smoke tests: trainer runs and loss decreases."""

    @pytest.fixture
    def output_dir(self, tmp_path):
        return str(tmp_path / "trainer_smoke")

    def test_trainer_runs_10_steps(self, output_dir):
        """Trainer completes 10 steps without crashing."""
        metrics = run_python_trainer(
            config_name="debug",
            steps=10,
            device="cuda" if torch.cuda.is_available() else "cpu",
            output_dir=output_dir,
        )
        assert metrics is not None
        assert len(metrics["losses"]) == 10

    def test_loss_decreases(self, output_dir):
        """Loss decreases over training."""
        metrics = run_python_trainer(
            config_name="debug",
            steps=10,
            device="cuda" if torch.cuda.is_available() else "cpu",
            output_dir=output_dir,
        )
        # Compare first few losses vs last few
        first_3 = sum(metrics["losses"][:3]) / 3
        last_3 = sum(metrics["losses"][-3:]) / 3
        assert last_3 < first_3, (
            f"Loss did not decrease: first_3={first_3:.4f}, last_3={last_3:.4f}"
        )

    def test_metrics_file_created(self, output_dir):
        """Training metrics JSON is saved."""
        run_python_trainer(
            config_name="debug",
            steps=10,
            device="cuda" if torch.cuda.is_available() else "cpu",
            output_dir=output_dir,
        )
        assert os.path.exists(os.path.join(output_dir, "training_metrics.json"))

    def test_checkpoint_saved(self, output_dir):
        """Checkpoint file is created."""
        run_python_trainer(
            config_name="debug",
            steps=10,
            device="cuda" if torch.cuda.is_available() else "cpu",
            output_dir=output_dir,
        )
        # Check for checkpoint file
        files = os.listdir(output_dir)
        checkpoint_files = [f for f in files if f.startswith("checkpoint_")]
        assert len(checkpoint_files) > 0
