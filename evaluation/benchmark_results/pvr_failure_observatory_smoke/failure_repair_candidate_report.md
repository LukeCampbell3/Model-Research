# PVR-EC Failure Repair Candidate Report

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
  "status": "PVR_EC_FAILURE_OBSERVATORY_READY",
  "failure_modes": [
    "PVR_EC_FAILURE_OWNER_PROTOTYPE_COLLAPSE",
    "PVR_EC_FAILURE_QPM_SHAPE_REGRESSION"
  ],
  "candidate_count": 12,
  "repair_candidates": [
    "CUDA events instead of global sync",
    "cache masks and ownership bias",
    "disable sparse logit decomposition in inference timing",
    "family_balanced_loss_light",
    "family_balanced_sampling",
    "owner_entropy_floor_diagnostic_only",
    "ownership_bias_clip_adjustment",
    "preallocate tensors",
    "prototype_entropy_regularization_light",
    "remove Python objects from measured forward",
    "separate diagnostic and inference paths",
    "warmup per shape"
  ],
  "repair_candidate_playbooks": {
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
    "larger experts",
    "new router architecture",
    "removing required expert execution"
  ],
  "promotion_ready": false
}
```