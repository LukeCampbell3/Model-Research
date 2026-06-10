"""Tests for PVR-EC-O Final Research Gate."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_final_research_gate")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestFinalGate:
    def test_final_research_verdict_written(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert "research_verdict" in r
    def test_final_deployment_verdict_written(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert "deployment_verdict" in r
    def test_research_and_deployment_verdicts_are_separate(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert r["research_verdict"] != r["deployment_verdict"]
    def test_owners_per_token_remains_one(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
    def test_Top2_Top4_execution_zero(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
    def test_production_map_not_mutated(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert r["hard_invariants"]["production_map_mutated"] is False
    def test_unknown_failure_blocks_or_registers(self):
        r = _load("pvr_ec_final_research_gate_report")
        assert r["unknown_failures"] == 0
    def test_research_verdict_valid(self):
        r = _load("pvr_ec_final_research_gate_report")
        valid = ["PVR_EC_RESEARCH_CANDIDATE_CONFIRMED","PVR_EC_RESEARCH_CANDIDATE_CONFIRMED_WITH_BLOCKERS",
                 "PVR_EC_RESEARCH_CANDIDATE_NOT_COMPETITIVE","PVR_EC_RESEARCH_REQUIRES_ARCHITECTURE_REVISION"]
        assert r["research_verdict"] in valid
    def test_deployment_verdict_valid(self):
        r = _load("pvr_ec_final_research_gate_report")
        valid = ["PVR_EC_DEPLOYMENT_STILL_BLOCKED","PVR_EC_DEPLOYMENT_CANDIDATE_REQUIRES_FINAL_GATE","PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED"]
        assert r["deployment_verdict"] in valid
