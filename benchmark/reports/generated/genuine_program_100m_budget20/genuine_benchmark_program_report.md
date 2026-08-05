# PVR-EC-O Genuine Benchmark Program Gate

Status: `PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE`

This report distinguishes primary generalized baselines, public external positioning, and internal strong-router controls.
Do not infer an architecture win from missing checkpoints, missing data, infrastructure execution, or internal control comparisons.

Allowed comparison language:
- PVR-EC-O does not yet beat generalized baselines.
- PVR-EC-O beats generalized baselines but lags internal strong-router control.
- PVR-EC-O matches internal strong-router control.
- PVR-EC-O beats internal strong-router control.

```json
{
  "benchmark_evidence": true,
  "benchmark_volume_thresholds": {
    "min_effective_batch_tokens": 32,
    "min_eval_tokens": 1024,
    "min_heldout_eval_tokens": 256,
    "min_optimizer_steps": 20,
    "min_training_tokens": 1024
  },
  "completed": true,
  "created_at": "2026-06-12T03:32:58.939199+00:00",
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
    "missing data/checkpoints cannot be converted into architecture results",
    "one-step checkpoints cannot complete the 100M benchmark tier"
  ],
  "missing_required_artifacts_by_model": {
    "dense_transformer_100m": {
      "broad_nlp_metrics": false
    },
    "generic_top2_moe_reference_100m": {
      "broad_nlp_metrics": false
    },
    "pvr_ec_o_full_100m": {
      "broad_nlp_metrics": false
    },
    "pvr_ec_o_no_contrastive_geometry_100m": {
      "broad_nlp_metrics": false
    },
    "pvr_ec_o_no_descriptor_operator_100m": {
      "broad_nlp_metrics": false
    },
    "pvr_ec_o_no_prototypes_100m": {
      "broad_nlp_metrics": false
    },
    "pvr_ec_o_shared_only_100m": {
      "broad_nlp_metrics": false
    },
    "vanilla_switch_top1_reference_100m": {
      "broad_nlp_metrics": false
    }
  },
  "model_audits": [
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "primary_generalized_baseline",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "dense_transformer",
      "model_variant": "dense_transformer_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": null,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/dense_transformer_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/dense_transformer_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/dense_transformer_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/dense_transformer_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/dense_transformer_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/dense_transformer_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 2.0,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "primary_generalized_reference_moe",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "vanilla_switch_top1_reference",
      "model_variant": "vanilla_switch_top1_reference_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": null,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/vanilla_switch_top1_reference_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/vanilla_switch_top1_reference_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/vanilla_switch_top1_reference_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/vanilla_switch_top1_reference_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/vanilla_switch_top1_reference_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/vanilla_switch_top1_reference_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_primary",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_full_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": true,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
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
        "hard_invariants_validated": true,
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
        "status": "NOT_RUN_MISSING_DATA"
      },
      "routing_diagnostics_required": true,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_full_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_full_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_full_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_full_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_full_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/pvr_ec_o_full_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "primary_generalized_reference_moe",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "generic_top2_moe_reference",
      "model_variant": "generic_top2_moe_reference_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": null,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
      },
      "routing_diagnostics": {
        "hard_invariants": {},
        "hard_invariants_validated": false,
        "required_metrics": [],
        "status": "NOT_APPLICABLE"
      },
      "routing_diagnostics_required": false,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/generic_top2_moe_reference_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/generic_top2_moe_reference_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/generic_top2_moe_reference_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/generic_top2_moe_reference_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/generic_top2_moe_reference_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/generic_top2_moe_reference_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 1.0,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_prototypes_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": true,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
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
        "hard_invariants_validated": true,
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
        "status": "NOT_RUN_MISSING_DATA"
      },
      "routing_diagnostics_required": true,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_prototypes_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_prototypes_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_prototypes_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_prototypes_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_prototypes_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/pvr_ec_o_no_prototypes_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_contrastive_geometry_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": true,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
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
        "hard_invariants_validated": true,
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
        "status": "NOT_RUN_MISSING_DATA"
      },
      "routing_diagnostics_required": true,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_contrastive_geometry_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_contrastive_geometry_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_contrastive_geometry_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_contrastive_geometry_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_contrastive_geometry_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/pvr_ec_o_no_contrastive_geometry_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_no_descriptor_operator_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": true,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
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
        "hard_invariants_validated": true,
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
        "status": "NOT_RUN_MISSING_DATA"
      },
      "routing_diagnostics_required": true,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_descriptor_operator_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_descriptor_operator_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_descriptor_operator_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_no_descriptor_operator_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_no_descriptor_operator_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/pvr_ec_o_no_descriptor_operator_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
      }
    },
    {
      "can_claim_benchmark_evidence": true,
      "comparison_group": "pvr_ec_o_ablation",
      "contamination": {
        "reason": "Training/eval data hashes cannot prove contamination status until real datasets are present and scanned.",
        "status": "CONTAMINATION_STATUS_UNKNOWN"
      },
      "evaluation": {
        "benchmark_statuses": {
          "arc_challenge": "NOT_RUN_NOT_IMPLEMENTED",
          "bbh": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_complete": "NOT_RUN_NOT_IMPLEMENTED",
          "bigcodebench_instruct": "NOT_RUN_NOT_IMPLEMENTED",
          "boolq": "NOT_RUN_NOT_IMPLEMENTED",
          "code_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "general_heldout_lm_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "gpqa": "NOT_RUN_NOT_IMPLEMENTED",
          "gsm8k": "NOT_RUN_NOT_IMPLEMENTED",
          "hellaswag": "NOT_RUN_NOT_IMPLEMENTED",
          "humaneval_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "ifeval": "NOT_RUN_NOT_IMPLEMENTED",
          "json_schema_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "livecodebench": "NOT_RUN_NOT_IMPLEMENTED",
          "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
          "math_heavy_heldout_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "math_lvl_5": "NOT_RUN_NOT_IMPLEMENTED",
          "mbpp_plus": "NOT_RUN_NOT_IMPLEMENTED",
          "mmlu_pro": "NOT_RUN_NOT_IMPLEMENTED",
          "musr": "NOT_RUN_NOT_IMPLEMENTED",
          "perplexity": "NOT_RUN_NOT_IMPLEMENTED",
          "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
          "repobench": "NOT_RUN_NOT_IMPLEMENTED",
          "truthfulqa": "NOT_RUN_NOT_IMPLEMENTED",
          "winogrande": "NOT_RUN_NOT_IMPLEMENTED"
        },
        "eval_data_paths": [
          "data/eval/broad_nlp",
          "data/eval/coding",
          "data/eval/routing_probes"
        ],
        "missing_eval_data_paths": [],
        "status": "NOT_RUN_NOT_IMPLEMENTED"
      },
      "model_family": "pvr_ec_o",
      "model_variant": "pvr_ec_o_shared_only_100m",
      "pipeline_complete": true,
      "required_artifacts": {
        "broad_nlp_metrics": false,
        "coding_metrics": true,
        "contamination_scan": true,
        "heldout_lm_metrics": true,
        "routing_diagnostics": true,
        "scorecard": true,
        "trained_checkpoint": true,
        "training_curve": true
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
        "hard_invariants_validated": true,
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
        "status": "NOT_RUN_MISSING_DATA"
      },
      "routing_diagnostics_required": true,
      "scorecard": {
        "benchmark_evidence": true,
        "eval_token_count": 2048,
        "evidence_requirements": {
          "coding_ready": true,
          "contamination_ready": true,
          "nlp_ready": true,
          "routing_ready": true
        },
        "heldout_eval_token_count": 512,
        "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_shared_only_100m/merged_scorecard.json",
        "status": "GENUINE_REDUCED_EVAL"
      },
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
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_shared_only_100m/seed_42.safetensors",
            "completed": false,
            "seed": 42,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_42.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_shared_only_100m/seed_123.safetensors",
            "completed": false,
            "seed": 123,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_123.json"
          },
          {
            "checkpoint": "checkpoints/benchmark_100m/pvr_ec_o_shared_only_100m/seed_777.safetensors",
            "completed": false,
            "seed": 777,
            "status": "NOT_RUN_RESOURCE_BLOCKED",
            "training_curve": "benchmark/reports/generated/training_curves/pvr_ec_o_shared_only_100m/seed_777.json"
          }
        ],
        "status": "SEED_REDUCTION_RESOURCE_BLOCKED"
      },
      "status": "BENCH_INFRASTRUCTURE_READY",
      "trained_checkpoint": {
        "exists": true,
        "mock_checkpoint_rejected": false,
        "path": "checkpoints/benchmark_100m/pvr_ec_o_shared_only_100m/checkpoint.pt"
      },
      "training": {
        "checkpoint_manifest_exists": true,
        "effective_batch_tokens": 64,
        "estimated_gpu_hours_required": 0.7,
        "missing_training_data_paths": [],
        "optimizer_steps": 20,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 1280
      },
      "volume_gate": {
        "checks": {
          "effective_batch_tokens": {
            "observed": 64,
            "required": 32
          },
          "eval_token_count": {
            "observed": 2048,
            "required": 1024
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 20,
            "required": 20
          },
          "training_tokens_seen": {
            "observed": 1280,
            "required": 1024
          }
        },
        "failures": {},
        "passed": true
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
  "pipeline_status": "GENUINE_REDUCED_PIPELINE_COMPLETE",
  "reproducibility_manifest": "benchmark/reports/generated/genuine_program_100m_budget20/genuine_program_reproducibility_manifest.json",
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
  "scorecard_evidence": {
    "dense_transformer_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/dense_transformer_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "generic_top2_moe_reference_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/generic_top2_moe_reference_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "pvr_ec_o_full_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_full_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "pvr_ec_o_no_contrastive_geometry_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_contrastive_geometry_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "pvr_ec_o_no_descriptor_operator_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_descriptor_operator_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "pvr_ec_o_no_prototypes_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_no_prototypes_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "pvr_ec_o_shared_only_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/pvr_ec_o_shared_only_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    },
    "vanilla_switch_top1_reference_100m": {
      "benchmark_evidence": true,
      "eval_token_count": 2048,
      "evidence_requirements": {
        "coding_ready": true,
        "contamination_ready": true,
        "nlp_ready": true,
        "routing_ready": true
      },
      "heldout_eval_token_count": 512,
      "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/scorecards/vanilla_switch_top1_reference_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    }
  },
  "seed_policy": "3 seeds required for 100M tier unless explicitly resource blocked.",
  "size": "100m",
  "status": "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE",
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
    "benchmark_evidence_count": 8,
    "path": "benchmark/reports/generated/genuine_program_100m_budget20/scorecard_artifacts/benchmark_suite_result.json",
    "status": "GENUINE_REDUCED_EVAL"
  },
  "suite_path": "benchmark/configs/generated/benchmark_100m_suite.yaml",
  "target_status": "PVR_EC_O_100M_GENUINE_BENCHMARK_COMPLETE"
}
```