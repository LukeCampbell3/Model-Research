"""Freeze the reduced-audit status for retention-gated EAN delta replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


FROZEN_CANDIDATE = "pvr_ec_o_ean_retention_gated_delta_replay_v1"
FROZEN_STATUS = "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_SUPPORTED"

DEFAULT_REPEAT_REPORT = "benchmark/reports/generated/ean_retention_gated_delta_replay_repeat_decision/retention_gated_delta_replay_repeat_report.json"
DEFAULT_CONFIG = "benchmark/configs/generated/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m.yaml"


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def run(
    *,
    repeat_report: str = DEFAULT_REPEAT_REPORT,
    candidate_config: str = DEFAULT_CONFIG,
    output: str = "benchmark/reports/generated/pvr_ec_o_ean_retention_gated_delta_replay_v1_candidate",
) -> dict[str, Any]:
    repeat = _load_json(repeat_report)
    config = _load_json(candidate_config)
    seed_summaries = repeat.get("seed_summaries", [])
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "candidate": FROZEN_CANDIDATE,
        "status": FROZEN_STATUS if repeat.get("status") == FROZEN_STATUS else "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FREEZE_BLOCKED",
        "candidate_config": candidate_config,
        "canonical_checkpoint_path": config.get("checkpoint_path"),
        "repeat_report": repeat_report,
        "supported_claim": (
            "At 300M, EAN initialization plus retention-gated structured expert-delta replay preserves or improves "
            "EAN broad/prose behavior, improves code/JSON structured slices, improves unseen structured spans, "
            "survives two replay-sampling seeds, and preserves strict Top1 invariants under the reduced repeat/promotion audit."
        ),
        "promoted_statuses": [
            "PVR_EAN_INIT_300M_SCORECARD_BROADLY_SUPPORTED",
            "PVR_EAN_STRUCTURED_SPAN_ROUTE_SHIFT_DELTA_HELP_LOSS_CONFIRMED",
            "PVR_EAN_STRUCTURED_SPAN_ROUTE_STABILITY_REPAIR_NOT_SUPPORTED",
            "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SHORT_REPLAY_SUPPORTED",
            "PVR_EAN_DELTA_REPLAY_GENERALIZATION_AUDIT_SUPPORTED",
            "PVR_EAN_DELTA_REPLAY_PROMOTION_AUDIT_NOT_SUPPORTED",
            "PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED",
            "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_SUPPORTED",
        ],
        "caveated_status": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_REDUCED_AUDIT_SUPPORTED",
        "do_not_promote": [
            "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_OFFICIAL_PROMOTION_SUPPORTED",
            "PVR_EAN_FULL_BENCHMARK_PROMOTION_SUPPORTED",
            "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
            "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
            "PVR_OFFICIAL_CODE_BENCH_SUPPORTED",
        ],
        "next_milestone": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT",
        "repeat_seed_count": repeat.get("seed_count"),
        "supported_seed_count": repeat.get("supported_seed_count"),
        "all_top1_invariants_clean": repeat.get("all_top1_invariants_clean"),
        "seed_summaries": seed_summaries,
        "benchmark_evidence_caveat": (
            "This is reduced repeat/promotion audit support. Official broad NLP/code benchmark support remains blocked "
            "until full adapters and full benchmark promotion audit run."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "candidate_status_report.json", payload)
    _write_markdown(out / "candidate_status_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# PVR-EC-O EAN Retention-Gated Delta Replay v1",
        "",
        f"Candidate: `{payload['candidate']}`",
        f"Status: `{payload['status']}`",
        f"Caveat: `{payload['caveated_status']}`",
        "",
        payload["supported_claim"],
        "",
        "## Seed Summary",
        "",
        "| seed | broad delta | code delta | json delta | unseen structured delta | Top1 clean |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in payload["seed_summaries"]:
        lines.append(
            f"| {row['seed']} | {row['broad_delta_vs_ean']} | {row['code_delta_vs_ean']} | "
            f"{row['json_delta_vs_ean']} | {row['unseen_structured_delta_vs_ean']} | "
            f"{row['top1_invariants_clean']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeat-report", default=DEFAULT_REPEAT_REPORT)
    parser.add_argument("--candidate-config", default=DEFAULT_CONFIG)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_ec_o_ean_retention_gated_delta_replay_v1_candidate")
    args = parser.parse_args()
    payload = run(repeat_report=args.repeat_report, candidate_config=args.candidate_config, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
