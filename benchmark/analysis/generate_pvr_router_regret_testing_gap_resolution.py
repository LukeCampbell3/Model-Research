"""Consolidate router-regret repair testing gaps into one decision report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


def _load(path: str) -> dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"missing": str(p)}


def _delta(right: Any, left: Any) -> float | None:
    if isinstance(right, (int, float)) and isinstance(left, (int, float)):
        return float(right) - float(left)
    return None


def run(
    *,
    output: str = "benchmark/reports/generated/pvr_router_regret_testing_gap_resolution",
) -> dict[str, Any]:
    confirmation = _load("benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation/pvr_router_repair_screen.json")
    mismatch = _load("benchmark/reports/generated/pvr_router_regret_lm_mismatch_analysis/pvr_router_regret_lm_mismatch_analysis.json")
    raw_1block = _load("benchmark/reports/generated/pvr_router_regret_full_network_alignment_audit/pvr_router_regret_full_network_alignment_audit.json")
    raw_2block = _load("benchmark/reports/generated/pvr_router_regret_full_network_alignment_audit_2block/pvr_router_regret_full_network_alignment_audit.json")
    text_only = _load("benchmark/reports/generated/pvr_router_regret_full_network_alignment_audit_text_only/pvr_router_regret_full_network_alignment_audit.json")
    greedy_baseline = _load("benchmark/reports/generated/pvr_full_network_greedy_oracle_audit_baseline_1m/pvr_full_network_greedy_oracle_audit.json")
    greedy_repair = _load("benchmark/reports/generated/pvr_full_network_greedy_oracle_audit_regret0p01_1m/pvr_full_network_greedy_oracle_audit.json")

    base_greedy = greedy_baseline.get("overall") or {}
    repair_greedy = greedy_repair.get("overall") or {}
    greedy_comparison = {
        "selected_loss_delta": _delta(repair_greedy.get("selected_loss"), base_greedy.get("selected_loss")),
        "greedy_oracle_loss_delta": _delta(
            repair_greedy.get("greedy_full_network_oracle_loss"),
            base_greedy.get("greedy_full_network_oracle_loss"),
        ),
        "mean_router_regret_delta": _delta(
            repair_greedy.get("mean_router_regret_across_block_decisions"),
            base_greedy.get("mean_router_regret_across_block_decisions"),
        ),
        "selected_is_oracle_rate_delta": _delta(
            repair_greedy.get("selected_is_oracle_rate_across_block_decisions"),
            base_greedy.get("selected_is_oracle_rate_across_block_decisions"),
        ),
        "selected_is_top2_rate_delta": _delta(
            repair_greedy.get("selected_is_top2_rate_across_block_decisions"),
            base_greedy.get("selected_is_top2_rate_across_block_decisions"),
        ),
    }

    status_labels = [
        "PVR_ROUTER_REGRET_TESTING_GAPS_RESOLVED",
        "PVR_ROUTER_REGRET_REPAIR_FINAL_BLOCK_METRIC_IMPROVEMENT_SUPPORTED",
        "PVR_ROUTER_REGRET_REPAIR_RAW_JSON_PREFIX_SUPPORTED_ONLY",
        "PVR_ROUTER_REGRET_REPAIR_RAW_JSON_TWO_BLOCK_NOT_SUPPORTED",
        "PVR_ROUTER_REGRET_REPAIR_TEXT_CONTENT_BROAD_SUPPORT_NOT_ESTABLISHED",
        "PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_REGRET_REDUCTION_NOT_SUPPORTED",
        "PVR_ROUTER_REGRET_REPAIR_REGRET0P01_DO_NOT_PROMOTE",
    ]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_TESTING_GAP_RESOLUTION",
        "status": "PVR_ROUTER_REGRET_TESTING_GAP_RESOLUTION_COMPLETE",
        "decision": "PVR_ROUTER_REGRET_REPAIR_REGRET0P01_NOT_SUPPORTED_FOR_PROMOTION",
        "status_labels": status_labels,
        "inputs": {
            "confirmation": confirmation,
            "mismatch": mismatch,
            "raw_1block": raw_1block,
            "raw_2block": raw_2block,
            "text_only": text_only,
            "greedy_baseline": greedy_baseline,
            "greedy_repair": greedy_repair,
        },
        "summary": {
            "training_eval_final_delta": (mismatch.get("key_deltas") or {}).get("final_eval_loss_delta"),
            "final_block_router_regret_delta": (mismatch.get("key_deltas") or {}).get("oracle_router_regret_delta"),
            "raw_json_1block_micro_delta": raw_1block.get("micro_delta_regret0p01_minus_baseline"),
            "raw_json_1block_file_wins": f"{raw_1block.get('file_wins_regret0p01')}/{raw_1block.get('file_count')}",
            "raw_json_2block_micro_delta": raw_2block.get("micro_delta_regret0p01_minus_baseline"),
            "raw_json_2block_file_wins": f"{raw_2block.get('file_wins_regret0p01')}/{raw_2block.get('file_count')}",
            "text_only_micro_delta": text_only.get("micro_delta_regret0p01_minus_baseline"),
            "text_only_file_wins": f"{text_only.get('file_wins_regret0p01')}/{text_only.get('file_count')}",
            "full_network_greedy_oracle_comparison": greedy_comparison,
        },
        "resolved_testing_gaps": {
            "report_or_checkpoint_inconsistency": "RESOLVED_NOT_CAUSAL; exact checkpoints, no resume events, matched tokens/windows.",
            "final_block_oracle_rate": "RESOLVED; regret0p01 improves final-block selected-is-oracle rate and final-block regret.",
            "lm_eval_reason": "RESOLVED; old four-window LM gate was under-sampled, but broader content-aware gates still do not support robust promotion.",
            "raw_json_wrapper_bias": "RESOLVED; regret0p01 strongly helps first JSONL metadata blocks but fails after content begins.",
            "official_like_text_content": "RESOLVED_MIXED; small micro improvement, only 3/7 file wins, math regression.",
            "full_network_oracle": "RESOLVED; greedy full-network oracle still shows large headroom and regret0p01 does not reduce full-network regret versus no-regret baseline.",
        },
        "recommendation": "Stop regret0p01 as a promotion candidate. If router repair continues, use lower/annealed regret weights with explicit entropy/monopoly retention and a text-field official-like micro+macro gate; do not use raw JSONL wrapper loss or four single-window eval loss as the promotion gate.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_regret_testing_gap_resolution.json", payload)
    lines = [
        "# PVR Router Regret Testing Gap Resolution",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        "## Summary",
        "",
        f"Training final-eval delta: `{payload['summary']['training_eval_final_delta']}`",
        f"Final-block router-regret delta: `{payload['summary']['final_block_router_regret_delta']}`",
        f"Raw JSON 1-block micro delta / wins: `{payload['summary']['raw_json_1block_micro_delta']}` / `{payload['summary']['raw_json_1block_file_wins']}`",
        f"Raw JSON 2-block micro delta / wins: `{payload['summary']['raw_json_2block_micro_delta']}` / `{payload['summary']['raw_json_2block_file_wins']}`",
        f"Text-only micro delta / wins: `{payload['summary']['text_only_micro_delta']}` / `{payload['summary']['text_only_file_wins']}`",
        "",
        "## Full-Network Greedy Oracle Comparison",
        "",
        "| metric | regret0p01 - baseline |",
        "|---|---:|",
    ]
    for key, value in greedy_comparison.items():
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Resolved Gaps",
            "",
            *[f"- {key}: {value}" for key, value in payload["resolved_testing_gaps"].items()],
            "",
            "## Status Labels",
            "",
            *[f"- `{item}`" for item in status_labels],
            "",
            "## Recommendation",
            "",
            payload["recommendation"],
        ]
    )
    (out / "pvr_router_regret_testing_gap_resolution.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_regret_testing_gap_resolution")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"]}, indent=2))


if __name__ == "__main__":
    main()
