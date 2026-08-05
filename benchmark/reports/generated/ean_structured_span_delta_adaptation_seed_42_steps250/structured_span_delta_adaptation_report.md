# EAN Structured-Span Delta Adaptation

Status: `PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED`

```json
{
  "benchmark_evidence_caveat": "diagnostic structured replay uses reduced eval structured files; do not treat as official promotion evidence",
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation",
  "comparison": {
    "baseline_mean_eval_loss": 4.856676840782166,
    "baseline_pvr_lm_loss": 3.422222343683243,
    "dense_lm_loss": 3.305846790075302,
    "ean_lm_loss": 3.010810148715973,
    "repaired_lm_loss": 3.182013305425644,
    "repaired_mean_eval_loss": 4.320738124847412,
    "repaired_minus_baseline_lm_loss": -0.24020903825759898,
    "repaired_minus_baseline_mean_eval_loss": -0.535938715934754,
    "repaired_minus_dense_lm_loss": -0.12383348464965804,
    "repaired_minus_ean_lm_loss": 0.1712031567096708,
    "scorecard_preserved_within_0_01": false,
    "structured_outliers_improved": true,
    "top1_invariants_clean": true
  },
  "created_at": "2026-06-17T03:26:34.251773+00:00",
  "decision_rule": "support requires clean Top1, scorecard preserved within 0.01 of EAN while still beating dense/baseline, and both structured outlier deltas shrinking",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "lrs": {
    "expert_lr": 1e-05,
    "router_lr": 1e-06,
    "trunk_lr": 0.0
  },
  "max_steps": 250,
  "parameter_counts": {
    "expert_delta": 81632064,
    "frozen": 202928848,
    "router": 196608,
    "trunk": 0
  },
  "row": {
    "checkpoint_exists": true,
    "checkpoint_manifest": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/checkpoint_manifest.json",
    "checkpoint_path": "checkpoints/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/checkpoint.pt",
    "effective_batch_tokens": 256,
    "error": null,
    "eval_curve": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/eval_curve.json",
    "eval_window_count": 5,
    "final_loss": 3.8808674812316895,
    "gpu_hours": 0.012562170426050822,
    "hardware_manifest": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/hardware_manifest.json",
    "model_variant": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42",
    "optimizer_steps": 250,
    "routing_curve": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/routing_curve.json",
    "routing_window_count": 5,
    "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
    "throughput_log": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/throughput_log.json",
    "tokens_seen": 64000,
    "training_curve": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/training_curve.json",
    "training_tokens_seen": 64000,
    "vram_peak": 1915299328
  },
  "schema_version": "1.0",
  "scorecard": {
    "benchmark_evidence": true,
    "benchmark_subset_label": "genuine_reduced_eval",
    "config": {
      "ablation": null,
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "batch_tokens": 1048576,
      "checkpoint_path": "checkpoints/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/checkpoint.pt",
      "comparison_group": "pvr_ec_o_primary",
      "contamination_scan_required": true,
      "context_length": 4096,
      "copy_scope": "embeddings_attention_norms",
      "created_at": "2026-06-13T11:43:11.123247+00:00",
      "diagnostic_only": true,
      "eval_data_paths": [
        "data/eval/broad_nlp",
        "data/eval/coding",
        "data/eval/routing_probes"
      ],
      "eval_suite": [
        "lm_c4_heldout",
        "lm_wikitext_103",
        "lm_pg19",
        "mmlu_pro",
        "gpqa",
        "bbh",
        "musr",
        "math_lvl_5",
        "ifeval",
        "arc_challenge",
        "hellaswag",
        "truthfulqa",
        "winogrande",
        "boolq",
        "gsm8k",
        "routing_sensitive_nlp_probes",
        "humaneval_plus",
        "mbpp_plus",
        "bigcodebench_complete",
        "bigcodebench_instruct",
        "livecodebench",
        "repobench"
      ],
      "experts_active_per_token": 1,
      "fairness_views": [
        "parameter_matched",
        "active_parameter_matched",
        "training_token_matched",
        "wall_clock_matched",
        "inference_budget_matched"
      ],
      "hidden_size": 1024,
      "is_internal_strong_router_control": false,
      "is_primary_baseline": false,
      "model_family": "pvr_ec_o",
      "model_size_label": "300m",
      "model_variant": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42",
      "num_experts_if_applicable": 8,
      "num_heads": 16,
      "num_layers": 24,
      "optimizer": "adamw",
      "output_path": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42",
      "precision": "bf16",
      "public_positioning_only": false,
      "repair": "structured_span_delta_adaptation",
      "scheduler": "cosine_with_warmup",
      "schema_version": "1.0",
      "tokenizer": "tiktoken_compatible_bpe",
      "total_params": 300000000,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens": 60000000000
    },
    "created_at": "2026-06-17T03:26:17.951586+00:00",
    "environment": {
      "cwd": "/workspace",
      "machine": "x86_64",
      "platform": "Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35",
      "processor": "x86_64",
      "python": "3.10.13"
    },
    "error": null,
    "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
    "limit": 200,
    "notes": "No benchmark evidence is claimed unless real checkpoint and data are present.",
    "schema_version": "1.0",
    "scorecard": {
      "active_params_per_token": 105000000,
      "bbh": null,
      "bits_per_byte": null,
      "brier_score": null,
      "calibration_ece": null,
      "checkpoint": "checkpoints/ean_structured_span_delta_adaptation_seed_42_steps250/pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42/checkpoint.pt",
      "code_eval_token_count": 12800,
      "code_token_loss": 6.046538553237915,
      "contamination_scan": "CONTAMINATION_STATUS_UNKNOWN",
      "context_length": 4096,
      "copy_span_loss": null,
      "eval_latency_ms_per_token": 0.7280853064730763,
      "eval_manifest_hash": "079c69bfbcab72c9499ef60ed6122486803a6970b7b6b69cdbe154463d244c74",
      "eval_token_count": 51200,
      "gpqa": null,
      "gpu_hours": null,
      "hardware": "not_run",
      "heldout_eval_token_count": 12800,
      "ifeval": null,
      "json_schema_eval_token_count": 12800,
      "json_token_loss": 6.046538553237915,
      "lm_loss": 3.182013305425644,
      "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
      "loss_by_descriptor_family": null,
      "loss_by_operator_family": null,
      "math_eval_token_count": 12800,
      "math_lvl_5": null,
      "math_token_loss": 6.046538553237915,
      "mmlu_pro": null,
      "model": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation_seed_42",
      "musr": null,
      "official_broad_nlp": {
        "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
        "bbh": "NOT_RUN_NOT_IMPLEMENTED",
        "boolq": "NOT_RUN_NOT_IMPLEMENTED",
        "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
        "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
        "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
        "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
        "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
        "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
        "musr": "NOT_RUN_NOT_IMPLEMENTED",
        "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
        "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "perplexity": 24.095215779723205,
      "prompt_sensitivity": null,
      "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
      "throughput": 1373.4654320166242,
      "tokenizer": "tiktoken_compatible_bpe",
      "tokens_evaluated": 51200,
      "total_params": 300000000,
      "training_data_manifest_hash": "4f82d92e02004043cedcdc63e1a63a644a6d6f05bea9484c2a50a598c058ee6d",
      "training_tokens": 60000000000,
      "truthfulqa": null,
      "vram_peak": 2850865152,
      "wall_clock": null
    },
    "scorecard_type": "nlp",
    "status": "GENUINE_REDUCED_EVAL"
  },
  "seed": 42,
  "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED",
  "structured_replay_paths": [
    "data/eval/coding/humaneval_base.jsonl",
    "data/eval/broad_nlp/json_schema_test_suite_type.txt",
    "data/eval/broad_nlp/cpython_json_decoder.txt",
    "data/eval/broad_nlp/the_algorithms_prime_numbers.txt"
  ],
  "structured_windows": {
    "windows": {
      "3600": {
        "dense_300m": {
          "delta_vs_baseline": 3.492197036743164,
          "loss": 12.357633590698242
        },
        "ean_seed42": {
          "delta_vs_baseline": 2.7385520935058594,
          "loss": 11.603988647460938
        },
        "pvr_baseline_seed42": {
          "delta_vs_baseline": 0.0,
          "loss": 8.865436553955078
        },
        "repaired_ean": {
          "delta_vs_baseline": -1.571742057800293,
          "loss": 7.293694496154785
        }
      },
      "4000": {
        "dense_300m": {
          "delta_vs_baseline": 5.258472442626953,
          "loss": 16.326175689697266
        },
        "ean_seed42": {
          "delta_vs_baseline": 3.838240623474121,
          "loss": 14.905943870544434
        },
        "pvr_baseline_seed42": {
          "delta_vs_baseline": 0.0,
          "loss": 11.067703247070312
        },
        "repaired_ean": {
          "delta_vs_baseline": -4.0662994384765625,
          "loss": 7.00140380859375
        }
      }
    }
  }
}
```
