# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:59:12.495382",
    "run_id": "algo_20260607_235417_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-minimax-candidate-selection --minimax-variants v1,v1_1_logit_norm_medium,sparse_ce_0_03_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_medium,sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_03_plus_temperature_T_1_2,sparse_ce_0_05_plus_temperature_T_1_2 --output-dir evaluation/benchmark_results/pvr_minimax_candidate_selection",
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
      "dyck",
      "listops",
      "scan"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_minimax_candidate_selection": true
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
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [
        "v1",
        "v1_1_logit_norm_medium",
        "sparse_ce_0_03_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_medium",
        "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_03_plus_temperature_T_1_2",
        "sparse_ce_0_05_plus_temperature_T_1_2"
      ],
      "stability_repair_variants": []
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
      "latency_p50_ms": 798.6502349376678,
      "latency_p95_ms": 798.6502349376678,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.4450599988146374,
      "avg_accuracy": 0.09719952415064355,
      "avg_train_loss": 0.18943354487419128,
      "latency_p50_ms": 321.5804994106293,
      "latency_p95_ms": 321.5804994106293,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1": {
      "count": 8,
      "avg_loss": 0.41956419843093806,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 278.9299786090851,
      "latency_p95_ms": 278.9299786090851,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.42206617549527436,
      "avg_accuracy": 0.2034342468683426,
      "avg_train_loss": 0.17292802035808563,
      "latency_p50_ms": 275.6232023239136,
      "latency_p95_ms": 275.6232023239136,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.45148713956587017,
      "avg_accuracy": 0.07809927543993778,
      "avg_train_loss": 0.1921829879283905,
      "latency_p50_ms": 268.79608631134033,
      "latency_p95_ms": 268.79608631134033,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.41956419843093806,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 276.82358026504517,
      "latency_p95_ms": 276.82358026504517,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.42206617549527436,
      "avg_accuracy": 0.2034342468683426,
      "avg_train_loss": 0.17292802035808563,
      "latency_p50_ms": 276.42855048179626,
      "latency_p95_ms": 276.42855048179626,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.4381992425381517,
      "avg_accuracy": 0.07224812514785445,
      "avg_train_loss": 0.18853318691253662,
      "latency_p50_ms": 268.68003606796265,
      "latency_p95_ms": 268.68003606796265,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.4238082887216782,
      "avg_accuracy": 0.19277533704874447,
      "avg_train_loss": 0.17420437932014465,
      "latency_p50_ms": 272.0881998538971,
      "latency_p95_ms": 272.0881998538971,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.4633988025598228,
      "avg_accuracy": 0.07809927543993778,
      "avg_train_loss": 0.1921829879283905,
      "latency_p50_ms": 260.8579099178314,
      "latency_p95_ms": 260.8579099178314,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.43784711696207523,
      "avg_accuracy": 0.2635769454047967,
      "avg_train_loss": 0.16685862839221954,
      "latency_p50_ms": 266.51743054389954,
      "latency_p95_ms": 266.51743054389954,
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
      "latency_p50_ms": 881.084680557251,
      "latency_p95_ms": 881.084680557251,
      "latency_p99_ms": 881.084680557251,
      "latency_max_ms": 881.084680557251,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 863.8427257537842,
      "latency_p95_ms": 863.8427257537842,
      "latency_p99_ms": 863.8427257537842,
      "latency_max_ms": 863.8427257537842,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 886.4991664886475,
      "latency_p95_ms": 886.4991664886475,
      "latency_p99_ms": 886.4991664886475,
      "latency_max_ms": 886.4991664886475,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 886.2943649291992,
      "latency_p95_ms": 886.2943649291992,
      "latency_p99_ms": 886.2943649291992,
      "latency_max_ms": 886.2943649291992,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 886.162281036377,
      "latency_p95_ms": 886.162281036377,
      "latency_p99_ms": 886.162281036377,
      "latency_max_ms": 886.162281036377,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 441.4246082305908,
      "latency_p95_ms": 441.4246082305908,
      "latency_p99_ms": 441.4246082305908,
      "latency_max_ms": 441.4246082305908,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 879.8980712890625,
      "latency_p95_ms": 879.8980712890625,
      "latency_p99_ms": 879.8980712890625,
      "latency_max_ms": 879.8980712890625,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.9959812164307,
      "latency_p95_ms": 663.9959812164307,
      "latency_p99_ms": 663.9959812164307,
      "latency_max_ms": 663.9959812164307,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 353.5459041595459,
      "latency_p95_ms": 353.5459041595459,
      "latency_p99_ms": 353.5459041595459,
      "latency_max_ms": 353.5459041595459,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 341.9175148010254,
      "latency_p95_ms": 341.9175148010254,
      "latency_p99_ms": 341.9175148010254,
      "latency_max_ms": 341.9175148010254,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 356.87828063964844,
      "latency_p95_ms": 356.87828063964844,
      "latency_p99_ms": 356.87828063964844,
      "latency_max_ms": 356.87828063964844,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 372.1022605895996,
      "latency_p95_ms": 372.1022605895996,
      "latency_p99_ms": 372.1022605895996,
      "latency_max_ms": 372.1022605895996,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 355.9730052947998,
      "latency_p95_ms": 355.9730052947998,
      "latency_p99_ms": 355.9730052947998,
      "latency_max_ms": 355.9730052947998,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 179.71086502075195,
      "latency_p95_ms": 179.71086502075195,
      "latency_p99_ms": 179.71086502075195,
      "latency_max_ms": 179.71086502075195,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 345.11852264404297,
      "latency_p95_ms": 345.11852264404297,
      "latency_p99_ms": 345.11852264404297,
      "latency_max_ms": 345.11852264404297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 267.3976421356201,
      "latency_p95_ms": 267.3976421356201,
      "latency_p99_ms": 267.3976421356201,
      "latency_max_ms": 267.3976421356201,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.365779876709,
      "latency_p95_ms": 302.365779876709,
      "latency_p99_ms": 302.365779876709,
      "latency_max_ms": 302.365779876709,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.99040603637695,
      "latency_p95_ms": 309.99040603637695,
      "latency_p99_ms": 309.99040603637695,
      "latency_max_ms": 309.99040603637695,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.61123847961426,
      "latency_p95_ms": 320.61123847961426,
      "latency_p99_ms": 320.61123847961426,
      "latency_max_ms": 320.61123847961426,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 319.38672065734863,
      "latency_p95_ms": 319.38672065734863,
      "latency_p99_ms": 319.38672065734863,
      "latency_max_ms": 319.38672065734863,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.63204193115234,
      "latency_p95_ms": 306.63204193115234,
      "latency_p99_ms": 306.63204193115234,
      "latency_max_ms": 306.63204193115234,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 154.80875968933105,
      "latency_p95_ms": 154.80875968933105,
      "latency_p99_ms": 154.80875968933105,
      "latency_max_ms": 154.80875968933105,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 288.27691078186035,
      "latency_p95_ms": 288.27691078186035,
      "latency_p99_ms": 288.27691078186035,
      "latency_max_ms": 288.27691078186035,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 229.3679714202881,
      "latency_p95_ms": 229.3679714202881,
      "latency_p99_ms": 229.3679714202881,
      "latency_max_ms": 229.3679714202881,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.42855644226074,
      "latency_p95_ms": 301.42855644226074,
      "latency_p99_ms": 301.42855644226074,
      "latency_max_ms": 301.42855644226074,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.709020614624,
      "latency_p95_ms": 313.709020614624,
      "latency_p99_ms": 313.709020614624,
      "latency_max_ms": 313.709020614624,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.4933967590332,
      "latency_p95_ms": 311.4933967590332,
      "latency_p99_ms": 311.4933967590332,
      "latency_max_ms": 311.4933967590332,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.906286239624,
      "latency_p95_ms": 315.906286239624,
      "latency_p99_ms": 315.906286239624,
      "latency_max_ms": 315.906286239624,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 297.041654586792,
      "latency_p95_ms": 297.041654586792,
      "latency_p99_ms": 297.041654586792,
      "latency_max_ms": 297.041654586792,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 156.61168098449707,
      "latency_p95_ms": 156.61168098449707,
      "latency_p99_ms": 156.61168098449707,
      "latency_max_ms": 156.61168098449707,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 285.64953804016113,
      "latency_p95_ms": 285.64953804016113,
      "latency_p99_ms": 285.64953804016113,
      "latency_max_ms": 285.64953804016113,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 223.1454849243164,
      "latency_p95_ms": 223.1454849243164,
      "latency_p99_ms": 223.1454849243164,
      "latency_max_ms": 223.1454849243164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 303.1425476074219,
      "latency_p95_ms": 303.1425476074219,
      "latency_p99_ms": 303.1425476074219,
      "latency_max_ms": 303.1425476074219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.9452934265137,
      "latency_p95_ms": 313.9452934265137,
      "latency_p99_ms": 313.9452934265137,
      "latency_max_ms": 313.9452934265137,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.0394058227539,
      "latency_p95_ms": 305.0394058227539,
      "latency_p99_ms": 305.0394058227539,
      "latency_max_ms": 305.0394058227539,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 318.9072608947754,
      "latency_p95_ms": 318.9072608947754,
      "latency_p99_ms": 318.9072608947754,
      "latency_max_ms": 318.9072608947754,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 282.1497917175293,
      "latency_p95_ms": 282.1497917175293,
      "latency_p99_ms": 282.1497917175293,
      "latency_max_ms": 282.1497917175293,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 144.6225643157959,
      "latency_p95_ms": 144.6225643157959,
      "latency_p99_ms": 144.6225643157959,
      "latency_max_ms": 144.6225643157959,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 273.33807945251465,
      "latency_p95_ms": 273.33807945251465,
      "latency_p99_ms": 273.33807945251465,
      "latency_max_ms": 273.33807945251465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 209.22374725341797,
      "latency_p95_ms": 209.22374725341797,
      "latency_p99_ms": 209.22374725341797,
      "latency_max_ms": 209.22374725341797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.6039810180664,
      "latency_p95_ms": 305.6039810180664,
      "latency_p99_ms": 305.6039810180664,
      "latency_max_ms": 305.6039810180664,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.7467842102051,
      "latency_p95_ms": 315.7467842102051,
      "latency_p99_ms": 315.7467842102051,
      "latency_max_ms": 315.7467842102051,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.8841438293457,
      "latency_p95_ms": 308.8841438293457,
      "latency_p99_ms": 308.8841438293457,
      "latency_max_ms": 308.8841438293457,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.38231468200684,
      "latency_p95_ms": 314.38231468200684,
      "latency_p99_ms": 314.38231468200684,
      "latency_max_ms": 314.38231468200684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.2992820739746,
      "latency_p95_ms": 305.2992820739746,
      "latency_p99_ms": 305.2992820739746,
      "latency_max_ms": 305.2992820739746,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 153.06448936462402,
      "latency_p95_ms": 153.06448936462402,
      "latency_p99_ms": 153.06448936462402,
      "latency_max_ms": 153.06448936462402,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 286.1137390136719,
      "latency_p95_ms": 286.1137390136719,
      "latency_p99_ms": 286.1137390136719,
      "latency_max_ms": 286.1137390136719,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 225.4939079284668,
      "latency_p95_ms": 225.4939079284668,
      "latency_p99_ms": 225.4939079284668,
      "latency_max_ms": 225.4939079284668,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.57225036621094,
      "latency_p95_ms": 302.57225036621094,
      "latency_p99_ms": 302.57225036621094,
      "latency_max_ms": 302.57225036621094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.0442371368408,
      "latency_p95_ms": 314.0442371368408,
      "latency_p99_ms": 314.0442371368408,
      "latency_max_ms": 314.0442371368408,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.3667964935303,
      "latency_p95_ms": 311.3667964935303,
      "latency_p99_ms": 311.3667964935303,
      "latency_max_ms": 311.3667964935303,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 327.6858329772949,
      "latency_p95_ms": 327.6858329772949,
      "latency_p99_ms": 327.6858329772949,
      "latency_max_ms": 327.6858329772949,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 300.1072406768799,
      "latency_p95_ms": 300.1072406768799,
      "latency_p99_ms": 300.1072406768799,
      "latency_max_ms": 300.1072406768799,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 148.17023277282715,
      "latency_p95_ms": 148.17023277282715,
      "latency_p99_ms": 148.17023277282715,
      "latency_max_ms": 148.17023277282715,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 283.245325088501,
      "latency_p95_ms": 283.245325088501,
      "latency_p99_ms": 283.245325088501,
      "latency_max_ms": 283.245325088501,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 224.23648834228516,
      "latency_p95_ms": 224.23648834228516,
      "latency_p99_ms": 224.23648834228516,
      "latency_max_ms": 224.23648834228516,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.77008628845215,
      "latency_p95_ms": 306.77008628845215,
      "latency_p99_ms": 306.77008628845215,
      "latency_max_ms": 306.77008628845215,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.6400032043457,
      "latency_p95_ms": 308.6400032043457,
      "latency_p99_ms": 308.6400032043457,
      "latency_max_ms": 308.6400032043457,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 307.422399520874,
      "latency_p95_ms": 307.422399520874,
      "latency_p99_ms": 307.422399520874,
      "latency_max_ms": 307.422399520874,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.2002353668213,
      "latency_p95_ms": 313.2002353668213,
      "latency_p99_ms": 313.2002353668213,
      "latency_max_ms": 313.2002353668213,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 282.4883460998535,
      "latency_p95_ms": 282.4883460998535,
      "latency_p99_ms": 282.4883460998535,
      "latency_max_ms": 282.4883460998535,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 142.75860786437988,
      "latency_p95_ms": 142.75860786437988,
      "latency_p99_ms": 142.75860786437988,
      "latency_max_ms": 142.75860786437988,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 277.66871452331543,
      "latency_p95_ms": 277.66871452331543,
      "latency_p99_ms": 277.66871452331543,
      "latency_max_ms": 277.66871452331543,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 210.49189567565918,
      "latency_p95_ms": 210.49189567565918,
      "latency_p99_ms": 210.49189567565918,
      "latency_max_ms": 210.49189567565918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 299.76415634155273,
      "latency_p95_ms": 299.76415634155273,
      "latency_p99_ms": 299.76415634155273,
      "latency_max_ms": 299.76415634155273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.9769821166992,
      "latency_p95_ms": 310.9769821166992,
      "latency_p99_ms": 310.9769821166992,
      "latency_max_ms": 310.9769821166992,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.24780464172363,
      "latency_p95_ms": 308.24780464172363,
      "latency_p99_ms": 308.24780464172363,
      "latency_max_ms": 308.24780464172363,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.5888366699219,
      "latency_p95_ms": 310.5888366699219,
      "latency_p99_ms": 310.5888366699219,
      "latency_max_ms": 310.5888366699219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 291.1372184753418,
      "latency_p95_ms": 291.1372184753418,
      "latency_p99_ms": 291.1372184753418,
      "latency_max_ms": 291.1372184753418,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 149.9612331390381,
      "latency_p95_ms": 149.9612331390381,
      "latency_p99_ms": 149.9612331390381,
      "latency_max_ms": 149.9612331390381,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 284.20567512512207,
      "latency_p95_ms": 284.20567512512207,
      "latency_p99_ms": 284.20567512512207,
      "latency_max_ms": 284.20567512512207,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 221.82369232177734,
      "latency_p95_ms": 221.82369232177734,
      "latency_p99_ms": 221.82369232177734,
      "latency_max_ms": 221.82369232177734,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 293.9777374267578,
      "latency_p95_ms": 293.9777374267578,
      "latency_p99_ms": 293.9777374267578,
      "latency_max_ms": 293.9777374267578,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 294.3263053894043,
      "latency_p95_ms": 294.3263053894043,
      "latency_p99_ms": 294.3263053894043,
      "latency_max_ms": 294.3263053894043,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 295.8836555480957,
      "latency_p95_ms": 295.8836555480957,
      "latency_p99_ms": 295.8836555480957,
      "latency_max_ms": 295.8836555480957,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.3739585876465,
      "latency_p95_ms": 301.3739585876465,
      "latency_p99_ms": 301.3739585876465,
      "latency_max_ms": 301.3739585876465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 273.5419273376465,
      "latency_p95_ms": 273.5419273376465,
      "latency_p99_ms": 273.5419273376465,
      "latency_max_ms": 273.5419273376465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 139.64438438415527,
      "latency_p95_ms": 139.64438438415527,
      "latency_p99_ms": 139.64438438415527,
      "latency_max_ms": 139.64438438415527,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 275.5861282348633,
      "latency_p95_ms": 275.5861282348633,
      "latency_p99_ms": 275.5861282348633,
      "latency_max_ms": 275.5861282348633,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 212.52918243408203,
      "latency_p95_ms": 212.52918243408203,
      "latency_p99_ms": 212.52918243408203,
      "latency_max_ms": 212.52918243408203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 290.26174545288086,
      "latency_p95_ms": 290.26174545288086,
      "latency_p99_ms": 290.26174545288086,
      "latency_max_ms": 290.26174545288086,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.61756134033203,
      "latency_p95_ms": 315.61756134033203,
      "latency_p99_ms": 315.61756134033203,
      "latency_max_ms": 315.61756134033203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 298.2358932495117,
      "latency_p95_ms": 298.2358932495117,
      "latency_p99_ms": 298.2358932495117,
      "latency_max_ms": 298.2358932495117,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.5146255493164,
      "latency_p95_ms": 301.5146255493164,
      "latency_p99_ms": 301.5146255493164,
      "latency_max_ms": 301.5146255493164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 290.32278060913086,
      "latency_p95_ms": 290.32278060913086,
      "latency_p99_ms": 290.32278060913086,
      "latency_max_ms": 290.32278060913086,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 143.53036880493164,
      "latency_p95_ms": 143.53036880493164,
      "latency_p99_ms": 143.53036880493164,
      "latency_max_ms": 143.53036880493164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 276.12996101379395,
      "latency_p95_ms": 276.12996101379395,
      "latency_p99_ms": 276.12996101379395,
      "latency_max_ms": 276.12996101379395,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 216.52650833129883,
      "latency_p95_ms": 216.52650833129883,
      "latency_p99_ms": 216.52650833129883,
      "latency_max_ms": 216.52650833129883,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```