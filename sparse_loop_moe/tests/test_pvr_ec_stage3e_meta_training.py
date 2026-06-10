"""Tests for PVR-EC-O Stage 3E Episodic Meta Training."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_stage3e_scaling_transfer")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestMetaTraining:
    def test_report_written(self):
        r = _load("pvr_ec_stage3e_episodic_meta_training_report")
        assert "results" in r
    def test_heldout_families_tested(self):
        r = _load("pvr_ec_stage3e_episodic_meta_training_report")
        assert "multisentence_delimiter" in r["results"]
        assert "paraphrase_invariance" in r["results"]
    def test_meta_verdict_valid(self):
        r = _load("pvr_ec_stage3e_episodic_meta_training_report")
        assert r["status"] in ["PVR_EC_STAGE3E_EPISODIC_META_TRAINING_HELPFUL", "PVR_EC_STAGE3E_META_TRAINING_NOT_HELPFUL"]
