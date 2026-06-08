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
    "evaluation/benchmark_results/pvr_failure_observatory_known_replay"
  ],
  "loaded_report_names": [
    "failure_attribution_report.json",
    "failure_case_replay_report.json",
    "failure_mode_registry_report.json",
    "failure_mode_scoreboard.json",
    "failure_mode_trend_report.json",
    "failure_observatory_events.json",
    "failure_observatory_gate_report.json",
    "failure_repair_candidate_report.json",
    "failure_repair_validation_report.json",
    "pvr_ec_nlp_observatory_bridge_plan.json"
  ],
  "scoreboard": {
    "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
    "mode_count": 2,
    "scoreboard": [
      {
        "failure_mode": "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
        "count": 18,
        "repeatable_count": 18,
        "unexplained_count": 0,
        "repaired_count": 0,
        "partial_repair_count": 0,
        "blocked_count": 18,
        "affected_seeds": [
          "123",
          "777"
        ],
        "affected_families": [
          "clrs_style"
        ],
        "affected_tasks": [
          "clrs_lcs",
          "clrs_searching",
          "clrs_sorting"
        ],
        "affected_shapes": [],
        "most_common_primary_metric": "loss_gap_vs_fixed",
        "current_status": "blocked",
        "recommended_next_action": "run bounded repair validation"
      },
      {
        "failure_mode": "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
        "count": 6,
        "repeatable_count": 6,
        "unexplained_count": 0,
        "repaired_count": 0,
        "partial_repair_count": 0,
        "blocked_count": 6,
        "affected_seeds": [
          "123",
          "777"
        ],
        "affected_families": [
          "listops"
        ],
        "affected_tasks": [
          "listops"
        ],
        "affected_shapes": [],
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
    "collapse_count": 15,
    "collapse_count_change": 0,
    "calibration_mean": 0.19292891033397178,
    "calibration_change": 0.0,
    "QPM_shape_pass_count": 19,
    "QPM_shape_pass_count_change": 0,
    "overamp_change": 0.0,
    "forward_purity_change": 0.0,
    "platform": "Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35"
  },
  "repair_candidates": {
    "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
    "failure_modes": [
      "PVR_EC_FAILURE_DATA_SPLIT_DIFFICULTY",
      "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE"
    ],
    "candidate_count": 8,
    "repair_candidates": [
      "bounded diagnostic-only repair",
      "family_balanced_loss_light",
      "family_balanced_sampling",
      "owner_entropy_floor_diagnostic_only",
      "ownership_bias_clip_adjustment",
      "prototype_entropy_regularization_light",
      "repeatability replay",
      "slice-specific validation"
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
      "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE": {
        "inspect": [
          "owner_entropy",
          "prototype_entropy",
          "dead_expert_count",
          "expert_monopoly_rate",
          "prototype_local_monopoly_rate"
        ],
        "allowed_repairs": [
          "family_balanced_sampling",
          "family_balanced_loss_light",
          "ownership_bias_clip_adjustment",
          "prototype_entropy_regularization_light",
          "owner_entropy_floor_diagnostic_only"
        ],
        "disallowed_repairs": [
          "Top2/Top4 execution",
          "new router architecture",
          "larger experts",
          "distillation"
        ]
      }
    },
    "disallowed_global": [
      "Top2/Top4 execution",
      "distillation",
      "larger experts",
      "model size increase",
      "new router architecture",
      "new routing architecture",
      "quantization"
    ],
    "promotion_ready": false
  },
  "repair_validation": {
    "status": "REPAIR_REQUIRES_MORE_EVIDENCE",
    "passed": false,
    "repair_results": [
      {
        "repair_candidate": "bounded diagnostic-only repair",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "family_balanced_loss_light",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "family_balanced_sampling",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "owner_entropy_floor_diagnostic_only",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "ownership_bias_clip_adjustment",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "prototype_entropy_regularization_light",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "repeatability replay",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      },
      {
        "repair_candidate": "slice-specific validation",
        "repair_result": "REPAIR_REQUIRES_MORE_EVIDENCE",
        "repair_validation_status": "REPAIR_REQUIRES_MORE_EVIDENCE"
      }
    ]
  }
}
```