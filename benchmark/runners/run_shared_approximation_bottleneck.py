"""Run shared-approximation bottleneck repairs for PVR-EC-O.

This diagnostic tests structural alternatives after global dense KL failed:

* shared_trunk_init_from_dense
* shared_capacity_plus
* gated_teacher_low_confidence_only

It does not add runtime Top-k routing and does not use the deprecated
route-confidence regularizer.
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
from benchmark.model_factory import _infer_ffn_size, build_model
from benchmark.runners.run_training import (
    _batch,
    _eval_loss,
    _load_bytes,
    _load_training_bytes,
    _routing_snapshot,
    _save_training_artifacts,
)


SHARED_INIT_SUPPORTED = "PVR_SHARED_TRUNK_INIT_SUPPORTED"
SHARED_CAPACITY_SUPPORTED = "PVR_SHARED_CAPACITY_REPAIR_SUPPORTED"
GATED_TEACHER_SUPPORTED = "PVR_GATED_TEACHER_SUPPORTED"
INCONCLUSIVE = "PVR_DENSE_APPROXIMATION_REPAIR_INCONCLUSIVE"
ROUTING_NOT_MAIN = "PVR_ROUTING_NOT_MAIN_BOTTLENECK"


def _set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _safe_mean(values: list[Any]) -> float | None:
    xs = [float(value) for value in values if isinstance(value, (int, float))]
    return mean(xs) if xs else None


def _delta(left: Any, right: Any) -> float | None:
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return float(left) - float(right)
    return None


def _ratio(left: Any, right: Any) -> float | None:
    if isinstance(left, (int, float)) and isinstance(right, (int, float)) and right != 0:
        return float(left) / float(right)
    return None


def _load_checkpoint(model, path: str, device: str) -> dict[str, Any]:
    checkpoint = torch.load(path, map_location=device)
    state = checkpoint.get("model_state_dict", checkpoint)
    model.load_state_dict(state, strict=False)
    return checkpoint


def _copy_if_same_shape(target: torch.nn.Parameter | torch.Tensor, source: torch.nn.Parameter | torch.Tensor) -> bool:
    if tuple(target.shape) != tuple(source.shape):
        return False
    with torch.no_grad():
        target.copy_(source)
    return True


def copy_compatible_dense_weights_to_pvr(dense_model, pvr_model, *, copy_scope: str = "full_compatible_shared_copy") -> dict[str, Any]:
    """Copy only compatible dense weights into PVR shared/common paths."""
    allowed_scopes = {
        "embeddings_only",
        "attention_only",
        "norms_only",
        "shared_ffn_bias_only",
        "embeddings_attention_norms",
        "full_compatible_shared_copy",
    }
    if copy_scope not in allowed_scopes:
        raise ValueError(f"Unsupported copy_scope: {copy_scope}")
    copied: list[str] = []
    skipped: list[str] = []
    copy_embeddings = copy_scope in {"embeddings_only", "embeddings_attention_norms", "full_compatible_shared_copy"}
    copy_attention = copy_scope in {"attention_only", "embeddings_attention_norms", "full_compatible_shared_copy"}
    copy_norms = copy_scope in {"norms_only", "embeddings_attention_norms", "full_compatible_shared_copy"}
    copy_shared_bias = copy_scope in {"shared_ffn_bias_only", "full_compatible_shared_copy"}
    if copy_embeddings:
        for name in ["token_emb.weight", "pos_emb.weight", "head.weight"]:
            target = dict(pvr_model.named_parameters()).get(name)
            source = dict(dense_model.named_parameters()).get(name)
            if target is not None and source is not None and _copy_if_same_shape(target, source):
                copied.append(name)
            else:
                skipped.append(name)
    if copy_norms:
        for name in ["ln_f.weight", "ln_f.bias"]:
            target = dict(pvr_model.named_parameters()).get(name)
            source = dict(dense_model.named_parameters()).get(name)
            if target is not None and source is not None and _copy_if_same_shape(target, source):
                copied.append(name)
            else:
                skipped.append(name)
    dense_layers = getattr(getattr(dense_model, "layers", None), "layers", [])
    for idx, (dense_layer, pvr_layer) in enumerate(zip(dense_layers, pvr_model.attn)):
        dense_state = dense_layer.state_dict()
        pvr_state = pvr_layer.state_dict()
        compatible = {}
        if copy_attention or copy_norms:
            for key, value in dense_state.items():
                is_attention = key.startswith("self_attn.")
                is_norm = key.startswith("norm")
                if (copy_attention and is_attention) or (copy_norms and is_norm):
                    if key in pvr_state and tuple(pvr_state[key].shape) == tuple(value.shape):
                        compatible[key] = value
        pvr_layer.load_state_dict(compatible, strict=False)
        copied.extend(f"attn.{idx}.{key}" for key in compatible)
        skipped.extend(f"attn.{idx}.{key}" for key in dense_state if key not in compatible and (copy_attention or copy_norms))
        shared = pvr_model.blocks[idx].shared if idx < len(pvr_model.blocks) else None
        if shared is not None and copy_scope == "full_compatible_shared_copy":
            if _copy_if_same_shape(shared.w1.weight, dense_layer.linear1.weight):
                copied.append(f"blocks.{idx}.shared.w1.weight")
            else:
                skipped.append(f"blocks.{idx}.shared.w1.weight")
            if _copy_if_same_shape(shared.w1.bias, dense_layer.linear1.bias):
                copied.append(f"blocks.{idx}.shared.w1.bias")
            else:
                skipped.append(f"blocks.{idx}.shared.w1.bias")
            if _copy_if_same_shape(shared.w2.weight, dense_layer.linear2.weight):
                copied.append(f"blocks.{idx}.shared.w2.weight")
            else:
                skipped.append(f"blocks.{idx}.shared.w2.weight")
            if _copy_if_same_shape(shared.w2.bias, dense_layer.linear2.bias):
                copied.append(f"blocks.{idx}.shared.w2.bias")
            else:
                skipped.append(f"blocks.{idx}.shared.w2.bias")
        elif shared is not None and copy_shared_bias:
            if _copy_if_same_shape(shared.w1.bias, dense_layer.linear1.bias):
                copied.append(f"blocks.{idx}.shared.w1.bias")
            else:
                skipped.append(f"blocks.{idx}.shared.w1.bias")
            if _copy_if_same_shape(shared.w2.bias, dense_layer.linear2.bias):
                copied.append(f"blocks.{idx}.shared.w2.bias")
            else:
                skipped.append(f"blocks.{idx}.shared.w2.bias")
    return {
        "copy_scope": copy_scope,
        "copied_count": len(copied),
        "skipped_count": len(skipped),
        "copied": copied[:80],
        "skipped_sample": skipped[:80],
    }


def _variant_config(base: dict[str, Any], variant: str, checkpoint_root: str, output_root: str, *, shared_capacity_multiplier: float | None = None) -> dict[str, Any]:
    cfg = copy.deepcopy(base)
    cfg["model_variant"] = variant
    cfg["checkpoint_path"] = str(Path(checkpoint_root) / variant / "checkpoint.pt")
    cfg["output_path"] = str(Path(output_root) / variant)
    cfg["diagnostic_only"] = True
    if shared_capacity_multiplier is not None:
        expert_ffn = int(cfg.get("materialization_ffn_size") or _infer_ffn_size(cfg))
        cfg["materialization_ffn_size"] = expert_ffn
        cfg["shared_materialization_ffn_size"] = max(expert_ffn + 1, int(round(expert_ffn * shared_capacity_multiplier)))
        cfg["shared_capacity_multiplier"] = shared_capacity_multiplier
    return cfg


def _teacher_kl_per_token(student_logits: torch.Tensor, teacher_logits: torch.Tensor, temperature: float) -> torch.Tensor:
    temp = max(1.0e-6, float(temperature))
    return F.kl_div(
        F.log_softmax(student_logits / temp, dim=-1),
        F.softmax(teacher_logits / temp, dim=-1),
        reduction="none",
    ).sum(dim=-1) * (temp * temp)


def _forward_with_route_margins(model, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor | None]:
    margins: list[torch.Tensor] = []

    def hook(module, inputs, _output):
        with torch.no_grad():
            h = module.ln(inputs[0])
            if module.descriptor_operator is not None:
                h = h + module.descriptor_operator(h)
            scores = module.router(h)
            top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
            if top.values.shape[-1] > 1:
                margins.append((top.values[..., 0] - top.values[..., 1]).detach())

    handles = [block.register_forward_hook(hook) for block in getattr(model, "blocks", [])]
    try:
        logits = model(x)
    finally:
        for handle in handles:
            handle.remove()
    if not margins:
        return logits, None
    return logits, torch.stack(margins).mean(dim=0)


def _gated_teacher_loss(
    *,
    student_logits: torch.Tensor,
    teacher_logits: torch.Tensor,
    token_losses: torch.Tensor,
    route_margins: torch.Tensor | None,
    temperature: float,
) -> tuple[torch.Tensor, dict[str, Any]]:
    per_token_kl = _teacher_kl_per_token(student_logits, teacher_logits, temperature)
    high_loss = token_losses.detach() > torch.quantile(token_losses.detach().float(), 0.5)
    if route_margins is not None:
        low_margin = route_margins < torch.quantile(route_margins.float(), 0.5)
        mask = high_loss | low_margin
    else:
        low_margin = torch.zeros_like(high_loss, dtype=torch.bool)
        mask = high_loss
    denom = mask.float().sum().clamp_min(1.0)
    loss = (per_token_kl * mask.float()).sum() / denom
    return loss, {
        "gated_teacher_mask_rate": float(mask.float().mean().detach().cpu().item()),
        "gated_teacher_high_loss_rate": float(high_loss.float().mean().detach().cpu().item()),
        "gated_teacher_low_margin_rate": float(low_margin.float().mean().detach().cpu().item()),
    }


def _train_variant(
    *,
    variant_name: str,
    mode: str,
    student_config: dict[str, Any],
    dense_config: dict[str, Any],
    dense_checkpoint: str,
    output_root: Path,
    device: str,
    seed: int,
    max_steps: int,
    batch_size: int,
    seq_len: int,
    lr: float,
    eval_interval: int,
    target_steps: int,
    target_training_tokens: int,
    target_eval_windows: int,
    gated_teacher_weight: float,
    gated_teacher_warmup_steps: int,
    temperature: float,
    copy_scope: str = "full_compatible_shared_copy",
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
    init_report: dict[str, Any] = {}
    try:
        tokens = _load_training_bytes(list(student_config.get("training_data_paths") or []))
        eval_tokens = _load_bytes(list(student_config.get("eval_data_paths") or []), require=False)
        student = build_model(student_config, device=device).model.train()
        teacher = None
        if mode in {"shared_trunk_init_from_dense", "gated_teacher_low_confidence_only"}:
            teacher = build_model(dense_config, device=device).model.eval()
            _load_checkpoint(teacher, dense_checkpoint, device)
            for param in teacher.parameters():
                param.requires_grad_(False)
        if mode == "shared_trunk_init_from_dense" and teacher is not None:
            init_report = copy_compatible_dense_weights_to_pvr(teacher, student, copy_scope=copy_scope)
        optimizer = torch.optim.AdamW(student.parameters(), lr=lr)
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        for step_idx in range(max_steps):
            step = step_idx + 1
            x, y = _batch(tokens, step_idx, batch_size, min(seq_len, int(student_config["context_length"]) - 1), device)
            optimizer.zero_grad(set_to_none=True)
            student_logits, route_margins = _forward_with_route_margins(student, x)
            token_losses = F.cross_entropy(student_logits.reshape(-1, student_logits.shape[-1]), y.reshape(-1), reduction="none").view_as(y)
            lm_loss = token_losses.mean()
            teacher_loss = student_logits.new_tensor(0.0)
            teacher_metrics = {
                "gated_teacher_mask_rate": None,
                "gated_teacher_high_loss_rate": None,
                "gated_teacher_low_margin_rate": None,
            }
            teacher_weight = 0.0
            if mode == "gated_teacher_low_confidence_only" and teacher is not None and step <= gated_teacher_warmup_steps:
                teacher_weight = gated_teacher_weight
                with torch.no_grad():
                    teacher_logits = teacher(x)
                teacher_loss, teacher_metrics = _gated_teacher_loss(
                    student_logits=student_logits,
                    teacher_logits=teacher_logits,
                    token_losses=token_losses,
                    route_margins=route_margins,
                    temperature=temperature,
                )
            loss = lm_loss + teacher_weight * teacher_loss
            loss.backward()
            optimizer.step()
            tokens_seen += int(x.numel())
            curve.append({
                "step": step,
                "optimizer_step": step,
                "loss": float(lm_loss.detach().cpu().item()),
                "optimized_loss": float(loss.detach().cpu().item()),
                "gated_teacher_loss": float(teacher_loss.detach().cpu().item()) if teacher_weight else None,
                "gated_teacher_weight": teacher_weight,
                "phase": mode,
                "tokens_seen": tokens_seen,
                "training_tokens_seen": tokens_seen,
                "effective_batch_tokens": effective_batch_tokens,
                **teacher_metrics,
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
                "init_report": init_report,
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
            tier="shared_approximation_bottleneck",
            device=device,
        )
        row["diagnostic_mode"] = mode
        row["variant_name"] = variant_name
        row["init_report"] = init_report
        row["mean_gated_teacher_loss"] = _safe_mean([item.get("gated_teacher_loss") for item in curve])
        row["mean_gated_teacher_mask_rate"] = _safe_mean([item.get("gated_teacher_mask_rate") for item in curve])
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
            tier="shared_approximation_bottleneck",
            device=device,
            error=repr(exc),
        )
        row["diagnostic_mode"] = mode
        row["variant_name"] = variant_name
        return row
    finally:
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()


def _load_curve(output_root: Path, model: str, filename: str, key: str) -> list[dict[str, Any]]:
    path = output_root / model / filename
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get(key, [])


def dense_gap_window_classification(
    *,
    output_root: str | Path,
    variants: dict[str, str],
    dense_eval_curve_path: str | Path = "benchmark/reports/generated/training_100m_real_4k/dense_transformer_100m/eval_curve.json",
) -> dict[str, Any]:
    root = Path(output_root)
    dense_rows = json.loads(Path(dense_eval_curve_path).read_text(encoding="utf-8")).get("eval_curve", []) if Path(dense_eval_curve_path).exists() else []
    dense_by_step = {row.get("step"): row for row in dense_rows}
    result: dict[str, Any] = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "dense_eval_curve_path": str(dense_eval_curve_path),
        "variants": {},
    }
    for label, model in variants.items():
        if label == "baseline":
            pass
        eval_rows = _load_curve(root, model, "eval_curve.json", "eval_curve")
        routing_rows = _load_curve(root, model, "routing_curve.json", "routing_curve")
        routing_by_step = {row.get("step"): row for row in routing_rows}
        margins = [float(row.get("prototype_margin")) for row in routing_rows if isinstance(row.get("prototype_margin"), (int, float))]
        threshold = sorted(margins)[len(margins) // 2] if margins else None
        buckets = {
            "dense_better_route_high_confidence": [],
            "dense_better_route_low_confidence": [],
            "pvr_better_route_high_confidence": [],
            "pvr_better_route_low_confidence": [],
        }
        for row in eval_rows:
            step = row.get("step")
            dense_loss = dense_by_step.get(step, {}).get("eval_loss")
            pvr_loss = row.get("eval_loss")
            margin = routing_by_step.get(step, {}).get("prototype_margin")
            if not isinstance(dense_loss, (int, float)) or not isinstance(pvr_loss, (int, float)) or not isinstance(margin, (int, float)) or threshold is None:
                continue
            dense_better = float(dense_loss) < float(pvr_loss)
            high_conf = float(margin) >= threshold
            key = (
                "dense_better_route_high_confidence" if dense_better and high_conf
                else "dense_better_route_low_confidence" if dense_better
                else "pvr_better_route_high_confidence" if high_conf
                else "pvr_better_route_low_confidence"
            )
            buckets[key].append({
                "step": step,
                "dense_eval_loss": float(dense_loss),
                "pvr_eval_loss": float(pvr_loss),
                "pvr_minus_dense_eval_loss": float(pvr_loss) - float(dense_loss),
                "route_margin": float(margin),
            })
        result["variants"][label] = {
            "model": model,
            "route_margin_threshold": threshold,
            "bucket_counts": {key: len(value) for key, value in buckets.items()},
            "bucket_mean_pvr_minus_dense": {
                key: _safe_mean([item["pvr_minus_dense_eval_loss"] for item in value])
                for key, value in buckets.items()
            },
            "windows": buckets,
        }
    return result


def _route_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    clean = bool(rows) and all(
        row.get("owners_per_token") == 1.0
        and row.get("top2_execution_count") == 0
        and row.get("top4_execution_count") == 0
        and row.get("runtime_dynamic_k_count") == 0
        and row.get("runtime_expert_choice_count") == 0
        and row.get("production_map_mutated") is False
        for row in rows
    )
    return {
        "top1_invariants_clean": clean,
        "mean_route_margin": _safe_mean([row.get("prototype_margin") for row in rows]),
        "mean_owner_entropy": _safe_mean([row.get("owner_entropy") for row in rows]),
        "mean_prototype_monopoly_rate": _safe_mean([row.get("prototype_monopoly_rate") for row in rows]),
    }


def summarize_matrix(output_root: str | Path, variants: dict[str, str]) -> dict[str, Any]:
    root = Path(output_root)
    baseline_name = variants["baseline"]
    baseline_train = _load_curve(root, baseline_name, "training_curve.json", "loss_curve")
    baseline_eval = _load_curve(root, baseline_name, "eval_curve.json", "eval_curve")
    baseline_route = _route_summary(_load_curve(root, baseline_name, "routing_curve.json", "routing_curve"))
    baseline = {
        "final_train_loss": baseline_train[-1]["loss"] if baseline_train else None,
        "mean_eval_loss": _safe_mean([row.get("eval_loss") for row in baseline_eval]),
        **baseline_route,
    }
    rows: dict[str, Any] = {}
    supported: dict[str, bool] = {}
    for label, model in variants.items():
        train = _load_curve(root, model, "training_curve.json", "loss_curve")
        eval_curve = _load_curve(root, model, "eval_curve.json", "eval_curve")
        routing = _route_summary(_load_curve(root, model, "routing_curve.json", "routing_curve"))
        current = {
            "model": model,
            "final_train_loss": train[-1]["loss"] if train else None,
            "mean_eval_loss": _safe_mean([row.get("eval_loss") for row in eval_curve]),
            "eval_window_count": len(eval_curve),
            **routing,
        }
        deltas = {
            "final_train_loss_delta_vs_baseline": _delta(current["final_train_loss"], baseline["final_train_loss"]),
            "mean_eval_loss_delta_vs_baseline": _delta(current["mean_eval_loss"], baseline["mean_eval_loss"]),
            "mean_route_margin_delta_vs_baseline": _delta(current["mean_route_margin"], baseline["mean_route_margin"]),
            "mean_owner_entropy_delta_vs_baseline": _delta(current["mean_owner_entropy"], baseline["mean_owner_entropy"]),
            "mean_prototype_monopoly_rate_delta_vs_baseline": _delta(current["mean_prototype_monopoly_rate"], baseline["mean_prototype_monopoly_rate"]),
        }
        margin_ratio = _ratio(current["mean_route_margin"], baseline["mean_route_margin"])
        entropy_ratio = _ratio(current["mean_owner_entropy"], baseline["mean_owner_entropy"])
        monopoly_delta = deltas["mean_prototype_monopoly_rate_delta_vs_baseline"]
        route_stable = (
            current["top1_invariants_clean"]
            and margin_ratio is not None and margin_ratio >= 0.50
            and current["mean_route_margin"] is not None and current["mean_route_margin"] >= 0.25
            and entropy_ratio is not None and entropy_ratio >= 0.80
            and monopoly_delta is not None and monopoly_delta <= 0.15
        )
        loss_supported = (
            label != "baseline"
            and deltas["final_train_loss_delta_vs_baseline"] is not None
            and deltas["mean_eval_loss_delta_vs_baseline"] is not None
            and deltas["final_train_loss_delta_vs_baseline"] < 0
            and deltas["mean_eval_loss_delta_vs_baseline"] <= 0
        )
        rows[label] = {**current, "deltas": deltas, "route_stable": route_stable, "loss_supported": loss_supported}
        supported[label] = bool(loss_supported and route_stable)
    if supported.get("shared_trunk_init_from_dense"):
        status = SHARED_INIT_SUPPORTED
    elif supported.get("shared_capacity_plus"):
        status = SHARED_CAPACITY_SUPPORTED
    elif supported.get("gated_teacher_low_confidence_only"):
        status = GATED_TEACHER_SUPPORTED
    else:
        status = INCONCLUSIVE
    routing_not_main = bool(rows) and all(row.get("top1_invariants_clean") for row in rows.values())
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "secondary_status": ROUTING_NOT_MAIN if routing_not_main else None,
        "baseline": baseline,
        "rows": rows,
        "supported_repairs": [label for label, ok in supported.items() if ok],
        "decision_rule": "repair is supported only if it improves final train loss and mean eval loss while Top1 invariants and route-collapse checks remain clean",
    }


def run(
    *,
    dense_config: str = "benchmark/configs/generated/dense_transformer_100m.yaml",
    pvr_config: str = "benchmark/configs/generated/pvr_ec_o_full_100m.yaml",
    output: str = "benchmark/reports/generated/shared_approximation_bottleneck_100m",
    checkpoint_root: str = "checkpoints/shared_approximation_bottleneck_100m",
    dense_checkpoint: str | None = None,
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
    shared_capacity_multiplier: float = 4.0,
    gated_teacher_weight: float = 0.001,
    gated_teacher_warmup_steps: int = 500,
    temperature: float = 2.0,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    dense_cfg = load_json_or_yaml(dense_config)
    pvr_cfg = load_json_or_yaml(pvr_config)
    dense_checkpoint = dense_checkpoint or str(dense_cfg.get("checkpoint_path"))
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    variants = {
        "baseline": _variant_config(pvr_cfg, "pvr_ec_o_full_100m_baseline", checkpoint_root, output),
        "shared_trunk_init_from_dense": _variant_config(pvr_cfg, "pvr_ec_o_full_100m_shared_trunk_init_from_dense", checkpoint_root, output),
        "shared_capacity_plus": _variant_config(pvr_cfg, "pvr_ec_o_full_100m_shared_capacity_plus", checkpoint_root, output, shared_capacity_multiplier=shared_capacity_multiplier),
        "gated_teacher_low_confidence_only": _variant_config(pvr_cfg, "pvr_ec_o_full_100m_gated_teacher_low_confidence_only", checkpoint_root, output),
    }
    modes = {
        "baseline": "baseline",
        "shared_trunk_init_from_dense": "shared_trunk_init_from_dense",
        "shared_capacity_plus": "shared_capacity_plus",
        "gated_teacher_low_confidence_only": "gated_teacher_low_confidence_only",
    }
    rows = []
    for label, cfg in variants.items():
        rows.append(_train_variant(
            variant_name=label,
            mode=modes[label],
            student_config=cfg,
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
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            gated_teacher_weight=gated_teacher_weight,
            gated_teacher_warmup_steps=gated_teacher_warmup_steps,
            temperature=temperature,
            copy_scope="full_compatible_shared_copy",
        ))
    variant_names = {label: cfg["model_variant"] for label, cfg in variants.items()}
    summary = summarize_matrix(out, variant_names)
    dense_gap_classification = dense_gap_window_classification(output_root=out, variants=variant_names)
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": summary["status"],
        "secondary_status": summary.get("secondary_status"),
        "experiment": "PVR_SHARED_APPROXIMATION_BOTTLENECK_TEST",
        "budget_status": "RESOURCE_REDUCED_BUDGET" if max_steps < target_steps else "NONE",
        "dense_checkpoint": dense_checkpoint,
        "dense_checkpoint_hash": sha256_file(dense_checkpoint) if Path(dense_checkpoint).exists() else "",
        "device": device,
        "environment": environment_payload(),
        "seed": seed,
        "max_steps": max_steps,
        "batch_size": batch_size,
        "seq_len": seq_len,
        "effective_batch_tokens": batch_size * seq_len,
        "shared_capacity_multiplier": shared_capacity_multiplier,
        "gated_teacher_weight": gated_teacher_weight,
        "gated_teacher_warmup_steps": gated_teacher_warmup_steps,
        "temperature": temperature,
        "variant_names": variant_names,
        "rows": rows,
        "summary": summary,
        "dense_gap_window_classification": dense_gap_classification,
        "deprecated_paths_not_used": [
            "in_bounds_probability_head_as_previously_implemented",
            "route_confidence_regularization_0_01",
            "global_dense_kl_persistent_objective",
        ],
    }
    write_json(out / "shared_approximation_bottleneck_report.json", payload)
    write_json(out / "dense_gap_window_classification.json", dense_gap_classification)
    _write_markdown(out / "shared_approximation_bottleneck_report.md", payload)
    print(payload["status"])
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Shared Approximation Bottleneck Report",
        "",
        f"Status: `{payload['status']}`",
        f"Secondary status: `{payload.get('secondary_status')}`",
        "",
        "| variant | final train delta | mean eval delta | route margin delta | route stable |",
        "|---|---:|---:|---:|---|",
    ]
    for label, row in payload["summary"]["rows"].items():
        deltas = row["deltas"]
        lines.append(
            f"| {label} | {deltas['final_train_loss_delta_vs_baseline']} | "
            f"{deltas['mean_eval_loss_delta_vs_baseline']} | "
            f"{deltas['mean_route_margin_delta_vs_baseline']} | {row['route_stable']} |"
        )
    lines.extend([
        "",
        "Deprecated paths were not used: prior in-bounds head, route-confidence regularizer, and persistent global dense KL.",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PVR shared-approximation bottleneck test")
    parser.add_argument("--dense-config", default="benchmark/configs/generated/dense_transformer_100m.yaml")
    parser.add_argument("--pvr-config", default="benchmark/configs/generated/pvr_ec_o_full_100m.yaml")
    parser.add_argument("--output", default="benchmark/reports/generated/shared_approximation_bottleneck_100m")
    parser.add_argument("--checkpoint-root", default="checkpoints/shared_approximation_bottleneck_100m")
    parser.add_argument("--dense-checkpoint", default=None)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--seed", type=int, default=20260613)
    parser.add_argument("--max-steps", type=int, default=1000)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--seq-len", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--eval-interval", type=int, default=200)
    parser.add_argument("--shared-capacity-multiplier", type=float, default=4.0)
    parser.add_argument("--gated-teacher-weight", type=float, default=0.001)
    parser.add_argument("--gated-teacher-warmup-steps", type=int, default=500)
    parser.add_argument("--temperature", type=float, default=2.0)
    args = parser.parse_args()
    run(
        dense_config=args.dense_config,
        pvr_config=args.pvr_config,
        output=args.output,
        checkpoint_root=args.checkpoint_root,
        dense_checkpoint=args.dense_checkpoint,
        device=args.device,
        seed=args.seed,
        max_steps=args.max_steps,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lr=args.lr,
        eval_interval=args.eval_interval,
        shared_capacity_multiplier=args.shared_capacity_multiplier,
        gated_teacher_weight=args.gated_teacher_weight,
        gated_teacher_warmup_steps=args.gated_teacher_warmup_steps,
        temperature=args.temperature,
    )


if __name__ == "__main__":
    main()
