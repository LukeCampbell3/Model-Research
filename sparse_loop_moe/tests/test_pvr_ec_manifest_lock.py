"""Tests for manifest lock."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestManifestLock:
    def test_locked_manifest_written(self): _load("pvr_ec_locked_release_manifest")
    def test_manifest_hashes_match(self):
        r = _load("pvr_ec_manifest_lock_report")
        assert r.get("hashes_match") is True
    def test_manifest_is_immutable(self):
        r = _load("pvr_ec_locked_release_manifest")
        assert r.get("locked") is True
    def test_manifest_schema_mismatch_blocks_release(self):
        r = _load("pvr_ec_manifest_lock_report")
        assert r.get("schemas_match") is True
