"""Test purity counters from the model forward pass."""

import pytest
import torch

from runtime_coder.model.config import TinyRuntimeCoderConfig
from runtime_coder.model.tiny_runtime_coder import TinyRuntimeCoder


class TestPurityCounters:
    """Test that purity counters are present and correctly initialized."""

    @pytest.fixture
    def model(self):
        config = TinyRuntimeCoderConfig()
        model = TinyRuntimeCoder(config)
        model.eval()
        return model

    def test_purity_counters_in_output(self, model):
        input_ids = torch.randint(0, 1000, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        assert "purity_counters" in output

    def test_purity_counters_all_zeros(self, model):
        """At Phase 0, all purity counters should be zero."""
        input_ids = torch.randint(0, 1000, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        counters = output["purity_counters"]
        for key, value in counters.items():
            assert value == 0 or value == 0.0, (
                f"Counter '{key}' should be 0 at Phase 0, got {value}"
            )

    def test_purity_counters_expected_keys(self, model):
        input_ids = torch.randint(0, 1000, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        counters = output["purity_counters"]
        expected_keys = {
            "top1_correct",
            "top2_correct",
            "top4_correct",
            "top8_correct",
            "total_predictions",
            "runtime_violations",
            "branch_compliance",
            "verifier_pass_rate",
        }
        assert set(counters.keys()) == expected_keys

    def test_purity_counters_are_numeric(self, model):
        input_ids = torch.randint(0, 1000, (1, 8))
        with torch.no_grad():
            output = model(input_ids)
        counters = output["purity_counters"]
        for key, value in counters.items():
            assert isinstance(value, (int, float)), (
                f"Counter '{key}' should be numeric, got {type(value)}"
            )

    def test_purity_counters_stable_across_calls(self, model):
        """Multiple forward calls should return same counters at Phase 0."""
        input_ids_1 = torch.randint(0, 1000, (1, 8))
        input_ids_2 = torch.randint(0, 1000, (2, 16))
        with torch.no_grad():
            out1 = model(input_ids_1)
            out2 = model(input_ids_2)
        assert out1["purity_counters"] == out2["purity_counters"]

    def test_purity_property_is_dict(self, model):
        """The purity_counters property should return a dict."""
        assert isinstance(model.purity_counters, dict)
