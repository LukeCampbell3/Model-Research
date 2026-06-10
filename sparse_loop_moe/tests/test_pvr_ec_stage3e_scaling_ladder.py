"""Tests for PVR-EC-O Stage 3E Scaling Ladder."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestScalingLadder:
    def test_report_written(self):
        r = _load("pvr_ec_stage3e_scaling_ladder_report")
        assert "results" in r
    def test_all_configs_tested(self):
        r = _load("pvr_ec_stage3e_scaling_ladder_report")
        assert "small_128_2layer" in r["results"]
        assert "medium_256_4layer" in r["results"]
    def test_param_counts_reported(self):
        r = _load("pvr_ec_stage3e_scaling_ladder_report")
        for cfg in r["results"].values():
            assert "parameter_count" in cfg
            assert cfg["parameter_count"] > 0
    def test_scale_verdict_valid(self):
        r = _load("pvr_ec_stage3e_scaling_ladder_report")
        assert r["status"] in ["PVR_EC_STAGE3E_SCALE_HELPS_TRANSFER", "PVR_EC_STAGE3E_SCALE_ALONE_NOT_ENOUGH"]
