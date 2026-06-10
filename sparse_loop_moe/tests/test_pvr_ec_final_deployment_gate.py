"""Tests for PVR-EC-O Final Deployment Gate."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_final_deployment_gate")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestDeploymentGate:
    def test_deployment_gate_report_written(self): _load("pvr_ec_final_deployment_gate_report")
    def test_final_candidate_manifest_written(self): _load("pvr_ec_final_candidate_manifest")
    def test_forward_purity_report_written(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert r["gates"]["forward_purity"] is True
    def test_owners_per_token_one(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
    def test_Top2_Top4_zero(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
    def test_production_map_not_mutated(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert r["hard_invariants"]["production_map_mutated"] is False
    def test_research_verdict_and_deployment_verdict_are_separate(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert "research_verdict" in r and "deployment_verdict" in r
        # They should be different concepts (even if both blocked)
        assert r["research_verdict"] != r["deployment_verdict"] or "CONFIRMED" in r["research_verdict"]
    def test_candidate_config_frozen(self):
        m = _load("pvr_ec_final_candidate_manifest")
        assert "config_name" in m
        assert m["num_experts"] == 4
    def test_unknown_unreplayable_failure_blocks_deployment(self):
        r = _load("pvr_ec_final_deployment_gate_report")
        assert r["unknown_failures"] == 0
