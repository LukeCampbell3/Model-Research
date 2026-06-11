"""Test TinyRuntimeCoder forward pass smoke tests."""

import pytest
import torch

from runtime_coder.model.config import TinyRuntimeCoderConfig
from runtime_coder.model.tiny_runtime_coder import TinyRuntimeCoder


class TestModelForward:
    """Smoke tests for TinyRuntimeCoder forward pass."""

    @pytest.fixture
    def model(self):
        config = TinyRuntimeCoderConfig()
        model = TinyRuntimeCoder(config)
        model.eval()
        return model

    @pytest.fixture
    def config(self):
        return TinyRuntimeCoderConfig()

    def test_forward_returns_logits(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (1, 16))
        with torch.no_grad():
            output = model(input_ids)
        assert "logits" in output
        assert output["logits"].shape == (1, 16, config.vocab_size)

    def test_forward_returns_purity_counters(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (1, 16))
        with torch.no_grad():
            output = model(input_ids)
        assert "purity_counters" in output
        assert isinstance(output["purity_counters"], dict)

    def test_forward_with_labels_returns_loss(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (1, 16))
        labels = torch.randint(0, config.vocab_size, (1, 16))
        with torch.no_grad():
            output = model(input_ids, labels=labels)
        assert "loss" in output
        assert output["loss"].dim() == 0  # scalar
        assert output["loss"].item() > 0

    def test_forward_batch_size(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (4, 32))
        with torch.no_grad():
            output = model(input_ids)
        assert output["logits"].shape == (4, 32, config.vocab_size)

    def test_forward_different_seq_lengths(self, model, config):
        for seq_len in [1, 8, 64, 128]:
            input_ids = torch.randint(0, config.vocab_size, (1, seq_len))
            with torch.no_grad():
                output = model(input_ids)
            assert output["logits"].shape == (1, seq_len, config.vocab_size)

    def test_model_has_parameters(self, model):
        assert model.num_parameters() > 0

    def test_logits_dtype_float(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        assert output["logits"].dtype == torch.float32

    def test_no_loss_without_labels(self, model, config):
        input_ids = torch.randint(0, config.vocab_size, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        assert "loss" not in output
