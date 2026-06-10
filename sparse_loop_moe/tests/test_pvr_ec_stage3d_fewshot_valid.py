"""Tests for PVR-EC-O Stage 3D Valid Few-Shot."""
import json, math
import pytest
from pathlib import Path

D = Path("evaluation/benchmark_results/pvr_stage3d_conditioning_repair")

def _load(n):
    p = D / f"{n}.json"
    if not p.exists(): pytest.skip(f"Not found: {p}")
    return json.loads(p.read_text())

class TestFewshotValid:
    def test_report_written(self):
        r = _load("pvr_ec_stage3d_fewshot_valid_context_report")
        assert "results_by_k" in r

    def test_all_k_finite(self):
        r = _load("pvr_ec_stage3d_fewshot_valid_context_report")
        assert r["all_finite"] is True

    def test_k0_present(self):
        r = _load("pvr_ec_stage3d_fewshot_valid_context_report")
        assert "0" in r["results_by_k"] or 0 in r["results_by_k"]

    def test_k8_finite(self):
        r = _load("pvr_ec_stage3d_fewshot_valid_context_report")
        k8 = r["results_by_k"].get("8", r["results_by_k"].get(8, {}))
        assert not math.isnan(k8.get("accuracy", float("nan")))

    def test_fewshot_helpful_classified(self):
        r = _load("pvr_ec_stage3d_fewshot_valid_context_report")
        assert "fewshot_helpful" in r
        assert isinstance(r["fewshot_helpful"], bool)
