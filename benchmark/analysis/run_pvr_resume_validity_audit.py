"""Audit resume validity for sparse-v2 300M 5M-token artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import git_commit, utc_now, write_json


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


def _checkpoint_meta(path: Path) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        return {"exists": False}
    out: dict[str, Any] = {"exists": True, "sha256": _sha256(path)}
    try:
        checkpoint = torch.load(path, map_location="cpu", weights_only=False)
    except Exception as exc:  # pragma: no cover - defensive audit path
        out["load_error"] = repr(exc)
        return out
    if not isinstance(checkpoint, dict):
        out["checkpoint_kind"] = "RAW_STATE_DICT_OR_UNKNOWN"
        return out
    out.update(
        {
            "training_status": checkpoint.get("training_status"),
            "checkpoint_kind": checkpoint.get("checkpoint_kind") or "WEIGHT_ONLY_LEGACY",
            "resume_mode": checkpoint.get("resume_mode"),
            "optimizer_steps": checkpoint.get("optimizer_steps"),
            "training_tokens_seen": checkpoint.get("training_tokens_seen"),
            "has_model_state": "model_state_dict" in checkpoint,
            "has_optimizer_state": "optimizer_state_dict" in checkpoint,
            "has_scheduler_state": "scheduler_state_dict" in checkpoint,
            "has_scaler_state": "scaler_state_dict" in checkpoint,
            "has_python_rng_state": "python_rng_state" in checkpoint,
            "has_numpy_rng_state": "numpy_rng_state" in checkpoint,
            "has_torch_cpu_rng_state": "torch_cpu_rng_state" in checkpoint,
            "has_torch_cuda_rng_state": "torch_cuda_rng_state_all" in checkpoint,
            "source_git_commit": checkpoint.get("source_git_commit"),
            "config_hash": checkpoint.get("config_hash"),
        }
    )
    out["exact_resume_capable"] = bool(
        out["has_model_state"]
        and out["has_optimizer_state"]
        and out["has_python_rng_state"]
        and out["has_torch_cpu_rng_state"]
    )
    out["weight_only"] = bool(out["has_model_state"] and not out["has_optimizer_state"])
    return out


def _row_to_audit(row: dict[str, Any], report_root_hint: Path | None = None) -> dict[str, Any]:
    checkpoint_path = Path(row.get("checkpoint_path") or "__missing_checkpoint_path__")
    if (not checkpoint_path.exists() or not checkpoint_path.is_file()) and row.get("checkpoint_manifest"):
        manifest = _load_json(Path(row["checkpoint_manifest"]))
        checkpoint_path = Path(manifest.get("checkpoint_path") or checkpoint_path)
    if (not checkpoint_path.exists() or not checkpoint_path.is_file()) and report_root_hint is not None:
        candidate = report_root_hint / str(row.get("variant", row.get("model_variant", ""))) / "checkpoint_manifest.json"
        if candidate.exists():
            manifest = _load_json(candidate)
            checkpoint_path = Path(manifest.get("checkpoint_path") or checkpoint_path)
    meta = _checkpoint_meta(checkpoint_path)
    if row.get("status") == "TRAINING_FAILED":
        validity = "TRAINING_FAILED_NON_COMPARABLE"
    elif meta.get("exact_resume_capable"):
        validity = "EXACT_RESUME_STATE_AVAILABLE"
    elif meta.get("weight_only"):
        validity = "WEIGHT_ONLY_CHECKPOINT_NON_EQUIVALENT_FOR_EXACT_RESUME"
    else:
        validity = "RESUME_STATE_UNKNOWN_OR_MISSING"
    return {
        "variant": row.get("variant") or row.get("model_variant"),
        "status": row.get("status"),
        "optimizer_steps": row.get("optimizer_steps"),
        "training_tokens_seen": row.get("training_tokens_seen"),
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_hash_reported": row.get("checkpoint_hash"),
        "checkpoint_metadata": meta,
        "resume_validity": validity,
    }


def run(
    *,
    decision_report: str,
    output: str,
    pvr_report_root: str = "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_pvr_current",
) -> dict[str, Any]:
    report = _load_json(Path(decision_report))
    report_root_hint = Path(pvr_report_root)
    rows = []
    for row in report.get("completed_rows", []):
        rows.append(_row_to_audit(row, report_root_hint))
    for row in report.get("failed_rows", []):
        rows.append(_row_to_audit(row, report_root_hint))
    exact_rows = [row for row in rows if row["resume_validity"] == "EXACT_RESUME_STATE_AVAILABLE"]
    weight_only_rows = [row for row in rows if row["resume_validity"] == "WEIGHT_ONLY_CHECKPOINT_NON_EQUIVALENT_FOR_EXACT_RESUME"]
    failed_rows = [row for row in rows if row["resume_validity"] == "TRAINING_FAILED_NON_COMPARABLE"]
    if exact_rows and not weight_only_rows:
        status = "PVR_EXACT_RESUME_VALIDATION_SUPPORTED"
    elif weight_only_rows:
        status = "PVR_WEIGHT_ONLY_RESUME_NON_EQUIVALENT_CONFIRMED"
    else:
        status = "PVR_RESUME_VALIDITY_AUDIT_BLOCKED"
    comparison_status = (
        "PVR_5M_COMPARISON_HAS_WEIGHT_ONLY_CHECKPOINT_CAVEAT"
        if weight_only_rows
        else "PVR_5M_COMPARISON_EXACT_RESUME_METADATA_AVAILABLE"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_RESUME_VALIDITY_AUDIT",
        "status": status,
        "comparison_status": comparison_status,
        "decision_report": decision_report,
        "rows": rows,
        "assertions": {
            "exact_resume_state_available_for_all_completed_rows": len(exact_rows) == len([r for r in rows if r["status"] == "GENUINE_REDUCED_TRAINING_COMPLETE"]),
            "weight_only_resume_non_equivalent_confirmed": bool(weight_only_rows),
            "failed_rows_non_comparable": bool(failed_rows),
        },
        "interpretation": "Legacy final checkpoints are loadable for evaluation but do not contain enough optimizer/RNG state to prove exact interrupted continuation.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_resume_validity_audit.json", payload)
    lines = [
        "# PVR Resume Validity Audit",
        "",
        f"Status: `{status}`",
        f"Comparison status: `{comparison_status}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["interpretation"],
        "",
        "| variant | run status | steps | tokens | resume validity | checkpoint kind | has optimizer | has RNG |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        meta = row["checkpoint_metadata"]
        has_rng = bool(meta.get("has_python_rng_state") and meta.get("has_torch_cpu_rng_state"))
        lines.append(
            f"| {row['variant']} | {row['status']} | {row['optimizer_steps']} | {row['training_tokens_seen']} | "
            f"{row['resume_validity']} | {meta.get('checkpoint_kind')} | {meta.get('has_optimizer_state')} | {has_rng} |"
        )
    lines.extend(
        [
            "",
            "## Required Interpretation",
            "",
            "- Weight-only checkpoints may be evaluated as final weights.",
            "- Weight-only checkpoints must not be reported as exact Adam-style continuation evidence.",
            "- Any future interrupted run must restore optimizer, scheduler/scaler where applicable, RNG state, step, tokens, config hash, and source commit.",
        ]
    )
    (out / "pvr_resume_validity_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--decision-report",
        default="benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_decision/sparse_v2_300m_long_curve_validation_5m_report.json",
    )
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_resume_validity_audit")
    parser.add_argument("--pvr-report-root", default="benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_pvr_current")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "assertions": payload["assertions"]}, indent=2))


if __name__ == "__main__":
    main()
