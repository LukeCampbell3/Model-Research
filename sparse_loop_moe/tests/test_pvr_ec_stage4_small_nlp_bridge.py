"""Tests for Stage 4 Small NLP Bridge."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage4_small_nlp_bridge")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestStage4:
    def test_stage4_dataset_report_written(self): _load("pvr_ec_stage4_dataset_report")
    def test_stage4_model_comparison_report_written(self): _load("pvr_ec_stage4_model_comparison_report")
    def test_stage4_descriptor_control_report_written(self): _load("pvr_ec_stage4_descriptor_control_report")
    def test_stage4_observatory_report_written(self): _load("pvr_ec_stage4_failure_observatory_report")
    def test_stage4_gate_report_written(self): _load("pvr_ec_stage4_research_gate_report")
    def test_invariants(self):
        r = _load("pvr_ec_stage4_research_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
        assert r["hard_invariants"]["production_map_mutated"] is False
    def test_unknown_failures_zero(self):
        r = _load("pvr_ec_stage4_research_gate_report")
        assert r["unknown_failures"] == 0
