"""Summarize the 1M-token PVR router-regret repair refinement sweep."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.analysis.summarize_pvr_router_regret_repair_screen import _configs, _load, _row
from benchmark.common import git_commit, load_json_or_yaml, utc_now, write_json


def _baseline_from_reference(path: Path) -> dict[str, Any]:
    payload = _load(path)
    baseline = payload.get("baseline")
    if not isinstance(baseline, dict):
        return {}
    return baseline


def run(
    *,
    suite: str = "benchmark/configs/generated/pvr_router_regret_repair_1m_refinement/pvr_router_regret_repair_1m_refinement_suite.yaml",
    training_report: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_refinement_run/training_run_report.json",
    oracle_root: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_refinement_oracle",
    baseline_report: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation/pvr_router_repair_screen.json",
    output: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_refinement",
) -> dict[str, Any]:
    suite_path = Path(suite)
    report = _load(Path(training_report))
    cfgs = _configs(suite_path)
    rows = [_row(row, cfgs, Path(oracle_root)) for row in report.get("rows", [])]
    completed = [row for row in rows if row.get("status") == "GENUINE_REDUCED_TRAINING_COMPLETE"]
    baseline = _baseline_from_reference(Path(baseline_report))
    candidates = [
        row
        for row in completed
        if isinstance(row.get("final_eval_loss"), (int, float))
        and isinstance(row.get("final_block_router_regret"), (int, float))
    ]
    winner = min(candidates, key=lambda row: row["final_eval_loss"], default=None)
    regret_winner = min(candidates, key=lambda row: row["final_block_router_regret"], default=None)
    all_completed = len(completed) == len(cfgs) and bool(cfgs)
    strict_top1 = all(
        row.get("owners_per_token") == 1.0 and row.get("top2_execution_count") == 0
        for row in completed
        if row.get("owners_per_token") is not None
    )
    oracle_present = all(row.get("oracle_audit_path") for row in completed)
    delta_eval = None
    delta_regret = None
    if baseline and winner:
        if isinstance(baseline.get("final_eval_loss"), (int, float)):
            delta_eval = winner["final_eval_loss"] - baseline["final_eval_loss"]
        if isinstance(baseline.get("final_block_router_regret"), (int, float)):
            delta_regret = winner["final_block_router_regret"] - baseline["final_block_router_regret"]
    supported = (
        winner is not None
        and isinstance(delta_eval, (int, float))
        and delta_eval < 0.0
        and isinstance(delta_regret, (int, float))
        and delta_regret < 0.0
        and strict_top1
        and all_completed
        and oracle_present
    )
    regret_reduced_any = (
        regret_winner is not None
        and isinstance(baseline.get("final_block_router_regret"), (int, float))
        and regret_winner["final_block_router_regret"] < baseline["final_block_router_regret"]
    )
    if supported:
        decision = "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_SUPPORTED"
    elif regret_reduced_any:
        decision = "PVR_ROUTER_REGRET_REPAIR_REDUCES_REGRET_BUT_LM_NOT_SUPPORTED"
    else:
        decision = "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_NOT_SUPPORTED"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT",
        "status": "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_COMPLETE" if all_completed and oracle_present else "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID",
        "decision": decision,
        "suite": suite,
        "training_report": training_report,
        "baseline_reference_report": baseline_report,
        "baseline": baseline,
        "rows": rows,
        "winner": winner,
        "regret_winner": regret_winner,
        "winner_delta_vs_baseline_eval": delta_eval,
        "winner_delta_vs_baseline_final_block_regret": delta_regret,
        "claim_gates": {
            "all_variants_completed": all_completed,
            "final_block_oracle_audits_present": oracle_present,
            "strict_top1_clean_for_completed_pvr": strict_top1,
            "winner_improves_eval": isinstance(delta_eval, (int, float)) and delta_eval < 0.0,
            "winner_reduces_final_block_regret": isinstance(delta_regret, (int, float)) and delta_regret < 0.0,
            "official_final_files_used": False,
        },
        "scope": "Bounded 1M-token lower-weight router-regret refinement on broad_nlp_train with official_like_dev evaluation. The 1M no-regret baseline is reused from the completed confirmation report; final official bounded files are not used.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_regret_repair_1m_refinement.json", payload)
    lines = [
        "# PVR Router Regret Repair 1M Refinement",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["scope"],
        "",
        "## Baseline Reference",
        "",
        f"Variant: `{baseline.get('model_variant')}`",
        f"Final eval: `{baseline.get('final_eval_loss')}`",
        f"Final-block regret: `{baseline.get('final_block_router_regret')}`",
        "",
        "## Claim Gates",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["claim_gates"].items()],
        "",
        "## Result Table",
        "",
        "| variant | regret w | final eval | mean eval | final train | train regret | final-block regret | oracle rate | top2 rate | Top1 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['model_variant']} | {row.get('router_regret_aux_weight')} | "
            f"{row.get('final_eval_loss')} | {row.get('mean_eval_loss')} | {row.get('final_train_loss')} | "
            f"{row.get('router_expected_regret_loss_train')} | {row.get('final_block_router_regret')} | "
            f"{row.get('selected_is_oracle_rate')} | {row.get('selected_is_top2_rate')} | "
            f"{row.get('owners_per_token') == 1.0 and row.get('top2_execution_count') == 0} |"
        )
    if winner:
        lines.extend(
            [
                "",
                "## Winner By Eval",
                "",
                f"Winner: `{winner['model_variant']}`",
                f"Eval delta vs 1M baseline: `{delta_eval}`",
                f"Final-block regret delta vs 1M baseline: `{delta_regret}`",
            ]
        )
    if regret_winner:
        lines.extend(
            [
                "",
                "## Winner By Regret",
                "",
                f"Winner: `{regret_winner['model_variant']}`",
                f"Final-block regret: `{regret_winner.get('final_block_router_regret')}`",
                f"Final eval: `{regret_winner.get('final_eval_loss')}`",
            ]
        )
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "This report tests whether lower regret weights can improve official-like LM loss while reducing final-block regret. It does not use final official bounded files and does not support teacher independence or architecture superiority by itself.",
        ]
    )
    (out / "pvr_router_regret_repair_1m_refinement.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/pvr_router_regret_repair_1m_refinement/pvr_router_regret_repair_1m_refinement_suite.yaml")
    parser.add_argument("--training-report", default="benchmark/reports/generated/pvr_router_regret_repair_1m_refinement_run/training_run_report.json")
    parser.add_argument("--oracle-root", default="benchmark/reports/generated/pvr_router_regret_repair_1m_refinement_oracle")
    parser.add_argument("--baseline-report", default="benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation/pvr_router_repair_screen.json")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_regret_repair_1m_refinement")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
