"""Compare corrected sparse-v2 against matched 100M generalized controls."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_lm_eval import run as run_lm_eval


CANDIDATE = "pvr_sparse_v2_full_from_start_aux001_100m"


def run(
    *,
    suite="benchmark/configs/generated/sparse_v2_100m_baseline_screen/sparse_v2_100m_baseline_screen_suite.yaml",
    output="benchmark/reports/generated/sparse_v2_100m_baseline_screen_decision",
    score_limit=64,
):
    suite_payload = load_json_or_yaml(suite)
    out = Path(output)
    rows = []
    for path in suite_payload["model_configs"]:
        config = load_json_or_yaml(path)
        materialized = build_model(config, device="meta")
        score = run_lm_eval(config, str(out / "scorecards" / f"{config['model_variant']}.json"), limit=score_limit)
        rows.append({
            "model_variant": config["model_variant"],
            "model_family": config["model_family"],
            "lm_loss": score["scorecard"].get("lm_loss"),
            "code_token_loss": score["scorecard"].get("code_token_loss"),
            "json_token_loss": score["scorecard"].get("json_token_loss"),
            "total_params_actual": materialized.total_params_actual,
            "active_params_per_token_actual": materialized.active_params_per_token_actual,
            "active_flops_per_token": 6 * materialized.active_params_per_token_actual,
            "strict_top1": config.get("experts_active_per_token") == 1 if config["model_family"] != "dense_transformer" else None,
            "config_path": path,
        })
    candidate = next(row for row in rows if row["model_variant"] == CANDIDATE)
    controls = [row for row in rows if row["model_variant"] != CANDIDATE]
    comparisons = [{
        "baseline": row["model_variant"],
        "candidate_minus_baseline_loss": candidate["lm_loss"] - row["lm_loss"],
        "candidate_minus_baseline_active_params": candidate["active_params_per_token_actual"] - row["active_params_per_token_actual"],
        "candidate_quality_win": candidate["lm_loss"] < row["lm_loss"],
        "candidate_active_compute_win": candidate["active_params_per_token_actual"] < row["active_params_per_token_actual"],
    } for row in controls]
    pareto = all(item["candidate_quality_win"] and item["candidate_active_compute_win"] for item in comparisons)
    status = "PVR_SPARSE_V2_100M_PARETO_SCREEN_SUPPORTED" if pareto else "PVR_SPARSE_V2_100M_PARETO_SCREEN_NOT_SUPPORTED"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": status,
        "official_test_data_used_for_selection": False,
        "training_tokens_per_model": suite_payload["training_tokens_per_model"],
        "rows": sorted(rows, key=lambda row: row["lm_loss"]),
        "candidate_comparisons": comparisons,
    }
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_v2_100m_baseline_screen_report.json", payload)
    lines = ["# Sparse-v2 100M Baseline Screen", "", f"Status: `{status}`", "", "| model | LM loss | active params | total params |", "|---|---:|---:|---:|"]
    for row in payload["rows"]:
        lines.append(f"| {row['model_variant']} | {row['lm_loss']} | {row['active_params_per_token_actual']} | {row['total_params_actual']} |")
    (out / "sparse_v2_100m_baseline_screen_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/sparse_v2_100m_baseline_screen/sparse_v2_100m_baseline_screen_suite.yaml")
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_v2_100m_baseline_screen_decision")
    parser.add_argument("--score-limit", type=int, default=64)
    args = parser.parse_args()
    payload = run(suite=args.suite, output=args.output, score_limit=args.score_limit)
    print(json.dumps({"status": payload["status"], "comparisons": payload["candidate_comparisons"]}, indent=2))


if __name__ == "__main__":
    main()
