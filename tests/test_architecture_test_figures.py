import json
from pathlib import Path

from benchmark.runners.run_architecture_test_figures import parse_junit, summarize, write_figures


def test_architecture_test_figures_parse_junit_and_write_svg(tmp_path):
    junit = tmp_path / "pytest_junit.xml"
    junit.write_text(
        """<?xml version="1.0" encoding="utf-8"?>
<testsuites>
  <testsuite name="pytest" tests="3" failures="1" errors="0" skipped="1" time="1.5">
    <testcase classname="tests.test_routing_invariant_logging" name="test_top1_owner_invariant" time="0.4" />
    <testcase classname="sparse_loop_moe.tests.test_pvr_ec_final_research_gate" name="test_final_gate" time="0.9">
      <failure message="failed">assert False</failure>
    </testcase>
    <testcase classname="tests.test_scaling_report_generation" name="test_scaling" time="0.2">
      <skipped message="resource blocked" />
    </testcase>
  </testsuite>
</testsuites>
""",
        encoding="utf-8",
    )

    rows = parse_junit(junit)
    summary = summarize(rows, exit_code=1, elapsed_seconds=2.0)
    figures = write_figures(tmp_path / "out", rows, summary)

    assert summary["status"] == "ARCHITECTURE_TEST_SUITE_BLOCKED"
    assert summary["total_tests"] == 3
    assert summary["passed"] == 1
    assert summary["failed"] == 1
    assert summary["skipped"] == 1
    assert summary["area_counts"]["routing"]["passed"] == 1
    assert summary["area_counts"]["final_gates"]["failure"] == 1
    assert len(figures) == 5
    for figure in figures:
        path = Path(figure["path"])
        assert path.exists()
        assert path.read_text(encoding="utf-8").startswith("<svg")

    (tmp_path / "summary.json").write_text(json.dumps(summary), encoding="utf-8")

