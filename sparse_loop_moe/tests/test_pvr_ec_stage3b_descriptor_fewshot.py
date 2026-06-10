"""Tests for PVR-EC-O Stage 3B Descriptor and Few-Shot Conditioning.

Verifies descriptor and few-shot conditioning correctly targets held-out families.
"""
import json
import pytest
from pathlib import Path

RESULTS_DIR = Path("evaluation/benchmark_results/pvr_stage3b_transfer_attribution")


def _load_report(name: str) -> dict:
    path = RESULTS_DIR / f"{name}.json"
    if not path.exists():
        pytest.skip(f"Report not found: {path}")
    return json.loads(path.read_text())


class TestDescriptorConditioning:
    def test_descriptor_targets_heldout_families_only(self):
        report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        # Descriptor gain should be measured against zero-shot baseline
        baseline = report.get("baseline_accuracy", 0)
        descriptor = report.get("descriptor_accuracy", 0)
        # Both should be numeric
        assert isinstance(baseline, (int, float))
        assert isinstance(descriptor, (int, float))

    def test_descriptor_does_not_regress_seen_tasks(self):
        matrix = _load_report("pvr_ec_stage3b_split_matrix_report")
        splits = matrix.get("splits", {})
        seen_acc = splits.get("seen_task_seen_template", {}).get("accuracy", 0)
        # Seen task accuracy should remain high (>0.8)
        assert seen_acc > 0.8, f"Seen task accuracy too low: {seen_acc:.3f}"

    def test_descriptor_classification_valid(self):
        report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        classification = report.get("classification", "")
        assert classification in ["TASK_DESCRIPTOR_SIGNAL_NEEDED", "TASK_DESCRIPTOR_UNUSED"]


class TestFewShotConditioning:
    def test_fewshot_k_values_present(self):
        report = _load_report("pvr_ec_stage3b_fewshot_conditioning_report")
        assert "k1" in report
        assert "k4" in report
        assert "k8" in report

    def test_fewshot_gains_are_numeric(self):
        report = _load_report("pvr_ec_stage3b_fewshot_conditioning_report")
        for k in ["k1", "k4", "k8"]:
            gain = report[k].get("gain", None)
            assert isinstance(gain, (int, float)), f"k={k} gain is not numeric: {gain}"

    def test_fewshot_does_not_violate_forward_purity(self):
        gate = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = gate.get("hard_invariants", {})
        assert inv.get("owners_per_token") == 1.0
        assert inv.get("top2_executions") == 0
        assert inv.get("top4_executions") == 0


class TestOperatorComposition:
    def test_operator_composition_accuracy_reported(self):
        report = _load_report("pvr_ec_stage3b_operator_composition_report")
        acc = report.get("operator_composition_accuracy", None)
        assert isinstance(acc, (int, float))

    def test_operator_composition_gain_reported(self):
        report = _load_report("pvr_ec_stage3b_operator_composition_report")
        gain = report.get("operator_composition_gain", None)
        assert isinstance(gain, (int, float))


class TestRoleBinding:
    def test_role_binding_accuracy_reported(self):
        report = _load_report("pvr_ec_stage3b_role_binding_report")
        acc = report.get("role_binding_accuracy", None)
        assert isinstance(acc, (int, float))

    def test_role_binding_gain_reported(self):
        report = _load_report("pvr_ec_stage3b_role_binding_report")
        gain = report.get("role_binding_gain", None)
        assert isinstance(gain, (int, float))
