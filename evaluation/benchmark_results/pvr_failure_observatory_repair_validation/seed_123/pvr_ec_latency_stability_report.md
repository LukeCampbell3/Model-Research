# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T03:39:13.916468",
    "run_id": "algo_20260608_033606_benchmark-lite",
    "git_commit": "c214633e8dfb56a3ba797333eee2da2c985b17cd",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --run-pvr-failure-repair-validation --repair-candidates family_balanced_sampling,logit_norm_cap_light,wrong_suppress_0_01,posthoc_temperature_T_1_2,qpm_runtime_hygiene --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --output-dir evaluation/benchmark_results/pvr_failure_observatory_repair_validation",
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
      "run_stability_repair_sweep": true
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
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [],
      "stability_repair_variants": [
        "family_balanced_sampling",
        "logit_norm_cap_light",
        "wrong_suppress_0_01",
        "posthoc_temperature_T_1_2",
        "qpm_runtime_hygiene"
      ]
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
      "latency_p50_ms": 840.9622311592102,
      "latency_p95_ms": 840.9622311592102,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling": {
      "count": 8,
      "avg_loss": 0.40125662565696985,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 317.8154528141022,
      "latency_p95_ms": 317.8154528141022,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light": {
      "count": 8,
      "avg_loss": 0.40125662565696985,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 318.36065649986267,
      "latency_p95_ms": 318.36065649986267,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01": {
      "count": 8,
      "avg_loss": 0.39278302170957125,
      "avg_accuracy": 0.24732155355308905,
      "avg_train_loss": 0.17814171314239502,
      "latency_p50_ms": 316.13054871559143,
      "latency_p95_ms": 316.13054871559143,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.41815000923816115,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 309.85116958618164,
      "latency_p95_ms": 309.85116958618164,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene": {
      "count": 8,
      "avg_loss": 0.40125662565696985,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 315.4067397117615,
      "latency_p95_ms": 315.4067397117615,
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
      "latency_p50_ms": 931.5798282623291,
      "latency_p95_ms": 931.5798282623291,
      "latency_p99_ms": 931.5798282623291,
      "latency_max_ms": 931.5798282623291,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 933.0968856811523,
      "latency_p95_ms": 933.0968856811523,
      "latency_p99_ms": 933.0968856811523,
      "latency_max_ms": 933.0968856811523,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 941.3173198699951,
      "latency_p95_ms": 941.3173198699951,
      "latency_p99_ms": 941.3173198699951,
      "latency_max_ms": 941.3173198699951,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 941.5218830108643,
      "latency_p95_ms": 941.5218830108643,
      "latency_p99_ms": 941.5218830108643,
      "latency_max_ms": 941.5218830108643,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 927.0343780517578,
      "latency_p95_ms": 927.0343780517578,
      "latency_p99_ms": 927.0343780517578,
      "latency_max_ms": 927.0343780517578,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 461.3206386566162,
      "latency_p95_ms": 461.3206386566162,
      "latency_p99_ms": 461.3206386566162,
      "latency_max_ms": 461.3206386566162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 904.7191143035889,
      "latency_p95_ms": 904.7191143035889,
      "latency_p99_ms": 904.7191143035889,
      "latency_max_ms": 904.7191143035889,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 687.1078014373779,
      "latency_p95_ms": 687.1078014373779,
      "latency_p99_ms": 687.1078014373779,
      "latency_max_ms": 687.1078014373779,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 335.8650207519531,
      "latency_p95_ms": 335.8650207519531,
      "latency_p99_ms": 335.8650207519531,
      "latency_max_ms": 335.8650207519531,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 342.39935874938965,
      "latency_p95_ms": 342.39935874938965,
      "latency_p99_ms": 342.39935874938965,
      "latency_max_ms": 342.39935874938965,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 344.01917457580566,
      "latency_p95_ms": 344.01917457580566,
      "latency_p99_ms": 344.01917457580566,
      "latency_max_ms": 344.01917457580566,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 363.8279438018799,
      "latency_p95_ms": 363.8279438018799,
      "latency_p99_ms": 363.8279438018799,
      "latency_max_ms": 363.8279438018799,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 358.0467700958252,
      "latency_p95_ms": 358.0467700958252,
      "latency_p99_ms": 358.0467700958252,
      "latency_max_ms": 358.0467700958252,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 181.38647079467773,
      "latency_p95_ms": 181.38647079467773,
      "latency_p99_ms": 181.38647079467773,
      "latency_max_ms": 181.38647079467773,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 348.16956520080566,
      "latency_p95_ms": 348.16956520080566,
      "latency_p99_ms": 348.16956520080566,
      "latency_max_ms": 348.16956520080566,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 268.80931854248047,
      "latency_p95_ms": 268.80931854248047,
      "latency_p99_ms": 268.80931854248047,
      "latency_max_ms": 268.80931854248047,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 341.519832611084,
      "latency_p95_ms": 341.519832611084,
      "latency_p99_ms": 341.519832611084,
      "latency_max_ms": 341.519832611084,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 342.33760833740234,
      "latency_p95_ms": 342.33760833740234,
      "latency_p99_ms": 342.33760833740234,
      "latency_max_ms": 342.33760833740234,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 344.34032440185547,
      "latency_p95_ms": 344.34032440185547,
      "latency_p99_ms": 344.34032440185547,
      "latency_max_ms": 344.34032440185547,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 366.4817810058594,
      "latency_p95_ms": 366.4817810058594,
      "latency_p99_ms": 366.4817810058594,
      "latency_max_ms": 366.4817810058594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 360.8584403991699,
      "latency_p95_ms": 360.8584403991699,
      "latency_p99_ms": 360.8584403991699,
      "latency_max_ms": 360.8584403991699,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 177.6123046875,
      "latency_p95_ms": 177.6123046875,
      "latency_p99_ms": 177.6123046875,
      "latency_max_ms": 177.6123046875,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 345.3240394592285,
      "latency_p95_ms": 345.3240394592285,
      "latency_p99_ms": 345.3240394592285,
      "latency_max_ms": 345.3240394592285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 268.41092109680176,
      "latency_p95_ms": 268.41092109680176,
      "latency_p99_ms": 268.41092109680176,
      "latency_max_ms": 268.41092109680176,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 337.7666473388672,
      "latency_p95_ms": 337.7666473388672,
      "latency_p99_ms": 337.7666473388672,
      "latency_max_ms": 337.7666473388672,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 347.19181060791016,
      "latency_p95_ms": 347.19181060791016,
      "latency_p99_ms": 347.19181060791016,
      "latency_max_ms": 347.19181060791016,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 344.6190357208252,
      "latency_p95_ms": 344.6190357208252,
      "latency_p99_ms": 344.6190357208252,
      "latency_max_ms": 344.6190357208252,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 364.76659774780273,
      "latency_p95_ms": 364.76659774780273,
      "latency_p99_ms": 364.76659774780273,
      "latency_max_ms": 364.76659774780273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 349.47657585144043,
      "latency_p95_ms": 349.47657585144043,
      "latency_p99_ms": 349.47657585144043,
      "latency_max_ms": 349.47657585144043,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 176.04589462280273,
      "latency_p95_ms": 176.04589462280273,
      "latency_p99_ms": 176.04589462280273,
      "latency_max_ms": 176.04589462280273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 340.4405117034912,
      "latency_p95_ms": 340.4405117034912,
      "latency_p99_ms": 340.4405117034912,
      "latency_max_ms": 340.4405117034912,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 268.7373161315918,
      "latency_p95_ms": 268.7373161315918,
      "latency_p99_ms": 268.7373161315918,
      "latency_max_ms": 268.7373161315918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 327.87394523620605,
      "latency_p95_ms": 327.87394523620605,
      "latency_p99_ms": 327.87394523620605,
      "latency_max_ms": 327.87394523620605,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 336.20500564575195,
      "latency_p95_ms": 336.20500564575195,
      "latency_p99_ms": 336.20500564575195,
      "latency_max_ms": 336.20500564575195,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 335.5717658996582,
      "latency_p95_ms": 335.5717658996582,
      "latency_p99_ms": 335.5717658996582,
      "latency_max_ms": 335.5717658996582,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 349.31278228759766,
      "latency_p95_ms": 349.31278228759766,
      "latency_p99_ms": 349.31278228759766,
      "latency_max_ms": 349.31278228759766,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 351.8531322479248,
      "latency_p95_ms": 351.8531322479248,
      "latency_p99_ms": 351.8531322479248,
      "latency_max_ms": 351.8531322479248,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 172.5454330444336,
      "latency_p95_ms": 172.5454330444336,
      "latency_p99_ms": 172.5454330444336,
      "latency_max_ms": 172.5454330444336,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 337.9237651824951,
      "latency_p95_ms": 337.9237651824951,
      "latency_p99_ms": 337.9237651824951,
      "latency_max_ms": 337.9237651824951,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__posthoc_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 267.52352714538574,
      "latency_p95_ms": 267.52352714538574,
      "latency_p99_ms": 267.52352714538574,
      "latency_max_ms": 267.52352714538574,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 336.6382122039795,
      "latency_p95_ms": 336.6382122039795,
      "latency_p99_ms": 336.6382122039795,
      "latency_max_ms": 336.6382122039795,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 345.8375930786133,
      "latency_p95_ms": 345.8375930786133,
      "latency_p99_ms": 345.8375930786133,
      "latency_max_ms": 345.8375930786133,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 341.47071838378906,
      "latency_p95_ms": 341.47071838378906,
      "latency_p99_ms": 341.47071838378906,
      "latency_max_ms": 341.47071838378906,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 362.72740364074707,
      "latency_p95_ms": 362.72740364074707,
      "latency_p99_ms": 362.72740364074707,
      "latency_max_ms": 362.72740364074707,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 352.13232040405273,
      "latency_p95_ms": 352.13232040405273,
      "latency_p99_ms": 352.13232040405273,
      "latency_max_ms": 352.13232040405273,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 176.01346969604492,
      "latency_p95_ms": 176.01346969604492,
      "latency_p99_ms": 176.01346969604492,
      "latency_max_ms": 176.01346969604492,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 344.2380428314209,
      "latency_p95_ms": 344.2380428314209,
      "latency_p99_ms": 344.2380428314209,
      "latency_max_ms": 344.2380428314209,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__qpm_runtime_hygiene",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 264.19615745544434,
      "latency_p95_ms": 264.19615745544434,
      "latency_p99_ms": 264.19615745544434,
      "latency_max_ms": 264.19615745544434,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```