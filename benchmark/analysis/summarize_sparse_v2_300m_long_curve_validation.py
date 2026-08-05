"""Summarize the 300M 5M-token long-curve validation rung."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import utc_now, write_json


COMPLETED_ROOTS = [
    "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m/dense_sparse_v2_300m_matched_long_curve",
    "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m/switch_top1_sparse_v2_300m_matched_long_curve",
    "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m/generic_top2_sparse_v2_300m_matched_long_curve",
    "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_pvr_current/pvr_teacher_independent_sparse_v2_300m_long_curve",
]

FAILED_ROOTS = [
    "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_pvr_aux0005/pvr_teacher_independent_sparse_v2_300m_aux0005_long_curve",
]


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _row(root: str) -> dict[str, Any]:
    path = Path(root)
    training = _load(path / "training_curve.json")
    eval_curve = _load(path / "eval_curve.json")
    manifest = _load(path / "checkpoint_manifest.json")
    train_rows = training.get("loss_curve") or []
    eval_rows = eval_curve.get("eval_curve") or []
    eval_losses = [row["eval_loss"] for row in eval_rows if row.get("eval_loss") is not None]
    return {
        "variant": path.name,
        "status": manifest.get("status") or training.get("status"),
        "optimizer_steps": manifest.get("optimizer_steps") or (train_rows[-1].get("step") if train_rows else 0),
        "training_tokens_seen": manifest.get("training_tokens_seen") or (train_rows[-1].get("tokens_seen") if train_rows else 0),
        "eval_window_count": manifest.get("eval_window_count") if manifest.get("eval_window_count") is not None else len(eval_rows),
        "final_train_loss": train_rows[-1]["loss"] if train_rows else None,
        "final_eval_loss": eval_losses[-1] if eval_losses else None,
        "mean_eval_loss": sum(eval_losses) / len(eval_losses) if eval_losses else None,
        "checkpoint_hash": manifest.get("checkpoint_hash"),
        "checkpoint_status_caveat": (
            "PVR final checkpoint metadata is inconsistent after timeout; curve/report artifacts are used for evidence."
            if path.name == "pvr_teacher_independent_sparse_v2_300m_long_curve"
            else ""
        ),
    }


def run(output: str = "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_decision") -> dict[str, Any]:
    completed = [_row(root) for root in COMPLETED_ROOTS]
    failed = [_row(root) for root in FAILED_ROOTS]
    ranked = sorted([row for row in completed if row["mean_eval_loss"] is not None], key=lambda row: row["mean_eval_loss"])
    candidate = next((row for row in completed if row["variant"] == "pvr_teacher_independent_sparse_v2_300m_long_curve"), {})
    winner = ranked[0] if ranked else {}
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_SPARSE_V2_300M_LONG_CURVE_VALIDATION_5M",
        "status": "PVR_300M_5M_LONG_CURVE_VALIDATION_COMPLETE_WITH_AUX_FAILURE",
        "scope": "5,000,192 training tokens/model for completed rows; train on broad_nlp_train, eval on official_like_dev. Final official bounded files not used.",
        "completed_rows": ranked,
        "failed_rows": failed,
        "winner": winner,
        "candidate": candidate,
        "decision": "PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_NOT_SUPPORTED",
        "claim_gates": {
            "all_main_baselines_completed": len(completed) == 4,
            "pvr_current_completed_5m": candidate.get("optimizer_steps") == 4883 and candidate.get("training_tokens_seen") == 5000192,
            "pvr_current_best_mean_eval": winner.get("variant") == "pvr_teacher_independent_sparse_v2_300m_long_curve",
            "official_final_files_used": False,
            "aux0005_valid": False,
        },
        "interpretation": "Current teacher-independent PVR reaches dense-like train loss but has worse official-like dev mean eval than dense, Switch, and generic Top2 at the 5M-token rung.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_v2_300m_long_curve_validation_5m_report.json", payload)
    lines = [
        "# Sparse-v2 300M 5M Long-Curve Validation",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        "",
        payload["scope"],
        "",
        "## Completed Rows",
        "",
        "| rank | variant | mean eval | final eval | final train | steps | tokens |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    for idx, row in enumerate(ranked, 1):
        lines.append(
            f"| {idx} | {row['variant']} | {row['mean_eval_loss']} | {row['final_eval_loss']} | "
            f"{row['final_train_loss']} | {row['optimizer_steps']} | {row['training_tokens_seen']} |"
        )
    lines.extend([
        "",
        "## Failed/Invalid Rows",
        "",
        "| variant | status | steps | tokens | eval windows | reason |",
        "|---|---|---:|---:|---:|---|",
    ])
    for row in failed:
        lines.append(
            f"| {row['variant']} | {row['status']} | {row['optimizer_steps']} | {row['training_tokens_seen']} | "
            f"{row['eval_window_count']} | invalid/no eval windows |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        payload["interpretation"],
    ])
    (out / "sparse_v2_300m_long_curve_validation_5m_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_decision")
    args = parser.parse_args()
    payload = run(args.output)
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
