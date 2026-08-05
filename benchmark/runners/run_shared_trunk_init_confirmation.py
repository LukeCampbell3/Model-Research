"""Confirm shared-trunk initialization as a PVR repair candidate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.runners.run_shared_approximation_bottleneck import (
    SHARED_INIT_SUPPORTED,
    _train_variant,
    _variant_config,
    summarize_matrix,
)


CANDIDATE_STATUS = "PVR_SHARED_TRUNK_INIT_REPAIR_CANDIDATE"
CONFIRMED_STATUS = "PVR_SHARED_TRUNK_INIT_CONFIRMED"
NOT_CONFIRMED_STATUS = "PVR_SHARED_TRUNK_INIT_NOT_CONFIRMED"
STATUS_300M_DENSE_GAP_CLOSED = "PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED"
STATUS_300M_REPAIR_SUPPORTED = "PVR_SHARED_TRUNK_INIT_300M_REPAIR_SUPPORTED"
STATUS_300M_NOT_SUPPORTED = "PVR_SHARED_TRUNK_INIT_300M_NOT_SUPPORTED"
STATUS_300M_INVARIANT_FAILED = "PVR_SHARED_TRUNK_INIT_300M_INVARIANT_FAILED"


def _safe_mean(values: list[Any]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return sum(xs) / len(xs) if xs else None


def _dense_reference(size: str) -> dict[str, Any]:
    comparison_path = Path(f"benchmark/reports/generated/comparison_{size}_real_4k/benchmark_comparison_report.json")
    if not comparison_path.exists():
        return {"status": "NOT_RUN_MISSING_CHECKPOINT"}
    rows = json.loads(comparison_path.read_text(encoding="utf-8")).get("rows", [])
    dense = next((row for row in rows if row.get("model") == f"dense_transformer_{size}"), None)
    if not dense:
        return {"status": "NOT_RUN_MISSING_CHECKPOINT"}
    eval_path = Path(f"benchmark/reports/generated/training_{size}_real_4k/dense_transformer_{size}/eval_curve.json")
    if eval_path.exists():
        eval_rows = json.loads(eval_path.read_text(encoding="utf-8")).get("eval_curve", [])
        dense["mean_eval_loss"] = _safe_mean([row.get("eval_loss") for row in eval_rows])
        dense["eval_window_count"] = len(eval_rows)
    return dense


def _status_for_size(size: str, summary: dict[str, Any], dense_reference: dict[str, Any]) -> str:
    if size != "300m":
        return summary["status"]
    row = summary.get("rows", {}).get("shared_trunk_init_from_dense", {})
    if not row.get("top1_invariants_clean") or not row.get("route_stable"):
        return STATUS_300M_INVARIANT_FAILED
    if not row.get("loss_supported"):
        return STATUS_300M_NOT_SUPPORTED
    init_eval = row.get("mean_eval_loss")
    dense_eval = dense_reference.get("mean_eval_loss")
    if isinstance(init_eval, (int, float)) and isinstance(dense_eval, (int, float)) and init_eval < dense_eval:
        return STATUS_300M_DENSE_GAP_CLOSED
    return STATUS_300M_REPAIR_SUPPORTED


def run_seed(
    *,
    seed: int,
    output: str,
    checkpoint_root: str,
    dense_config: str = "benchmark/configs/generated/dense_transformer_100m.yaml",
    pvr_config: str = "benchmark/configs/generated/pvr_ec_o_full_100m.yaml",
    dense_checkpoint: str | None = None,
    device: str = "cuda",
    max_steps: int = 4000,
    batch_size: int = 2,
    seq_len: int = 128,
    lr: float = 1e-5,
    eval_interval: int = 400,
    size: str | None = None,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    dense_cfg = load_json_or_yaml(dense_config)
    pvr_cfg = load_json_or_yaml(pvr_config)
    size = size or str(pvr_cfg.get("model_size_label") or "100m")
    dense_checkpoint = dense_checkpoint or str(dense_cfg.get("checkpoint_path"))
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    base_variant = str(pvr_cfg["model_variant"])
    variants = {
        "baseline": _variant_config(pvr_cfg, f"{base_variant}_baseline_seed_{seed}", checkpoint_root, output),
        "shared_trunk_init_from_dense": _variant_config(pvr_cfg, f"{base_variant}_shared_trunk_init_from_dense_seed_{seed}", checkpoint_root, output),
    }
    rows = []
    rows.append(_train_variant(
        variant_name="baseline",
        mode="baseline",
        student_config=variants["baseline"],
        dense_config=dense_cfg,
        dense_checkpoint=dense_checkpoint,
        output_root=out,
        device=device,
        seed=seed,
        max_steps=max_steps,
        batch_size=batch_size,
        seq_len=seq_len,
        lr=lr,
        eval_interval=eval_interval,
        target_steps=4000,
        target_training_tokens=1_000_000,
        target_eval_windows=10,
        gated_teacher_weight=0.0,
        gated_teacher_warmup_steps=0,
        temperature=2.0,
    ))
    rows.append(_train_variant(
        variant_name="shared_trunk_init_from_dense",
        mode="shared_trunk_init_from_dense",
        student_config=variants["shared_trunk_init_from_dense"],
        dense_config=dense_cfg,
        dense_checkpoint=dense_checkpoint,
        output_root=out,
        device=device,
        seed=seed,
        max_steps=max_steps,
        batch_size=batch_size,
        seq_len=seq_len,
        lr=lr,
        eval_interval=eval_interval,
        target_steps=4000,
        target_training_tokens=1_000_000,
        target_eval_windows=10,
        gated_teacher_weight=0.0,
        gated_teacher_warmup_steps=0,
        temperature=2.0,
    ))
    variant_names = {label: cfg["model_variant"] for label, cfg in variants.items()}
    summary = summarize_matrix(out, variant_names)
    dense_reference = _dense_reference(size)
    status = _status_for_size(size, summary, dense_reference)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "repair_status_vs_pvr_baseline": summary["status"],
        "seed": seed,
        "size": size,
        "max_steps": max_steps,
        "training_tokens_per_model": max_steps * batch_size * seq_len,
        "eval_windows": max_steps // eval_interval,
        "variant_names": variant_names,
        "dense_reference": dense_reference,
        "rows": rows,
        "summary": summary,
    }
    write_json(out / "shared_trunk_init_seed_report.json", payload)
    return payload


def aggregate(seed_reports: list[str], output: str = "benchmark/reports/generated/shared_trunk_init_confirmation_100m") -> dict[str, Any]:
    reports = [json.loads(Path(path).read_text(encoding="utf-8")) for path in seed_reports if Path(path).exists()]
    supported = [report for report in reports if report.get("status") == SHARED_INIT_SUPPORTED]
    status = CONFIRMED_STATUS if len(supported) >= 2 else CANDIDATE_STATUS if supported else NOT_CONFIRMED_STATUS
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "seed_report_paths": seed_reports,
        "seed_count": len(reports),
        "supported_seed_count": len(supported),
        "promotion_condition": "mean eval loss improves, final train loss does not materially regress, Top1 invariants remain clean, route stability remains true, and improvement survives at least one repeat seed",
        "reports": reports,
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "shared_trunk_init_confirmation_report.json", payload)
    _write_markdown(out / "shared_trunk_init_confirmation_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Shared-Trunk Init Confirmation",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"Supported seeds: `{payload['supported_seed_count']}` / `{payload['seed_count']}`",
        "",
        "| seed | status | final train delta | mean eval delta | route stable |",
        "|---:|---|---:|---:|---|",
    ]
    for report in payload["reports"]:
        row = report["summary"]["rows"].get("shared_trunk_init_from_dense", {})
        deltas = row.get("deltas", {})
        lines.append(
            f"| {report.get('seed')} | {report.get('status')} | "
            f"{deltas.get('final_train_loss_delta_vs_baseline')} | "
            f"{deltas.get('mean_eval_loss_delta_vs_baseline')} | "
            f"{row.get('route_stable')} |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run shared-trunk init confirmation seed")
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--checkpoint-root", required=True)
    parser.add_argument("--dense-config", default="benchmark/configs/generated/dense_transformer_100m.yaml")
    parser.add_argument("--pvr-config", default="benchmark/configs/generated/pvr_ec_o_full_100m.yaml")
    parser.add_argument("--dense-checkpoint", default=None)
    parser.add_argument("--size", default=None)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--max-steps", type=int, default=4000)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--seq-len", type=int, default=128)
    parser.add_argument("--eval-interval", type=int, default=400)
    args = parser.parse_args()
    payload = run_seed(
        seed=args.seed,
        output=args.output,
        checkpoint_root=args.checkpoint_root,
        dense_config=args.dense_config,
        pvr_config=args.pvr_config,
        dense_checkpoint=args.dense_checkpoint,
        size=args.size,
        device=args.device,
        max_steps=args.max_steps,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        eval_interval=args.eval_interval,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
