# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:28:08.502029",
    "run_id": "algo_20260607_182553_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --max-train-seconds 120 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-matched-wall-clock-gate --output-dir evaluation/benchmark_results/pvr_final_matched_wall_clock",
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
      "run_matched_wall_clock_gate": true
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
      "max_train_seconds": 120.0
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
      "eval_loss": 0.21594616118818521,
      "accuracy": 0.49127272727272725
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1755795106291771,
      "accuracy": 0.5577925153955471
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.20173880364745855,
      "accuracy": 0.5481997677119629
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 1.5207750350236893,
      "accuracy": 0.16809486952675806
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1994481198489666,
      "accuracy": 0.08578584846587352
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2926559578627348,
      "accuracy": 0.040863981319322826
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.4141271449625492,
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
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.24352463521063328,
      "accuracy": 0.43536363636363634
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.21351177990436554,
      "accuracy": 0.43439128375177644
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.2334343809634447,
      "accuracy": 0.42421602787456447
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 1.3997729234397411,
      "accuracy": 0.24112671384343212
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.1875239098444581,
      "accuracy": 0.1419327906491338
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.2794491592794657,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.3926179800182581,
      "accuracy": 0.038155969057077146
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18357864022254944,
      "eval_loss": 0.26145026956995326,
      "accuracy": 0.06740442655935613
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6666666666666666,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```