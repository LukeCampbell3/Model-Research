# PVR-EC-O Genuine Benchmark Program Gate

Status: `NOT_RUN_MISSING_DATA`

This report distinguishes primary generalized baselines, public external positioning, and internal strong-router controls.
Do not infer an architecture win from missing checkpoints, missing data, infrastructure execution, or internal control comparisons.

Allowed comparison language:
- PVR-EC-O does not yet beat generalized baselines.
- PVR-EC-O beats generalized baselines but lags internal strong-router control.
- PVR-EC-O matches internal strong-router control.
- PVR-EC-O beats internal strong-router control.

```json
{
  "benchmark_evidence": false,
  "completed": false,
  "created_at": "2026-06-12T02:59:17.147599+00:00",
  "environment": {
    "cwd": "/workspace",
    "machine": "x86_64",
    "platform": "Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35",
    "processor": "x86_64",
    "python": "3.10.13"
  },
  "git_commit": "68b36a5ceb130c263177e840f906b8c33ff2dd52",
  "hard_routing_invariants": {
    "owners_per_token": 1.0,
    "production_map_mutated": false,
    "runtime_dynamic_k_count": 0,
    "runtime_expert_choice_count": 0,
    "top2_execution_count": 0,
    "top4_execution_count": 0
  },
  "invalid_claims_blocked": [
    "model construction is not benchmark evidence",
    "finite forward probes are not benchmark evidence",
    "mock checkpoints are rejected",
    "toy data is not a genuine benchmark",
    "missing data/checkpoints cannot be converted into architecture results"
  ],
  "missing_required_artifacts_by_model": {
    "dense_transformer_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "generic_top2_moe_reference_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "pvr_ec_o_full_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "routing_diagnostics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "pvr_ec_o_no_contrastive_geometry_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "routing_diagnostics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "pvr_ec_o_no_descriptor_operator_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "routing_diagnostics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "pvr_ec_o_no_prototypes_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "routing_diagnostics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "pvr_ec_o_shared_only_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "routing_diagnostics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    },
    "vanilla_switch_top1_reference_100m": {
      "broad_nlp_metrics": false,
      "coding_metrics": false,
      "contamination_scan": false,
      "heldout_lm_metrics": false,
      "scorecard": false,
      "trained_checkpoint": false,
      "training_curve": false
    }
  },
  "model_audits": [
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "primary_generalized_baseline",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "dense_transformer",
      "model_variant": "dense_transformer_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": null,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/dense_transformer_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/dense_transformer_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/dense_transformer_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/dense_transformer_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 2.0,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "vanilla_switch_top1_reference",
      "model_variant": "vanilla_switch_top1_reference_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": null,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/vanilla_switch_top1_reference_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/vanilla_switch_top1_reference_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/vanilla_switch_top1_reference_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/vanilla_switch_top1_reference_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_primary",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_full_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": false,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        "hard_invariants_validated": false,
        "required_metrics": [
          "owners_per_token",
          "top2_execution_count",
          "top4_execution_count",
          "runtime_dynamic_k_count",
          "runtime_expert_choice_count",
          "prototype_entropy",
          "prototype_margin",
          "owner_entropy",
          "owner_churn",
          "expert_utilization",
          "expert_gini",
          "prototype_monopoly_rate",
          "high_gap_monopoly_rate",
          "challenger_disagreement_rate",
          "stale_owner_rate",
          "descriptor_control_margin",
          "operator_control_margin",
          "failure_mode_distribution"
        ],
        "status": "NOT_RUN_MISSING_CHECKPOINT"
      },
      "routing_diagnostics_required": true,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/pvr_ec_o_full_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_full_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_full_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/pvr_ec_o_full_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "primary_generalized_reference_moe",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "generic_top2_moe_reference",
      "model_variant": "generic_top2_moe_reference_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": null,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/generic_top2_moe_reference_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/generic_top2_moe_reference_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/generic_top2_moe_reference_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/generic_top2_moe_reference_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 1.0,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_prototypes_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": false,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        "hard_invariants_validated": false,
        "required_metrics": [
          "owners_per_token",
          "top2_execution_count",
          "top4_execution_count",
          "runtime_dynamic_k_count",
          "runtime_expert_choice_count",
          "prototype_entropy",
          "prototype_margin",
          "owner_entropy",
          "owner_churn",
          "expert_utilization",
          "expert_gini",
          "prototype_monopoly_rate",
          "high_gap_monopoly_rate",
          "challenger_disagreement_rate",
          "stale_owner_rate",
          "descriptor_control_margin",
          "operator_control_margin",
          "failure_mode_distribution"
        ],
        "status": "NOT_RUN_MISSING_CHECKPOINT"
      },
      "routing_diagnostics_required": true,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_prototypes_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_prototypes_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_prototypes_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/pvr_ec_o_no_prototypes_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": false,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        "hard_invariants_validated": false,
        "required_metrics": [
          "owners_per_token",
          "top2_execution_count",
          "top4_execution_count",
          "runtime_dynamic_k_count",
          "runtime_expert_choice_count",
          "prototype_entropy",
          "prototype_margin",
          "owner_entropy",
          "owner_churn",
          "expert_utilization",
          "expert_gini",
          "prototype_monopoly_rate",
          "high_gap_monopoly_rate",
          "challenger_disagreement_rate",
          "stale_owner_rate",
          "descriptor_control_margin",
          "operator_control_margin",
          "failure_mode_distribution"
        ],
        "status": "NOT_RUN_MISSING_CHECKPOINT"
      },
      "routing_diagnostics_required": true,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_contrastive_geometry_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_contrastive_geometry_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_contrastive_geometry_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/pvr_ec_o_no_contrastive_geometry_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_descriptor_operator_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": false,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        "hard_invariants_validated": false,
        "required_metrics": [
          "owners_per_token",
          "top2_execution_count",
          "top4_execution_count",
          "runtime_dynamic_k_count",
          "runtime_expert_choice_count",
          "prototype_entropy",
          "prototype_margin",
          "owner_entropy",
          "owner_churn",
          "expert_utilization",
          "expert_gini",
          "prototype_monopoly_rate",
          "high_gap_monopoly_rate",
          "challenger_disagreement_rate",
          "stale_owner_rate",
          "descriptor_control_margin",
          "operator_control_margin",
          "failure_mode_distribution"
        ],
        "status": "NOT_RUN_MISSING_CHECKPOINT"
      },
      "routing_diagnostics_required": true,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_descriptor_operator_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_descriptor_operator_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_no_descriptor_operator_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/pvr_ec_o_no_descriptor_operator_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    },
    {
      "can_claim_benchmark_evidence": false,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_MISSING_DATA",
          "bbh": "NOT_RUN_MISSING_DATA",
          "bigcodebench_complete": "NOT_RUN_MISSING_DATA",
          "bigcodebench_instruct": "NOT_RUN_MISSING_DATA",
          "boolq": "NOT_RUN_MISSING_DATA",
          "code_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "general_heldout_lm_loss": "NOT_RUN_MISSING_DATA",
          "gpqa": "NOT_RUN_MISSING_DATA",
          "gsm8k": "NOT_RUN_MISSING_DATA",
          "hellaswag": "NOT_RUN_MISSING_DATA",
          "humaneval_plus": "NOT_RUN_MISSING_DATA",
          "ifeval": "NOT_RUN_MISSING_DATA",
          "json_schema_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "livecodebench": "NOT_RUN_MISSING_DATA",
          "long_context_loss_by_position": "NOT_RUN_MISSING_DATA",
          "math_heavy_heldout_loss": "NOT_RUN_MISSING_DATA",
          "math_lvl_5": "NOT_RUN_MISSING_DATA",
          "mbpp_plus": "NOT_RUN_MISSING_DATA",
          "mmlu_pro": "NOT_RUN_MISSING_DATA",
          "musr": "NOT_RUN_MISSING_DATA",
          "perplexity": "NOT_RUN_MISSING_DATA",
          "rare_token_loss": "NOT_RUN_MISSING_DATA",
          "repobench": "NOT_RUN_MISSING_DATA",
          "truthfulqa": "NOT_RUN_MISSING_DATA",
          "winogrande": "NOT_RUN_MISSING_DATA"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "missing_eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding"
        ],
        "status": "NOT_RUN_MISSING_DATA"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_shared_only_100m",
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": false,
        "contamination_scan": false,
        "heldout_lm_metrics": false,
        "routing_diagnostics": false,
        "scorecard": false,
        "trained_checkpoint": false,
        "training_curve": false
      },
      "routing_diagnostics": {
        "hard_invariants": {
          "owners_per_token": 1.0,
          "production_map_mutated": false,
          "runtime_dynamic_k_count": 0,
          "runtime_expert_choice_count": 0,
          "top2_execution_count": 0,
          "top4_execution_count": 0
        },
        "hard_invariants_validated": false,
        "required_metrics": [
          "owners_per_token",
          "top2_execution_count",
          "top4_execution_count",
          "runtime_dynamic_k_count",
          "runtime_expert_choice_count",
          "prototype_entropy",
          "prototype_margin",
          "owner_entropy",
          "owner_churn",
          "expert_utilization",
          "expert_gini",
          "prototype_monopoly_rate",
          "high_gap_monopoly_rate",
          "challenger_disagreement_rate",
          "stale_owner_rate",
          "descriptor_control_margin",
          "operator_control_margin",
          "failure_mode_distribution"
        ],
        "status": "NOT_RUN_MISSING_CHECKPOINT"
      },
      "routing_diagnostics_required": true,
      "seeds": {
        "completed_seeds": [],
        "missing_seeds": [
          42,
          123,
          777
        ],
        "reason": "Real training/eval prerequisites are absent; no seed can be counted.",
        "required_seeds": [
          42,
          123,
          777
        ],
        "rows": [
          {
            "checkpoint": "checkpoints/pvr_ec_o_shared_only_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_shared_only_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/pvr_ec_o_shared_only_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_MISSING_DATA",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "NOT_RUN_MISSING_DATA",
      "trained_checkpoint": {
        "exists": false,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/pvr_ec_o_shared_only_100m/model.safetensors"
      },
      "training": {
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [
          "data/broad_nlp_train"
        ],
        "status": "NOT_RUN_MISSING_DATA",
        "training_curve_exists": false,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ]
      }
    }
  ],
  "model_count": 8,
  "next_required_inputs": [
    "real training data at data/broad_nlp_train and data/code_train",
    "real heldout/eval data at data/eval/broad_nlp and data/eval/coding",
    "trained checkpoints for every model/seed in the tier",
    "implemented official or explicitly reduced benchmark adapters",
    "completed contamination scan with dataset hashes"
  ],
  "reproducibility_manifest": "benchmark/reports/generated/genuine_program_100m_docker/genuine_program_reproducibility_manifest.json",
  "required_benchmarks": {
    "broad_nlp": [
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
      "gsm8k"
    ],
    "coding": [
      "humaneval_plus",
      "mbpp_plus",
      "bigcodebench_complete",
      "bigcodebench_instruct",
      "livecodebench",
      "repobench"
    ],
    "language_modeling": [
      "general_heldout_lm_loss",
      "perplexity",
      "code_heavy_heldout_loss",
      "math_heavy_heldout_loss",
      "json_schema_heavy_heldout_loss",
      "long_context_loss_by_position",
      "rare_token_loss"
    ],
    "routing_diagnostics": [
      "owners_per_token",
      "top2_execution_count",
      "top4_execution_count",
      "runtime_dynamic_k_count",
      "runtime_expert_choice_count",
      "prototype_entropy",
      "prototype_margin",
      "owner_entropy",
      "owner_churn",
      "expert_utilization",
      "expert_gini",
      "prototype_monopoly_rate",
      "high_gap_monopoly_rate",
      "challenger_disagreement_rate",
      "stale_owner_rate",
      "descriptor_control_margin",
      "operator_control_margin",
      "failure_mode_distribution"
    ]
  },
  "required_seeds": [
    42,
    123,
    777
  ],
  "schema_version": "1.0",
  "seed_policy": "3 seeds required for 100M tier unless explicitly resource blocked.",
  "size": "100m",
  "status": "NOT_RUN_MISSING_DATA",
  "suite": {
    "evidence_rule": "Only runs with real checkpoint, real data, routing diagnostics, contamination scan, and scorecards count as benchmark evidence.",
    "models": [
      {
        "comparison_group": "primary_generalized_baseline",
        "config_path": "benchmark/configs/generated/dense_transformer_100m.yaml",
        "model_variant": "dense_transformer_100m"
      },
      {
        "comparison_group": "primary_generalized_reference_moe",
        "config_path": "benchmark/configs/generated/vanilla_switch_top1_reference_100m.yaml",
        "model_variant": "vanilla_switch_top1_reference_100m"
      },
      {
        "comparison_group": "pvr_ec_o_primary",
        "config_path": "benchmark/configs/generated/pvr_ec_o_full_100m.yaml",
        "model_variant": "pvr_ec_o_full_100m"
      },
      {
        "comparison_group": "primary_generalized_reference_moe",
        "config_path": "benchmark/configs/generated/generic_top2_moe_reference_100m.yaml",
        "model_variant": "generic_top2_moe_reference_100m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_prototypes_100m.yaml",
        "model_variant": "pvr_ec_o_no_prototypes_100m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_contrastive_geometry_100m.yaml",
        "model_variant": "pvr_ec_o_no_contrastive_geometry_100m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_no_descriptor_operator_100m.yaml",
        "model_variant": "pvr_ec_o_no_descriptor_operator_100m"
      },
      {
        "comparison_group": "pvr_ec_o_ablation",
        "config_path": "benchmark/configs/generated/pvr_ec_o_shared_only_100m.yaml",
        "model_variant": "pvr_ec_o_shared_only_100m"
      }
    ],
    "required_artifacts": [
      "scorecards",
      "manifests",
      "routing_diagnostics",
      "contamination_scan",
      "benchmark_report"
    ],
    "schema_version": "1.0",
    "stage": "genuine_100m_architecture_benchmark",
    "subset_label": "genuine_reduced_eval",
    "suite_name": "pvr_ec_o_100m_genuine_architecture_benchmark"
  },
  "suite_artifacts": {
    "benchmark_evidence_count": 0,
    "path": "benchmark/reports/generated/genuine_program_100m_docker/scorecard_artifacts/benchmark_suite_result.json",
    "status": "NOT_RUN_MISSING_CHECKPOINT"
  },
  "suite_path": "benchmark/configs/generated/benchmark_100m_suite.yaml",
  "target_status": "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE"
}
```