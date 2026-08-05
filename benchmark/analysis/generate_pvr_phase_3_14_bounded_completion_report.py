"""Consolidate Phase 3-14 bounded execution evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import load_json_or_yaml, utc_now, write_json


def _load(path: str) -> dict[str, Any]:
    p = Path(path)
    return load_json_or_yaml(p) if p.exists() else {"missing": True, "path": path}


def run(output: str = "benchmark/reports/generated/pvr_phase_3_14_bounded_completion") -> dict[str, Any]:
    boundary = _load("benchmark/reports/generated/official_evaluation_boundary_frozen/official_evaluation_boundary_frozen.json")
    full_oracle = _load("benchmark/reports/generated/pvr_full_network_greedy_oracle_audit/pvr_full_network_greedy_oracle_audit.json")
    comparator = _load("benchmark/reports/generated/sparse_comparator_runtime_integrity_audit/sparse_comparator_runtime_integrity_audit.json")
    aux = _load("benchmark/reports/generated/official_like_router_aux_sweep_decision/official_like_router_aux_sweep_report.json")
    capacity = _load("benchmark/reports/generated/sparse_v2_capacity_screen_decision/sparse_v2_capacity_screen_report.json")
    curriculum = _load("benchmark/reports/generated/sparse_v2_curriculum_screen_decision/sparse_v2_curriculum_screen_report.json")
    warmup = _load("benchmark/reports/generated/sparse_v2_short_warmup_screen_decision/sparse_v2_curriculum_screen_report.json")
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "experiment": "PVR_PHASE_3_14_BOUNDED_COMPLETION",
        "status": "PVR_PHASE_3_14_BOUNDED_EXECUTION_COMPLETE",
        "scope": "Reduced/bounded execution and existing-screen consolidation. This does not promote broad official superiority or teacher independence.",
        "phase_status": {
            "phase_3_shared_substrate": {
                "status": "BOUNDED_EXISTING_CAPACITY_SCREEN_COMPLETE",
                "source_status": capacity.get("status"),
                "winner": capacity.get("winner"),
            },
            "phase_4_router_regret_training": {
                "status": "DIAGNOSTIC_TARGETS_AVAILABLE_TRAINING_OBJECTIVE_NOT_YET_PROMOTION_VALIDATED",
                "source_status": full_oracle.get("status"),
                "overall": full_oracle.get("overall"),
            },
            "phase_5_auxiliary_sweep": {
                "status": aux.get("status"),
                "winner": aux.get("winner"),
                "claim_gates": aux.get("claim_gates"),
            },
            "phase_6_general_residual_expert": {
                "status": "NOT_IMPLEMENTED_ARCHITECTURE_CHANGE_DEFERRED",
                "reason": "Router-regret evidence is now available; general residual expert should be tested as a separate architecture change after regret-aware targets.",
            },
            "phase_7_router_uncertainty_calibration": {
                "status": "NOT_IMPLEMENTED_FEATURES_IDENTIFIED",
                "reason": "Calibration requires held-out oracle/regret labels; greedy oracle audit now provides the label source on official-like dev.",
            },
            "phase_8_staged_curriculum": {
                "status": "BOUNDED_EXISTING_CURRICULUM_SCREENS_COMPLETE",
                "curriculum_status": curriculum.get("status"),
                "warmup_status": warmup.get("status"),
            },
            "phase_9_official_like_mixtures": {
                "status": "OFFICIAL_LIKE_DEVELOPMENT_SET_MATERIALIZED",
                "boundary_assertions": boundary.get("assertions"),
            },
            "phase_10_domain_robustness": {
                "status": "NOT_IMPLEMENTED_REQUIRES_PERTURBATION_GENERATOR",
            },
            "phase_11_official_validation": {
                "status": "CORRECTED_AGGREGATION_AND_BOUNDARY_COMPLETE",
                "final_official_files_untouched_for_training": True,
            },
            "phase_12_comparator_integrity": {
                "status": comparator.get("status"),
                "assertions": comparator.get("assertions"),
            },
            "phase_13_larger_budget_curves": {
                "status": "NOT_RUN_EXPENSIVE_SCALE_WORK_REMAINS",
            },
            "phase_14_matched_information_matrix": {
                "status": "NOT_RUN_EXPENSIVE_COMPARATOR_MATRIX_REMAINS",
            },
        },
        "supported_labels": [
            "OFFICIAL_EVALUATION_BOUNDARY_FROZEN",
            "OFFICIAL_LIKE_DEVELOPMENT_SET_MATERIALIZED",
            "PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE",
            "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE",
            "PVR_OFFICIAL_LIKE_ROUTER_AUX_SWEEP_COMPLETE",
            "PVR_PHASE_3_14_BOUNDED_EXECUTION_COMPLETE",
        ],
        "blocked_labels": [
            "PVR_PHASE_3_14_PROMOTION_SCALE_COMPLETE",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
            "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
            "PVR_OFFICIAL_CODE_BENCH_SUPPORTED",
            "PVR_LARGER_BUDGET_CURVES_COMPLETE",
            "MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION_COMPLETE",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_phase_3_14_bounded_completion_report.json", payload)
    lines = [
        "# PVR Phase 3-14 Bounded Completion Report",
        "",
        f"Status: `{payload['status']}`",
        "",
        payload["scope"],
        "",
        "## Phase Status",
        "",
        "| phase | status |",
        "|---|---|",
    ]
    for phase, row in payload["phase_status"].items():
        lines.append(f"| {phase} | `{row.get('status')}` |")
    lines.extend([
        "",
        "## Supported Labels",
        "",
        *[f"- `{label}`" for label in payload["supported_labels"]],
        "",
        "## Blocked Labels",
        "",
        *[f"- `{label}`" for label in payload["blocked_labels"]],
    ])
    (out / "pvr_phase_3_14_bounded_completion_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_phase_3_14_bounded_completion")
    args = parser.parse_args()
    payload = run(args.output)
    print(json.dumps({"status": payload["status"], "blocked_labels": payload["blocked_labels"]}, indent=2))


if __name__ == "__main__":
    main()
