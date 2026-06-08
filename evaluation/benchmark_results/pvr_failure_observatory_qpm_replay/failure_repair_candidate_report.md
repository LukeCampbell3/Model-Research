# PVR-EC Failure Repair Candidate Report

**Status:** PVR_EC_FAILURE_OBSERVATORY_READY

```json
{
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
}
```