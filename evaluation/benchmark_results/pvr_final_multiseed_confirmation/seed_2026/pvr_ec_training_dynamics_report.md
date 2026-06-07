# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:45:38.285590",
    "run_id": "algo_20260607_174322_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 2026,
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
        2026
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
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.22179481573402882,
      "accuracy": 0.44536363636363635
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.19380450248718262,
      "accuracy": 0.5106055219812774
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.21609133575111628,
      "accuracy": 0.509388308168796
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 1.4335313439369202,
      "accuracy": 0.11938288591586405
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.19737683236598969,
      "accuracy": 0.08391038696537678
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.300133652985096,
      "accuracy": 0.03688297282307266
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.40572931431233883,
      "accuracy": 0.0037359900373599006
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.2726064858337243,
      "accuracy": 0.03406853091768413
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.2885015681385994,
      "accuracy": 0.185
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.26751320343464613,
      "accuracy": 0.10783268159734566
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.2837356049567461,
      "accuracy": 0.1613433991482772
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 1.3940101973712444,
      "accuracy": 0.18009894903246582
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.2064154827967286,
      "accuracy": 0.11364562118126273
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.3074561841785908,
      "accuracy": 0.07542983915696062
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.41389917954802513,
      "accuracy": 0.06621004566210045
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.22074340283870697,
      "eval_loss": 0.2919406443834305,
      "accuracy": 0.07424182749113824
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.18395077250897884,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.17868976388126612,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.1796662723645568,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 1.286568507552147,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.19539925176650286,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.29588529095053673,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.40159808844327927,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.2721534085770448,
      "accuracy": 0.10456872784560851
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6666666666666666,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```