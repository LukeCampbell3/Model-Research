"""Tests for canary rollout simulation."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestCanary:
    def test_canary_rollout_report_written(self): _load("pvr_ec_canary_rollout_simulation_report")
    def test_canary_has_all_traffic_slices(self):
        r = _load("pvr_ec_canary_rollout_simulation_report")
        assert len(r.get("results", {})) >= 5
    def test_no_rollback_triggered(self):
        r = _load("pvr_ec_canary_rollout_simulation_report")
        assert r.get("rollback_triggered") is False
    def test_forward_purity_failure_triggers_rollback(self):
        r = _load("pvr_ec_canary_rollout_simulation_report")
        for _, slice_r in r.get("results", {}).items():
            assert slice_r.get("owners_per_token") == 1.0
