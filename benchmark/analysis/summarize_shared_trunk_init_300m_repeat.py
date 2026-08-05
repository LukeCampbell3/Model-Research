"""Summarize repeat 300M shared-trunk init confirmation results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_SCORECARD_SUPPORTED_EVAL_MIXED = "PVR_SHARED_TRUNK_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED"
STATUS_REPEAT_SUPPORTED = "PVR_SHARED_TRUNK_INIT_300M_REPEAT_SUPPORTED"
STATUS_NOT_SUPPORTED = "PVR_SHARED_TRUNK_INIT_300M_REPEAT_NOT_SUPPORTED"


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(str(path).replace("\\", "/")).read_text(encoding="utf-8"))


def _score(path: str | Path) -> dict[str, Any]:
    return _load(path)["scorecard"]


def run(
    *,
    seed_report: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/shared_trunk_init_seed_report.json",
    baseline_scorecard: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json",
    init_scorecard: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json",
    dense_reference_report: str = "benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json",
    output: str = "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42_decision",
) -> dict[str, Any]:
    report = _load(seed_report)
    baseline_card = _score(baseline_scorecard)
    init_card = _score(init_scorecard)
    dense_rows = _load(dense_reference_report).get("rows", [])
    dense = next((row for row in dense_rows if row.get("model") == "dense_transformer_300m"), {})
    init_row = report["summary"]["rows"]["shared_trunk_init_from_dense"]
    baseline_row = report["summary"]["rows"]["baseline"]
    lm_delta_vs_baseline = float(init_card["lm_loss"]) - float(baseline_card["lm_loss"])
    lm_delta_vs_dense = float(init_card["lm_loss"]) - float(dense["lm_loss"])
    eval_curve_supported = bool(init_row.get("loss_supported") and init_row.get("route_stable"))
    scorecard_supported = lm_delta_vs_baseline < 0 and lm_delta_vs_dense < 0 and init_row.get("route_stable")
    status = (
        STATUS_REPEAT_SUPPORTED if eval_curve_supported and scorecard_supported
        else STATUS_SCORECARD_SUPPORTED_EVAL_MIXED if scorecard_supported
        else STATUS_NOT_SUPPORTED
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": status,
        "seed": report.get("seed"),
        "source_seed_report": seed_report,
        "training_eval_curve_decision": {
            "status": report.get("status"),
            "baseline_pvr_mean_eval_loss": baseline_row.get("mean_eval_loss"),
            "shared_trunk_init_mean_eval_loss": init_row.get("mean_eval_loss"),
            "init_minus_baseline_mean_eval_loss": init_row.get("deltas", {}).get("mean_eval_loss_delta_vs_baseline"),
            "baseline_pvr_final_train_loss": baseline_row.get("final_train_loss"),
            "shared_trunk_init_final_train_loss": init_row.get("final_train_loss"),
            "init_minus_baseline_final_train_loss": init_row.get("deltas", {}).get("final_train_loss_delta_vs_baseline"),
        },
        "reduced_lm_scorecard_decision": {
            "baseline_pvr_lm_loss": baseline_card.get("lm_loss"),
            "shared_trunk_init_pvr_lm_loss": init_card.get("lm_loss"),
            "dense_reference_lm_loss": dense.get("lm_loss"),
            "init_minus_baseline_lm_loss": lm_delta_vs_baseline,
            "init_minus_dense_lm_loss": lm_delta_vs_dense,
            "scorecard_dense_gap_closed": lm_delta_vs_dense < 0,
            "paths": {
                "baseline": baseline_scorecard,
                "shared_trunk_init": init_scorecard,
            },
        },
        "route_stability": {
            "top1_invariants_clean": init_row.get("top1_invariants_clean"),
            "route_stable": init_row.get("route_stable"),
            "mean_route_margin_delta_vs_baseline": init_row.get("deltas", {}).get("mean_route_margin_delta_vs_baseline"),
            "mean_owner_entropy_delta_vs_baseline": init_row.get("deltas", {}).get("mean_owner_entropy_delta_vs_baseline"),
            "mean_prototype_monopoly_rate_delta_vs_baseline": init_row.get("deltas", {}).get("mean_prototype_monopoly_rate_delta_vs_baseline"),
        },
        "interpretation": (
            "Repeat seed supports the reduced LM scorecard dense-gap claim, but does not support the training eval-curve "
            "gate because mean eval loss regressed while final train loss and reduced LM loss improved."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "shared_trunk_init_300m_repeat_decision_report.json", payload)
    lines = [
        "# Shared-Trunk Init 300M Repeat Decision",
        "",
        f"Status: `{payload['status']}`",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        "```",
        "",
    ]
    (out / "shared_trunk_init_300m_repeat_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-report", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/shared_trunk_init_seed_report.json")
    parser.add_argument("--baseline-scorecard", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json")
    parser.add_argument("--init-scorecard", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json")
    parser.add_argument("--dense-reference-report", default="benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42_decision")
    args = parser.parse_args()
    payload = run(
        seed_report=args.seed_report,
        baseline_scorecard=args.baseline_scorecard,
        init_scorecard=args.init_scorecard,
        dense_reference_report=args.dense_reference_report,
        output=args.output,
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
