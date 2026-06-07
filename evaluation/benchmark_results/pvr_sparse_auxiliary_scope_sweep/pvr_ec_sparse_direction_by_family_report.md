# PVR-EC Sparse Direction By Family Report

**Status:** PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION, PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER, PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY, PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED

```json
{
  "metadata": {
    "timestamp": "2026-06-07T03:24:44.342132",
    "run_id": "algo_20260607_032151_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_scale_schedule_1_to_8 --enable-ownership-map --ownership-map-mode frozen --run-sparse-auxiliary-scope-sweep --sparse-aux-scopes aux_all_tokens,aux_decision_tokens_only,aux_final_tokens_only,aux_listops_scan_only,aux_scan_only,aux_listops_only,aux_dyck_final_state_only --output-dir evaluation/benchmark_results/pvr_sparse_auxiliary_scope_sweep",
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
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_INCORRECT_LOGIT_OVERAMPLIFICATION",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_BLOCKER",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_DIAGNOSTIC_READY",
    "PVR_EC_SPARSE_LOGIT_DIRECTION_MISALIGNED"
  ],
  "promotion_ready": false,
  "by_family": {
    "clrs_style": {
      "avg_loss": 0.2283196166778604,
      "avg_accuracy": 0.4675775601741621,
      "correct_class_logit_delta": 6.2181932628154755,
      "incorrect_class_logit_delta_mean": 2.1131970758239427,
      "incorrect_class_logit_delta_max": 7.001865535974503,
      "delta_correct_minus_top_wrong": -0.7836723315219084,
      "incorrect_logit_overamplification_rate": 0.5538648416598638,
      "correct_logit_underamplification_rate": 0.0,
      "residual_help_rate": 0.9999674434463183,
      "residual_harm_rate": 3.255208381839717e-05,
      "token_to_sequence_transfer_ratio": 0.08074121141299757
    },
    "dyck": {
      "avg_loss": 0.33659559550384677,
      "avg_accuracy": 0.0786744061249319,
      "correct_class_logit_delta": 4.1738424102465315,
      "incorrect_class_logit_delta_mean": 3.7293781290451693,
      "incorrect_class_logit_delta_max": 5.214117914438248,
      "delta_correct_minus_top_wrong": -1.0402754805982113,
      "incorrect_logit_overamplification_rate": 0.9263240409394103,
      "correct_logit_underamplification_rate": 0.0,
      "residual_help_rate": 0.9999999813735485,
      "residual_harm_rate": 0.0,
      "token_to_sequence_transfer_ratio": 0.024843955656942664
    },
    "listops": {
      "avg_loss": 1.3692205734550953,
      "avg_accuracy": 0.20945907993034882,
      "correct_class_logit_delta": 2.9735691025853157,
      "incorrect_class_logit_delta_mean": 1.9765026196837425,
      "incorrect_class_logit_delta_max": 5.21066752076149,
      "delta_correct_minus_top_wrong": -2.2370984479784966,
      "incorrect_logit_overamplification_rate": 0.8467087112367153,
      "correct_logit_underamplification_rate": 0.1560296209063381,
      "residual_help_rate": 0.8685627579689026,
      "residual_harm_rate": 0.13143724540714175,
      "token_to_sequence_transfer_ratio": 0.08137225201611724
    },
    "scan_style": {
      "avg_loss": 0.23808985389769077,
      "avg_accuracy": 0.08497863072974252,
      "correct_class_logit_delta": 4.12590654194355,
      "incorrect_class_logit_delta_mean": 3.6454086005687714,
      "incorrect_class_logit_delta_max": 5.027536749839783,
      "delta_correct_minus_top_wrong": -0.9016300924122334,
      "incorrect_logit_overamplification_rate": 0.9057612903416157,
      "correct_logit_underamplification_rate": 0.0,
      "residual_help_rate": 0.999999986961484,
      "residual_harm_rate": 0.0,
      "token_to_sequence_transfer_ratio": 0.02631318707638805
    }
  }
}
```