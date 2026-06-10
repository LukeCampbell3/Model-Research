# PVR-EC Parity Init Sweep Report

**Status:** PVR_EC_NONLINEAR_OVERFIT_READY

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_FIXED_OWNER_PARITY_FAILED, PVR_EC_LEARNED_OWNER_PARITY_FAILED, PVR_EC_LOSS_SCHEDULE_BLOCKER, PVR_EC_NONLINEAR_OVERFIT_FAILED, PVR_EC_NONLINEAR_OVERFIT_READY, PVR_EC_PARITY_OVERFIT_FAILED, PVR_EC_ROUND_ROBIN_PARITY_FAILED

```json
{
  "metadata": {
    "timestamp": "2026-06-10T00:39:23.556648",
    "run_id": "algo_20260610_003923_pvr-overfit-sanity",
    "git_commit": "928992ecf24f649e7449de43e61a75deed225384",
    "docker_image": "N/A",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec_stage3f_descriptor_confirmation.py sparse_loop_moe/tests/test_pvr_ec_stage4_small_nlp_bridge.py sparse_loop_moe/tests/test_pvr_ec_stage5_research_nlp.py sparse_loop_moe/tests/test_pvr_ec_final_research_gate.py sparse_loop_moe/tests/test_pvr_ec_stage3e_gate.py sparse_loop_moe/tests/test_pvr_ec.py -q --tb=line",
    "model_variants": [
      "pvr_full",
      "pvr_full_scale_schedule_1_to_4"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 500,
    "sample_limit": null,
    "mode": "pvr-nonlinear-overfit",
    "scale": "tiny",
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
    "pvr_expert_delta_scale_decay": null,
    "pvr_overfit_tasks": [
      "toy_identity"
    ],
    "pvr_overfit_steps": 2,
    "pvr_overfit_batch_size": 2,
    "failures": []
  },
  "statuses": [
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_FIXED_OWNER_PARITY_FAILED",
    "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
    "PVR_EC_LOSS_SCHEDULE_BLOCKER",
    "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "PVR_EC_NONLINEAR_OVERFIT_READY",
    "PVR_EC_PARITY_OVERFIT_FAILED",
    "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
  ],
  "promotion_ready": false,
  "analysis": {
    "overall_status": "PVR_EC_NONLINEAR_OVERFIT_FAILED",
    "statuses": [
      "PVR_EC_DO_NOT_PROMOTE",
      "PVR_EC_FIXED_OWNER_PARITY_FAILED",
      "PVR_EC_LEARNED_OWNER_PARITY_FAILED",
      "PVR_EC_LOSS_SCHEDULE_BLOCKER",
      "PVR_EC_NONLINEAR_OVERFIT_FAILED",
      "PVR_EC_NONLINEAR_OVERFIT_READY",
      "PVR_EC_PARITY_OVERFIT_FAILED",
      "PVR_EC_ROUND_ROBIN_PARITY_FAILED"
    ],
    "controls_pass": false,
    "fixed_owner_parity": false,
    "round_robin_parity": false,
    "uniform_owner_parity": false,
    "learned_owner_parity": false,
    "sparse_only_parity": false,
    "shared_only_parity": false,
    "dense_parity": false,
    "fixed_moe_parity": false,
    "micro_ffn_parity": false,
    "best_expert_delta_scale": null,
    "best_expert_delta_scale_accuracy": 0.0,
    "dominant_failure_mode": "loss_schedule_or_target_blocker",
    "recommended_repair": "verify_parity_target_and_loss_construction",
    "parity_results_by_model": {
      "pvr_full": {},
      "pvr_full_scale_schedule_1_to_4": {}
    },
    "nonlinear_results_by_model": {
      "pvr_full": {},
      "pvr_full_scale_schedule_1_to_4": {}
    }
  },
  "status": "PVR_EC_NONLINEAR_OVERFIT_READY",
  "note": "Init sweep included via delta_rank and micro_ffn variants"
}
```