# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:36:35.003255",
    "run_id": "algo_20260607_193140_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 9001,
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
        9001
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
      "avg_loss": 0.43365278929316753,
      "avg_accuracy": 0.09600030596660385,
      "avg_train_loss": 0.21655501425266266,
      "latency_p50_ms": 956.1307430267334,
      "latency_p95_ms": 956.1307430267334,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.37685146322473884,
      "avg_accuracy": 0.335971191900745,
      "avg_train_loss": 0.18353383243083954,
      "latency_p50_ms": 600.0955104827881,
      "latency_p95_ms": 600.0955104827881,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.3945126073279729,
      "avg_accuracy": 0.2544760950092409,
      "avg_train_loss": 0.19993677735328674,
      "latency_p50_ms": 603.4337282180786,
      "latency_p95_ms": 603.4337282180786,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.37685146322473884,
      "avg_accuracy": 0.335971191900745,
      "avg_train_loss": 0.18353383243083954,
      "latency_p50_ms": 602.8076112270355,
      "latency_p95_ms": 602.8076112270355,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium": {
      "count": 8,
      "avg_loss": 0.3740150838081414,
      "avg_accuracy": 0.340325904228385,
      "avg_train_loss": 0.18648390471935272,
      "latency_p50_ms": 603.038489818573,
      "latency_p95_ms": 603.038489818573,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.36942815415871644,
      "avg_accuracy": 0.3393609072972176,
      "avg_train_loss": 0.17750969529151917,
      "latency_p50_ms": 604.9996912479401,
      "latency_p95_ms": 604.9996912479401,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.398964631681641,
      "avg_accuracy": 0.24575428474172203,
      "avg_train_loss": 0.2060525119304657,
      "latency_p50_ms": 599.3112623691559,
      "latency_p95_ms": 599.3112623691559,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.40043345085966087,
      "avg_accuracy": 0.335971191900745,
      "avg_train_loss": 0.18353383243083954,
      "latency_p50_ms": 590.9607112407684,
      "latency_p95_ms": 590.9607112407684,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.4135574370933076,
      "avg_accuracy": 0.2544760950092409,
      "avg_train_loss": 0.19993677735328674,
      "latency_p50_ms": 590.7643437385559,
      "latency_p95_ms": 590.7643437385559,
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
      "latency_p50_ms": 1068.8278675079346,
      "latency_p95_ms": 1068.8278675079346,
      "latency_p99_ms": 1068.8278675079346,
      "latency_max_ms": 1068.8278675079346,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1052.748441696167,
      "latency_p95_ms": 1052.748441696167,
      "latency_p99_ms": 1052.748441696167,
      "latency_max_ms": 1052.748441696167,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1065.037488937378,
      "latency_p95_ms": 1065.037488937378,
      "latency_p99_ms": 1065.037488937378,
      "latency_max_ms": 1065.037488937378,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1077.90207862854,
      "latency_p95_ms": 1077.90207862854,
      "latency_p99_ms": 1077.90207862854,
      "latency_max_ms": 1077.90207862854,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1053.0281066894531,
      "latency_p95_ms": 1053.0281066894531,
      "latency_p99_ms": 1053.0281066894531,
      "latency_max_ms": 1053.0281066894531,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 523.5509872436523,
      "latency_p95_ms": 523.5509872436523,
      "latency_p99_ms": 523.5509872436523,
      "latency_max_ms": 523.5509872436523,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1032.491683959961,
      "latency_p95_ms": 1032.491683959961,
      "latency_p99_ms": 1032.491683959961,
      "latency_max_ms": 1032.491683959961,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 775.4592895507812,
      "latency_p95_ms": 775.4592895507812,
      "latency_p99_ms": 775.4592895507812,
      "latency_max_ms": 775.4592895507812,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.8439846038818,
      "latency_p95_ms": 668.8439846038818,
      "latency_p99_ms": 668.8439846038818,
      "latency_max_ms": 668.8439846038818,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 661.8978977203369,
      "latency_p95_ms": 661.8978977203369,
      "latency_p99_ms": 661.8978977203369,
      "latency_max_ms": 661.8978977203369,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.4520969390869,
      "latency_p95_ms": 667.4520969390869,
      "latency_p99_ms": 667.4520969390869,
      "latency_max_ms": 667.4520969390869,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 679.1946887969971,
      "latency_p95_ms": 679.1946887969971,
      "latency_p99_ms": 679.1946887969971,
      "latency_max_ms": 679.1946887969971,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.5737628936768,
      "latency_p95_ms": 666.5737628936768,
      "latency_p99_ms": 666.5737628936768,
      "latency_max_ms": 666.5737628936768,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 331.2990665435791,
      "latency_p95_ms": 331.2990665435791,
      "latency_p99_ms": 331.2990665435791,
      "latency_max_ms": 331.2990665435791,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 639.4872665405273,
      "latency_p95_ms": 639.4872665405273,
      "latency_p99_ms": 639.4872665405273,
      "latency_max_ms": 639.4872665405273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 486.01531982421875,
      "latency_p95_ms": 486.01531982421875,
      "latency_p99_ms": 486.01531982421875,
      "latency_max_ms": 486.01531982421875,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 675.915002822876,
      "latency_p95_ms": 675.915002822876,
      "latency_p99_ms": 675.915002822876,
      "latency_max_ms": 675.915002822876,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.3604717254639,
      "latency_p95_ms": 668.3604717254639,
      "latency_p99_ms": 668.3604717254639,
      "latency_max_ms": 668.3604717254639,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.5552597045898,
      "latency_p95_ms": 668.5552597045898,
      "latency_p99_ms": 668.5552597045898,
      "latency_max_ms": 668.5552597045898,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.6366024017334,
      "latency_p95_ms": 674.6366024017334,
      "latency_p99_ms": 674.6366024017334,
      "latency_max_ms": 674.6366024017334,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 683.5653781890869,
      "latency_p95_ms": 683.5653781890869,
      "latency_p99_ms": 683.5653781890869,
      "latency_max_ms": 683.5653781890869,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 330.7774066925049,
      "latency_p95_ms": 330.7774066925049,
      "latency_p99_ms": 330.7774066925049,
      "latency_max_ms": 330.7774066925049,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 641.1471366882324,
      "latency_p95_ms": 641.1471366882324,
      "latency_p99_ms": 641.1471366882324,
      "latency_max_ms": 641.1471366882324,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 484.5125675201416,
      "latency_p95_ms": 484.5125675201416,
      "latency_p99_ms": 484.5125675201416,
      "latency_max_ms": 484.5125675201416,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.7276782989502,
      "latency_p95_ms": 674.7276782989502,
      "latency_p99_ms": 674.7276782989502,
      "latency_max_ms": 674.7276782989502,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.3384952545166,
      "latency_p95_ms": 662.3384952545166,
      "latency_p99_ms": 662.3384952545166,
      "latency_max_ms": 662.3384952545166,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.3959445953369,
      "latency_p95_ms": 672.3959445953369,
      "latency_p99_ms": 672.3959445953369,
      "latency_max_ms": 672.3959445953369,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 680.4745197296143,
      "latency_p95_ms": 680.4745197296143,
      "latency_p99_ms": 680.4745197296143,
      "latency_max_ms": 680.4745197296143,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 665.1153564453125,
      "latency_p95_ms": 665.1153564453125,
      "latency_p99_ms": 665.1153564453125,
      "latency_max_ms": 665.1153564453125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 331.1798572540283,
      "latency_p95_ms": 331.1798572540283,
      "latency_p99_ms": 331.1798572540283,
      "latency_max_ms": 331.1798572540283,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 636.5525722503662,
      "latency_p95_ms": 636.5525722503662,
      "latency_p99_ms": 636.5525722503662,
      "latency_max_ms": 636.5525722503662,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 499.6764659881592,
      "latency_p95_ms": 499.6764659881592,
      "latency_p99_ms": 499.6764659881592,
      "latency_max_ms": 499.6764659881592,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.6820468902588,
      "latency_p95_ms": 672.6820468902588,
      "latency_p99_ms": 672.6820468902588,
      "latency_max_ms": 672.6820468902588,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 669.7347164154053,
      "latency_p95_ms": 669.7347164154053,
      "latency_p99_ms": 669.7347164154053,
      "latency_max_ms": 669.7347164154053,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.564920425415,
      "latency_p95_ms": 663.564920425415,
      "latency_p99_ms": 663.564920425415,
      "latency_max_ms": 663.564920425415,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 677.4044036865234,
      "latency_p95_ms": 677.4044036865234,
      "latency_p99_ms": 677.4044036865234,
      "latency_max_ms": 677.4044036865234,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.1468486785889,
      "latency_p95_ms": 668.1468486785889,
      "latency_p99_ms": 668.1468486785889,
      "latency_max_ms": 668.1468486785889,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 329.5786380767822,
      "latency_p95_ms": 329.5786380767822,
      "latency_p99_ms": 329.5786380767822,
      "latency_max_ms": 329.5786380767822,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 648.1144428253174,
      "latency_p95_ms": 648.1144428253174,
      "latency_p99_ms": 648.1144428253174,
      "latency_max_ms": 648.1144428253174,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 495.08190155029297,
      "latency_p95_ms": 495.08190155029297,
      "latency_p99_ms": 495.08190155029297,
      "latency_max_ms": 495.08190155029297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.7984676361084,
      "latency_p95_ms": 671.7984676361084,
      "latency_p99_ms": 671.7984676361084,
      "latency_max_ms": 671.7984676361084,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.9304065704346,
      "latency_p95_ms": 673.9304065704346,
      "latency_p99_ms": 673.9304065704346,
      "latency_max_ms": 673.9304065704346,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.8954315185547,
      "latency_p95_ms": 672.8954315185547,
      "latency_p99_ms": 672.8954315185547,
      "latency_max_ms": 672.8954315185547,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.7127513885498,
      "latency_p95_ms": 676.7127513885498,
      "latency_p99_ms": 676.7127513885498,
      "latency_max_ms": 676.7127513885498,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.6412143707275,
      "latency_p95_ms": 663.6412143707275,
      "latency_p99_ms": 663.6412143707275,
      "latency_max_ms": 663.6412143707275,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.5934829711914,
      "latency_p95_ms": 338.5934829711914,
      "latency_p99_ms": 338.5934829711914,
      "latency_max_ms": 338.5934829711914,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 646.8024253845215,
      "latency_p95_ms": 646.8024253845215,
      "latency_p99_ms": 646.8024253845215,
      "latency_max_ms": 646.8024253845215,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 495.6233501434326,
      "latency_p95_ms": 495.6233501434326,
      "latency_p99_ms": 495.6233501434326,
      "latency_max_ms": 495.6233501434326,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.6835803985596,
      "latency_p95_ms": 664.6835803985596,
      "latency_p99_ms": 664.6835803985596,
      "latency_max_ms": 664.6835803985596,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 655.9736728668213,
      "latency_p95_ms": 655.9736728668213,
      "latency_p99_ms": 655.9736728668213,
      "latency_max_ms": 655.9736728668213,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.5179634094238,
      "latency_p95_ms": 676.5179634094238,
      "latency_p99_ms": 676.5179634094238,
      "latency_max_ms": 676.5179634094238,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 687.4740123748779,
      "latency_p95_ms": 687.4740123748779,
      "latency_p99_ms": 687.4740123748779,
      "latency_max_ms": 687.4740123748779,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 660.4206562042236,
      "latency_p95_ms": 660.4206562042236,
      "latency_p99_ms": 660.4206562042236,
      "latency_max_ms": 660.4206562042236,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 329.3578624725342,
      "latency_p95_ms": 329.3578624725342,
      "latency_p99_ms": 329.3578624725342,
      "latency_max_ms": 329.3578624725342,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 633.307695388794,
      "latency_p95_ms": 633.307695388794,
      "latency_p99_ms": 633.307695388794,
      "latency_max_ms": 633.307695388794,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 486.7546558380127,
      "latency_p95_ms": 486.7546558380127,
      "latency_p99_ms": 486.7546558380127,
      "latency_max_ms": 486.7546558380127,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 651.2067317962646,
      "latency_p95_ms": 651.2067317962646,
      "latency_p99_ms": 651.2067317962646,
      "latency_max_ms": 651.2067317962646,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 655.134916305542,
      "latency_p95_ms": 655.134916305542,
      "latency_p99_ms": 655.134916305542,
      "latency_max_ms": 655.134916305542,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.3815765380859,
      "latency_p95_ms": 663.3815765380859,
      "latency_p99_ms": 663.3815765380859,
      "latency_max_ms": 663.3815765380859,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 667.8049564361572,
      "latency_p95_ms": 667.8049564361572,
      "latency_p99_ms": 667.8049564361572,
      "latency_max_ms": 667.8049564361572,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 649.2393016815186,
      "latency_p95_ms": 649.2393016815186,
      "latency_p99_ms": 649.2393016815186,
      "latency_max_ms": 649.2393016815186,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 326.54285430908203,
      "latency_p95_ms": 326.54285430908203,
      "latency_p99_ms": 326.54285430908203,
      "latency_max_ms": 326.54285430908203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 628.0815601348877,
      "latency_p95_ms": 628.0815601348877,
      "latency_p99_ms": 628.0815601348877,
      "latency_max_ms": 628.0815601348877,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 486.2937927246094,
      "latency_p95_ms": 486.2937927246094,
      "latency_p99_ms": 486.2937927246094,
      "latency_max_ms": 486.2937927246094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 657.9465866088867,
      "latency_p95_ms": 657.9465866088867,
      "latency_p99_ms": 657.9465866088867,
      "latency_max_ms": 657.9465866088867,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 647.8354930877686,
      "latency_p95_ms": 647.8354930877686,
      "latency_p99_ms": 647.8354930877686,
      "latency_max_ms": 647.8354930877686,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 659.064531326294,
      "latency_p95_ms": 659.064531326294,
      "latency_p99_ms": 659.064531326294,
      "latency_max_ms": 659.064531326294,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.5502014160156,
      "latency_p95_ms": 672.5502014160156,
      "latency_p99_ms": 672.5502014160156,
      "latency_max_ms": 672.5502014160156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 650.6316661834717,
      "latency_p95_ms": 650.6316661834717,
      "latency_p99_ms": 650.6316661834717,
      "latency_max_ms": 650.6316661834717,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 326.37524604797363,
      "latency_p95_ms": 326.37524604797363,
      "latency_p99_ms": 326.37524604797363,
      "latency_max_ms": 326.37524604797363,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 630.5067539215088,
      "latency_p95_ms": 630.5067539215088,
      "latency_p99_ms": 630.5067539215088,
      "latency_max_ms": 630.5067539215088,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 481.2042713165283,
      "latency_p95_ms": 481.2042713165283,
      "latency_p99_ms": 481.2042713165283,
      "latency_max_ms": 481.2042713165283,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```