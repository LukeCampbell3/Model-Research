# PVR-EC Latency Stability Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T19:31:39.573190",
    "run_id": "algo_20260607_192631_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 2026,
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
        2026
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
      "avg_loss": 0.4051392263111969,
      "avg_accuracy": 0.21791622906883187,
      "avg_train_loss": 0.1727062165737152,
      "latency_p50_ms": 963.7782573699951,
      "latency_p95_ms": 963.7782573699951,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1": {
      "count": 8,
      "avg_loss": 0.37423891096841544,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224744379520416,
      "latency_p50_ms": 609.5091104507446,
      "latency_p95_ms": 609.5091104507446,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.38248463200094795,
      "avg_accuracy": 0.2671120354903755,
      "avg_train_loss": 0.16951239109039307,
      "latency_p50_ms": 614.7547960281372,
      "latency_p95_ms": 614.7547960281372,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light": {
      "count": 8,
      "avg_loss": 0.374238919505539,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224745869636536,
      "latency_p50_ms": 610.3770136833191,
      "latency_p95_ms": 610.3770136833191,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium": {
      "count": 8,
      "avg_loss": 0.3745938003218422,
      "avg_accuracy": 0.3097768216283071,
      "avg_train_loss": 0.16059164702892303,
      "latency_p50_ms": 606.4158380031586,
      "latency_p95_ms": 606.4158380031586,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.37055438450382405,
      "avg_accuracy": 0.31887785043492983,
      "avg_train_loss": 0.1504926234483719,
      "latency_p50_ms": 611.1288666725159,
      "latency_p95_ms": 611.1288666725159,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light": {
      "count": 8,
      "avg_loss": 0.38660131534561515,
      "avg_accuracy": 0.25592984197369595,
      "avg_train_loss": 0.17259939014911652,
      "latency_p50_ms": 616.2688732147217,
      "latency_p95_ms": 616.2688732147217,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.396124194880637,
      "avg_accuracy": 0.31330901334752226,
      "avg_train_loss": 0.15224745869636536,
      "latency_p50_ms": 599.9646186828613,
      "latency_p95_ms": 599.9646186828613,
      "latency_p95_p50_ratio": 1.0,
      "owner_change_rate": null,
      "owner_changed_success_rate": null
    },
    "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration": {
      "count": 8,
      "avg_loss": 0.40154885357090586,
      "avg_accuracy": 0.2671120354903755,
      "avg_train_loss": 0.16951239109039307,
      "latency_p50_ms": 603.755384683609,
      "latency_p95_ms": 603.755384683609,
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
      "latency_p50_ms": 1065.7246112823486,
      "latency_p95_ms": 1065.7246112823486,
      "latency_p99_ms": 1065.7246112823486,
      "latency_max_ms": 1065.7246112823486,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1070.4774856567383,
      "latency_p95_ms": 1070.4774856567383,
      "latency_p99_ms": 1070.4774856567383,
      "latency_max_ms": 1070.4774856567383,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1065.5975341796875,
      "latency_p95_ms": 1065.5975341796875,
      "latency_p99_ms": 1065.5975341796875,
      "latency_max_ms": 1065.5975341796875,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1073.9257335662842,
      "latency_p95_ms": 1073.9257335662842,
      "latency_p99_ms": 1073.9257335662842,
      "latency_max_ms": 1073.9257335662842,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1071.974515914917,
      "latency_p95_ms": 1071.974515914917,
      "latency_p99_ms": 1071.974515914917,
      "latency_max_ms": 1071.974515914917,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 534.2390537261963,
      "latency_p95_ms": 534.2390537261963,
      "latency_p99_ms": 534.2390537261963,
      "latency_max_ms": 534.2390537261963,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 1032.8199863433838,
      "latency_p95_ms": 1032.8199863433838,
      "latency_p99_ms": 1032.8199863433838,
      "latency_max_ms": 1032.8199863433838,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "fixed_moe_vectorized",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 795.4671382904053,
      "latency_p95_ms": 795.4671382904053,
      "latency_p99_ms": 795.4671382904053,
      "latency_max_ms": 795.4671382904053,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 668.6644554138184,
      "latency_p95_ms": 668.6644554138184,
      "latency_p99_ms": 668.6644554138184,
      "latency_max_ms": 668.6644554138184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.2815761566162,
      "latency_p95_ms": 671.2815761566162,
      "latency_p99_ms": 671.2815761566162,
      "latency_max_ms": 671.2815761566162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.3820648193359,
      "latency_p95_ms": 676.3820648193359,
      "latency_p99_ms": 676.3820648193359,
      "latency_max_ms": 676.3820648193359,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 684.5605373382568,
      "latency_p95_ms": 684.5605373382568,
      "latency_p99_ms": 684.5605373382568,
      "latency_max_ms": 684.5605373382568,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.9439964294434,
      "latency_p95_ms": 673.9439964294434,
      "latency_p99_ms": 673.9439964294434,
      "latency_max_ms": 673.9439964294434,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 334.5143795013428,
      "latency_p95_ms": 334.5143795013428,
      "latency_p99_ms": 334.5143795013428,
      "latency_max_ms": 334.5143795013428,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 658.9019298553467,
      "latency_p95_ms": 658.9019298553467,
      "latency_p99_ms": 658.9019298553467,
      "latency_max_ms": 658.9019298553467,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__final_candidate_v1",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 507.8239440917969,
      "latency_p95_ms": 507.8239440917969,
      "latency_p99_ms": 507.8239440917969,
      "latency_max_ms": 507.8239440917969,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 670.8512306213379,
      "latency_p95_ms": 670.8512306213379,
      "latency_p99_ms": 670.8512306213379,
      "latency_max_ms": 670.8512306213379,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 675.4236221313477,
      "latency_p95_ms": 675.4236221313477,
      "latency_p99_ms": 675.4236221313477,
      "latency_max_ms": 675.4236221313477,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 679.9042224884033,
      "latency_p95_ms": 679.9042224884033,
      "latency_p99_ms": 679.9042224884033,
      "latency_max_ms": 679.9042224884033,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 685.133695602417,
      "latency_p95_ms": 685.133695602417,
      "latency_p99_ms": 685.133695602417,
      "latency_max_ms": 685.133695602417,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.3154220581055,
      "latency_p95_ms": 681.3154220581055,
      "latency_p99_ms": 681.3154220581055,
      "latency_max_ms": 681.3154220581055,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 336.72046661376953,
      "latency_p95_ms": 336.72046661376953,
      "latency_p99_ms": 336.72046661376953,
      "latency_max_ms": 336.72046661376953,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 675.649881362915,
      "latency_p95_ms": 675.649881362915,
      "latency_p99_ms": 675.649881362915,
      "latency_max_ms": 675.649881362915,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 513.0398273468018,
      "latency_p95_ms": 513.0398273468018,
      "latency_p99_ms": 513.0398273468018,
      "latency_max_ms": 513.0398273468018,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.4904308319092,
      "latency_p95_ms": 671.4904308319092,
      "latency_p99_ms": 671.4904308319092,
      "latency_max_ms": 671.4904308319092,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.5998859405518,
      "latency_p95_ms": 674.5998859405518,
      "latency_p99_ms": 674.5998859405518,
      "latency_max_ms": 674.5998859405518,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 672.3065376281738,
      "latency_p95_ms": 672.3065376281738,
      "latency_p99_ms": 672.3065376281738,
      "latency_max_ms": 672.3065376281738,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 682.6777458190918,
      "latency_p95_ms": 682.6777458190918,
      "latency_p99_ms": 682.6777458190918,
      "latency_max_ms": 682.6777458190918,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 674.0052700042725,
      "latency_p95_ms": 674.0052700042725,
      "latency_p99_ms": 674.0052700042725,
      "latency_max_ms": 674.0052700042725,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 335.50429344177246,
      "latency_p95_ms": 335.50429344177246,
      "latency_p99_ms": 335.50429344177246,
      "latency_max_ms": 335.50429344177246,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 665.0116443634033,
      "latency_p95_ms": 665.0116443634033,
      "latency_p99_ms": 665.0116443634033,
      "latency_max_ms": 665.0116443634033,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 507.42030143737793,
      "latency_p95_ms": 507.42030143737793,
      "latency_p99_ms": 507.42030143737793,
      "latency_max_ms": 507.42030143737793,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.7630672454834,
      "latency_p95_ms": 666.7630672454834,
      "latency_p99_ms": 666.7630672454834,
      "latency_max_ms": 666.7630672454834,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.8882884979248,
      "latency_p95_ms": 662.8882884979248,
      "latency_p99_ms": 662.8882884979248,
      "latency_max_ms": 662.8882884979248,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 664.8776531219482,
      "latency_p95_ms": 664.8776531219482,
      "latency_p99_ms": 664.8776531219482,
      "latency_max_ms": 664.8776531219482,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.0863018035889,
      "latency_p95_ms": 681.0863018035889,
      "latency_p99_ms": 681.0863018035889,
      "latency_max_ms": 681.0863018035889,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 676.7580509185791,
      "latency_p95_ms": 676.7580509185791,
      "latency_p99_ms": 676.7580509185791,
      "latency_max_ms": 676.7580509185791,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 334.1047763824463,
      "latency_p95_ms": 334.1047763824463,
      "latency_p99_ms": 334.1047763824463,
      "latency_max_ms": 334.1047763824463,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 661.9343757629395,
      "latency_p95_ms": 661.9343757629395,
      "latency_p99_ms": 661.9343757629395,
      "latency_max_ms": 661.9343757629395,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_penalty_medium",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 502.9141902923584,
      "latency_p95_ms": 502.9141902923584,
      "latency_p99_ms": 502.9141902923584,
      "latency_max_ms": 502.9141902923584,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.1853580474854,
      "latency_p95_ms": 663.1853580474854,
      "latency_p99_ms": 663.1853580474854,
      "latency_max_ms": 663.1853580474854,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 681.5788745880127,
      "latency_p95_ms": 681.5788745880127,
      "latency_p99_ms": 681.5788745880127,
      "latency_max_ms": 681.5788745880127,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 677.1550178527832,
      "latency_p95_ms": 677.1550178527832,
      "latency_p99_ms": 677.1550178527832,
      "latency_max_ms": 677.1550178527832,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 684.5390796661377,
      "latency_p95_ms": 684.5390796661377,
      "latency_p99_ms": 684.5390796661377,
      "latency_max_ms": 684.5390796661377,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 677.337646484375,
      "latency_p95_ms": 677.337646484375,
      "latency_p99_ms": 677.337646484375,
      "latency_max_ms": 677.337646484375,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 337.77713775634766,
      "latency_p95_ms": 337.77713775634766,
      "latency_p99_ms": 337.77713775634766,
      "latency_max_ms": 337.77713775634766,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 658.3786010742188,
      "latency_p95_ms": 658.3786010742188,
      "latency_p99_ms": 658.3786010742188,
      "latency_max_ms": 658.3786010742188,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 509.0792179107666,
      "latency_p95_ms": 509.0792179107666,
      "latency_p99_ms": 509.0792179107666,
      "latency_max_ms": 509.0792179107666,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.2347011566162,
      "latency_p95_ms": 673.2347011566162,
      "latency_p99_ms": 673.2347011566162,
      "latency_max_ms": 673.2347011566162,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 683.8066577911377,
      "latency_p95_ms": 683.8066577911377,
      "latency_p99_ms": 683.8066577911377,
      "latency_max_ms": 683.8066577911377,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 671.6494560241699,
      "latency_p95_ms": 671.6494560241699,
      "latency_p99_ms": 671.6494560241699,
      "latency_max_ms": 671.6494560241699,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 688.4164810180664,
      "latency_p95_ms": 688.4164810180664,
      "latency_p99_ms": 688.4164810180664,
      "latency_max_ms": 688.4164810180664,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 679.3475151062012,
      "latency_p95_ms": 679.3475151062012,
      "latency_p99_ms": 679.3475151062012,
      "latency_max_ms": 679.3475151062012,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 339.9784564971924,
      "latency_p95_ms": 339.9784564971924,
      "latency_p99_ms": 339.9784564971924,
      "latency_max_ms": 339.9784564971924,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 678.945779800415,
      "latency_p95_ms": 678.945779800415,
      "latency_p99_ms": 678.945779800415,
      "latency_max_ms": 678.945779800415,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 514.7719383239746,
      "latency_p95_ms": 514.7719383239746,
      "latency_p99_ms": 514.7719383239746,
      "latency_max_ms": 514.7719383239746,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 657.1860313415527,
      "latency_p95_ms": 657.1860313415527,
      "latency_p99_ms": 657.1860313415527,
      "latency_max_ms": 657.1860313415527,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 666.1741733551025,
      "latency_p95_ms": 666.1741733551025,
      "latency_p99_ms": 666.1741733551025,
      "latency_max_ms": 666.1741733551025,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.945032119751,
      "latency_p95_ms": 662.945032119751,
      "latency_p99_ms": 662.945032119751,
      "latency_max_ms": 662.945032119751,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 670.3588962554932,
      "latency_p95_ms": 670.3588962554932,
      "latency_p99_ms": 670.3588962554932,
      "latency_max_ms": 670.3588962554932,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 662.3344421386719,
      "latency_p95_ms": 662.3344421386719,
      "latency_p99_ms": 662.3344421386719,
      "latency_max_ms": 662.3344421386719,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 334.43236351013184,
      "latency_p95_ms": 334.43236351013184,
      "latency_p99_ms": 334.43236351013184,
      "latency_max_ms": 334.43236351013184,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 649.6851444244385,
      "latency_p95_ms": 649.6851444244385,
      "latency_p99_ms": 649.6851444244385,
      "latency_max_ms": 649.6851444244385,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 496.600866317749,
      "latency_p95_ms": 496.600866317749,
      "latency_p99_ms": 496.600866317749,
      "latency_max_ms": 496.600866317749,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 655.0734043121338,
      "latency_p95_ms": 655.0734043121338,
      "latency_p99_ms": 655.0734043121338,
      "latency_max_ms": 655.0734043121338,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 663.8228893280029,
      "latency_p95_ms": 663.8228893280029,
      "latency_p99_ms": 663.8228893280029,
      "latency_max_ms": 663.8228893280029,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 660.5823040008545,
      "latency_p95_ms": 660.5823040008545,
      "latency_p99_ms": 660.5823040008545,
      "latency_max_ms": 660.5823040008545,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 673.1967926025391,
      "latency_p95_ms": 673.1967926025391,
      "latency_p99_ms": 673.1967926025391,
      "latency_max_ms": 673.1967926025391,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 669.386625289917,
      "latency_p95_ms": 669.386625289917,
      "latency_p99_ms": 669.386625289917,
      "latency_max_ms": 669.386625289917,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 343.7485694885254,
      "latency_p95_ms": 343.7485694885254,
      "latency_p99_ms": 343.7485694885254,
      "latency_max_ms": 343.7485694885254,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 660.7017517089844,
      "latency_p95_ms": 660.7017517089844,
      "latency_p99_ms": 660.7017517089844,
      "latency_max_ms": 660.7017517089844,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_posthoc_temperature_calibration",
      "batch_size": null,
      "sequence_length": null,
      "latency_p50_ms": 503.53074073791504,
      "latency_p95_ms": 503.53074073791504,
      "latency_p99_ms": 503.53074073791504,
      "latency_max_ms": 503.53074073791504,
      "latency_std_ms": null,
      "latency_p95_p50_ratio": 1.0
    }
  ]
}
```