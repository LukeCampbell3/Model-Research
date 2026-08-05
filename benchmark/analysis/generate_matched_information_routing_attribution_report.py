"""Consolidate the current matched-information routing-attribution evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark.common import git_commit, utc_now, write_json


CANDIDATE = "pvr_teacher_independent_sparse_v2_300m"
BASELINES = [
    "dense_sparse_v2_300m_matched",
    "switch_top1_sparse_v2_300m_matched",
    "generic_top2_sparse_v2_300m_matched",
]


def _wilson_ci(successes: int, n: int, z: float = 1.959963984540054) -> list[float] | None:
    if n <= 0:
        return None
    p = successes / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / denom
    return [max(0.0, center - margin), min(1.0, center + margin)]


def _load(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {"missing": True, "path": str(p)}
    return json.loads(p.read_text(encoding="utf-8"))


def _training_rows(root: Path) -> dict[str, Any]:
    rows = {}
    for variant in [*BASELINES, CANDIDATE]:
        manifest = _load(root / variant / "checkpoint_manifest.json")
        rows[variant] = {
            "status": manifest.get("status"),
            "checkpoint_path": manifest.get("checkpoint_path"),
            "checkpoint_exists": Path(str(manifest.get("checkpoint_path", ""))).exists(),
            "optimizer_steps": manifest.get("optimizer_steps"),
            "training_tokens_seen": manifest.get("training_tokens_seen"),
            "effective_batch_tokens": manifest.get("effective_batch_tokens"),
            "eval_window_count": manifest.get("eval_window_count"),
            "resource_reduction": manifest.get("resource_reduction", {}).get("status"),
        }
    return rows


def _official_rows(root: Path) -> dict[str, Any]:
    rows = {}
    for variant in [*BASELINES, CANDIDATE]:
        nlp = _load(root / "scorecards" / variant / "nlp_scorecard.json")
        code = _load(root / "scorecards" / variant / "coding_scorecard.json")
        routing = _load(root / "routing_diagnostics" / f"{variant}.json")
        nlp_score = nlp.get("scorecard", {})
        code_score = code.get("scorecard", {})
        route_score = routing.get("scorecard", {})
        rows[variant] = {
            "merged_status": _load(root / "scorecards" / variant / "merged_scorecard.json").get("status"),
            "benchmark_evidence": _load(root / "scorecards" / variant / "merged_scorecard.json").get("benchmark_evidence"),
            "lm_loss": nlp_score.get("lm_loss"),
            "code_token_loss": nlp_score.get("code_token_loss"),
            "json_token_loss": nlp_score.get("json_token_loss"),
            "math_token_loss": nlp_score.get("math_token_loss"),
            "eval_token_count": nlp_score.get("eval_token_count"),
            "compile_rate": code_score.get("compile_rate"),
            "code_sample_count": code_score.get("humaneval_base_reduced_sample_count"),
            "routing_status": routing.get("status"),
            "owners_per_token": route_score.get("owners_per_token"),
            "top2_execution_count": route_score.get("top2_execution_count"),
            "top4_execution_count": route_score.get("top4_execution_count"),
        }
    return rows


def _comparator_integrity(config_root: str = "benchmark/configs/generated/sparse_v2_300m_confirmation/configs") -> dict[str, Any]:
    rows = {}
    for variant in [*BASELINES, CANDIDATE]:
        config = _load(Path(config_root) / f"{variant}.yaml")
        family = config.get("model_family")
        rows[variant] = {
            "model_family": family,
            "configured_experts_active_per_token": config.get("experts_active_per_token"),
            "strict_pvr_invariants_applicable": family == "pvr_ec_o",
            "declared_top1_comparator": config.get("experts_active_per_token") == 1,
            "dynamic_topk_execution_audited": family == "pvr_ec_o",
            "capacity_overflow_audited": False,
            "fallback_expert_use_audited": False,
            "routing_map_mutation_audited": family == "pvr_ec_o",
            "note": (
                "Strict PVR Top1 invariants apply to PVR only. Switch Top1 validity is represented by its configured experts_active_per_token=1 here; "
                "runtime dispatch counters for Switch capacity overflow/fallback are not implemented in this audit."
                if family != "pvr_ec_o"
                else "PVR routing diagnostics validate owners_per_token and no Top2/Top4/runtime dynamic execution."
            ),
        }
    return rows


def _rank(rows: dict[str, Any], key: str) -> list[dict[str, Any]]:
    sortable = [
        {"variant": variant, key: row.get(key)}
        for variant, row in rows.items()
        if isinstance(row.get(key), (int, float))
    ]
    return sorted(sortable, key=lambda row: row[key])


def build(
    *,
    training_root: str = "benchmark/reports/generated/sparse_v2_300m_confirmation",
    paired_report: str = "benchmark/reports/generated/sparse_v2_300m_local_significance/paired_lm_significance_report.json",
    official_root: str = "benchmark/reports/generated/sparse_v2_300m_official_bounded_benchmark",
    official_paired_report: str = "benchmark/reports/generated/sparse_v2_300m_official_bounded_paired_significance/official_bounded_paired_lm_significance_report.json",
    aggregation_audit_report: str = "benchmark/reports/generated/sparse_v2_300m_official_aggregation_reversal_audit/official_aggregation_reversal_audit.json",
    decomposition_audit_report: str = "benchmark/reports/generated/pvr_official_decomposition_audit/pvr_official_decomposition_audit.json",
    final_block_expert_sweep_report: str = "benchmark/reports/generated/pvr_final_block_expert_sweep_audit/pvr_final_block_expert_sweep_audit.json",
    boundary_report: str = "benchmark/reports/generated/official_evaluation_boundary_frozen/official_evaluation_boundary_frozen.json",
    full_network_greedy_oracle_report: str = "benchmark/reports/generated/pvr_full_network_greedy_oracle_audit/pvr_full_network_greedy_oracle_audit.json",
    comparator_runtime_integrity_report: str = "benchmark/reports/generated/sparse_comparator_runtime_integrity_audit/sparse_comparator_runtime_integrity_audit.json",
    router_aux_sweep_report: str = "benchmark/reports/generated/official_like_router_aux_sweep_decision/official_like_router_aux_sweep_report.json",
    phase_3_14_report: str = "benchmark/reports/generated/pvr_phase_3_14_bounded_completion/pvr_phase_3_14_bounded_completion_report.json",
    long_curve_5m_report: str = "benchmark/reports/generated/sparse_v2_300m_long_curve_validation_5m_decision/sparse_v2_300m_long_curve_validation_5m_report.json",
    integrity_report: str = "benchmark/reports/generated/sparse_execution_integrity_audit_rerun/sparse_execution_integrity_audit.json",
    output: str = "benchmark/reports/generated/matched_information_routing_attribution_validation",
) -> dict[str, Any]:
    training = _training_rows(Path(training_root))
    paired = _load(paired_report)
    official_paired = _load(official_paired_report)
    aggregation_audit = _load(aggregation_audit_report)
    decomposition_audit = _load(decomposition_audit_report)
    final_block_expert_sweep = _load(final_block_expert_sweep_report)
    boundary = _load(boundary_report)
    full_network_greedy_oracle = _load(full_network_greedy_oracle_report)
    comparator_runtime_integrity = _load(comparator_runtime_integrity_report)
    router_aux_sweep = _load(router_aux_sweep_report)
    phase_3_14 = _load(phase_3_14_report)
    long_curve_5m = _load(long_curve_5m_report)
    official = _official_rows(Path(official_root))
    integrity = _load(integrity_report)
    paired_sparse_wins = [
        row for row in paired.get("comparisons", [])
        if "dense" not in str(row.get("baseline", "")) and row.get("significant_candidate_win") is True
    ]
    sparse_baseline_count = len([row for row in paired.get("comparisons", []) if "dense" not in str(row.get("baseline", ""))])
    local_sparse_supported = sparse_baseline_count > 0 and len(paired_sparse_wins) == sparse_baseline_count
    dense_comparison = next((row for row in paired.get("comparisons", []) if "dense" in str(row.get("baseline", ""))), {})
    official_lm_rank = _rank(official, "lm_loss")
    official_candidate = official.get(CANDIDATE, {})
    official_candidate_best = bool(official_lm_rank and official_lm_rank[0]["variant"] == CANDIDATE)
    official_top1_clean = (
        official_candidate.get("owners_per_token") == 1.0
        and official_candidate.get("top2_execution_count") == 0
        and official_candidate.get("top4_execution_count") == 0
    )
    all_checkpoints = all(row.get("checkpoint_exists") for row in training.values())
    all_tokens_matched = len({row.get("training_tokens_seen") for row in training.values()}) == 1
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "git_commit": git_commit(),
        "experiment": "MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION",
        "status": "MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION_PARTIAL_COMPLETE",
        "decision": "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_BOUNDED_ADVANTAGE_NOT_SUPPORTED",
        "supported_labels": [
            "PVR_SPARSE_V2_EXECUTION_INTEGRITY_READY",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_LOCAL_TOP2_ADVANTAGE_SUPPORTED",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_LOCAL_SWITCH_ADVANTAGE_SUPPORTED_ACTIVE_COST_HIGHER",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_LOCAL_DENSE_GAP_NOT_CLOSED",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_AGGREGATE_ADVANTAGE_NOT_SUPPORTED",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_DENSE_COMPARISON_AGGREGATION_SENSITIVE",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_SPARSE_BASELINE_ADVANTAGE_NOT_SUPPORTED",
            "PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_SUPPORTED",
            "PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE",
            "PVR_OFFICIAL_FINAL_BLOCK_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE",
            "PVR_OFFICIAL_FINAL_BLOCK_SELECTED_EXPERT_INTERVENTION_GATE_SUPPORTED",
            "PVR_OFFICIAL_FINAL_BLOCK_ROUTER_REGRET_CONFIRMED",
            "PVR_OFFICIAL_FINAL_BLOCK_ORACLE_BEATS_SWITCH_AND_TOP2_DIAGNOSTIC_SUPPORTED",
            "OFFICIAL_EVALUATION_BOUNDARY_FROZEN",
            "OFFICIAL_LIKE_DEVELOPMENT_SET_MATERIALIZED",
            "PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE",
            "SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE",
            "PVR_OFFICIAL_LIKE_ROUTER_AUX_SWEEP_COMPLETE",
            "PVR_PHASE_3_14_BOUNDED_EXECUTION_COMPLETE",
            "PVR_300M_5M_LONG_CURVE_VALIDATION_COMPLETE_WITH_AUX_FAILURE",
        ],
        "blocked_labels": [
            "MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION_COMPLETE",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_DENSE_GAP_CLOSED",
            "PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_BOUNDED_ADVANTAGE_SUPPORTED",
            "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
            "PVR_OFFICIAL_CODE_BENCH_SUPPORTED",
            "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
            "PVR_TEACHER_INDEPENDENCE_SUPPORTED",
            "PVR_OFFICIAL_ROUTER_NEAR_ORACLE_SUPPORTED",
            "PVR_OFFICIAL_FULL_NETWORK_ORACLE_EXPERT_SELECTION_SUPPORTED",
            "PVR_PHASE_3_14_PROMOTION_SCALE_COMPLETE",
            "PVR_LARGER_BUDGET_CURVES_COMPLETE",
            "PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_SUPPORTED",
        ],
        "training_volume": {
            "all_checkpoints_present": all_checkpoints,
            "all_training_tokens_matched": all_tokens_matched,
            "rows": training,
            "caveat": "All variants now have 2,150,400 training tokens; dense/Switch/Top2/PVR were rerun or completed with the current sparse-v2 code path. This supports local comparative advantage over tested sparse baselines, not novelty or the full matched-information teacher-transfer matrix.",
        },
        "execution_integrity": {
            "status": integrity.get("status"),
            "conditions": integrity.get("conditions"),
            "source": integrity_report,
        },
        "official_evaluation_boundary": {
            "status": boundary.get("status"),
            "tiers": boundary.get("tiers"),
            "assertions": boundary.get("assertions"),
            "source": boundary_report,
        },
        "paired_local_heldout": {
            "status": paired.get("status"),
            "local_sparse_baseline_advantage_supported": local_sparse_supported,
            "dense_gap_closed": bool(dense_comparison.get("significant_candidate_win") is True),
            "comparisons": paired.get("comparisons", []),
            "source": paired_report,
        },
        "official_bounded": {
            "suite_status": _load(Path(official_root) / "benchmark_suite_result.json").get("status"),
            "candidate_top1_clean": official_top1_clean,
            "candidate_best_lm_loss": official_candidate_best,
            "lm_loss_rank": official_lm_rank,
            "rows": official,
            "source": official_root,
            "scope": "Deterministic bounded official-data slices; not full official leaderboard evidence.",
        },
        "comparator_integrity": _comparator_integrity(),
        "compile_rate_interpretation": {
            variant: {
                "compile_rate": row.get("compile_rate"),
                "sample_count": row.get("code_sample_count"),
                "success_count": round(float(row.get("compile_rate") or 0.0) * int(row.get("code_sample_count") or 0)),
                "wilson_ci95": _wilson_ci(
                    round(float(row.get("compile_rate") or 0.0) * int(row.get("code_sample_count") or 0)),
                    int(row.get("code_sample_count") or 0),
                ),
            }
            for variant, row in official.items()
        },
        "official_bounded_paired": {
            "status": official_paired.get("status"),
            "comparisons": official_paired.get("comparisons", []),
            "source": official_paired_report,
            "interpretation": "Candidate beats dense by paired/file bootstrap on bounded official files, but loses to Switch and does not beat generic Top2 by the preregistered all-baseline rule.",
        },
        "official_aggregation_reversal_audit": {
            "status": aggregation_audit.get("status"),
            "comparisons": aggregation_audit.get("comparisons", []),
            "aggregation_definitions": aggregation_audit.get("aggregation_definitions", {}),
            "source": aggregation_audit_report,
        },
        "pvr_official_decomposition_audit": {
            "status": decomposition_audit.get("status"),
            "summary": decomposition_audit.get("summary"),
            "oracle_expert_selection": decomposition_audit.get("oracle_expert_selection"),
            "source": decomposition_audit_report,
        },
        "pvr_final_block_expert_sweep_audit": {
            "status": final_block_expert_sweep.get("status"),
            "scope": final_block_expert_sweep.get("scope"),
            "overall": final_block_expert_sweep.get("overall"),
            "claim_gates": final_block_expert_sweep.get("claim_gates"),
            "final_block_oracle_vs_comparators": final_block_expert_sweep.get("final_block_oracle_vs_comparators"),
            "not_run": final_block_expert_sweep.get("not_run"),
            "source": final_block_expert_sweep_report,
            "interpretation": (
                "The selected expert beats shared-only, mean-wrong, shuffled-residual, and random-residual interventions, "
                "but final-block oracle loss is materially lower than selected loss. This confirms useful experts and "
                "substantial final-block router regret on the bounded official files."
            ),
        },
        "pvr_full_network_greedy_oracle_audit": {
            "status": full_network_greedy_oracle.get("status"),
            "scope": full_network_greedy_oracle.get("scope"),
            "overall": full_network_greedy_oracle.get("overall"),
            "claim_gates": full_network_greedy_oracle.get("claim_gates"),
            "source": full_network_greedy_oracle_report,
        },
        "sparse_comparator_runtime_integrity_audit": {
            "status": comparator_runtime_integrity.get("status"),
            "assertions": comparator_runtime_integrity.get("assertions"),
            "source": comparator_runtime_integrity_report,
        },
        "official_like_router_aux_sweep": {
            "status": router_aux_sweep.get("status"),
            "winner": router_aux_sweep.get("winner"),
            "claim_gates": router_aux_sweep.get("claim_gates"),
            "source": router_aux_sweep_report,
        },
        "pvr_phase_3_14_bounded_completion": {
            "status": phase_3_14.get("status"),
            "phase_status": phase_3_14.get("phase_status"),
            "blocked_labels": phase_3_14.get("blocked_labels"),
            "source": phase_3_14_report,
        },
        "sparse_v2_300m_5m_long_curve_validation": {
            "status": long_curve_5m.get("status"),
            "decision": long_curve_5m.get("decision"),
            "claim_gates": long_curve_5m.get("claim_gates"),
            "winner": long_curve_5m.get("winner"),
            "candidate": long_curve_5m.get("candidate"),
            "source": long_curve_5m_report,
        },
        "required_but_not_yet_run_for_strong_architecture_claim": [
            "Original teacher",
            "Dense continuation",
            "Dense-EAN",
            "Shared trunk + dense residual adapter",
            "Standard sparse upcycling",
            "Same-teacher Switch Top1",
            "Plain OneDelta/PVR",
            "OneDelta/PVR-EAN",
            "OneDelta/PVR-EAN-RG",
            "Token-matched and profiler compute-matched views",
            "Separately trained Top1/Top2/Top4",
            "Full EAN factorial with frozen/randomized/shuffled controls",
        ],
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "matched_information_routing_attribution_report.json", payload)
    lines = [
        "# Matched Information Routing Attribution Validation",
        "",
        f"Status: `{payload['status']}`",
        f"Decision: `{payload['decision']}`",
        "",
        "## Main Result",
        "",
        "Local paired heldout supports a teacher-independent sparse-v2 comparative advantage over tested sparse baselines, but the bounded official-data scorecard does not support an official bounded advantage.",
        "",
        "## Paired Local Heldout",
        "",
        "| baseline | candidate-baseline loss | 95% CI | significant win | active-param delta |",
        "|---|---:|---|---|---:|",
    ]
    for row in paired.get("comparisons", []):
        lines.append(
            f"| {row.get('baseline')} | {row.get('candidate_minus_baseline_mean_loss')} | "
            f"{row.get('ci95')} | {row.get('significant_candidate_win')} | {row.get('candidate_active_params_delta')} |"
        )
    lines.extend([
        "",
        "## Official Evaluation Boundary",
        "",
        f"Status: `{boundary.get('status')}`",
        "",
        *[f"- {key}: `{value}`" for key, value in (boundary.get("assertions") or {}).items()],
        "",
        "Official-like development data is not yet materialized, so router-regret/substrate repair training must not use the final eight official bounded files.",
        "",
    ])
    lines.extend(["", "## Bounded Official LM Rank", "", "| rank | variant | lm_loss | compile_rate | strict PVR Top1 clean |", "|---:|---|---:|---:|---|"])
    for idx, row in enumerate(official_lm_rank, 1):
        variant = row["variant"]
        top1 = (
            official[variant].get("owners_per_token") == 1.0
            and official[variant].get("top2_execution_count") == 0
            if variant == CANDIDATE
            else "not_applicable"
        )
        lines.append(f"| {idx} | {variant} | {row['lm_loss']} | {official[variant].get('compile_rate')} | {top1} |")
    lines.extend([
        "",
        "## Bounded Official Paired/File Bootstrap",
        "",
        "| baseline | block delta | block 95% CI | file delta | file 95% CI | file wins | significant file win |",
        "|---|---:|---|---:|---|---:|---|",
    ])
    for row in official_paired.get("comparisons", []):
        lines.append(
            f"| {row.get('baseline')} | {row.get('candidate_minus_baseline_mean_loss')} | "
            f"{row.get('block_bootstrap_ci95')} | {row.get('candidate_minus_baseline_file_mean_loss')} | "
            f"{row.get('file_bootstrap_ci95')} | {row.get('file_win_count')}/{row.get('paired_file_count')} | "
            f"{row.get('significant_candidate_win_file_bootstrap')} |"
        )
    lines.extend([
        "",
        "## Comparator Integrity",
        "",
        "| variant | family | configured active experts | strict PVR invariants applicable | declared Top1 comparator | dynamic Top-K audited | capacity/fallback audited |",
        "|---|---|---:|---|---|---|---|",
    ])
    for variant, row in payload["comparator_integrity"].items():
        lines.append(
            f"| {variant} | {row['model_family']} | {row['configured_experts_active_per_token']} | "
            f"{row['strict_pvr_invariants_applicable']} | {row['declared_top1_comparator']} | "
            f"{row['dynamic_topk_execution_audited']} | {row['capacity_overflow_audited'] or row['fallback_expert_use_audited']} |"
        )
    lines.extend([
        "",
        "## Aggregation Reversal Audit",
        "",
        "The scorecard `lm_loss` and the paired all-file audit use different aggregation definitions. The scorecard path evaluates limited windows of selected concatenated text; the aggregation audit evaluates up to 32 blocks per official JSONL file and reports both token-weighted and file-balanced results.",
        "",
    ])
    for comparison in aggregation_audit.get("comparisons", []):
        lines.extend([
            f"### PVR vs {comparison.get('baseline')}",
            "",
            f"- Micro delta: `{comparison.get('candidate_minus_baseline_micro')}`",
            f"- Macro file delta: `{comparison.get('candidate_minus_baseline_macro_file')}`",
            f"- File wins: `{comparison.get('candidate_file_wins')}/{comparison.get('file_count')}`",
            f"- Exact sign-test p: `{comparison.get('exact_sign_test_p')}`",
            f"- Exact sign-flip p: `{comparison.get('exact_sign_flip_p')}`",
            "",
        ])
    lines.extend([
        "",
        "## PVR Official Shared/Expert Decomposition",
        "",
        f"Status: `{decomposition_audit.get('status')}`",
        f"Mean full-minus-shared: `{(decomposition_audit.get('summary') or {}).get('mean_full_minus_shared')}`",
        f"Mean wrong-shift-minus-full: `{(decomposition_audit.get('summary') or {}).get('mean_wrong_shift_minus_full')}`",
        f"Full beats shared files: `{(decomposition_audit.get('summary') or {}).get('full_beats_shared_files')}/{(decomposition_audit.get('summary') or {}).get('file_count')}`",
        f"Wrong-shift harms files: `{(decomposition_audit.get('summary') or {}).get('wrong_shift_harms_files')}/{(decomposition_audit.get('summary') or {}).get('file_count')}`",
        f"Oracle expert selection: `{decomposition_audit.get('oracle_expert_selection')}`",
        "",
    ])
    sweep_overall = final_block_expert_sweep.get("overall") or {}
    lines.extend([
        "",
        "## PVR Final-Block All-Expert Sweep",
        "",
        f"Status: `{final_block_expert_sweep.get('status')}`",
        "",
        str(final_block_expert_sweep.get("scope") or ""),
        "",
        f"Selected loss: `{sweep_overall.get('selected_loss')}`",
        f"Shared-only loss: `{sweep_overall.get('shared_only_loss')}`",
        f"Oracle loss: `{sweep_overall.get('oracle_loss')}`",
        f"Mean wrong loss: `{sweep_overall.get('mean_wrong_loss')}`",
        f"Shuffled residual loss: `{sweep_overall.get('shuffled_residual_loss')}`",
        f"Random residual loss: `{sweep_overall.get('random_residual_loss')}`",
        f"Mean router regret: `{sweep_overall.get('mean_router_regret')}`",
        f"95th-percentile router regret: `{sweep_overall.get('p95_router_regret')}`",
        f"Selected-is-oracle rate: `{sweep_overall.get('selected_is_oracle_rate')}`",
        f"Selected-is-top2 rate: `{sweep_overall.get('selected_is_top2_rate')}`",
        "",
        "Final-block oracle vs comparators:",
        "",
        "| comparator | oracle - comparator micro loss |",
        "|---|---:|",
        *[
            f"| {variant} | {delta} |"
            for variant, delta in ((final_block_expert_sweep.get("final_block_oracle_vs_comparators") or {}).get("oracle_minus_comparator_micro_loss") or {}).items()
        ],
        "",
        "Interpretation: selected experts are useful, but final-block oracle expert selection is materially better than the trained router selection. This supports a router-regret diagnosis for the available final-block expert bank while keeping full-network oracle selection marked `NOT_RUN_NOT_IMPLEMENTED`.",
        "",
        "Claim gates:",
        "",
        *[f"- {key}: `{value}`" for key, value in (final_block_expert_sweep.get("claim_gates") or {}).items()],
        "",
    ])
    greedy_overall = full_network_greedy_oracle.get("overall") or {}
    lines.extend([
        "",
        "## PVR Full-Network Greedy Oracle Audit",
        "",
        f"Status: `{full_network_greedy_oracle.get('status')}`",
        "",
        str(full_network_greedy_oracle.get("scope") or ""),
        "",
        f"Selected loss: `{greedy_overall.get('selected_loss')}`",
        f"Greedy full-network oracle loss: `{greedy_overall.get('greedy_full_network_oracle_loss')}`",
        f"Greedy oracle improvement over selected: `{greedy_overall.get('greedy_oracle_improvement_over_selected')}`",
        f"Selected-is-oracle rate across block decisions: `{greedy_overall.get('selected_is_oracle_rate_across_block_decisions')}`",
        "",
        "## Sparse Comparator Runtime Integrity",
        "",
        f"Status: `{comparator_runtime_integrity.get('status')}`",
        "",
        *[f"- {key}: `{value}`" for key, value in (comparator_runtime_integrity.get("assertions") or {}).items()],
        "",
        "## Official-Like Router Auxiliary Sweep",
        "",
        f"Status: `{router_aux_sweep.get('status')}`",
        f"Winner: `{(router_aux_sweep.get('winner') or {}).get('model_variant')}`",
        f"Winner aux weight: `{(router_aux_sweep.get('winner') or {}).get('routing_aux_weight')}`",
        f"Winner final loss: `{(router_aux_sweep.get('winner') or {}).get('final_loss')}`",
        "",
        "## Phase 3-14 Bounded Completion",
        "",
        f"Status: `{phase_3_14.get('status')}`",
        "",
        "## 300M 5M Long-Curve Validation",
        "",
        f"Status: `{long_curve_5m.get('status')}`",
        f"Decision: `{long_curve_5m.get('decision')}`",
        f"Winner: `{(long_curve_5m.get('winner') or {}).get('variant')}`",
        f"Candidate mean eval: `{(long_curve_5m.get('candidate') or {}).get('mean_eval_loss')}`",
        f"Winner mean eval: `{(long_curve_5m.get('winner') or {}).get('mean_eval_loss')}`",
        "",
    ])
    lines.extend([
        "",
        "## Compile-Rate Interpretation",
        "",
        "The bounded code-oriented compile check uses only 16 samples, so it is reported as descriptive evidence with Wilson intervals, not broad code capability.",
        "",
        "| variant | compile rate | successes / samples | Wilson 95% CI |",
        "|---|---:|---:|---|",
    ])
    for variant, row in payload["compile_rate_interpretation"].items():
        lines.append(
            f"| {variant} | {row['compile_rate']} | {row['success_count']} / {row['sample_count']} | {row['wilson_ci95']} |"
        )
    lines.extend([
        "",
        "## Blocked Claims",
        "",
        *[f"- `{label}`" for label in payload["blocked_labels"]],
        "",
        "## Missing Strong-Claim Comparators",
        "",
        *[f"- {item}" for item in payload["required_but_not_yet_run_for_strong_architecture_claim"]],
    ])
    (out / "matched_information_routing_attribution_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="benchmark/reports/generated/matched_information_routing_attribution_validation")
    args = parser.parse_args()
    payload = build(output=args.output)
    print(json.dumps({"status": payload["status"], "decision": payload["decision"]}, indent=2))


if __name__ == "__main__":
    main()
