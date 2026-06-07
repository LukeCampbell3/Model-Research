# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T17:56:53.391144",
    "run_id": "algo_20260607_175345_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
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
    "train_steps": 1000,
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
        1000
      ],
      "seed_list": [
        42
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
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.06789457891136408,
      "accuracy": 0.8694545454545455
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.08492331812158227,
      "accuracy": 0.7815493790656416
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.06521756621077657,
      "accuracy": 0.8619821912504839
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 1.188930232077837,
      "accuracy": 0.40097174633488736
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.16358677111566067,
      "accuracy": 0.30530882049163394
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.2419213280081749,
      "accuracy": 0.2641509433962264
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.38098048232495785,
      "accuracy": 0.0617501034340091
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.034878071397542953,
      "eval_loss": 0.25057701642314595,
      "accuracy": 0.10653465346534653
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.06350293941795826,
      "accuracy": 0.9179090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.08272757241502404,
      "accuracy": 0.7863985807214666
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.07917519239708781,
      "accuracy": 0.860723964382501
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 1.207721270620823,
      "accuracy": 0.3432286693253946
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.16112761851400137,
      "accuracy": 0.2848585003098533
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.2398893814533949,
      "accuracy": 0.24109014675052412
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.36000750213861465,
      "accuracy": 0.32509309060819197
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 1000,
      "train_loss": 0.027974294498562813,
      "eval_loss": 0.23192078868548074,
      "accuracy": 0.3912871287128713
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```