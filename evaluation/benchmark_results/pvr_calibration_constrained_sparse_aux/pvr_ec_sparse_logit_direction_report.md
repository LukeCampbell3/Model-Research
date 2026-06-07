# PVR-EC Sparse Logit Direction Report

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
  "model_table": {
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__baseline_main_loss": {
      "params": 482690,
      "avg_accuracy": 0.06054665483850138,
      "avg_exact_match": 0.0,
      "avg_loss": 0.46348367095924914,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17268744165371785,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4129659630901491,
      "avg_qpc": 0.17268744165371785,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05": {
      "params": 482690,
      "avg_accuracy": 0.24243722927027295,
      "avg_exact_match": 0.0,
      "avg_loss": 0.40044378609551734,
      "avg_qpc": 0.24243722927027295,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_margin_0_03": {
      "params": 482690,
      "avg_accuracy": 0.20060030496405545,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4201112611529728,
      "avg_qpc": 0.20060030496405545,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_wrong_suppress_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17590030562267703,
      "avg_exact_match": 0.0,
      "avg_loss": 0.41126188018824905,
      "avg_qpc": 0.17590030562267703,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_wrong_suppress_0_01": {
      "params": 482690,
      "avg_accuracy": 0.23800205349819248,
      "avg_exact_match": 0.0,
      "avg_loss": 0.3987135972129181,
      "avg_qpc": 0.23800205349819248,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_logit_norm_penalty_light": {
      "params": 482690,
      "avg_accuracy": 0.24730744124607193,
      "avg_exact_match": 0.0,
      "avg_loss": 0.39579605466375745,
      "avg_qpc": 0.24730744124607193,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05_plus_temperature_regularization": {
      "params": 482690,
      "avg_accuracy": 0.24746650398247153,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4005933780378351,
      "avg_qpc": 0.24746650398247153,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_warmup_decay": {
      "params": 482690,
      "avg_accuracy": 0.17931110841711173,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4111922134179622,
      "avg_qpc": 0.17931110841711173,
      "avg_loops": 1.0
    }
  },
  "avg_loss": 0.46348367095924914,
  "avg_accuracy": 0.06054665483850138,
  "quality_per_ms": 0.06054665483850138,
  "latency_p50": 11.274146378040314,
  "latency_p95": 11.274146378040314,
  "calibration_proxy": 0.08361890806194867,
  "correct_class_logit_delta": 0.5405222679983126,
  "incorrect_class_logit_delta_mean": 0.45247794874982594,
  "incorrect_class_logit_delta_max": 3.2975218265006943,
  "delta_correct_minus_top_wrong": -2.756999535486102,
  "sparse_margin_delta": -2.756999535486102,
  "combined_margin_delta": 0.2412580560582379,
  "shared_margin": -2.872743589182695,
  "combined_margin": -2.6314855289335055,
  "sparse_logit_norm": 34.761158322294555,
  "combined_logit_norm": 24.05731731156508,
  "incorrect_logit_overamplification_rate": 0.9794975132681429,
  "correct_logit_underamplification_rate": 0.4465818303906417,
  "residual_help_rate": 0.6453027786531795,
  "residual_harm_rate": 0.3544546033566197,
  "decision_token_help_rate": 0.6470743940056611,
  "final_token_loss_delta": -0.6754102623090148,
  "token_to_sequence_transfer_ratio": 0.06254858857579991,
  "expert_delta_contribution_pct": 0.9225260329011056,
  "shared_sparse_ratio": 0.11373381791539336,
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