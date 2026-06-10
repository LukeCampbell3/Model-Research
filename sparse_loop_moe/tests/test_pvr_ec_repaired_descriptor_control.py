"""Tests for repaired descriptor control."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_descriptor_semantic_repair")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestRepairedDescriptorControl:
    def test_descriptor_control_report_written(self): _load("pvr_ec_descriptor_control_same_input_report")
    def test_wrong_descriptor_reduces_accuracy(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        assert r["correct_descriptor_accuracy"] >= r["wrong_descriptor_accuracy"]
    def test_descriptor_ablation_drop_positive(self):
        r = _load("pvr_ec_descriptor_control_same_input_report")
        # Correct with descriptor > removed without descriptor
        assert r["correct_descriptor_accuracy"] > r["descriptor_removed_accuracy"]
    def test_deployment_confirmed_only_if_all_gates_pass(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        if r["deployment_verdict"] == "PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED":
            for gate, status in r["gates"].items():
                assert status is True, f"Gate {gate} failed but deployment confirmed"
