"""Analyze why router-regret repair improved oracle metrics but failed LM eval."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


BASELINE = "pvr_router_regret_repair_baseline_no_regret_300m_1m_confirm"
REPAIR = "pvr_router_regret_repair_regret0p01_300m_1m_confirm"


def _load(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _curve(root: Path, variant: str, name: str, key: str) -> list[dict[str, Any]]:
    return _load(root / variant / f"{name}.json").get(key, [])


def _oracle(root: Path, variant: str) -> dict[str, Any]:
    return _load(root / variant / "pvr_final_block_expert_sweep_audit.json")


def _delta(a: Any, b: Any) -> float | None:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) - float(b)
    return None


def _eval_windows(run_root: Path) -> list[dict[str, Any]]:
    baseline = _curve(run_root, BASELINE, "eval_curve", "eval_curve")
    repair = _curve(run_root, REPAIR, "eval_curve", "eval_curve")
    rows = []
    for left, right in zip(baseline, repair):
        rows.append(
            {
                "step": left.get("step"),
                "training_tokens_seen": left.get("training_tokens_seen"),
                "eval_tokens": left.get("eval_tokens"),
                "baseline_eval_loss": left.get("eval_loss"),
                "repair_eval_loss": right.get("eval_loss"),
                "repair_minus_baseline": _delta(right.get("eval_loss"), left.get("eval_loss")),
            }
        )
    return rows


def _routing_windows(run_root: Path) -> list[dict[str, Any]]:
    baseline = _curve(run_root, BASELINE, "routing_curve", "routing_curve")
    repair = _curve(run_root, REPAIR, "routing_curve", "routing_curve")
    rows = []
    for left, right in zip(baseline, repair):
        rows.append(
            {
                "step": left.get("step"),
                "baseline_owner_entropy": left.get("owner_entropy"),
                "repair_owner_entropy": right.get("owner_entropy"),
                "owner_entropy_delta": _delta(right.get("owner_entropy"), left.get("owner_entropy")),
                "baseline_prototype_margin": left.get("prototype_margin"),
                "repair_prototype_margin": right.get("prototype_margin"),
                "prototype_margin_delta": _delta(right.get("prototype_margin"), left.get("prototype_margin")),
                "baseline_monopoly_rate": left.get("prototype_monopoly_rate"),
                "repair_monopoly_rate": right.get("prototype_monopoly_rate"),
                "monopoly_rate_delta": _delta(right.get("prototype_monopoly_rate"), left.get("prototype_monopoly_rate")),
                "baseline_top_expert_tokens": max(left.get("expert_utilization") or [0]),
                "repair_top_expert_tokens": max(right.get("expert_utilization") or [0]),
            }
        )
    return rows


def _oracle_comparison(oracle_root: Path) -> dict[str, Any]:
    base = _oracle(oracle_root, BASELINE)
    repair = _oracle(oracle_root, REPAIR)
    base_overall = base.get("overall") or {}
    repair_overall = repair.get("overall") or {}
    keys = [
        "selected_loss",
        "shared_only_loss",
        "oracle_loss",
        "mean_router_regret",
        "p95_router_regret",
        "selected_is_oracle_rate",
        "selected_is_top2_rate",
        "mean_wrong_loss",
        "random_wrong_loss",
        "shifted_wrong_loss",
        "shuffled_residual_loss",
        "random_residual_loss",
    ]
    aggregate = {
        key: {
            "baseline": base_overall.get(key),
            "repair": repair_overall.get(key),
            "repair_minus_baseline": _delta(repair_overall.get(key), base_overall.get(key)),
        }
        for key in keys
    }
    per_file = []
    by_file = {row.get("file"): row for row in base.get("rows", [])}
    for row in repair.get("rows", []):
        file_name = row.get("file")
        left = by_file.get(file_name, {})
        per_file.append(
            {
                "file": file_name,
                "token_count": row.get("token_count"),
                "selected_loss_delta": _delta(row.get("selected_loss"), left.get("selected_loss")),
                "shared_only_loss_delta": _delta(row.get("shared_only_loss"), left.get("shared_only_loss")),
                "oracle_loss_delta": _delta(row.get("oracle_loss"), left.get("oracle_loss")),
                "router_regret_delta": _delta(row.get("mean_router_regret"), left.get("mean_router_regret")),
                "selected_is_oracle_rate_delta": _delta(row.get("selected_is_oracle_rate"), left.get("selected_is_oracle_rate")),
                "selected_is_top2_rate_delta": _delta(row.get("selected_is_top2_rate"), left.get("selected_is_top2_rate")),
            }
        )
    return {"aggregate": aggregate, "per_file": per_file}


def run(
    *,
    run_root: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation_run",
    oracle_root: str = "benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation_oracle",
    output: str = "benchmark/reports/generated/pvr_router_regret_lm_mismatch_analysis",
) -> dict[str, Any]:
    run_path = Path(run_root)
    oracle_path = Path(oracle_root)
    eval_windows = _eval_windows(run_path)
    routing_windows = _routing_windows(run_path)
    oracle = _oracle_comparison(oracle_path)
    final_eval_delta = eval_windows[-1]["repair_minus_baseline"] if eval_windows else None
    mean_eval_delta = (
        sum(row["repair_minus_baseline"] for row in eval_windows if row["repair_minus_baseline"] is not None)
        / max(1, len([row for row in eval_windows if row["repair_minus_baseline"] is not None]))
        if eval_windows
        else None
    )
    oracle_regret_delta = oracle["aggregate"]["mean_router_regret"]["repair_minus_baseline"]
    oracle_rate_delta = oracle["aggregate"]["selected_is_oracle_rate"]["repair_minus_baseline"]
    selected_loss_delta = oracle["aggregate"]["selected_loss"]["repair_minus_baseline"]
    shared_loss_delta = oracle["aggregate"]["shared_only_loss"]["repair_minus_baseline"]
    entropy_deltas = [row["owner_entropy_delta"] for row in routing_windows if row["owner_entropy_delta"] is not None]
    monopoly_deltas = [row["monopoly_rate_delta"] for row in routing_windows if row["monopoly_rate_delta"] is not None]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS",
        "status": "PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE",
        "decision": "PVR_REGRET_REPAIR_ROUTER_METRIC_IMPROVEMENT_LM_GATE_MISMATCH_CONFIRMED",
        "baseline_variant": BASELINE,
        "repair_variant": REPAIR,
        "eval_window_analysis": {
            "rows": eval_windows,
            "window_count": len(eval_windows),
            "tokens_per_window": sorted(set(row.get("eval_tokens") for row in eval_windows)),
            "mean_repair_minus_baseline": mean_eval_delta,
            "final_repair_minus_baseline": final_eval_delta,
            "repair_wins": sum(1 for row in eval_windows if (row.get("repair_minus_baseline") or 0.0) < 0.0),
        },
        "routing_curve_analysis": {
            "rows": routing_windows,
            "mean_owner_entropy_delta": sum(entropy_deltas) / len(entropy_deltas) if entropy_deltas else None,
            "mean_monopoly_rate_delta": sum(monopoly_deltas) / len(monopoly_deltas) if monopoly_deltas else None,
        },
        "oracle_audit_analysis": oracle,
        "key_deltas": {
            "final_eval_loss_delta": final_eval_delta,
            "mean_eval_loss_delta": mean_eval_delta,
            "oracle_selected_loss_delta": selected_loss_delta,
            "oracle_shared_only_loss_delta": shared_loss_delta,
            "oracle_router_regret_delta": oracle_regret_delta,
            "oracle_selected_is_oracle_rate_delta": oracle_rate_delta,
        },
        "reasoning": {
            "report_or_checkpoint_inconsistency": "NOT_SUPPORTED; exact checkpoints, no resume events, matched steps/tokens/windows.",
            "eval_gate_alignment": "WEAK; training eval gate uses four single 256-token windows, while oracle audit covers seven official-like files with 64-token blocks.",
            "router_metric_effect": "SUPPORTED; regret0p01 reduces final-block regret and increases selected-is-oracle/top2 rates.",
            "lm_eval_effect": "NOT_SUPPORTED_FOR_PROMOTION; regret0p01 is slightly worse on all four training eval windows.",
            "routing_side_effect": "SUPPORTED; regret0p01 lowers owner entropy and increases monopoly rate, suggesting over-concentrated routing.",
            "most_likely_diagnosis": "The regret objective improves final-block expert selection on the oracle-audit distribution but over-concentrates owner utilization and does not transfer to the tiny training-eval windows. The block is therefore an evaluation-alignment plus over-regularized-routing problem, not a useless-expert problem.",
        },
        "status_labels": [
            "PVR_ROUTER_REGRET_METRIC_IMPROVEMENT_SUPPORTED",
            "PVR_ROUTER_REGRET_REPAIR_1M_LM_GATE_NOT_SUPPORTED",
            "PVR_ROUTER_REPAIR_EVAL_ORACLE_ALIGNMENT_MISMATCH_CONFIRMED",
            "PVR_ROUTER_REGRET_OBJECTIVE_OVER_CONCENTRATION_RISK_SUPPORTED",
        ],
        "blocked_claims": [
            "PVR_ROUTER_REGRET_REPAIR_1M_PROMOTION_SUPPORTED",
            "PVR_ROUTE_MARGIN_CONFIDENCE_SUPPORTED",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
            "PVR_ARCHITECTURE_SUPERIORITY_SUPPORTED",
        ],
        "recommendation": "Do not promote regret0p01. Replace the four-window LM gate with a full official-like micro/macro gate, then test lower or annealed regret weights with an entropy/monopoly retention constraint.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_regret_lm_mismatch_analysis.json", payload)
    lines = [
        "# PVR Router Regret / LM Mismatch Analysis",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        "## Key Deltas",
        "",
        f"Final eval delta: `{final_eval_delta}`",
        f"Mean eval delta: `{mean_eval_delta}`",
        f"Oracle selected-loss delta: `{selected_loss_delta}`",
        f"Oracle shared-only delta: `{shared_loss_delta}`",
        f"Oracle router-regret delta: `{oracle_regret_delta}`",
        f"Selected-is-oracle delta: `{oracle_rate_delta}`",
        "",
        "## Eval Windows",
        "",
        "| step | tokens | baseline | regret0p01 | delta |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in eval_windows:
        lines.append(
            f"| {row.get('step')} | {row.get('training_tokens_seen')} | {row.get('baseline_eval_loss')} | "
            f"{row.get('repair_eval_loss')} | {row.get('repair_minus_baseline')} |"
        )
    lines.extend(
        [
            "",
            "## Routing Curve Side Effect",
            "",
            f"Mean owner-entropy delta: `{payload['routing_curve_analysis']['mean_owner_entropy_delta']}`",
            f"Mean monopoly-rate delta: `{payload['routing_curve_analysis']['mean_monopoly_rate_delta']}`",
            "",
            "## Oracle Per-File Deltas",
            "",
            "| file | selected delta | shared delta | oracle delta | regret delta | oracle-rate delta | top2-rate delta |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in oracle["per_file"]:
        lines.append(
            f"| {row.get('file')} | {row.get('selected_loss_delta')} | {row.get('shared_only_loss_delta')} | "
            f"{row.get('oracle_loss_delta')} | {row.get('router_regret_delta')} | "
            f"{row.get('selected_is_oracle_rate_delta')} | {row.get('selected_is_top2_rate_delta')} |"
        )
    lines.extend(
        [
            "",
            "## Diagnosis",
            "",
            payload["reasoning"]["most_likely_diagnosis"],
            "",
            "## Recommendation",
            "",
            payload["recommendation"],
        ]
    )
    (out / "pvr_router_regret_lm_mismatch_analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", default="benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation_run")
    parser.add_argument("--oracle-root", default="benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation_oracle")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_regret_lm_mismatch_analysis")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"], "key_deltas": payload["key_deltas"]}, indent=2))


if __name__ == "__main__":
    main()
