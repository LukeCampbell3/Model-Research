# PVR-EC Failure Observatory Gate Report

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

**Statuses:** PVR_EC_FAILURE_OBSERVATORY_READY, PVR_EC_RESEARCH_EXPANSION_ALLOWED, PVR_EC_DEPLOYMENT_STILL_BLOCKED, PVR_EC_DO_NOT_PROMOTE

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "deployment_verdict": "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
  "research_verdict": "PVR_EC_RESEARCH_EXPANSION_ALLOWED",
  "statuses": [
    "PVR_EC_FAILURE_OBSERVATORY_READY",
    "PVR_EC_RESEARCH_EXPANSION_ALLOWED",
    "PVR_EC_DEPLOYMENT_STILL_BLOCKED",
    "PVR_EC_DO_NOT_PROMOTE"
  ],
  "forward_purity_passed": true,
  "unknown_failure_active": false,
  "all_failures_classified": true,
  "qpm_issues_classified": true,
  "event_count": 24,
  "input_dirs": [
    "evaluation/benchmark_results/pvr_failure_observatory_qpm_replay"
  ],
  "loaded_report_names": [
    "aux_alpha_capability_report.json",
    "capacity_distillation_compression_plan.json",
    "capacity_fairness_audit_report.json",
    "capacity_fairness_matrix_report.json",
    "capacity_interpolation_report.json",
    "capacity_knee_report.json",
    "failure_attribution_report.json",
    "failure_case_replay_report.json",
    "failure_mode_registry_report.json",
    "failure_mode_scoreboard.json",
    "failure_mode_trend_report.json",
    "failure_observatory_events.json",
    "failure_observatory_gate_report.json",
    "failure_repair_candidate_report.json",
    "failure_repair_validation_report.json",
    "fair_deployment_comparison_report.json",
    "fixed_moe_vectorization_report.json",
    "inference_latency_matrix.json",
    "longer_capability_report.json",
    "memory_efficiency_report.json",
    "pvr_deploy_go_no_go.json",
    "pvr_deploy_status.json",
    "pvr_deployment_report.json",
    "pvr_ec_capacity_architecture_report.json",
    "pvr_ec_latency_stability_report.json",
    "pvr_ec_learning_separation_report.json",
    "pvr_ec_loss_calibration_report.json",
    "pvr_ec_nlp_observatory_bridge_plan.json",
    "pvr_ec_ownership_integration_report.json",
    "pvr_ec_qpm_failing_shape_replay_report.json",
    "pvr_ec_root_baseline_matrix.json",
    "pvr_ec_root_cause_loop_report.json",
    "pvr_ec_root_cause_summary.json",
    "pvr_ec_shared_sparse_ablation_report.json",
    "pvr_ec_task_fit_report.json",
    "pvr_ec_training_dynamics_report.json",
    "pvr_hot_path_profile.json",
    "pvr_inference_latency_report.json"
  ],
  "scoreboard": {
    "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
    "mode_count": 2,
    "scoreboard": [
      {
        "failure_mode": "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
        "count": 7,
        "repeatable_count": 7,
        "unexplained_count": 0,
        "repaired_count": 0,
        "partial_repair_count": 0,
        "blocked_count": 7,
        "affected_seeds": [],
        "affected_families": [],
        "affected_tasks": [],
        "affected_shapes": [
          "b1-s16",
          "b1-s64",
          "b32-s16",
          "b8-s16"
        ],
        "most_common_primary_metric": "loss_gap_vs_fixed",
        "current_status": "blocked",
        "recommended_next_action": "run bounded repair validation"
      },
      {
        "failure_mode": "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION",
        "count": 17,
        "repeatable_count": 17,
        "unexplained_count": 0,
        "repaired_count": 0,
        "partial_repair_count": 0,
        "blocked_count": 17,
        "affected_seeds": [],
        "affected_families": [],
        "affected_tasks": [],
        "affected_shapes": [
          "b16-s128",
          "b16-s64",
          "b32-s128",
          "b32-s16",
          "b32-s64",
          "b64-s128",
          "b64-s16",
          "b64-s64",
          "b8-s64"
        ],
        "most_common_primary_metric": "loss_gap_vs_fixed",
        "current_status": "blocked",
        "recommended_next_action": "run bounded repair validation"
      }
    ]
  },
  "trend": {
    "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
    "failure_count": 24,
    "failure_count_change": 0,
    "collapse_count": 0,
    "collapse_count_change": 0,
    "calibration_mean": 0.0,
    "calibration_change": 0.0,
    "QPM_shape_pass_count": 7,
    "QPM_shape_pass_count_change": 0,
    "overamp_change": 0.0,
    "forward_purity_change": 0.0,
    "platform": "Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35"
  },
  "repair_candidates": {
    "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
    "failure_modes": [
      "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
      "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
    ],
    "candidate_count": 10,
    "repair_candidates": [
      "CUDA events instead of global sync",
      "bounded diagnostic-only repair",
      "cache masks and ownership bias",
      "disable sparse logit decomposition in inference timing",
      "preallocate tensors",
      "remove Python objects from measured forward",
      "repeatability replay",
      "separate diagnostic and inference paths",
      "slice-specific validation",
      "warmup per shape"
    ],
    "repair_candidate_playbooks": {
      "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY": {
        "inspect": [
          "loss_gap_vs_fixed",
          "accuracy_gap_vs_fixed",
          "calibration_gap",
          "runtime_purity_passed"
        ],
        "allowed_repairs": [
          "bounded diagnostic-only repair",
          "repeatability replay",
          "slice-specific validation"
        ],
        "disallowed_repairs": [
          "Top2/Top4 execution",
          "new routing architecture",
          "distillation",
          "quantization",
          "model size increase"
        ]
      },
      "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION": {
        "inspect": [
          "latency_p50",
          "latency_p95",
          "p95_p50_ratio",
          "memory_peak",
          "diagnostic_tensor_retention",
          "cuda_sync_count",
          "cpu_transfer_count",
          "temporary_tensor_alloc_estimate"
        ],
        "allowed_repairs": [
          "separate diagnostic and inference paths",
          "disable sparse logit decomposition in inference timing",
          "preallocate tensors",
          "cache masks and ownership bias",
          "remove Python objects from measured forward",
          "CUDA events instead of global sync",
          "warmup per shape"
        ],
        "disallowed_repairs": [
          "changing model math",
          "removing required expert execution",
          "changing output",
          "Top2/Top4"
        ]
      }
    },
    "disallowed_global": [
      "Top2/Top4",
      "Top2/Top4 execution",
      "changing model math",
      "changing output",
      "distillation",
      "model size increase",
      "new routing architecture",
      "quantization",
      "removing required expert execution"
    ],
    "promotion_ready": false
  },
  "repair_validation": {
    "status": "REPAIR_REQUIRES_MORE_EVIDENCE",
    "passed": false,
    "repair_results": [
      {
        "repair_candidate": "CUDA events instead of global sync",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "bounded diagnostic-only repair",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "cache masks and ownership bias",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "disable sparse logit decomposition in inference timing",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "preallocate tensors",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "remove Python objects from measured forward",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "repeatability replay",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "separate diagnostic and inference paths",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "slice-specific validation",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      },
      {
        "repair_candidate": "warmup per shape",
        "repair_result": "REPAIR_SOLVED",
        "repair_validation_status": "REPAIR_SOLVED"
      }
    ]
  }
}
```