"""Summarize bounded PVR router-regret repair screen."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, load_json_or_yaml, sha256_file, utc_now, write_json


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _configs(suite_path: Path) -> dict[str, dict[str, Any]]:
    suite = load_json_or_yaml(str(suite_path))
    out = {}
    for path in suite["model_configs"]:
        cfg = load_json_or_yaml(path)
        out[cfg["model_variant"]] = cfg
    return out


def _row(report_row: dict[str, Any], configs: dict[str, dict[str, Any]], oracle_root: Path) -> dict[str, Any]:
    variant = report_row["model_variant"]
    cfg = configs.get(variant, {})
    eval_curve = _load(Path(report_row["eval_curve"])).get("eval_curve", [])
    train_curve = _load(Path(report_row["training_curve"])).get("loss_curve", [])
    routing_curve = _load(Path(report_row["routing_curve"])).get("routing_curve", [])
    oracle_path = oracle_root / variant / "pvr_final_block_expert_sweep_audit.json"
    oracle = _load(oracle_path).get("overall") or {}
    ckpt = Path(report_row["checkpoint_path"])
    final_train_row = train_curve[-1] if train_curve else {}
    final_routing = routing_curve[-1] if routing_curve else {}
    return {
        "model_variant": variant,
        "status": report_row.get("status"),
        "checkpoint_path": str(ckpt),
        "checkpoint_hash": sha256_file(ckpt) if ckpt.exists() else "",
        "optimizer_steps": report_row.get("optimizer_steps"),
        "training_tokens_seen": report_row.get("training_tokens_seen"),
        "eval_window_count": report_row.get("eval_window_count"),
        "final_train_loss": report_row.get("final_loss"),
        "final_eval_loss": eval_curve[-1].get("eval_loss") if eval_curve else None,
        "mean_eval_loss": (
            sum(row["eval_loss"] for row in eval_curve if row.get("eval_loss") is not None)
            / max(1, len([row for row in eval_curve if row.get("eval_loss") is not None]))
            if eval_curve
            else None
        ),
        "router_regret_aux_weight": cfg.get("router_regret_aux_weight"),
        "router_oracle_kl_weight": cfg.get("router_oracle_kl_weight"),
        "router_expected_regret_loss_train": final_train_row.get("router_expected_regret_loss"),
        "router_oracle_kl_loss_train": final_train_row.get("router_oracle_kl_loss"),
        "router_selected_is_oracle_rate_train": final_train_row.get("router_selected_is_oracle_rate_train"),
        "router_selected_is_top2_rate_train": final_train_row.get("router_selected_is_top2_rate_train"),
        "owners_per_token": final_routing.get("owners_per_token"),
        "top2_execution_count": final_routing.get("top2_execution_count"),
        "owner_entropy": final_routing.get("owner_entropy"),
        "prototype_margin": final_routing.get("prototype_margin"),
        "prototype_monopoly_rate": final_routing.get("prototype_monopoly_rate"),
        "oracle_audit_path": str(oracle_path) if oracle_path.exists() else "",
        "selected_expert_loss": oracle.get("selected_loss"),
        "shared_only_loss": oracle.get("shared_only_loss"),
        "oracle_expert_loss": oracle.get("oracle_loss"),
        "final_block_router_regret": oracle.get("mean_router_regret"),
        "selected_is_oracle_rate": oracle.get("selected_is_oracle_rate"),
        "selected_is_top2_rate": oracle.get("selected_is_top2_rate"),
        "mean_wrong_loss": oracle.get("mean_wrong_loss"),
        "wrong_expert_harm": (
            oracle.get("mean_wrong_loss") - oracle.get("selected_loss")
            if isinstance(oracle.get("mean_wrong_loss"), (int, float)) and isinstance(oracle.get("selected_loss"), (int, float))
            else None
        ),
    }


def run(
    *,
    suite: str = "benchmark/configs/generated/pvr_router_regret_repair_screen/pvr_router_regret_repair_screen_suite.yaml",
    training_report: str = "benchmark/reports/generated/pvr_router_regret_repair_screen_run/training_run_report.json",
    oracle_root: str = "benchmark/reports/generated/pvr_router_regret_repair_screen_oracle",
    output: str = "benchmark/reports/generated/pvr_router_repair_screen",
) -> dict[str, Any]:
    suite_path = Path(suite)
    report = _load(Path(training_report))
    cfgs = _configs(suite_path)
    rows = [_row(row, cfgs, Path(oracle_root)) for row in report.get("rows", [])]
    completed = [row for row in rows if row.get("status") == "GENUINE_REDUCED_TRAINING_COMPLETE"]
    baseline = next(
        (
            row
            for row in rows
            if float(row.get("router_regret_aux_weight") or 0.0) == 0.0
            and float(row.get("router_oracle_kl_weight") or 0.0) == 0.0
        ),
        None,
    )
    winner = min(
        [row for row in completed if isinstance(row.get("final_eval_loss"), (int, float))],
        key=lambda row: row["final_eval_loss"],
        default=None,
    )
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
        if isinstance(winner.get("final_eval_loss"), (int, float)) and isinstance(baseline.get("final_eval_loss"), (int, float)):
            delta_eval = winner["final_eval_loss"] - baseline["final_eval_loss"]
        if isinstance(winner.get("final_block_router_regret"), (int, float)) and isinstance(baseline.get("final_block_router_regret"), (int, float)):
            delta_regret = winner["final_block_router_regret"] - baseline["final_block_router_regret"]
    supported = (
        winner is not None
        and baseline is not None
        and winner["model_variant"] != baseline["model_variant"]
        and isinstance(delta_eval, (int, float))
        and delta_eval < 0.0
        and isinstance(delta_regret, (int, float))
        and delta_regret < 0.0
        and strict_top1
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_REPAIR_SCREEN",
        "status": "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE" if all_completed and oracle_present else "PVR_ROUTER_REGRET_REPAIR_SCREEN_INCOMPLETE_OR_INVALID",
        "decision": "PVR_ROUTER_REGRET_REPAIR_SUPPORTED" if supported else "PVR_ROUTER_REGRET_REPAIR_NOT_SUPPORTED",
        "suite": suite,
        "training_report": training_report,
        "rows": rows,
        "winner": winner,
        "baseline": baseline,
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
        "scope": "Bounded 500K-token router-regret repair screen on broad_nlp_train with official_like_dev evaluation. Final official bounded files are not used.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_repair_screen.json", payload)
    lines = [
        "# PVR Router Regret Repair Screen",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["scope"],
        "",
        "## Claim Gates",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["claim_gates"].items()],
        "",
        "## Result Table",
        "",
        "| variant | regret w | KL w | final eval | mean eval | final train | train regret | train oracle rate | final-block regret | oracle rate | top2 rate | Top1 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['model_variant']} | {row.get('router_regret_aux_weight')} | {row.get('router_oracle_kl_weight')} | "
            f"{row.get('final_eval_loss')} | {row.get('mean_eval_loss')} | {row.get('final_train_loss')} | "
            f"{row.get('router_expected_regret_loss_train')} | {row.get('router_selected_is_oracle_rate_train')} | "
            f"{row.get('final_block_router_regret')} | {row.get('selected_is_oracle_rate')} | {row.get('selected_is_top2_rate')} | "
            f"{row.get('owners_per_token') == 1.0 and row.get('top2_execution_count') == 0} |"
        )
    if winner:
        lines.extend([
            "",
            "## Winner",
            "",
            f"Winner: `{winner['model_variant']}`",
            f"Eval delta vs baseline: `{delta_eval}`",
            f"Final-block regret delta vs baseline: `{delta_regret}`",
        ])
    lines.extend([
        "",
        "## Interpretation Boundary",
        "",
        "This is a bounded final-block regret repair screen. It does not prove full-network router repair, official benchmark advantage, or teacher independence.",
    ])
    (out / "pvr_router_repair_screen.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/pvr_router_regret_repair_screen/pvr_router_regret_repair_screen_suite.yaml")
    parser.add_argument("--training-report", default="benchmark/reports/generated/pvr_router_regret_repair_screen_run/training_run_report.json")
    parser.add_argument("--oracle-root", default="benchmark/reports/generated/pvr_router_regret_repair_screen_oracle")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_repair_screen")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
