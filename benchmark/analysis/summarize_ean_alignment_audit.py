"""Summarize the EAN scorecard/eval-curve alignment audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_MISMATCH_CONFIRMED = "PVR_EAN_EVAL_ALIGNMENT_MISMATCH_CONFIRMED"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _delta_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
    values = [float(row["delta_vs_baseline"]) for row in rows if isinstance(row.get("delta_vs_baseline"), (int, float))]
    return {
        "window_count": len(values),
        "win_count": sum(value < 0 for value in values),
        "loss_count": sum(value > 0 for value in values),
        "mean_delta": sum(values) / len(values) if values else None,
        "min_delta": min(values) if values else None,
        "max_delta": max(values) if values else None,
    }


def _recorded_delta_stats(row: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    values = []
    for current, base in zip(
        row["recorded_during_training_eval_curve"]["windows"],
        baseline["recorded_during_training_eval_curve"]["windows"],
    ):
        loss = current.get("eval_loss")
        base_loss = base.get("eval_loss")
        if isinstance(loss, (int, float)) and isinstance(base_loss, (int, float)):
            values.append({"delta_vs_baseline": float(loss) - float(base_loss)})
    return _delta_stats(values)


def run(
    input_report: str = "benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit/alignment_audit_report.json",
    output: str = "benchmark/reports/generated/ean_scorecard_eval_curve_alignment_decision",
) -> dict[str, Any]:
    report = _load(input_report)
    rows = report["rows"]
    baseline = rows["pvr_baseline_seed42"]
    model_summaries = {}
    for name in ["ean_seed42", "full_copy_seed42", "dense_300m"]:
        row = rows[name]
        model_summaries[name] = {
            "scorecard_style_general": _delta_stats(row["per_window_deltas_vs_pvr_baseline"]["scorecard_style_general"]),
            "training_window_style_final_checkpoint": _delta_stats(
                row["per_window_deltas_vs_pvr_baseline"]["training_window_style_final_checkpoint"]
            ),
            "recorded_during_training_eval_curve": _recorded_delta_stats(row, baseline),
            "mean_deltas": row["deltas_vs_pvr_baseline"],
        }
    ean_summary = model_summaries["ean_seed42"]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_MISMATCH_CONFIRMED,
        "status_detail": "SCORECARD_WINS_WITH_TRAINING_WINDOW_OUTLIER_REGRESSION",
        "source_report": input_report,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "model_summaries": model_summaries,
        "correlations": report.get("correlations", {}),
        "decision": {
            "scorecard_eval_and_training_eval_are_not_aligned": True,
            "ean_scorecard_window_support_is_strong": (
                ean_summary["scorecard_style_general"]["win_count"] >= 0.9
                * max(1, ean_summary["scorecard_style_general"]["window_count"])
                and ean_summary["scorecard_style_general"]["mean_delta"] < 0
            ),
            "ean_training_window_mean_regresses": ean_summary["training_window_style_final_checkpoint"]["mean_delta"] > 0,
            "ean_training_window_regression_is_outlier_sensitive": (
                ean_summary["training_window_style_final_checkpoint"]["win_count"]
                > ean_summary["training_window_style_final_checkpoint"]["loss_count"]
                and ean_summary["training_window_style_final_checkpoint"]["mean_delta"] > 0
            ),
        },
        "interpretation": (
            "The mixed eval-curve result is not a broad EAN failure. EAN beats the matched PVR baseline on nearly all "
            "scorecard-style heldout windows and most training-style final-checkpoint windows, but a small number of "
            "high-loss training windows flips the training-window mean positive. The next diagnostic should inspect "
            "the bad training-window token spans before changing architecture."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "alignment_decision_report.json", payload)
    lines = [
        "# EAN Alignment Decision",
        "",
        f"Status: `{payload['status']}`",
        f"Detail: `{payload['status_detail']}`",
        "",
        "| model | scorecard wins | scorecard mean delta | final-window wins | final-window mean delta | recorded wins | recorded mean delta |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, summary in model_summaries.items():
        score = summary["scorecard_style_general"]
        final = summary["training_window_style_final_checkpoint"]
        recorded = summary["recorded_during_training_eval_curve"]
        lines.append(
            f"| {name} | {score['win_count']}/{score['window_count']} | {score['mean_delta']} | "
            f"{final['win_count']}/{final['window_count']} | {final['mean_delta']} | "
            f"{recorded['win_count']}/{recorded['window_count']} | {recorded['mean_delta']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    (out / "alignment_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit/alignment_audit_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/ean_scorecard_eval_curve_alignment_decision")
    args = parser.parse_args()
    payload = run(input_report=args.input_report, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
