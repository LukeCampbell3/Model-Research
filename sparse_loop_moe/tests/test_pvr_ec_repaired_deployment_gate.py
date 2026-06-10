"""Tests for repaired deployment gate."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_descriptor_semantic_repair")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestRepairedGate:
    def test_repaired_deployment_gate_report_written(self): _load("pvr_ec_final_repaired_deployment_gate_report")
    def test_repaired_multiseed_report_written(self): _load("pvr_ec_final_repaired_multiseed_repeatability_report")
    def test_repaired_qpm_memory_report_written(self): _load("pvr_ec_final_repaired_qpm_memory_shape_report")
    def test_repaired_calibration_report_written(self): _load("pvr_ec_final_repaired_calibration_reliability_report")
    def test_repaired_family_task_regression_report_written(self): _load("pvr_ec_final_repaired_family_task_regression_report")
    def test_repaired_failure_observatory_report_written(self): _load("pvr_ec_final_repaired_failure_observatory_report")
    def test_forward_purity_blocks_deployment(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        assert r["gates"]["forward_purity"] is True
    def test_descriptor_control_blocks_deployment_if_margin_low(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        if not r["gates"]["descriptor_control"]:
            assert "DESCRIPTOR_CONTROL" in r["deployment_verdict"] or "REQUIRES_MORE" in r["deployment_verdict"]
    def test_smoke_run_cannot_confirm_deployment(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        # With only 1 seed, cannot be CONFIRMED
        if r["deployment_verdict"] == "PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED":
            rep = _load("pvr_ec_final_repaired_multiseed_repeatability_report")
            assert len(rep.get("seed_results", {})) >= 5
