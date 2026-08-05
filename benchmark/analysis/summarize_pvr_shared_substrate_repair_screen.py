"""Summarize the PVR shared-substrate repair screen."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, load_json_or_yaml, sha256_file, utc_now, write_json


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _variant_config_map(suite_path: Path) -> dict[str, dict[str, Any]]:
    suite = load_json_or_yaml(str(suite_path))
    out = {}
    for item in suite["model_configs"]:
        cfg = load_json_or_yaml(item)
        out[cfg["model_variant"]] = cfg
    return out


def _closest_eval(eval_rows: list[dict[str, Any]], target_tokens: int) -> dict[str, Any] | None:
    if not eval_rows:
        return None
    return min(eval_rows, key=lambda row: abs(int(row.get("training_tokens_seen") or 0) - target_tokens))


def _row(
    report_row: dict[str, Any],
    configs: dict[str, dict[str, Any]],
    rung_tokens: list[int],
    oracle_root: Path,
) -> dict[str, Any]:
    variant = report_row["model_variant"]
    cfg = configs.get(variant, {})
    eval_curve = _load(Path(report_row["eval_curve"])).get("eval_curve", [])
    routing_curve = _load(Path(report_row["routing_curve"])).get("routing_curve", [])
    checkpoint_path = Path(report_row["checkpoint_path"])
    rung_eval = {
        str(target): (_closest_eval(eval_curve, target) or {})
        for target in rung_tokens
    }
    final_eval = eval_curve[-1].get("eval_loss") if eval_curve else None
    final_routing = routing_curve[-1] if routing_curve else {}
    oracle_path = oracle_root / variant / "pvr_final_block_expert_sweep_audit.json"
    oracle_payload = _load(oracle_path)
    oracle_overall = oracle_payload.get("overall") or {}
    return {
        "model_variant": variant,
        "status": report_row.get("status"),
        "config_path": cfg.get("output_path"),
        "checkpoint_path": str(checkpoint_path),
        "checkpoint_hash": sha256_file(checkpoint_path) if checkpoint_path.exists() else "",
        "optimizer_steps": report_row.get("optimizer_steps"),
        "training_tokens_seen": report_row.get("training_tokens_seen"),
        "eval_window_count": report_row.get("eval_window_count"),
        "final_train_loss": report_row.get("final_loss"),
        "final_eval_loss": final_eval,
        "rung_eval": rung_eval,
        "substrate_mode": cfg.get("substrate_mode"),
        "training_curriculum": cfg.get("training_curriculum"),
        "shared_warmup_steps": cfg.get("shared_warmup_steps"),
        "hidden_size": cfg.get("hidden_size"),
        "num_layers": cfg.get("num_layers"),
        "shared_materialization_ffn_size": cfg.get("shared_materialization_ffn_size"),
        "owners_per_token": final_routing.get("owners_per_token"),
        "top2_execution_count": final_routing.get("top2_execution_count"),
        "owner_entropy": final_routing.get("owner_entropy"),
        "prototype_margin": final_routing.get("prototype_margin"),
        "prototype_monopoly_rate": final_routing.get("prototype_monopoly_rate"),
        "oracle_audit_path": str(oracle_path) if oracle_path.exists() else "",
        "selected_expert_loss": oracle_overall.get("selected_loss"),
        "shared_only_loss": oracle_overall.get("shared_only_loss"),
        "oracle_expert_loss": oracle_overall.get("oracle_loss"),
        "router_regret": oracle_overall.get("mean_router_regret"),
        "selected_is_oracle_rate": oracle_overall.get("selected_is_oracle_rate"),
        "selected_is_top2_rate": oracle_overall.get("selected_is_top2_rate"),
        "mean_wrong_loss": oracle_overall.get("mean_wrong_loss"),
        "wrong_expert_harm": (
            oracle_overall.get("mean_wrong_loss") - oracle_overall.get("selected_loss")
            if isinstance(oracle_overall.get("mean_wrong_loss"), (int, float))
            and isinstance(oracle_overall.get("selected_loss"), (int, float))
            else None
        ),
        "vram_peak": report_row.get("vram_peak"),
    }


def run(
    *,
    suite: str = "benchmark/configs/generated/pvr_shared_substrate_repair_screen/pvr_shared_substrate_repair_screen_suite.yaml",
    training_report: str = "benchmark/reports/generated/pvr_shared_substrate_repair_screen_run/training_run_report.json",
    oracle_root: str = "benchmark/reports/generated/pvr_shared_substrate_repair_screen_oracle",
    output: str = "benchmark/reports/generated/pvr_shared_substrate_repair_screen",
) -> dict[str, Any]:
    suite_path = Path(suite)
    report = _load(Path(training_report))
    configs = _variant_config_map(suite_path)
    suite_payload = load_json_or_yaml(str(suite_path))
    rung_tokens = list(suite_payload.get("rung_tokens") or [])
    rows = [_row(row, configs, rung_tokens, Path(oracle_root)) for row in report.get("rows", [])]
    completed = [row for row in rows if row["status"] == "GENUINE_REDUCED_TRAINING_COMPLETE"]
    expected_count = len(configs)
    all_completed = len(completed) == expected_count and expected_count > 0
    valid_windows = all((row.get("eval_window_count") or 0) >= len(rung_tokens) for row in completed)
    strict_top1_clean = all(
        row.get("owners_per_token") == 1.0 and row.get("top2_execution_count") == 0
        for row in completed
        if row.get("owners_per_token") is not None
    )
    oracle_complete = all(row.get("oracle_audit_path") for row in completed)
    winner = min(
        [row for row in completed if isinstance(row.get("final_eval_loss"), (int, float))],
        key=lambda row: row["final_eval_loss"],
        default=None,
    )
    baseline = next((row for row in rows if row["model_variant"] == "pvr_shared_substrate_attention_norms_current_300m"), None)
    winner_delta = None
    if winner and baseline and isinstance(baseline.get("final_eval_loss"), (int, float)):
        winner_delta = winner["final_eval_loss"] - baseline["final_eval_loss"]
    status = "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE" if all_completed and valid_windows else "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_INCOMPLETE_OR_INVALID"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN",
        "status": status,
        "suite": suite,
        "training_report": training_report,
        "expected_variant_count": expected_count,
        "completed_variant_count": len(completed),
        "rung_tokens": rung_tokens,
        "rows": rows,
        "winner": winner,
        "winner_delta_vs_current_attention_norms": winner_delta,
        "claim_gates": {
            "all_variants_completed": all_completed,
            "all_rung_eval_windows_present": valid_windows,
            "strict_top1_clean_for_completed_pvr": strict_top1_clean,
            "final_block_oracle_audits_present": oracle_complete,
            "official_final_files_used": False,
        },
        "decision": (
            "PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED"
            if winner and baseline and winner["model_variant"] != baseline["model_variant"] and winner_delta is not None and winner_delta < 0
            else "PVR_SHARED_SUBSTRATE_REPAIR_NOT_SUPPORTED"
        ),
        "scope": "Teacher-independent substrate screen on broad_nlp_train with official_like_dev evaluation. Final official bounded files are not used.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_shared_substrate_repair_screen.json", payload)
    lines = [
        "# PVR Shared Substrate Repair Screen",
        "",
        f"Status: `{status}`",
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
        "| variant | substrate | curriculum | tokens | eval windows | final eval | final train | owner entropy | margin | monopoly |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['model_variant']} | {row.get('substrate_mode')} | {row.get('training_curriculum')} | "
            f"{row.get('training_tokens_seen')} | {row.get('eval_window_count')} | {row.get('final_eval_loss')} | "
            f"{row.get('final_train_loss')} | {row.get('owner_entropy')} | {row.get('prototype_margin')} | {row.get('prototype_monopoly_rate')} |"
        )
    lines.extend(["", "## Rung Eval Losses", ""])
    for row in rows:
        lines.append(f"### {row['model_variant']}")
        for target, eval_row in row.get("rung_eval", {}).items():
            lines.append(f"- `{target}` tokens: step `{eval_row.get('optimizer_step')}`, eval loss `{eval_row.get('eval_loss')}`")
        lines.append("")
    if winner:
        lines.extend([
            "## Winner",
            "",
            f"Winner: `{winner['model_variant']}`",
            f"Delta vs current attention+norms baseline: `{winner_delta}`",
        ])
    lines.extend([
        "",
        "## Final-Block Oracle / Regret",
        "",
        "| variant | selected | shared-only | oracle | regret | oracle rate | top2 rate | mean wrong | wrong harm |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in rows:
        lines.append(
            f"| {row['model_variant']} | {row.get('selected_expert_loss')} | {row.get('shared_only_loss')} | "
            f"{row.get('oracle_expert_loss')} | {row.get('router_regret')} | {row.get('selected_is_oracle_rate')} | "
            f"{row.get('selected_is_top2_rate')} | {row.get('mean_wrong_loss')} | {row.get('wrong_expert_harm')} |"
        )
    (out / "pvr_shared_substrate_repair_screen.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default="benchmark/configs/generated/pvr_shared_substrate_repair_screen/pvr_shared_substrate_repair_screen_suite.yaml")
    parser.add_argument("--training-report", default="benchmark/reports/generated/pvr_shared_substrate_repair_screen_run/training_run_report.json")
    parser.add_argument("--oracle-root", default="benchmark/reports/generated/pvr_shared_substrate_repair_screen_oracle")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_shared_substrate_repair_screen")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
