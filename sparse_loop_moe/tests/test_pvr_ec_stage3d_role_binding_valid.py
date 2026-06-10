"""Tests for PVR-EC-O Stage 3D Valid Role Binding."""
import json, math
import pytest
from pathlib import Path

D = Path("evaluation/benchmark_results/pvr_stage3d_conditioning_repair")

def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestRoleBindingValid:
    def test_report_written(self):
        r = _load("pvr_ec_stage3d_role_binding_valid_report")
        assert "role_accuracy" in r

    def test_finite(self):
        r = _load("pvr_ec_stage3d_role_binding_valid_report")
        assert r["finite"] is True
        assert r["role_nan_count"] == 0

    def test_role_acc_finite(self):
        r = _load("pvr_ec_stage3d_role_binding_valid_report")
        assert not math.isnan(r["role_accuracy"])

    def test_swap_acc_finite(self):
        r = _load("pvr_ec_stage3d_role_binding_valid_report")
        assert not math.isnan(r["role_swap_accuracy"])
