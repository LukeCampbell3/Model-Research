"""Summarize the official-like router auxiliary-weight sweep."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, utc_now, write_json


def _final_routing(path: str | None) -> dict[str, Any]:
    if not path or not Path(path).exists():
        return {}
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    curve = payload.get("routing_curve") or []
    return curve[-1] if curve else {}


def _weight_from_variant(name: str) -> float:
    suffix = name.split("_aux", 1)[-1].split("_", 1)[0].replace("p", ".")
    return float(suffix)


def run(
    *,
    training_report: str = "benchmark/reports/generated/official_like_router_aux_sweep/training_run_report.json",
    output: str = "benchmark/reports/generated/official_like_router_aux_sweep_decision",
) -> dict[str, Any]:
    report = load_json_or_yaml(training_report)
    rows = []
    for row in report.get("rows", []):
        routing = _final_routing(row.get("routing_curve"))
        rows.append(
            {
                "model_variant": row.get("model_variant"),
                "routing_aux_weight": _weight_from_variant(str(row.get("model_variant"))),
                "final_loss": row.get("final_loss"),
                "optimizer_steps": row.get("optimizer_steps"),
                "training_tokens_seen": row.get("training_tokens_seen"),
                "eval_window_count": row.get("eval_window_count"),
                "owners_per_token": routing.get("owners_per_token"),
                "top2_execution_count": routing.get("top2_execution_count"),
                "owner_entropy": routing.get("owner_entropy"),
                "prototype_margin": routing.get("prototype_margin"),
                "prototype_monopoly_rate": routing.get("prototype_monopoly_rate"),
            }
        )
    ranked = sorted(rows, key=lambda item: item["final_loss"])
    winner = ranked[0] if ranked else {}
    zero = next((row for row in rows if row["routing_aux_weight"] == 0.0), {})
    current = next((row for row in rows if abs(row["routing_aux_weight"] - 0.001) < 1e-12), {})
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_OFFICIAL_LIKE_ROUTER_AUX_WEIGHT_SWEEP",
        "status": "PVR_OFFICIAL_LIKE_ROUTER_AUX_SWEEP_COMPLETE",
        "scope": "Reduced 100M official-like development screen; final official files not used.",
        "training_report": training_report,
        "rows": ranked,
        "winner": winner,
        "winner_delta_vs_zero_aux": winner.get("final_loss") - zero.get("final_loss") if winner and zero else None,
        "winner_delta_vs_current_aux": winner.get("final_loss") - current.get("final_loss") if winner and current else None,
        "claim_gates": {
            "all_models_completed": report.get("completed_model_count") == report.get("model_count"),
            "resource_reduction_none": (report.get("resource_reduction") or {}).get("status") == "NONE",
            "official_final_files_used": False,
            "strict_top1_clean_for_winner": winner.get("owners_per_token") == 1.0 and winner.get("top2_execution_count") == 0,
        },
        "caveat": "This is a short reduced screen for routing auxiliary weight selection pressure, not promotion-scale training.",
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "official_like_router_aux_sweep_report.json", payload)
    lines = [
        "# Official-Like Router Auxiliary Sweep",
        "",
        f"Status: `{payload['status']}`",
        "",
        payload["scope"],
        "",
        f"Winner: `{winner.get('model_variant')}`",
        f"Winner aux weight: `{winner.get('routing_aux_weight')}`",
        f"Winner final loss: `{winner.get('final_loss')}`",
        f"Winner delta vs zero aux: `{payload['winner_delta_vs_zero_aux']}`",
        f"Winner delta vs current aux: `{payload['winner_delta_vs_current_aux']}`",
        "",
        "## Rows",
        "",
        "| variant | aux | final loss | owner entropy | margin | monopoly |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in ranked:
        lines.append(
            f"| {row['model_variant']} | {row['routing_aux_weight']} | {row['final_loss']} | "
            f"{row['owner_entropy']} | {row['prototype_margin']} | {row['prototype_monopoly_rate']} |"
        )
    (out / "official_like_router_aux_sweep_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--training-report", default="benchmark/reports/generated/official_like_router_aux_sweep/training_run_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/official_like_router_aux_sweep_decision")
    args = parser.parse_args()
    payload = run(training_report=args.training_report, output=args.output)
    print(json.dumps({"status": payload["status"], "winner": payload["winner"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
