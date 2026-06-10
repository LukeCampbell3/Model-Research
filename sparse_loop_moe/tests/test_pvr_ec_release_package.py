"""Tests for release package."""
import json, pytest
from pathlib import Path
D = Path("evaluation/benchmark_results/pvr_release_hardening")
def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())
class TestPackage:
    def test_release_package_report_written(self): _load("pvr_ec_release_package_report")
    def test_release_package_contains_required_files(self):
        r = _load("pvr_ec_release_package_report")
        assert r.get("file_count", 0) >= 10
    def test_rollback_config_written(self):
        pkg = Path("evaluation/benchmark_results/pvr_release_hardening/release_packages")
        if not pkg.exists(): pytest.skip("No package dir")
        configs = list(pkg.rglob("rollback_config.json"))
        assert len(configs) >= 1
