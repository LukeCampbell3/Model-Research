# EAN Structured-Span Route-Stability Repair

Status: `PVR_EAN_STRUCTURED_SPAN_REPAIR_NOT_SUPPORTED`

```json
{
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_route_stability",
  "comparison": {
    "baseline_mean_eval_loss": 4.856676840782166,
    "baseline_pvr_lm_loss": 3.422222343683243,
    "dense_lm_loss": 3.305846790075302,
    "ean_lm_loss": 3.010810148715973,
    "repaired_lm_loss": 3.014079146385193,
    "repaired_mean_eval_loss": 5.005123496055603,
    "repaired_minus_baseline_lm_loss": -0.4081431972980498,
    "repaired_minus_baseline_mean_eval_loss": 0.14844665527343714,
    "repaired_minus_dense_lm_loss": -0.2917676436901089,
    "repaired_minus_ean_lm_loss": 0.003268997669219953,
    "top1_invariants_clean": true
  },
  "created_at": "2026-06-17T02:57:35.537941+00:00",
  "decision_rule": "support requires preserving or improving EAN scorecard loss, beating baseline/dense scorecard loss, clean Top1 invariants, and shrinking both structured outlier deltas versus EAN",
  "deprecated_paths_not_used": [
    "runtime_top2_or_top4",
    "global_dense_kl",
    "route_confidence_regularizer",
    "in_bounds_head_repair"
  ],
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "high_loss_margin": 0.25,
  "route_stability_weight": 0.02,
  "row": {
    "checkpoint_exists": true,
    "checkpoint_manifest": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/checkpoint_manifest.json",
    "checkpoint_path": "checkpoints/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/checkpoint.pt",
    "effective_batch_tokens": 256,
    "error": null,
    "eval_curve": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/eval_curve.json",
    "eval_window_count": 10,
    "final_loss": 2.5851798057556152,
    "gpu_hours": 0.2513498955965042,
    "hardware_manifest": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/hardware_manifest.json",
    "model_variant": "pvr_ec_o_full_300m_ean_structured_route_stability_seed_42",
    "optimizer_steps": 4000,
    "routing_curve": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/routing_curve.json",
    "routing_window_count": 10,
    "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
    "throughput_log": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/throughput_log.json",
    "tokens_seen": 1024000,
    "training_curve": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/training_curve.json",
    "training_tokens_seen": 1024000,
    "vram_peak": 7395591680
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
      "checkpoint_path": "checkpoints/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/checkpoint.pt",
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
      "model_variant": "pvr_ec_o_full_300m_ean_structured_route_stability_seed_42",
      "num_experts_if_applicable": 8,
      "num_heads": 16,
      "num_layers": 24,
      "optimizer": "adamw",
      "output_path": "benchmark/reports/generated/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42",
      "precision": "bf16",
      "public_positioning_only": false,
      "repair": "structured_span_route_stability",
      "scheduler": "cosine_with_warmup",
      "schema_version": "1.0",
      "tokenizer": "tiktoken_compatible_bpe",
      "total_params": 300000000,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens": 60000000000
    },
    "created_at": "2026-06-17T02:57:18.999423+00:00",
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
      "checkpoint": "checkpoints/ean_structured_span_route_stability_repair_seed_42/pvr_ec_o_full_300m_ean_structured_route_stability_seed_42/checkpoint.pt",
      "code_eval_token_count": 12800,
      "code_token_loss": 8.453881646394729,
      "contamination_scan": "CONTAMINATION_STATUS_UNKNOWN",
      "context_length": 4096,
      "copy_span_loss": null,
      "eval_latency_ms_per_token": 0.705356071703136,
      "eval_manifest_hash": "079c69bfbcab72c9499ef60ed6122486803a6970b7b6b69cdbe154463d244c74",
      "eval_token_count": 51200,
      "gpqa": null,
      "gpu_hours": null,
      "hardware": "not_run",
      "heldout_eval_token_count": 12800,
      "ifeval": null,
      "json_schema_eval_token_count": 12800,
      "json_token_loss": 8.453881646394729,
      "lm_loss": 3.014079146385193,
      "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
      "loss_by_descriptor_family": null,
      "loss_by_operator_family": null,
      "math_eval_token_count": 12800,
      "math_lvl_5": null,
      "math_token_loss": 8.453881646394729,
      "mmlu_pro": null,
      "model": "pvr_ec_o_full_300m_ean_structured_route_stability_seed_42",
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
      "perplexity": 20.370324214483883,
      "prompt_sensitivity": null,
      "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
      "throughput": 1417.723671939796,
      "tokenizer": "tiktoken_compatible_bpe",
      "tokens_evaluated": 51200,
      "total_params": 300000000,
      "training_data_manifest_hash": "4f82d92e02004043cedcdc63e1a63a644a6d6f05bea9484c2a50a598c058ee6d",
      "training_tokens": 60000000000,
      "truthfulqa": null,
      "vram_peak": 7547462144,
      "wall_clock": null
    },
    "scorecard_type": "nlp",
    "status": "GENUINE_REDUCED_EVAL"
  },
  "seed": 42,
  "status": "PVR_EAN_STRUCTURED_SPAN_REPAIR_NOT_SUPPORTED",
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
          "delta_vs_baseline": 2.7892942428588867,
          "loss": 11.654730796813965
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
          "delta_vs_baseline": 3.8363399505615234,
          "loss": 14.904043197631836
        }
      }
    }
  }
}
```
