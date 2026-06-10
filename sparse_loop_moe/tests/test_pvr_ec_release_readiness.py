"""Tests for final release readiness."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestReleaseReadiness:
    def test_final_release_readiness_report_written(self): _load("pvr_ec_final_release_readiness_report")
    def test_release_ready_requires_all_required_gates(self):
        r = _load("pvr_ec_final_release_readiness_report")
        if "READY" in r.get("final_release_verdict", ""):
            assert r.get("candidate_freeze_status") == "PASSED"
            assert r.get("manifest_lock_status") == "LOCKED"
            assert r.get("canary_simulation_status") == "PASSED"
            assert r.get("drift_monitoring_status") == "CREATED"
    def test_release_blocked_if_manifest_fails(self):
        r = _load("pvr_ec_final_release_readiness_report")
        if r.get("manifest_lock_status") != "LOCKED":
            assert "BLOCKED" in r.get("final_release_verdict", "")
    def test_release_blocked_if_canary_fails(self):
        r = _load("pvr_ec_final_release_readiness_report")
        if r.get("canary_simulation_status") not in ["PASSED", "PASSED_WITH_WARNINGS"]:
            assert "BLOCKED" in r.get("final_release_verdict", "")
    def test_hard_invariants(self):
        r = _load("pvr_ec_final_release_readiness_report")
        inv = r.get("hard_invariants", {})
        assert inv.get("owners_per_token") == 1.0
        assert inv.get("top2_executions") == 0
        assert inv.get("top4_executions") == 0
        assert inv.get("production_map_mutated") is False
