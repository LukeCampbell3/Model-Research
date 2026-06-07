# PVR-EC Latency Stability Report

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
  "by_model": {
    "fixed_moe_vectorized": {
      "count": 8,
      "avg_loss": 0.4128779768167684,
      "avg_accuracy": 0.2465923217227525,
      "avg_train_loss": 0.15063753724098206,
      "latency_p50_ms": 921.2344288825989,
      "latency_p95_ms": 921.2344288825989,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.46422695667327696,
      "avg_accuracy": 0.05611798299936589,
      "avg_train_loss": 0.2083549052476883,
      "latency_p50_ms": 660.0803434848785,
      "latency_p95_ms": 660.0803434848785,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.40141062977878994,
      "avg_accuracy": 0.23333173692305506,
      "avg_train_loss": 0.18357864022254944,
      "latency_p50_ms": 576.4380097389221,
      "latency_p95_ms": 576.4380097389221,
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
      "latency_p50_ms": 1017.0116424560547,
      "latency_p95_ms": 1017.0116424560547,
      "latency_p99_ms": 1017.0116424560547,
      "latency_max_ms": 1017.0116424560547,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1016.9167518615723,
      "latency_p95_ms": 1016.9167518615723,
      "latency_p99_ms": 1016.9167518615723,
      "latency_max_ms": 1016.9167518615723,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1028.0284881591797,
      "latency_p95_ms": 1028.0284881591797,
      "latency_p99_ms": 1028.0284881591797,
      "latency_max_ms": 1028.0284881591797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1032.6833724975586,
      "latency_p95_ms": 1032.6833724975586,
      "latency_p99_ms": 1032.6833724975586,
      "latency_max_ms": 1032.6833724975586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1018.6548233032227,
      "latency_p95_ms": 1018.6548233032227,
      "latency_p99_ms": 1018.6548233032227,
      "latency_max_ms": 1018.6548233032227,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 507.0185661315918,
      "latency_p95_ms": 507.0185661315918,
      "latency_p99_ms": 507.0185661315918,
      "latency_max_ms": 507.0185661315918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 995.7473278045654,
      "latency_p95_ms": 995.7473278045654,
      "latency_p99_ms": 995.7473278045654,
      "latency_max_ms": 995.7473278045654,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 753.8144588470459,
      "latency_p95_ms": 753.8144588470459,
      "latency_p99_ms": 753.8144588470459,
      "latency_max_ms": 753.8144588470459,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 717.2958850860596,
      "latency_p95_ms": 717.2958850860596,
      "latency_p99_ms": 717.2958850860596,
      "latency_max_ms": 717.2958850860596,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 791.1758422851562,
      "latency_p95_ms": 791.1758422851562,
      "latency_p99_ms": 791.1758422851562,
      "latency_max_ms": 791.1758422851562,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 742.8781986236572,
      "latency_p95_ms": 742.8781986236572,
      "latency_p99_ms": 742.8781986236572,
      "latency_max_ms": 742.8781986236572,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 744.6520328521729,
      "latency_p95_ms": 744.6520328521729,
      "latency_p99_ms": 744.6520328521729,
      "latency_max_ms": 744.6520328521729,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 712.043285369873,
      "latency_p95_ms": 712.043285369873,
      "latency_p99_ms": 712.043285369873,
      "latency_max_ms": 712.043285369873,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 351.96614265441895,
      "latency_p95_ms": 351.96614265441895,
      "latency_p99_ms": 351.96614265441895,
      "latency_max_ms": 351.96614265441895,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 695.192813873291,
      "latency_p95_ms": 695.192813873291,
      "latency_p99_ms": 695.192813873291,
      "latency_max_ms": 695.192813873291,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 525.4385471343994,
      "latency_p95_ms": 525.4385471343994,
      "latency_p99_ms": 525.4385471343994,
      "latency_max_ms": 525.4385471343994,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 625.6613731384277,
      "latency_p95_ms": 625.6613731384277,
      "latency_p99_ms": 625.6613731384277,
      "latency_max_ms": 625.6613731384277,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 635.4291439056396,
      "latency_p95_ms": 635.4291439056396,
      "latency_p99_ms": 635.4291439056396,
      "latency_max_ms": 635.4291439056396,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.6096477508545,
      "latency_p95_ms": 638.6096477508545,
      "latency_p99_ms": 638.6096477508545,
      "latency_max_ms": 638.6096477508545,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 652.5187492370605,
      "latency_p95_ms": 652.5187492370605,
      "latency_p99_ms": 652.5187492370605,
      "latency_max_ms": 652.5187492370605,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.0388736724854,
      "latency_p95_ms": 638.0388736724854,
      "latency_p99_ms": 638.0388736724854,
      "latency_max_ms": 638.0388736724854,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.6310272216797,
      "latency_p95_ms": 320.6310272216797,
      "latency_p99_ms": 320.6310272216797,
      "latency_max_ms": 320.6310272216797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 621.4339733123779,
      "latency_p95_ms": 621.4339733123779,
      "latency_p99_ms": 621.4339733123779,
      "latency_max_ms": 621.4339733123779,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 479.18128967285156,
      "latency_p95_ms": 479.18128967285156,
      "latency_p99_ms": 479.18128967285156,
      "latency_max_ms": 479.18128967285156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```