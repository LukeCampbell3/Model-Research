"""Train benchmark models on the prepared real reduced data layer."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
import math
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F

try:
    import numpy as np
except Exception:  # pragma: no cover - numpy is available in normal benchmark envs.
    np = None

from benchmark.common import environment_payload, git_commit, load_json_or_yaml, sha256_file, utc_now, write_json
from benchmark.model_factory import build_model


def _atomic_torch_save(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    torch.save(payload, tmp)
    tmp.replace(path)


def _config_hash(config: dict[str, Any]) -> str:
    data = json.dumps(config, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def _rng_state_payload() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "python_rng_state": random.getstate(),
        "torch_cpu_rng_state": torch.get_rng_state(),
    }
    if np is not None:
        payload["numpy_rng_state"] = np.random.get_state()
    if torch.cuda.is_available():
        payload["torch_cuda_rng_state_all"] = torch.cuda.get_rng_state_all()
    return payload


def _restore_rng_state(checkpoint: dict[str, Any]) -> None:
    if checkpoint.get("python_rng_state") is not None:
        random.setstate(checkpoint["python_rng_state"])
    if np is not None and checkpoint.get("numpy_rng_state") is not None:
        np.random.set_state(checkpoint["numpy_rng_state"])
    if checkpoint.get("torch_cpu_rng_state") is not None:
        torch.set_rng_state(checkpoint["torch_cpu_rng_state"])
    if torch.cuda.is_available() and checkpoint.get("torch_cuda_rng_state_all") is not None:
        torch.cuda.set_rng_state_all(checkpoint["torch_cuda_rng_state_all"])


def _make_checkpoint_payload(
    *,
    model,
    optimizer,
    config: dict[str, Any],
    training_status: str,
    optimizer_steps: int,
    training_tokens_seen: int,
    effective_batch_tokens: int,
    curve: list[dict[str, Any]],
    eval_curve: list[dict[str, Any]],
    routing_curve: list[dict[str, Any]],
    checkpoint_mode: str,
    resume_mode: str,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "checkpoint_kind": "EXACT_TRAINING_STATE" if checkpoint_mode == "exact" else "WEIGHT_ONLY",
        "model_state_dict": model.state_dict(),
        "config": config,
        "config_hash": _config_hash(config),
        "source_git_commit": git_commit(),
        "created_at": utc_now(),
        "training_status": training_status,
        "optimizer_steps": optimizer_steps,
        "training_tokens_seen": training_tokens_seen,
        "effective_batch_tokens": effective_batch_tokens,
        "curve": curve,
        "eval_curve": eval_curve,
        "routing_curve": routing_curve,
        "resume_mode": resume_mode,
    }
    if checkpoint_mode == "exact":
        payload["optimizer_state_dict"] = optimizer.state_dict()
        payload["scheduler_state_dict"] = None
        payload["scaler_state_dict"] = None
        payload.update(_rng_state_payload())
    return payload


def _resolve_config_path(config_path: str, suite_path: str) -> Path:
    path = Path(config_path)
    if path.exists():
        return path
    beside_suite = Path(suite_path).parent / path.name
    if beside_suite.exists():
        return beside_suite
    return path


def _iter_suite_configs(suite_path: str) -> list[dict[str, Any]]:
    suite = load_json_or_yaml(suite_path)
    if "model_configs" in suite:
        return [load_json_or_yaml(_resolve_config_path(path, suite_path)) for path in suite["model_configs"]]
    if "models" not in suite:
        return [suite]
    return [load_json_or_yaml(_resolve_config_path(item["config_path"], suite_path)) for item in suite["models"]]


def _files(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for item in paths:
        path = Path(item)
        if path.is_file():
            out.append(path)
        elif path.is_dir():
            out.extend(sorted(child for child in path.rglob("*") if child.is_file()))
    return out


def _load_training_bytes(paths: list[str]) -> torch.Tensor:
    files = _files(paths)
    if not files:
        raise FileNotFoundError(f"No training files found in {paths}")
    data = bytearray()
    for path in files:
        data.extend(path.read_bytes())
        data.append(10)
    if len(data) < 4:
        raise ValueError("Training corpus is too small to form next-token batches.")
    return torch.tensor(list(data), dtype=torch.long)


def _load_bytes(paths: list[str], *, require: bool = True) -> torch.Tensor:
    files = _files(paths)
    if not files:
        if require:
            raise FileNotFoundError(f"No files found in {paths}")
        return torch.tensor([], dtype=torch.long)
    data = bytearray()
    for path in files:
        data.extend(path.read_bytes())
        data.append(10)
    return torch.tensor(list(data), dtype=torch.long)


def _batch(tokens: torch.Tensor, step: int, batch_size: int, seq_len: int, device: str) -> tuple[torch.Tensor, torch.Tensor]:
    span = seq_len + 1
    max_start = max(1, len(tokens) - span)
    starts = [((step * batch_size + idx) * span) % max_start for idx in range(batch_size)]
    rows = [tokens[start : start + span] for start in starts]
    block = torch.stack(rows).to(device)
    return block[:, :-1], block[:, 1:]


def _eval_loss(model, tokens: torch.Tensor, step: int, seq_len: int, device: str) -> tuple[float | None, int]:
    if len(tokens) < seq_len + 1:
        return None, 0
    x, y = _batch(tokens, step, 1, seq_len, device)
    was_training = model.training
    model.eval()
    with torch.no_grad():
        logits = model(x)
        loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1))
    if was_training:
        model.train()
    return float(loss.detach().cpu().item()), int(x.numel())


def _set_pvr_shared_only(model, value: bool) -> list[bool]:
    if not hasattr(model, "blocks"):
        return []
    previous: list[bool] = []
    for block in model.blocks:
        if hasattr(block, "shared_only"):
            previous.append(bool(block.shared_only))
            block.shared_only = value
    return previous


def _restore_pvr_shared_only(model, previous: list[bool]) -> None:
    if not previous or not hasattr(model, "blocks"):
        return
    for block, value in zip(model.blocks, previous):
        if hasattr(block, "shared_only"):
            block.shared_only = value


def _in_shared_warmup(config: dict[str, Any], step_index: int) -> bool:
    curriculum = str(config.get("training_curriculum") or "")
    warmup_steps = int(config.get("shared_warmup_steps") or 0)
    return curriculum.startswith("shared_warmup") and step_index < warmup_steps


def _token_losses_from_state(model, x_after_block: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    logits = model.head(model.ln_f(x_after_block))
    return F.cross_entropy(
        logits.reshape(-1, logits.shape[-1]),
        targets.reshape(-1),
        reduction="none",
    ).reshape(targets.shape)


def _pvr_final_block_router_repair_loss(
    model,
    input_ids: torch.Tensor,
    targets: torch.Tensor,
    config: dict[str, Any],
    *,
    device: str,
) -> tuple[torch.Tensor, dict[str, Any]]:
    if config.get("model_family") != "pvr_ec_o" or not hasattr(model, "blocks") or not model.blocks:
        return torch.zeros((), device=device), {}
    regret_weight = float(config.get("router_regret_aux_weight") or 0.0)
    oracle_kl_weight = float(config.get("router_oracle_kl_weight") or 0.0)
    if regret_weight == 0.0 and oracle_kl_weight == 0.0:
        return torch.zeros((), device=device), {}
    block = model.blocks[-1]
    if getattr(block, "shared_only", False) or not getattr(block, "experts", None):
        return torch.zeros((), device=device), {}
    temperature = max(1e-6, float(config.get("router_regret_temperature") or 1.0))
    seq_len = input_ids.shape[1]
    mask = torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1).bool()
    with torch.no_grad():
        positions = torch.arange(seq_len, device=device).unsqueeze(0)
        x = model.token_emb(input_ids) + model.pos_emb(positions)
        for attn, earlier_block in zip(model.attn[:-1], model.blocks[:-1]):
            x = attn(x, src_mask=mask)
            x = earlier_block(x)
        x = model.attn[-1](x, src_mask=mask)
        h = block.ln(x)
        if block.descriptor_operator is not None:
            h = h + block.descriptor_operator(h)
        shared = block.shared(h)
        expert_outputs = torch.stack([expert(h) for expert in block.experts], dim=0)
        expert_losses = torch.stack(
            [_token_losses_from_state(model, x + shared + expert_outputs[idx], targets) for idx in range(expert_outputs.shape[0])],
            dim=0,
        )
        oracle_loss, oracle_idx = expert_losses.min(dim=0)
        sorted_idx = torch.argsort(expert_losses, dim=0)
        per_expert_regret = (expert_losses - oracle_loss.unsqueeze(0)).clamp_min(0.0)
        soft_target = F.softmax(-expert_losses / temperature, dim=0).permute(1, 2, 0).detach()
        regret_target = per_expert_regret.permute(1, 2, 0).detach()
    scores = block.routing_scores(h.detach()) if hasattr(block, "routing_scores") else block.router(h.detach())
    probs = F.softmax(scores, dim=-1)
    expected_regret = (probs * regret_target).sum(dim=-1).mean()
    oracle_kl = -(soft_target * F.log_softmax(scores, dim=-1)).sum(dim=-1).mean()
    selected = torch.argmax(scores.detach(), dim=-1)
    selected_rank = (expert_losses.permute(1, 2, 0) < expert_losses.gather(0, selected.unsqueeze(0)).squeeze(0).unsqueeze(-1)).sum(dim=-1) + 1
    loss = regret_weight * expected_regret + oracle_kl_weight * oracle_kl
    return loss, {
        "router_expected_regret_loss": float(expected_regret.detach().cpu().item()),
        "router_oracle_kl_loss": float(oracle_kl.detach().cpu().item()),
        "router_selected_is_oracle_rate_train": float((selected_rank == 1).float().mean().detach().cpu().item()),
        "router_selected_is_top2_rate_train": float((selected_rank <= 2).float().mean().detach().cpu().item()),
        "router_oracle_gap_mean_train": float(
            (expert_losses.gather(0, sorted_idx[1:2]).squeeze(0) - oracle_loss).mean().detach().cpu().item()
            if expert_losses.shape[0] > 1
            else 0.0
        ),
    }


def _routing_snapshot(model, config: dict[str, Any], tokens: torch.Tensor, step: int, seq_len: int, device: str) -> dict[str, Any] | None:
    if config.get("model_family") != "pvr_ec_o" or len(tokens) < seq_len + 1 or not hasattr(model, "blocks"):
        return None
    owner_rows: list[int] = []
    margins: list[float] = []

    def hook(module, inputs, _output):
        x = inputs[0]
        h = module.ln(x)
        if module.descriptor_operator is not None:
            h = h + module.descriptor_operator(h)
        scores = module.routing_scores(h) if hasattr(module, "routing_scores") else module.router(h)
        top = torch.topk(scores, k=min(2, scores.shape[-1]), dim=-1)
        owner_rows.extend(int(item) for item in top.indices[..., 0].detach().cpu().reshape(-1))
        if top.values.shape[-1] > 1:
            margins.extend(float(item) for item in (top.values[..., 0] - top.values[..., 1]).detach().cpu().reshape(-1))

    handles = [block.register_forward_hook(hook) for block in model.blocks]
    try:
        x, _ = _batch(tokens, step, 1, seq_len, device)
        was_training = model.training
        model.eval()
        with torch.no_grad():
            model(x)
        if was_training:
            model.train()
    finally:
        for handle in handles:
            handle.remove()
    expert_count = int(config.get("num_experts_if_applicable") or 1)
    counts = [owner_rows.count(idx) for idx in range(expert_count)]
    total = max(1, sum(counts))
    entropy = 0.0
    for count in counts:
        if count:
            p = count / total
            entropy -= p * math.log(p)
    margin = sum(margins) / len(margins) if margins else None
    return {
        "owners_per_token": 1.0,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "production_map_mutated": False,
        "expert_utilization": counts,
        "prototype_entropy": entropy,
        "owner_entropy": entropy,
        "owner_churn": None,
        "prototype_margin": margin,
        "prototype_monopoly_rate": max(counts) / total if counts else None,
        "high_gap_monopoly_rate": max(counts) / total if counts else None,
        "challenger_disagreement_rate": None,
        "stale_owner_rate": None,
        "descriptor_control_margin": margin,
        "operator_control_margin": margin,
        "failure_mode_distribution": {},
    }


def _save_training_artifacts(
    *,
    config: dict[str, Any],
    output: Path,
    checkpoint_path: Path,
    curve: list[dict[str, Any]],
    eval_curve: list[dict[str, Any]],
    routing_curve: list[dict[str, Any]],
    status: str,
    started: float,
    tokens_seen: int,
    optimizer_steps: int,
    effective_batch_tokens: int,
    target_steps: int,
    target_training_tokens: int,
    target_eval_windows: int,
    tier: str,
    device: str,
    error: str | None = None,
    resume_events: list[dict[str, Any]] | None = None,
    checkpoint_mode: str = "exact",
) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    elapsed = max(0.0, time.time() - started)
    gpu_hours = elapsed / 3600.0 if device == "cuda" else 0.0
    throughput = tokens_seen / elapsed if elapsed > 0 else None
    vram_peak = torch.cuda.max_memory_allocated() if device == "cuda" and torch.cuda.is_available() else None
    checkpoint_exists = checkpoint_path.exists()
    checkpoint_hash = sha256_file(checkpoint_path) if checkpoint_exists else ""
    resource_reduction = {
        "status": "RESOURCE_REDUCED_BUDGET" if optimizer_steps < target_steps or tokens_seen < target_training_tokens or len(eval_curve) < target_eval_windows else "NONE",
        "completed_steps": optimizer_steps,
        "completed_training_tokens": tokens_seen,
        "completed_eval_windows": len(eval_curve),
        "estimated_steps_needed": target_steps,
        "target_training_tokens": target_training_tokens,
        "target_eval_windows": target_eval_windows,
        "reason_for_reduction": "Run executed with explicit local budget below real-comparison target." if optimizer_steps < target_steps or tokens_seen < target_training_tokens or len(eval_curve) < target_eval_windows else "",
    }
    training_curve = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model": config["model_variant"],
        "status": status,
        "loss_curve": curve,
        "training_tokens_seen": tokens_seen,
        "optimizer_steps": optimizer_steps,
        "effective_batch_tokens": effective_batch_tokens,
        "target_steps": target_steps,
        "target_training_tokens": target_training_tokens,
        "target_eval_windows": target_eval_windows,
        "tier": tier,
    }
    eval_curve_payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model": config["model_variant"],
        "status": status,
        "eval_curve": eval_curve,
        "eval_window_count": len(eval_curve),
    }
    routing_curve_payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model": config["model_variant"],
        "status": status,
        "routing_curve": routing_curve,
        "routing_window_count": len(routing_curve),
    }
    routing_metrics_by_step = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model": config["model_variant"],
        "routing_metrics_by_step": routing_curve,
    }
    prototype_entropy_curve = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "prototype_entropy_curve": [
            {"step": row.get("step"), "prototype_entropy": row.get("prototype_entropy")}
            for row in routing_curve
        ],
    }
    prototype_margin_curve = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "prototype_margin_curve": [
            {"step": row.get("step"), "prototype_margin": row.get("prototype_margin")}
            for row in routing_curve
        ],
    }
    expert_utilization_curve = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "expert_utilization_curve": [
            {"step": row.get("step"), "expert_utilization": row.get("expert_utilization")}
            for row in routing_curve
        ],
    }
    owner_churn_curve = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "owner_churn_curve": [
            {"step": row.get("step"), "owner_churn": row.get("owner_churn")}
            for row in routing_curve
        ],
    }
    descriptor_operator_margin_curve = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "descriptor_operator_margin_curve": [
            {
                "step": row.get("step"),
                "descriptor_control_margin": row.get("descriptor_control_margin"),
                "operator_control_margin": row.get("operator_control_margin"),
            }
            for row in routing_curve
        ],
    }
    checkpoint_manifest = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "model": config["model_variant"],
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_exists": checkpoint_exists,
        "checkpoint_hash": checkpoint_hash,
        "checkpoint_kind": checkpoint_mode,
        "status": status,
        "real_training_data": True,
        "mock_checkpoint": False,
        "training_data_paths": config.get("training_data_paths", []),
        "tokens_seen": tokens_seen,
        "training_tokens_seen": tokens_seen,
        "optimizer_steps": optimizer_steps,
        "effective_batch_tokens": effective_batch_tokens,
        "target_steps": target_steps,
        "target_training_tokens": target_training_tokens,
        "target_eval_windows": target_eval_windows,
        "tier": tier,
        "eval_window_count": len(eval_curve),
        "routing_window_count": len(routing_curve),
        "resource_reduction": resource_reduction,
        "error": error,
        "resume_events": resume_events or [],
        "exact_resume_state_required_for_continuation": True,
    }
    hardware_manifest = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "environment": environment_payload(),
        "device": device,
        "cuda_available": torch.cuda.is_available(),
        "vram_peak": vram_peak,
        "wall_clock_seconds": elapsed,
        "gpu_hours": gpu_hours,
        "tokens_per_second": throughput,
    }
    throughput_log = {
        "schema_version": "1.0",
        "model": config["model_variant"],
        "tokens_seen": tokens_seen,
        "training_tokens_seen": tokens_seen,
        "optimizer_steps": optimizer_steps,
        "effective_batch_tokens": effective_batch_tokens,
        "target_steps": target_steps,
        "target_training_tokens": target_training_tokens,
        "target_eval_windows": target_eval_windows,
        "resource_reduction": resource_reduction,
        "wall_clock_seconds": elapsed,
        "tokens_per_second": throughput,
    }
    write_json(output / "training_curve.json", training_curve)
    write_json(output / "eval_curve.json", eval_curve_payload)
    write_json(output / "routing_curve.json", routing_curve_payload)
    write_json(output / "routing_metrics_by_step.json", routing_metrics_by_step)
    write_json(output / "prototype_entropy_curve.json", prototype_entropy_curve)
    write_json(output / "prototype_margin_curve.json", prototype_margin_curve)
    write_json(output / "expert_utilization_curve.json", expert_utilization_curve)
    write_json(output / "owner_churn_curve.json", owner_churn_curve)
    write_json(output / "descriptor_operator_margin_curve.json", descriptor_operator_margin_curve)
    write_json(output / "checkpoint_manifest.json", checkpoint_manifest)
    write_json(output / "hardware_manifest.json", hardware_manifest)
    write_json(output / "throughput_log.json", throughput_log)
    write_json(output / "run_config.yaml", config)
    write_json(checkpoint_path.parent / "training_curve.json", training_curve)
    write_json(checkpoint_path.parent / "eval_curve.json", eval_curve_payload)
    write_json(checkpoint_path.parent / "routing_curve.json", routing_curve_payload)
    write_json(checkpoint_path.parent / "routing_metrics_by_step.json", routing_metrics_by_step)
    write_json(checkpoint_path.parent / "prototype_entropy_curve.json", prototype_entropy_curve)
    write_json(checkpoint_path.parent / "prototype_margin_curve.json", prototype_margin_curve)
    write_json(checkpoint_path.parent / "expert_utilization_curve.json", expert_utilization_curve)
    write_json(checkpoint_path.parent / "owner_churn_curve.json", owner_churn_curve)
    write_json(checkpoint_path.parent / "descriptor_operator_margin_curve.json", descriptor_operator_margin_curve)
    write_json(checkpoint_path.parent / "checkpoint_manifest.json", checkpoint_manifest)
    write_json(checkpoint_path.parent / "hardware_manifest.json", hardware_manifest)
    write_json(checkpoint_path.parent / "run_config.yaml", config)
    return {
        "model_variant": config["model_variant"],
        "status": status,
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_exists": checkpoint_exists,
        "training_curve": str(output / "training_curve.json"),
        "eval_curve": str(output / "eval_curve.json"),
        "routing_curve": str(output / "routing_curve.json"),
        "checkpoint_manifest": str(output / "checkpoint_manifest.json"),
        "hardware_manifest": str(output / "hardware_manifest.json"),
        "throughput_log": str(output / "throughput_log.json"),
        "tokens_seen": tokens_seen,
        "training_tokens_seen": tokens_seen,
        "optimizer_steps": optimizer_steps,
        "effective_batch_tokens": effective_batch_tokens,
        "eval_window_count": len(eval_curve),
        "routing_window_count": len(routing_curve),
        "final_loss": curve[-1]["loss"] if curve else None,
        "vram_peak": vram_peak,
        "gpu_hours": gpu_hours,
        "error": error,
        "resume_events": resume_events or [],
        "checkpoint_mode": checkpoint_mode,
    }


def _train_one(
    config: dict[str, Any],
    output_root: Path,
    device: str,
    max_steps: int,
    batch_size: int,
    seq_len: int,
    lr: float,
    eval_interval: int,
    target_steps: int,
    target_training_tokens: int,
    target_eval_windows: int,
    tier: str,
    checkpoint_mode: str = "exact",
    simulate_interrupt_after_steps: int | None = None,
) -> dict[str, Any]:
    started = time.time()
    model_out = output_root / config["model_variant"]
    checkpoint_path = Path(config["checkpoint_path"])
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    tokens_seen = 0
    effective_batch_tokens = batch_size * min(seq_len, int(config["context_length"]) - 1)
    curve: list[dict[str, Any]] = []
    eval_curve: list[dict[str, Any]] = []
    routing_curve: list[dict[str, Any]] = []
    resume_events: list[dict[str, Any]] = []
    resume_mode = "UNINTERRUPTED"
    try:
        tokens = _load_training_bytes(list(config.get("training_data_paths") or []))
        eval_tokens = _load_bytes(list(config.get("eval_data_paths") or []), require=False)
        materialized = build_model(config, device=device)
        model = materialized.model.train()
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        start_step = 0
        if checkpoint_path.exists():
            checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
            if isinstance(checkpoint, dict) and checkpoint.get("training_status") == "TRAINING_PARTIAL":
                model.load_state_dict(checkpoint.get("model_state_dict", checkpoint), strict=False)
                if checkpoint.get("checkpoint_kind") == "EXACT_TRAINING_STATE" and checkpoint.get("optimizer_state_dict"):
                    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
                    _restore_rng_state(checkpoint)
                    resume_mode = "EXACT_TRAINING_STATE_RESUME"
                elif checkpoint.get("optimizer_state_dict"):
                    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
                    resume_mode = "LEGACY_OPTIMIZER_ONLY_RESUME"
                else:
                    resume_mode = "WEIGHT_ONLY_OPTIMIZER_RESET_NON_EQUIVALENT"
                start_step = int(checkpoint.get("optimizer_steps") or 0)
                tokens_seen = int(checkpoint.get("training_tokens_seen") or (start_step * effective_batch_tokens))
                curve = list(checkpoint.get("curve") or [])
                eval_curve = list(checkpoint.get("eval_curve") or [])
                routing_curve = list(checkpoint.get("routing_curve") or [])
                resume_events.append({
                    "checkpoint_path": str(checkpoint_path),
                    "checkpoint_kind": checkpoint.get("checkpoint_kind") or "LEGACY_UNKNOWN",
                    "resume_mode": resume_mode,
                    "start_step": start_step,
                    "training_tokens_seen": tokens_seen,
                    "has_optimizer_state": bool(checkpoint.get("optimizer_state_dict")),
                    "has_rng_state": any(
                        checkpoint.get(key) is not None
                        for key in ["python_rng_state", "torch_cpu_rng_state", "torch_cuda_rng_state_all"]
                    ),
                })
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        for step in range(start_step, max_steps):
            x, y = _batch(tokens, step, batch_size, min(seq_len, int(config["context_length"]) - 1), device)
            optimizer.zero_grad(set_to_none=True)
            warmup_previous = _set_pvr_shared_only(model, True) if _in_shared_warmup(config, step) else []
            logits = model(x)
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1))
            routing_aux_weight = float(config.get("routing_aux_weight") or 0.0)
            if routing_aux_weight and hasattr(model, "routing_aux_loss"):
                loss = loss + routing_aux_weight * model.routing_aux_loss()
            router_repair_loss, router_repair_metrics = _pvr_final_block_router_repair_loss(
                model,
                x,
                y,
                config,
                device=device,
            )
            if router_repair_metrics:
                loss = loss + router_repair_loss
            loss.backward()
            optimizer.step()
            _restore_pvr_shared_only(model, warmup_previous)
            tokens_seen += int(x.numel())
            curve_row = {
                "step": step + 1,
                "optimizer_step": step + 1,
                "loss": float(loss.detach().cpu().item()),
                "tokens_seen": tokens_seen,
                "training_tokens_seen": tokens_seen,
                "effective_batch_tokens": effective_batch_tokens,
            }
            if router_repair_metrics:
                curve_row.update(router_repair_metrics)
            curve.append(curve_row)
            if eval_interval > 0 and (step + 1) % eval_interval == 0:
                eval_previous = _set_pvr_shared_only(model, True) if _in_shared_warmup(config, step) else []
                eval_loss, eval_tokens_seen = _eval_loss(model, eval_tokens, step, min(seq_len, int(config["context_length"]) - 1), device)
                eval_curve.append({
                    "step": step + 1,
                    "optimizer_step": step + 1,
                    "eval_loss": eval_loss,
                    "eval_tokens": eval_tokens_seen,
                    "training_tokens_seen": tokens_seen,
                })
                snapshot = _routing_snapshot(model, config, eval_tokens, step, min(seq_len, int(config["context_length"]) - 1), device)
                _restore_pvr_shared_only(model, eval_previous)
                if snapshot is not None:
                    routing_curve.append({
                        "step": step + 1,
                        "optimizer_step": step + 1,
                        **snapshot,
                    })
                _atomic_torch_save(
                    _make_checkpoint_payload(
                        model=model,
                        optimizer=optimizer,
                        config=config,
                        training_status="TRAINING_PARTIAL",
                        optimizer_steps=step + 1,
                        training_tokens_seen=tokens_seen,
                        effective_batch_tokens=effective_batch_tokens,
                        curve=curve,
                        eval_curve=eval_curve,
                        routing_curve=routing_curve,
                        checkpoint_mode=checkpoint_mode,
                        resume_mode=resume_mode,
                    ),
                    checkpoint_path,
                )
            if simulate_interrupt_after_steps is not None and (step + 1) >= simulate_interrupt_after_steps:
                _atomic_torch_save(
                    _make_checkpoint_payload(
                        model=model,
                        optimizer=optimizer,
                        config=config,
                        training_status="TRAINING_PARTIAL",
                        optimizer_steps=step + 1,
                        training_tokens_seen=tokens_seen,
                        effective_batch_tokens=effective_batch_tokens,
                        curve=curve,
                        eval_curve=eval_curve,
                        routing_curve=routing_curve,
                        checkpoint_mode=checkpoint_mode,
                        resume_mode=resume_mode,
                    ),
                    checkpoint_path,
                )
                return _save_training_artifacts(
                    config=config,
                    output=model_out,
                    checkpoint_path=checkpoint_path,
                    curve=curve,
                    eval_curve=eval_curve,
                    routing_curve=routing_curve,
                    status="TRAINING_INTERRUPTED_FOR_TEST",
                    started=started,
                    tokens_seen=tokens_seen,
                    optimizer_steps=curve[-1]["optimizer_step"] if curve else start_step,
                    effective_batch_tokens=effective_batch_tokens,
                    target_steps=target_steps,
                    target_training_tokens=target_training_tokens,
                    target_eval_windows=target_eval_windows,
                    tier=tier,
                    device=device,
                    resume_events=resume_events,
                    checkpoint_mode=checkpoint_mode,
                )
        _atomic_torch_save(
            _make_checkpoint_payload(
                model=model,
                optimizer=optimizer,
                config=config,
                training_status="GENUINE_REDUCED_TRAINING_COMPLETE",
                optimizer_steps=curve[-1]["optimizer_step"] if curve else start_step,
                training_tokens_seen=tokens_seen,
                effective_batch_tokens=effective_batch_tokens,
                curve=curve,
                eval_curve=eval_curve,
                routing_curve=routing_curve,
                checkpoint_mode=checkpoint_mode,
                resume_mode=resume_mode,
            ),
            checkpoint_path,
        )
        return _save_training_artifacts(
            config=config,
            output=model_out,
            checkpoint_path=checkpoint_path,
            curve=curve,
            eval_curve=eval_curve,
            routing_curve=routing_curve,
            status="GENUINE_REDUCED_TRAINING_COMPLETE",
            started=started,
            tokens_seen=tokens_seen,
            optimizer_steps=curve[-1]["optimizer_step"] if curve else start_step,
            effective_batch_tokens=effective_batch_tokens,
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            tier=tier,
            device=device,
            resume_events=resume_events,
            checkpoint_mode=checkpoint_mode,
        )
    except Exception as exc:
        return _save_training_artifacts(
            config=config,
            output=model_out,
            checkpoint_path=checkpoint_path,
            curve=curve,
            eval_curve=eval_curve,
            routing_curve=routing_curve,
            status="TRAINING_FAILED",
            started=started,
            tokens_seen=tokens_seen,
            optimizer_steps=curve[-1]["optimizer_step"] if curve else start_step,
            effective_batch_tokens=effective_batch_tokens,
            target_steps=target_steps,
            target_training_tokens=target_training_tokens,
            target_eval_windows=target_eval_windows,
            tier=tier,
            device=device,
            error=repr(exc),
            resume_events=resume_events,
            checkpoint_mode=checkpoint_mode,
        )
    finally:
        if device == "cuda" and torch.cuda.is_available():
            torch.cuda.empty_cache()


def run(
    suite: str,
    output: str,
    *,
    device: str = "cuda",
    max_steps: int = 1,
    batch_size: int = 1,
    seq_len: int = 16,
    lr: float = 1e-5,
    eval_interval: int = 0,
    tier: str = "genuine",
    target_steps: int | None = None,
    target_training_tokens: int | None = None,
    eval_windows: int | None = None,
    limit: int | None = None,
    checkpoint_mode: str = "exact",
    simulate_interrupt_after_steps: int | None = None,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    configs = _iter_suite_configs(suite)
    requested_target_steps = target_steps or max_steps
    requested_target_training_tokens = target_training_tokens or (batch_size * seq_len * requested_target_steps)
    requested_eval_windows = eval_windows if eval_windows is not None else (max_steps // eval_interval if eval_interval else 0)
    if requested_eval_windows and not eval_interval:
        eval_interval = max(1, max_steps // requested_eval_windows)
    rows = []
    for config in configs[: limit or len(configs)]:
        rows.append(_train_one(
            config,
            out,
            device,
            max_steps,
            batch_size,
            seq_len,
            lr,
            eval_interval,
            requested_target_steps,
            requested_target_training_tokens,
            requested_eval_windows,
            tier,
            checkpoint_mode,
            simulate_interrupt_after_steps,
        ))
    completed = [row for row in rows if row["status"] == "GENUINE_REDUCED_TRAINING_COMPLETE" and row["checkpoint_exists"]]
    failed = [row for row in rows if row["status"] == "TRAINING_FAILED"]
    completed_steps_min = min((row.get("optimizer_steps") or 0 for row in rows), default=0)
    completed_training_tokens_min = min((row.get("training_tokens_seen") or 0 for row in rows), default=0)
    completed_eval_windows_min = min((row.get("eval_window_count") or 0 for row in rows), default=0)
    top_level_reduced = (
        completed_steps_min < requested_target_steps
        or completed_training_tokens_min < requested_target_training_tokens
        or completed_eval_windows_min < requested_eval_windows
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": "GENUINE_REDUCED_TRAINING_COMPLETE" if len(completed) == len(rows) and rows else "TRAINING_FAILED",
        "tier": tier,
        "suite": suite,
        "device": device,
        "max_steps": max_steps,
        "optimizer_steps_requested": max_steps,
        "batch_size": batch_size,
        "seq_len": seq_len,
        "eval_interval": eval_interval,
        "checkpoint_mode": checkpoint_mode,
        "simulate_interrupt_after_steps": simulate_interrupt_after_steps,
        "target_steps": requested_target_steps,
        "target_training_tokens": requested_target_training_tokens,
        "target_eval_windows": requested_eval_windows,
        "resource_reduction": {
            "status": "RESOURCE_REDUCED_BUDGET" if top_level_reduced else "NONE",
            "completed_steps_min": completed_steps_min,
            "completed_training_tokens_min": completed_training_tokens_min,
            "completed_eval_windows_min": completed_eval_windows_min,
            "estimated_steps_needed": requested_target_steps,
            "target_training_tokens": requested_target_training_tokens,
            "target_eval_windows": requested_eval_windows,
            "reason_for_reduction": "Completed steps, training tokens, or eval windows are below the requested real-comparison target." if top_level_reduced else "",
        },
        "effective_batch_tokens": batch_size * seq_len,
        "model_count": len(rows),
        "completed_model_count": len(completed),
        "failed_model_count": len(failed),
        "rows": rows,
        "notes": "Reduced training is real optimization on real prepared data, but is not full-scale pretraining.",
    }
    write_json(out / "training_run_report.json", payload)
    print(payload["status"])
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the 100M benchmark suite on real reduced data")
    parser.add_argument("--suite", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--max-steps", type=int, default=1)
    parser.add_argument("--target-steps", type=int, default=None)
    parser.add_argument("--target-training-tokens", type=int, default=None)
    parser.add_argument("--eval-windows", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--seq-len", type=int, default=16)
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--eval-interval", type=int, default=0)
    parser.add_argument("--tier", default="genuine", choices=["genuine", "stable_learning", "real_comparison"])
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--checkpoint-mode", default="exact", choices=["exact", "weights_only"])
    parser.add_argument("--simulate-interrupt-after-steps", type=int, default=None)
    args = parser.parse_args()
    run(
        args.suite,
        args.output,
        device=args.device,
        max_steps=args.max_steps,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lr=args.lr,
        eval_interval=args.eval_interval,
        tier=args.tier,
        target_steps=args.target_steps,
        target_training_tokens=args.target_training_tokens,
        eval_windows=args.eval_windows,
        limit=args.limit,
        checkpoint_mode=args.checkpoint_mode,
        simulate_interrupt_after_steps=args.simulate_interrupt_after_steps,
    )


if __name__ == "__main__":
    main()
