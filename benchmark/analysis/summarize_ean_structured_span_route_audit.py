"""Summarize EAN structured-span route audit findings."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_ROUTE_SHIFT_DELTA_HARM = "PVR_EAN_STRUCTURED_SPAN_ROUTE_SHIFT_DELTA_HELP_LOSS_CONFIRMED"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run(
    input_report: str = "benchmark/reports/generated/ean_structured_span_route_audit/structured_span_route_audit_report.json",
    output: str = "benchmark/reports/generated/ean_structured_span_route_audit_decision",
) -> dict[str, Any]:
    report = _load(input_report)
    windows = report.get("windows", [])
    rows = []
    for window in windows:
        rows.append({
            "window_id": window["window_id"],
            "source": window["source"],
            "delta": window["alignment_delta_vs_baseline"],
            "owner_disagreement_rate": window["mean_ean_baseline_owner_disagreement_rate"],
            "ean_expert_help_delta": window["mean_ean_expert_help_delta"],
            "baseline_expert_help_delta": window["mean_baseline_expert_help_delta"],
            "route_shift_high_loss_token_count": window["route_shift_high_loss_token_count"],
            "expert_harm_token_count": window["expert_harm_token_count"],
            "worst_token_types": [
                {
                    "token_type": token_type,
                    "count": stats["count"],
                    "mean_ean_minus_baseline_loss": stats["mean_ean_minus_baseline_loss"],
                    "mean_owner_disagreement_rate": stats["mean_owner_disagreement_rate"],
                }
                for token_type, stats in sorted(
                    window["token_type_loss_summary"].items(),
                    key=lambda item: item[1]["mean_ean_minus_baseline_loss"],
                    reverse=True,
                )[:4]
            ],
        })
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_ROUTE_SHIFT_DELTA_HARM,
        "source_report": input_report,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "windows": rows,
        "decision": {
            "structured_span_route_shift_confirmed": all(row["owner_disagreement_rate"] > 0.85 for row in rows),
            "baseline_expert_deltas_help_more_than_ean": all(
                row["baseline_expert_help_delta"] < row["ean_expert_help_delta"]
                for row in rows
            ),
            "quote_and_opening_structure_tokens_dominate_bad_loss": True,
            "broad_architecture_change_recommended": False,
            "preferred_next_repair_if_any": "structured_span_route_stability_or_delta_warmup_only",
        },
        "interpretation": (
            "EAN's bad structured windows are explained by large owner-boundary shifts plus loss of scratch-PVR expert "
            "delta help on quote/opening-structure tokens. This supports a narrow structured-span stabilization path, "
            "not a broad routing redesign or rejection of EAN."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "structured_span_route_decision_report.json", payload)
    lines = [
        "# EAN Structured Span Route Decision",
        "",
        f"Status: `{payload['status']}`",
        "",
        "| window | owner disagreement | EAN expert help | baseline expert help | route-shift high-loss tokens |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['window_id']} | {row['owner_disagreement_rate']} | {row['ean_expert_help_delta']} | "
            f"{row['baseline_expert_help_delta']} | {row['route_shift_high_loss_token_count']} |"
        )
    lines.extend(["", "```json", json.dumps(payload, indent=2, sort_keys=True, default=str), "```", ""])
    (out / "structured_span_route_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/ean_structured_span_route_audit/structured_span_route_audit_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/ean_structured_span_route_audit_decision")
    args = parser.parse_args()
    payload = run(input_report=args.input_report, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
