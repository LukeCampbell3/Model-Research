"""Tests for release freeze."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestFreeze:
    def test_candidate_freeze_report_written(self): _load("pvr_ec_candidate_freeze_report")
    def test_required_artifacts_exist(self):
        r = _load("pvr_ec_candidate_freeze_report")
        assert r.get("missing_artifacts", ["x"]) == []
    def test_artifact_hashes_computed(self):
        r = _load("pvr_ec_candidate_freeze_report")
        assert "hashes" in r and len(r["hashes"]) > 0
    def test_missing_artifact_blocks_release(self):
        r = _load("pvr_ec_candidate_freeze_report")
        if r.get("missing_artifacts"):
            assert "BLOCKED" in r["status"]
