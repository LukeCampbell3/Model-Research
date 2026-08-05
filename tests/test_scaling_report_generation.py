import json

from benchmark.runners.run_benchmark_suite import run_suite
from benchmark.runners.run_scaling_report import generate as generate_scaling
from benchmark.scripts.generate_model_size_matrix import generate


def test_scaling_report_can_compare_multiple_sizes(tmp_path):
    generate(tmp_path)
    for size in ["100m", "300m", "700m"]:
        run_suite(
            str(tmp_path / "benchmark" / "configs" / "generated" / f"benchmark_{size}_suite.yaml"),
            str(tmp_path / "benchmark" / "reports" / "generated" / f"benchmark_{size}_run"),
        )
    payload = generate_scaling(
        str(tmp_path / "benchmark" / "reports" / "generated"),
        str(tmp_path / "benchmark" / "manifests" / "model_size_matrix_manifest.json"),
        str(tmp_path / "benchmark" / "reports" / "generated" / "scaling_report"),
    )
    assert payload["status"] == "NOT_RUN_RESOURCE_BLOCKED"
    axes = payload["scaling_axes"]
    for key in [
        "capability_by_size",
        "efficiency_by_size",
        "routing_specialization_by_size",
        "coding_capability_by_size",
        "quality_per_active_param_by_size",
        "quality_per_gpu_hour_by_size",
        "code_score_per_active_flop_by_size",
    ]:
        assert key in axes
    saved = json.loads((tmp_path / "benchmark" / "reports" / "generated" / "scaling_report" / "scaling_report.json").read_text())
    assert saved["benchmark_evidence"] is False

