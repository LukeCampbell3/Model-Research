"""Summarize the EAN structured-span route-stability repair attempt."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_NOT_SUPPORTED = "PVR_EAN_STRUCTURED_SPAN_ROUTE_STABILITY_REPAIR_NOT_SUPPORTED"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run(
    input_report: str = "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/structured_span_repair_report.json",
    output: str = "benchmark/reports/generated/ean_structured_span_route_stability_repair_decision",
) -> dict[str, Any]:
    report = _load(input_report)
    comparison = report["comparison"]
    windows = report["structured_windows"]["windows"]
    window_rows = []
    for step, rows in windows.items():
        ean_delta = rows["ean_seed42"]["delta_vs_baseline"]
        repaired_delta = rows["repaired_ean"]["delta_vs_baseline"]
        window_rows.append({
            "step": int(step),
            "ean_delta_vs_baseline": ean_delta,
            "repaired_delta_vs_baseline": repaired_delta,
            "repair_minus_ean_delta": repaired_delta - ean_delta,
            "baseline_loss": rows["pvr_baseline_seed42"]["loss"],
            "ean_loss": rows["ean_seed42"]["loss"],
            "repaired_loss": rows["repaired_ean"]["loss"],
            "dense_loss": rows["dense_300m"]["loss"],
        })
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_NOT_SUPPORTED,
        "source_report": input_report,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_route_stability",
        "comparison": comparison,
        "structured_windows": window_rows,
        "decision": {
            "top1_invariants_clean": comparison.get("top1_invariants_clean"),
            "scorecard_still_beats_dense": comparison["repaired_minus_dense_lm_loss"] < 0,
            "scorecard_regresses_vs_ean": comparison["repaired_minus_ean_lm_loss"] > 0,
            "both_structured_outliers_improved": all(row["repair_minus_ean_delta"] < 0 for row in window_rows),
            "route_stability_auxiliary_supported": False,
            "architecture_change_recommended": False,
            "next_recommended_step": "do not preserve scratch owners directly; try structured delta warmup or robust eval stratification only if needed",
        },
        "interpretation": (
            "The training-only route-stability auxiliary preserved strict Top1 execution and still beat dense on the scorecard, "
            "but it slightly regressed EAN scorecard loss and failed to improve both structured outliers. Directly matching "
            "scratch-PVR owners on high-loss structured tokens is therefore too blunt."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "structured_span_repair_decision_report.json", payload)
    lines = [
        "# EAN Structured-Span Repair Decision",
        "",
        f"Status: `{payload['status']}`",
        "",
        "| step | EAN delta | repaired delta | repair - EAN |",
        "|---:|---:|---:|---:|",
    ]
    for row in window_rows:
        lines.append(f"| {row['step']} | {row['ean_delta_vs_baseline']} | {row['repaired_delta_vs_baseline']} | {row['repair_minus_ean_delta']} |")
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    (out / "structured_span_repair_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/structured_span_repair_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/ean_structured_span_route_stability_repair_decision")
    args = parser.parse_args()
    payload = run(input_report=args.input_report, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
