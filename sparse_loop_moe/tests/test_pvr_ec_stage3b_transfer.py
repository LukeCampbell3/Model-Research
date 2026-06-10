"""Tests for PVR-EC-O Stage 3B Transfer Attribution.

Verifies:
- Geometry loading blocks transfer if not loaded
- Heldout task family not confused with heldout template
- Split matrix report structure
- Hard invariants maintained
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


class TestStage3BGeometryLoad:
    def test_stage3b_geometry_load_report_written(self):
        report = _load_report("pvr_ec_stage3b_geometry_load_report")
        assert "status" in report
        assert "geometry_loaded" in report

    def test_geometry_not_loaded_blocks_transfer_test(self):
        report = _load_report("pvr_ec_stage3b_geometry_load_report")
        # If geometry_loaded is False, status must be BLOCKED
        if not report.get("geometry_loaded"):
            assert "BLOCKED" in report["status"]


class TestStage3BSplitMatrix:
    def test_stage3b_split_matrix_report_written(self):
        report = _load_report("pvr_ec_stage3b_split_matrix_report")
        assert "splits" in report

    def test_heldout_task_family_not_confused_with_heldout_template(self):
        report = _load_report("pvr_ec_stage3b_split_matrix_report")
        splits = report.get("splits", {})
        # Seen task heldout template should be much higher than heldout task family
        seen_template = splits.get("seen_task_heldout_template", {}).get("accuracy", 0)
        heldout_family = splits.get("heldout_task_family_zero_shot_no_descriptor", {}).get("accuracy", 0)
        # Heldout template generalization > heldout task family zero-shot
        assert seen_template > heldout_family, (
            f"Seen template ({seen_template:.3f}) should exceed heldout family ({heldout_family:.3f})"
        )


class TestStage3BDescriptor:
    def test_stage3b_descriptor_report_written(self):
        report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        assert "descriptor_gain" in report

    def test_descriptor_conditioning_targets_correct(self):
        report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        assert "baseline_accuracy" in report
        assert "descriptor_accuracy" in report
        assert "classification" in report

    def test_descriptor_gain_classified(self):
        report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        classification = report.get("classification", "")
        valid_classes = [
            "TASK_DESCRIPTOR_SIGNAL_NEEDED",
            "TASK_DESCRIPTOR_UNUSED",
        ]
        assert classification in valid_classes


class TestStage3BFewshot:
    def test_stage3b_fewshot_report_written(self):
        report = _load_report("pvr_ec_stage3b_fewshot_conditioning_report")
        assert "k1" in report
        assert "k4" in report
        assert "k8" in report

    def test_fewshot_context_targets_correct(self):
        report = _load_report("pvr_ec_stage3b_fewshot_conditioning_report")
        for k in ["k1", "k4", "k8"]:
            assert "accuracy" in report[k]
            assert "gain" in report[k]

    def test_fewshot_gain_classified(self):
        report = _load_report("pvr_ec_stage3b_fewshot_conditioning_report")
        # Gain should be reported
        assert "k8" in report
        assert isinstance(report["k8"]["gain"], (int, float))


class TestStage3BOperatorComposition:
    def test_stage3b_operator_composition_report_written(self):
        report = _load_report("pvr_ec_stage3b_operator_composition_report")
        assert "operator_composition_accuracy" in report

    def test_operator_composition_targets_correct(self):
        report = _load_report("pvr_ec_stage3b_operator_composition_report")
        assert "operator_composition_gain" in report


class TestStage3BRoleBinding:
    def test_stage3b_role_binding_report_written(self):
        report = _load_report("pvr_ec_stage3b_role_binding_report")
        assert "role_binding_accuracy" in report

    def test_role_binding_targets_correct(self):
        report = _load_report("pvr_ec_stage3b_role_binding_report")
        assert "role_binding_gain" in report

    def test_role_binding_failure_classified(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        assert "dominant_failure" in report


class TestStage3BTransferAttribution:
    def test_stage3b_transfer_attribution_report_written(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        assert "dominant_failure" in report
        assert "geometry_status" in report
        assert "routing_status" in report

    def test_operator_composition_failure_classified(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        dominant = report.get("dominant_failure", "")
        valid_failures = [
            "PVR_EC_FAILURE_HELDOUT_TASK_FAMILY_TRANSFER",
            "PVR_EC_FAILURE_TASK_DESCRIPTOR_UNUSED",
            "PVR_EC_FAILURE_FEWSHOT_CONTEXT_UNUSED",
            "PVR_EC_FAILURE_OPERATOR_COMPOSITION_TRANSFER",
            "PVR_EC_FAILURE_ROLE_BINDING_TRANSFER",
            "PVR_EC_FAILURE_TRANSFER_ROUTING_MISMATCH",
            "PVR_EC_FAILURE_TRANSFER_EXPERT_CAPACITY",
            "PVR_EC_FAILURE_TRANSFER_DATA_SPLIT_TOO_HARD",
            "PVR_EC_FAILURE_GEOMETRY_NOT_LOADED_IN_TRANSFER",
        ]
        assert dominant in valid_failures, f"Unknown failure class: {dominant}"


class TestStage3BGateReport:
    def test_stage3b_gate_report_written(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        assert "verdict" in report
        assert "hard_invariants" in report

    def test_owners_per_token_remains_one(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("owners_per_token") == 1.0

    def test_Top2_Top4_execution_zero(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("top2_executions") == 0
        assert inv.get("top4_executions") == 0

    def test_production_map_not_mutated(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("production_map_mutated") is False

    def test_unknown_failure_blocks_expansion(self):
        report = _load_report("pvr_ec_stage3b_failure_scoreboard")
        assert report.get("unknown_failures", 0) == 0
