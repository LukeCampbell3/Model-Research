# PVR-EC Deployment vs Research Verdict Report

**Status:** PVR_EC_REPEATABILITY_BLOCKED

**Statuses:** PVR_EC_ALGORITHMIC_STAGE_COMPLETE, PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE, PVR_EC_DO_NOT_PROMOTE, PVR_EC_NLP_BRIDGE_LADDER_REQUIRED, PVR_EC_NLP_BRIDGE_STAGE_1_READY, PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS, PVR_EC_REPEATABILITY_BLOCKED

```json
{
  "metadata": {
    "seed": 42,
    "input_dirs": [
      "evaluation/benchmark_results/pvr_minimax_collapse_case_replay",
      "evaluation/benchmark_results/pvr_minimax_candidate_selection",
      "evaluation/benchmark_results/pvr_minimax_stability_repair_sweep",
      "evaluation/benchmark_results/pvr_minimax_qpm_failing_shape_replay",
      "evaluation/benchmark_results/pvr_minimax_qpm_formula_audit",
      "evaluation/benchmark_results/pvr_minimax_shape_qpm_runtime_repair",
      "evaluation/benchmark_results/pvr_final_candidate_v1_2_revalidation"
    ],
    "command": "evaluation/run_algorithmic_benchmarks.py --run-pvr-nlp-research-readiness-gate --input-dirs evaluation/benchmark_results/pvr_minimax_collapse_case_replay,evaluation/benchmark_results/pvr_minimax_candidate_selection,evaluation/benchmark_results/pvr_minimax_stability_repair_sweep,evaluation/benchmark_results/pvr_minimax_qpm_failing_shape_replay,evaluation/benchmark_results/pvr_minimax_qpm_formula_audit,evaluation/benchmark_results/pvr_minimax_shape_qpm_runtime_repair,evaluation/benchmark_results/pvr_final_candidate_v1_2_revalidation --output-dir evaluation/benchmark_results/pvr_nlp_research_readiness"
  },
  "status": "PVR_EC_REPEATABILITY_BLOCKED",
  "deployment_verdict": "PVR_EC_REPEATABILITY_BLOCKED",
  "research_verdict": "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
  "statuses": [
    "PVR_EC_ALGORITHMIC_STAGE_COMPLETE",
    "PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_NLP_BRIDGE_LADDER_REQUIRED",
    "PVR_EC_NLP_BRIDGE_STAGE_1_READY",
    "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
    "PVR_EC_REPEATABILITY_BLOCKED"
  ],
  "promotion_ready": false,
  "research_ready": true,
  "collapse_count": 4,
  "unexplained_collapse_count": 0,
  "qpm_classified": true,
  "calibration_measured": true,
  "mean_competitive": true,
  "forward_purity": true,
  "missing_reports": []
}
```