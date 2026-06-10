# PVR-EC QPM / Memory Repair Report

**Status:** PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_MEMORY_SHAPE_REGRESSION_ANALYZED, PVR_EC_MEMORY_SHAPE_REGRESSION_REPAIRED, PVR_EC_QPM_SHAPE_REGRESSION_ANALYZED, PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T12:06:42.355777",
    "run_id": "algo_20260610_120642_smoke",
    "git_commit": "40abf0eeee8adcd8bbeaf41be833cfb6fd251c98",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 30,
    "sample_limit": null,
    "mode": "smoke",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED",
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_MEMORY_SHAPE_REGRESSION_ANALYZED",
    "PVR_EC_MEMORY_SHAPE_REGRESSION_REPAIRED",
    "PVR_EC_QPM_SHAPE_REGRESSION_ANALYZED",
    "PVR_EC_QPM_SHAPE_REGRESSION_REPAIRED"
  ],
  "promotion_ready": false,
  "passed": true,
  "shape_count": 1,
  "qpm_failed_shapes": [
    {
      "batch_size": 1,
      "seq_len": 16,
      "fixed_latency_p50": 1.0,
      "candidate_latency_p50": 0.8,
      "fixed_latency_p95": 1.1,
      "candidate_latency_p95": 0.9,
      "fixed_memory_peak": 10,
      "candidate_memory_peak": 9,
      "fixed_quality_per_ms": 0.032258064516129115,
      "candidate_quality_per_ms": -0.04166666666666666,
      "QPM_pass": false,
      "memory_pass": true,
      "owners_per_token": 1.0,
      "Top2_executions": 0.0,
      "Top4_executions": 0.0,
      "hot_path_mode": "FULLY_VECTORIZED",
      "diagnostics_enabled": false,
      "cuda_sync_count": 0,
      "cpu_transfer_count": 0,
      "file_write_count": 0,
      "temporary_tensor_alloc_estimate": null
    }
  ],
  "memory_failed_shapes": [],
  "shapes": [
    {
      "batch_size": 1,
      "seq_len": 16,
      "fixed_latency_p50": 1.0,
      "candidate_latency_p50": 0.8,
      "fixed_latency_p95": 1.1,
      "candidate_latency_p95": 0.9,
      "fixed_memory_peak": 10,
      "candidate_memory_peak": 9,
      "fixed_quality_per_ms": 0.032258064516129115,
      "candidate_quality_per_ms": -0.04166666666666666,
      "QPM_pass": false,
      "memory_pass": true,
      "owners_per_token": 1.0,
      "Top2_executions": 0.0,
      "Top4_executions": 0.0,
      "hot_path_mode": "FULLY_VECTORIZED",
      "diagnostics_enabled": false,
      "cuda_sync_count": 0,
      "cpu_transfer_count": 0,
      "file_write_count": 0,
      "temporary_tensor_alloc_estimate": null
    }
  ]
}
```