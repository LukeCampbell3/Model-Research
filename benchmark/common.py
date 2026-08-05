"""Shared utilities for the PVR-EC-O benchmark harness."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ARCHITECTURE_STATUSES = {
    "PVR_EC_O_LOSES_TO_GENERALIZED_BASELINES",
    "PVR_EC_O_PARAMETER_EFFICIENT_ONLY",
    "PVR_EC_O_ROUTING_ADVANTAGE_ON_STRUCTURED_TASKS",
    "PVR_EC_O_GENERALIZED_BASELINE_COMPETITIVE",
    "PVR_EC_O_GENERALIZED_BASELINE_WIN",
    "PVR_EC_O_BROAD_NLP_COMPETITIVE",
    "PVR_EC_O_CODE_COMPETITIVE",
    "PVR_EC_O_INTERNAL_STRONG_ROUTER_COMPETITIVE",
    "PVR_EC_O_BEATS_GENERALIZED_BASELINES_BUT_LAGS_INTERNAL_STRONG_ROUTER",
}

INFRASTRUCTURE_STATUSES = {
    "BENCH_INFRASTRUCTURE_READY",
    "BENCH_INFRASTRUCTURE_INCOMPLETE",
    "GENUINE_REDUCED_PIPELINE_COMPLETE",
    "GENUINE_REDUCED_BENCHMARK_COMPLETE",
    "RESOURCE_REDUCED_BUDGET",
    "NOT_RUN_RESOURCE_BLOCKED",
    "NOT_RUN_MISSING_CHECKPOINT",
    "NOT_RUN_MISSING_DATA",
    "SEED_REDUCTION_RESOURCE_BLOCKED",
    "TRAINING_FAILED",
    "EVAL_FAILED",
    "NOT_RUN_NOT_IMPLEMENTED",
    "CONTAMINATION_STATUS_UNKNOWN",
    "PVR_EC_O_ROUTING_INVARIANT_FAILED",
}

GENUINE_STAGE_STATUSES = {
    "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE",
    "PVR_EC_O_100M_STABLE_LEARNING_BENCHMARK_COMPLETE",
    "PVR_EC_O_100M_REAL_COMPARISON_COMPLETE",
    "PVR_EC_O_300M_GENUINE_BENCHMARK_COMPLETE",
    "PVR_EC_O_300M_REAL_COMPARISON_COMPLETE",
    "PVR_EC_O_700M_GENUINE_BENCHMARK_COMPLETE",
    "PVR_EC_O_700M_REAL_COMPARISON_COMPLETE",
    "PVR_EC_O_MULTI_SIZE_SCALING_COMPLETE",
    "PVR_EC_O_BROAD_NLP_SCALE_POSITIONED",
    "PVR_EC_O_CODE_SCALE_POSITIONED",
    "PVR_EC_O_1_3B_PROMOTION_TIER_EVALUATED",
    "PVR_EC_O_INTERNAL_STRONG_ROUTER_EVALUATED",
}

REQUIRED_MODEL_CONFIG_FIELDS = [
    "model_family",
    "model_variant",
    "model_size_label",
    "total_params",
    "active_params_per_token",
    "active_flops_estimate",
    "num_layers",
    "hidden_size",
    "num_heads",
    "num_experts_if_applicable",
    "experts_active_per_token",
    "context_length",
    "training_tokens",
    "batch_tokens",
    "optimizer",
    "scheduler",
    "eval_suite",
    "output_path",
    "comparison_group",
    "is_primary_baseline",
    "is_internal_strong_router_control",
]

SCORECARD_COMMON_FIELDS = [
    "model",
    "checkpoint",
    "training_tokens",
    "total_params",
    "active_params_per_token",
    "context_length",
    "tokenizer",
    "training_data_manifest_hash",
    "eval_manifest_hash",
    "contamination_scan",
    "hardware",
    "wall_clock",
    "gpu_hours",
    "vram_peak",
    "throughput",
]

ROUTING_INVARIANT_FIELDS = [
    "owners_per_token",
    "top2_execution_count",
    "top4_execution_count",
    "runtime_dynamic_k_count",
    "runtime_expert_choice_count",
    "production_map_mutated",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return ""


def load_json_or_yaml(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {p}")
    text = p.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{p} must be JSON-compatible YAML for this stdlib runner. "
            "Regenerate configs with benchmark/scripts/generate_model_size_matrix.py."
        ) from exc


def write_json(path: str | Path, payload: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8")


def sha256_file(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_paths(paths: list[str]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for item in paths:
        p = Path(item)
        if p.is_file():
            hashes[str(p)] = sha256_file(p)
        elif p.is_dir():
            for child in sorted(x for x in p.rglob("*") if x.is_file()):
                hashes[str(child)] = sha256_file(child)
    return hashes


def environment_payload() -> dict[str, Any]:
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cwd": str(Path.cwd()),
    }


def manifest_payload(source_paths: list[str], notes: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "source_paths": source_paths,
        "hashes": hash_paths(source_paths),
        "environment": environment_payload(),
        "notes": notes,
    }


def require_fields(payload: dict[str, Any], fields: list[str], label: str) -> None:
    missing = [field for field in fields if field not in payload]
    if missing:
        raise ValueError(f"{label} missing required fields: {', '.join(missing)}")


def checkpoint_status(config: dict[str, Any], *, infrastructure_only: bool = False) -> str | None:
    checkpoint = str(config.get("checkpoint_path") or "")
    if not checkpoint:
        return "NOT_RUN_MISSING_CHECKPOINT"
    if "mock" in checkpoint.lower() and not infrastructure_only:
        raise ValueError("Mock checkpoints are rejected outside infrastructure-only validation.")
    if not Path(checkpoint).exists():
        return "NOT_RUN_MISSING_CHECKPOINT"
    return None


def data_status(config: dict[str, Any]) -> str | None:
    required_paths = list(config.get("eval_data_paths") or [])
    if not required_paths:
        return "NOT_RUN_MISSING_DATA"
    if any(not Path(path).exists() for path in required_paths):
        return "NOT_RUN_MISSING_DATA"
    return None


def base_metadata(config: dict[str, Any], limit: int | None = None) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "environment": environment_payload(),
        "limit": limit,
        "benchmark_subset_label": "genuine_reduced_eval" if limit else "genuine_full_eval",
        "benchmark_evidence": False,
        "notes": "No benchmark evidence is claimed unless real checkpoint and data are present.",
        "config": config,
    }


def manifest_hash(path: str | Path) -> str:
    p = Path(path)
    return sha256_file(p) if p.exists() else ""


def common_scorecard(config: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": config.get("model_variant"),
        "checkpoint": config.get("checkpoint_path", ""),
        "training_tokens": config.get("training_tokens"),
        "total_params": config.get("total_params"),
        "active_params_per_token": config.get("active_params_per_token"),
        "context_length": config.get("context_length"),
        "tokenizer": config.get("tokenizer", "tiktoken_compatible_bpe"),
        "training_data_manifest_hash": manifest_hash("benchmark/manifests/training_data_manifest.json"),
        "eval_manifest_hash": manifest_hash("benchmark/manifests/eval_manifest.json"),
        "contamination_scan": "CONTAMINATION_STATUS_UNKNOWN",
        "hardware": config.get("hardware", "not_run"),
        "wall_clock": None,
        "gpu_hours": None,
        "vram_peak": None,
        "throughput": None,
    }


def status_for_config(config: dict[str, Any], *, infrastructure_only: bool = False) -> str:
    ckpt = checkpoint_status(config, infrastructure_only=infrastructure_only)
    if ckpt:
        return ckpt
    data = data_status(config)
    if data:
        return data
    return "BENCH_INFRASTRUCTURE_READY"


def parser_with_config(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--infrastructure-only", action="store_true")
    return parser


def write_markdown_report(path: str | Path, title: str, payload: dict[str, Any]) -> None:
    lines = [
        f"# {title}",
        "",
        f"Status: `{payload.get('status', 'unknown')}`",
        "",
        "This report distinguishes primary generalized baselines, public external positioning, and internal strong-router controls.",
        "Do not infer an architecture win from missing checkpoints, missing data, infrastructure execution, or internal control comparisons.",
        "",
        "Allowed comparison language:",
        "- PVR-EC-O does not yet beat generalized baselines.",
        "- PVR-EC-O beats generalized baselines but lags internal strong-router control.",
        "- PVR-EC-O matches internal strong-router control.",
        "- PVR-EC-O beats internal strong-router control.",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        "```",
    ]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(lines), encoding="utf-8")


def route_invariants_for_not_run() -> dict[str, Any]:
    return {
        "owners_per_token": None,
        "top2_execution_count": None,
        "top4_execution_count": None,
        "runtime_dynamic_k_count": None,
        "runtime_expert_choice_count": None,
        "production_map_mutated": None,
        "invariants_validated": False,
    }
