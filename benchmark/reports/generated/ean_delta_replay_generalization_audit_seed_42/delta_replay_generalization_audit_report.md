# EAN Delta Replay Generalization Audit

Status: `PVR_EAN_DELTA_REPLAY_GENERALIZATION_AUDIT_SUPPORTED`

```json
{
  "benchmark_evidence_caveat": "heldout spans are deterministic exclusions from reduced structured replay files; this is diagnostic evidence, not official benchmark promotion evidence",
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_short_structured_delta_replay",
  "comparison": {
    "baseline_pvr_lm_loss": 3.422222343683243,
    "code_token_loss": 6.90492072224617,
    "dense_lm_loss": 3.305846790075302,
    "ean_lm_loss": 3.010810148715973,
    "json_token_loss": 6.90492072224617,
    "repaired_lm_loss": 3.0021095263957975,
    "repaired_minus_baseline_lm_loss": -0.4201128172874453,
    "repaired_minus_dense_lm_loss": -0.3037372636795044,
    "repaired_minus_ean_lm_loss": -0.008700622320175544,
    "top1_invariants_clean": true
  },
  "created_at": "2026-06-17T03:35:28.913140+00:00",
  "decision_rule": "support requires held-out structured spans improving over EAN, broad LM scorecard at least matching EAN, beating dense, and clean Top1 invariants",
  "experiment": "PVR_EAN_DELTA_REPLAY_GENERALIZATION_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "heldout_spans": [
    {
      "end": 42990,
      "family": "humaneval_like",
      "path": "data/eval/coding/humaneval_base.jsonl",
      "span_id": "humaneval_like_0",
      "start": 42861
    },
    {
      "end": 85852,
      "family": "humaneval_like",
      "path": "data/eval/coding/humaneval_base.jsonl",
      "span_id": "humaneval_like_1",
      "start": 85723
    },
    {
      "end": 128714,
      "family": "humaneval_like",
      "path": "data/eval/coding/humaneval_base.jsonl",
      "span_id": "humaneval_like_2",
      "start": 128585
    },
    {
      "end": 171576,
      "family": "humaneval_like",
      "path": "data/eval/coding/humaneval_base.jsonl",
      "span_id": "humaneval_like_3",
      "start": 171447
    },
    {
      "end": 2784,
      "family": "json_schema",
      "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
      "span_id": "json_schema_0",
      "start": 2655
    },
    {
      "end": 5440,
      "family": "json_schema",
      "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
      "span_id": "json_schema_1",
      "start": 5311
    },
    {
      "end": 8096,
      "family": "json_schema",
      "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
      "span_id": "json_schema_2",
      "start": 7967
    },
    {
      "end": 10752,
      "family": "json_schema",
      "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
      "span_id": "json_schema_3",
      "start": 10623
    }
  ],
  "heldout_structured_eval": {
    "family_summary": {
      "humaneval_like": {
        "count": 4,
        "mean_repair_minus_baseline": 0.04455113410949707,
        "mean_repair_minus_dense": -4.731495976448059,
        "mean_repair_minus_ean": -2.5412726402282715,
        "win_rate_vs_ean": 1.0
      },
      "json_schema": {
        "count": 4,
        "mean_repair_minus_baseline": -0.2656276226043701,
        "mean_repair_minus_dense": -3.8870718479156494,
        "mean_repair_minus_ean": -2.8474533557891846,
        "win_rate_vs_ean": 1.0
      }
    },
    "overall": {
      "count": 8,
      "mean_repair_minus_baseline": -0.11053824424743652,
      "mean_repair_minus_dense": -4.309283912181854,
      "mean_repair_minus_ean": -2.694362998008728,
      "win_rate_vs_ean": 1.0
    },
    "rows": [
      {
        "end": 42990,
        "family": "humaneval_like",
        "losses": {
          "baseline_pvr_seed42": 9.708907127380371,
          "dense_300m": 15.193252563476562,
          "ean_seed42": 13.395232200622559,
          "repaired_delta_replay": 11.19838809967041
        },
        "path": "data/eval/coding/humaneval_base.jsonl",
        "raw_decoded_text": "\\ndef triangle_area(a, h):\\n    \\\"\\\"\\\"Given length of a side and high return area for a triangle.\\n    >>> triangle_area(5, 3)\\n",
        "repair_minus_baseline": 1.489480972290039,
        "repair_minus_dense": -3.9948644638061523,
        "repair_minus_ean": -2.1968441009521484,
        "span_id": "humaneval_like_0",
        "start": 42861
      },
      {
        "end": 85852,
        "family": "humaneval_like",
        "losses": {
          "baseline_pvr_seed42": 13.306273460388184,
          "dense_300m": 19.473281860351562,
          "ean_seed42": 16.904939651489258,
          "repaired_delta_replay": 13.202263832092285
        },
        "path": "data/eval/coding/humaneval_base.jsonl",
        "raw_decoded_text": "a > 3.7:\\n            letter_grade.append(\\\"A\\\")\\n        elif gpa > 3.3:\\n            letter_grade.append(\\\"A-\\\")\\n        elif",
        "repair_minus_baseline": -0.10400962829589844,
        "repair_minus_dense": -6.271018028259277,
        "repair_minus_ean": -3.7026758193969727,
        "span_id": "humaneval_like_1",
        "start": 85723
      },
      {
        "end": 128714,
        "family": "humaneval_like",
        "losses": {
          "baseline_pvr_seed42": 11.39330768585205,
          "dense_300m": 16.30516815185547,
          "ean_seed42": 13.718600273132324,
          "repaired_delta_replay": 11.03752613067627
        },
        "path": "data/eval/coding/humaneval_base.jsonl",
        "raw_decoded_text": " elements of lst1 to be even, return \\\"YES\\\".\\n    Otherwise, return \\\"NO\\\".\\n    For example:\\n    exchange([1, 2, 3, 4], [1, 2",
        "repair_minus_baseline": -0.35578155517578125,
        "repair_minus_dense": -5.267642021179199,
        "repair_minus_ean": -2.6810741424560547,
        "span_id": "humaneval_like_2",
        "start": 128585
      },
      {
        "end": 171576,
        "family": "humaneval_like",
        "losses": {
          "baseline_pvr_seed42": 7.083217144012451,
          "dense_300m": 9.624191284179688,
          "ean_seed42": 7.81622838973999,
          "repaired_delta_replay": 6.23173189163208
        },
        "path": "data/eval/coding/humaneval_base.jsonl",
        "raw_decoded_text": "ement exists then return -1. The given array will not contain\\n    duplicate values.\\n\\n    Examples:\\n    can_arrange([1,2,4,3,",
        "repair_minus_baseline": -0.8514852523803711,
        "repair_minus_dense": -3.3924593925476074,
        "repair_minus_ean": -1.5844964981079102,
        "span_id": "humaneval_like_3",
        "start": 171447
      },
      {
        "end": 2784,
        "family": "json_schema",
        "losses": {
          "baseline_pvr_seed42": 10.212475776672363,
          "dense_300m": 13.100582122802734,
          "ean_seed42": 12.034255027770996,
          "repaired_delta_replay": 9.029749870300293
        },
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "raw_decoded_text": " is not a number\",\n                \"data\": [],\n                \"valid\": false\n            },\n            {\n                \"desc",
        "repair_minus_baseline": -1.1827259063720703,
        "repair_minus_dense": -4.070832252502441,
        "repair_minus_ean": -3.004505157470703,
        "span_id": "json_schema_0",
        "start": 2655
      },
      {
        "end": 5440,
        "family": "json_schema",
        "losses": {
          "baseline_pvr_seed42": 10.231292724609375,
          "dense_300m": 13.189247131347656,
          "ean_seed42": 12.170920372009277,
          "repaired_delta_replay": 8.980449676513672
        },
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "raw_decoded_text": "y is not an object\",\n                \"data\": [],\n                \"valid\": false\n            },\n            {\n                \"de",
        "repair_minus_baseline": -1.2508430480957031,
        "repair_minus_dense": -4.208797454833984,
        "repair_minus_ean": -3.1904706954956055,
        "span_id": "json_schema_1",
        "start": 5311
      },
      {
        "end": 8096,
        "family": "json_schema",
        "losses": {
          "baseline_pvr_seed42": 9.930900573730469,
          "dense_300m": 13.64269733428955,
          "ean_seed42": 12.518198013305664,
          "repaired_delta_replay": 9.967832565307617
        },
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "raw_decoded_text": "\n                \"data\": [],\n                \"valid\": false\n            },\n            {\n                \"description\": \"true is",
        "repair_minus_baseline": 0.03693199157714844,
        "repair_minus_dense": -3.6748647689819336,
        "repair_minus_ean": -2.550365447998047,
        "span_id": "json_schema_2",
        "start": 7967
      },
      {
        "end": 10752,
        "family": "json_schema",
        "losses": {
          "baseline_pvr_seed42": 11.232419967651367,
          "dense_300m": 16.16033935546875,
          "ean_seed42": 15.211018562316895,
          "repaired_delta_replay": 12.566546440124512
        },
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "raw_decoded_text": "  },\n            {\n                \"description\": \"an object is invalid\",\n                \"data\": {},\n                \"valid\": f",
        "repair_minus_baseline": 1.3341264724731445,
        "repair_minus_dense": -3.5937929153442383,
        "repair_minus_ean": -2.644472122192383,
        "span_id": "json_schema_3",
        "start": 10623
      }
    ]
  },
  "lrs": {
    "expert_lr": 1e-05,
    "router_lr": 1e-06,
    "trunk_lr": 0.0
  },
  "parameter_counts": {
    "expert_delta": 81632064,
    "frozen": 202928848,
    "router": 196608,
    "trunk": 0
  },
  "replay_byte_count_after_exclusion": 243422,
  "row": {
    "checkpoint_exists": true,
    "checkpoint_manifest": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/checkpoint_manifest.json",
    "checkpoint_path": "checkpoints/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/checkpoint.pt",
    "effective_batch_tokens": 256,
    "error": null,
    "eval_curve": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/eval_curve.json",
    "eval_window_count": 4,
    "final_loss": 12.04589557647705,
    "gpu_hours": 0.007064464688301087,
    "hardware_manifest": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/hardware_manifest.json",
    "model_variant": "pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42",
    "optimizer_steps": 100,
    "routing_curve": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/routing_curve.json",
    "routing_window_count": 4,
    "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
    "throughput_log": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/throughput_log.json",
    "tokens_seen": 25600,
    "training_curve": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/training_curve.json",
    "training_tokens_seen": 25600,
    "vram_peak": 1911901184
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
      "checkpoint_path": "checkpoints/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/checkpoint.pt",
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
      "model_variant": "pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42",
      "num_experts_if_applicable": 8,
      "num_heads": 16,
      "num_layers": 24,
      "optimizer": "adamw",
      "output_path": "benchmark/reports/generated/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42",
      "precision": "bf16",
      "public_positioning_only": false,
      "repair": "structured_delta_replay_generalization_audit",
      "scheduler": "cosine_with_warmup",
      "schema_version": "1.0",
      "tokenizer": "tiktoken_compatible_bpe",
      "total_params": 300000000,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens": 60000000000
    },
    "created_at": "2026-06-17T03:35:11.641111+00:00",
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
      "checkpoint": "checkpoints/ean_delta_replay_generalization_audit_seed_42/pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42/checkpoint.pt",
      "code_eval_token_count": 12800,
      "code_token_loss": 6.90492072224617,
      "contamination_scan": "CONTAMINATION_STATUS_UNKNOWN",
      "context_length": 4096,
      "copy_span_loss": null,
      "eval_latency_ms_per_token": 0.732542248442769,
      "eval_manifest_hash": "079c69bfbcab72c9499ef60ed6122486803a6970b7b6b69cdbe154463d244c74",
      "eval_token_count": 51200,
      "gpqa": null,
      "gpu_hours": null,
      "hardware": "not_run",
      "heldout_eval_token_count": 12800,
      "ifeval": null,
      "json_schema_eval_token_count": 12800,
      "json_token_loss": 6.90492072224617,
      "lm_loss": 3.0021095263957975,
      "long_context_loss_by_position": "NOT_RUN_NOT_IMPLEMENTED",
      "loss_by_descriptor_family": null,
      "loss_by_operator_family": null,
      "math_eval_token_count": 12800,
      "math_lvl_5": null,
      "math_token_loss": 6.90492072224617,
      "mmlu_pro": null,
      "model": "pvr_ec_o_embeddings_attention_norms_init_v1_delta_replay_generalization_seed_42",
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
      "perplexity": 20.12795261628348,
      "prompt_sensitivity": null,
      "rare_token_loss": "NOT_RUN_NOT_IMPLEMENTED",
      "throughput": 1365.1089778450184,
      "tokenizer": "tiktoken_compatible_bpe",
      "tokens_evaluated": 51200,
      "total_params": 300000000,
      "training_data_manifest_hash": "4f82d92e02004043cedcdc63e1a63a644a6d6f05bea9484c2a50a598c058ee6d",
      "training_tokens": 60000000000,
      "truthfulqa": null,
      "vram_peak": 2849164288,
      "wall_clock": null
    },
    "scorecard_type": "nlp",
    "status": "GENUINE_REDUCED_EVAL"
  },
  "scorecard_slice_comparison": {
    "code_heavy_scorecard_loss": {
      "baseline_pvr": 9.669155575037003,
      "dense": 9.610573108196258,
      "ean": 8.438839778900146,
      "repair_minus_baseline": -2.7642348527908327,
      "repair_minus_dense": -2.7056523859500876,
      "repair_minus_ean": -1.5339190566539758,
      "repaired": 6.90492072224617
    },
    "gutenberg_prose_lm_loss": {
      "baseline_pvr": 3.422222343683243,
      "dense": 3.305846790075302,
      "ean": 3.010810148715973,
      "repair_minus_baseline": -0.4201128172874453,
      "repair_minus_dense": -0.3037372636795044,
      "repair_minus_ean": -0.008700622320175544,
      "repaired": 3.0021095263957975
    },
    "schema_heavy_scorecard_loss": {
      "baseline_pvr": 9.669155575037003,
      "dense": 9.610573108196258,
      "ean": 8.438839778900146,
      "repair_minus_baseline": -2.7642348527908327,
      "repair_minus_dense": -2.7056523859500876,
      "repair_minus_ean": -1.5339190566539758,
      "repaired": 6.90492072224617
    }
  },
  "seed": 42,
  "status": "PVR_EAN_DELTA_REPLAY_GENERALIZATION_AUDIT_SUPPORTED",
  "supported_conditions": {
    "broad_lm_scorecard_beats_dense": true,
    "broad_lm_scorecard_matches_or_beats_ean": true,
    "heldout_structured_improves_over_ean": true,
    "top1_invariants_clean": true
  }
}
```
