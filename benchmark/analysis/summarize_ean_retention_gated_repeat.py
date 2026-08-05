"""Summarize repeat evidence for retention-gated EAN delta replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json
from benchmark.runners.run_ean_structured_delta_replay_retention_gated import (
    RETENTION_CANDIDATE,
    STATUS_SUPPORTED,
)


STATUS_REPEAT_SUPPORTED = "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_SUPPORTED"
STATUS_REPEAT_NOT_SUPPORTED = "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_NOT_SUPPORTED"


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _candidate_summary(report: dict[str, Any]) -> dict[str, Any]:
    row = report["rows"]["pvr_ean_retention_gated_delta_replay_300m"]
    ean = report["rows"]["pvr_ean_300m"]
    slices = row["slice_summary"]
    ean_slices = ean["slice_summary"]
    return {
        "seed": report.get("seed"),
        "status": report.get("status"),
        "best_step": report.get("best_step"),
        "broad_lm": slices["broad_lm"]["mean_loss"],
        "broad_delta_vs_ean": slices["broad_lm"]["mean_loss"] - ean_slices["broad_lm"]["mean_loss"],
        "code_heavy": slices["code_heavy"]["mean_loss"],
        "code_delta_vs_ean": slices["code_heavy"]["mean_loss"] - ean_slices["code_heavy"]["mean_loss"],
        "json_schema": slices["json_schema"]["mean_loss"],
        "json_delta_vs_ean": slices["json_schema"]["mean_loss"] - ean_slices["json_schema"]["mean_loss"],
        "unseen_structured": slices["unseen_structured_spans"]["mean_loss"],
        "unseen_structured_delta_vs_ean": (
            slices["unseen_structured_spans"]["mean_loss"]
            - ean_slices["unseen_structured_spans"]["mean_loss"]
        ),
        "top1_invariants_clean": row.get("top1_invariants_clean"),
        "supported_conditions": report.get("supported_conditions", {}),
        "seeded_replay_sampling": report.get("seeded_replay_sampling"),
    }


def run(
    *,
    reports: list[str],
    output: str = "benchmark/reports/generated/ean_retention_gated_delta_replay_repeat_decision",
) -> dict[str, Any]:
    loaded = [_load_json(path) for path in reports]
    summaries = [_candidate_summary(report) for report in loaded]
    seeds = {summary["seed"] for summary in summaries}
    all_supported = all(summary["status"] == STATUS_SUPPORTED for summary in summaries)
    all_top1_clean = all(summary["top1_invariants_clean"] is True for summary in summaries)
    distinct_seed_count = len(seeds)
    status = (
        STATUS_REPEAT_SUPPORTED
        if all_supported and all_top1_clean and distinct_seed_count >= 2
        else STATUS_REPEAT_NOT_SUPPORTED
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "experiment": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT",
        "candidate": RETENTION_CANDIDATE,
        "reports": reports,
        "seed_count": distinct_seed_count,
        "supported_seed_count": sum(summary["status"] == STATUS_SUPPORTED for summary in summaries),
        "all_top1_invariants_clean": all_top1_clean,
        "seed_summaries": summaries,
        "decision_rule": (
            "Repeat support requires at least two distinct seeds, each with retention-gated support status and clean Top1 invariants."
        ),
        "benchmark_evidence_caveat": (
            "Reduced repeat/promotion audit evidence only. Do not label as official broad benchmark promotion until full adapters run."
        ),
        "do_not_promote": [
            "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_OFFICIAL_PROMOTION_SUPPORTED",
            "PVR_EAN_FULL_BENCHMARK_PROMOTION_SUPPORTED",
            "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "retention_gated_delta_replay_repeat_report.json", payload)
    _write_markdown(out / "retention_gated_delta_replay_repeat_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# EAN Retention-Gated Delta Replay Repeat",
        "",
        f"Status: `{payload['status']}`",
        f"Candidate: `{payload['candidate']}`",
        "",
        "| seed | status | broad delta | code delta | json delta | unseen structured delta | Top1 clean |",
        "|---:|---|---:|---:|---:|---:|---|",
    ]
    for row in payload["seed_summaries"]:
        lines.append(
            f"| {row['seed']} | {row['status']} | {row['broad_delta_vs_ean']} | "
            f"{row['code_delta_vs_ean']} | {row['json_delta_vs_ean']} | "
            f"{row['unseen_structured_delta_vs_ean']} | {row['top1_invariants_clean']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reports", nargs="+", required=True)
    parser.add_argument("--output", default="benchmark/reports/generated/ean_retention_gated_delta_replay_repeat_decision")
    args = parser.parse_args()
    payload = run(reports=args.reports, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
