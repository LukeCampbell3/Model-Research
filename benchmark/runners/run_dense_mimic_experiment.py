"""Run a matched dense-teacher mimic diagnostic for PVR-EC-O.

This runner tests the recommendation "dense approximation first, routing
specialization second" without changing the main benchmark gate. It trains two
fresh PVR students under the same budget:

* baseline: standard LM loss
* dense_mimic: LM loss plus KL to a frozen dense teacher during warmup
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import time
from pathlib import Path
from statistics import mean
from typing import Any

import torch
import torch.nn.functional as F

from benchmark.common import environment_payload, git_commit, load_json_or_yaml, sha256_file, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_training import (
    _batch,
    _eval_loss,
    _load_bytes,
    _load_training_bytes,
    _routing_snapshot,
    _save_training_artifacts,
)


SUPPORTED_STATUS = "PVR_EC_O_EARLY_DENSE_APPROXIMATION_SUPPORTED"
LOSS_ONLY_WEAK_STATUS = "PVR_DENSE_MIMIC_LOSS_ONLY_WEAK_SIGNAL"
NOT_SUPPORTED_STATUS = "PVR_DENSE_MIMIC_NOT_SUPPORTED"
INCONCLUSIVE_STATUS = "PVR_DENSE_MIMIC_RECOMMENDATION_INCONCLUSIVE"


def distill_weight_for_step(step: int, *, warmup_steps: int, distill_weight: float, decay_steps: int) -> float:
    """Dense imitation first, then specialization by linearly decaying KL."""
    if step <= warmup_steps:
        return distill_weight
    if decay_steps <= 0:
        return 0.0
    remaining = max(0.0, 1.0 - ((step - warmup_steps) / decay_steps))
    return distill_weight * remaining


def _load_checkpoint(model, path: str, device: str) -> None:
    checkpoint = torch.load(path, map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    model.load_state_dict(state, strict=False)


def _variant_config(base: dict[str, Any], variant: str, checkpoint_root: str, output_root: str) -> dict[str, Any]:
    cfg = copy.deepcopy(base)
    cfg["model_variant"] = variant
    cfg["checkpoint_path"] = str(Path(checkpoint_root) / variant / "checkpoint.pt")
    cfg["output_path"] = str(Path(output_root) / variant)
    cfg["diagnostic_only"] = True
    return cfg


def _set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _teacher_kl(student_logits: torch.Tensor, teacher_logits: torch.Tensor, temperature: float) -> torch.Tensor:
    temp = max(1.0e-6, float(temperature))
    return F.kl_div(
        F.log_softmax(student_logits / temp, dim=-1),
        F.softmax(teacher_logits / temp, dim=-1),
        reduction="batchmean",
    ) * (temp * temp)


def _train_student(
    *,
    student_config: dict[str, Any],
    teacher_config: dict[str, Any],
    teacher_checkpoint: str,
    output_root: Path,
    device: str,
    mode: str,
    seed: int,
    max_steps: int,
    batch_size: int,
    seq_len: int,
    lr: float,
    eval_interval: int,
    target_steps: int,
    target_training_tokens: int,
    target_eval_windows: int,
    distill_weight: float,
    distill_warmup_steps: int,
    distill_decay_steps: int,
    temperature: float,
) -> dict[str, Any]:
    _set_seed(seed)
    started = time.time()
    model_out = output_root / student_config["model_variant"]
    checkpoint_path = Path(student_config["checkpoint_path"])
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    tokens_seen = 0
    effective_batch_tokens = batch_size * min(seq_len, int(student_config["context_length"]) - 1)
    curve: list[dict[str, Any]] = []
    eval_curve: list[dict[str, Any]] = []
    routing_curve: list[dict[str, Any]] = []
    try:
        tokens = _load_training_bytes(list(student_config.get("training_data_paths") or []))
        eval_tokens = _load_bytes(list(student_config.get("eval_data_paths") or []), require=False)
        student = build_model(student_config, device=device).model.train()
        teacher = None
        if mode == "dense_mimic":
            teacher = build_model(teacher_config, device=device).model.eval()
            _load_checkpoint(teacher, teacher_checkpoint, device)
            for param in teacher.parameters():
                param.requires_grad_(False)
        optimizer = torch.optim.AdamW(student.parameters(), lr=lr)
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        for step_idx in range(max_steps):
            step = step_idx + 1
            x, y = _batch(tokens, step_idx, batch_size, min(seq_len, int(student_config["context_length"]) - 1), device)
            optimizer.zero_grad(set_to_none=True)
            student_logits = student(x)
            lm_loss = F.cross_entropy(student_logits.reshape(-1, student_logits.shape[-1]), y.reshape(-1))
            kl_loss = student_logits.new_tensor(0.0)
            weight = 0.0
            if teacher is not None:
                weight = distill_weight_for_step(
                    step,
                    warmup_steps=distill_warmup_steps,
                    distill_weight=distill_weight,
                    decay_steps=distill_decay_steps,
                )
                if weight > 0:
                    with torch.no_grad():
                        teacher_logits = teacher(x)
                    kl_loss = _teacher_kl(student_logits, teacher_logits, temperature)
            loss = lm_loss + weight * kl_loss
            loss.backward()
            optimizer.step()
            tokens_seen += int(x.numel())
            curve.append({
                "step": step,
                "optimizer_step": step,
                "loss": float(lm_loss.detach().cpu().item()),
                "optimized_loss": float(loss.detach().cpu().item()),
                "dense_teacher_kl_loss": float(kl_loss.detach().cpu().item()) if mode == "dense_mimic" else None,
                "dense_mimic_weight": weight,
                "phase": "dense_imitation" if weight > 0 else "top1_specialization",
                "tokens_seen": tokens_seen,
                "training_tokens_seen": tokens_seen,
                "effective_batch_tokens": effective_batch_tokens,
            })
            if eval_interval > 0 and step % eval_interval == 0:
                eval_loss, eval_tokens_seen = _eval_loss(student, eval_tokens, step_idx, min(seq_len, int(student_config["context_length"]) - 1), device)
                eval_curve.append({
                    "step": step,
                    "optimizer_step": step,
                    "eval_loss": eval_loss,
                    "eval_tokens": eval_tokens_seen,
                    "training_tokens_seen": tokens_seen,
                })
                snapshot = _routing_snapshot(student, student_config, eval_tokens, step_idx, min(seq_len, int(student_config["context_length"]) - 1), device)
                if snapshot is not None:
                    routing_curve.append({"step": step, "optimizer_step": step, **snapshot})
        torch.save(
            {
                "model_state_dict": student.state_dict(),
                "config": student_config,
                "created_at": utc_now(),
                "training_status": "GENUINE_REDUCED_TRAINING_COMPLETE",
                "diagnostic_mode": mode,
            },
            checkpoint_path,
        )
        row = _save_training_artifacts(
            config=student_config,
            output=model_out,
            checkpoint_path=checkpoint_path,
            curve=curve,
            eval_curve=eval_curve,
            routing_curve=routing_curve,
            status="GENUINE_REDUCED_TRAINING_COMPLETE",
            started=started,
            tokens_seen=tokens_seen,
            optimizer_steps=len(curve),
            effective_batch_tokens=effective_batch_tokens,
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            tier="dense_mimic_diagnostic",
            device=device,
        )
        row["diagnostic_mode"] = mode
        row["mean_dense_teacher_kl_loss"] = _safe_mean([item.get("dense_teacher_kl_loss") for item in curve])
        row["imitation_step_count"] = sum(1 for item in curve if (item.get("dense_mimic_weight") or 0) > 0)
        return row
    except Exception as exc:
        row = _save_training_artifacts(
            config=student_config,
            output=model_out,
            checkpoint_path=checkpoint_path,
            curve=curve,
            eval_curve=eval_curve,
            routing_curve=routing_curve,
            status="TRAINING_FAILED",
            started=started,
            tokens_seen=tokens_seen,
            optimizer_steps=len(curve),
            effective_batch_tokens=effective_batch_tokens,
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            tier="dense_mimic_diagnostic",
            device=device,
            error=repr(exc),
        )
        row["diagnostic_mode"] = mode
        return row
    finally:
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()


def _safe_mean(values: list[Any]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return mean(xs) if xs else None


def _high_low_margin_losses(eval_curve: list[dict[str, Any]], routing_curve: list[dict[str, Any]]) -> dict[str, Any]:
    routing_by_step = {row.get("step"): row for row in routing_curve}
    paired = []
    for row in eval_curve:
        route = routing_by_step.get(row.get("step"), {})
        margin = route.get("prototype_margin")
        loss = row.get("eval_loss")
        if isinstance(margin, (int, float)) and isinstance(loss, (int, float)):
            paired.append({"step": row.get("step"), "eval_loss": float(loss), "prototype_margin": float(margin)})
    margins = [row["prototype_margin"] for row in paired]
    if not margins:
        return {
            "margin_threshold": None,
            "high_margin_mean_eval_loss": None,
            "low_margin_mean_eval_loss": None,
            "high_margin_window_count": 0,
            "low_margin_window_count": 0,
        }
    threshold = sorted(margins)[len(margins) // 2]
    high = [row["eval_loss"] for row in paired if row["prototype_margin"] >= threshold]
    low = [row["eval_loss"] for row in paired if row["prototype_margin"] < threshold]
    return {
        "margin_threshold": threshold,
        "high_margin_mean_eval_loss": _safe_mean(high),
        "low_margin_mean_eval_loss": _safe_mean(low),
        "high_margin_window_count": len(high),
        "low_margin_window_count": len(low),
    }


def _routing_summary(routing_curve: list[dict[str, Any]]) -> dict[str, Any]:
    hard_invariant_clean = bool(routing_curve) and all(
        row.get("owners_per_token") == 1.0
        and row.get("top2_execution_count") == 0
        and row.get("top4_execution_count") == 0
        and row.get("runtime_dynamic_k_count") == 0
        and row.get("runtime_expert_choice_count") == 0
        and row.get("production_map_mutated") is False
        for row in routing_curve
    )
    return {
        "top1_invariants_clean": hard_invariant_clean,
        "mean_route_margin": _safe_mean([row.get("prototype_margin") for row in routing_curve]),
        "mean_owner_entropy": _safe_mean([row.get("owner_entropy") for row in routing_curve]),
        "mean_prototype_margin": _safe_mean([row.get("prototype_margin") for row in routing_curve]),
        "mean_prototype_monopoly_rate": _safe_mean([row.get("prototype_monopoly_rate") for row in routing_curve]),
        "mean_high_gap_monopoly_rate": _safe_mean([row.get("high_gap_monopoly_rate") for row in routing_curve]),
    }


def _load_curve(output_root: Path, model: str, filename: str, key: str) -> list[dict[str, Any]]:
    path = output_root / model / filename
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get(key, [])


def summarize_effectiveness(output_root: str | Path, baseline_variant: str, mimic_variant: str) -> dict[str, Any]:
    root = Path(output_root)
    baseline_train = _load_curve(root, baseline_variant, "training_curve.json", "loss_curve")
    mimic_train = _load_curve(root, mimic_variant, "training_curve.json", "loss_curve")
    baseline_eval = _load_curve(root, baseline_variant, "eval_curve.json", "eval_curve")
    mimic_eval = _load_curve(root, mimic_variant, "eval_curve.json", "eval_curve")
    baseline_routing = _load_curve(root, baseline_variant, "routing_curve.json", "routing_curve")
    mimic_routing = _load_curve(root, mimic_variant, "routing_curve.json", "routing_curve")
    baseline_final = baseline_train[-1]["loss"] if baseline_train else None
    mimic_final = mimic_train[-1]["loss"] if mimic_train else None
    baseline_eval_mean = _safe_mean([row.get("eval_loss") for row in baseline_eval])
    mimic_eval_mean = _safe_mean([row.get("eval_loss") for row in mimic_eval])
    baseline_route = _routing_summary(baseline_routing)
    mimic_route = _routing_summary(mimic_routing)
    baseline_margin_windows = _high_low_margin_losses(baseline_eval, baseline_routing)
    mimic_margin_windows = _high_low_margin_losses(mimic_eval, mimic_routing)
    deltas = {
        "final_train_loss_delta_mimic_minus_baseline": _delta(mimic_final, baseline_final),
        "mean_eval_loss_delta_mimic_minus_baseline": _delta(mimic_eval_mean, baseline_eval_mean),
        "mean_route_margin_delta_mimic_minus_baseline": _delta(mimic_route["mean_route_margin"], baseline_route["mean_route_margin"]),
        "mean_owner_entropy_delta_mimic_minus_baseline": _delta(mimic_route["mean_owner_entropy"], baseline_route["mean_owner_entropy"]),
        "mean_prototype_monopoly_rate_delta_mimic_minus_baseline": _delta(mimic_route["mean_prototype_monopoly_rate"], baseline_route["mean_prototype_monopoly_rate"]),
        "high_margin_eval_loss_delta_mimic_minus_baseline": _delta(mimic_margin_windows["high_margin_mean_eval_loss"], baseline_margin_windows["high_margin_mean_eval_loss"]),
        "low_margin_eval_loss_delta_mimic_minus_baseline": _delta(mimic_margin_windows["low_margin_mean_eval_loss"], baseline_margin_windows["low_margin_mean_eval_loss"]),
    }
    loss_improves_or_matches = (
        deltas["final_train_loss_delta_mimic_minus_baseline"] is not None
        and deltas["mean_eval_loss_delta_mimic_minus_baseline"] is not None
        and deltas["final_train_loss_delta_mimic_minus_baseline"] < 0
        and deltas["mean_eval_loss_delta_mimic_minus_baseline"] <= 0
    )
    margin_ratio = _ratio(mimic_route["mean_route_margin"], baseline_route["mean_route_margin"])
    entropy_ratio = _ratio(mimic_route["mean_owner_entropy"], baseline_route["mean_owner_entropy"])
    monopoly_delta = deltas["mean_prototype_monopoly_rate_delta_mimic_minus_baseline"]
    route_collapse_checks = {
        "top1_invariants_clean": mimic_route["top1_invariants_clean"],
        "route_margin_not_collapsed": margin_ratio is not None and margin_ratio >= 0.80,
        "owner_entropy_not_collapsed": entropy_ratio is not None and entropy_ratio >= 0.80,
        "expert_utilization_not_collapsed": monopoly_delta is not None and monopoly_delta <= 0.15,
    }
    route_collapse_stable = all(route_collapse_checks.values())
    if loss_improves_or_matches and route_collapse_stable:
        status = SUPPORTED_STATUS
    elif loss_improves_or_matches:
        status = LOSS_ONLY_WEAK_STATUS
    elif baseline_train and mimic_train:
        status = NOT_SUPPORTED_STATUS
    else:
        status = INCONCLUSIVE_STATUS
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "baseline_variant": baseline_variant,
        "mimic_variant": mimic_variant,
        "baseline": {
            "final_train_loss": baseline_final,
            "mean_eval_loss": baseline_eval_mean,
            **baseline_route,
            **baseline_margin_windows,
            "eval_window_count": len(baseline_eval),
            "routing_window_count": len(baseline_routing),
        },
        "dense_mimic": {
            "final_train_loss": mimic_final,
            "mean_eval_loss": mimic_eval_mean,
            **mimic_route,
            **mimic_margin_windows,
            "eval_window_count": len(mimic_eval),
            "routing_window_count": len(mimic_routing),
            "mean_teacher_kl": _safe_mean([row.get("dense_teacher_kl_loss") for row in mimic_train]),
            "imitation_step_count": sum(1 for row in mimic_train if (row.get("dense_mimic_weight") or 0) > 0),
        },
        "deltas": deltas,
        "route_collapse_checks": route_collapse_checks,
        "route_collapse_stable": route_collapse_stable,
        "loss_improves_or_matches": loss_improves_or_matches,
        "decision_rule": "supported only if loss improves or matches baseline, Top1 invariants remain clean, route margin does not collapse, owner entropy does not collapse, and expert utilization does not collapse",
    }


def _delta(left: Any, right: Any) -> float | None:
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return float(left) - float(right)
    return None


def _ratio(left: Any, right: Any) -> float | None:
    if isinstance(left, (int, float)) and isinstance(right, (int, float)) and right != 0:
        return float(left) / float(right)
    return None


def run(
    *,
    dense_config: str = "benchmark/configs/generated/dense_transformer_100m.yaml",
    pvr_config: str = "benchmark/configs/generated/pvr_ec_o_full_100m.yaml",
    output: str = "benchmark/reports/generated/dense_mimic_100m",
    checkpoint_root: str = "checkpoints/dense_mimic_100m",
    teacher_checkpoint: str | None = None,
    device: str = "cuda",
    seed: int = 20260613,
    max_steps: int = 1000,
    batch_size: int = 2,
    seq_len: int = 128,
    lr: float = 1e-5,
    eval_interval: int = 200,
    target_steps: int = 4000,
    target_training_tokens: int = 1_000_000,
    target_eval_windows: int = 10,
    distill_weight: float = 0.5,
    distill_warmup_steps: int = 500,
    distill_decay_steps: int = 500,
    temperature: float = 2.0,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    dense_cfg = load_json_or_yaml(dense_config)
    pvr_cfg = load_json_or_yaml(pvr_config)
    teacher_checkpoint = teacher_checkpoint or str(dense_cfg.get("checkpoint_path"))
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    baseline_variant = f"{pvr_cfg['model_variant']}_dense_mimic_baseline"
    mimic_variant = f"{pvr_cfg['model_variant']}_dense_mimic_student"
    rows = []
    for mode, variant in [("baseline", baseline_variant), ("dense_mimic", mimic_variant)]:
        cfg = _variant_config(pvr_cfg, variant, checkpoint_root, output)
        rows.append(_train_student(
            student_config=cfg,
            teacher_config=dense_cfg,
            teacher_checkpoint=teacher_checkpoint,
            output_root=out,
            device=device,
            mode=mode,
            seed=seed,
            max_steps=max_steps,
            batch_size=batch_size,
            seq_len=seq_len,
            lr=lr,
            eval_interval=eval_interval,
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            distill_weight=distill_weight,
            distill_warmup_steps=distill_warmup_steps,
            distill_decay_steps=distill_decay_steps,
            temperature=temperature,
        ))
    summary = summarize_effectiveness(out, baseline_variant, mimic_variant)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": summary["status"],
        "budget_status": "RESOURCE_REDUCED_BUDGET" if max_steps < target_steps else "NONE",
        "experiment": "dense_approximation_first_then_top1_specialization",
        "teacher_checkpoint": teacher_checkpoint,
        "teacher_checkpoint_hash": sha256_file(teacher_checkpoint) if Path(teacher_checkpoint).exists() else "",
        "device": device,
        "environment": environment_payload(),
        "seed": seed,
        "max_steps": max_steps,
        "batch_size": batch_size,
        "seq_len": seq_len,
        "effective_batch_tokens": batch_size * seq_len,
        "distill_weight": distill_weight,
        "distill_warmup_steps": distill_warmup_steps,
        "distill_decay_steps": distill_decay_steps,
        "temperature": temperature,
        "rows": rows,
        "effectiveness": summary,
    }
    write_json(out / "dense_mimic_experiment_report.json", payload)
    _write_markdown(out / "dense_mimic_experiment_report.md", payload)
    print(payload["status"])
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    eff = payload["effectiveness"]
    deltas = eff["deltas"]
    lines = [
        "# Dense Mimic Experiment Report",
        "",
        f"Status: `{payload['status']}`",
        "",
        "Matched diagnostic experiment: fresh PVR baseline vs fresh PVR dense-mimic student.",
        "",
        f"- Final train loss delta mimic-baseline: `{deltas['final_train_loss_delta_mimic_minus_baseline']}`",
        f"- Mean eval loss delta mimic-baseline: `{deltas['mean_eval_loss_delta_mimic_minus_baseline']}`",
        f"- Mean route margin delta mimic-baseline: `{deltas['mean_route_margin_delta_mimic_minus_baseline']}`",
        "",
        "This run is diagnostic-only and does not modify benchmark promotion gates.",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run dense-teacher mimic diagnostic for PVR")
    parser.add_argument("--dense-config", default="benchmark/configs/generated/dense_transformer_100m.yaml")
    parser.add_argument("--pvr-config", default="benchmark/configs/generated/pvr_ec_o_full_100m.yaml")
    parser.add_argument("--output", default="benchmark/reports/generated/dense_mimic_100m")
    parser.add_argument("--checkpoint-root", default="checkpoints/dense_mimic_100m")
    parser.add_argument("--teacher-checkpoint", default=None)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seed", type=int, default=20260613)
    parser.add_argument("--max-steps", type=int, default=1000)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--seq-len", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--eval-interval", type=int, default=200)
    parser.add_argument("--distill-weight", type=float, default=0.5)
    parser.add_argument("--distill-warmup-steps", type=int, default=500)
    parser.add_argument("--distill-decay-steps", type=int, default=500)
    parser.add_argument("--temperature", type=float, default=2.0)
    args = parser.parse_args()
    run(
        dense_config=args.dense_config,
        pvr_config=args.pvr_config,
        output=args.output,
        checkpoint_root=args.checkpoint_root,
        teacher_checkpoint=args.teacher_checkpoint,
        device=args.device,
        seed=args.seed,
        max_steps=args.max_steps,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lr=args.lr,
        eval_interval=args.eval_interval,
        distill_weight=args.distill_weight,
        distill_warmup_steps=args.distill_warmup_steps,
        distill_decay_steps=args.distill_decay_steps,
        temperature=args.temperature,
    )


if __name__ == "__main__":
    main()
