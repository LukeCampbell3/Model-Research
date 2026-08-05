"""Run architecture tests and turn pytest metrics into figure images."""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


DEFAULT_TEST_ROOTS = ["tests", "sparse_loop_moe/tests"]
DEFAULT_OUTPUT = "benchmark/reports/generated/architecture_test_figures"

AREA_RULES = [
    ("final_gates", ["final", "release", "deployment", "readiness", "gate"]),
    ("routing", ["routing", "router", "top1", "top2", "owner", "ownership", "expert"]),
    ("descriptor_control", ["descriptor", "operator", "semantic", "role", "fewshot"]),
    ("scaling", ["scaling", "300m", "700m", "size", "trunk"]),
    ("benchmark_evidence", ["benchmark", "scorecard", "manifest", "contamination", "public"]),
    ("nlp_bridge", ["nlp", "stage4", "stage5", "language"]),
    ("safety_invariants", ["no_runtime", "invariant", "blocked", "freeze", "canary", "drift"]),
    ("training_diagnostics", ["training", "loss", "calibration", "memory", "qpm", "bottleneck"]),
]


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _status(case: ET.Element) -> str:
    for child in case:
        name = _local_name(child.tag)
        if name in {"failure", "error", "skipped"}:
            return name
    return "passed"


def _case_id(row: dict[str, Any]) -> str:
    classname = row.get("classname") or ""
    name = row.get("name") or ""
    return f"{classname}::{name}" if classname else str(name)


def _area_for(row: dict[str, Any]) -> str:
    haystack = " ".join(str(row.get(key, "")) for key in ["classname", "name", "file"]).lower()
    for area, needles in AREA_RULES:
        if any(needle in haystack for needle in needles):
            return area
    if "pvr_ec" in haystack:
        return "pvr_ec_core"
    return "general"


def parse_junit(path: str | Path) -> list[dict[str, Any]]:
    """Parse pytest JUnit XML into per-test metric rows."""
    root = ET.parse(path).getroot()
    rows: list[dict[str, Any]] = []
    for case in root.iter():
        if _local_name(case.tag) != "testcase":
            continue
        row = {
            "classname": case.attrib.get("classname", ""),
            "name": case.attrib.get("name", ""),
            "file": case.attrib.get("file", ""),
            "line": case.attrib.get("line", ""),
            "time_seconds": _float(case.attrib.get("time")),
            "status": _status(case),
        }
        row["id"] = _case_id(row)
        row["area"] = _area_for(row)
        rows.append(row)
    return rows


def summarize(rows: list[dict[str, Any]], *, exit_code: int, elapsed_seconds: float) -> dict[str, Any]:
    status_counts = Counter(row["status"] for row in rows)
    area_counts: dict[str, Counter] = defaultdict(Counter)
    file_duration: dict[str, float] = defaultdict(float)
    file_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        area_counts[row["area"]][row["status"]] += 1
        file_key = row["classname"].split(".")[0] if row["classname"] else row.get("file") or "unknown"
        if "." in row["classname"]:
            parts = row["classname"].split(".")
            file_key = ".".join(parts[:2]) if parts[0] in {"tests", "sparse_loop_moe"} else parts[0]
        file_duration[file_key] += float(row["time_seconds"])
        file_counts[file_key] += 1
    total = len(rows)
    failed = status_counts.get("failure", 0) + status_counts.get("error", 0)
    skipped = status_counts.get("skipped", 0)
    passed = status_counts.get("passed", 0)
    conclusion = "ARCHITECTURE_TEST_SUITE_PASSED" if exit_code == 0 and failed == 0 and total > 0 else "ARCHITECTURE_TEST_SUITE_BLOCKED"
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": conclusion,
        "pytest_exit_code": exit_code,
        "elapsed_seconds": elapsed_seconds,
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "pass_rate": (passed / total) if total else 0.0,
        "total_test_time_seconds": sum(float(row["time_seconds"]) for row in rows),
        "status_counts": dict(status_counts),
        "area_counts": {area: dict(counts) for area, counts in sorted(area_counts.items())},
        "slowest_tests": sorted(rows, key=lambda row: float(row["time_seconds"]), reverse=True)[:25],
        "duration_by_file": [
            {
                "file_group": file_key,
                "time_seconds": seconds,
                "test_count": file_counts[file_key],
            }
            for file_key, seconds in sorted(file_duration.items(), key=lambda item: item[1], reverse=True)
        ],
        "architecture_conclusion": (
            "All collected architecture tests passed."
            if conclusion == "ARCHITECTURE_TEST_SUITE_PASSED"
            else "Architecture conclusion is blocked by failing, errored, or uncollected tests."
        ),
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _svg_start(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#172026}.title{font-size:24px;font-weight:700}.head{font-size:17px;font-weight:700}.small{font-size:13px}.axis{stroke:#5d6970;stroke-width:1}.grid{stroke:#d8dee3;stroke-width:1}.ok{fill:#27856f}.bad{fill:#b65a4b}.skip{fill:#b68a2e}.blue{fill:#2f6f9f}.panel{fill:#f7f9fb;stroke:#cbd4db}",
        "</style>",
    ]


