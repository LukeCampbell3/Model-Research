# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:21:31.987251",
    "run_id": "algo_20260607_191628_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
        123
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
      "avg_loss": 0.412875771910573,
      "avg_accuracy": 0.2465671708173199,
      "avg_train_loss": 0.15063926577568054,
      "latency_p50_ms": 966.333419084549,
      "latency_p95_ms": 966.333419084549,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.40127988128612435,
      "avg_accuracy": 0.23404695068351358,
      "avg_train_loss": 0.18338394165039062,
      "latency_p50_ms": 603.5023033618927,
      "latency_p95_ms": 603.5023033618927,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.4115613133568937,
      "avg_accuracy": 0.18282003317413148,
      "avg_train_loss": 0.19408826529979706,
      "latency_p50_ms": 605.4846048355103,
      "latency_p95_ms": 605.4846048355103,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.401406412323316,
      "avg_accuracy": 0.2334902667664851,
      "avg_train_loss": 0.18364323675632477,
      "latency_p50_ms": 607.8071892261505,
      "latency_p95_ms": 607.8071892261505,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium": {
      "count": 8,
      "avg_loss": 0.398577261560907,
      "avg_accuracy": 0.213413735155882,
      "avg_train_loss": 0.1846141815185547,
      "latency_p50_ms": 606.421947479248,
      "latency_p95_ms": 606.421947479248,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.39278302170957125,
      "avg_accuracy": 0.24732155355308905,
      "avg_train_loss": 0.17814171314239502,
      "latency_p50_ms": 605.1914989948273,
      "latency_p95_ms": 605.1914989948273,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.41072008661770576,
      "avg_accuracy": 0.19466493546444957,
      "avg_train_loss": 0.1934904307126999,
      "latency_p50_ms": 617.6197230815887,
      "latency_p95_ms": 617.6197230815887,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.41815000923816115,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 598.8970994949341,
      "latency_p95_ms": 598.8970994949341,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.42583591653965414,
      "avg_accuracy": 0.18282003317413148,
      "avg_train_loss": 0.19408826529979706,
      "latency_p50_ms": 596.1752533912659,
      "latency_p95_ms": 596.1752533912659,
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
      "latency_p50_ms": 1084.2154026031494,
      "latency_p95_ms": 1084.2154026031494,
      "latency_p99_ms": 1084.2154026031494,
      "latency_max_ms": 1084.2154026031494,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1070.9271430969238,
      "latency_p95_ms": 1070.9271430969238,
      "latency_p99_ms": 1070.9271430969238,
      "latency_max_ms": 1070.9271430969238,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1073.411226272583,
      "latency_p95_ms": 1073.411226272583,
      "latency_p99_ms": 1073.411226272583,
      "latency_max_ms": 1073.411226272583,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1080.8711051940918,
      "latency_p95_ms": 1080.8711051940918,
      "latency_p99_ms": 1080.8711051940918,
      "latency_max_ms": 1080.8711051940918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1066.9867992401123,
      "latency_p95_ms": 1066.9867992401123,
      "latency_p99_ms": 1066.9867992401123,
      "latency_max_ms": 1066.9867992401123,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 530.5881500244141,
      "latency_p95_ms": 530.5881500244141,
      "latency_p99_ms": 530.5881500244141,
      "latency_max_ms": 530.5881500244141,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1038.8872623443604,
      "latency_p95_ms": 1038.8872623443604,
      "latency_p99_ms": 1038.8872623443604,
      "latency_max_ms": 1038.8872623443604,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 784.7802639007568,
      "latency_p95_ms": 784.7802639007568,
      "latency_p99_ms": 784.7802639007568,
      "latency_max_ms": 784.7802639007568,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.6834659576416,
      "latency_p95_ms": 659.6834659576416,
      "latency_p99_ms": 659.6834659576416,
      "latency_max_ms": 659.6834659576416,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.194013595581,
      "latency_p95_ms": 662.194013595581,
      "latency_p99_ms": 662.194013595581,
      "latency_max_ms": 662.194013595581,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.4088077545166,
      "latency_p95_ms": 659.4088077545166,
      "latency_p99_ms": 659.4088077545166,
      "latency_max_ms": 659.4088077545166,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 680.7913780212402,
      "latency_p95_ms": 680.7913780212402,
      "latency_p99_ms": 680.7913780212402,
      "latency_max_ms": 680.7913780212402,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.7719306945801,
      "latency_p95_ms": 672.7719306945801,
      "latency_p99_ms": 672.7719306945801,
      "latency_max_ms": 672.7719306945801,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 332.5469493865967,
      "latency_p95_ms": 332.5469493865967,
      "latency_p99_ms": 332.5469493865967,
      "latency_max_ms": 332.5469493865967,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 655.0891399383545,
      "latency_p95_ms": 655.0891399383545,
      "latency_p99_ms": 655.0891399383545,
      "latency_max_ms": 655.0891399383545,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 505.53274154663086,
      "latency_p95_ms": 505.53274154663086,
      "latency_p99_ms": 505.53274154663086,
      "latency_max_ms": 505.53274154663086,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.4668064117432,
      "latency_p95_ms": 668.4668064117432,
      "latency_p99_ms": 668.4668064117432,
      "latency_max_ms": 668.4668064117432,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.6802425384521,
      "latency_p95_ms": 664.6802425384521,
      "latency_p99_ms": 664.6802425384521,
      "latency_max_ms": 664.6802425384521,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 656.3615798950195,
      "latency_p95_ms": 656.3615798950195,
      "latency_p99_ms": 656.3615798950195,
      "latency_max_ms": 656.3615798950195,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.2293529510498,
      "latency_p95_ms": 681.2293529510498,
      "latency_p99_ms": 681.2293529510498,
      "latency_max_ms": 681.2293529510498,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.6934280395508,
      "latency_p95_ms": 663.6934280395508,
      "latency_p99_ms": 663.6934280395508,
      "latency_max_ms": 663.6934280395508,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 333.2953453063965,
      "latency_p95_ms": 333.2953453063965,
      "latency_p99_ms": 333.2953453063965,
      "latency_max_ms": 333.2953453063965,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.6996173858643,
      "latency_p95_ms": 673.6996173858643,
      "latency_p99_ms": 673.6996173858643,
      "latency_max_ms": 673.6996173858643,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 502.45046615600586,
      "latency_p95_ms": 502.45046615600586,
      "latency_p99_ms": 502.45046615600586,
      "latency_max_ms": 502.45046615600586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 660.8035564422607,
      "latency_p95_ms": 660.8035564422607,
      "latency_p99_ms": 660.8035564422607,
      "latency_max_ms": 660.8035564422607,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.4424781799316,
      "latency_p95_ms": 678.4424781799316,
      "latency_p99_ms": 678.4424781799316,
      "latency_max_ms": 678.4424781799316,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.1770763397217,
      "latency_p95_ms": 672.1770763397217,
      "latency_p99_ms": 672.1770763397217,
      "latency_max_ms": 672.1770763397217,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.6504001617432,
      "latency_p95_ms": 681.6504001617432,
      "latency_p99_ms": 681.6504001617432,
      "latency_max_ms": 681.6504001617432,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 675.1153469085693,
      "latency_p95_ms": 675.1153469085693,
      "latency_p99_ms": 675.1153469085693,
      "latency_max_ms": 675.1153469085693,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 332.96895027160645,
      "latency_p95_ms": 332.96895027160645,
      "latency_p99_ms": 332.96895027160645,
      "latency_max_ms": 332.96895027160645,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.6221408843994,
      "latency_p95_ms": 663.6221408843994,
      "latency_p99_ms": 663.6221408843994,
      "latency_max_ms": 663.6221408843994,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 497.6775646209717,
      "latency_p95_ms": 497.6775646209717,
      "latency_p99_ms": 497.6775646209717,
      "latency_max_ms": 497.6775646209717,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 653.0628204345703,
      "latency_p95_ms": 653.0628204345703,
      "latency_p99_ms": 653.0628204345703,
      "latency_max_ms": 653.0628204345703,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.4664535522461,
      "latency_p95_ms": 663.4664535522461,
      "latency_p99_ms": 663.4664535522461,
      "latency_max_ms": 663.4664535522461,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.1571521759033,
      "latency_p95_ms": 664.1571521759033,
      "latency_p99_ms": 664.1571521759033,
      "latency_max_ms": 664.1571521759033,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 686.9475841522217,
      "latency_p95_ms": 686.9475841522217,
      "latency_p99_ms": 686.9475841522217,
      "latency_max_ms": 686.9475841522217,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.0620441436768,
      "latency_p95_ms": 667.0620441436768,
      "latency_p99_ms": 667.0620441436768,
      "latency_max_ms": 667.0620441436768,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 337.8713130950928,
      "latency_p95_ms": 337.8713130950928,
      "latency_p99_ms": 337.8713130950928,
      "latency_max_ms": 337.8713130950928,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 680.3109645843506,
      "latency_p95_ms": 680.3109645843506,
      "latency_p99_ms": 680.3109645843506,
      "latency_max_ms": 680.3109645843506,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 498.49724769592285,
      "latency_p95_ms": 498.49724769592285,
      "latency_p99_ms": 498.49724769592285,
      "latency_max_ms": 498.49724769592285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 660.0089073181152,
      "latency_p95_ms": 660.0089073181152,
      "latency_p99_ms": 660.0089073181152,
      "latency_max_ms": 660.0089073181152,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.91969871521,
      "latency_p95_ms": 676.91969871521,
      "latency_p99_ms": 676.91969871521,
      "latency_max_ms": 676.91969871521,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.8241539001465,
      "latency_p95_ms": 662.8241539001465,
      "latency_p99_ms": 662.8241539001465,
      "latency_max_ms": 662.8241539001465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 684.4861507415771,
      "latency_p95_ms": 684.4861507415771,
      "latency_p99_ms": 684.4861507415771,
      "latency_max_ms": 684.4861507415771,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.4041538238525,
      "latency_p95_ms": 664.4041538238525,
      "latency_p99_ms": 664.4041538238525,
      "latency_max_ms": 664.4041538238525,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 335.5753421783447,
      "latency_p95_ms": 335.5753421783447,
      "latency_p99_ms": 335.5753421783447,
      "latency_max_ms": 335.5753421783447,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.3670845031738,
      "latency_p95_ms": 659.3670845031738,
      "latency_p99_ms": 659.3670845031738,
      "latency_max_ms": 659.3670845031738,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 497.94650077819824,
      "latency_p95_ms": 497.94650077819824,
      "latency_p99_ms": 497.94650077819824,
      "latency_max_ms": 497.94650077819824,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 643.2757377624512,
      "latency_p95_ms": 643.2757377624512,
      "latency_p99_ms": 643.2757377624512,
      "latency_max_ms": 643.2757377624512,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 652.0850658416748,
      "latency_p95_ms": 652.0850658416748,
      "latency_p99_ms": 652.0850658416748,
      "latency_max_ms": 652.0850658416748,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 661.109447479248,
      "latency_p95_ms": 661.109447479248,
      "latency_p99_ms": 661.109447479248,
      "latency_max_ms": 661.109447479248,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 702.171802520752,
      "latency_p95_ms": 702.171802520752,
      "latency_p99_ms": 702.171802520752,
      "latency_max_ms": 702.171802520752,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 719.2230224609375,
      "latency_p95_ms": 719.2230224609375,
      "latency_p99_ms": 719.2230224609375,
      "latency_max_ms": 719.2230224609375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 347.03779220581055,
      "latency_p95_ms": 347.03779220581055,
      "latency_p99_ms": 347.03779220581055,
      "latency_max_ms": 347.03779220581055,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 694.5834159851074,
      "latency_p95_ms": 694.5834159851074,
      "latency_p99_ms": 694.5834159851074,
      "latency_max_ms": 694.5834159851074,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 521.4715003967285,
      "latency_p95_ms": 521.4715003967285,
      "latency_p99_ms": 521.4715003967285,
      "latency_max_ms": 521.4715003967285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 642.9100036621094,
      "latency_p95_ms": 642.9100036621094,
      "latency_p99_ms": 642.9100036621094,
      "latency_max_ms": 642.9100036621094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 658.4885120391846,
      "latency_p95_ms": 658.4885120391846,
      "latency_p99_ms": 658.4885120391846,
      "latency_max_ms": 658.4885120391846,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.3444347381592,
      "latency_p95_ms": 659.3444347381592,
      "latency_p99_ms": 659.3444347381592,
      "latency_max_ms": 659.3444347381592,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 670.3610420227051,
      "latency_p95_ms": 670.3610420227051,
      "latency_p99_ms": 670.3610420227051,
      "latency_max_ms": 670.3610420227051,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.6232509613037,
      "latency_p95_ms": 674.6232509613037,
      "latency_p99_ms": 674.6232509613037,
      "latency_max_ms": 674.6232509613037,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 341.2506580352783,
      "latency_p95_ms": 341.2506580352783,
      "latency_p99_ms": 341.2506580352783,
      "latency_max_ms": 341.2506580352783,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 650.0418186187744,
      "latency_p95_ms": 650.0418186187744,
      "latency_p99_ms": 650.0418186187744,
      "latency_max_ms": 650.0418186187744,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 494.157075881958,
      "latency_p95_ms": 494.157075881958,
      "latency_p99_ms": 494.157075881958,
      "latency_max_ms": 494.157075881958,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 648.0576992034912,
      "latency_p95_ms": 648.0576992034912,
      "latency_p99_ms": 648.0576992034912,
      "latency_max_ms": 648.0576992034912,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 652.6401042938232,
      "latency_p95_ms": 652.6401042938232,
      "latency_p99_ms": 652.6401042938232,
      "latency_max_ms": 652.6401042938232,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 647.2129821777344,
      "latency_p95_ms": 647.2129821777344,
      "latency_p99_ms": 647.2129821777344,
      "latency_max_ms": 647.2129821777344,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.6044883728027,
      "latency_p95_ms": 673.6044883728027,
      "latency_p99_ms": 673.6044883728027,
      "latency_max_ms": 673.6044883728027,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.5523986816406,
      "latency_p95_ms": 668.5523986816406,
      "latency_p99_ms": 668.5523986816406,
      "latency_max_ms": 668.5523986816406,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 332.89480209350586,
      "latency_p95_ms": 332.89480209350586,
      "latency_p99_ms": 332.89480209350586,
      "latency_max_ms": 332.89480209350586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 648.705244064331,
      "latency_p95_ms": 648.705244064331,
      "latency_p99_ms": 648.705244064331,
      "latency_max_ms": 648.705244064331,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 497.73430824279785,
      "latency_p95_ms": 497.73430824279785,
      "latency_p99_ms": 497.73430824279785,
      "latency_max_ms": 497.73430824279785,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```