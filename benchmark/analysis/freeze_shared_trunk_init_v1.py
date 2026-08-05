"""Freeze and audit the pvr_ec_o_full_shared_trunk_init_v1 repair candidate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json


REFERENCE_MODELS = [
    "dense_transformer_300m",
    "vanilla_switch_top1_reference_300m",
    "generic_top2_moe_reference_300m",
]

COPY_SCOPE_ABLATION_SCOPES = [
    "embeddings_only",
    "attention_only",
    "norms_only",
    "shared_ffn_bias_only",
    "embeddings_attention_norms",
    "full_compatible_shared_copy",
]


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _scorecard(path: str | Path) -> dict[str, Any]:
    return _load(path)["scorecard"]


def _quality(lm_loss: float | None, denominator: float | int | None) -> float | None:
    if not isinstance(lm_loss, (int, float)) or lm_loss <= 0 or not denominator:
        return None
    return 1.0 / float(lm_loss) / float(denominator)


def _row_from_comparison(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": row["model"],
        "source": "comparison_300m_real_4k",
        "lm_loss": row.get("lm_loss"),
        "perplexity": row.get("perplexity"),
        "active_params_per_token": row.get("active_params_per_token"),
        "active_flops_per_token": row.get("active_flops_per_token"),
        "eval_vram_peak": row.get("vram_peak"),
        "training_vram_peak": None,
        "tokens_per_second": row.get("tokens_per_second"),
        "training_tokens_per_second": row.get("training_tokens_per_second"),
        "quality_per_active_param": row.get("quality_per_active_param"),
        "quality_per_active_flop": row.get("quality_per_active_flop"),
        "optimizer_steps": row.get("optimizer_steps"),
        "training_tokens_seen": row.get("training_tokens_seen"),
        "eval_token_count": row.get("eval_token_count"),
        "heldout_eval_token_count": row.get("heldout_eval_token_count"),
        "routing_window_count": row.get("routing_window_count"),
        "routing_diagnostics": row.get("routing_diagnostics"),
        "scorecard_path": row.get("scorecard_path"),
    }


def _matched_pvr_row(
    *,
    model: str,
    variant_name: str,
    scorecard_path: str,
    seed_report: dict[str, Any],
    active_flops_per_token: int,
    active_params_per_token: int,
) -> dict[str, Any]:
    card = _scorecard(scorecard_path)
    train_row = next(row for row in seed_report["rows"] if row["variant_name"] == variant_name)
    hardware = _load(train_row["hardware_manifest"]) if Path(train_row["hardware_manifest"]).exists() else {}
    lm_loss = card.get("lm_loss")
    return {
        "model": model,
        "source": "shared_trunk_init_300m_confirmation",
        "lm_loss": lm_loss,
        "perplexity": card.get("perplexity"),
        "active_params_per_token": active_params_per_token,
        "active_flops_per_token": active_flops_per_token,
        "eval_vram_peak": card.get("vram_peak"),
        "training_vram_peak": train_row.get("vram_peak") or hardware.get("vram_peak"),
        "tokens_per_second": card.get("throughput"),
        "training_tokens_per_second": hardware.get("tokens_per_second"),
        "quality_per_active_param": _quality(lm_loss, active_params_per_token),
        "quality_per_active_flop": _quality(lm_loss, active_flops_per_token),
        "optimizer_steps": train_row.get("optimizer_steps"),
        "training_tokens_seen": train_row.get("training_tokens_seen"),
        "eval_token_count": card.get("eval_token_count"),
        "heldout_eval_token_count": card.get("heldout_eval_token_count"),
        "routing_window_count": train_row.get("routing_window_count"),
        "routing_diagnostics": seed_report.get("summary", {}).get("rows", {}).get(variant_name, {}),
        "scorecard_path": scorecard_path,
        "checkpoint_path": train_row.get("checkpoint_path"),
    }


def _write_md(path: Path, title: str, payload: dict[str, Any]) -> None:
    lines = [
        f"# {title}",
        "",
        f"Status: `{payload.get('status')}`",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        "```",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run(
    *,
    output: str,
    config_output: str,
    seed_report_path: str,
    decision_report_path: str,
    comparison_report_path: str,
    pvr_base_config: str,
) -> dict[str, Any]:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    seed_report = _load(seed_report_path)
    decision_report = _load(decision_report_path)
    comparison_report = _load(comparison_report_path)
    pvr_cfg = load_json_or_yaml(pvr_base_config)
    init_row = next(row for row in seed_report["rows"] if row["variant_name"] == "shared_trunk_init_from_dense")
    init_report = init_row.get("init_report", {})
    pvr_cfg.update({
        "model_variant": "pvr_ec_o_full_shared_trunk_init_v1",
        "repair_candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "model_size_label": "300m",
        "checkpoint_path": init_row["checkpoint_path"],
        "output_path": "benchmark/reports/generated/pvr_ec_o_full_shared_trunk_init_v1",
        "teacher_initialized_sparse_transfer": True,
        "from_scratch_dense_dominance_proven": False,
        "dense_init_source": "dense_transformer_300m",
        "copy_scope": "full_compatible_shared_copy",
        "copied_compatible_weight_count": init_report.get("copied_count"),
        "skipped_incompatible_weight_count": init_report.get("skipped_count"),
        "deprecated_paths_not_used": [
            "in_bounds_probability_head_as_previously_implemented",
            "route_confidence_regularization_0_01",
            "persistent_global_dense_kl",
        ],
    })
    write_json(config_output, pvr_cfg)

    reference_by_model = {row["model"]: row for row in comparison_report["rows"]}
    rows = [_row_from_comparison(reference_by_model[name]) for name in REFERENCE_MODELS]
    active_flops = int(pvr_cfg["active_flops_estimate"])
    active_params = int(pvr_cfg["active_params_per_token"])
    lm_paths = seed_report["lm_eval_confirmation"]["paths"]
    rows.append(_matched_pvr_row(
        model="pvr_ec_o_full_300m_baseline",
        variant_name="baseline",
        scorecard_path=lm_paths["baseline"],
        seed_report=seed_report,
        active_flops_per_token=active_flops,
        active_params_per_token=active_params,
    ))
    rows.append(_matched_pvr_row(
        model="pvr_ec_o_full_shared_trunk_init_v1",
        variant_name="shared_trunk_init_from_dense",
        scorecard_path=lm_paths["shared_trunk_init"],
        seed_report=seed_report,
        active_flops_per_token=active_flops,
        active_params_per_token=active_params,
    ))
    rows = sorted(rows, key=lambda item: item["lm_loss"] if isinstance(item["lm_loss"], (int, float)) else float("inf"))

    freeze_report = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": "PVR_SHARED_TRUNK_INIT_REPAIR_CANDIDATE",
        "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "candidate_config": str(config_output),
        "evidence_statuses": [
            "PVR_SHARED_TRUNK_INIT_CONFIRMED",
            "PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED",
            "PVR_ROUTING_NOT_MAIN_BOTTLENECK",
        ],
        "supported_claim": (
            "Dense-compatible shared-trunk initialization materially improves 300M PVR-EC-O "
            "while preserving strict Top1 routing."
        ),
        "not_proven_claim": "PVR-EC-O from scratch beats dense under equal total training conditions.",
        "copy_scope": {
            "name": "full_compatible_shared_copy",
            "copied_compatible_weight_count": init_report.get("copied_count"),
            "skipped_incompatible_weight_count": init_report.get("skipped_count"),
            "copied_sample": init_report.get("copied", [])[:20],
            "skipped_sample": init_report.get("skipped_sample", [])[:20],
        },
        "decision_report": decision_report,
        "deprecated_paths_not_used": pvr_cfg["deprecated_paths_not_used"],
    }
    write_json(out / "freeze_report.json", freeze_report)
    _write_md(out / "freeze_report.md", "PVR-EC-O Shared Trunk Init v1 Freeze", freeze_report)

    audit = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": "PVR_SHARED_TRUNK_INIT_V1_ACTIVE_COMPUTE_AUDIT_COMPLETE",
        "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "comparison_scope": [
            *REFERENCE_MODELS,
            "pvr_ec_o_full_300m_baseline",
            "pvr_ec_o_full_shared_trunk_init_v1",
        ],
        "rows": rows,
        "rankings": {
            "lm_loss_ascending": [{"model": row["model"], "lm_loss": row["lm_loss"]} for row in rows],
            "quality_per_active_param_descending": [
                {"model": row["model"], "quality_per_active_param": row["quality_per_active_param"]}
                for row in sorted(rows, key=lambda item: item["quality_per_active_param"] or -1.0, reverse=True)
            ],
            "quality_per_active_flop_descending": [
                {"model": row["model"], "quality_per_active_flop": row["quality_per_active_flop"]}
                for row in sorted(rows, key=lambda item: item["quality_per_active_flop"] or -1.0, reverse=True)
            ],
        },
        "interpretation": (
            "The candidate has the best LM loss in this comparison and preserves the 105M active-parameter/"
            "630M active-FLOP Top1 PVR execution estimate. Its proof remains a teacher-initialized sparse "
            "transfer claim, not a from-scratch architecture dominance claim."
        ),
    }
    write_json(out / "active_compute_audit_report.json", audit)
    _write_md(out / "active_compute_audit_report.md", "PVR-EC-O Shared Trunk Init v1 Active Compute Audit", audit)

    ablation = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": "PVR_SHARED_TRUNK_INIT_COPY_SCOPE_ABLATION_READY_NOT_RUN",
        "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "reason_not_run": "The high-value 300M confirmation is complete; this artifact freezes the ablation matrix without launching six additional 300M 4k-step jobs.",
        "required_budget_per_scope": {
            "optimizer_steps": 4000,
            "effective_batch_tokens": 256,
            "training_tokens_seen": 1024000,
            "eval_windows": 10,
            "routing_windows_for_pvr": 10,
        },
        "copy_scopes": COPY_SCOPE_ABLATION_SCOPES,
        "decision_rule": (
            "A scope is supported only if it improves mean eval loss versus matched PVR baseline, does not materially "
            "regress final train loss, keeps Top1 invariants clean, and preserves route stability."
        ),
        "runner_support": {
            "function": "benchmark.runners.run_shared_approximation_bottleneck.copy_compatible_dense_weights_to_pvr",
            "copy_scope_argument": True,
        },
    }
    write_json(out / "copy_scope_ablation_plan.json", ablation)
    _write_md(out / "copy_scope_ablation_plan.md", "PVR-EC-O Shared Trunk Init Copy-Scope Ablation Plan", ablation)
    return {"freeze_report": freeze_report, "active_compute_audit": audit, "copy_scope_ablation_plan": ablation}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_ec_o_full_shared_trunk_init_v1_candidate")
    parser.add_argument("--config-output", default="benchmark/configs/generated/pvr_ec_o_full_shared_trunk_init_v1_300m.yaml")
    parser.add_argument("--seed-report", default="benchmark/reports/generated/shared_trunk_init_300m_confirmation/shared_trunk_init_seed_report.json")
    parser.add_argument("--decision-report", default="benchmark/reports/generated/shared_trunk_init_300m_decision/shared_trunk_init_300m_decision_report.json")
    parser.add_argument("--comparison-report", default="benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json")
    parser.add_argument("--pvr-base-config", default="benchmark/configs/generated/pvr_ec_o_full_300m.yaml")
    args = parser.parse_args()
    run(
        output=args.output,
        config_output=args.config_output,
        seed_report_path=args.seed_report,
        decision_report_path=args.decision_report,
        comparison_report_path=args.comparison_report,
        pvr_base_config=args.pvr_base_config,
    )


if __name__ == "__main__":
    main()
