# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:26:31.052139",
    "run_id": "algo_20260607_192132_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-repeatability-repair-sweep --repeatability-repair-variants final_candidate_v1,sparse_ce_0_03_plus_logit_norm_penalty_light,sparse_ce_0_05_plus_logit_norm_penalty_light,sparse_ce_0_05_plus_logit_norm_penalty_medium,sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_05_plus_posthoc_temperature_calibration,sparse_ce_0_03_plus_posthoc_temperature_calibration --output-dir evaluation/benchmark_results/pvr_blocker_repeatability_repair",
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
      "run_repeatability_repair_sweep": true
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
      "max_train_seconds": null,
      "repeatability_repair_variants": [
        "final_candidate_v1",
        "sparse_ce_0_03_plus_logit_norm_penalty_light",
        "sparse_ce_0_05_plus_logit_norm_penalty_light",
        "sparse_ce_0_05_plus_logit_norm_penalty_medium",
        "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_05_plus_posthoc_temperature_calibration",
        "sparse_ce_0_03_plus_posthoc_temperature_calibration"
      ],
      "calibration_repair_variants": []
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
      "avg_loss": 0.41420443988560385,
      "avg_accuracy": 0.15311703218460868,
      "avg_train_loss": 0.162117600440979,
      "latency_p50_ms": 966.8728411197662,
      "latency_p95_ms": 966.8728411197662,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.41956419843093806,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 599.5854139328003,
      "latency_p95_ms": 599.5854139328003,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.45148713956587017,
      "avg_accuracy": 0.07809927543993778,
      "avg_train_loss": 0.1921829879283905,
      "latency_p50_ms": 590.2003347873688,
      "latency_p95_ms": 590.2003347873688,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.4195925988800203,
      "avg_accuracy": 0.2639483046057569,
      "avg_train_loss": 0.16693343222141266,
      "latency_p50_ms": 602.7615070343018,
      "latency_p95_ms": 602.7615070343018,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium": {
      "count": 8,
      "avg_loss": 0.42206634705265367,
      "avg_accuracy": 0.2040425816043523,
      "avg_train_loss": 0.17292451858520508,
      "latency_p50_ms": 600.7533371448517,
      "latency_p95_ms": 600.7533371448517,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.4238082887216782,
      "avg_accuracy": 0.19277533704874447,
      "avg_train_loss": 0.17420437932014465,
      "latency_p50_ms": 597.4246561527252,
      "latency_p95_ms": 597.4246561527252,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.4381992425381517,
      "avg_accuracy": 0.07224812514785445,
      "avg_train_loss": 0.18853318691253662,
      "latency_p50_ms": 590.6816124916077,
      "latency_p95_ms": 590.6816124916077,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.43786912298916525,
      "avg_accuracy": 0.2639483046057569,
      "avg_train_loss": 0.16693344712257385,
      "latency_p50_ms": 595.6334173679352,
      "latency_p95_ms": 595.6334173679352,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.4633988025598228,
      "avg_accuracy": 0.07809927543993778,
      "avg_train_loss": 0.1921829879283905,
      "latency_p50_ms": 584.2557847499847,
      "latency_p95_ms": 584.2557847499847,
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
      "latency_p50_ms": 1076.6949653625488,
      "latency_p95_ms": 1076.6949653625488,
      "latency_p99_ms": 1076.6949653625488,
      "latency_max_ms": 1076.6949653625488,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1044.7609424591064,
      "latency_p95_ms": 1044.7609424591064,
      "latency_p99_ms": 1044.7609424591064,
      "latency_max_ms": 1044.7609424591064,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1069.3693161010742,
      "latency_p95_ms": 1069.3693161010742,
      "latency_p99_ms": 1069.3693161010742,
      "latency_max_ms": 1069.3693161010742,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1074.7950077056885,
      "latency_p95_ms": 1074.7950077056885,
      "latency_p99_ms": 1074.7950077056885,
      "latency_max_ms": 1074.7950077056885,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1072.4120140075684,
      "latency_p95_ms": 1072.4120140075684,
      "latency_p99_ms": 1072.4120140075684,
      "latency_max_ms": 1072.4120140075684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 536.9677543640137,
      "latency_p95_ms": 536.9677543640137,
      "latency_p99_ms": 536.9677543640137,
      "latency_max_ms": 536.9677543640137,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1059.4902038574219,
      "latency_p95_ms": 1059.4902038574219,
      "latency_p99_ms": 1059.4902038574219,
      "latency_max_ms": 1059.4902038574219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 800.492525100708,
      "latency_p95_ms": 800.492525100708,
      "latency_p99_ms": 800.492525100708,
      "latency_max_ms": 800.492525100708,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 658.6999893188477,
      "latency_p95_ms": 658.6999893188477,
      "latency_p99_ms": 658.6999893188477,
      "latency_max_ms": 658.6999893188477,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.4309501647949,
      "latency_p95_ms": 666.4309501647949,
      "latency_p99_ms": 666.4309501647949,
      "latency_max_ms": 666.4309501647949,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.9612350463867,
      "latency_p95_ms": 672.9612350463867,
      "latency_p99_ms": 672.9612350463867,
      "latency_max_ms": 672.9612350463867,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.0234832763672,
      "latency_p95_ms": 676.0234832763672,
      "latency_p99_ms": 676.0234832763672,
      "latency_max_ms": 676.0234832763672,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 665.1194095611572,
      "latency_p95_ms": 665.1194095611572,
      "latency_p99_ms": 665.1194095611572,
      "latency_max_ms": 665.1194095611572,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 330.03807067871094,
      "latency_p95_ms": 330.03807067871094,
      "latency_p99_ms": 330.03807067871094,
      "latency_max_ms": 330.03807067871094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 636.361837387085,
      "latency_p95_ms": 636.361837387085,
      "latency_p99_ms": 636.361837387085,
      "latency_max_ms": 636.361837387085,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 491.04833602905273,
      "latency_p95_ms": 491.04833602905273,
      "latency_p99_ms": 491.04833602905273,
      "latency_max_ms": 491.04833602905273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.4282550811768,
      "latency_p95_ms": 667.4282550811768,
      "latency_p99_ms": 667.4282550811768,
      "latency_max_ms": 667.4282550811768,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.4041023254395,
      "latency_p95_ms": 668.4041023254395,
      "latency_p99_ms": 668.4041023254395,
      "latency_max_ms": 668.4041023254395,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 665.4667854309082,
      "latency_p95_ms": 665.4667854309082,
      "latency_p99_ms": 665.4667854309082,
      "latency_max_ms": 665.4667854309082,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.4916439056396,
      "latency_p95_ms": 674.4916439056396,
      "latency_p99_ms": 674.4916439056396,
      "latency_max_ms": 674.4916439056396,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 631.9248676300049,
      "latency_p95_ms": 631.9248676300049,
      "latency_p99_ms": 631.9248676300049,
      "latency_max_ms": 631.9248676300049,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.65959548950195,
      "latency_p95_ms": 314.65959548950195,
      "latency_p99_ms": 314.65959548950195,
      "latency_max_ms": 314.65959548950195,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 628.211498260498,
      "latency_p95_ms": 628.211498260498,
      "latency_p99_ms": 628.211498260498,
      "latency_max_ms": 628.211498260498,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 471.01593017578125,
      "latency_p95_ms": 471.01593017578125,
      "latency_p99_ms": 471.01593017578125,
      "latency_max_ms": 471.01593017578125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.7537689208984,
      "latency_p95_ms": 666.7537689208984,
      "latency_p99_ms": 666.7537689208984,
      "latency_max_ms": 666.7537689208984,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.2790050506592,
      "latency_p95_ms": 667.2790050506592,
      "latency_p99_ms": 667.2790050506592,
      "latency_max_ms": 667.2790050506592,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 677.626371383667,
      "latency_p95_ms": 677.626371383667,
      "latency_p99_ms": 677.626371383667,
      "latency_max_ms": 677.626371383667,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 684.2641830444336,
      "latency_p95_ms": 684.2641830444336,
      "latency_p99_ms": 684.2641830444336,
      "latency_max_ms": 684.2641830444336,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.9401912689209,
      "latency_p95_ms": 663.9401912689209,
      "latency_p99_ms": 663.9401912689209,
      "latency_max_ms": 663.9401912689209,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 332.5526714324951,
      "latency_p95_ms": 332.5526714324951,
      "latency_p99_ms": 332.5526714324951,
      "latency_max_ms": 332.5526714324951,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 631.4370632171631,
      "latency_p95_ms": 631.4370632171631,
      "latency_p99_ms": 631.4370632171631,
      "latency_max_ms": 631.4370632171631,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 498.23880195617676,
      "latency_p95_ms": 498.23880195617676,
      "latency_p99_ms": 498.23880195617676,
      "latency_max_ms": 498.23880195617676,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.0613803863525,
      "latency_p95_ms": 663.0613803863525,
      "latency_p99_ms": 663.0613803863525,
      "latency_max_ms": 663.0613803863525,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.5585460662842,
      "latency_p95_ms": 672.5585460662842,
      "latency_p99_ms": 672.5585460662842,
      "latency_max_ms": 672.5585460662842,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 670.3305244445801,
      "latency_p95_ms": 670.3305244445801,
      "latency_p99_ms": 670.3305244445801,
      "latency_max_ms": 670.3305244445801,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.7377853393555,
      "latency_p95_ms": 676.7377853393555,
      "latency_p99_ms": 676.7377853393555,
      "latency_max_ms": 676.7377853393555,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 653.0959606170654,
      "latency_p95_ms": 653.0959606170654,
      "latency_p99_ms": 653.0959606170654,
      "latency_max_ms": 653.0959606170654,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 329.9059867858887,
      "latency_p95_ms": 329.9059867858887,
      "latency_p99_ms": 329.9059867858887,
      "latency_max_ms": 329.9059867858887,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 647.3140716552734,
      "latency_p95_ms": 647.3140716552734,
      "latency_p99_ms": 647.3140716552734,
      "latency_max_ms": 647.3140716552734,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 493.0224418640137,
      "latency_p95_ms": 493.0224418640137,
      "latency_p99_ms": 493.0224418640137,
      "latency_max_ms": 493.0224418640137,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.1269969940186,
      "latency_p95_ms": 659.1269969940186,
      "latency_p99_ms": 659.1269969940186,
      "latency_max_ms": 659.1269969940186,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.1181144714355,
      "latency_p95_ms": 673.1181144714355,
      "latency_p99_ms": 673.1181144714355,
      "latency_max_ms": 673.1181144714355,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.2486534118652,
      "latency_p95_ms": 668.2486534118652,
      "latency_p99_ms": 668.2486534118652,
      "latency_max_ms": 668.2486534118652,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.0514297485352,
      "latency_p95_ms": 672.0514297485352,
      "latency_p99_ms": 672.0514297485352,
      "latency_max_ms": 672.0514297485352,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 643.5611248016357,
      "latency_p95_ms": 643.5611248016357,
      "latency_p99_ms": 643.5611248016357,
      "latency_max_ms": 643.5611248016357,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 331.6493034362793,
      "latency_p95_ms": 331.6493034362793,
      "latency_p99_ms": 331.6493034362793,
      "latency_max_ms": 331.6493034362793,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 638.634204864502,
      "latency_p95_ms": 638.634204864502,
      "latency_p99_ms": 638.634204864502,
      "latency_max_ms": 638.634204864502,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 493.0074214935303,
      "latency_p95_ms": 493.0074214935303,
      "latency_p99_ms": 493.0074214935303,
      "latency_max_ms": 493.0074214935303,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 670.3891754150391,
      "latency_p95_ms": 670.3891754150391,
      "latency_p99_ms": 670.3891754150391,
      "latency_max_ms": 670.3891754150391,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 661.4513397216797,
      "latency_p95_ms": 661.4513397216797,
      "latency_p99_ms": 661.4513397216797,
      "latency_max_ms": 661.4513397216797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.7885055541992,
      "latency_p95_ms": 667.7885055541992,
      "latency_p99_ms": 667.7885055541992,
      "latency_max_ms": 667.7885055541992,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 675.1441955566406,
      "latency_p95_ms": 675.1441955566406,
      "latency_p99_ms": 675.1441955566406,
      "latency_max_ms": 675.1441955566406,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 633.2943439483643,
      "latency_p95_ms": 633.2943439483643,
      "latency_p99_ms": 633.2943439483643,
      "latency_max_ms": 633.2943439483643,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.6158199310303,
      "latency_p95_ms": 316.6158199310303,
      "latency_p99_ms": 316.6158199310303,
      "latency_max_ms": 316.6158199310303,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 631.1039924621582,
      "latency_p95_ms": 631.1039924621582,
      "latency_p99_ms": 631.1039924621582,
      "latency_max_ms": 631.1039924621582,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 469.66552734375,
      "latency_p95_ms": 469.66552734375,
      "latency_p99_ms": 469.66552734375,
      "latency_max_ms": 469.66552734375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.5244102478027,
      "latency_p95_ms": 666.5244102478027,
      "latency_p99_ms": 666.5244102478027,
      "latency_max_ms": 666.5244102478027,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.692361831665,
      "latency_p95_ms": 681.692361831665,
      "latency_p99_ms": 681.692361831665,
      "latency_max_ms": 681.692361831665,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.7852916717529,
      "latency_p95_ms": 662.7852916717529,
      "latency_p99_ms": 662.7852916717529,
      "latency_max_ms": 662.7852916717529,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 669.5756912231445,
      "latency_p95_ms": 669.5756912231445,
      "latency_p99_ms": 669.5756912231445,
      "latency_max_ms": 669.5756912231445,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 654.4163227081299,
      "latency_p95_ms": 654.4163227081299,
      "latency_p99_ms": 654.4163227081299,
      "latency_max_ms": 654.4163227081299,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.1439380645752,
      "latency_p95_ms": 320.1439380645752,
      "latency_p99_ms": 320.1439380645752,
      "latency_max_ms": 320.1439380645752,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 632.7030658721924,
      "latency_p95_ms": 632.7030658721924,
      "latency_p99_ms": 632.7030658721924,
      "latency_max_ms": 632.7030658721924,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 477.22625732421875,
      "latency_p95_ms": 477.22625732421875,
      "latency_p99_ms": 477.22625732421875,
      "latency_max_ms": 477.22625732421875,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 655.236005783081,
      "latency_p95_ms": 655.236005783081,
      "latency_p99_ms": 655.236005783081,
      "latency_max_ms": 655.236005783081,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 654.2203426361084,
      "latency_p95_ms": 654.2203426361084,
      "latency_p99_ms": 654.2203426361084,
      "latency_max_ms": 654.2203426361084,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.9752597808838,
      "latency_p95_ms": 666.9752597808838,
      "latency_p99_ms": 666.9752597808838,
      "latency_max_ms": 666.9752597808838,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.0229225158691,
      "latency_p95_ms": 664.0229225158691,
      "latency_p99_ms": 664.0229225158691,
      "latency_max_ms": 664.0229225158691,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 624.8118877410889,
      "latency_p95_ms": 624.8118877410889,
      "latency_p99_ms": 624.8118877410889,
      "latency_max_ms": 624.8118877410889,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.178747177124,
      "latency_p95_ms": 320.178747177124,
      "latency_p99_ms": 320.178747177124,
      "latency_max_ms": 320.178747177124,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 620.7573413848877,
      "latency_p95_ms": 620.7573413848877,
      "latency_p99_ms": 620.7573413848877,
      "latency_max_ms": 620.7573413848877,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 467.84377098083496,
      "latency_p95_ms": 467.84377098083496,
      "latency_p99_ms": 467.84377098083496,
      "latency_max_ms": 467.84377098083496,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```