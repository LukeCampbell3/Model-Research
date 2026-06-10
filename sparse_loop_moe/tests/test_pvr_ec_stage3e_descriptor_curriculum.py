"""Tests for PVR-EC-O Stage 3E Descriptor Curriculum."""
import json, math, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestDescriptorCurriculum:
    def test_report_written(self):
        r = _load("pvr_ec_stage3e_descriptor_curriculum_report")
        assert "descriptor_gain" in r
    def test_gain_finite(self):
        r = _load("pvr_ec_stage3e_descriptor_curriculum_report")
        assert not math.isnan(r["descriptor_gain"])
    def test_ablation_measured(self):
        r = _load("pvr_ec_stage3e_descriptor_curriculum_report")
        assert "ablation_drop" in r
    def test_corruption_measured(self):
        r = _load("pvr_ec_stage3e_descriptor_curriculum_report")
        assert "corruption_drop" in r
