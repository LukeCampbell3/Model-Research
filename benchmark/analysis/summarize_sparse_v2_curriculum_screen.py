"""Score and select a teacher-free sparse-v2 curriculum without official test data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, utc_now, write_json
from benchmark.runners.run_lm_eval import run as run_lm_eval


def _curve(path: Path, key: str) -> list[dict[str, Any]]:
    return list((load_json_or_yaml(path).get(key) or [])) if path.exists() else []


def run(
    *,
    suite: str = "benchmark/configs/generated/sparse_v2_curriculum_screen/sparse_v2_curriculum_screen_suite.yaml",
    output: str = "benchmark/reports/generated/sparse_v2_curriculum_screen_decision",
    score_limit: int = 64,
) -> dict[str, Any]:
    suite_payload = load_json_or_yaml(suite)
    out = Path(output)
    score_root = out / "scorecards"
    rows = []
    for config_path in suite_payload["model_configs"]:
        config = load_json_or_yaml(config_path)
        score_path = score_root / f"{config['model_variant']}.json"
        score = run_lm_eval(config, str(score_path), limit=score_limit)
        training = _curve(Path(config["output_path"]) / "training_curve.json", "loss_curve")
        routing = _curve(Path(config["output_path"]) / "routing_curve.json", "routing_curve")
        phase2 = [row for row in training if row.get("phase") == "matched_specialization_budget"]
        router_gradient_max = max((float(row.get("router_gradient_norm") or 0.0) for row in phase2), default=0.0)
        top1_clean = bool(routing) and all(
            row.get("owners_per_token") == 1.0
            and row.get("top2_execution_count") == 0
            and row.get("top4_execution_count") == 0
            for row in routing
        )
        rows.append({
            "model_variant": config["model_variant"],
            "training_curriculum": config["training_curriculum"],
            "routing_aux_weight": config["routing_aux_weight"],
            "prototype_routing": config["prototype_routing"],
            "lm_loss": score["scorecard"].get("lm_loss"),
            "code_token_loss": score["scorecard"].get("code_token_loss"),
            "json_token_loss": score["scorecard"].get("json_token_loss"),
            "router_gradient_max": router_gradient_max,
            "router_gradient_present": router_gradient_max > 0.0,
            "top1_clean": top1_clean,
            "checkpoint_path": config["checkpoint_path"],
            "config_path": config_path,
        })
    eligible = [
        row for row in rows
        if isinstance(row["lm_loss"], (int, float)) and row["router_gradient_present"] and row["top1_clean"]
    ]
    ranked = sorted(eligible, key=lambda row: row["lm_loss"])
    winner = ranked[0] if ranked else None
    full = next((row for row in rows if row["training_curriculum"] == "full_training"), None)
    status = "PVR_SPARSE_V2_CURRICULUM_SCREEN_SUPPORTED" if winner and full and winner["lm_loss"] < full["lm_loss"] else "PVR_SPARSE_V2_CURRICULUM_SCREEN_NOT_SUPPORTED"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": status,
        "official_test_data_used_for_selection": False,
        "selection_dataset": "local Frankenstein heldout plus diagnostic code/JSON losses",
        "rows": rows,
        "winner": winner,
        "winner_delta_vs_full_from_start": (
            winner["lm_loss"] - full["lm_loss"] if winner and full else None
        ),
        "promotion_rule": suite_payload["selection_rule"],
    }
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "sparse_v2_curriculum_screen_report.json", payload)
    lines = [
        "# Sparse-v2 Teacher-Free Curriculum Screen",
        "",
        f"Status: `{status}`",
        "",
        "| variant | curriculum | aux | prototypes | LM loss | router grad | Top1 |",
        "|---|---|---:|---|---:|---:|---|",
    ]
    for row in sorted(rows, key=lambda item: item["lm_loss"] if isinstance(item["lm_loss"], (int, float)) else 1e9):
        lines.append(
            f"| {row['model_variant']} | {row['training_curriculum']} | {row['routing_aux_weight']} | "
            f"{row['prototype_routing']} | {row['lm_loss']} | {row['router_gradient_max']} | {row['top1_clean']} |"
        )
    (out / "sparse_v2_curriculum_screen_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/sparse_v2_curriculum_screen/sparse_v2_curriculum_screen_suite.yaml")
    parser.add_argument("--output", default="benchmark/reports/generated/sparse_v2_curriculum_screen_decision")
    parser.add_argument("--score-limit", type=int, default=64)
    args = parser.parse_args()
    payload = run(suite=args.suite, output=args.output, score_limit=args.score_limit)
    print(json.dumps({"status": payload["status"], "winner": payload["winner"]}, indent=2))


if __name__ == "__main__":
    main()
