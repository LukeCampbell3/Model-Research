# PVR-EC Failure Repair Candidate Report

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
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
}
```