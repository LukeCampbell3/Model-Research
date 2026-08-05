"""Freeze and decide the embeddings+attention+norms init v1 candidate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json


STATUS_SCORECARD_SUPPORTED_EVAL_MIXED = "PVR_EAN_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED"
STATUS_REPEAT_SUPPORTED = "PVR_EAN_INIT_300M_REPEAT_SUPPORTED"
STATUS_NOT_SUPPORTED = "PVR_EAN_INIT_300M_REPEAT_NOT_SUPPORTED"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _score(path: str | Path) -> dict[str, Any]:
    return _load(path)["scorecard"]


def _quality(lm_loss: float | None, denominator: float | int | None) -> float | None:
    if not isinstance(lm_loss, (int, float)) or lm_loss <= 0 or not denominator:
        return None
    return 1.0 / float(lm_loss) / float(denominator)


def _reference_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": row["model"],
        "source": "comparison_300m_real_4k",
        "lm_loss": row.get("lm_loss"),
        "active_params_per_token": row.get("active_params_per_token"),
        "active_flops_per_token": row.get("active_flops_per_token"),
        "vram_peak": row.get("vram_peak"),
        "tokens_per_second": row.get("tokens_per_second"),
        "quality_per_active_param": row.get("quality_per_active_param"),
        "quality_per_active_flop": row.get("quality_per_active_flop"),
    }


def _candidate_row(
    *,
    model: str,
    source: str,
    lm_loss: float,
    scorecard: dict[str, Any],
    active_params: int,
    active_flops: int,
) -> dict[str, Any]:
    return {
        "model": model,
        "source": source,
        "lm_loss": lm_loss,
        "active_params_per_token": active_params,
        "active_flops_per_token": active_flops,
        "vram_peak": scorecard.get("vram_peak"),
        "tokens_per_second": scorecard.get("throughput"),
        "quality_per_active_param": _quality(lm_loss, active_params),
        "quality_per_active_flop": _quality(lm_loss, active_flops),
    }


def run(
    *,
    output: str = "benchmark/reports/generated/pvr_ec_o_embeddings_attention_norms_init_v1_candidate",
    config_output: str = "benchmark/configs/generated/pvr_ec_o_embeddings_attention_norms_init_v1_300m.yaml",
    pvr_base_config: str = "benchmark/configs/generated/pvr_ec_o_full_300m.yaml",
    ean_report: str = "benchmark/reports/generated/ean_init_300m_repeat_seed_42/copy_scope_ablation_report.json",
    baseline_scorecard: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json",
    full_copy_scorecard: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json",
    comparison_report: str = "benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json",
) -> dict[str, Any]:
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    ean = _load(ean_report)
    ean_row = ean["rows"][0]
    ean_scorecard_path = Path(ean_report).parent / "lm_eval" / f"{ean_row['model']}_nlp_scorecard.json"
    ean_scorecard_payload = _load(ean_scorecard_path)
    ean_card = ean_scorecard_payload["scorecard"]
    baseline_card = _score(baseline_scorecard)
    full_card = _score(full_copy_scorecard)
    comparison = _load(comparison_report)
    dense = next(row for row in comparison["rows"] if row["model"] == "dense_transformer_300m")
    switch = next(row for row in comparison["rows"] if row["model"] == "vanilla_switch_top1_reference_300m")
    top2 = next(row for row in comparison["rows"] if row["model"] == "generic_top2_moe_reference_300m")
    active_params = int(ean_card["active_params_per_token"])
    active_flops = int(ean_scorecard_payload["config"]["active_flops_estimate"])
    lm_loss = float(ean_card["lm_loss"])
    lm_delta_vs_baseline = lm_loss - float(baseline_card["lm_loss"])
    lm_delta_vs_dense = lm_loss - float(dense["lm_loss"])
    lm_delta_vs_full_copy = lm_loss - float(full_card["lm_loss"])
    mean_eval_delta = ean_row["deltas"]["mean_eval_loss_delta_vs_baseline"]
    train_delta = ean_row["deltas"]["final_train_loss_delta_vs_baseline"]
    eval_curve_material_regression = isinstance(mean_eval_delta, (int, float)) and mean_eval_delta > 0.05
    scorecard_supported = lm_delta_vs_baseline < 0 and lm_delta_vs_dense < 0 and bool(ean_row.get("route_stable"))
    status = (
        STATUS_REPEAT_SUPPORTED if scorecard_supported and not eval_curve_material_regression
        else STATUS_SCORECARD_SUPPORTED_EVAL_MIXED if scorecard_supported
        else STATUS_NOT_SUPPORTED
    )
    cfg = load_json_or_yaml(pvr_base_config)
    cfg.update({
        "model_variant": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "repair_candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "predecessor_candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "fallback_candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "copy_scope": "embeddings_attention_norms",
        "checkpoint_path": ean_row["checkpoint_path"],
        "output_path": "benchmark/reports/generated/pvr_ec_o_embeddings_attention_norms_init_v1",
        "teacher_initialized_sparse_transfer": True,
        "from_scratch_dense_dominance_proven": False,
        "dense_init_source": "dense_transformer_300m",
        "candidate_revision_reason": "copy-scope ablation showed embeddings+attention+norms as the main transfer carrier",
        "deprecated_paths_not_used": [
            "in_bounds_probability_head_as_previously_implemented",
            "route_confidence_regularization_0_01",
            "persistent_global_dense_kl",
            "dense_ffn_shared_tail_copy_by_default",
        ],
    })
    write_json(config_output, cfg)
    rows = [
        _candidate_row(
            model="pvr_ec_o_embeddings_attention_norms_init_v1_seed_42",
            source="ean_init_300m_repeat_seed_42",
            lm_loss=lm_loss,
            scorecard=ean_card,
            active_params=active_params,
            active_flops=active_flops,
        ),
        _candidate_row(
            model="pvr_ec_o_full_compatible_shared_copy_seed_42",
            source="shared_trunk_init_300m_repeat_seed_42",
            lm_loss=float(full_card["lm_loss"]),
            scorecard=full_card,
            active_params=active_params,
            active_flops=active_flops,
        ),
        _candidate_row(
            model="pvr_ec_o_full_300m_baseline_seed_42",
            source="shared_trunk_init_300m_repeat_seed_42",
            lm_loss=float(baseline_card["lm_loss"]),
            scorecard=baseline_card,
            active_params=active_params,
            active_flops=active_flops,
        ),
        _reference_row(dense),
        _reference_row(switch),
        _reference_row(top2),
    ]
    rows = sorted(rows, key=lambda item: item["lm_loss"])
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
        "fallback_candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "candidate_config": config_output,
        "supported_claim": (
            "Embeddings+attention+norms dense-compatible initialization is the main observed transfer carrier "
            "and repeats the 300M reduced LM scorecard dense-gap closure with strict Top1 routing."
        ),
        "not_fully_supported": [
            "300M repeat is clean across all eval views",
            "from-scratch PVR dominance",
            "teacher independence",
            "full-compatible shared copy is always optimal",
        ],
        "decision": {
            "scorecard_supported": scorecard_supported,
            "eval_curve_material_regression": eval_curve_material_regression,
            "lm_loss": lm_loss,
            "baseline_pvr_lm_loss": baseline_card["lm_loss"],
            "dense_reference_lm_loss": dense["lm_loss"],
            "full_copy_lm_loss": full_card["lm_loss"],
            "init_minus_baseline_lm_loss": lm_delta_vs_baseline,
            "init_minus_dense_lm_loss": lm_delta_vs_dense,
            "init_minus_full_copy_lm_loss": lm_delta_vs_full_copy,
            "init_minus_baseline_mean_eval_loss": mean_eval_delta,
            "init_minus_baseline_final_train_loss": train_delta,
        },
        "route_stability": {
            "top1_invariants_clean": ean_row.get("top1_invariants_clean"),
            "route_stable": ean_row.get("route_stable"),
            "mean_route_margin_delta_vs_baseline": ean_row["deltas"].get("mean_route_margin_delta_vs_baseline"),
            "mean_owner_entropy_delta_vs_baseline": ean_row["deltas"].get("mean_owner_entropy_delta_vs_baseline"),
            "mean_prototype_monopoly_rate_delta_vs_baseline": ean_row["deltas"].get("mean_prototype_monopoly_rate_delta_vs_baseline"),
        },
        "active_compute_audit": {
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
        },
        "source_reports": {
            "ean_repeat": ean_report,
            "ean_scorecard": str(ean_scorecard_path),
            "baseline_scorecard": baseline_scorecard,
            "full_copy_scorecard": full_copy_scorecard,
            "comparison_report": comparison_report,
        },
    }
    write_json(out / "freeze_report.json", payload)
    lines = [
        "# PVR-EC-O EAN Init v1 Freeze",
        "",
        f"Status: `{payload['status']}`",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        "```",
        "",
    ]
    (out / "freeze_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_ec_o_embeddings_attention_norms_init_v1_candidate")
    parser.add_argument("--config-output", default="benchmark/configs/generated/pvr_ec_o_embeddings_attention_norms_init_v1_300m.yaml")
    parser.add_argument("--pvr-base-config", default="benchmark/configs/generated/pvr_ec_o_full_300m.yaml")
    parser.add_argument("--ean-report", default="benchmark/reports/generated/ean_init_300m_repeat_seed_42/copy_scope_ablation_report.json")
    parser.add_argument("--baseline-scorecard", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json")
    parser.add_argument("--full-copy-scorecard", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json")
    parser.add_argument("--comparison-report", default="benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json")
    args = parser.parse_args()
    payload = run(
        output=args.output,
        config_output=args.config_output,
        pvr_base_config=args.pvr_base_config,
        ean_report=args.ean_report,
        baseline_scorecard=args.baseline_scorecard,
        full_copy_scorecard=args.full_copy_scorecard,
        comparison_report=args.comparison_report,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
