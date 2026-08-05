"""Summarize EAN structured-span delta adaptation sweep."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_SUPPORTED = "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SHORT_REPLAY_SUPPORTED"
STATUS_OVERFIT_LONGER_REPLAY = "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_LONGER_REPLAY_OVERFITS"


DEFAULT_REPORTS = [
    "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps100/structured_span_delta_adaptation_report.json",
    "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/structured_span_delta_adaptation_report.json",
    "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42/structured_span_delta_adaptation_report.json",
]


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _row(path: str) -> dict[str, Any]:
    report = _load(path)
    comparison = report["comparison"]
    windows = report["structured_windows"]["windows"]
    return {
        "source_report": path,
        "status": report["status"],
        "optimizer_steps": report["row"]["optimizer_steps"],
        "training_tokens_seen": report["row"]["training_tokens_seen"],
        "lm_loss": comparison["repaired_lm_loss"],
        "repaired_minus_ean_lm_loss": comparison["repaired_minus_ean_lm_loss"],
        "repaired_minus_dense_lm_loss": comparison["repaired_minus_dense_lm_loss"],
        "repaired_minus_baseline_lm_loss": comparison["repaired_minus_baseline_lm_loss"],
        "repaired_minus_baseline_mean_eval_loss": comparison["repaired_minus_baseline_mean_eval_loss"],
        "top1_invariants_clean": comparison["top1_invariants_clean"],
        "structured_outliers_improved": comparison["structured_outliers_improved"],
        "scorecard_preserved_within_0_01": comparison["scorecard_preserved_within_0_01"],
        "structured_window_deltas": {
            step: {
                "ean_delta_vs_baseline": rows["ean_seed42"]["delta_vs_baseline"],
                "repaired_delta_vs_baseline": rows["repaired_ean"]["delta_vs_baseline"],
                "repair_minus_ean_delta": rows["repaired_ean"]["delta_vs_baseline"] - rows["ean_seed42"]["delta_vs_baseline"],
            }
            for step, rows in windows.items()
        },
    }


def run(
    reports: list[str] | None = None,
    output: str = "benchmark/reports/generated/ean_structured_span_delta_adaptation_sweep_decision",
) -> dict[str, Any]:
    rows = sorted([_row(path) for path in (reports or DEFAULT_REPORTS)], key=lambda item: item["optimizer_steps"])
    supported = [
        row for row in rows
        if row["top1_invariants_clean"]
        and row["structured_outliers_improved"]
        and row["scorecard_preserved_within_0_01"]
        and row["repaired_minus_dense_lm_loss"] < 0
    ]
    longer_overfit = [
        row for row in rows
        if row["structured_outliers_improved"] and not row["scorecard_preserved_within_0_01"]
    ]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_SUPPORTED if supported else STATUS_OVERFIT_LONGER_REPLAY if longer_overfit else "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SWEEP_NOT_SUPPORTED",
        "secondary_status": STATUS_OVERFIT_LONGER_REPLAY if longer_overfit else None,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation",
        "rows": rows,
        "best_supported": supported[0] if supported else None,
        "decision": {
            "short_replay_supported": bool(supported),
            "longer_replay_overfits_broad_scorecard": bool(longer_overfit),
            "owner_preservation_still_not_supported": True,
            "architecture_change_recommended": False,
            "recommended_recipe": "EAN init + short structured expert-delta replay; stop early before scorecard drift",
        },
        "interpretation": (
            "Short structured expert-delta replay recovers the bad code/JSON spans while preserving or slightly improving "
            "the EAN scorecard. Longer replay continues improving structured windows but overfits the replay distribution "
            "and regresses broad LM scorecard."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "delta_adaptation_sweep_decision_report.json", payload)
    lines = [
        "# EAN Structured Delta Adaptation Sweep",
        "",
        f"Status: `{payload['status']}`",
        f"Secondary: `{payload.get('secondary_status')}`",
        "",
        "| steps | status | LM loss | vs EAN | vs dense | structured improved |",
        "|---:|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['optimizer_steps']} | {row['status']} | {row['lm_loss']} | "
            f"{row['repaired_minus_ean_lm_loss']} | {row['repaired_minus_dense_lm_loss']} | "
            f"{row['structured_outliers_improved']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    (out / "delta_adaptation_sweep_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reports", nargs="*", default=None)
    parser.add_argument("--output", default="benchmark/reports/generated/ean_structured_span_delta_adaptation_sweep_decision")
    args = parser.parse_args()
    payload = run(reports=args.reports, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
