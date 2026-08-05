"""Run copy-scope ablations for the shared-trunk init PVR repair."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json
from benchmark.runners.run_lm_eval import run as run_lm_eval
from benchmark.runners.run_shared_approximation_bottleneck import (
    _safe_mean,
    _train_variant,
    _variant_config,
)


COPY_SCOPES = [
    "embeddings_only",
    "attention_only",
    "norms_only",
    "shared_ffn_bias_only",
    "embeddings_attention_norms",
    "full_compatible_shared_copy",
]

STATUS_COMPLETE = "PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_COMPLETE"
STATUS_INCONCLUSIVE = "PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_INCONCLUSIVE"
STATUS_INVARIANT_FAILED = "PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_INVARIANT_FAILED"


def _load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _load_curve(path: str | Path, key: str) -> list[dict[str, Any]]:
    p = Path(str(path).replace("\\", "/"))
    if not p.exists():
        return []
    return _load_json(p).get(key, [])


def _delta(value: Any, baseline: Any) -> float | None:
    if isinstance(value, (int, float)) and isinstance(baseline, (int, float)):
        return float(value) - float(baseline)
    return None


def _ratio(value: Any, baseline: Any) -> float | None:
    if isinstance(value, (int, float)) and isinstance(baseline, (int, float)) and abs(float(baseline)) > 1.0e-9:
        return float(value) / float(baseline)
    return None


def _route_summary(routing_rows: list[dict[str, Any]]) -> dict[str, Any]:
    clean = bool(routing_rows) and all(
        row.get("owners_per_token") == 1.0
        and row.get("top2_execution_count") == 0
        and row.get("top4_execution_count") == 0
        and row.get("runtime_dynamic_k_count") == 0
        and row.get("runtime_expert_choice_count") == 0
        and row.get("production_map_mutated") is False
        for row in routing_rows
    )
    return {
        "top1_invariants_clean": clean,
        "mean_route_margin": _safe_mean([row.get("prototype_margin") for row in routing_rows]),
        "mean_owner_entropy": _safe_mean([row.get("owner_entropy") for row in routing_rows]),
        "mean_prototype_monopoly_rate": _safe_mean([row.get("prototype_monopoly_rate") for row in routing_rows]),
    }


def _row_from_artifacts(label: str, row: dict[str, Any], baseline: dict[str, Any], scorecard: dict[str, Any] | None) -> dict[str, Any]:
    train = _load_curve(row.get("training_curve", ""), "loss_curve")
    eval_curve = _load_curve(row.get("eval_curve", ""), "eval_curve")
    routing = _route_summary(_load_curve(row.get("routing_curve", ""), "routing_curve"))
    current = {
        "copy_scope": label,
        "model": row.get("model_variant"),
        "checkpoint_path": row.get("checkpoint_path"),
        "status": row.get("status"),
        "optimizer_steps": row.get("optimizer_steps"),
        "training_tokens_seen": row.get("training_tokens_seen"),
        "effective_batch_tokens": row.get("effective_batch_tokens"),
        "eval_window_count": len(eval_curve),
        "routing_window_count": len(_load_curve(row.get("routing_curve", ""), "routing_curve")),
        "final_train_loss": train[-1]["loss"] if train else None,
        "mean_eval_loss": _safe_mean([item.get("eval_loss") for item in eval_curve]),
        "lm_loss": scorecard.get("scorecard", {}).get("lm_loss") if scorecard else None,
        "perplexity": scorecard.get("scorecard", {}).get("perplexity") if scorecard else None,
        "eval_token_count": scorecard.get("scorecard", {}).get("eval_token_count") if scorecard else None,
        "heldout_eval_token_count": scorecard.get("scorecard", {}).get("heldout_eval_token_count") if scorecard else None,
        "tokens_per_second": scorecard.get("scorecard", {}).get("throughput") if scorecard else None,
        "eval_vram_peak": scorecard.get("scorecard", {}).get("vram_peak") if scorecard else None,
        "training_vram_peak": row.get("vram_peak"),
        "init_report": row.get("init_report", {}),
        **routing,
    }
    deltas = {
        "final_train_loss_delta_vs_baseline": _delta(current["final_train_loss"], baseline.get("final_train_loss")),
        "mean_eval_loss_delta_vs_baseline": _delta(current["mean_eval_loss"], baseline.get("mean_eval_loss")),
        "lm_loss_delta_vs_baseline": _delta(current["lm_loss"], baseline.get("lm_loss")),
        "mean_route_margin_delta_vs_baseline": _delta(current["mean_route_margin"], baseline.get("mean_route_margin")),
        "mean_owner_entropy_delta_vs_baseline": _delta(current["mean_owner_entropy"], baseline.get("mean_owner_entropy")),
        "mean_prototype_monopoly_rate_delta_vs_baseline": _delta(
            current["mean_prototype_monopoly_rate"], baseline.get("mean_prototype_monopoly_rate")
        ),
    }
    margin_ratio = _ratio(current["mean_route_margin"], baseline.get("mean_route_margin"))
    entropy_ratio = _ratio(current["mean_owner_entropy"], baseline.get("mean_owner_entropy"))
    route_stable = (
        current["top1_invariants_clean"]
        and margin_ratio is not None and margin_ratio >= 0.50
        and current["mean_route_margin"] is not None and current["mean_route_margin"] >= 0.25
        and entropy_ratio is not None and entropy_ratio >= 0.80
        and deltas["mean_prototype_monopoly_rate_delta_vs_baseline"] is not None
        and deltas["mean_prototype_monopoly_rate_delta_vs_baseline"] <= 0.15
    )
    loss_supported = (
        deltas["final_train_loss_delta_vs_baseline"] is not None
        and deltas["mean_eval_loss_delta_vs_baseline"] is not None
        and deltas["lm_loss_delta_vs_baseline"] is not None
        and deltas["final_train_loss_delta_vs_baseline"] < 0
        and deltas["mean_eval_loss_delta_vs_baseline"] <= 0
        and deltas["lm_loss_delta_vs_baseline"] <= 0
    )
    return {**current, "deltas": deltas, "route_stable": route_stable, "loss_supported": loss_supported}


def _baseline_from_seed_report(path: str) -> dict[str, Any]:
    report = _load_json(path)
    baseline_row = next(row for row in report["rows"] if row.get("variant_name") == "baseline")
    lm_path = report.get("lm_eval_confirmation", {}).get("paths", {}).get("baseline")
    scorecard = _load_json(lm_path) if lm_path else None
    routing = report.get("summary", {}).get("rows", {}).get("baseline", {})
    return {
        "source_report": path,
        "model": baseline_row.get("model_variant"),
        "checkpoint_path": baseline_row.get("checkpoint_path"),
        "final_train_loss": routing.get("final_train_loss") or baseline_row.get("final_loss"),
        "mean_eval_loss": routing.get("mean_eval_loss"),
        "lm_loss": scorecard.get("scorecard", {}).get("lm_loss") if scorecard else None,
        "mean_route_margin": routing.get("mean_route_margin"),
        "mean_owner_entropy": routing.get("mean_owner_entropy"),
        "mean_prototype_monopoly_rate": routing.get("mean_prototype_monopoly_rate"),
        "top1_invariants_clean": routing.get("top1_invariants_clean"),
    }


def run(
    *,
    seed: int,
    output: str,
    checkpoint_root: str,
    dense_config: str,
    pvr_config: str,
    baseline_seed_report: str,
    dense_checkpoint: str | None = None,
    scopes: list[str] | None = None,
    device: str = "cuda",
    max_steps: int = 4000,
    batch_size: int = 2,
    seq_len: int = 128,
    lr: float = 1e-5,
    eval_interval: int = 400,
    lm_eval_limit: int = 200,
) -> dict[str, Any]:
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    selected_scopes = scopes or COPY_SCOPES
    unknown = sorted(set(selected_scopes) - set(COPY_SCOPES))
    if unknown:
        raise ValueError(f"Unsupported copy scopes: {unknown}")
    dense_cfg = load_json_or_yaml(dense_config)
    pvr_cfg = load_json_or_yaml(pvr_config)
    dense_checkpoint = dense_checkpoint or str(dense_cfg.get("checkpoint_path"))
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    baseline = _baseline_from_seed_report(baseline_seed_report)
    rows = []
    variant_names = {}
    scorecard_dir = out / "lm_eval"
    scorecard_dir.mkdir(parents=True, exist_ok=True)
    for scope in selected_scopes:
        variant = f"{pvr_cfg['model_variant']}_shared_trunk_init_v1_scope_{scope}_seed_{seed}"
        cfg = _variant_config(pvr_cfg, variant, checkpoint_root, output)
        cfg["copy_scope"] = scope
        row = _train_variant(
            variant_name=scope,
            mode="shared_trunk_init_from_dense",
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
            target_steps=4000,
            target_training_tokens=1_000_000,
            target_eval_windows=10,
            gated_teacher_weight=0.0,
            gated_teacher_warmup_steps=0,
            temperature=2.0,
            copy_scope=scope,
        )
        variant_names[scope] = cfg["model_variant"]
        eval_cfg = {**cfg, "checkpoint_path": row.get("checkpoint_path") or cfg["checkpoint_path"]}
        config_path = out / cfg["model_variant"] / "lm_eval_config.json"
        write_json(config_path, eval_cfg)
        scorecard_path = scorecard_dir / f"{cfg['model_variant']}_nlp_scorecard.json"
        scorecard = run_lm_eval(eval_cfg, str(scorecard_path), limit=lm_eval_limit)
        rows.append(_row_from_artifacts(scope, row, baseline, scorecard))
    clean_invariants = bool(rows) and all(row.get("top1_invariants_clean") for row in rows)
    supported = [row for row in rows if row.get("loss_supported") and row.get("route_stable")]
    status = STATUS_COMPLETE if supported else STATUS_INVARIANT_FAILED if not clean_invariants else STATUS_INCONCLUSIVE
    ranked = sorted(rows, key=lambda item: item["lm_loss"] if isinstance(item["lm_loss"], (int, float)) else float("inf"))
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "seed": seed,
        "max_steps": max_steps,
        "training_tokens_per_scope": max_steps * batch_size * seq_len,
        "eval_windows": max_steps // eval_interval if eval_interval else 0,
        "baseline": baseline,
        "variant_names": variant_names,
        "rows": rows,
        "supported_scopes": [row["copy_scope"] for row in supported],
        "best_scope_by_lm_loss": ranked[0]["copy_scope"] if ranked else None,
        "rankings": {
            "lm_loss_ascending": [{"copy_scope": row["copy_scope"], "lm_loss": row["lm_loss"]} for row in ranked],
            "mean_eval_loss_ascending": [
                {"copy_scope": row["copy_scope"], "mean_eval_loss": row["mean_eval_loss"]}
                for row in sorted(rows, key=lambda item: item["mean_eval_loss"] if isinstance(item["mean_eval_loss"], (int, float)) else float("inf"))
            ],
        },
        "decision_rule": (
            "A scope is supported only if it improves final train loss, training eval loss, and reduced LM loss "
            "versus the matched PVR baseline while keeping strict Top1 invariants and route stability clean."
        ),
        "deprecated_paths_not_used": [
            "in_bounds_probability_head_as_previously_implemented",
            "route_confidence_regularization_0_01",
            "persistent_global_dense_kl",
        ],
    }
    write_json(out / "copy_scope_ablation_report.json", payload)
    _write_markdown(out / "copy_scope_ablation_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Shared-Trunk Init Copy-Scope Ablation",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"Best scope by LM loss: `{payload.get('best_scope_by_lm_loss')}`",
        "",
        "| scope | LM loss | mean eval | train delta | LM delta | route stable |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in payload["rows"]:
        deltas = row.get("deltas", {})
        lines.append(
            f"| {row['copy_scope']} | {row.get('lm_loss')} | {row.get('mean_eval_loss')} | "
            f"{deltas.get('final_train_loss_delta_vs_baseline')} | {deltas.get('lm_loss_delta_vs_baseline')} | "
            f"{row.get('route_stable')} |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run shared-trunk init copy-scope ablation")
    parser.add_argument("--seed", type=int, default=20260614)
    parser.add_argument("--output", default="benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation")
    parser.add_argument("--checkpoint-root", default="checkpoints/shared_trunk_init_300m_copy_scope_ablation")
    parser.add_argument("--dense-config", default="benchmark/configs/generated/dense_transformer_300m.yaml")
    parser.add_argument("--pvr-config", default="benchmark/configs/generated/pvr_ec_o_full_300m.yaml")
    parser.add_argument("--baseline-seed-report", default="benchmark/reports/generated/shared_trunk_init_300m_confirmation/shared_trunk_init_seed_report.json")
    parser.add_argument("--dense-checkpoint", default=None)
    parser.add_argument("--scopes", nargs="*", default=None)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--max-steps", type=int, default=4000)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--seq-len", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--eval-interval", type=int, default=400)
    parser.add_argument("--lm-eval-limit", type=int, default=200)
    args = parser.parse_args()
    payload = run(
        seed=args.seed,
        output=args.output,
        checkpoint_root=args.checkpoint_root,
        dense_config=args.dense_config,
        pvr_config=args.pvr_config,
        baseline_seed_report=args.baseline_seed_report,
        dense_checkpoint=args.dense_checkpoint,
        scopes=args.scopes,
        device=args.device,
        max_steps=args.max_steps,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lr=args.lr,
        eval_interval=args.eval_interval,
        lm_eval_limit=args.lm_eval_limit,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
