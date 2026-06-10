"""Tests for PVR-EC-O Stage 3B Failure Attribution.

Verifies failure classification logic and attribution rules.
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


class TestFailureAttribution:
    def test_dominant_failure_classified(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        dominant = report.get("dominant_failure", "")
        assert dominant != "", "No dominant failure classified"

    def test_failure_class_is_valid(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        dominant = report.get("dominant_failure", "")
        valid = [
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
        assert dominant in valid, f"Invalid failure class: {dominant}"

    def test_geometry_status_reported(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        geo = report.get("geometry_status", {})
        assert "membership_entropy" in geo
        assert "membership_margin" in geo

    def test_routing_status_reported(self):
        report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        routing = report.get("routing_status", {})
        assert "owners_per_token" in routing
        assert routing["owners_per_token"] == 1.0


class TestFailureScoreboard:
    def test_scoreboard_written(self):
        report = _load_report("pvr_ec_stage3b_failure_scoreboard")
        assert "total_failures" in report
        assert "unknown_failures" in report

    def test_no_unknown_failures(self):
        report = _load_report("pvr_ec_stage3b_failure_scoreboard")
        assert report.get("unknown_failures", -1) == 0

    def test_failure_classes_listed(self):
        report = _load_report("pvr_ec_stage3b_failure_scoreboard")
        classes = report.get("failure_classes", [])
        assert len(classes) >= 1, "At least one failure class expected"


class TestHardInvariants:
    def test_runtime_dynamic_k_zero(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        # Top2/Top4 = 0 implies dynamic-K = 0
        assert inv.get("top2_executions", -1) == 0
        assert inv.get("top4_executions", -1) == 0

    def test_runtime_expert_choice_zero(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        # No Expert Choice in runtime = Top1 only
        assert inv.get("owners_per_token") == 1.0

    def test_production_map_not_mutated(self):
        report = _load_report("pvr_ec_stage3b_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("production_map_mutated") is False


class TestAttributionRules:
    """Test the attribution rules from the specification."""

    def test_descriptor_unused_classification_logic(self):
        """If descriptor doesn't help, classify DESCRIPTOR_UNUSED."""
        desc_report = _load_report("pvr_ec_stage3b_descriptor_conditioning_report")
        gain = desc_report.get("descriptor_gain", 0)
        classification = desc_report.get("classification", "")
        
        if gain <= 0.05:
            assert classification == "TASK_DESCRIPTOR_UNUSED"

    def test_transfer_not_routing_when_geometry_sharp(self):
        """If geometry is sharp but transfer fails, routing is not primary."""
        attr_report = _load_report("pvr_ec_stage3b_transfer_attribution_report")
        geo = attr_report.get("geometry_status", {})
        
        if geo.get("membership_entropy", 999) < 0.5 and geo.get("membership_margin", 0) > 0.8:
            # Geometry is sharp, so failure is not geometry-related
            dominant = attr_report.get("dominant_failure", "")
            assert dominant != "PVR_EC_FAILURE_GEOMETRY_NOT_LOADED_IN_TRANSFER"
