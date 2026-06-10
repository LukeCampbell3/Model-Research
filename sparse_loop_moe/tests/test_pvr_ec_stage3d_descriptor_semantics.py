"""Tests for PVR-EC-O Stage 3D Descriptor Semantics."""
import json, math
import pytest
from pathlib import Path

D = Path("evaluation/benchmark_results/pvr_stage3d_conditioning_repair")

def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestDescriptorSemantics:
    def test_report_written(self):
        r = _load("pvr_ec_stage3d_descriptor_semantics_report")
        assert "descriptor_gain" in r

    def test_descriptor_gain_finite(self):
        r = _load("pvr_ec_stage3d_descriptor_semantics_report")
        assert not math.isnan(r["descriptor_gain"])

    def test_ablation_measured(self):
        r = _load("pvr_ec_stage3d_descriptor_semantics_report")
        assert "descriptor_ablation_drop" in r

    def test_corruption_measured(self):
        r = _load("pvr_ec_stage3d_descriptor_semantics_report")
        assert "descriptor_corruption_drop" in r

    def test_invariants_preserved(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        inv = r["hard_invariants"]
        assert inv["owners_per_token"] == 1.0
        assert inv["top2_executions"] == 0
        assert inv["top4_executions"] == 0
        assert inv["production_map_mutated"] is False
