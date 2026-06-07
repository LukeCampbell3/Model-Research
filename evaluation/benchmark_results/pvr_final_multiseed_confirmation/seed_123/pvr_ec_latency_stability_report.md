# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:41:02.230720",
    "run_id": "algo_20260607_173845_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-multiseed-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_multiseed_confirmation",
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
    "train_steps": 500,
    "sample_limit": 1000,
    "mode": "benchmark-lite",
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
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_multiseed_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        123
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "max_train_seconds": null
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "by_model": {
    "fixed_moe_vectorized": {
      "count": 8,
      "avg_loss": 0.4128779808913047,
      "avg_accuracy": 0.2465923217227525,
      "avg_train_loss": 0.15063753724098206,
      "latency_p50_ms": 960.5477154254913,
      "latency_p95_ms": 960.5477154254913,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.46422695667327696,
      "avg_accuracy": 0.05611798299936589,
      "avg_train_loss": 0.2083549052476883,
      "latency_p50_ms": 712.7372026443481,
      "latency_p95_ms": 712.7372026443481,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.40100697781114525,
      "avg_accuracy": 0.23434802820851366,
      "avg_train_loss": 0.18344131112098694,
      "latency_p50_ms": 639.3009126186371,
      "latency_p95_ms": 639.3009126186371,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    }
  },
  "latency_p95_p50_ratio_reported": true,
  "max_latency_p95_p50_ratio": 1.0,
  "rows": [
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1062.6587867736816,
      "latency_p95_ms": 1062.6587867736816,
      "latency_p99_ms": 1062.6587867736816,
      "latency_max_ms": 1062.6587867736816,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1063.7907981872559,
      "latency_p95_ms": 1063.7907981872559,
      "latency_p99_ms": 1063.7907981872559,
      "latency_max_ms": 1063.7907981872559,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1066.4291381835938,
      "latency_p95_ms": 1066.4291381835938,
      "latency_p99_ms": 1066.4291381835938,
      "latency_max_ms": 1066.4291381835938,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1070.4150199890137,
      "latency_p95_ms": 1070.4150199890137,
      "latency_p99_ms": 1070.4150199890137,
      "latency_max_ms": 1070.4150199890137,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1069.4284439086914,
      "latency_p95_ms": 1069.4284439086914,
      "latency_p99_ms": 1069.4284439086914,
      "latency_max_ms": 1069.4284439086914,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 529.7424793243408,
      "latency_p95_ms": 529.7424793243408,
      "latency_p99_ms": 529.7424793243408,
      "latency_max_ms": 529.7424793243408,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1038.3565425872803,
      "latency_p95_ms": 1038.3565425872803,
      "latency_p99_ms": 1038.3565425872803,
      "latency_max_ms": 1038.3565425872803,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 783.5605144500732,
      "latency_p95_ms": 783.5605144500732,
      "latency_p99_ms": 783.5605144500732,
      "latency_max_ms": 783.5605144500732,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 792.1195030212402,
      "latency_p95_ms": 792.1195030212402,
      "latency_p99_ms": 792.1195030212402,
      "latency_max_ms": 792.1195030212402,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 839.3619060516357,
      "latency_p95_ms": 839.3619060516357,
      "latency_p99_ms": 839.3619060516357,
      "latency_max_ms": 839.3619060516357,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 810.1170063018799,
      "latency_p95_ms": 810.1170063018799,
      "latency_p99_ms": 810.1170063018799,
      "latency_max_ms": 810.1170063018799,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 802.6385307312012,
      "latency_p95_ms": 802.6385307312012,
      "latency_p99_ms": 802.6385307312012,
      "latency_max_ms": 802.6385307312012,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 764.6698951721191,
      "latency_p95_ms": 764.6698951721191,
      "latency_p99_ms": 764.6698951721191,
      "latency_max_ms": 764.6698951721191,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 379.03308868408203,
      "latency_p95_ms": 379.03308868408203,
      "latency_p99_ms": 379.03308868408203,
      "latency_max_ms": 379.03308868408203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 747.5271224975586,
      "latency_p95_ms": 747.5271224975586,
      "latency_p99_ms": 747.5271224975586,
      "latency_max_ms": 747.5271224975586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 566.4305686950684,
      "latency_p95_ms": 566.4305686950684,
      "latency_p99_ms": 566.4305686950684,
      "latency_max_ms": 566.4305686950684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 691.7369365692139,
      "latency_p95_ms": 691.7369365692139,
      "latency_p99_ms": 691.7369365692139,
      "latency_max_ms": 691.7369365692139,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 711.1926078796387,
      "latency_p95_ms": 711.1926078796387,
      "latency_p99_ms": 711.1926078796387,
      "latency_max_ms": 711.1926078796387,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 699.7246742248535,
      "latency_p95_ms": 699.7246742248535,
      "latency_p99_ms": 699.7246742248535,
      "latency_max_ms": 699.7246742248535,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 724.3747711181641,
      "latency_p95_ms": 724.3747711181641,
      "latency_p99_ms": 724.3747711181641,
      "latency_max_ms": 724.3747711181641,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 712.5377655029297,
      "latency_p95_ms": 712.5377655029297,
      "latency_p99_ms": 712.5377655029297,
      "latency_max_ms": 712.5377655029297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 356.8530082702637,
      "latency_p95_ms": 356.8530082702637,
      "latency_p99_ms": 356.8530082702637,
      "latency_max_ms": 356.8530082702637,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 687.7374649047852,
      "latency_p95_ms": 687.7374649047852,
      "latency_p99_ms": 687.7374649047852,
      "latency_max_ms": 687.7374649047852,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 530.250072479248,
      "latency_p95_ms": 530.250072479248,
      "latency_p99_ms": 530.250072479248,
      "latency_max_ms": 530.250072479248,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```