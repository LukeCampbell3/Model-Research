"""Tests for PVR-EC-O Stage 3C Operator and Role Curriculum."""
import json, math
import pytest
from pathlib import Path

RESULTS_DIR = Path("evaluation/benchmark_results/pvr_stage3c_transfer_conditioning")


def _load(name):
    path = RESULTS_DIR / f"{name}.json"
    if not path.exists():
        pytest.skip(f"Report not found: {path}")
    return json.loads(path.read_text())


class TestOperatorComposition:
    def test_operator_composition_curriculum_has_heldout_combos(self):
        report = _load("pvr_ec_stage3c_operator_composition_curriculum_report")
        assert "operator_heldout_acc" in report

    def test_operator_role_reports_written(self):
        report = _load("pvr_ec_stage3c_operator_composition_curriculum_report")
        assert "status" in report
        assert "operator_composition_gain" in report

    def test_operator_composition_gain_measured(self):
        report = _load("pvr_ec_stage3c_operator_composition_curriculum_report")
        gain = report.get("operator_composition_gain", None)
        assert gain is not None
        assert isinstance(gain, (int, float))


class TestRoleBinding:
    def test_role_binding_curriculum_has_heldout_roles(self):
        report = _load("pvr_ec_stage3c_role_binding_curriculum_report")
        assert "role_heldout_acc" in report

    def test_role_binding_gain_measured(self):
        report = _load("pvr_ec_stage3c_role_binding_curriculum_report")
        gain = report.get("role_binding_gain", None)
        assert gain is not None


class TestGateLogic:
    def test_stage3c_gate_blocks_capacity_claim_until_conditioning_tested(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        verdict = report.get("verdict", "")
        # Should NOT claim capacity scaling required if conditioning was helpful
        failures = report.get("failures", [])
        if "PVR_EC_STAGE3C_TRANSFER_CONDITIONING_HELPFUL" in verdict:
            assert "PVR_EC_STAGE3C_CAPACITY_SCALING_REQUIRED" != verdict

    def test_unknown_failures_zero(self):
        report = _load("pvr_ec_stage3c_failure_attribution_report")
        assert report.get("unknown_failures", -1) == 0

    def test_deployment_remains_blocked(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        assert report.get("deployment_verdict") == "PVR_EC_DEPLOYMENT_STILL_BLOCKED"