def _text(x: float, y: float, value: Any, klass: str = "small", anchor: str = "start") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{klass}" text-anchor="{anchor}">{html.escape(str(value))}</text>'


def _bar(value: float, maximum: float, width: float) -> float:
    if maximum <= 0:
        return 0
    return max(0.0, min(width, value / maximum * width))


def _figure_summary(path: Path, summary: dict[str, Any]) -> None:
    width, height = 920, 520
    lines = _svg_start(width, height)
    lines.append(_text(40, 48, "Figure 1. Architecture Test Verdict", "title"))
    status = summary["status"]
    ok = status == "ARCHITECTURE_TEST_SUITE_PASSED"
    color = "#27856f" if ok else "#b65a4b"
    lines.append(f'<rect x="50" y="84" width="820" height="130" rx="8" fill="#f7f9fb" stroke="#cbd4db"/>')
    lines.append(f'<circle cx="105" cy="149" r="28" fill="{color}"/>')
    lines.append(_text(155, 134, status, "head"))
    lines.append(_text(155, 166, summary["architecture_conclusion"], "small"))
    metrics = [
        ("Total", summary["total_tests"]),
        ("Passed", summary["passed"]),
        ("Failed/Error", summary["failed"]),
        ("Skipped", summary["skipped"]),
        ("Pass Rate", f"{summary['pass_rate'] * 100:.1f}%"),
        ("Elapsed", f"{summary['elapsed_seconds']:.1f}s"),
    ]
    for idx, (label, value) in enumerate(metrics):
        x = 60 + (idx % 3) * 280
        y = 270 + (idx // 3) * 95
        lines.append(f'<rect x="{x}" y="{y}" width="240" height="68" rx="6" class="panel"/>')
        lines.append(_text(x + 18, y + 27, label, "small"))
        lines.append(_text(x + 18, y + 54, value, "head"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def _figure_area(path: Path, summary: dict[str, Any]) -> None:
    areas = summary["area_counts"]
    rows = []
    for area, counts in areas.items():
        rows.append((area, counts.get("passed", 0), counts.get("failure", 0) + counts.get("error", 0), counts.get("skipped", 0)))
    rows.sort(key=lambda item: sum(item[1:]), reverse=True)
    width, height = 1040, max(420, 100 + len(rows) * 34)
    lines = _svg_start(width, height)
    lines.append(_text(40, 48, "Figure 2. Test Coverage by Architecture Area", "title"))
    max_total = max([sum(item[1:]) for item in rows] or [1])
    for idx, (area, passed, failed, skipped) in enumerate(rows):
        y = 88 + idx * 34
        lines.append(_text(55, y + 15, area, "small"))
        x = 270
        passed_w = _bar(passed, max_total, 590)
        failed_w = _bar(failed, max_total, 590)
        skipped_w = _bar(skipped, max_total, 590)
        lines.append(f'<rect x="{x}" y="{y}" width="590" height="18" fill="#eef2f5"/>')
        lines.append(f'<rect x="{x}" y="{y}" width="{passed_w:.1f}" height="18" fill="#27856f"/>')
        lines.append(f'<rect x="{x + passed_w:.1f}" y="{y}" width="{failed_w:.1f}" height="18" fill="#b65a4b"/>')
        lines.append(f'<rect x="{x + passed_w + failed_w:.1f}" y="{y}" width="{skipped_w:.1f}" height="18" fill="#b68a2e"/>')
        lines.append(_text(880, y + 15, f"{passed} pass / {failed} fail / {skipped} skip", "small"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def _figure_duration(path: Path, summary: dict[str, Any]) -> None:
    rows = summary["duration_by_file"][:20]
    width, height = 1040, max(430, 100 + len(rows) * 30)
    lines = _svg_start(width, height)
    lines.append(_text(40, 48, "Figure 3. Test Runtime by File Group", "title"))
    max_time = max([row["time_seconds"] for row in rows] or [1.0])
    for idx, row in enumerate(rows):
        y = 88 + idx * 30
        value = float(row["time_seconds"])
        lines.append(_text(55, y + 14, row["file_group"], "small"))
        lines.append(f'<rect x="335" y="{y}" width="520" height="16" fill="#eef2f5"/>')
        lines.append(f'<rect x="335" y="{y}" width="{_bar(value, max_time, 520):.1f}" height="16" fill="#2f6f9f"/>')
        lines.append(_text(875, y + 14, f"{value:.2f}s ({row['test_count']} tests)", "small"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def _figure_slowest(path: Path, summary: dict[str, Any]) -> None:
    rows = summary["slowest_tests"][:15]
    width, height = 1120, max(460, 110 + len(rows) * 34)
    lines = _svg_start(width, height)
    lines.append(_text(40, 48, "Figure 4. Slowest Individual Tests", "title"))
    max_time = max([float(row["time_seconds"]) for row in rows] or [1.0])
    for idx, row in enumerate(rows):
        y = 90 + idx * 34
        label = row["id"]
        if len(label) > 78:
            label = "..." + label[-75:]
        value = float(row["time_seconds"])
        lines.append(_text(55, y + 15, label, "small"))
        lines.append(f'<rect x="680" y="{y}" width="260" height="18" fill="#eef2f5"/>')
        lines.append(f'<rect x="680" y="{y}" width="{_bar(value, max_time, 260):.1f}" height="18" fill="#b68a2e"/>')
        lines.append(_text(960, y + 15, f"{value:.3f}s", "small"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def _figure_failures(path: Path, rows: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    failures = [row for row in rows if row["status"] in {"failure", "error"}]
    width, height = 1040, max(360, 118 + max(1, len(failures[:12])) * 40)
    lines = _svg_start(width, height)
    lines.append(_text(40, 48, "Figure 5. Architecture Conclusion From Tests", "title"))
    if not failures:
        lines.append(f'<rect x="55" y="90" width="930" height="120" rx="8" fill="#eef8f2" stroke="#8ab99e"/>')
        lines.append(_text(80, 135, "No failing or errored tests in collected architecture evidence.", "head"))
        lines.append(_text(80, 170, f"Conclusion: {summary['status']}", "small"))
    else:
        lines.append(f'<rect x="55" y="90" width="930" height="70" rx="8" fill="#fff1ee" stroke="#c9877b"/>')
        lines.append(_text(80, 132, f"{len(failures)} failures/errors block the architecture conclusion.", "head"))
        for idx, row in enumerate(failures[:12]):
            y = 200 + idx * 40
            label = row["id"]
            if len(label) > 100:
                label = "..." + label[-97:]
            lines.append(f'<circle cx="72" cy="{y-5}" r="8" fill="#b65a4b"/>')
            lines.append(_text(95, y, label, "small"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_figures(output: str | Path, rows: list[dict[str, Any]], summary: dict[str, Any]) -> list[dict[str, str]]:
    figure_dir = Path(output) / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)
    figures = [
        ("Figure 1", figure_dir / "figure_1_architecture_test_verdict.svg", "Architecture test verdict and high-level run metrics."),
        ("Figure 2", figure_dir / "figure_2_area_coverage.svg", "Pass, fail, and skip counts grouped by architecture area."),
        ("Figure 3", figure_dir / "figure_3_runtime_by_file_group.svg", "Aggregate pytest runtime by file group."),
        ("Figure 4", figure_dir / "figure_4_slowest_tests.svg", "Slowest individual tests from the executed suite."),
        ("Figure 5", figure_dir / "figure_5_failure_conclusion.svg", "Failure panel or final pass conclusion from the executed tests."),
    ]
    _figure_summary(figures[0][1], summary)
    _figure_area(figures[1][1], summary)
    _figure_duration(figures[2][1], summary)
    _figure_slowest(figures[3][1], summary)
    _figure_failures(figures[4][1], rows, summary)
    return [{"id": item[0], "path": str(item[1]), "caption": item[2]} for item in figures]


def _write_report(path: Path, summary: dict[str, Any], figures: list[dict[str, str]]) -> None:
    lines = [
        "# Architecture Test Figures",
        "",
        f"Status: `{summary['status']}`",
        "",
        summary["architecture_conclusion"],
        "",
        "## Metrics",
        "",
        f"- Total tests: `{summary['total_tests']}`",
        f"- Passed: `{summary['passed']}`",
        f"- Failed/errors: `{summary['failed']}`",
        f"- Skipped: `{summary['skipped']}`",
        f"- Pass rate: `{summary['pass_rate'] * 100:.1f}%`",
        f"- Elapsed wall time: `{summary['elapsed_seconds']:.1f}s`",
        "",
        "## Figure Images",
        "",
    ]
    for figure in figures:
        lines.append(f"- {figure['id']}: `{figure['path']}` - {figure['caption']}")
    path.write_text("\n".join(lines), encoding="utf-8")


def run_pytest(test_roots: list[str], output: str, extra_args: list[str] | None = None) -> dict[str, Any]:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    junit_path = out / "pytest_junit.xml"
    stdout_path = out / "pytest_stdout.txt"
    stderr_path = out / "pytest_stderr.txt"
    args = [sys.executable, "-m", "pytest", *test_roots, f"--junitxml={junit_path}", "--durations=0"]
    if extra_args:
        args.extend(extra_args)
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    started = utc_now()
    import time

    t0 = time.perf_counter()
    proc = subprocess.run(args, text=True, capture_output=True, env=env)
    elapsed = time.perf_counter() - t0
    stdout_path.write_text(proc.stdout, encoding="utf-8", errors="replace")
    stderr_path.write_text(proc.stderr, encoding="utf-8", errors="replace")
    rows = parse_junit(junit_path) if junit_path.exists() else []
    summary = summarize(rows, exit_code=proc.returncode, elapsed_seconds=elapsed)
    figures = write_figures(out, rows, summary)
    data_dir = out / "data"
    _write_csv(data_dir / "test_cases.csv", rows, ["id", "area", "classname", "name", "file", "line", "time_seconds", "status"])
    _write_csv(data_dir / "duration_by_file.csv", summary["duration_by_file"], ["file_group", "time_seconds", "test_count"])
    manifest = {
        **summary,
        "started_at": started,
        "pytest_command": args,
        "test_roots": test_roots,
        "junit_xml": str(junit_path),
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
        "figures": figures,
        "tables": {
            "test_cases": str(data_dir / "test_cases.csv"),
            "duration_by_file": str(data_dir / "duration_by_file.csv"),
        },
    }
    write_json(out / "architecture_test_figures.json", manifest)
    _write_report(out / "architecture_test_figures.md", manifest, figures)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pytest and generate architecture metric figure images")
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--tests", nargs="+", default=DEFAULT_TEST_ROOTS)
    parser.add_argument("--pytest-arg", action="append", default=[], help="Extra argument forwarded to pytest; repeat as needed.")
    args = parser.parse_args()
    manifest = run_pytest(args.tests, args.output, args.pytest_arg)
    print(manifest["status"])
    print(f"tests={manifest['total_tests']} passed={manifest['passed']} failed={manifest['failed']} skipped={manifest['skipped']}")
    raise SystemExit(int(manifest["pytest_exit_code"]))


if __name__ == "__main__":
    main()
