# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:04:18.617274",
    "run_id": "algo_20260607_235913_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 2026,
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
        2026
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
      "avg_loss": 0.40513353542579955,
      "avg_accuracy": 0.2179172791466334,
      "avg_train_loss": 0.17266248166561127,
      "latency_p50_ms": 796.2744235992432,
      "latency_p95_ms": 796.2744235992432,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_deploy_top1": {
      "count": 8,
      "avg_loss": 0.4316840081010014,
      "avg_accuracy": 0.12047529540869384,
      "avg_train_loss": 0.22074340283870697,
      "latency_p50_ms": 328.9979100227356,
      "latency_p95_ms": 328.9979100227356,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1": {
      "count": 8,
      "avg_loss": 0.374238919505539,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224745869636536,
      "latency_p50_ms": 284.97451543807983,
      "latency_p95_ms": 284.97451543807983,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.3745938003218422,
      "avg_accuracy": 0.3097768216283071,
      "avg_train_loss": 0.16059164702892303,
      "latency_p50_ms": 283.8214635848999,
      "latency_p95_ms": 283.8214635848999,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.38248463200094795,
      "avg_accuracy": 0.2671120354903755,
      "avg_train_loss": 0.16951239109039307,
      "latency_p50_ms": 287.6935005187988,
      "latency_p95_ms": 287.6935005187988,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.374238919505539,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224745869636536,
      "latency_p50_ms": 282.91723132133484,
      "latency_p95_ms": 282.91723132133484,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium": {
      "count": 8,
      "avg_loss": 0.3745938003218422,
      "avg_accuracy": 0.3097768216283071,
      "avg_train_loss": 0.16059164702892303,
      "latency_p50_ms": 281.7520797252655,
      "latency_p95_ms": 281.7520797252655,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.38660131534561515,
      "avg_accuracy": 0.25592984197369595,
      "avg_train_loss": 0.17259939014911652,
      "latency_p50_ms": 287.1812582015991,
      "latency_p95_ms": 287.1812582015991,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.37055439311855787,
      "avg_accuracy": 0.31887785043492983,
      "avg_train_loss": 0.1504926234483719,
      "latency_p50_ms": 284.59298610687256,
      "latency_p95_ms": 284.59298610687256,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.40154885357090586,
      "avg_accuracy": 0.2671120354903755,
      "avg_train_loss": 0.16951239109039307,
      "latency_p50_ms": 280.3995907306671,
      "latency_p95_ms": 280.3995907306671,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2": {
      "count": 8,
      "avg_loss": 0.396124194880637,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224745869636536,
      "latency_p50_ms": 275.85238218307495,
      "latency_p95_ms": 275.85238218307495,
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
      "latency_p50_ms": 881.0155391693115,
      "latency_p95_ms": 881.0155391693115,
      "latency_p99_ms": 881.0155391693115,
      "latency_max_ms": 881.0155391693115,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 879.8792362213135,
      "latency_p95_ms": 879.8792362213135,
      "latency_p99_ms": 879.8792362213135,
      "latency_max_ms": 879.8792362213135,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 880.9359073638916,
      "latency_p95_ms": 880.9359073638916,
      "latency_p99_ms": 880.9359073638916,
      "latency_max_ms": 880.9359073638916,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 887.671709060669,
      "latency_p95_ms": 887.671709060669,
      "latency_p99_ms": 887.671709060669,
      "latency_max_ms": 887.671709060669,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 887.3226642608643,
      "latency_p95_ms": 887.3226642608643,
      "latency_p99_ms": 887.3226642608643,
      "latency_max_ms": 887.3226642608643,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 440.6740665435791,
      "latency_p95_ms": 440.6740665435791,
      "latency_p99_ms": 440.6740665435791,
      "latency_max_ms": 440.6740665435791,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 853.7657260894775,
      "latency_p95_ms": 853.7657260894775,
      "latency_p99_ms": 853.7657260894775,
      "latency_max_ms": 853.7657260894775,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 658.9305400848389,
      "latency_p95_ms": 658.9305400848389,
      "latency_p99_ms": 658.9305400848389,
      "latency_max_ms": 658.9305400848389,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 338.6051654815674,
      "latency_p95_ms": 338.6051654815674,
      "latency_p99_ms": 338.6051654815674,
      "latency_max_ms": 338.6051654815674,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 359.59529876708984,
      "latency_p95_ms": 359.59529876708984,
      "latency_p99_ms": 359.59529876708984,
      "latency_max_ms": 359.59529876708984,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 360.6078624725342,
      "latency_p95_ms": 360.6078624725342,
      "latency_p99_ms": 360.6078624725342,
      "latency_max_ms": 360.6078624725342,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 382.8284740447998,
      "latency_p95_ms": 382.8284740447998,
      "latency_p99_ms": 382.8284740447998,
      "latency_max_ms": 382.8284740447998,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 365.74840545654297,
      "latency_p95_ms": 365.74840545654297,
      "latency_p99_ms": 365.74840545654297,
      "latency_max_ms": 365.74840545654297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 178.92026901245117,
      "latency_p95_ms": 178.92026901245117,
      "latency_p99_ms": 178.92026901245117,
      "latency_max_ms": 178.92026901245117,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 354.7096252441406,
      "latency_p95_ms": 354.7096252441406,
      "latency_p99_ms": 354.7096252441406,
      "latency_max_ms": 354.7096252441406,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 290.9681797027588,
      "latency_p95_ms": 290.9681797027588,
      "latency_p99_ms": 290.9681797027588,
      "latency_max_ms": 290.9681797027588,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.0159378051758,
      "latency_p95_ms": 313.0159378051758,
      "latency_p99_ms": 313.0159378051758,
      "latency_max_ms": 313.0159378051758,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.96851348876953,
      "latency_p95_ms": 315.96851348876953,
      "latency_p99_ms": 315.96851348876953,
      "latency_max_ms": 315.96851348876953,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 312.6795291900635,
      "latency_p95_ms": 312.6795291900635,
      "latency_p99_ms": 312.6795291900635,
      "latency_max_ms": 312.6795291900635,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 322.57819175720215,
      "latency_p95_ms": 322.57819175720215,
      "latency_p99_ms": 322.57819175720215,
      "latency_max_ms": 322.57819175720215,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.2469654083252,
      "latency_p95_ms": 313.2469654083252,
      "latency_p99_ms": 313.2469654083252,
      "latency_max_ms": 313.2469654083252,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 156.2638282775879,
      "latency_p95_ms": 156.2638282775879,
      "latency_p99_ms": 156.2638282775879,
      "latency_max_ms": 156.2638282775879,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.4133186340332,
      "latency_p95_ms": 304.4133186340332,
      "latency_p99_ms": 304.4133186340332,
      "latency_max_ms": 304.4133186340332,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 241.62983894348145,
      "latency_p95_ms": 241.62983894348145,
      "latency_p99_ms": 241.62983894348145,
      "latency_max_ms": 241.62983894348145,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 318.5091018676758,
      "latency_p95_ms": 318.5091018676758,
      "latency_p99_ms": 318.5091018676758,
      "latency_max_ms": 318.5091018676758,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 306.7669868469238,
      "latency_p95_ms": 306.7669868469238,
      "latency_p99_ms": 306.7669868469238,
      "latency_max_ms": 306.7669868469238,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.06836891174316,
      "latency_p95_ms": 310.06836891174316,
      "latency_p99_ms": 310.06836891174316,
      "latency_max_ms": 310.06836891174316,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 324.1686820983887,
      "latency_p95_ms": 324.1686820983887,
      "latency_p99_ms": 324.1686820983887,
      "latency_max_ms": 324.1686820983887,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.22226333618164,
      "latency_p95_ms": 315.22226333618164,
      "latency_p99_ms": 315.22226333618164,
      "latency_max_ms": 315.22226333618164,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 155.44819831848145,
      "latency_p95_ms": 155.44819831848145,
      "latency_p99_ms": 155.44819831848145,
      "latency_max_ms": 155.44819831848145,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.87885665893555,
      "latency_p95_ms": 302.87885665893555,
      "latency_p99_ms": 302.87885665893555,
      "latency_max_ms": 302.87885665893555,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 237.50925064086914,
      "latency_p95_ms": 237.50925064086914,
      "latency_p99_ms": 237.50925064086914,
      "latency_max_ms": 237.50925064086914,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.1623783111572,
      "latency_p95_ms": 309.1623783111572,
      "latency_p99_ms": 309.1623783111572,
      "latency_max_ms": 309.1623783111572,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 318.39632987976074,
      "latency_p95_ms": 318.39632987976074,
      "latency_p99_ms": 318.39632987976074,
      "latency_max_ms": 318.39632987976074,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 317.7156448364258,
      "latency_p95_ms": 317.7156448364258,
      "latency_p99_ms": 317.7156448364258,
      "latency_max_ms": 317.7156448364258,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.51825523376465,
      "latency_p95_ms": 320.51825523376465,
      "latency_p99_ms": 320.51825523376465,
      "latency_max_ms": 320.51825523376465,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.6651725769043,
      "latency_p95_ms": 316.6651725769043,
      "latency_p99_ms": 316.6651725769043,
      "latency_max_ms": 316.6651725769043,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 160.15195846557617,
      "latency_p95_ms": 160.15195846557617,
      "latency_p99_ms": 160.15195846557617,
      "latency_max_ms": 160.15195846557617,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.6888484954834,
      "latency_p95_ms": 315.6888484954834,
      "latency_p99_ms": 315.6888484954834,
      "latency_max_ms": 315.6888484954834,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 243.24941635131836,
      "latency_p95_ms": 243.24941635131836,
      "latency_p99_ms": 243.24941635131836,
      "latency_max_ms": 243.24941635131836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.6957206726074,
      "latency_p95_ms": 309.6957206726074,
      "latency_p99_ms": 309.6957206726074,
      "latency_max_ms": 309.6957206726074,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.7031841278076,
      "latency_p95_ms": 308.7031841278076,
      "latency_p99_ms": 308.7031841278076,
      "latency_max_ms": 308.7031841278076,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.74778938293457,
      "latency_p95_ms": 311.74778938293457,
      "latency_p99_ms": 311.74778938293457,
      "latency_max_ms": 311.74778938293457,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 320.1878070831299,
      "latency_p95_ms": 320.1878070831299,
      "latency_p99_ms": 320.1878070831299,
      "latency_max_ms": 320.1878070831299,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.74445152282715,
      "latency_p95_ms": 311.74445152282715,
      "latency_p99_ms": 311.74445152282715,
      "latency_max_ms": 311.74445152282715,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 157.1955680847168,
      "latency_p95_ms": 157.1955680847168,
      "latency_p99_ms": 157.1955680847168,
      "latency_max_ms": 157.1955680847168,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.04536628723145,
      "latency_p95_ms": 305.04536628723145,
      "latency_p99_ms": 305.04536628723145,
      "latency_max_ms": 305.04536628723145,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 239.01796340942383,
      "latency_p95_ms": 239.01796340942383,
      "latency_p99_ms": 239.01796340942383,
      "latency_max_ms": 239.01796340942383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 307.6815605163574,
      "latency_p95_ms": 307.6815605163574,
      "latency_p99_ms": 307.6815605163574,
      "latency_max_ms": 307.6815605163574,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 311.0527992248535,
      "latency_p95_ms": 311.0527992248535,
      "latency_p99_ms": 311.0527992248535,
      "latency_max_ms": 311.0527992248535,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.8861446380615,
      "latency_p95_ms": 310.8861446380615,
      "latency_p99_ms": 310.8861446380615,
      "latency_max_ms": 310.8861446380615,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.27464294433594,
      "latency_p95_ms": 316.27464294433594,
      "latency_p99_ms": 316.27464294433594,
      "latency_max_ms": 316.27464294433594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 312.98232078552246,
      "latency_p95_ms": 312.98232078552246,
      "latency_p99_ms": 312.98232078552246,
      "latency_max_ms": 312.98232078552246,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 153.53655815124512,
      "latency_p95_ms": 153.53655815124512,
      "latency_p99_ms": 153.53655815124512,
      "latency_max_ms": 153.53655815124512,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.6598434448242,
      "latency_p95_ms": 304.6598434448242,
      "latency_p99_ms": 304.6598434448242,
      "latency_max_ms": 304.6598434448242,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 236.94276809692383,
      "latency_p95_ms": 236.94276809692383,
      "latency_p99_ms": 236.94276809692383,
      "latency_max_ms": 236.94276809692383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.02330780029297,
      "latency_p95_ms": 310.02330780029297,
      "latency_p99_ms": 310.02330780029297,
      "latency_max_ms": 310.02330780029297,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 318.18413734436035,
      "latency_p95_ms": 318.18413734436035,
      "latency_p99_ms": 318.18413734436035,
      "latency_max_ms": 318.18413734436035,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 314.00084495544434,
      "latency_p95_ms": 314.00084495544434,
      "latency_p99_ms": 314.00084495544434,
      "latency_max_ms": 314.00084495544434,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 321.13027572631836,
      "latency_p95_ms": 321.13027572631836,
      "latency_p99_ms": 321.13027572631836,
      "latency_max_ms": 321.13027572631836,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 319.2720413208008,
      "latency_p95_ms": 319.2720413208008,
      "latency_p99_ms": 319.2720413208008,
      "latency_max_ms": 319.2720413208008,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 160.06946563720703,
      "latency_p95_ms": 160.06946563720703,
      "latency_p99_ms": 160.06946563720703,
      "latency_max_ms": 160.06946563720703,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 313.0061626434326,
      "latency_p95_ms": 313.0061626434326,
      "latency_p99_ms": 313.0061626434326,
      "latency_max_ms": 313.0061626434326,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 241.76383018493652,
      "latency_p95_ms": 241.76383018493652,
      "latency_p99_ms": 241.76383018493652,
      "latency_max_ms": 241.76383018493652,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.2065372467041,
      "latency_p95_ms": 305.2065372467041,
      "latency_p99_ms": 305.2065372467041,
      "latency_max_ms": 305.2065372467041,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 312.4880790710449,
      "latency_p95_ms": 312.4880790710449,
      "latency_p99_ms": 312.4880790710449,
      "latency_max_ms": 312.4880790710449,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 316.67113304138184,
      "latency_p95_ms": 316.67113304138184,
      "latency_p99_ms": 316.67113304138184,
      "latency_max_ms": 316.67113304138184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 332.31258392333984,
      "latency_p95_ms": 332.31258392333984,
      "latency_p99_ms": 332.31258392333984,
      "latency_max_ms": 332.31258392333984,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.89646911621094,
      "latency_p95_ms": 309.89646911621094,
      "latency_p99_ms": 309.89646911621094,
      "latency_max_ms": 309.89646911621094,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 156.36634826660156,
      "latency_p95_ms": 156.36634826660156,
      "latency_p99_ms": 156.36634826660156,
      "latency_max_ms": 156.36634826660156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 302.9026985168457,
      "latency_p95_ms": 302.9026985168457,
      "latency_p99_ms": 302.9026985168457,
      "latency_max_ms": 302.9026985168457,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 240.90003967285156,
      "latency_p95_ms": 240.90003967285156,
      "latency_p99_ms": 240.90003967285156,
      "latency_max_ms": 240.90003967285156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 303.27892303466797,
      "latency_p95_ms": 303.27892303466797,
      "latency_p99_ms": 303.27892303466797,
      "latency_max_ms": 303.27892303466797,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 305.0353527069092,
      "latency_p95_ms": 305.0353527069092,
      "latency_p99_ms": 305.0353527069092,
      "latency_max_ms": 305.0353527069092,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.49480628967285,
      "latency_p95_ms": 308.49480628967285,
      "latency_p99_ms": 308.49480628967285,
      "latency_max_ms": 308.49480628967285,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.79888343811035,
      "latency_p95_ms": 310.79888343811035,
      "latency_p99_ms": 310.79888343811035,
      "latency_max_ms": 310.79888343811035,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 315.0336742401123,
      "latency_p95_ms": 315.0336742401123,
      "latency_p99_ms": 315.0336742401123,
      "latency_max_ms": 315.0336742401123,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 154.41322326660156,
      "latency_p95_ms": 154.41322326660156,
      "latency_p99_ms": 154.41322326660156,
      "latency_max_ms": 154.41322326660156,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 308.50744247436523,
      "latency_p95_ms": 308.50744247436523,
      "latency_p99_ms": 308.50744247436523,
      "latency_max_ms": 308.50744247436523,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 237.63442039489746,
      "latency_p95_ms": 237.63442039489746,
      "latency_p99_ms": 237.63442039489746,
      "latency_max_ms": 237.63442039489746,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 300.703763961792,
      "latency_p95_ms": 300.703763961792,
      "latency_p99_ms": 300.703763961792,
      "latency_max_ms": 300.703763961792,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 310.14132499694824,
      "latency_p95_ms": 310.14132499694824,
      "latency_p99_ms": 310.14132499694824,
      "latency_max_ms": 310.14132499694824,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 304.1696548461914,
      "latency_p95_ms": 304.1696548461914,
      "latency_p99_ms": 304.1696548461914,
      "latency_max_ms": 304.1696548461914,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 309.43870544433594,
      "latency_p95_ms": 309.43870544433594,
      "latency_p99_ms": 309.43870544433594,
      "latency_max_ms": 309.43870544433594,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 303.58290672302246,
      "latency_p95_ms": 303.58290672302246,
      "latency_p99_ms": 303.58290672302246,
      "latency_max_ms": 303.58290672302246,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 151.75628662109375,
      "latency_p95_ms": 151.75628662109375,
      "latency_p99_ms": 151.75628662109375,
      "latency_max_ms": 151.75628662109375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 295.0608730316162,
      "latency_p95_ms": 295.0608730316162,
      "latency_p99_ms": 295.0608730316162,
      "latency_max_ms": 295.0608730316162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 231.9655418395996,
      "latency_p95_ms": 231.9655418395996,
      "latency_p99_ms": 231.9655418395996,
      "latency_max_ms": 231.9655418395996,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```