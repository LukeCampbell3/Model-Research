"""Tests for PVR-EC-O Stage 3D Context Overflow Repair."""
import json, math
import pytest
from pathlib import Path

D = Path("evaluation/benchmark_results/pvr_stage3d_conditioning_repair")

def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestOverflowRepair:
    def test_no_nan_in_fewshot(self):
        r = _load("pvr_ec_stage3d_context_overflow_repair_report")
        assert r["total_nan_count"] == 0

    def test_k1_k4_k8_finite(self):
        r = _load("pvr_ec_stage3d_context_overflow_repair_report")
        for k in ["k1", "k2", "k4", "k8"]:
            acc = r["fewshot_results"][k]["accuracy"]
            assert not math.isnan(acc), f"{k} is NaN"

    def test_max_seq_len_256(self):
        r = _load("pvr_ec_stage3d_context_overflow_repair_report")
        assert r["max_seq_len"] == 256

class TestNaNGuard:
    def test_nan_guard_report_written(self):
        r = _load("pvr_ec_stage3d_nan_guard_report")
        assert "total_nan" in r
        assert r["total_nan"] == 0

    def test_finite_rate_one(self):
        r = _load("pvr_ec_stage3d_nan_guard_report")
        assert r["finite_rate"] == 1.0
