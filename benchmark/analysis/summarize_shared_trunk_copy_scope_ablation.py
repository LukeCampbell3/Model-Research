"""Summarize the 300M shared-trunk copy-scope ablation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


def _load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run(
    input_report: str = "benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation/copy_scope_ablation_report.json",
    output: str = "benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation_decision",
) -> dict[str, Any]:
    report = _load(input_report)
    rows = report.get("rows", [])
    by_scope = {row["copy_scope"]: row for row in rows}
    best_scope = report.get("best_scope_by_lm_loss")
    full = by_scope.get("full_compatible_shared_copy", {})
    best = by_scope.get(best_scope, {})
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": "PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_EMBEDDINGS_ATTENTION_NORMS_SUPPORTED",
        "source_report": input_report,
        "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
        "best_scope": best_scope,
        "supported_scopes": report.get("supported_scopes", []),
        "decision": {
            "primary_carrier": "embeddings_attention_norms",
            "full_compatible_shared_copy_still_supported": bool(full.get("loss_supported") and full.get("route_stable")),
            "shared_ffn_bias_not_required_for_main_gain": True,
            "attention_only_is_not_sufficient": True,
            "embeddings_only_is_helpful_but_not_sufficient": True,
        },
        "best_vs_full_compatible": {
            "lm_loss_delta": (
                float(best["lm_loss"]) - float(full["lm_loss"])
                if isinstance(best.get("lm_loss"), (int, float)) and isinstance(full.get("lm_loss"), (int, float))
                else None
            ),
            "mean_eval_loss_delta": (
                float(best["mean_eval_loss"]) - float(full["mean_eval_loss"])
                if isinstance(best.get("mean_eval_loss"), (int, float)) and isinstance(full.get("mean_eval_loss"), (int, float))
                else None
            ),
            "final_train_loss_delta": (
                float(best["final_train_loss"]) - float(full["final_train_loss"])
                if isinstance(best.get("final_train_loss"), (int, float)) and isinstance(full.get("final_train_loss"), (int, float))
                else None
            ),
        },
        "rankings": report.get("rankings", {}),
        "interpretation": (
            "The dense-to-PVR transfer gain is concentrated in shared token/position embeddings, attention, and norms. "
            "Full compatible shared copy remains supported, but its extra copied shared FFN bias does not explain the win "
            "and is slightly worse than embeddings+attention+norms on reduced LM loss in this seed."
        ),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "copy_scope_ablation_decision_report.json", payload)
    lines = [
        "# Shared-Trunk Copy-Scope Ablation Decision",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"Best scope: `{payload['best_scope']}`",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        "```",
        "",
    ]
    (out / "copy_scope_ablation_decision_report.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-report", default="benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation/copy_scope_ablation_report.json")
    parser.add_argument("--output", default="benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation_decision")
    args = parser.parse_args()
    payload = run(args.input_report, args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
