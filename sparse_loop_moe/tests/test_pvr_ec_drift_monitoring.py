"""Tests for drift monitoring baselines."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestDrift:
    def test_drift_monitoring_baseline_report_written(self): _load("pvr_ec_drift_monitoring_baseline_report")
    def test_descriptor_control_monitor_defined(self):
        r = _load("pvr_ec_drift_monitoring_baseline_report")
        assert "descriptor_control_margin" in r.get("baselines", {})
    def test_owner_prototype_drift_monitor_defined(self):
        r = _load("pvr_ec_drift_monitoring_baseline_report")
        assert "owners_per_token" in r.get("baselines", {})
    def test_calibration_drift_monitor_defined(self):
        r = _load("pvr_ec_drift_monitoring_baseline_report")
        assert "calibration_proxy" in r.get("baselines", {})
    def test_qpm_memory_drift_monitor_defined(self):
        r = _load("pvr_ec_drift_monitoring_baseline_report")
        assert "qpm_tokens_per_second" in r.get("baselines", {})
    def test_rollback_thresholds_defined(self):
        r = _load("pvr_ec_drift_monitoring_baseline_report")
        for monitor, cfg in r.get("baselines", {}).items():
            assert "rollback_threshold" in cfg, f"Missing rollback for {monitor}"
