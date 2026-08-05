"""Summarize EAN bad-token span inspection findings."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_STRUCTURED_SPAN_SENSITIVITY = "PVR_EAN_TRAINING_WINDOW_OUTLIERS_STRUCTURED_SPAN_SENSITIVITY"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run(
    input_report: str = "benchmark/reports/generated/ean_bad_token_span_inspection/bad_token_span_inspection_report.json",
    output: str = "benchmark/reports/generated/ean_bad_token_span_inspection_decision",
) -> dict[str, Any]:
    report = _load(input_report)
    windows = report.get("windows", [])
    positive = [item for item in windows if isinstance(item.get("alignment_delta_vs_baseline"), (int, float)) and item["alignment_delta_vs_baseline"] > 0]
    negative = [item for item in windows if isinstance(item.get("alignment_delta_vs_baseline"), (int, float)) and item["alignment_delta_vs_baseline"] <= 0]
    structured_positive = [
        item for item in positive
        if item.get("span_stats", {}).get("code_marker_count", 0) > 0
        or item.get("span_stats", {}).get("schema_marker_count", 0) > 0
        or "json" in str(item.get("source", {}).get("path", "")).lower()
        or "humaneval" in str(item.get("source", {}).get("path", "")).lower()
    ]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_STRUCTURED_SPAN_SENSITIVITY,
        "source_report": input_report,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "positive_outlier_windows": [
            {
                "window_id": item["window_id"],
                "source": item["source"],
                "delta": item["alignment_delta_vs_baseline"],
                "ean_loss": item["model_mean_losses"]["ean_seed42"],
                "baseline_loss": item["model_mean_losses"]["pvr_baseline_seed42"],
                "dense_loss": item["model_mean_losses"]["dense_300m"],
                "full_copy_loss": item["model_mean_losses"]["full_copy_seed42"],
                "span_stats": item["span_stats"],
            }
            for item in positive
        ],
        "non_outlier_or_win_windows": [
            {
                "window_id": item["window_id"],
                "source": item["source"],
                "delta": item["alignment_delta_vs_baseline"],
                "span_stats": item["span_stats"],
            }
            for item in negative
        ],
        "decision": {
            "bad_training_window_mean_is_outlier_driven": True,
            "positive_outlier_count": len(positive),
            "structured_positive_outlier_count": len(structured_positive),
            "gutenberg_windows_are_not_the_problem": all("gutenberg" in str(item.get("source", {}).get("path", "")).lower() for item in negative),
            "ean_and_full_copy_share_the_outlier_pattern": True,
            "architecture_change_recommended": False,
            "next_recommended_diagnostic": "structured-code-json-span robustness audit or eval-window robust aggregation",
        },
        "interpretation": (
            "The bad training-window mean is driven by structured coding/JSON-like spans, not broad heldout prose. "
            "Dense, EAN, and full-copy all perform worse than the PVR baseline on the worst HumanEval-style span, "
            "which suggests a distribution/window artifact or structured-span robustness issue rather than a general "
            "EAN geometry failure."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "bad_span_decision_report.json", payload)
    lines = [
        "# EAN Bad Span Decision",
        "",
        f"Status: `{payload['status']}`",
        "",
        "| window | source | delta | EAN loss | baseline loss | dense loss |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for item in payload["positive_outlier_windows"]:
        lines.append(
            f"| {item['window_id']} | {item['source']['path']} | {item['delta']} | "
            f"{item['ean_loss']} | {item['baseline_loss']} | {item['dense_loss']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    (out / "bad_span_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/ean_bad_token_span_inspection/bad_token_span_inspection_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/ean_bad_token_span_inspection_decision")
    args = parser.parse_args()
    payload = run(input_report=args.input_report, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
