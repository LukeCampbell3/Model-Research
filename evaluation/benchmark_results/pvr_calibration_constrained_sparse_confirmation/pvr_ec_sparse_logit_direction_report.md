# PVR-EC Sparse Logit Direction Report

**Status:** PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

**Statuses:** PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION, PVR_EC_DO_NOT_PROMOTE, PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION, PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T14:10:51.125573",
    "run_id": "algo_20260607_140807_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8,pvr_ec_ownership_top1_best_sparse_logit_repair --enable-ownership-map --ownership-map-mode frozen --run-sparse-direction-transfer-confirmation --output-dir evaluation/benchmark_results/pvr_calibration_constrained_sparse_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_best_sparse_logit_repair"
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
    "fixed_moe_vectorized": {
      "params": 1001092,
      "avg_accuracy": 0.25857819999606313,
      "avg_exact_match": 0.00925,
      "avg_loss": 0.3886076922838887,
      "avg_qpc": 0.12928909999803156,
      "avg_loops": 1.0
    },
    "pvr_ec_deploy_top1": {
      "params": 614274,
      "avg_accuracy": 0.0771500010285979,
      "avg_exact_match": 0.0,
      "avg_loss": 0.45097945421002805,
      "avg_qpc": 0.0771500010285979,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8": {
      "params": 482690,
      "avg_accuracy": 0.06054665483850138,
      "avg_exact_match": 0.0,
      "avg_loss": 0.46348366168482846,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_best_sparse_logit_repair": {
      "params": 482690,
      "avg_accuracy": 0.24662427509545803,
      "avg_exact_match": 0.0,
      "avg_loss": 0.39578524367728585,
      "avg_qpc": 0.24662427509545803,
      "avg_loops": 1.0
    }
  },
  "avg_loss": 0.45723155794742826,
  "avg_accuracy": 0.06884832793354963,
  "quality_per_ms": 0.06884832793354963,
  "latency_p50": 0.6223247200250626,
  "latency_p95": 0.6223247200250626,
  "calibration_proxy": 0.08747283368039552,
  "correct_class_logit_delta": 0.12402330924745308,
  "incorrect_class_logit_delta_mean": 0.05557926814071834,
  "incorrect_class_logit_delta_max": 2.3707534011142952,
  "delta_correct_minus_top_wrong": -2.246730081814652,
  "sparse_margin_delta": -2.246730081814652,
  "combined_margin_delta": 0.011939626537544712,
  "shared_margin": -2.6076432584474483,
  "combined_margin": -2.5957036398661635,
  "sparse_logit_norm": 23.26655243895948,
  "combined_logit_norm": 29.052977142234642,
  "incorrect_logit_overamplification_rate": 0.9884997431654483,
  "correct_logit_underamplification_rate": 0.5428052239797884,
  "residual_help_rate": 0.6105461632056782,
  "residual_harm_rate": 0.38910307770129293,
  "decision_token_help_rate": 0.6176421874358008,
  "final_token_loss_delta": -0.39924823243086394,
  "token_to_sequence_transfer_ratio": -1.471803878530161,
  "expert_delta_contribution_pct": 0.8922798124707707,
  "shared_sparse_ratio": 0.15506214186219341,
  "by_family": {
    "clrs_style": {
      "avg_loss": 0.2637824281636212,
      "avg_accuracy": 0.26234503313183843,
      "correct_class_logit_delta": 2.342974208140125,
      "incorrect_class_logit_delta_mean": 1.701699339836422,
      "incorrect_class_logit_delta_max": 3.513906069099903,
      "delta_correct_minus_top_wrong": -1.1709318730152316,
      "incorrect_logit_overamplification_rate": 0.8226877150850164,
      "correct_logit_underamplification_rate": 0.11605196551681729,
      "residual_help_rate": 0.8362023822135396,
      "residual_harm_rate": 0.16366284785585272,
      "token_to_sequence_transfer_ratio": 0.5139864263111192
    },
    "dyck": {
      "avg_loss": 0.3487409269437194,
      "avg_accuracy": 0.018790061049961015,
      "correct_class_logit_delta": 0.7187481027924353,
      "incorrect_class_logit_delta_mean": 0.4818730764091015,
      "incorrect_class_logit_delta_max": 2.7835439493258796,
      "delta_correct_minus_top_wrong": -2.06479585212138,
      "incorrect_logit_overamplification_rate": 0.9838657335688671,
      "correct_logit_underamplification_rate": 0.5575413215491507,
      "residual_help_rate": 0.6848338334303762,
      "residual_harm_rate": 0.3147532974059383,
      "token_to_sequence_transfer_ratio": -0.24264722524883445
    },
    "listops": {
      "avg_loss": 1.5147844590246677,
      "avg_accuracy": 0.13613810406485796,
      "correct_class_logit_delta": 0.8823041812841742,
      "incorrect_class_logit_delta_mean": 0.6962917045069238,
      "incorrect_class_logit_delta_max": 3.0365192517638206,
      "delta_correct_minus_top_wrong": -2.1542150055368743,
      "incorrect_logit_overamplification_rate": 0.9515349914630254,
      "correct_logit_underamplification_rate": 0.3978599331167061,
      "residual_help_rate": 0.752738282084465,
      "residual_harm_rate": 0.24711117607269747,
      "token_to_sequence_transfer_ratio": 0.07952965434713148
    },
    "scan_style": {
      "avg_loss": 0.24519101406137148,
      "avg_accuracy": 0.032051245169928744,
      "correct_class_logit_delta": 0.7650017139191428,
      "incorrect_class_logit_delta_mean": 0.5944783383359512,
      "incorrect_class_logit_delta_max": 2.8231717633704343,
      "delta_correct_minus_top_wrong": -2.0581700205802917,
      "incorrect_logit_overamplification_rate": 0.9815157142778238,
      "correct_logit_underamplification_rate": 0.5317383445799351,
      "residual_help_rate": 0.6361881162350377,
      "residual_harm_rate": 0.3635626534620921,
      "token_to_sequence_transfer_ratio": -4.399985329590183
    }
  }
}
```