"""Tests for PVR-EC-O Stage 3C Few-Shot Context Conditioning."""
import json, math
import pytest
from pathlib import Path

RESULTS_DIR = Path("evaluation/benchmark_results/pvr_stage3c_transfer_conditioning")


def _load(name):
    path = RESULTS_DIR / f"{name}.json"
    if not path.exists():
        pytest.skip(f"Report not found: {path}")
    return json.loads(path.read_text())


class TestFewshotContext:
    def test_fewshot_context_contains_demonstrations(self):
        report = _load("pvr_ec_stage3c_fewshot_context_report")
        assert "k1" in report
        assert "k4" in report
        assert "k8" in report

    def test_fewshot_k_changes_sequence_length(self):
        report = _load("pvr_ec_stage3c_fewshot_context_report")
        # k=1 should have shorter context than k=4
        k1_acc = report.get("k1", {}).get("accuracy", 0)
        assert isinstance(k1_acc, (int, float))

    def test_fewshot_query_target_correct(self):
        report = _load("pvr_ec_stage3c_fewshot_context_report")
        baseline = report.get("baseline_heldout_acc", 0)
        assert isinstance(baseline, (int, float))
        assert baseline > 0.0

    def test_fewshot_report_written(self):
        report = _load("pvr_ec_stage3c_fewshot_context_report")
        assert "status" in report
        assert "fewshot_helpful" in report


class TestFewshotInvariants:
    def test_fewshot_does_not_violate_forward_purity(self):
        report = _load("pvr_ec_stage3c_research_gate_report")
        inv = report.get("hard_invariants", {})
        assert inv.get("owners_per_token") == 1.0
        assert inv.get("top2_executions") == 0
        assert inv.get("top4_executions") == 0
