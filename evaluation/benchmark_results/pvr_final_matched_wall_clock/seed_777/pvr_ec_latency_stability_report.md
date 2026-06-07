# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:30:23.402474",
    "run_id": "algo_20260607_182809_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
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
        777
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
      "avg_loss": 0.41424106022653484,
      "avg_accuracy": 0.15306213128950222,
      "avg_train_loss": 0.16213898360729218,
      "latency_p50_ms": 932.1775138378143,
      "latency_p95_ms": 932.1775138378143,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.4450599988146374,
      "avg_accuracy": 0.09719952415064355,
      "avg_train_loss": 0.18943354487419128,
      "latency_p50_ms": 662.4855995178223,
      "latency_p95_ms": 662.4855995178223,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.4195641192685192,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685861349105835,
      "latency_p50_ms": 575.3621757030487,
      "latency_p95_ms": 575.3621757030487,
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
      "latency_p50_ms": 1032.8009128570557,
      "latency_p95_ms": 1032.8009128570557,
      "latency_p99_ms": 1032.8009128570557,
      "latency_max_ms": 1032.8009128570557,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1006.4530372619629,
      "latency_p95_ms": 1006.4530372619629,
      "latency_p99_ms": 1006.4530372619629,
      "latency_max_ms": 1006.4530372619629,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1025.4673957824707,
      "latency_p95_ms": 1025.4673957824707,
      "latency_p99_ms": 1025.4673957824707,
      "latency_max_ms": 1025.4673957824707,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1036.7963314056396,
      "latency_p95_ms": 1036.7963314056396,
      "latency_p99_ms": 1036.7963314056396,
      "latency_max_ms": 1036.7963314056396,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1025.763988494873,
      "latency_p95_ms": 1025.763988494873,
      "latency_p99_ms": 1025.763988494873,
      "latency_max_ms": 1025.763988494873,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 515.3908729553223,
      "latency_p95_ms": 515.3908729553223,
      "latency_p99_ms": 515.3908729553223,
      "latency_max_ms": 515.3908729553223,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1030.90500831604,
      "latency_p95_ms": 1030.90500831604,
      "latency_p99_ms": 1030.90500831604,
      "latency_max_ms": 1030.90500831604,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 783.8425636291504,
      "latency_p95_ms": 783.8425636291504,
      "latency_p99_ms": 783.8425636291504,
      "latency_max_ms": 783.8425636291504,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 721.1272716522217,
      "latency_p95_ms": 721.1272716522217,
      "latency_p99_ms": 721.1272716522217,
      "latency_max_ms": 721.1272716522217,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 716.2742614746094,
      "latency_p95_ms": 716.2742614746094,
      "latency_p99_ms": 716.2742614746094,
      "latency_max_ms": 716.2742614746094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 742.4719333648682,
      "latency_p95_ms": 742.4719333648682,
      "latency_p99_ms": 742.4719333648682,
      "latency_max_ms": 742.4719333648682,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 754.6567916870117,
      "latency_p95_ms": 754.6567916870117,
      "latency_p99_ms": 754.6567916870117,
      "latency_max_ms": 754.6567916870117,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 740.3934001922607,
      "latency_p95_ms": 740.3934001922607,
      "latency_p99_ms": 740.3934001922607,
      "latency_max_ms": 740.3934001922607,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 362.9891872406006,
      "latency_p95_ms": 362.9891872406006,
      "latency_p99_ms": 362.9891872406006,
      "latency_max_ms": 362.9891872406006,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 718.4963226318359,
      "latency_p95_ms": 718.4963226318359,
      "latency_p99_ms": 718.4963226318359,
      "latency_max_ms": 718.4963226318359,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 543.4756278991699,
      "latency_p95_ms": 543.4756278991699,
      "latency_p99_ms": 543.4756278991699,
      "latency_max_ms": 543.4756278991699,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 633.4199905395508,
      "latency_p95_ms": 633.4199905395508,
      "latency_p99_ms": 633.4199905395508,
      "latency_max_ms": 633.4199905395508,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 645.7152366638184,
      "latency_p95_ms": 645.7152366638184,
      "latency_p99_ms": 645.7152366638184,
      "latency_max_ms": 645.7152366638184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 649.5547294616699,
      "latency_p95_ms": 649.5547294616699,
      "latency_p99_ms": 649.5547294616699,
      "latency_max_ms": 649.5547294616699,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 653.5661220550537,
      "latency_p95_ms": 653.5661220550537,
      "latency_p99_ms": 653.5661220550537,
      "latency_max_ms": 653.5661220550537,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 624.2890357971191,
      "latency_p95_ms": 624.2890357971191,
      "latency_p99_ms": 624.2890357971191,
      "latency_max_ms": 624.2890357971191,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.9724426269531,
      "latency_p95_ms": 320.9724426269531,
      "latency_p99_ms": 320.9724426269531,
      "latency_max_ms": 320.9724426269531,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 605.3056716918945,
      "latency_p95_ms": 605.3056716918945,
      "latency_p99_ms": 605.3056716918945,
      "latency_max_ms": 605.3056716918945,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 470.0741767883301,
      "latency_p95_ms": 470.0741767883301,
      "latency_p99_ms": 470.0741767883301,
      "latency_max_ms": 470.0741767883301,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```