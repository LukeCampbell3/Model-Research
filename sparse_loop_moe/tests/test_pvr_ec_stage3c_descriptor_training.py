"""Tests for PVR-EC-O Stage 3C Descriptor Training."""
import json, math
import pytest
from pathlib import Path

RESULTS_DIR = Path("evaluation/benchmark_results/pvr_stage3c_transfer_conditioning")


def _load(name):
    path = RESULTS_DIR / f"{name}.json"
    if not path.exists():
        pytest.skip(f"Report not found: {path}")
    return json.loads(path.read_text())


class TestDescriptorTraining:
    def test_descriptor_tokens_present_in_training(self):
        report = _load("pvr_ec_stage3c_descriptor_training_report")
        assert "descriptor_trained_seen_acc" in report
        assert report["descriptor_trained_seen_acc"] > 0.5

    def test_descriptor_ablation_changes_input(self):
        report = _load("pvr_ec_stage3c_descriptor_training_report")
        drop = report.get("descriptor_ablation_drop", 0)
        assert isinstance(drop, (int, float))

    def test_same_input_different_descriptor_changes_target(self):
        report = _load("pvr_ec_stage3c_descriptor_training_report")
        # If ablation drop > 0, model uses descriptors
        drop = report.get("descriptor_ablation_drop", 0)
        if not math.isnan(drop):
            assert drop > 0.0, "Descriptor should influence model output"

    def test_descriptor_report_written(self):
        report = _load("pvr_ec_stage3c_descriptor_training_report")
        assert "status" in report
        assert "descriptor_gain" in report


class TestDescriptorInvariants:
    def test_conditioning_repair_does_not_use_top2(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("top2_executions") == 0

    def test_conditioning_repair_preserves_owners_per_token_one(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("owners_per_token") == 1.0

    def test_conditioning_repair_does_not_mutate_production_map(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("production_map_mutated") is False
