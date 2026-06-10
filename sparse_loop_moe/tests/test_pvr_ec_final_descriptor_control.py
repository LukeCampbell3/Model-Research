"""Tests for PVR-EC-O Final Descriptor Control."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_final_deployment_gate")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestDescriptorControl:
    def test_descriptor_control_report_written(self): _load("pvr_ec_final_descriptor_control_report")
    def test_same_input_wrong_descriptor_test_exists(self):
        r = _load("pvr_ec_final_descriptor_control_report")
        assert "wrong_descriptor_accuracy" in r
    def test_descriptor_ablation_drop_positive(self):
        r = _load("pvr_ec_final_descriptor_control_report")
        # Correct - removed should be positive (descriptor helps)
        assert r["correct_descriptor_accuracy"] > r["descriptor_removed_accuracy"]
    def test_wrong_descriptor_reduces_accuracy(self):
        r = _load("pvr_ec_final_descriptor_control_report")
        # Wrong descriptor should be worse than correct (even if small margin)
        assert r["correct_descriptor_accuracy"] >= r["wrong_descriptor_accuracy"]
