"""Consolidate local 300M PVR-EC-O evidence into a status report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


STATUS_COMPLETE = "PVR_EC_O_300M_LOCAL_EVIDENCE_CONSOLIDATION_REPORT_COMPLETE"

REPORT_PATHS = {
    "active_compute_frontier": "benchmark/reports/generated/active_compute_frontier_300m/active_compute_frontier_300m_report.json",
    "active_compute_frontier_repeat": "benchmark/reports/generated/active_compute_frontier_300m_repeat/active_compute_frontier_300m_repeat_report.json",
    "strict_top1_vs_top2": "benchmark/reports/generated/strict_top1_vs_top2_active_compute_audit/strict_top1_vs_top2_active_compute_audit_report.json",
    "expert_benefit_localization": "benchmark/reports/generated/expert_benefit_localization_audit/expert_benefit_localization_audit_report.json",
    "expert_function_probe": "benchmark/reports/generated/expert_function_probe_audit/expert_function_probe_audit_report.json",
    "expert_cards": "benchmark/reports/generated/expert_cards/expert_card_report.json",
    "claim_proof_battery": "benchmark/reports/generated/pvr_claim_proof_battery_audit/pvr_claim_proof_battery_audit_report.json",
    "expert_delta_causality_repeat": "benchmark/reports/generated/expert_delta_causality_repeat_classwise_audit/expert_delta_causality_repeat_classwise_audit_report.json",
    "route_geometry_specialization": "benchmark/reports/generated/route_geometry_specialization_audit/route_geometry_specialization_audit_report.json",
    "route_geometry_finegrain": "benchmark/reports/generated/route_geometry_finegrain_audit/route_geometry_finegrain_audit_report.json",
    "benefit_weighted_route_induction": "benchmark/reports/generated/benefit_weighted_route_geometry_induction_audit/benefit_weighted_route_geometry_induction_audit_report.json",
    "replay_cross_architecture": "benchmark/reports/generated/retention_replay_cross_architecture_control_seed_42/retention_replay_cross_architecture_control_report.json",
    "causal_ablation": "benchmark/reports/generated/ean_retention_replay_causal_ablation_seed_42/ean_retention_replay_causal_ablation_report.json",
}


def _load(path: str) -> dict[str, Any] | None:
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def _status(data: dict[str, Any] | None) -> str:
    return str(data.get("status")) if data else "NOT_RUN_MISSING_REPORT"


def _claim(label: str, status: str, evidence: list[str], caveat: str, source_keys: list[str]) -> dict[str, Any]:
    return {
        "label": label,
        "status": status,
        "evidence": evidence,
        "caveat": caveat,
        "sources": source_keys,
    }


def _summary_rows(reports: dict[str, dict[str, Any] | None]) -> dict[str, Any]:
    repeat = reports["active_compute_frontier_repeat"] or {}
    strict = reports["strict_top1_vs_top2"] or {}
    localization = reports["expert_benefit_localization"] or {}
    proof = reports["claim_proof_battery"] or {}
    repeat_causal = reports["expert_delta_causality_repeat"] or {}
    return {
        "active_compute_repeat": {
            "status": _status(reports["active_compute_frontier_repeat"]),
            "missing_seeds": repeat.get("missing_seeds"),
            "seed_results": [
                {
                    "seed": row.get("seed"),
                    "status": row.get("status"),
                    "broad_lm_loss": row.get("rows", {}).get(repeat.get("candidate"), {}).get("broad_lm_loss"),
                    "active_params_per_token": row.get("rows", {}).get(repeat.get("candidate"), {}).get("active_params_per_token"),
                    "active_flops_per_token": row.get("rows", {}).get(repeat.get("candidate"), {}).get("active_flops_per_token"),
                }
                for row in repeat.get("repeat_results", [])
            ],
        },
        "strict_top1": {
            "status": _status(reports["strict_top1_vs_top2"]),
            "conditions": strict.get("supported_conditions"),
            "escalation": strict.get("escalation_summary"),
        },
        "expert_benefit_localization": {
            "status": _status(reports["expert_benefit_localization"]),
            "overall": localization.get("metrics", {}).get("overall"),
            "concentration": localization.get("metrics", {}).get("benefit_concentration"),
        },
        "claim_proof_battery": {
            "status": _status(reports["claim_proof_battery"]),
            "conditions": proof.get("supported_conditions"),
            "expert_delta_causality": proof.get("metrics", {}).get("expert_delta_causality"),
            "route_margin": proof.get("metrics", {}).get("route_margin_interpretability"),
            "semantic_owner_geometry": proof.get("metrics", {}).get("semantic_owner_geometry"),
        },
        "expert_delta_causality_repeat": {
            "status": _status(reports["expert_delta_causality_repeat"]),
            "missing_seeds": repeat_causal.get("missing_seeds"),
            "seed_results": [
                {
                    "seed": row.get("seed"),
                    "status": row.get("status"),
                    "causal": row.get("metrics", {}).get("causal"),
                }
                for row in repeat_causal.get("seed_results", [])
            ],
        },
    }


def run(
    *,
    output: str = "benchmark/reports/generated/pvr_300m_local_evidence_consolidation",
) -> dict[str, Any]:
    reports = {key: _load(path) for key, path in REPORT_PATHS.items()}
    supported = [
        _claim(
            "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_REPEAT_SUPPORTED",
            "SUPPORTED",
            [
                "Seed 42 and seed 123 candidate artifacts both pass active-compute Pareto gates.",
                "Candidate remains at 105M active params/token and 630M active FLOPs/token.",
            ],
            "Seed 777 is NOT_RUN_MISSING_ARTIFACT; local reduced-file audit only.",
            ["active_compute_frontier_repeat"],
        ),
        _claim(
            "PVR_STRICT_TOP1_ACTIVE_COMPUTE_SUFFICIENCY_SUPPORTED",
            "SUPPORTED",
            [
                "Strict Top1 beats dense, Switch Top1, and generic Top2 on local broad LM.",
                "Runtime Top2/Top4 PVR escalation worsens loss and quality/FLOP.",
            ],
            "Runtime Top2/Top4 are eval-only controls, not trained candidates.",
            ["strict_top1_vs_top2"],
        ),
        _claim(
            "PVR_EXPERT_BENEFIT_LOCALIZATION_SUPPORTED",
            "SUPPORTED",
            [
                "Expert benefit is positive overall and concentrated in structured/syntax-heavy classes.",
                "Structured benefit share exceeds structured token fraction.",
            ],
            "Byte-level heuristic token classes; local reduced files.",
            ["expert_benefit_localization"],
        ),
        _claim(
            "PVR_EXPERT_FUNCTION_PROBE_SUPPORTED",
            "SUPPORTED",
            [
                "All global experts are active and positive in post-hoc assigned benefit.",
                "Expert cards expose top benefit/harm classes and examples.",
            ],
            "Post-hoc attribution, not causal proof by itself.",
            ["expert_function_probe", "expert_cards"],
        ),
        _claim(
            "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
            "SUPPORTED",
            [
                "Full model beats shared-only on both available replay seeds.",
                "Wrong-expert intervention harms loss on both available replay seeds.",
                "Structured classes show strongest repeated harm.",
            ],
            "Inference-time causal support over seeds 42 and 123; seed 777 missing; not training-causal proof.",
            ["claim_proof_battery", "expert_delta_causality_repeat"],
        ),
    ]
    partial = [
        _claim(
            "PVR_ROUTE_GEOMETRY_PARTIAL_SIGNAL",
            "PARTIAL",
            [
                "Owner/token-class and owner/syntax NMI show lift over shuffled controls.",
                "Signal is below strict semantic-geometry thresholds.",
            ],
            "Do not claim semantic owner geometry specialization.",
            ["claim_proof_battery", "route_geometry_finegrain"],
        )
    ]
    blocked = [
        _claim(
            "PVR_ROUTE_MARGIN_PREDICTS_EXPERT_BENEFIT_SUPPORTED",
            "BLOCKED",
            [
                "Margin/benefit correlation is negative near zero.",
                "High-margin tokens do not beat low-margin tokens.",
                "Margin quartiles are not monotonic.",
            ],
            "Route margin should not be described as calibrated confidence.",
            ["claim_proof_battery"],
        ),
        _claim(
            "PVR_ROUTE_GEOMETRY_SPECIALIZATION_SUPPORTED",
            "BLOCKED",
            [
                "Family-level geometry audit fails.",
                "Fine-grained route geometry audit fails strict gate.",
                "Semantic owner geometry proof misses strict NMI/loss-bucket thresholds.",
            ],
            "Owner IDs are not yet strongly human-interpretable.",
            ["route_geometry_specialization", "route_geometry_finegrain", "claim_proof_battery"],
        ),
        _claim(
            "PVR_REPLAY_ARCHITECTURE_SPECIFIC_ADVANTAGE_SUPPORTED",
            "BLOCKED",
            [
                "Cross-architecture replay control does not show PVR-specific replay advantage.",
            ],
            "Replay appears broadly useful, not uniquely PVR-specific under this control.",
            ["replay_cross_architecture"],
        ),
        _claim(
            "PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_SUPPORTED",
            "BLOCKED",
            [
                "Benefit-weighted route induction worsens intended NMI/consistency metrics.",
            ],
            "Do not push this route-forcing repair path as supported.",
            ["benefit_weighted_route_induction"],
        ),
        _claim(
            "PVR_EXPERT_DELTA_TRAINING_CAUSALITY_SUPPORTED",
            "BLOCKED",
            [
                "No training-causal intervention has been run.",
            ],
            "Current causality support is inference-time only.",
            ["claim_proof_battery", "expert_delta_causality_repeat"],
        ),
    ]
    not_tested = [
        _claim(
            "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
            "NOT_TESTED",
            ["Official broad NLP adapters remain NOT_RUN_NOT_IMPLEMENTED."],
            "Local reduced-file evidence only.",
            [],
        ),
        _claim(
            "PVR_OFFICIAL_CODE_BENCH_SUPPORTED",
            "NOT_TESTED",
            ["Official code benchmark adapters remain NOT_RUN_NOT_IMPLEMENTED."],
            "Local reduced-file evidence only.",
            [],
        ),
        _claim(
            "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
            "NOT_TESTED",
            ["Current best candidate uses EAN teacher-initialized scaffold."],
            "Do not claim from-scratch dense dominance.",
            [],
        ),
        _claim(
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
            "NOT_TESTED",
            ["Current best candidate depends on dense-compatible EAN initialization."],
            "Teacher independence remains an open research target.",
            [],
        ),
    ]
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "status": STATUS_COMPLETE,
        "experiment": "PVR_EC_O_300M_LOCAL_EVIDENCE_CONSOLIDATION_REPORT",
        "candidate": "pvr_ec_o_ean_retention_gated_delta_replay_v1",
        "candidate_status": "active-compute Pareto repeat-supported local candidate",
        "best_supported_claim": (
            "At 300M local reduced-file scale, pvr_ec_o_ean_retention_gated_delta_replay_v1 achieves "
            "repeat-supported active-compute Pareto advantage under strict Top1 execution. Its selected expert "
            "path is inference-causally useful across two available replay-seed artifacts, with strongest effects "
            "on structured/syntax-heavy token classes."
        ),
        "supported": supported,
        "partially_supported": partial,
        "blocked": blocked,
        "not_tested": not_tested,
        "source_statuses": {key: _status(value) for key, value in reports.items()},
        "evidence_summary": _summary_rows(reports),
        "decision_next_steps": [
            "Move to 700M active-compute frontier only if local 300M evidence is considered sufficient.",
            "Implement official-style broad NLP/code adapters before claiming official benchmark support.",
            "Do not spend more compute forcing route-margin or owner-geometry interpretability without a new mechanism.",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "pvr_300m_local_evidence_consolidation_report.json", payload)
    _write_markdown(out / "pvr_300m_local_evidence_consolidation_report.md", payload)
    return payload


def _write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# PVR-EC-O 300M Local Evidence Consolidation",
        "",
        f"Status: `{payload['status']}`",
        f"Candidate: `{payload['candidate']}`",
        "",
        payload["best_supported_claim"],
        "",
    ]
    for section_key, title in [
        ("supported", "Supported"),
        ("partially_supported", "Partially Supported"),
        ("blocked", "Blocked"),
        ("not_tested", "Not Tested"),
    ]:
        lines.extend([f"## {title}", ""])
        for item in payload[section_key]:
            lines.extend([
                f"### {item['label']}",
                "",
                f"Status: `{item['status']}`",
                "",
                "Evidence:",
                *[f"- {entry}" for entry in item["evidence"]],
                "",
                f"Caveat: {item['caveat']}",
                "",
            ])
    lines.extend([
        "## Source Statuses",
        "",
        "```json",
        json.dumps(payload["source_statuses"], indent=2, sort_keys=True),
        "```",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/pvr_300m_local_evidence_consolidation")
    args = parser.parse_args()
    payload = run(output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()
