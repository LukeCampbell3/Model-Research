"""Tests for PVR-EC-O Stage 3D Combination Sweep and Gate."""
import json, math
import pytest
from pathlib import Path

D = Path("evaluation/benchmark_results/pvr_stage3d_conditioning_repair")

def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestCombinationSweep:
    def test_report_written(self):
        r = _load("pvr_ec_stage3d_minimal_combination_sweep_report")
        assert "combo_results" in r

    def test_best_combo_identified(self):
        r = _load("pvr_ec_stage3d_minimal_combination_sweep_report")
        assert "best_combo_name" in r
        assert "best_combo_acc" in r

    def test_baseline_present(self):
        r = _load("pvr_ec_stage3d_minimal_combination_sweep_report")
        assert "baseline_heldout_acc" in r

class TestResearchGate:
    def test_gate_report_written(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert "verdict" in r

    def test_verdict_valid(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        valid = [
            "PVR_EC_STAGE3D_COMPACT_FEWSHOT_REPAIRED",
            "PVR_EC_STAGE3D_DESCRIPTOR_SEMANTICS_HELPFUL",
            "PVR_EC_STAGE3D_ROLE_BINDING_REPAIRED",
            "PVR_EC_STAGE3D_TRANSFER_CONDITIONING_IMPROVED",
            "PVR_EC_STAGE3D_CONDITIONING_INTERFERENCE_BLOCKED",
            "PVR_EC_STAGE3D_CAPACITY_SCALING_REQUIRED",
            "PVR_EC_STAGE3D_DO_NOT_EXPAND",
        ]
        assert r["verdict"] in valid

    def test_owners_per_token(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["hard_invariants"]["owners_per_token"] == 1.0

    def test_top2_top4_zero(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["hard_invariants"]["top2_executions"] == 0
        assert r["hard_invariants"]["top4_executions"] == 0

    def test_production_map_not_mutated(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["hard_invariants"]["production_map_mutated"] is False

    def test_unknown_failures_zero(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["unknown_failures"] == 0

    def test_overflow_repaired(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["overflow_repaired"] is True

    def test_deployment_still_blocked(self):
        r = _load("pvr_ec_stage3d_research_gate_report")
        assert r["deployment_verdict"] == "PVR_EC_DEPLOYMENT_STILL_BLOCKED"
