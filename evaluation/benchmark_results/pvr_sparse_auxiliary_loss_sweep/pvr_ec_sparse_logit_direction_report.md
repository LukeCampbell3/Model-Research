# PVR-EC Sparse Logit Direction Report

**Status:** PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

**Statuses:** PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION, PVR_EC_DO_NOT_PROMOTE, PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION, PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:18:03.818607",
    "run_id": "algo_20260607_031408_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-loss-sweep --sparse-aux-loss-variants baseline_main_loss,sparse_ce_0_03,sparse_ce_0_05,margin_align_0_03_m0_5,margin_align_0_05_m0_5,wrong_suppress_0_03_t0_25,sparse_ce_0_03_plus_margin_0_03,margin_0_03_plus_wrong_suppress_0_03,sparse_ce_0_03_plus_harm_0_03 --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_loss_sweep",
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
      "avg_loss": 0.46348366168482846,
      "avg_qpc": 0.06054665483850138,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17268744165371785,
      "avg_exact_match": 0.0,
      "avg_loss": 0.41296596180958056,
      "avg_qpc": 0.17268744165371785,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_05": {
      "params": 482690,
      "avg_accuracy": 0.24243722927027295,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4004437902864689,
      "avg_qpc": 0.24243722927027295,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_03_m0_5": {
      "params": 482690,
      "avg_accuracy": 0.10121606180580317,
      "avg_exact_match": 0.0,
      "avg_loss": 0.446313688182272,
      "avg_qpc": 0.10121606180580317,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_align_0_05_m0_5": {
      "params": 482690,
      "avg_accuracy": 0.11243111735688467,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4407933249215906,
      "avg_qpc": 0.11243111735688467,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__wrong_suppress_0_03_t0_25": {
      "params": 482690,
      "avg_accuracy": 0.06802156528639025,
      "avg_exact_match": 0.0,
      "avg_loss": 0.44242214163144433,
      "avg_qpc": 0.06802156528639025,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_margin_0_03": {
      "params": 482690,
      "avg_accuracy": 0.2102302618601088,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4218268555123359,
      "avg_qpc": 0.2102302618601088,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__margin_0_03_plus_wrong_suppress_0_03": {
      "params": 482690,
      "avg_accuracy": 0.11535639563864514,
      "avg_exact_match": 0.0,
      "avg_loss": 0.42275461923175806,
      "avg_qpc": 0.11535639563864514,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_scale_schedule_1_to_8__aux__sparse_ce_0_03_plus_harm_0_03": {
      "params": 482690,
      "avg_accuracy": 0.17619962371543163,
      "avg_exact_match": 0.0,
      "avg_loss": 0.4157806743557254,
      "avg_qpc": 0.17619962371543163,
      "avg_loops": 1.0
    }
  },
  "avg_loss": 0.46348366168482846,
  "avg_accuracy": 0.06054665483850138,
  "quality_per_ms": 0.06054665483850138,
  "latency_p50": 0.6177078485488892,
  "latency_p95": 0.6177078485488892,
  "calibration_proxy": 0.08361891197652371,
  "correct_class_logit_delta": 0.540522301584133,
  "incorrect_class_logit_delta_mean": 0.45247794258951524,
  "incorrect_class_logit_delta_max": 3.297521810978651,
  "delta_correct_minus_top_wrong": -2.756999489851296,
  "sparse_margin_delta": -2.756999489851296,
  "combined_margin_delta": 0.24125803481244168,
  "shared_margin": -2.872743577696383,
  "combined_margin": -2.6314855661864085,
  "sparse_logit_norm": 34.76115824778875,
  "combined_logit_norm": 24.05731720725695,
  "incorrect_logit_overamplification_rate": 0.9794975132681429,
  "correct_logit_underamplification_rate": 0.4465818303906417,
  "residual_help_rate": 0.6453027786531795,
  "residual_harm_rate": 0.3544546033566197,
  "decision_token_help_rate": 0.6470743940056611,
  "final_token_loss_delta": -0.6754102862905711,
  "token_to_sequence_transfer_ratio": 0.06254858933453986,
  "expert_delta_contribution_pct": 0.922526032812233,
  "shared_sparse_ratio": 0.11373381812397079,
  "by_family": {
    "clrs_style": {
      "avg_loss": 0.26488294342049845,
      "avg_accuracy": 0.22313104441027173,
      "correct_class_logit_delta": 3.9476061965871376,
      "incorrect_class_logit_delta_mean": 1.9635143789842173,
      "incorrect_class_logit_delta_max": 5.059113676349322,
      "delta_correct_minus_top_wrong": -1.111507475928024,
      "incorrect_logit_overamplification_rate": 0.8202955777998324,
      "correct_logit_underamplification_rate": 0.06300101892325242,
      "residual_help_rate": 0.9184906093610657,
      "residual_harm_rate": 0.08149518341384397,
      "token_to_sequence_transfer_ratio": 0.10047986093867484
    },
    "dyck": {
      "avg_loss": 0.34465245305801984,
      "avg_accuracy": 0.07189708668839578,
      "correct_class_logit_delta": 2.1761255887406015,
      "incorrect_class_logit_delta_mean": 1.8028789701916308,
      "incorrect_class_logit_delta_max": 4.442642139615836,
      "delta_correct_minus_top_wrong": -2.266516549995652,
      "incorrect_logit_overamplification_rate": 0.9520585943289377,
      "correct_logit_underamplification_rate": 0.24347212880066194,
      "residual_help_rate": 0.8691793835066535,
      "residual_harm_rate": 0.13064964999621564,
      "token_to_sequence_transfer_ratio": 0.09523511847799895
    },
    "listops": {
      "avg_loss": 1.463897584213151,
      "avg_accuracy": 0.164139002789792,
      "correct_class_logit_delta": 1.7294070545014821,
      "incorrect_class_logit_delta_mean": 1.282514919501005,
      "incorrect_class_logit_delta_max": 4.2930197103155985,
      "delta_correct_minus_top_wrong": -2.5636126978529825,
      "incorrect_logit_overamplification_rate": 0.909804774241315,
      "correct_logit_underamplification_rate": 0.3119120935573139,
      "residual_help_rate": 0.7468819390568469,
      "residual_harm_rate": 0.2530407328934719,
      "token_to_sequence_transfer_ratio": 0.09776326365401419
    },
    "scan_style": {
      "avg_loss": 0.24464532531177005,
      "avg_accuracy": 0.07094855704608095,
      "correct_class_logit_delta": 2.1864705872887193,
      "incorrect_class_logit_delta_mean": 1.833766326217705,
      "incorrect_class_logit_delta_max": 4.3890467782815294,
      "delta_correct_minus_top_wrong": -2.2025762212773166,
      "incorrect_logit_overamplification_rate": 0.9424414251827531,
      "correct_logit_underamplification_rate": 0.24165713335403577,
      "residual_help_rate": 0.7733737595586313,
      "residual_harm_rate": 0.22655040046245428,
      "token_to_sequence_transfer_ratio": 0.06870031586265303
    }
  }
}
```