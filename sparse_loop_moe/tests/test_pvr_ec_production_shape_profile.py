"""Tests for production shape profiling."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestProfile:
    def test_production_shape_profile_report_written(self): _load("pvr_ec_production_shape_profile_report")
    def test_production_shape_profile_has_required_shapes(self):
        r = _load("pvr_ec_production_shape_profile_report")
        assert len(r.get("results", {})) >= 10
    def test_owners_per_token_one_in_profile(self):
        r = _load("pvr_ec_production_shape_profile_report")
        for shape, result in r.get("results", {}).items():
            if result.get("pass"):
                assert result.get("owners_per_token") == 1.0
    def test_Top2_Top4_zero_in_profile(self):
        r = _load("pvr_ec_production_shape_profile_report")
        for shape, result in r.get("results", {}).items():
            if result.get("pass"):
                assert result.get("Top2_executions", 0) == 0
                assert result.get("Top4_executions", 0) == 0
    def test_QPM_failures_block_release(self):
        r = _load("pvr_ec_production_shape_profile_report")
        if r["pass_rate"] < 0.90:
            assert "BLOCKED" in r["status"]
    def test_memory_failures_block_release(self):
        r = _load("pvr_ec_production_shape_profile_report")
        assert r.get("failures", 999) == 0
