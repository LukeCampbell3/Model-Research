"""Tests for Stage 3F Descriptor Confirmation."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3f_descriptor_confirmation")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestStage3F:
    def test_stage3f_descriptor_reproduction_report_written(self):
        _load("pvr_ec_stage3f_descriptor_reproduction_report")
    def test_stage3f_descriptor_ablation_positive(self):
        r = _load("pvr_ec_stage3f_research_gate_report")
        assert r["avg_ablation_drop"] > 0.01
    def test_stage3f_blocks_if_descriptor_not_repeatable(self):
        r = _load("pvr_ec_stage3f_research_gate_report")
        if not r["reproduced"]:
            assert "NOT_REPEATABLE" in r["verdict"]
    def test_invariants(self):
        r = _load("pvr_ec_stage3f_research_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
        assert r["hard_invariants"]["production_map_mutated"] is False
