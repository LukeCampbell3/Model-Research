# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:53:44.402988",
    "run_id": "algo_20260607_175204_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps-list 500,1000,2000 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-longer-training-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_longer_training_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
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
      "run_longer_training_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        777
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
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.25702635291963816,
      "accuracy": 0.2720909090909091
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.2398307528346777,
      "accuracy": 0.19011002011120312
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.24611769802868366,
      "accuracy": 0.3308168795973674
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 1.4206876046955585,
      "accuracy": 0.18241412937479684
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.1956030959263444,
      "accuracy": 0.09416473562249841
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.28213198482990265,
      "accuracy": 0.05716851242143071
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.4017317108809948,
      "accuracy": 0.019055684946008893
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.27079928169647854,
      "accuracy": 0.0786761791518034
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21892981510609388,
      "accuracy": 0.5381818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21400899160653353,
      "accuracy": 0.4650419969241689
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21387974172830582,
      "accuracy": 0.490418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 1.5707997642457485,
      "accuracy": 0.18249539495069889
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.1930565619841218,
      "accuracy": 0.13440067410996417
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2756177671253681,
      "accuracy": 0.10865010475905418
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.39493958465754986,
      "accuracy": 0.08003387677323735
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2752813609937827,
      "accuracy": 0.10939357907253269
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```