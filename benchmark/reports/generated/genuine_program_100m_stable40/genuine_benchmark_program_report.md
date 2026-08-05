# PVR-EC-O Genuine Benchmark Program Gate

Status: `PVR_EC_O_100M_STABLE_LEARNING_BENCHMARK_COMPLETE`

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
    "min_eval_windows": 4,
    "min_heldout_eval_tokens": 256,
    "min_optimizer_steps": 40,
    "min_training_tokens": 2560
  },
  "completed": true,
  "created_at": "2026-06-12T03:44:24.197476+00:00",
  "environment": {
    "cwd": "/workspace",
    "machine": "x86_64",
    "platform": "Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35",
    "processor": "x86_64",
    "python": "3.10.13"
  },
  "git_commit": "6b182db68405ade30e47a158e0ee1b176a78aedb",
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/dense_transformer_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -20.449066162109375,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 0,
        "train_eval_gap": -17.35631561279297,
        "train_loss_slope": -2.7200487576998196
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
        "eval_curve": [
          {
            "eval_loss": 163.42544555664062,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 133.60658264160156,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 123.84906005859375,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 102.0782470703125,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 225.51646423339844,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 199.0096435546875,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 219.8446502685547,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 211.29547119140625,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 204.8134002685547,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 200.0974578857422,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 193.80226135253906,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 188.03955078125,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 198.91415405273438,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 142.98147583007812,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 146.50863647460938,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 173.12332153320312,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 180.02578735351562,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 177.25770568847656,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 177.26693725585938,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 158.12863159179688,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 135.50904846191406,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 141.0585174560547,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 128.7701416015625,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 139.96287536621094,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 139.0221405029297,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 128.43218994140625,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 135.5093994140625,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 134.27169799804688,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 138.8106689453125,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 138.79678344726562,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 130.2397003173828,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 132.23773193359375,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 137.92037963867188,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 125.58894348144531,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 128.57322692871094,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 129.96791076660156,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 122.79643249511719,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 121.87236785888672,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 131.09629821777344,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 118.29927825927734,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 118.07763671875,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 118.80671691894531,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 113.8514633178711,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 119.43456268310547,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [],
        "routing_curve_exists": true,
        "routing_window_count": 0,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/vanilla_switch_top1_reference_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -50.97813924153646,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 0,
        "train_eval_gap": -22.275848388671875,
        "train_loss_slope": -5.179860432942708
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
        "eval_curve": [
          {
            "eval_loss": 337.3322448730469,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 291.25762939453125,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 247.60781860351562,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 184.3978271484375,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 408.688232421875,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 378.2488098144531,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 398.53045654296875,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 403.88665771484375,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 403.9163513183594,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 378.6943664550781,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 380.9070739746094,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 378.85406494140625,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 381.3287658691406,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 281.162353515625,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 311.8952331542969,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 353.5441589355469,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 361.7492980957031,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 355.861083984375,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 361.5968322753906,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 329.310302734375,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 292.4256896972656,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 313.3062438964844,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 274.0823974609375,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 298.9272766113281,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 292.0419006347656,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 285.3226623535156,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 293.6459655761719,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 287.416259765625,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 289.0657043457031,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 278.830810546875,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 266.4830627441406,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 277.16558837890625,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 292.16796875,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 257.3257141113281,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 253.34765625,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 258.2424011230469,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 238.95155334472656,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 246.02330017089844,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 241.82861328125,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 222.33705139160156,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 222.04119873046875,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 219.40451049804688,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 209.23489379882812,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 206.67367553710938,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [],
        "routing_curve_exists": true,
        "routing_window_count": 0,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_full_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -48.10161336263021,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 4,
        "train_eval_gap": -19.5255126953125,
        "train_loss_slope": -4.850226769080529
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
        "eval_curve": [
          {
            "eval_loss": 293.95660400390625,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 257.679443359375,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 196.44078063964844,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 149.65176391601562,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 358.33612060546875,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 339.396484375,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 366.66448974609375,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 355.4526062011719,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 348.75567626953125,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 324.1797790527344,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 341.928466796875,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 327.21380615234375,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 320.7375793457031,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 243.71841430664062,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 270.986572265625,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 294.5607604980469,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 308.471923828125,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 306.4315185546875,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 298.7958984375,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 285.82037353515625,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 245.79466247558594,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 274.7617492675781,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 232.66722106933594,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 249.5158233642578,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 248.26486206054688,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 237.87734985351562,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 248.63671875,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 245.0248260498047,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 232.48721313476562,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 233.88259887695312,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 219.79600524902344,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 225.830810546875,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 232.15277099609375,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 206.13619995117188,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 199.9371337890625,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 206.2887725830078,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 192.4698486328125,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 194.39431762695312,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 199.28274536132812,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 180.24893188476562,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 182.34364318847656,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 169.31561279296875,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 163.142578125,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 169.17727661132812,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [
          {
            "expert_utilization": [
              85,
              112,
              105,
              94,
              119,
              120,
              85,
              48
            ],
            "optimizer_step": 10,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.38129279570906266,
            "prototype_monopoly_rate": 0.15625,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 10,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              96,
              118,
              118,
              81,
              91,
              152,
              80,
              32
            ],
            "optimizer_step": 20,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3745725954746983,
            "prototype_monopoly_rate": 0.19791666666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 20,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              87,
              129,
              124,
              108,
              97,
              138,
              47,
              38
            ],
            "optimizer_step": 30,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.40187414185493253,
            "prototype_monopoly_rate": 0.1796875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 30,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              70,
              129,
              142,
              108,
              82,
              152,
              62,
              23
            ],
            "optimizer_step": 40,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3902544931333978,
            "prototype_monopoly_rate": 0.19791666666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 40,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "routing_curve_exists": true,
        "routing_window_count": 4,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/generic_top2_moe_reference_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -50.904998779296875,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 0,
        "train_eval_gap": -23.870346069335938,
        "train_loss_slope": -5.357362796098758
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
        "eval_curve": [
          {
            "eval_loss": 341.312255859375,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 303.26971435546875,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 248.61070251464844,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 188.59725952148438,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 421.4047546386719,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 397.1086120605469,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 416.8789367675781,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 422.2705383300781,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 409.9248352050781,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 388.7900085449219,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 395.9178771972656,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 394.4584045410156,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 394.57403564453125,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 290.13623046875,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 315.123779296875,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 363.5445556640625,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 374.6865539550781,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 366.23016357421875,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 380.8373718261719,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 348.80975341796875,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 302.431884765625,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 318.49017333984375,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 282.339599609375,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 307.8821105957031,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 297.8370361328125,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 294.7108154296875,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 296.3460388183594,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 294.72039794921875,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 301.26580810546875,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 288.345947265625,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 280.0352478027344,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 281.2448425292969,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 293.38031005859375,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 269.2290344238281,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 259.0829772949219,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 261.94403076171875,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 241.34999084472656,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 250.09475708007812,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 246.92660522460938,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 224.35707092285156,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 222.63552856445312,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 218.98875427246094,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 212.44850158691406,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 212.4676055908203,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [],
        "routing_curve_exists": true,
        "routing_window_count": 0,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_prototypes_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -49.093424479166664,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 4,
        "train_eval_gap": -16.812255859375,
        "train_loss_slope": -4.966360238882212
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
        "eval_curve": [
          {
            "eval_loss": 291.32708740234375,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 242.88465881347656,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 186.11383056640625,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 144.04681396484375,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 354.547119140625,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 339.32965087890625,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 355.1582336425781,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 355.4416198730469,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 333.03863525390625,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 319.7528076171875,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 326.7264099121094,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 321.3393249511719,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 325.3736572265625,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 250.1696319580078,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 270.5885314941406,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 299.9837951660156,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 308.6599426269531,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 298.7458190917969,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 307.01312255859375,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 284.1883239746094,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 240.80108642578125,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 257.8878173828125,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 230.95713806152344,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 252.17015075683594,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 242.53623962402344,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 232.85313415527344,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 234.46417236328125,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 240.512451171875,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 227.32545471191406,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 217.3070526123047,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 214.4346466064453,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 218.90988159179688,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 223.7039031982422,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 202.79449462890625,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 198.03884887695312,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 202.25021362304688,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 179.5475311279297,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 189.36651611328125,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 187.23464965820312,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 167.9055938720703,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 171.98992919921875,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 160.84722900390625,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 161.38218688964844,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 160.85906982421875,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [
          {
            "expert_utilization": [
              100,
              99,
              106,
              69,
              119,
              77,
              122,
              76
            ],
            "optimizer_step": 10,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3775445629435126,
            "prototype_monopoly_rate": 0.15885416666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 10,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              91,
              117,
              80,
              64,
              94,
              98,
              150,
              74
            ],
            "optimizer_step": 20,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.40383571714240435,
            "prototype_monopoly_rate": 0.1953125,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 20,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              102,
              92,
              94,
              58,
              109,
              89,
              144,
              80
            ],
            "optimizer_step": 30,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.38219730331911705,
            "prototype_monopoly_rate": 0.1875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 30,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              97,
              106,
              104,
              41,
              101,
              91,
              142,
              86
            ],
            "optimizer_step": 40,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3932070628701088,
            "prototype_monopoly_rate": 0.18489583333333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 40,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "routing_curve_exists": true,
        "routing_window_count": 4,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_contrastive_geometry_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -48.09746297200521,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 4,
        "train_eval_gap": -20.594161987304688,
        "train_loss_slope": -5.031961685571915
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
        "eval_curve": [
          {
            "eval_loss": 284.4272766113281,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 248.95567321777344,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 189.55166625976562,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 140.1348876953125,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 356.9755554199219,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 332.36029052734375,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 352.5216064453125,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 332.8149719238281,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 348.1361389160156,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 322.1824951171875,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 322.93463134765625,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 319.4926452636719,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 326.1581115722656,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 243.26979064941406,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 259.8523864746094,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 297.4634704589844,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 297.45684814453125,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 303.86627197265625,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 296.61981201171875,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 278.05499267578125,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 247.41729736328125,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 271.5461730957031,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 234.15255737304688,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 254.39942932128906,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 237.1487274169922,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 235.89486694335938,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 235.31275939941406,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 227.43130493164062,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 231.99400329589844,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 224.09446716308594,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 211.13076782226562,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 212.31192016601562,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 220.0030059814453,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 200.01255798339844,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 196.4965057373047,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 201.967529296875,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 186.83511352539062,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 186.26976013183594,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 188.00144958496094,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 172.73236083984375,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 172.6275177001953,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 157.94911193847656,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 160.3459014892578,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 160.7290496826172,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [
          {
            "expert_utilization": [
              138,
              108,
              76,
              67,
              117,
              59,
              130,
              73
            ],
            "optimizer_step": 10,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3972638537234161,
            "prototype_monopoly_rate": 0.1796875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 10,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              143,
              81,
              81,
              69,
              103,
              58,
              169,
              64
            ],
            "optimizer_step": 20,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.39079161832341924,
            "prototype_monopoly_rate": 0.22005208333333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 20,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              136,
              80,
              85,
              56,
              120,
              54,
              179,
              58
            ],
            "optimizer_step": 30,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.38784610920508084,
            "prototype_monopoly_rate": 0.23307291666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 30,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              137,
              68,
              96,
              86,
              105,
              38,
              186,
              52
            ],
            "optimizer_step": 40,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.4065829488487604,
            "prototype_monopoly_rate": 0.2421875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 40,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "routing_curve_exists": true,
        "routing_window_count": 4,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_descriptor_operator_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -46.34294637044271,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 4,
        "train_eval_gap": -25.211944580078125,
        "train_loss_slope": -4.525656675681089
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
        "eval_curve": [
          {
            "eval_loss": 303.15472412109375,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 265.23797607421875,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 209.4932861328125,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 164.12588500976562,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 365.83843994140625,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 338.44305419921875,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 363.1042785644531,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 359.15948486328125,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 351.57049560546875,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 337.8208923339844,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 335.639404296875,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 329.118408203125,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 338.4471740722656,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 253.9190673828125,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 278.0887451171875,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 308.5006408691406,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 314.4387512207031,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 343.345703125,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 317.51116943359375,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 305.8507995605469,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 254.21298217773438,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 286.3602294921875,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 245.22874450683594,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 261.62725830078125,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 260.8840637207031,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 251.46771240234375,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 257.49652099609375,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 257.7054138183594,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 256.3338928222656,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 247.2144317626953,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 231.07601928710938,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 240.84832763671875,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 248.7170867919922,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 219.5663299560547,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 218.486572265625,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 222.49900817871094,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 205.13536071777344,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 208.0713653564453,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 213.6544647216797,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 198.91085815429688,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 194.7175750732422,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 186.6221923828125,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 181.06361389160156,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 189.33782958984375,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [
          {
            "expert_utilization": [
              74,
              68,
              97,
              108,
              159,
              125,
              84,
              53
            ],
            "optimizer_step": 10,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.32853740646775503,
            "prototype_monopoly_rate": 0.20703125,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 10,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              80,
              79,
              95,
              104,
              158,
              136,
              73,
              43
            ],
            "optimizer_step": 20,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.32875899710537243,
            "prototype_monopoly_rate": 0.20572916666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 20,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              64,
              61,
              87,
              101,
              190,
              130,
              93,
              42
            ],
            "optimizer_step": 30,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.2990112467959989,
            "prototype_monopoly_rate": 0.24739583333333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 30,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              69,
              75,
              75,
              106,
              201,
              125,
              80,
              37
            ],
            "optimizer_step": 40,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.30502122022638406,
            "prototype_monopoly_rate": 0.26171875,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 40,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "routing_curve_exists": true,
        "routing_window_count": 4,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
        "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_shared_only_100m/merged_scorecard.json",
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
      "stable_learning_gate": {
        "checks": {
          "loss_curve_slope_present": true,
          "routing_diagnostics_over_time_present": true,
          "train_eval_gap_present": true
        },
        "eval_loss_slope": -56.845115661621094,
        "eval_window_count": 4,
        "failures": {},
        "passed": true,
        "routing_window_count": 4,
        "train_eval_gap": -16.969505310058594,
        "train_loss_slope": -6.707037901267027
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
        "eval_curve": [
          {
            "eval_loss": 293.56585693359375,
            "eval_tokens": 64,
            "optimizer_step": 10,
            "step": 10,
            "training_tokens_seen": 640
          },
          {
            "eval_loss": 239.37478637695312,
            "eval_tokens": 64,
            "optimizer_step": 20,
            "step": 20,
            "training_tokens_seen": 1280
          },
          {
            "eval_loss": 161.2771759033203,
            "eval_tokens": 64,
            "optimizer_step": 30,
            "step": 30,
            "training_tokens_seen": 1920
          },
          {
            "eval_loss": 123.03050994873047,
            "eval_tokens": 64,
            "optimizer_step": 40,
            "step": 40,
            "training_tokens_seen": 2560
          }
        ],
        "eval_curve_exists": true,
        "eval_window_count": 4,
        "loss_curve": [
          {
            "effective_batch_tokens": 64,
            "loss": 401.5744934082031,
            "optimizer_step": 1,
            "step": 1,
            "tokens_seen": 64,
            "training_tokens_seen": 64
          },
          {
            "effective_batch_tokens": 64,
            "loss": 368.106689453125,
            "optimizer_step": 2,
            "step": 2,
            "tokens_seen": 128,
            "training_tokens_seen": 128
          },
          {
            "effective_batch_tokens": 64,
            "loss": 388.6014099121094,
            "optimizer_step": 3,
            "step": 3,
            "tokens_seen": 192,
            "training_tokens_seen": 192
          },
          {
            "effective_batch_tokens": 64,
            "loss": 392.60467529296875,
            "optimizer_step": 4,
            "step": 4,
            "tokens_seen": 256,
            "training_tokens_seen": 256
          },
          {
            "effective_batch_tokens": 64,
            "loss": 364.729248046875,
            "optimizer_step": 5,
            "step": 5,
            "tokens_seen": 320,
            "training_tokens_seen": 320
          },
          {
            "effective_batch_tokens": 64,
            "loss": 343.6820068359375,
            "optimizer_step": 6,
            "step": 6,
            "tokens_seen": 384,
            "training_tokens_seen": 384
          },
          {
            "effective_batch_tokens": 64,
            "loss": 350.0600280761719,
            "optimizer_step": 7,
            "step": 7,
            "tokens_seen": 448,
            "training_tokens_seen": 448
          },
          {
            "effective_batch_tokens": 64,
            "loss": 337.7404479980469,
            "optimizer_step": 8,
            "step": 8,
            "tokens_seen": 512,
            "training_tokens_seen": 512
          },
          {
            "effective_batch_tokens": 64,
            "loss": 338.495361328125,
            "optimizer_step": 9,
            "step": 9,
            "tokens_seen": 576,
            "training_tokens_seen": 576
          },
          {
            "effective_batch_tokens": 64,
            "loss": 250.4470977783203,
            "optimizer_step": 10,
            "step": 10,
            "tokens_seen": 640,
            "training_tokens_seen": 640
          },
          {
            "effective_batch_tokens": 64,
            "loss": 269.55267333984375,
            "optimizer_step": 11,
            "step": 11,
            "tokens_seen": 704,
            "training_tokens_seen": 704
          },
          {
            "effective_batch_tokens": 64,
            "loss": 299.34039306640625,
            "optimizer_step": 12,
            "step": 12,
            "tokens_seen": 768,
            "training_tokens_seen": 768
          },
          {
            "effective_batch_tokens": 64,
            "loss": 305.9905700683594,
            "optimizer_step": 13,
            "step": 13,
            "tokens_seen": 832,
            "training_tokens_seen": 832
          },
          {
            "effective_batch_tokens": 64,
            "loss": 320.8599548339844,
            "optimizer_step": 14,
            "step": 14,
            "tokens_seen": 896,
            "training_tokens_seen": 896
          },
          {
            "effective_batch_tokens": 64,
            "loss": 303.40057373046875,
            "optimizer_step": 15,
            "step": 15,
            "tokens_seen": 960,
            "training_tokens_seen": 960
          },
          {
            "effective_batch_tokens": 64,
            "loss": 280.361083984375,
            "optimizer_step": 16,
            "step": 16,
            "tokens_seen": 1024,
            "training_tokens_seen": 1024
          },
          {
            "effective_batch_tokens": 64,
            "loss": 235.32240295410156,
            "optimizer_step": 17,
            "step": 17,
            "tokens_seen": 1088,
            "training_tokens_seen": 1088
          },
          {
            "effective_batch_tokens": 64,
            "loss": 254.99391174316406,
            "optimizer_step": 18,
            "step": 18,
            "tokens_seen": 1152,
            "training_tokens_seen": 1152
          },
          {
            "effective_batch_tokens": 64,
            "loss": 222.46376037597656,
            "optimizer_step": 19,
            "step": 19,
            "tokens_seen": 1216,
            "training_tokens_seen": 1216
          },
          {
            "effective_batch_tokens": 64,
            "loss": 233.4862518310547,
            "optimizer_step": 20,
            "step": 20,
            "tokens_seen": 1280,
            "training_tokens_seen": 1280
          },
          {
            "effective_batch_tokens": 64,
            "loss": 230.31045532226562,
            "optimizer_step": 21,
            "step": 21,
            "tokens_seen": 1344,
            "training_tokens_seen": 1344
          },
          {
            "effective_batch_tokens": 64,
            "loss": 214.7998809814453,
            "optimizer_step": 22,
            "step": 22,
            "tokens_seen": 1408,
            "training_tokens_seen": 1408
          },
          {
            "effective_batch_tokens": 64,
            "loss": 215.4672393798828,
            "optimizer_step": 23,
            "step": 23,
            "tokens_seen": 1472,
            "training_tokens_seen": 1472
          },
          {
            "effective_batch_tokens": 64,
            "loss": 218.4500274658203,
            "optimizer_step": 24,
            "step": 24,
            "tokens_seen": 1536,
            "training_tokens_seen": 1536
          },
          {
            "effective_batch_tokens": 64,
            "loss": 204.17840576171875,
            "optimizer_step": 25,
            "step": 25,
            "tokens_seen": 1600,
            "training_tokens_seen": 1600
          },
          {
            "effective_batch_tokens": 64,
            "loss": 193.08827209472656,
            "optimizer_step": 26,
            "step": 26,
            "tokens_seen": 1664,
            "training_tokens_seen": 1664
          },
          {
            "effective_batch_tokens": 64,
            "loss": 187.14605712890625,
            "optimizer_step": 27,
            "step": 27,
            "tokens_seen": 1728,
            "training_tokens_seen": 1728
          },
          {
            "effective_batch_tokens": 64,
            "loss": 190.57977294921875,
            "optimizer_step": 28,
            "step": 28,
            "tokens_seen": 1792,
            "training_tokens_seen": 1792
          },
          {
            "effective_batch_tokens": 64,
            "loss": 204.66220092773438,
            "optimizer_step": 29,
            "step": 29,
            "tokens_seen": 1856,
            "training_tokens_seen": 1856
          },
          {
            "effective_batch_tokens": 64,
            "loss": 175.2816619873047,
            "optimizer_step": 30,
            "step": 30,
            "tokens_seen": 1920,
            "training_tokens_seen": 1920
          },
          {
            "effective_batch_tokens": 64,
            "loss": 168.64064025878906,
            "optimizer_step": 31,
            "step": 31,
            "tokens_seen": 1984,
            "training_tokens_seen": 1984
          },
          {
            "effective_batch_tokens": 64,
            "loss": 174.80987548828125,
            "optimizer_step": 32,
            "step": 32,
            "tokens_seen": 2048,
            "training_tokens_seen": 2048
          },
          {
            "effective_batch_tokens": 64,
            "loss": 162.1143035888672,
            "optimizer_step": 33,
            "step": 33,
            "tokens_seen": 2112,
            "training_tokens_seen": 2112
          },
          {
            "effective_batch_tokens": 64,
            "loss": 163.4752197265625,
            "optimizer_step": 34,
            "step": 34,
            "tokens_seen": 2176,
            "training_tokens_seen": 2176
          },
          {
            "effective_batch_tokens": 64,
            "loss": 164.21279907226562,
            "optimizer_step": 35,
            "step": 35,
            "tokens_seen": 2240,
            "training_tokens_seen": 2240
          },
          {
            "effective_batch_tokens": 64,
            "loss": 145.58203125,
            "optimizer_step": 36,
            "step": 36,
            "tokens_seen": 2304,
            "training_tokens_seen": 2304
          },
          {
            "effective_batch_tokens": 64,
            "loss": 147.35687255859375,
            "optimizer_step": 37,
            "step": 37,
            "tokens_seen": 2368,
            "training_tokens_seen": 2368
          },
          {
            "effective_batch_tokens": 64,
            "loss": 138.5817413330078,
            "optimizer_step": 38,
            "step": 38,
            "tokens_seen": 2432,
            "training_tokens_seen": 2432
          },
          {
            "effective_batch_tokens": 64,
            "loss": 136.9321746826172,
            "optimizer_step": 39,
            "step": 39,
            "tokens_seen": 2496,
            "training_tokens_seen": 2496
          },
          {
            "effective_batch_tokens": 64,
            "loss": 140.00001525878906,
            "optimizer_step": 40,
            "step": 40,
            "tokens_seen": 2560,
            "training_tokens_seen": 2560
          }
        ],
        "missing_training_data_paths": [],
        "optimizer_steps": 40,
        "routing_curve": [
          {
            "expert_utilization": [
              95,
              100,
              105,
              73,
              119,
              105,
              100,
              71
            ],
            "optimizer_step": 10,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3731051178571458,
            "prototype_monopoly_rate": 0.15494791666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 10,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              91,
              91,
              94,
              82,
              113,
              96,
              106,
              95
            ],
            "optimizer_step": 20,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.36564026186048676,
            "prototype_monopoly_rate": 0.14713541666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 20,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              111,
              121,
              95,
              56,
              93,
              122,
              95,
              75
            ],
            "optimizer_step": 30,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.359269428057208,
            "prototype_monopoly_rate": 0.15885416666666666,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 30,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          },
          {
            "expert_utilization": [
              96,
              136,
              94,
              70,
              77,
              129,
              80,
              86
            ],
            "optimizer_step": 40,
            "owners_per_token": 1.0,
            "production_map_mutated": false,
            "prototype_margin": 0.3554664695984684,
            "prototype_monopoly_rate": 0.17708333333333334,
            "runtime_dynamic_k_count": 0,
            "runtime_expert_choice_count": 0,
            "step": 40,
            "top2_execution_count": 0,
            "top4_execution_count": 0
          }
        ],
        "routing_curve_exists": true,
        "routing_window_count": 4,
        "status": "NOT_RUN_RESOURCE_BLOCKED",
        "training_curve_exists": true,
        "training_curve_required": true,
        "training_data_paths": [
          "data/broad_nlp_train"
        ],
        "training_tokens_seen": 2560
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
          "eval_windows": {
            "observed": 4,
            "required": 4
          },
          "heldout_eval_token_count": {
            "observed": 512,
            "required": 256
          },
          "optimizer_steps": {
            "observed": 40,
            "required": 40
          },
          "training_tokens_seen": {
            "observed": 2560,
            "required": 2560
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
  "reproducibility_manifest": "benchmark/reports/generated/genuine_program_100m_stable40/genuine_program_reproducibility_manifest.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/dense_transformer_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/generic_top2_moe_reference_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_full_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_contrastive_geometry_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_descriptor_operator_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_no_prototypes_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/pvr_ec_o_shared_only_100m/merged_scorecard.json",
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
      "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/scorecards/vanilla_switch_top1_reference_100m/merged_scorecard.json",
      "status": "GENUINE_REDUCED_EVAL"
    }
  },
  "seed_policy": "3 seeds required for 100M tier unless explicitly resource blocked.",
  "size": "100m",
  "status": "PVR_EC_O_100M_STABLE_LEARNING_BENCHMARK_COMPLETE",
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
    "path": "benchmark/reports/generated/genuine_program_100m_stable40/scorecard_artifacts/benchmark_suite_result.json",
    "status": "GENUINE_REDUCED_EVAL"
  },
  "suite_path": "benchmark/configs/generated/benchmark_100m_suite.yaml",
  "target_status": "PVR_EC_O_100M_STABLE_LEARNING_BENCHMARK_COMPLETE",
  "tier": "stable_learning"
}
```