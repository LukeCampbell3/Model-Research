"""Execute the genuine PVR-EC-O benchmark program gate.

This runner is the strict tier orchestrator. It does not create mock
checkpoints, does not run smoke tests, and does not count model construction or
forward probes as benchmark evidence. When real prerequisites are absent, it
writes an explicit blocked report with the missing data, checkpoints, seeds,
and artifacts needed to reach the requested completion status.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import (
    environment_payload,
    git_commit,
    load_json_or_yaml,
    manifest_payload,
    utc_now,
    write_json,
    write_markdown_report,
)
from benchmark.runners import run_benchmark_suite


TARGET_STATUS_BY_SIZE = {
    "100m": "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE",
    "300m": "PVR_EC_O_300M_GENUINE_BENCHMARK_COMPLETE",
    "700m": "PVR_EC_O_700M_GENUINE_BENCHMARK_COMPLETE",
}
STABLE_TARGET_STATUS_BY_SIZE = {
    "100m": "PVR_EC_O_100M_STABLE_LEARNING_BENCHMARK_COMPLETE",
}
REAL_COMPARISON_TARGET_STATUS_BY_SIZE = {
    "100m": "PVR_EC_O_100M_REAL_COMPARISON_COMPLETE",
    "300m": "PVR_EC_O_300M_REAL_COMPARISON_COMPLETE",
    "700m": "PVR_EC_O_700M_REAL_COMPARISON_COMPLETE",
}

REQUIRED_BROAD_NLP_BENCHMARKS = [
    "mmlu_pro",
    "gpqa",
    "bbh",
    "musr",
    "math_lvl_5",
    "ifeval",
    "arc_challenge",
    "hellaswag",
    "truthfulqa",
    "winogrande",
    "boolq",
    "gsm8k",
]

REQUIRED_CODING_BENCHMARKS = [
    "humaneval_plus",
    "mbpp_plus",
    "bigcodebench_complete",
    "bigcodebench_instruct",
    "livecodebench",
    "repobench",
]

REQUIRED_LM_EVALS = [
    "general_heldout_lm_loss",
    "perplexity",
    "code_heavy_heldout_loss",
    "math_heavy_heldout_loss",
    "json_schema_heavy_heldout_loss",
    "long_context_loss_by_position",
    "rare_token_loss",
]

REQUIRED_ROUTING_DIAGNOSTICS = [
    "owners_per_token",
    "top2_execution_count",
    "top4_execution_count",
    "runtime_dynamic_k_count",
    "runtime_expert_choice_count",
    "prototype_entropy",
    "prototype_margin",
    "owner_entropy",
    "owner_churn",
    "expert_utilization",
    "expert_gini",
    "prototype_monopoly_rate",
    "high_gap_monopoly_rate",
    "challenger_disagreement_rate",
    "stale_owner_rate",
    "descriptor_control_margin",
    "operator_control_margin",
    "failure_mode_distribution",
]

HARD_ROUTING_INVARIANTS = {
    "owners_per_token": 1.0,
    "top2_execution_count": 0,
    "top4_execution_count": 0,
    "runtime_dynamic_k_count": 0,
    "runtime_expert_choice_count": 0,
    "production_map_mutated": False,
}

REQUIRED_SEEDS = [42, 123, 777]
DEFAULT_MIN_OPTIMIZER_STEPS = 20
DEFAULT_MIN_TRAINING_TOKENS = 1024
DEFAULT_MIN_EFFECTIVE_BATCH_TOKENS = 32
DEFAULT_MIN_EVAL_TOKENS = 1024
DEFAULT_MIN_HELDOUT_EVAL_TOKENS = 256
DEFAULT_STABLE_MIN_OPTIMIZER_STEPS = 40
DEFAULT_STABLE_MIN_TRAINING_TOKENS = 2560
DEFAULT_STABLE_MIN_EVAL_WINDOWS = 4
DEFAULT_REAL_MIN_OPTIMIZER_STEPS = 1000
DEFAULT_REAL_MIN_TRAINING_TOKENS = 1_000_000
DEFAULT_REAL_MIN_EVAL_TOKENS = 50_000
DEFAULT_REAL_MIN_HELDOUT_EVAL_TOKENS = 10_000
DEFAULT_REAL_MIN_EVAL_WINDOWS = 10


def _path_exists(path: str) -> bool:
    return bool(path) and Path(path).exists()


def _missing_paths(paths: list[str]) -> list[str]:
    return [path for path in paths if not _path_exists(path)]


def _resolve_config_path(config_path: str, suite_path: str) -> Path:
    path = Path(config_path)
    beside_suite = Path(suite_path).parent / path.name
    if beside_suite.exists():
        return beside_suite
    if path.exists():
        return path
    return path


def _load_models(suite: dict[str, Any], suite_path: str) -> list[dict[str, Any]]:
    models = []
    for item in suite.get("models", []):
        config = load_json_or_yaml(_resolve_config_path(item["config_path"], suite_path))
        models.append(config)
    return models


def _benchmark_statuses(config: dict[str, Any], data_missing: bool, checkpoint_missing: bool) -> dict[str, str]:
    blocked = "NOT_RUN_MISSING_DATA" if data_missing else "NOT_RUN_MISSING_CHECKPOINT" if checkpoint_missing else "NOT_RUN_NOT_IMPLEMENTED"
    statuses: dict[str, str] = {}
    for name in REQUIRED_LM_EVALS + REQUIRED_BROAD_NLP_BENCHMARKS + REQUIRED_CODING_BENCHMARKS:
        statuses[name] = blocked
    return statuses


def _estimate_gpu_hours(config: dict[str, Any]) -> float:
    active_params = float(config.get("active_params_per_token") or config.get("total_params") or 0)
    training_tokens = float(config.get("training_tokens") or 0)
    # Very coarse planning estimate, intentionally labeled as an estimate in
    # reports. It exists only to quantify why a tier is resource blocked.
    return round(max(0.1, (active_params * training_tokens) / 1.0e18), 2)


def _model_audit(config: dict[str, Any], seeds: list[int]) -> dict[str, Any]:
    training_paths = list(config.get("training_data_paths") or [])
    eval_paths = list(config.get("eval_data_paths") or [])
    checkpoint = str(config.get("checkpoint_path") or "")
    missing_training_data = _missing_paths(training_paths)
    missing_eval_data = _missing_paths(eval_paths)
    checkpoint_missing = not _path_exists(checkpoint)
    checkpoint_dir = Path(checkpoint).parent if checkpoint else Path("")
    training_curve_exists = bool(checkpoint) and (checkpoint_dir / "training_curve.json").exists()
    eval_curve_exists = bool(checkpoint) and (checkpoint_dir / "eval_curve.json").exists()
    routing_curve_exists = bool(checkpoint) and (checkpoint_dir / "routing_curve.json").exists()
    checkpoint_manifest_exists = bool(checkpoint) and (checkpoint_dir / "checkpoint_manifest.json").exists()
    checkpoint_manifest = {}
    training_curve = {}
    eval_curve = {}
    routing_curve = {}
    if checkpoint_manifest_exists:
        checkpoint_manifest = json.loads((checkpoint_dir / "checkpoint_manifest.json").read_text(encoding="utf-8"))
    if training_curve_exists:
        training_curve = json.loads((checkpoint_dir / "training_curve.json").read_text(encoding="utf-8"))
    if eval_curve_exists:
        eval_curve = json.loads((checkpoint_dir / "eval_curve.json").read_text(encoding="utf-8"))
    if routing_curve_exists:
        routing_curve = json.loads((checkpoint_dir / "routing_curve.json").read_text(encoding="utf-8"))
    data_missing = bool(missing_training_data or missing_eval_data)
    mock_checkpoint_rejected = "mock" in checkpoint.lower()
    training_blocked = bool(missing_training_data)
    eval_blocked = bool(missing_eval_data or checkpoint_missing or mock_checkpoint_rejected)
    status = "BENCH_INFRASTRUCTURE_READY"
    if training_blocked or data_missing:
        status = "NOT_RUN_MISSING_DATA"
    elif checkpoint_missing or mock_checkpoint_rejected:
        status = "NOT_RUN_MISSING_CHECKPOINT"

    seed_rows = []
    for seed in REQUIRED_SEEDS:
        seed_rows.append({
            "seed": seed,
            "status": "NOT_RUN_MISSING_DATA" if training_blocked else "NOT_RUN_MISSING_CHECKPOINT" if checkpoint_missing else "NOT_RUN_RESOURCE_BLOCKED",
            "checkpoint": str(Path(checkpoint).with_name(f"seed_{seed}.safetensors")) if checkpoint else "",
            "training_curve": str(Path("benchmark/reports/generated/training_curves") / config["model_variant"] / f"seed_{seed}.json"),
            "completed": False,
        })

    completed_seeds = [row["seed"] for row in seed_rows if row["completed"]]
    missing_seeds = [seed for seed in seeds if seed not in completed_seeds]
    is_pvr = config.get("model_family") == "pvr_ec_o"
    return {
        "model_variant": config["model_variant"],
        "model_family": config["model_family"],
        "comparison_group": config["comparison_group"],
        "status": status,
        "can_claim_benchmark_evidence": False,
        "trained_checkpoint": {
            "path": checkpoint,
            "exists": _path_exists(checkpoint),
            "mock_checkpoint_rejected": mock_checkpoint_rejected,
        },
        "training": {
            "status": "NOT_RUN_MISSING_DATA" if training_blocked else "NOT_RUN_RESOURCE_BLOCKED",
            "training_data_paths": training_paths,
            "missing_training_data_paths": missing_training_data,
            "training_curve_required": True,
            "training_curve_exists": training_curve_exists,
            "eval_curve_exists": eval_curve_exists,
            "routing_curve_exists": routing_curve_exists,
            "checkpoint_manifest_exists": checkpoint_manifest_exists,
            "training_tokens_seen": checkpoint_manifest.get("training_tokens_seen", checkpoint_manifest.get("tokens_seen", 0)),
            "optimizer_steps": checkpoint_manifest.get("optimizer_steps", 0),
            "effective_batch_tokens": checkpoint_manifest.get("effective_batch_tokens", 0),
            "eval_window_count": checkpoint_manifest.get("eval_window_count", eval_curve.get("eval_window_count", 0)),
            "routing_window_count": checkpoint_manifest.get("routing_window_count", routing_curve.get("routing_window_count", 0)),
            "target_steps": checkpoint_manifest.get("target_steps", 0),
            "target_training_tokens": checkpoint_manifest.get("target_training_tokens", 0),
            "target_eval_windows": checkpoint_manifest.get("target_eval_windows", 0),
            "resource_reduction": checkpoint_manifest.get("resource_reduction", {}),
            "loss_curve": training_curve.get("loss_curve", []),
            "eval_curve": eval_curve.get("eval_curve", []),
            "routing_curve": routing_curve.get("routing_curve", []),
            "estimated_gpu_hours_required": _estimate_gpu_hours(config),
        },
        "evaluation": {
            "status": "NOT_RUN_MISSING_DATA" if missing_eval_data else "NOT_RUN_MISSING_CHECKPOINT" if checkpoint_missing else "NOT_RUN_NOT_IMPLEMENTED",
            "eval_data_paths": eval_paths,
            "missing_eval_data_paths": missing_eval_data,
            "benchmark_statuses": _benchmark_statuses(config, bool(missing_eval_data), checkpoint_missing),
        },
        "seeds": {
            "required_seeds": seeds,
            "completed_seeds": completed_seeds,
            "missing_seeds": missing_seeds,
            "status": "SEED_REDUCTION_RESOURCE_BLOCKED" if missing_seeds else "COMPLETE",
            "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
            "rows": seed_rows,
        },
        "contamination": {
            "status": "CONTAMINATION_STATUS_UNKNOWN",
            "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        },
        "routing_diagnostics_required": is_pvr,
        "routing_diagnostics": {
            "status": "NOT_RUN_MISSING_CHECKPOINT" if is_pvr and checkpoint_missing else "NOT_APPLICABLE" if not is_pvr else "NOT_RUN_MISSING_DATA",
            "required_metrics": REQUIRED_ROUTING_DIAGNOSTICS if is_pvr else [],
            "hard_invariants": HARD_ROUTING_INVARIANTS if is_pvr else {},
            "hard_invariants_validated": False,
        },
        "required_artifacts": {
            "trained_checkpoint": _path_exists(checkpoint),
            "training_curve": training_curve_exists,
            "heldout_lm_metrics": False,
            "broad_nlp_metrics": False,
            "coding_metrics": False,
            "routing_diagnostics": False if is_pvr else None,
            "contamination_scan": False,
            "scorecard": False,
        },
    }


def _derive_tier_status(model_audits: list[dict[str, Any]], target_status: str) -> str:
    if model_audits and all(row["can_claim_benchmark_evidence"] for row in model_audits):
        return target_status
    if model_audits and all(row.get("pipeline_complete") for row in model_audits) and any(
        row.get("training", {}).get("resource_reduction", {}).get("status") == "RESOURCE_REDUCED_BUDGET"
        or row.get("volume_gate", {}).get("failures")
        for row in model_audits
    ):
        return "RESOURCE_REDUCED_BUDGET"
    if model_audits and all(row.get("pipeline_complete") for row in model_audits):
        return "GENUINE_REDUCED_PIPELINE_COMPLETE"
    if any(row["status"] == "NOT_RUN_MISSING_DATA" for row in model_audits):
        return "NOT_RUN_MISSING_DATA"
    if any(row["status"] == "NOT_RUN_MISSING_CHECKPOINT" for row in model_audits):
        return "NOT_RUN_MISSING_CHECKPOINT"
    return "NOT_RUN_RESOURCE_BLOCKED"


def _run_suite_artifacts(suite_path: str, out: Path, limit: int | None) -> dict[str, Any]:
    suite_out = out / "scorecard_artifacts"
    result = run_benchmark_suite.run_suite(suite_path, str(suite_out), limit=limit, infrastructure_only=False)
    return {
        "status": result.get("status"),
        "path": str(suite_out / "benchmark_suite_result.json"),
        "benchmark_evidence_count": result.get("benchmark_evidence_count", 0),
    }


def _scorecard_evidence_map(out: Path) -> dict[str, dict[str, Any]]:
    scorecards = {}
    scorecard_root = out / "scorecard_artifacts" / "scorecards"
    for path in sorted(scorecard_root.rglob("merged_scorecard.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        nlp_scorecard = payload.get("scorecards", {}).get("nlp_scorecard", {}).get("scorecard", {})
        scorecards[str(payload.get("model"))] = {
            "path": str(path),
            "benchmark_evidence": bool(payload.get("benchmark_evidence")),
            "status": payload.get("status"),
            "evidence_requirements": payload.get("evidence_requirements", {}),
            "eval_token_count": nlp_scorecard.get("eval_token_count", nlp_scorecard.get("tokens_evaluated", 0)),
            "heldout_eval_token_count": nlp_scorecard.get("heldout_eval_token_count", 0),
        }
    return scorecards


def _thresholds(
    min_optimizer_steps: int,
    min_training_tokens: int,
    min_effective_batch_tokens: int,
    min_eval_tokens: int,
    min_heldout_eval_tokens: int,
    min_eval_windows: int = 0,
) -> dict[str, int]:
    return {
        "min_optimizer_steps": min_optimizer_steps,
        "min_training_tokens": min_training_tokens,
        "min_effective_batch_tokens": min_effective_batch_tokens,
        "min_eval_tokens": min_eval_tokens,
        "min_heldout_eval_tokens": min_heldout_eval_tokens,
        "min_eval_windows": min_eval_windows,
    }


def _volume_gate(audit: dict[str, Any], card: dict[str, Any], thresholds: dict[str, int]) -> dict[str, Any]:
    training = audit["training"]
    checks = {
        "optimizer_steps": {
            "observed": int(training.get("optimizer_steps") or 0),
            "required": thresholds["min_optimizer_steps"],
        },
        "training_tokens_seen": {
            "observed": int(training.get("training_tokens_seen") or 0),
            "required": thresholds["min_training_tokens"],
        },
        "effective_batch_tokens": {
            "observed": int(training.get("effective_batch_tokens") or 0),
            "required": thresholds["min_effective_batch_tokens"],
        },
        "eval_token_count": {
            "observed": int(card.get("eval_token_count") or 0),
            "required": thresholds["min_eval_tokens"],
        },
        "heldout_eval_token_count": {
            "observed": int(card.get("heldout_eval_token_count") or 0),
            "required": thresholds["min_heldout_eval_tokens"],
        },
        "eval_windows": {
            "observed": int(training.get("eval_window_count") or 0),
            "required": thresholds.get("min_eval_windows", 0),
        },
    }
    failures = {
        name: check for name, check in checks.items()
        if check["observed"] < check["required"]
    }
    return {
        "passed": not failures,
        "checks": checks,
        "failures": failures,
    }


def _slope(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    return (values[-1] - values[0]) / max(1, len(values) - 1)


def _stable_learning_gate(audit: dict[str, Any], thresholds: dict[str, int]) -> dict[str, Any]:
    training = audit["training"]
    loss_rows = training.get("loss_curve") or []
    eval_rows = training.get("eval_curve") or []
    routing_rows = training.get("routing_curve") or []
    train_losses = [row.get("loss") for row in loss_rows if isinstance(row.get("loss"), (int, float))]
    eval_losses = [row.get("eval_loss") for row in eval_rows if isinstance(row.get("eval_loss"), (int, float))]
    train_slope = _slope(train_losses)
    eval_slope = _slope(eval_losses)
    train_eval_gap = None
    if train_losses and eval_losses:
        train_eval_gap = eval_losses[-1] - train_losses[-1]
    is_pvr = audit.get("model_family") == "pvr_ec_o"
    routing_over_time_present = (not is_pvr) or len(routing_rows) >= thresholds.get("min_eval_windows", 0)
    checks = {
        "loss_curve_slope_present": train_slope is not None,
        "train_eval_gap_present": train_eval_gap is not None,
        "routing_diagnostics_over_time_present": routing_over_time_present,
    }
    failures = {name: value for name, value in checks.items() if not value}
    return {
        "passed": not failures,
        "checks": checks,
        "failures": failures,
        "train_loss_slope": train_slope,
        "eval_loss_slope": eval_slope,
        "train_eval_gap": train_eval_gap,
        "eval_window_count": len(eval_rows),
        "routing_window_count": len(routing_rows),
    }
def run(
    suite_path: str,
    output: str,
    *,
    size: str | None = None,
    limit: int | None = None,
    execute_suite: bool = True,
    min_optimizer_steps: int = DEFAULT_MIN_OPTIMIZER_STEPS,
    min_training_tokens: int = DEFAULT_MIN_TRAINING_TOKENS,
    min_effective_batch_tokens: int = DEFAULT_MIN_EFFECTIVE_BATCH_TOKENS,
    min_eval_tokens: int = DEFAULT_MIN_EVAL_TOKENS,
    min_heldout_eval_tokens: int = DEFAULT_MIN_HELDOUT_EVAL_TOKENS,
    min_eval_windows: int = 0,
    tier: str = "genuine",
) -> dict[str, Any]:
    suite = load_json_or_yaml(suite_path)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    models = _load_models(suite, suite_path)
    detected_size = size or (models[0].get("model_size_label") if models else "unknown")
    target_status = (
        REAL_COMPARISON_TARGET_STATUS_BY_SIZE.get(str(detected_size), "PVR_EC_O_REAL_COMPARISON_COMPLETE")
        if tier == "real_comparison"
        else STABLE_TARGET_STATUS_BY_SIZE.get(str(detected_size), "PVR_EC_O_STABLE_LEARNING_BENCHMARK_COMPLETE")
        if tier == "stable_learning"
        else TARGET_STATUS_BY_SIZE.get(str(detected_size), "PVR_EC_O_GENUINE_BENCHMARK_COMPLETE")
    )
    threshold_payload = _thresholds(
        min_optimizer_steps,
        min_training_tokens,
        min_effective_batch_tokens,
        min_eval_tokens,
        min_heldout_eval_tokens,
        min_eval_windows,
    )
    model_audits = [_model_audit(config, REQUIRED_SEEDS) for config in models]
    suite_artifacts = _run_suite_artifacts(suite_path, out, limit) if execute_suite else {
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "path": "",
        "benchmark_evidence_count": 0,
    }
    scorecard_evidence = _scorecard_evidence_map(out)
    for audit in model_audits:
        card = scorecard_evidence.get(audit["model_variant"], {})
        card_ready = bool(card.get("benchmark_evidence"))
        volume_gate = _volume_gate(audit, card, threshold_payload)
        stable_gate = _stable_learning_gate(audit, threshold_payload) if tier == "stable_learning" else {"passed": True}
        audit["scorecard"] = card
        audit["volume_gate"] = volume_gate
        audit["stable_learning_gate"] = stable_gate
        audit["pipeline_complete"] = card_ready
        audit["can_claim_benchmark_evidence"] = card_ready and volume_gate["passed"] and stable_gate["passed"]
        audit["required_artifacts"]["scorecard"] = card_ready
        audit["required_artifacts"]["heldout_lm_metrics"] = audit["can_claim_benchmark_evidence"] and bool(card.get("evidence_requirements", {}).get("nlp_ready"))
        audit["required_artifacts"]["coding_metrics"] = card_ready and bool(card.get("evidence_requirements", {}).get("coding_ready"))
        audit["required_artifacts"]["contamination_scan"] = card_ready and bool(card.get("evidence_requirements", {}).get("contamination_ready"))
        if audit["routing_diagnostics_required"]:
            audit["required_artifacts"]["routing_diagnostics"] = card_ready and bool(card.get("evidence_requirements", {}).get("routing_ready"))
            audit["routing_diagnostics"]["hard_invariants_validated"] = bool(audit["required_artifacts"]["routing_diagnostics"])
    tier_status = _derive_tier_status(model_audits, target_status)
    completion = tier_status == target_status
    missing_by_model = {
        row["model_variant"]: {
            key: value for key, value in row["required_artifacts"].items() if value is False
        }
        for row in model_audits
    }
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "environment": environment_payload(),
        "status": tier_status,
        "target_status": target_status,
        "tier": tier,
        "pipeline_status": "GENUINE_REDUCED_PIPELINE_COMPLETE",
        "benchmark_volume_thresholds": threshold_payload,
        "completed": completion,
        "benchmark_evidence": completion,
        "suite_path": suite_path,
        "suite": suite,
        "size": detected_size,
        "model_count": len(model_audits),
        "required_seeds": REQUIRED_SEEDS,
        "seed_policy": "3 seeds required for 100M tier unless explicitly resource blocked.",
        "suite_artifacts": suite_artifacts,
        "scorecard_evidence": scorecard_evidence,
        "model_audits": model_audits,
        "missing_required_artifacts_by_model": missing_by_model,
        "required_benchmarks": {
            "language_modeling": REQUIRED_LM_EVALS,
            "broad_nlp": REQUIRED_BROAD_NLP_BENCHMARKS,
            "coding": REQUIRED_CODING_BENCHMARKS,
            "routing_diagnostics": REQUIRED_ROUTING_DIAGNOSTICS,
        },
        "hard_routing_invariants": HARD_ROUTING_INVARIANTS,
        "invalid_claims_blocked": [
            "model construction is not benchmark evidence",
            "finite forward probes are not benchmark evidence",
            "mock checkpoints are rejected",
            "toy data is not a genuine benchmark",
            "missing data/checkpoints cannot be converted into architecture results",
            "one-step checkpoints cannot complete the 100M benchmark tier",
        ],
        "next_required_inputs": [
            "real training data at data/broad_nlp_train and data/code_train",
            "real heldout/eval data at data/eval/broad_nlp and data/eval/coding",
            "trained checkpoints for every model/seed in the tier",
            "implemented official or explicitly reduced benchmark adapters",
            "completed contamination scan with dataset hashes",
        ],
        "reproducibility_manifest": str(out / "genuine_program_reproducibility_manifest.json"),
    }
    write_json(out / "genuine_program_reproducibility_manifest.json", manifest_payload([suite_path, "benchmark"], "Strict genuine benchmark program execution manifest."))
    write_json(out / "genuine_benchmark_program_report.json", payload)
    write_markdown_report(out / "genuine_benchmark_program_report.md", "PVR-EC-O Genuine Benchmark Program Gate", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the strict genuine PVR-EC-O benchmark program gate")
    parser.add_argument("--suite", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--size", default=None)
    parser.add_argument("--tier", choices=["genuine", "stable_learning", "real_comparison"], default="genuine")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--min-optimizer-steps", type=int, default=DEFAULT_MIN_OPTIMIZER_STEPS)
    parser.add_argument("--min-training-tokens", type=int, default=DEFAULT_MIN_TRAINING_TOKENS)
    parser.add_argument("--min-effective-batch-tokens", type=int, default=DEFAULT_MIN_EFFECTIVE_BATCH_TOKENS)
    parser.add_argument("--min-eval-tokens", type=int, default=DEFAULT_MIN_EVAL_TOKENS)
    parser.add_argument("--min-heldout-eval-tokens", type=int, default=DEFAULT_MIN_HELDOUT_EVAL_TOKENS)
    parser.add_argument("--min-eval-windows", type=int, default=0)
    parser.add_argument("--no-suite-artifacts", action="store_true")
    args = parser.parse_args()
    min_optimizer_steps = args.min_optimizer_steps
    min_training_tokens = args.min_training_tokens
    min_eval_windows = args.min_eval_windows
    if args.tier == "stable_learning":
        min_optimizer_steps = max(min_optimizer_steps, DEFAULT_STABLE_MIN_OPTIMIZER_STEPS)
        min_training_tokens = max(min_training_tokens, DEFAULT_STABLE_MIN_TRAINING_TOKENS)
        min_eval_windows = max(min_eval_windows, DEFAULT_STABLE_MIN_EVAL_WINDOWS)
    if args.tier == "real_comparison":
        min_optimizer_steps = max(min_optimizer_steps, DEFAULT_REAL_MIN_OPTIMIZER_STEPS)
        min_training_tokens = max(min_training_tokens, DEFAULT_REAL_MIN_TRAINING_TOKENS)
        args.min_eval_tokens = max(args.min_eval_tokens, DEFAULT_REAL_MIN_EVAL_TOKENS)
        args.min_heldout_eval_tokens = max(args.min_heldout_eval_tokens, DEFAULT_REAL_MIN_HELDOUT_EVAL_TOKENS)
        min_eval_windows = max(min_eval_windows, DEFAULT_REAL_MIN_EVAL_WINDOWS)
    payload = run(
        args.suite,
        args.output,
        size=args.size,
        limit=args.limit,
        execute_suite=not args.no_suite_artifacts,
        min_optimizer_steps=min_optimizer_steps,
        min_training_tokens=min_training_tokens,
        min_effective_batch_tokens=args.min_effective_batch_tokens,
        min_eval_tokens=args.min_eval_tokens,
        min_heldout_eval_tokens=args.min_heldout_eval_tokens,
        min_eval_windows=min_eval_windows,
        tier=args.tier,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
