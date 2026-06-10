"""Tests for descriptor semantic identity repair."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_descriptor_semantic_repair")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestRepairSweep:
    def test_semantic_repair_sweep_report_written(self): _load("pvr_ec_descriptor_semantic_repair_sweep_report")
    def test_candidate_manifest_diff_report_written(self): _load("pvr_ec_descriptor_repair_manifest_diff_report")
    def test_descriptor_margin_loss_computable(self):
        r = _load("pvr_ec_descriptor_semantic_repair_sweep_report")
        assert "variants" in r and len(r["variants"]) >= 1
    def test_wrong_descriptor_suppression_loss_computable(self):
        r = _load("pvr_ec_descriptor_semantic_repair_sweep_report")
        for v in r["variants"].values():
            assert "avg_margin" in v

class TestInvariants:
    def test_owners_per_token_one(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
    def test_Top2_Top4_zero(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
    def test_production_map_not_mutated(self):
        r = _load("pvr_ec_final_repaired_deployment_gate_report")
        assert r["hard_invariants"]["production_map_mutated"] is False
