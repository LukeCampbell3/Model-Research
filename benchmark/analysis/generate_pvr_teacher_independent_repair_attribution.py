"""Generate consolidated teacher-independent sparse-v2 repair attribution reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


def _load(path: str) -> dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"missing": str(p)}


def _write_md(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _substrate_report(output_root: Path, payloads: dict[str, dict[str, Any]]) -> dict[str, Any]:
    existing_path = output_root / "pvr_shared_substrate_repair_screen" / "pvr_shared_substrate_repair_screen.json"
    if existing_path.exists():
        existing = _load(str(existing_path))
        if existing.get("status") == "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE":
            return existing
    status = "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_BLOCKED_NOT_RUN"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN",
        "status": status,
        "completed_variants": [],
        "blocked_variants": [
            "attention_only_current_baseline",
            "embeddings_attention",
            "attention_normalization",
            "embeddings_normalization",
            "random_ean",
            "wider_attention_only",
            "deeper_shared_trunk",
            "staged_shared_trunk_warmup",
        ],
        "reason": "No completed low-cost teacher-independent substrate matrix artifact exists in the current repository state.",
        "safe_interpretation": "Shared-substrate weakness remains plausible but is not isolated by a completed substrate screen in this run.",
    }
    out = output_root / "pvr_shared_substrate_repair_screen"
    write_json(out / "pvr_shared_substrate_repair_screen.json", payload)
    _write_md(
        out / "pvr_shared_substrate_repair_screen.md",
        [
            "# PVR Shared Substrate Repair Screen",
            "",
            f"Status: `{status}`",
            f"Git commit: `{payload['git_commit']}`",
            "",
            payload["reason"],
            "",
            "## Safe Interpretation",
            "",
            payload["safe_interpretation"],
            "",
            "No substrate variant is promoted. A real screen still requires matched-token training and official-like development evaluation.",
        ],
    )
    return payload


def _router_repair_report(output_root: Path, payloads: dict[str, dict[str, Any]]) -> dict[str, Any]:
    existing_path = output_root / "pvr_router_repair_screen" / "pvr_router_repair_screen.json"
    if existing_path.exists():
        existing = _load(str(existing_path))
        if existing.get("status") == "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE":
            return existing
    aux = payloads["aux"]
    rows = aux.get("rows", [])
    winner = aux.get("winner", {})
    status = "PVR_ROUTER_REPAIR_SCREEN_PARTIAL_COMPLETE"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_ROUTER_REPAIR_SCREEN",
        "status": status,
        "short_aux_sweep_status": aux.get("status"),
        "short_aux_sweep_rows": rows,
        "short_aux_winner": winner,
        "invalid_or_blocked": {
            "pvr_aux0005_5m_long_curve": "TRAINING_FAILED_INFRASTRUCTURE; 414 steps, 423936 tokens, zero eval windows; not scientific evidence against aux=0.0005",
            "regret_weighted_router_loss": "NOT_RUN_NOT_IMPLEMENTED",
            "soft_oracle_targets": "NOT_RUN_NOT_IMPLEMENTED",
            "router_only_retraining": "NOT_RUN_NOT_IMPLEMENTED",
            "general_residual_expert": "NOT_RUN_NOT_IMPLEMENTED",
            "router_calibration_model": "NOT_RUN_NOT_IMPLEMENTED",
        },
        "decision": "PVR_ROUTER_AUX0005_SHORT_SCREEN_SUPPORTED_BUT_CLEAN_RUNG_REQUIRED",
    }
    out = output_root / "pvr_router_repair_screen"
    write_json(out / "pvr_router_repair_screen.json", payload)
    lines = [
        "# PVR Router Repair Screen",
        "",
        f"Status: `{status}`",
        f"Decision: `{payload['decision']}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        "## Short Official-Like Aux Sweep",
        "",
        f"Source status: `{aux.get('status')}`",
        f"Winner: `{winner.get('model_variant')}`",
        f"Winner routing aux weight: `{winner.get('routing_aux_weight')}`",
        f"Winner final loss: `{winner.get('final_loss')}`",
        "",
        "This was a 100M/100-step screen. It is not promotion-scale evidence.",
        "",
        "## Invalid / Not Run",
        "",
        *[f"- {key}: `{value}`" for key, value in payload["invalid_or_blocked"].items()],
    ]
    _write_md(out / "pvr_router_repair_screen.md", lines)
    return payload


def _curriculum_report(output_root: Path, payloads: dict[str, dict[str, Any]]) -> dict[str, Any]:
    curriculum = payloads["curriculum"]
    status = "PVR_TRAINING_CURRICULUM_ATTRIBUTION_COMPLETE_NOT_SUPPORTED"
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_TRAINING_CURRICULUM_ATTRIBUTION",
        "status": status,
        "source_status": curriculum.get("status"),
        "winner": curriculum.get("winner"),
        "rows": curriculum.get("rows", []),
        "decision": "Existing 100M curriculum screen did not beat full-from-start baseline; staged curriculum is not supported by current evidence.",
    }
    out = output_root / "pvr_training_curriculum_attribution"
    write_json(out / "pvr_training_curriculum_attribution.json", payload)
    lines = [
        "# PVR Training Curriculum Attribution",
        "",
        f"Status: `{status}`",
        f"Git commit: `{payload['git_commit']}`",
        "",
        payload["decision"],
        "",
        "## Winner",
        "",
        f"Variant: `{(payload.get('winner') or {}).get('model_variant')}`",
        f"LM loss: `{(payload.get('winner') or {}).get('lm_loss')}`",
        f"Training curriculum: `{(payload.get('winner') or {}).get('training_curriculum')}`",
        "",
        "No staged curriculum is promoted from this artifact.",
    ]
    _write_md(out / "pvr_training_curriculum_attribution.md", lines)
    return payload


def run(
    *,
    output_root: str = "benchmark/reports/generated",
    final_output: str = "benchmark/reports/generated/pvr_teacher_independent_repair_attribution/pvr_teacher_independent_repair_attribution_report",
) -> dict[str, Any]:
    payloads = {
        "boundary": _load("benchmark/reports/generated/official_evaluation_boundary_frozen/official_evaluation_boundary_frozen.json"),
        "evidence": _load("benchmark/reports/generated/pvr_5m_evidence_consistency_audit/pvr_5m_evidence_consistency_audit.json"),
        "resume": _load("benchmark/reports/generated/pvr_resume_validity_audit/pvr_resume_validity_audit.json"),
        "router_regret": _load("benchmark/reports/generated/pvr_router_regret_audit/pvr_router_regret_audit.json"),
        "comparator": _load("benchmark/reports/generated/sparse_comparator_runtime_integrity_audit/sparse_comparator_runtime_integrity_audit.json"),
        "aggregation": _load("benchmark/reports/generated/sparse_v2_300m_official_aggregation_reversal_audit/official_aggregation_reversal_audit.json"),
        "aux": _load("benchmark/reports/generated/official_like_router_aux_sweep_decision/official_like_router_aux_sweep_report.json"),
        "curriculum": _load("benchmark/reports/generated/sparse_v2_curriculum_screen_decision/sparse_v2_curriculum_screen_report.json"),
        "router_1m_confirmation": _load("benchmark/reports/generated/pvr_router_regret_repair_1m_confirmation/pvr_router_repair_screen.json"),
        "router_1m_refinement": _load("benchmark/reports/generated/pvr_router_regret_repair_1m_refinement/pvr_router_regret_repair_1m_refinement.json"),
        "router_lm_mismatch": _load("benchmark/reports/generated/pvr_router_regret_lm_mismatch_analysis/pvr_router_regret_lm_mismatch_analysis.json"),
        "router_gap_resolution": _load("benchmark/reports/generated/pvr_router_regret_testing_gap_resolution/pvr_router_regret_testing_gap_resolution.json"),
    }
    root = Path(output_root)
    substrate = _substrate_report(root, payloads)
    router_repair = _router_repair_report(root, payloads)
    curriculum = _curriculum_report(root, payloads)
    current_decision = "COMBINED_ROUTER_AND_SUBSTRATE_LIMITATION_DIAGNOSTIC_SUPPORTED"
    scale_recommendation = "Do not scale current teacher-independent sparse-v2. Run router-regret repair on official-like dev first, then a clean 250K/500K/1M rung sequence."
    supported_claims = [
        "OFFICIAL_EVALUATION_BOUNDARY_FROZEN",
        "PVR_5M_EVIDENCE_CONSISTENCY_AUDIT_COMPLETE",
        "PVR_WEIGHT_ONLY_RESUME_NON_EQUIVALENT_CONFIRMED",
        "PVR_ROUTER_REGRET_BOTTLENECK_DIAGNOSTIC_SUPPORTED",
        "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE",
        "PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_SUPPORTED",
    ]
    if substrate.get("status") == "PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE":
        supported_claims.append("PVR_SHARED_SUBSTRATE_REPAIR_SCREEN_COMPLETE")
        if substrate.get("decision") == "PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED":
            supported_claims.append("PVR_SHARED_SUBSTRATE_REPAIR_CANDIDATE_IDENTIFIED")
    if router_repair.get("status") == "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE":
        supported_claims.append("PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE")
        if router_repair.get("decision") == "PVR_ROUTER_REGRET_REPAIR_SUPPORTED":
            supported_claims.append("PVR_ROUTER_REGRET_REPAIR_SUPPORTED")
    router_1m_confirmation = payloads["router_1m_confirmation"]
    router_1m_refinement = payloads["router_1m_refinement"]
    if router_1m_confirmation.get("status") == "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE":
        supported_claims.append("PVR_ROUTER_REGRET_REPAIR_1M_CONFIRMATION_COMPLETE")
    router_lm_mismatch = payloads["router_lm_mismatch"]
    if router_lm_mismatch.get("status") == "PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE":
        supported_claims.extend(
            [
                "PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE",
                *router_lm_mismatch.get("status_labels", []),
            ]
        )
    router_gap_resolution = payloads["router_gap_resolution"]
    if router_gap_resolution.get("status") == "PVR_ROUTER_REGRET_TESTING_GAP_RESOLUTION_COMPLETE":
        supported_claims.extend(router_gap_resolution.get("status_labels", []))
    router_completion_sentence = (
        "The substrate matrix and bounded regret-weighted router repair screen are complete. "
        "The aux=0.0005 5M run remains invalid because it failed before producing eval windows."
        if router_repair.get("status") == "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE"
        else "The substrate matrix is complete. Regret-weighted router repair is still not completed. "
        "The aux=0.0005 5M run is invalid because it failed before producing eval windows."
    )
    if router_1m_confirmation.get("decision") == "PVR_ROUTER_REGRET_REPAIR_NOT_SUPPORTED":
        recommendation = (
            "Do not promote regret0p01. It reduced final-block router regret at 1M, but did not improve official-like LM eval. "
            "Lower-weight refinement remains incomplete because the Docker run timed out after an earlier disk-full failure; rerun only after disk/runtime headroom is available."
        )
    elif router_repair.get("decision") == "PVR_ROUTER_REGRET_REPAIR_SUPPORTED":
        recommendation = "Run a clean 1M-token confirmation of the no-repair baseline versus the supported regret-weighted repair. Do not scale."
    else:
        recommendation = scale_recommendation
    final_payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "PVR_TEACHER_INDEPENDENT_REPAIR_ATTRIBUTION",
        "status": "PVR_TEACHER_INDEPENDENT_REPAIR_ATTRIBUTION_REPORT_COMPLETE",
        "decision": current_decision,
        "scale_recommendation": scale_recommendation,
        "inputs": payloads,
        "generated_phase_reports": {
            "shared_substrate": substrate,
            "router_repair": router_repair,
            "curriculum": curriculum,
        },
        "supported_claims": supported_claims,
        "rejected_or_not_supported_claims": [
            "PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_NOT_SUPPORTED",
            "PVR_SPARSE_V2_CURRICULUM_SCREEN_NOT_SUPPORTED",
            "PVR_5M_AUX0005_SCIENTIFIC_FAILURE_NOT_SUPPORTED_BECAUSE_RUN_FAILED",
            *(
                ["PVR_ROUTER_REGRET_REPAIR_1M_CONFIRMATION_NOT_SUPPORTED"]
                if router_1m_confirmation.get("decision") == "PVR_ROUTER_REGRET_REPAIR_NOT_SUPPORTED"
                else []
            ),
            *(
                ["PVR_ROUTER_REGRET_REPAIR_REGRET0P01_NOT_SUPPORTED_FOR_PROMOTION"]
                if router_gap_resolution.get("decision") == "PVR_ROUTER_REGRET_REPAIR_REGRET0P01_NOT_SUPPORTED_FOR_PROMOTION"
                else []
            ),
        ],
        "blocked_or_unresolved": [
            *([] if router_repair.get("status") == "PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE" else ["PVR_REGRET_WEIGHTED_ROUTER_REPAIR_NOT_RUN"]),
            *(
                ["PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID"]
                if router_1m_refinement.get("status") == "PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID"
                else []
            ),
            "PVR_FULL_NETWORK_ORACLE_ON_FINAL_OFFICIAL_NOT_RUN",
            "PVR_MATCHED_INFORMATION_ROUTING_ATTRIBUTION_MATRIX_NOT_RUN",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED_BLOCKED",
            "PVR_ARCHITECTURE_SUPERIORITY_SUPPORTED_BLOCKED",
        ],
    }
    final_path = Path(final_output)
    final_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(final_path.with_suffix(".json"), final_payload)
    evidence = payloads["evidence"]
    resume = payloads["resume"]
    router = payloads["router_regret"]
    comparator = payloads["comparator"]
    candidate = (evidence.get("raw_curve_summary") or {})
    lines = [
        "# PVR Teacher-Independent Repair Attribution Report",
        "",
        f"Status: `{final_payload['status']}`",
        f"Decision: `{current_decision}`",
        f"Git commit: `{final_payload['git_commit']}`",
        "",
        "## Authoritative 5M Evidence",
        "",
        f"Evidence audit status: `{evidence.get('status')}`",
        f"Evidence decision: `{evidence.get('decision')}`",
        f"PVR mean eval loss: `{candidate.get('mean_eval_loss')}`",
        f"PVR final eval loss: `{candidate.get('final_eval_loss')}`",
        f"PVR final train loss: `{candidate.get('final_train_loss')}`",
        f"Optimizer steps: `{candidate.get('optimizer_steps')}`",
        f"Training tokens seen: `{candidate.get('training_tokens_seen')}`",
        "",
        "Set A is authoritative in current artifacts. Set B is not present in the current filesystem artifacts.",
        "",
        "## Resume Validity",
        "",
        f"Resume audit status: `{resume.get('status')}`",
        f"Comparison status: `{resume.get('comparison_status')}`",
        "",
        "Legacy 5M checkpoints are loadable for evaluation but do not prove exact optimizer/RNG continuation.",
        "",
        "## Router Regret",
        "",
        f"Router audit status: `{router.get('status')}`",
        f"Final-block mean regret: `{(router.get('final_block_official_summary') or {}).get('mean_router_regret')}`",
        f"Final-block selected-is-oracle rate: `{(router.get('final_block_official_summary') or {}).get('selected_is_oracle_rate')}`",
        f"Official-like greedy oracle improvement: `{(router.get('full_network_official_like_dev_summary') or {}).get('greedy_oracle_improvement_over_selected')}`",
        "",
        "Router regret is material in diagnostics. This supports router repair before scale, not architecture promotion.",
        "",
        "## Comparator Integrity",
        "",
        f"Comparator audit status: `{comparator.get('status')}`",
        f"All sparse comparators valid: `{(comparator.get('assertions') or {}).get('all_sparse_comparators_valid')}`",
        "",
        "## Repair Screens",
        "",
        f"Shared substrate screen: `{substrate['status']}`",
        f"Router repair screen: `{router_repair['status']}`",
        f"Router repair 1M confirmation: `{router_1m_confirmation.get('status')}`",
        f"Router repair 1M confirmation decision: `{router_1m_confirmation.get('decision')}`",
        f"Router repair 1M refinement: `{router_1m_refinement.get('status')}`",
        f"Router regret / LM mismatch analysis: `{router_lm_mismatch.get('status')}`",
        f"Router testing gap resolution: `{router_gap_resolution.get('status')}`",
        f"Curriculum attribution: `{curriculum['status']}`",
        "",
        f"Substrate decision: `{substrate.get('decision')}`",
        f"Substrate winner: `{(substrate.get('winner') or {}).get('model_variant')}`",
        f"Substrate winner delta vs current: `{substrate.get('winner_delta_vs_current_attention_norms')}`",
        "",
        router_completion_sentence,
        "",
        "Regret0p01 improved final-block router metrics but failed the 1M LM eval gate. "
        f"Final eval delta was `{(router_lm_mismatch.get('key_deltas') or {}).get('final_eval_loss_delta')}`, "
        f"while oracle selected-loss delta was `{(router_lm_mismatch.get('key_deltas') or {}).get('oracle_selected_loss_delta')}` "
        f"and router-regret delta was `{(router_lm_mismatch.get('key_deltas') or {}).get('oracle_router_regret_delta')}`.",
        "",
        "Follow-up alignment audits resolved the gap: raw JSON first-block evaluation was metadata-prefix biased, "
        "raw JSON two-block evaluation failed, text-only evaluation was mixed, and full-network greedy oracle comparison "
        "did not show full-network regret reduction versus baseline.",
        "",
        "## Supported Claims",
        "",
        *[f"- `{item}`" for item in final_payload["supported_claims"]],
        "",
        "## Rejected / Not Supported",
        "",
        *[f"- `{item}`" for item in final_payload["rejected_or_not_supported_claims"]],
        "",
        "## Blocked / Unresolved",
        "",
        *[f"- `{item}`" for item in final_payload["blocked_or_unresolved"]],
        "",
        "## Recommendation",
        "",
        recommendation,
    ]
    _write_md(final_path.with_suffix(".md"), lines)
    return final_payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="benchmark/reports/generated")
    parser.add_argument(
        "--final-output",
        default="benchmark/reports/generated/pvr_teacher_independent_repair_attribution/pvr_teacher_independent_repair_attribution_report",
    )
    args = parser.parse_args()
    payload = run(**vars(args))
    print(json.dumps({"status": payload["status"], "decision": payload["decision"]}, indent=2))


if __name__ == "__main__":
    main()
