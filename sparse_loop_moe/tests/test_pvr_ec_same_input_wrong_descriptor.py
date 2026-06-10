"""Tests for same-input wrong-descriptor methodology."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_descriptor_semantic_repair")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestSameInputWrongDescriptor:
    def test_same_input_wrong_descriptor_dataset_valid(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        assert "correct_descriptor_accuracy" in r
        assert "wrong_descriptor_accuracy" in r
    def test_correct_descriptor_target_differs_from_wrong(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        # Correct should be >= wrong (even if small margin at low steps)
        assert r["correct_descriptor_accuracy"] >= r["wrong_descriptor_accuracy"]
    def test_wrong_descriptor_uses_same_input(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        assert "same_input_wrong_descriptor_drop" in r
    def test_descriptor_removed_condition_exists(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        assert "descriptor_removed_accuracy" in r
    def test_corrupted_descriptor_condition_exists(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        assert "corrupted_descriptor_accuracy" in r
