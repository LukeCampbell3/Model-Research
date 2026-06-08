# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:54:16.323129",
    "run_id": "algo_20260607_234918_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
      "avg_loss": 0.4128779768167684,
      "avg_accuracy": 0.2465923217227525,
      "avg_train_loss": 0.15063753724098206,
      "latency_p50_ms": 797.3158657550812,
      "latency_p95_ms": 797.3158657550812,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.46422695667327696,
      "avg_accuracy": 0.05611798299936589,
      "avg_train_loss": 0.2083549052476883,
      "latency_p50_ms": 317.38486886024475,
      "latency_p95_ms": 317.38486886024475,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1": {
      "count": 8,
      "avg_loss": 0.40125662565696985,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 291.8024957180023,
      "latency_p95_ms": 291.8024957180023,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.398577261560907,
      "avg_accuracy": 0.213413735155882,
      "avg_train_loss": 0.1846141815185547,
      "latency_p50_ms": 275.53725242614746,
      "latency_p95_ms": 275.53725242614746,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.4115613133568937,
      "avg_accuracy": 0.18282003317413148,
      "avg_train_loss": 0.19408826529979706,
      "latency_p50_ms": 275.0902473926544,
      "latency_p95_ms": 275.0902473926544,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.40125662565696985,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 278.8848876953125,
      "latency_p95_ms": 278.8848876953125,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.398577261560907,
      "avg_accuracy": 0.213413735155882,
      "avg_train_loss": 0.1846141815185547,
      "latency_p50_ms": 276.86673402786255,
      "latency_p95_ms": 276.86673402786255,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.40960301187199855,
      "avg_accuracy": 0.20752995845307737,
      "avg_train_loss": 0.19041119515895844,
      "latency_p50_ms": 282.31924772262573,
      "latency_p95_ms": 282.31924772262573,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.39278302170957125,
      "avg_accuracy": 0.24732155355308905,
      "avg_train_loss": 0.17814171314239502,
      "latency_p50_ms": 277.05663442611694,
      "latency_p95_ms": 277.05663442611694,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.42583591653965414,
      "avg_accuracy": 0.18282003317413148,
      "avg_train_loss": 0.19408826529979706,
      "latency_p50_ms": 270.8844542503357,
      "latency_p95_ms": 270.8844542503357,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.41815000923816115,
      "avg_accuracy": 0.23395668899979996,
      "avg_train_loss": 0.1834246814250946,
      "latency_p50_ms": 271.1185812950134,
      "latency_p95_ms": 271.1185812950134,
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
      "latency_p50_ms": 883.4075927734375,
      "latency_p95_ms": 883.4075927734375,
      "latency_p99_ms": 883.4075927734375,
      "latency_max_ms": 883.4075927734375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 885.5187892913818,
      "latency_p95_ms": 885.5187892913818,
      "latency_p99_ms": 885.5187892913818,
      "latency_max_ms": 885.5187892913818,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 889.7175788879395,
      "latency_p95_ms": 889.7175788879395,
      "latency_p99_ms": 889.7175788879395,
      "latency_max_ms": 889.7175788879395,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 888.8795375823975,
      "latency_p95_ms": 888.8795375823975,
      "latency_p99_ms": 888.8795375823975,
      "latency_max_ms": 888.8795375823975,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 880.6624412536621,
      "latency_p95_ms": 880.6624412536621,
      "latency_p99_ms": 880.6624412536621,
      "latency_max_ms": 880.6624412536621,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 439.971923828125,
      "latency_p95_ms": 439.971923828125,
      "latency_p99_ms": 439.971923828125,
      "latency_max_ms": 439.971923828125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 861.0646724700928,
      "latency_p95_ms": 861.0646724700928,
      "latency_p99_ms": 861.0646724700928,
      "latency_max_ms": 861.0646724700928,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 649.3043899536133,
      "latency_p95_ms": 649.3043899536133,
      "latency_p99_ms": 649.3043899536133,
      "latency_max_ms": 649.3043899536133,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 347.5968837738037,
      "latency_p95_ms": 347.5968837738037,
      "latency_p99_ms": 347.5968837738037,
      "latency_max_ms": 347.5968837738037,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 354.9642562866211,
      "latency_p95_ms": 354.9642562866211,
      "latency_p99_ms": 354.9642562866211,
      "latency_max_ms": 354.9642562866211,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 365.3256893157959,
      "latency_p95_ms": 365.3256893157959,
      "latency_p99_ms": 365.3256893157959,
      "latency_max_ms": 365.3256893157959,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 371.1812496185303,
      "latency_p95_ms": 371.1812496185303,
      "latency_p99_ms": 371.1812496185303,
      "latency_max_ms": 371.1812496185303,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 348.47187995910645,
      "latency_p95_ms": 348.47187995910645,
      "latency_p99_ms": 348.47187995910645,
      "latency_max_ms": 348.47187995910645,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 168.49946975708008,
      "latency_p95_ms": 168.49946975708008,
      "latency_p99_ms": 168.49946975708008,
      "latency_max_ms": 168.49946975708008,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 331.1638832092285,
      "latency_p95_ms": 331.1638832092285,
      "latency_p99_ms": 331.1638832092285,
      "latency_max_ms": 331.1638832092285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 251.875638961792,
      "latency_p95_ms": 251.875638961792,
      "latency_p99_ms": 251.875638961792,
      "latency_max_ms": 251.875638961792,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.36614418029785,
      "latency_p95_ms": 320.36614418029785,
      "latency_p99_ms": 320.36614418029785,
      "latency_max_ms": 320.36614418029785,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.5194778442383,
      "latency_p95_ms": 313.5194778442383,
      "latency_p99_ms": 313.5194778442383,
      "latency_max_ms": 313.5194778442383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.6906623840332,
      "latency_p95_ms": 313.6906623840332,
      "latency_p99_ms": 313.6906623840332,
      "latency_max_ms": 313.6906623840332,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.0775451660156,
      "latency_p95_ms": 338.0775451660156,
      "latency_p99_ms": 338.0775451660156,
      "latency_max_ms": 338.0775451660156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 327.40211486816406,
      "latency_p95_ms": 327.40211486816406,
      "latency_p99_ms": 327.40211486816406,
      "latency_max_ms": 327.40211486816406,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 166.18609428405762,
      "latency_p95_ms": 166.18609428405762,
      "latency_p99_ms": 166.18609428405762,
      "latency_max_ms": 166.18609428405762,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 317.51251220703125,
      "latency_p95_ms": 317.51251220703125,
      "latency_p99_ms": 317.51251220703125,
      "latency_max_ms": 317.51251220703125,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 237.66541481018066,
      "latency_p95_ms": 237.66541481018066,
      "latency_p99_ms": 237.66541481018066,
      "latency_max_ms": 237.66541481018066,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 291.2313938140869,
      "latency_p95_ms": 291.2313938140869,
      "latency_p99_ms": 291.2313938140869,
      "latency_max_ms": 291.2313938140869,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.9766502380371,
      "latency_p95_ms": 308.9766502380371,
      "latency_p99_ms": 308.9766502380371,
      "latency_max_ms": 308.9766502380371,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 296.39649391174316,
      "latency_p95_ms": 296.39649391174316,
      "latency_p99_ms": 296.39649391174316,
      "latency_max_ms": 296.39649391174316,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.19739532470703,
      "latency_p95_ms": 316.19739532470703,
      "latency_p99_ms": 316.19739532470703,
      "latency_max_ms": 316.19739532470703,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.89866638183594,
      "latency_p95_ms": 305.89866638183594,
      "latency_p99_ms": 305.89866638183594,
      "latency_max_ms": 305.89866638183594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 155.00259399414062,
      "latency_p95_ms": 155.00259399414062,
      "latency_p99_ms": 155.00259399414062,
      "latency_max_ms": 155.00259399414062,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 303.7528991699219,
      "latency_p95_ms": 303.7528991699219,
      "latency_p99_ms": 303.7528991699219,
      "latency_max_ms": 303.7528991699219,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 226.84192657470703,
      "latency_p95_ms": 226.84192657470703,
      "latency_p99_ms": 226.84192657470703,
      "latency_max_ms": 226.84192657470703,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 287.8243923187256,
      "latency_p95_ms": 287.8243923187256,
      "latency_p99_ms": 287.8243923187256,
      "latency_max_ms": 287.8243923187256,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.44286155700684,
      "latency_p95_ms": 301.44286155700684,
      "latency_p99_ms": 301.44286155700684,
      "latency_max_ms": 301.44286155700684,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 297.0736026763916,
      "latency_p95_ms": 297.0736026763916,
      "latency_p99_ms": 297.0736026763916,
      "latency_max_ms": 297.0736026763916,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 317.6698684692383,
      "latency_p95_ms": 317.6698684692383,
      "latency_p99_ms": 317.6698684692383,
      "latency_max_ms": 317.6698684692383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.8686981201172,
      "latency_p95_ms": 304.8686981201172,
      "latency_p99_ms": 304.8686981201172,
      "latency_max_ms": 304.8686981201172,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 154.05869483947754,
      "latency_p95_ms": 154.05869483947754,
      "latency_p99_ms": 154.05869483947754,
      "latency_max_ms": 154.05869483947754,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.3948154449463,
      "latency_p95_ms": 306.3948154449463,
      "latency_p99_ms": 306.3948154449463,
      "latency_max_ms": 306.3948154449463,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 231.38904571533203,
      "latency_p95_ms": 231.38904571533203,
      "latency_p99_ms": 231.38904571533203,
      "latency_max_ms": 231.38904571533203,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.8130226135254,
      "latency_p95_ms": 309.8130226135254,
      "latency_p99_ms": 309.8130226135254,
      "latency_max_ms": 309.8130226135254,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.8958568572998,
      "latency_p95_ms": 301.8958568572998,
      "latency_p99_ms": 301.8958568572998,
      "latency_max_ms": 301.8958568572998,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 299.66020584106445,
      "latency_p95_ms": 299.66020584106445,
      "latency_p99_ms": 299.66020584106445,
      "latency_max_ms": 299.66020584106445,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.676326751709,
      "latency_p95_ms": 320.676326751709,
      "latency_p99_ms": 320.676326751709,
      "latency_max_ms": 320.676326751709,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 312.9754066467285,
      "latency_p95_ms": 312.9754066467285,
      "latency_p99_ms": 312.9754066467285,
      "latency_max_ms": 312.9754066467285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 157.210111618042,
      "latency_p95_ms": 157.210111618042,
      "latency_p99_ms": 157.210111618042,
      "latency_max_ms": 157.210111618042,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 298.1245517730713,
      "latency_p95_ms": 298.1245517730713,
      "latency_p99_ms": 298.1245517730713,
      "latency_max_ms": 298.1245517730713,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 230.72361946105957,
      "latency_p95_ms": 230.72361946105957,
      "latency_p99_ms": 230.72361946105957,
      "latency_max_ms": 230.72361946105957,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 294.55018043518066,
      "latency_p95_ms": 294.55018043518066,
      "latency_p99_ms": 294.55018043518066,
      "latency_max_ms": 294.55018043518066,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.90152740478516,
      "latency_p95_ms": 305.90152740478516,
      "latency_p99_ms": 305.90152740478516,
      "latency_max_ms": 305.90152740478516,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 299.6342182159424,
      "latency_p95_ms": 299.6342182159424,
      "latency_p99_ms": 299.6342182159424,
      "latency_max_ms": 299.6342182159424,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.8804130554199,
      "latency_p95_ms": 320.8804130554199,
      "latency_p99_ms": 320.8804130554199,
      "latency_max_ms": 320.8804130554199,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.3534240722656,
      "latency_p95_ms": 308.3534240722656,
      "latency_p99_ms": 308.3534240722656,
      "latency_max_ms": 308.3534240722656,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 156.05735778808594,
      "latency_p95_ms": 156.05735778808594,
      "latency_p99_ms": 156.05735778808594,
      "latency_max_ms": 156.05735778808594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 299.47447776794434,
      "latency_p95_ms": 299.47447776794434,
      "latency_p99_ms": 299.47447776794434,
      "latency_max_ms": 299.47447776794434,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 230.08227348327637,
      "latency_p95_ms": 230.08227348327637,
      "latency_p99_ms": 230.08227348327637,
      "latency_max_ms": 230.08227348327637,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 295.15767097473145,
      "latency_p95_ms": 295.15767097473145,
      "latency_p99_ms": 295.15767097473145,
      "latency_max_ms": 295.15767097473145,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.1927719116211,
      "latency_p95_ms": 314.1927719116211,
      "latency_p99_ms": 314.1927719116211,
      "latency_max_ms": 314.1927719116211,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.4628162384033,
      "latency_p95_ms": 302.4628162384033,
      "latency_p99_ms": 302.4628162384033,
      "latency_max_ms": 302.4628162384033,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 325.25634765625,
      "latency_p95_ms": 325.25634765625,
      "latency_p99_ms": 325.25634765625,
      "latency_max_ms": 325.25634765625,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.11964988708496,
      "latency_p95_ms": 313.11964988708496,
      "latency_p99_ms": 313.11964988708496,
      "latency_max_ms": 313.11964988708496,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 156.82387351989746,
      "latency_p95_ms": 156.82387351989746,
      "latency_p99_ms": 156.82387351989746,
      "latency_max_ms": 156.82387351989746,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.7203712463379,
      "latency_p95_ms": 311.7203712463379,
      "latency_p99_ms": 311.7203712463379,
      "latency_max_ms": 311.7203712463379,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 239.8204803466797,
      "latency_p95_ms": 239.8204803466797,
      "latency_p99_ms": 239.8204803466797,
      "latency_max_ms": 239.8204803466797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 296.9069480895996,
      "latency_p95_ms": 296.9069480895996,
      "latency_p99_ms": 296.9069480895996,
      "latency_max_ms": 296.9069480895996,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 307.786226272583,
      "latency_p95_ms": 307.786226272583,
      "latency_p99_ms": 307.786226272583,
      "latency_max_ms": 307.786226272583,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.19795417785645,
      "latency_p95_ms": 305.19795417785645,
      "latency_p99_ms": 305.19795417785645,
      "latency_max_ms": 305.19795417785645,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.7695999145508,
      "latency_p95_ms": 316.7695999145508,
      "latency_p99_ms": 316.7695999145508,
      "latency_max_ms": 316.7695999145508,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.5037212371826,
      "latency_p95_ms": 310.5037212371826,
      "latency_p99_ms": 310.5037212371826,
      "latency_max_ms": 310.5037212371826,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 153.98812294006348,
      "latency_p95_ms": 153.98812294006348,
      "latency_p99_ms": 153.98812294006348,
      "latency_max_ms": 153.98812294006348,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 296.6289520263672,
      "latency_p95_ms": 296.6289520263672,
      "latency_p99_ms": 296.6289520263672,
      "latency_max_ms": 296.6289520263672,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 228.67155075073242,
      "latency_p95_ms": 228.67155075073242,
      "latency_p99_ms": 228.67155075073242,
      "latency_max_ms": 228.67155075073242,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 282.56845474243164,
      "latency_p95_ms": 282.56845474243164,
      "latency_p99_ms": 282.56845474243164,
      "latency_max_ms": 282.56845474243164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 294.10576820373535,
      "latency_p95_ms": 294.10576820373535,
      "latency_p99_ms": 294.10576820373535,
      "latency_max_ms": 294.10576820373535,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 291.80264472961426,
      "latency_p95_ms": 291.80264472961426,
      "latency_p99_ms": 291.80264472961426,
      "latency_max_ms": 291.80264472961426,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.0156784057617,
      "latency_p95_ms": 310.0156784057617,
      "latency_p99_ms": 310.0156784057617,
      "latency_max_ms": 310.0156784057617,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.7307472229004,
      "latency_p95_ms": 306.7307472229004,
      "latency_p99_ms": 306.7307472229004,
      "latency_max_ms": 306.7307472229004,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 154.08825874328613,
      "latency_p95_ms": 154.08825874328613,
      "latency_p99_ms": 154.08825874328613,
      "latency_max_ms": 154.08825874328613,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 298.1681823730469,
      "latency_p95_ms": 298.1681823730469,
      "latency_p99_ms": 298.1681823730469,
      "latency_max_ms": 298.1681823730469,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 229.59589958190918,
      "latency_p95_ms": 229.59589958190918,
      "latency_p99_ms": 229.59589958190918,
      "latency_max_ms": 229.59589958190918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 292.41228103637695,
      "latency_p95_ms": 292.41228103637695,
      "latency_p99_ms": 292.41228103637695,
      "latency_max_ms": 292.41228103637695,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 298.5048294067383,
      "latency_p95_ms": 298.5048294067383,
      "latency_p99_ms": 298.5048294067383,
      "latency_max_ms": 298.5048294067383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 295.8540916442871,
      "latency_p95_ms": 295.8540916442871,
      "latency_p99_ms": 295.8540916442871,
      "latency_max_ms": 295.8540916442871,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.28764152526855,
      "latency_p95_ms": 311.28764152526855,
      "latency_p99_ms": 311.28764152526855,
      "latency_max_ms": 311.28764152526855,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 301.25951766967773,
      "latency_p95_ms": 301.25951766967773,
      "latency_p99_ms": 301.25951766967773,
      "latency_max_ms": 301.25951766967773,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 152.16970443725586,
      "latency_p95_ms": 152.16970443725586,
      "latency_p99_ms": 152.16970443725586,
      "latency_max_ms": 152.16970443725586,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 293.11370849609375,
      "latency_p95_ms": 293.11370849609375,
      "latency_p99_ms": 293.11370849609375,
      "latency_max_ms": 293.11370849609375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 224.34687614440918,
      "latency_p95_ms": 224.34687614440918,
      "latency_p99_ms": 224.34687614440918,
      "latency_max_ms": 224.34687614440918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```