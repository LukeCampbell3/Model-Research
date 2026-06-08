# PVR-EC NLP Research Readiness Report

**Status:** PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS

**Statuses:** PVR_EC_ALGORITHMIC_STAGE_COMPLETE, PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE, PVR_EC_DO_NOT_PROMOTE, PVR_EC_NLP_BRIDGE_LADDER_REQUIRED, PVR_EC_NLP_BRIDGE_STAGE_1_READY, PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS, PVR_EC_REPEATABILITY_BLOCKED

```json
{
  "metadata": {
    "seed": 42,
    "input_dirs": [
      "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0"
    ],
    "command": "C:\\Users\\jcthi\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pytest -q sparse_loop_moe/tests/test_pvr_ec.py -k minimax or nlp_research or qpm or collapse"
  },
  "status": "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
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
  "collapse_count": 1,
  "unexplained_collapse_count": 0,
  "qpm_classified": true,
  "calibration_measured": true,
  "mean_competitive": true,
  "forward_purity": true,
  "missing_reports": [],
  "passed": true,
  "nlp_bridge_ladder": {
    "status": "PVR_EC_NLP_BRIDGE_STAGE_1_READY",
    "statuses": [
      "PVR_EC_NLP_BRIDGE_LADDER_REQUIRED",
      "PVR_EC_NLP_BRIDGE_STAGE_1_READY"
    ],
    "research_verdict": "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
    "stage_1_ready": true,
    "stages": [
      {
        "stage": 1,
        "name": "character/byte-level copy and transformation",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 2,
        "name": "small-vocab synthetic language modeling",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 3,
        "name": "algorithmic text tasks with natural-language wrappers",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 4,
        "name": "short-context language modeling",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 5,
        "name": "instruction-style toy QA",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 6,
        "name": "small real NLP benchmark subset",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      },
      {
        "stage": 7,
        "name": "larger NLP benchmark suite",
        "required_models": [
          "fixed_moe_vectorized",
          "dense_baseline_or_dense_transformer",
          "pvr_ec_deploy_top1",
          "pvr_ec_ownership_top1_final_candidate"
        ],
        "required_metrics": [
          "owners/token",
          "Top2/Top4 executions",
          "loss",
          "accuracy_or_token_accuracy",
          "calibration",
          "latency",
          "memory",
          "collapse cases",
          "task/family breakdown",
          "confidence metrics",
          "incorrect overamp metrics"
        ],
        "promotion_rule": "advance only if forward purity passes, Top2/Top4 stay zero, metrics are competitive or explained, calibration is measured, collapses are absent or classified, and artifacts are reproducible"
      }
    ]
  },
  "source_reports": {
    "collapse": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_collapse_case_replay_report.json",
    "minimax": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_minimax_candidate_selection_report.json",
    "stability": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_stability_repair_sweep_report.json",
    "qpm_replay": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_qpm_failing_shape_replay_report.json",
    "qpm_formula": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_qpm_formula_audit_report.json",
    "qpm_runtime": "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0\\pvr_ec_shape_qpm_runtime_repair_report.json",
    "v1_2_revalidation": null
  }
}
```