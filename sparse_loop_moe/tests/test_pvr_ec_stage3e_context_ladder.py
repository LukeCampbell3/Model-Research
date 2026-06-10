"""Tests for PVR-EC-O Stage 3E Context Length Ladder."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestContextLadder:
    def test_report_written(self):
        r = _load("pvr_ec_stage3e_context_length_ladder_report")
        assert "results" in r
    def test_multiple_contexts_tested(self):
        r = _load("pvr_ec_stage3e_context_length_ladder_report")
        assert len(r["results"]) >= 4
    def test_verdict_valid(self):
        r = _load("pvr_ec_stage3e_context_length_ladder_report")
        assert r["status"] in ["PVR_EC_STAGE3E_CONTEXT_LENGTH_HELPS_TRANSFER", "PVR_EC_STAGE3E_CONTEXT_LENGTH_NOT_PRIMARY"]
