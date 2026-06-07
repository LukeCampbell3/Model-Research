# PVR-EC Sparse Direction By Family Report

**Status:** PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

**Statuses:** PVR_EC_CORRECT_LOGIT_UNDERAMPLIFICATION, PVR_EC_DO_NOT_PROMOTE, PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION, PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:13:54.653030",
    "run_id": "algo_20260607_031113_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-logit-direction-diagnostic --output-dir evaluation/benchmark_results/pvr_sparse_logit_direction",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
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
      "avg_loss": 0.2822246220894158,
      "avg_accuracy": 0.14225713822897623,
      "correct_class_logit_delta": 1.2501203492671873,
      "incorrect_class_logit_delta_mean": 1.3306937076849863,
      "incorrect_class_logit_delta_max": 2.780024543404579,
      "delta_correct_minus_top_wrong": -1.5299041482309501,
      "incorrect_logit_overamplification_rate": 0.9739251670738062,
      "correct_logit_underamplification_rate": 0.17123016637924593,
      "residual_help_rate": 0.7543035758038362,
      "residual_harm_rate": 0.24549427178377906,
      "token_to_sequence_transfer_ratio": 0.7070278319568915
    },
    "dyck": {
      "avg_loss": 0.35375421090672415,
      "avg_accuracy": 0.0038678686859169985,
      "correct_class_logit_delta": -0.7054247756799062,
      "incorrect_class_logit_delta_mean": -0.9067476068933805,
      "incorrect_class_logit_delta_max": 2.0122494331250587,
      "delta_correct_minus_top_wrong": -2.7176742317775884,
      "incorrect_logit_overamplification_rate": 0.999759953469038,
      "correct_logit_underamplification_rate": 0.836311982323726,
      "residual_help_rate": 0.5272507594587902,
      "residual_harm_rate": 0.4721299461089075,
      "token_to_sequence_transfer_ratio": -0.3714472528691114
    },
    "listops": {
      "avg_loss": 1.6073681395500898,
      "avg_accuracy": 0.0908414312194574,
      "correct_class_logit_delta": -0.07243225008278387,
      "incorrect_class_logit_delta_mean": -0.2206141168717295,
      "incorrect_class_logit_delta_max": 2.4336464144289494,
      "delta_correct_minus_top_wrong": -2.5060786306858063,
      "incorrect_logit_overamplification_rate": 0.9868161994963884,
      "correct_logit_underamplification_rate": 0.5608945190906525,
      "residual_help_rate": 0.6583926975727081,
      "residual_harm_rate": 0.3413939536549151,
      "token_to_sequence_transfer_ratio": 0.06940642821515992
    },
    "scan_style": {
      "avg_loss": 0.24815153307281435,
      "avg_accuracy": 0.012719020095088506,
      "correct_class_logit_delta": -0.6374307768419385,
      "incorrect_class_logit_delta_mean": -0.7566282493062317,
      "incorrect_class_logit_delta_max": 2.083898050710559,
      "delta_correct_minus_top_wrong": -2.7213288359344006,
      "incorrect_logit_overamplification_rate": 0.9999431688338518,
      "correct_logit_underamplification_rate": 0.7976075168699026,
      "residual_help_rate": 0.4542821808718145,
      "residual_harm_rate": 0.5453439801931381,
      "token_to_sequence_transfer_ratio": -6.611070870062419
    }
  }
}
```