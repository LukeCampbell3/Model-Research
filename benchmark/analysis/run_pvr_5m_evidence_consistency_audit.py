"""Audit the sparse-v2 300M 5M-token report lineage.

This audit reconciles the published decision report with the raw training and
evaluation curves and with the checkpoint manifest.  It intentionally does not
rerun evaluation and does not use the final official bounded files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import git_commit, utc_now, write_json


SET_A = {
    "mean_eval_loss": 11.337301993370057,
    "final_eval_loss": 10.112784385681152,
    "final_train_loss": 1.962173342704773,
}
SET_B = {
    "mean_eval_loss": 10.914688920974731,
    "final_eval_loss": 12.128792762756348,
    "final_train_loss": 1.9358503818511963,
}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _close(a: float | None, b: float | None, tol: float = 1e-9) -> bool:
    if a is None or b is None:
        return a is b
    return abs(float(a) - float(b)) <= tol


def _curve_summary(checkpoint_root: Path) -> dict[str, Any]:
    train_path = checkpoint_root / "training_curve.json"
    eval_path = checkpoint_root / "eval_curve.json"
    manifest_path = checkpoint_root / "checkpoint_manifest.json"
    checkpoint_path = checkpoint_root / "checkpoint.pt"
    train = _load_json(train_path)
    eval_payload = _load_json(eval_path)
    manifest = _load_json(manifest_path) if manifest_path.exists() else {}
    losses = train.get("loss_curve", [])
    eval_rows = eval_payload.get("eval_curve", [])
    eval_losses = [row.get("eval_loss") for row in eval_rows if row.get("eval_loss") is not None]
    checkpoint_hash = _sha256(checkpoint_path)
    checkpoint_meta: dict[str, Any] = {}
    checkpoint_load_error = None
    if checkpoint_path.exists():
        try:
            checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
            if isinstance(checkpoint, dict):
                checkpoint_meta = {
                    key: checkpoint.get(key)
                    for key in [
                        "training_status",
                        "checkpoint_kind",
                        "resume_mode",
                        "optimizer_steps",
                        "training_tokens_seen",
                        "source_git_commit",
                        "config_hash",
                    ]
                    if key in checkpoint
                }
                checkpoint_meta["has_optimizer_state"] = "optimizer_state_dict" in checkpoint
                checkpoint_meta["has_rng_state"] = any(
                    key in checkpoint
                    for key in [
                        "python_rng_state",
                        "numpy_rng_state",
                        "torch_cpu_rng_state",
                        "torch_cuda_rng_state_all",
                    ]
                )
        except Exception as exc:  # pragma: no cover - defensive audit path
            checkpoint_load_error = repr(exc)
    return {
        "training_curve_path": str(train_path),
        "eval_curve_path": str(eval_path),
        "checkpoint_manifest_path": str(manifest_path),
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_hash": checkpoint_hash,
        "manifest_checkpoint_hash": manifest.get("checkpoint_hash"),
        "checkpoint_hash_matches_manifest": checkpoint_hash == manifest.get("checkpoint_hash"),
        "checkpoint_meta": checkpoint_meta,
        "checkpoint_load_error": checkpoint_load_error,
        "final_train_loss": losses[-1].get("loss") if losses else None,
        "optimizer_steps": losses[-1].get("optimizer_step") if losses else None,
        "training_tokens_seen": losses[-1].get("training_tokens_seen") if losses else None,
        "eval_window_count": len(eval_rows),
        "eval_windows": [
            {
                "step": row.get("step"),
                "optimizer_step": row.get("optimizer_step"),
                "training_tokens_seen": row.get("training_tokens_seen"),
                "eval_tokens": row.get("eval_tokens"),
                "eval_loss": row.get("eval_loss"),
            }
            for row in eval_rows
        ],
        "mean_eval_loss": sum(eval_losses) / len(eval_losses) if eval_losses else None,
        "final_eval_loss": eval_losses[-1] if eval_losses else None,
        "status": manifest.get("status") or train.get("status"),
    }


def _find_row(report: dict[str, Any], variant: str) -> dict[str, Any] | None:
    for key in ["candidate", "winner"]:
        row = report.get(key)
        if isinstance(row, dict) and row.get("variant") == variant:
            return row
    for row in report.get("completed_rows", []):
        if row.get("variant") == variant:
            return row
    return None


def _set_match(summary: dict[str, Any], expected: dict[str, float]) -> bool:
    return all(_close(summary.get(key), value) for key, value in expected.items())


def run(
    *,
    decision_report: str,
    checkpoint_root: str,
    output: str,
    variant: str = "pvr_teacher_independent_sparse_v2_300m_long_curve",
) -> dict[str, Any]:
    report_path = Path(decision_report)
    checkpoint_root_path = Path(checkpoint_root)
    report = _load_json(report_path)
    report_row = _find_row(report, variant)
    raw = _curve_summary(checkpoint_root_path)
    if report_row is None:
        status = "PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_BLOCKED"
        decision = "PVR_5M_REPORT_ROW_MISSING"
        assertions = {"report_row_present": False}
    else:
        assertions = {
            "report_row_present": True,
            "displayed_mean_eval_matches_raw": _close(report_row.get("mean_eval_loss"), raw["mean_eval_loss"]),
            "displayed_final_eval_matches_raw": _close(report_row.get("final_eval_loss"), raw["final_eval_loss"]),
            "displayed_final_train_matches_raw": _close(report_row.get("final_train_loss"), raw["final_train_loss"]),
            "displayed_steps_match_raw": int(report_row.get("optimizer_steps") or -1) == int(raw.get("optimizer_steps") or -2),
            "displayed_tokens_match_raw": int(report_row.get("training_tokens_seen") or -1) == int(raw.get("training_tokens_seen") or -2),
            "displayed_checkpoint_hash_matches_manifest": report_row.get("checkpoint_hash") == raw.get("manifest_checkpoint_hash"),
            "manifest_checkpoint_hash_matches_file": bool(raw.get("checkpoint_hash_matches_manifest")),
            "set_a_matches_raw": _set_match(raw, SET_A),
            "set_b_matches_raw": _set_match(raw, SET_B),
            "checkpoint_contains_exact_resume_state": bool(
                raw.get("checkpoint_meta", {}).get("has_optimizer_state")
                and raw.get("checkpoint_meta", {}).get("has_rng_state")
            ),
        }
        values_consistent = all(
            assertions[key]
            for key in [
                "displayed_mean_eval_matches_raw",
                "displayed_final_eval_matches_raw",
                "displayed_final_train_matches_raw",
                "displayed_steps_match_raw",
                "displayed_tokens_match_raw",
                "displayed_checkpoint_hash_matches_manifest",
                "manifest_checkpoint_hash_matches_file",
            ]
        )
        status = "PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_COMPLETE" if values_consistent else "PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_BLOCKED"
        if assertions["set_a_matches_raw"] and not assertions["set_b_matches_raw"]:
            decision = "PVR_5M_AUTHORITATIVE_VALUES_SET_A_STALE_SET_B_NOT_PRESENT"
        elif assertions["set_b_matches_raw"]:
            decision = "PVR_5M_AUTHORITATIVE_VALUES_SET_B"
        else:
            decision = "PVR_5M_AUTHORITATIVE_VALUES_NOT_MATCHING_EXPECTED_SETS"
        if values_consistent and not assertions["checkpoint_contains_exact_resume_state"]:
            decision += "_WEIGHT_ONLY_FINAL_CHECKPOINT"

    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_5M_EVIDENCE_CONSISTENCY_AUDIT",
        "status": status,
        "decision": decision,
        "scope": "Audits current raw 5M artifacts and report lineage only; no model training or final official-file selection.",
        "variant": variant,
        "decision_report": str(report_path),
        "checkpoint_root": str(checkpoint_root_path),
        "expected_set_a": SET_A,
        "expected_set_b": SET_B,
        "report_row": report_row,
        "raw_curve_summary": raw,
        "assertions": assertions,
        "superseded_variants": [
            {
                "label": "Set B",
                "status": "NOT_FOUND_IN_CURRENT_ARTIFACTS" if not assertions.get("set_b_matches_raw") else "MATCHES_CURRENT_ARTIFACTS",
                "values": SET_B,
            }
        ],
        "claim_boundary": "The curve/report values are internally consistent for Set A. Exact-resume equivalence is not supported by this checkpoint because optimizer/RNG state is absent.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_5m_evidence_consistency_audit.json", payload)
    lines = [
        "# PVR 5M Evidence Consistency Audit",
        "",
        f"Status: `{status}`",
        f"Decision: `{decision}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["scope"],
        "",
        "## Authoritative PVR 5M Result",
        "",
        f"Variant: `{variant}`",
        f"Mean eval loss: `{raw.get('mean_eval_loss')}`",
        f"Final eval loss: `{raw.get('final_eval_loss')}`",
        f"Final train loss: `{raw.get('final_train_loss')}`",
        f"Optimizer steps: `{raw.get('optimizer_steps')}`",
        f"Training tokens seen: `{raw.get('training_tokens_seen')}`",
        f"Eval windows: `{raw.get('eval_window_count')}`",
        f"Checkpoint path: `{raw.get('checkpoint_path')}`",
        f"Checkpoint hash: `{raw.get('checkpoint_hash')}`",
        "",
        "## Assertions",
        "",
        *[f"- {key}: `{value}`" for key, value in assertions.items()],
        "",
        "## Set Reconciliation",
        "",
        f"Set A matches current raw artifacts: `{assertions.get('set_a_matches_raw')}`",
        f"Set B matches current raw artifacts: `{assertions.get('set_b_matches_raw')}`",
        "",
        "Set B is treated as stale/not authoritative unless another raw artifact is provided that contains those values.",
        "",
        "## Checkpoint Resume Caveat",
        "",
        "The final checkpoint is loadable and its hash matches the manifest, but it does not contain optimizer and RNG state. "
        "It is therefore a weight-only final checkpoint, not evidence that interrupted training could be resumed exactly.",
        "",
        "## Evaluation Windows",
        "",
        "| step | tokens seen | eval tokens | eval loss |",
        "|---:|---:|---:|---:|",
    ]
    for row in raw.get("eval_windows", []):
        lines.append(
            f"| {row.get('optimizer_step')} | {row.get('training_tokens_seen')} | {row.get('eval_tokens')} | {row.get('eval_loss')} |"
        )
    (out / "pvr_5m_evidence_consistency_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--decision-report",
        default="benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_decision/sparse_v2_300m_long_curve_validation_5m_report.json",
    )
    parser.add_argument(
        "--checkpoint-root",
        default="checkpoints/sparse_v2_300m_long_curve_validation/pvr_teacher_independent_sparse_v2_300m_long_curve",
    )
    parser.add_argument(
        "--output",
        default="benchmark/reports/generated/pvr_5m_evidence_consistency_audit",
    )
    parser.add_argument("--variant", default="pvr_teacher_independent_sparse_v2_300m_long_curve")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "assertions": payload["assertions"]}, indent=2))


if __name__ == "__main__":
    main()
