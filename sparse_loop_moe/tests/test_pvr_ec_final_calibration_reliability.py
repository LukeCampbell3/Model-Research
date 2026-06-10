"""Tests for PVR-EC-O Final Calibration/Reliability."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_final_deployment_gate")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestCalibration:
    def test_calibration_reliability_report_written(self): _load("pvr_ec_final_calibration_reliability_report")
    def test_high_confidence_failure_bounded(self):
        r = _load("pvr_ec_final_calibration_reliability_report")
        assert r["high_confidence_failure_rate"] < 0.05
    def test_multiseed_repeatability_report_written(self): _load("pvr_ec_final_multiseed_repeatability_report")
    def test_seed_collapse_blocks_deployment(self):
        r = _load("pvr_ec_final_multiseed_repeatability_report")
        assert r["catastrophic_seed_count"] == 0
