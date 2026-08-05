"""Compare materialized benchmark architectures without claiming capability."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from benchmark.common import write_json, write_markdown_report


def _load_creation_reports(paths: list[str]) -> list[dict[str, Any]]:
    rows = []
    for item in paths:
        path = Path(item)
        if path.is_dir():
            path = path / "model_creation_report.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows.extend(payload.get("rows", []))
    return rows


def run(reports: list[str], output: str) -> dict[str, Any]:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    rows = _load_creation_reports(reports)
    by_size: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_size[str(row["model_size_label"])].append(row)
    comparisons = {}
    for size, items in by_size.items():
        dense = next((r for r in items if r["model_family"] == "dense_transformer"), None)
        dense_active = float(dense["active_params_per_token_actual"]) if dense else None
        comparisons[size] = []
        for row in items:
            active = float(row["active_params_per_token_actual"])
            comparisons[size].append({
                "model_variant": row["model_variant"],
                "model_family": row["model_family"],
                "comparison_group": row["comparison_group"],
                "total_params_actual": row["total_params_actual"],
                "active_params_per_token_actual": row["active_params_per_token_actual"],
                "active_params_vs_dense_ratio": active / dense_active if dense_active else None,
                "benchmark_evidence": False,
            })
    payload = {
        "schema_version": "1.0",
        "status": "BENCH_INFRASTRUCTURE_READY" if rows else "BENCH_INFRASTRUCTURE_INCOMPLETE",
        "benchmark_evidence": False,
        "comparison_type": "architecture_materialization_and_parameter_accounting",
        "model_count": len(rows),
        "comparisons_by_size": comparisons,
        "valid_claim": "Models were created and compared for architecture accounting only. Capability comparison remains blocked until real training/eval data and checkpoints exist.",
    }
    write_json(out / "model_comparison_report.json", payload)
    write_markdown_report(out / "model_comparison_report.md", "PVR-EC-O Model Comparison Report", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare materialized benchmark architectures")
    parser.add_argument("--reports", required=True, help="Comma-separated creation report files or directories")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = run([x.strip() for x in args.reports.split(",") if x.strip()], args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
