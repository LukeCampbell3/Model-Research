# PVR-EC Sparse Direction By Family Report

**Status:** PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

**Statuses:** PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION, PVR_EC_DO_NOT_PROMOTE, PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION, PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T14:05:49.030475",
    "run_id": "algo_20260607_132702_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-calibration-constrained-sparse-aux-sweep --sparse-aux-loss-variants baseline_main_loss,sparse_ce_0_03,sparse_ce_0_05,sparse_ce_0_03_plus_margin_0_03,sparse_ce_0_03_plus_wrong_suppress_0_03,sparse_ce_0_05_plus_wrong_suppress_0_01,sparse_ce_0_05_plus_logit_norm_penalty_light,sparse_ce_0_05_plus_temperature_regularization,sparse_ce_warmup_decay --output-dir evaluation/benchmark_results/pvr_calibration_constrained_sparse_aux",
    "model_variants": [
      "pvr_ec_ownership_top1_scale_schedule_1_to_8"
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
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED",
  "statuses": [
    "PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED"
  ],
  "promotion_ready": false,
  "by_family": {
    "clrs_style": {
      "avg_loss": 0.24617239443102368,
      "avg_accuracy": 0.36380183255263826,
      "correct_class_logit_delta": 4.778104046152698,
      "incorrect_class_logit_delta_mean": 1.8261936840911706,
      "incorrect_class_logit_delta_max": 5.7403807855314675,
      "delta_correct_minus_top_wrong": -0.9622767310313605,
      "incorrect_logit_overamplification_rate": 0.6664367435431039,
      "correct_logit_underamplification_rate": 0.02496246217358728,
      "residual_help_rate": 0.9481876153084967,
      "residual_harm_rate": 0.05180059140359474,
      "token_to_sequence_transfer_ratio": 0.12003383108581012
    },
    "dyck": {
      "avg_loss": 0.3409419562322674,
      "avg_accuracy": 0.06609901763862774,
      "correct_class_logit_delta": 2.6262009845296332,
      "incorrect_class_logit_delta_mean": 2.2639415017935485,
      "incorrect_class_logit_delta_max": 4.233789567318228,
      "delta_correct_minus_top_wrong": -1.607588567253616,
      "incorrect_logit_overamplification_rate": 0.9520083589272367,
      "correct_logit_underamplification_rate": 0.13941830390669768,
      "residual_help_rate": 0.9424775157261777,
      "residual_harm_rate": 0.057450510739592446,
      "token_to_sequence_transfer_ratio": 0.06541597441555314
    },
    "listops": {
      "avg_loss": 1.3989999331533909,
      "avg_accuracy": 0.19545394970885055,
      "correct_class_logit_delta": 2.2413157967772954,
      "incorrect_class_logit_delta_mean": 1.559566340279869,
      "incorrect_class_logit_delta_max": 4.416225198242399,
      "delta_correct_minus_top_wrong": -2.174909402098921,
      "incorrect_logit_overamplification_rate": 0.8847046382725239,
      "correct_logit_underamplification_rate": 0.21745787182670837,
      "residual_help_rate": 0.8084655060536332,
      "residual_harm_rate": 0.19146027384946743,
      "token_to_sequence_transfer_ratio": 0.11644773196915846
    },
    "scan_style": {
      "avg_loss": 0.2412158432416618,
      "avg_accuracy": 0.07458638911935506,
      "correct_class_logit_delta": 2.611343545295919,
      "incorrect_class_logit_delta_mean": 2.2771069006994367,
      "incorrect_class_logit_delta_max": 4.1721362844109535,
      "delta_correct_minus_top_wrong": -1.5607927605095837,
      "incorrect_logit_overamplification_rate": 0.9411165995730294,
      "correct_logit_underamplification_rate": 0.13944178714316674,
      "residual_help_rate": 0.8855823829977049,
      "residual_harm_rate": 0.11435499941823461,
      "token_to_sequence_transfer_ratio": 0.057974853806221444
    }
  }
}
```