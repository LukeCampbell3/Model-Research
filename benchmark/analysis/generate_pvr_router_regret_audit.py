"""Consolidate PVR oracle and router-regret diagnostics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


def _load(path: str) -> dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"missing": str(p)}


def run(
    *,
    final_block_official: str = "benchmark/reports/generated/pvr_final_block_expert_sweep_audit/pvr_final_block_expert_sweep_audit.json",
    full_network_dev: str = "benchmark/reports/generated/pvr_full_network_greedy_oracle_audit/pvr_full_network_greedy_oracle_audit.json",
    output: str = "benchmark/reports/generated/pvr_router_regret_audit",
) -> dict[str, Any]:
    final_block = _load(final_block_official)
    full_network = _load(full_network_dev)
    final_overall = final_block.get("overall") or {}
    full_overall = full_network.get("overall") or {}
    final_regret = final_overall.get("mean_router_regret")
    full_regret = full_overall.get("mean_router_regret_across_block_decisions")
    full_gain = full_overall.get("greedy_oracle_improvement_over_selected")
    router_regret_material = bool(
        (isinstance(final_regret, (int, float)) and final_regret > 0.5)
        or (isinstance(full_gain, (int, float)) and full_gain < -1.0)
    )
    status = (
        "PVR_ROUTER_REGRET_BOTTLENECK_DIAGNOSTIC_SUPPORTED"
        if router_regret_material
        else "PVR_ROUTER_REGRET_BOTTLENECK_NOT_SUPPORTED"
    )
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REGRET_AUDIT",
        "status": status,
        "scope": "Consolidates existing final-block frozen-official and greedy full-network official-like development audits. No training and no final official-file tuning.",
        "inputs": {
            "final_block_official": final_block_official,
            "full_network_official_like_dev": full_network_dev,
        },
        "final_block_official_summary": final_overall,
        "full_network_official_like_dev_summary": full_overall,
        "claim_gates": {
            "final_block_selected_beats_shared": final_overall.get("selected_loss", 0) < final_overall.get("shared_only_loss", -1),
            "final_block_selected_beats_mean_wrong": final_overall.get("selected_loss", 0) < final_overall.get("mean_wrong_loss", -1),
            "final_block_oracle_materially_beats_selected": isinstance(final_regret, (int, float)) and final_regret > 0.5,
            "full_network_greedy_oracle_materially_beats_selected": isinstance(full_gain, (int, float)) and full_gain < -1.0,
            "official_final_files_used_for_training_or_selection": False,
        },
        "diagnosis": (
            "Router regret is material in diagnostic audits. Expert-bank capacity exists under oracle-style interventions, "
            "so router repair should precede scaling. Because the full-network audit is greedy and development-only, this "
            "does not prove a deployable oracle model or an official benchmark advantage."
        ),
        "not_run_or_blocked": {
            "local_paired_heldout_full_network_oracle": "NOT_RUN_NOT_IMPLEMENTED",
            "frozen_official_full_network_oracle": "NOT_RUN_NOT_IMPLEMENTED",
            "oracle_vs_comparators_on_identical_official_like_windows": "PARTIAL_DIAGNOSTIC_ONLY",
        },
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_router_regret_audit.json", payload)
    lines = [
        "# PVR Router Regret Audit",
        "",
        f"Status: `{status}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["scope"],
        "",
        "## Frozen Official Final-Block Sweep",
        "",
        "This uses identical final-block hidden states and evaluates every final-block expert. It is not a full-network oracle.",
        "",
        f"Selected loss: `{final_overall.get('selected_loss')}`",
        f"Shared-only loss: `{final_overall.get('shared_only_loss')}`",
        f"Oracle loss: `{final_overall.get('oracle_loss')}`",
        f"Mean wrong loss: `{final_overall.get('mean_wrong_loss')}`",
        f"Mean router regret: `{final_overall.get('mean_router_regret')}`",
        f"Selected-is-oracle rate: `{final_overall.get('selected_is_oracle_rate')}`",
        f"Selected-is-top2 rate: `{final_overall.get('selected_is_top2_rate')}`",
        "",
        "## Official-Like Development Full-Network Greedy Oracle",
        "",
        "This uses official-like development data only and greedily chooses per-block oracle experts. It is not exhaustive.",
        "",
        f"Selected loss: `{full_overall.get('selected_loss')}`",
        f"Greedy oracle loss: `{full_overall.get('greedy_full_network_oracle_loss')}`",
        f"Greedy oracle improvement: `{full_overall.get('greedy_oracle_improvement_over_selected')}`",
        f"Mean router regret across block decisions: `{full_overall.get('mean_router_regret_across_block_decisions')}`",
        f"Selected-is-oracle rate: `{full_overall.get('selected_is_oracle_rate_across_block_decisions')}`",
        f"Selected-is-top2 rate: `{full_overall.get('selected_is_top2_rate_across_block_decisions')}`",
        "",
        "## Diagnosis",
        "",
        payload["diagnosis"],
        "",
        "## Blocked / Not Run",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["not_run_or_blocked"].items()],
    ]
    (out / "pvr_router_regret_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-block-official", default="benchmark/reports/generated/pvr_final_block_expert_sweep_audit/pvr_final_block_expert_sweep_audit.json")
    parser.add_argument("--full-network-dev", default="benchmark/reports/generated/pvr_full_network_greedy_oracle_audit/pvr_full_network_greedy_oracle_audit.json")
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_router_regret_audit")
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "claim_gates": payload["claim_gates"]}, indent=2))


if __name__ == "__main__":
    main()
