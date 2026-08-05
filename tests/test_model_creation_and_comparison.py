import json

from benchmark.runners.run_model_comparison import run as run_comparison
from benchmark.runners.run_model_creation import run as run_creation
from benchmark.scripts.generate_model_size_matrix import generate


def test_model_creation_and_comparison_reports(tmp_path):
    generate(tmp_path)
    creation = run_creation(
        str(tmp_path / "benchmark" / "configs" / "generated" / "benchmark_100m_suite.yaml"),
        str(tmp_path / "creation"),
        device="meta",
        limit=3,
    )
    assert creation["status"] == "BENCH_INFRASTRUCTURE_READY"
    assert creation["created_model_count"] == 3
    assert creation["benchmark_evidence"] is False
    for row in creation["rows"]:
        assert row["created"] is True
        assert row["total_params_actual"] > 0
        assert row["forward_probe"]["executed_forward"] is False

    comparison = run_comparison([str(tmp_path / "creation")], str(tmp_path / "comparison"))
    assert comparison["status"] == "BENCH_INFRASTRUCTURE_READY"
    assert comparison["benchmark_evidence"] is False
    saved = json.loads((tmp_path / "comparison" / "model_comparison_report.json").read_text())
    assert saved["model_count"] == 3
