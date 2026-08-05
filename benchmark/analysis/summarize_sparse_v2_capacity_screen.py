"""Select a sparse-v2 capacity allocation under the Top2 active budget."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.model_factory import build_model
from benchmark.runners.run_lm_eval import run as run_lm_eval


def run(
    *,
    suite="benchmark/configs/generated/sparse_v2_capacity_screen/sparse_v2_capacity_screen_suite.yaml",
    baseline_report="benchmark/reports/generated/sparse_v2_100m_baseline_screen_decision/sparse_v2_100m_baseline_screen_report.json",
    output="benchmark/reports/generated/sparse_v2_capacity_screen_decision",
    score_limit=64,
):
    spec = load_json_or_yaml(suite)
    baselines = load_json_or_yaml(baseline_report)
    top2 = next(row for row in baselines["rows"] if row["model_family"] == "generic_top2_moe_reference")
    out = Path(output)
    rows = []
    for path in spec["model_configs"]:
        config = load_json_or_yaml(path)
        model = build_model(config, device="meta")
        score = run_lm_eval(config, str(out / "scorecards" / f"{config['model_variant']}.json"), limit=score_limit)
        rows.append({
            "model_variant": config["model_variant"],
            "lm_loss": score["scorecard"].get("lm_loss"),
            "code_token_loss": score["scorecard"].get("code_token_loss"),
            "num_experts": config["num_experts_if_applicable"],
            "shared_ffn_size": config.get("shared_materialization_ffn_size"),
            "expert_ffn_size": config.get("materialization_ffn_size"),
            "total_params_actual": model.total_params_actual,
            "active_params_per_token_actual": model.active_params_per_token_actual,
            "below_top2_active_budget": model.active_params_per_token_actual < top2["active_params_per_token_actual"],
            "config_path": path,
        })
    eligible = [row for row in rows if row["below_top2_active_budget"]]
    winner = min(eligible, key=lambda row: row["lm_loss"])
    original = rows[0]
    closes_top2 = winner["lm_loss"] < top2["lm_loss"]
    improves = winner["lm_loss"] < original["lm_loss"]
    status = (
        "PVR_SPARSE_V2_CAPACITY_SCREEN_BEATS_TOP2"
        if closes_top2
        else "PVR_SPARSE_V2_CAPACITY_SCREEN_SUPPORTED"
        if improves
        else "PVR_SPARSE_V2_CAPACITY_SCREEN_NOT_SUPPORTED"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": status,
        "official_test_data_used_for_selection": False,
        "top2_reference": top2,
        "rows": sorted(rows, key=lambda row: row["lm_loss"]),
        "winner": winner,
        "winner_delta_vs_original": winner["lm_loss"] - original["lm_loss"],
        "winner_delta_vs_top2": winner["lm_loss"] - top2["lm_loss"],
    }
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_v2_capacity_screen_report.json", payload)
    lines = ["# Sparse-v2 Capacity Screen", "", f"Status: `{status}`", "", "| model | loss | active params | total params |", "|---|---:|---:|---:|"]
    for row in payload["rows"]:
        lines.append(f"| {row['model_variant']} | {row['lm_loss']} | {row['active_params_per_token_actual']} | {row['total_params_actual']} |")
    (out / "sparse_v2_capacity_screen_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/sparse_v2_capacity_screen/sparse_v2_capacity_screen_suite.yaml")
    parser.add_argument("--baseline-report", default="benchmark/reports/generated/sparse_v2_100m_baseline_screen_decision/sparse_v2_100m_baseline_screen_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_v2_capacity_screen_decision")
    parser.add_argument("--score-limit", type=int, default=64)
    args = parser.parse_args()
    payload = run(suite=args.suite, baseline_report=args.baseline_report, output=args.output, score_limit=args.score_limit)
    print(json.dumps({"status": payload["status"], "winner": payload["winner"], "delta_vs_top2": payload["winner_delta_vs_top2"]}, indent=2))


if __name__ == "__main__":
    main()
