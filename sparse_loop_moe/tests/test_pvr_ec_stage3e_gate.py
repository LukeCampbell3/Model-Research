"""Tests for PVR-EC-O Stage 3E Final Gate."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestGate:
    def test_gate_report_written(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert "verdict" in r
    def test_verdict_valid(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        valid = [
            "PVR_EC_STAGE3E_SCALE_HELPS_TRANSFER",
            "PVR_EC_STAGE3E_SCALE_ALONE_NOT_ENOUGH",
            "PVR_EC_STAGE3E_CONTEXT_LENGTH_HELPS_TRANSFER",
            "PVR_EC_STAGE3E_CONTEXT_LENGTH_NOT_PRIMARY",
            "PVR_EC_STAGE3E_EPISODIC_META_TRAINING_HELPFUL",
            "PVR_EC_STAGE3E_META_TRAINING_NOT_HELPFUL",
            "PVR_EC_STAGE3E_TRANSFER_EMERGES",
            "PVR_EC_STAGE3E_TRANSFER_STILL_BLOCKED",
            "PVR_EC_STAGE3E_RESEARCH_ALLOWED_WITH_BLOCKERS",
        ]
        assert r["verdict"] in valid
    def test_owners_per_token(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0
    def test_top2_top4_zero(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0
    def test_production_map_not_mutated(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert r["hard_invariants"]["production_map_mutated"] is False
    def test_unknown_failures_zero(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert r["unknown_failures"] == 0
    def test_deployment_still_blocked(self):
        r = _load("pvr_ec_stage3e_research_gate_report")
        assert r["deployment_verdict"] == "PVR_EC_DEPLOYMENT_STILL_BLOCKED"
