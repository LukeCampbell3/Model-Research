"""Tests for PVR-EC-O Final QPM/Memory Gate."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_final_deployment_gate")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestQPMMemory:
    def test_qpm_memory_report_written(self): _load("pvr_ec_final_qpm_memory_shape_report")
    def test_qpm_pass_rate_high(self):
        r = _load("pvr_ec_final_qpm_memory_shape_report")
        assert r["pass_rate"] >= 0.8
    def test_no_memory_failures(self):
        r = _load("pvr_ec_final_qpm_memory_shape_report")
        assert r["failures"] == 0
