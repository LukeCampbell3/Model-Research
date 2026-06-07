# PVR-EC Training Dynamics Report

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
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2159461621195078,
      "accuracy": 0.49127272727272725
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.17557950783520937,
      "accuracy": 0.5577925153955471
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.20173880830407143,
      "accuracy": 0.5481997677119629
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 1.5207750648260117,
      "accuracy": 0.16809486952675806
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.19944812171161175,
      "accuracy": 0.08578584846587352
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2926559541374445,
      "accuracy": 0.040863981319322826
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.41412714682519436,
      "accuracy": 0.022579970729667574
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2827530813713868,
      "accuracy": 0.058148893360160964
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2900001537054777,
      "accuracy": 0.14772727272727273
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2672149548307061,
      "accuracy": 0.09438654666035054
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.3000552002340555,
      "accuracy": 0.0886566008517228
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 1.6239676922559738,
      "accuracy": 0.07245134896063689
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.21062343753874302,
      "accuracy": 0.03235232728031726
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.3023117482662201,
      "accuracy": 0.012259194395796848
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.4242316372692585,
      "accuracy": 0.00010453690152623876
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2954108292857806,
      "accuracy": 0.001006036217303823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.24337041657418013,
      "accuracy": 0.43781818181818183
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.21290451288223267,
      "accuracy": 0.43498342018000946
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.23304080218076706,
      "accuracy": 0.4271196283391405
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 1.3982210345566273,
      "accuracy": 0.24137549756744803
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.18748673796653748,
      "accuracy": 0.1429764141097892
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.279479693621397,
      "accuracy": 0.0843549328663164
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.3923667725175619,
      "accuracy": 0.03794689525402467
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18344131112098694,
      "eval_loss": 0.26118585218985874,
      "accuracy": 0.06820925553319919
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6666666666666666,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```