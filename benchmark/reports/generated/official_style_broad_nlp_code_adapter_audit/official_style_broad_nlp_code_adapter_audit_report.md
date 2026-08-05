# Official-Style Broad NLP Code Adapter Audit

Status: `PVR_OFFICIAL_STYLE_BROAD_NLP_CODE_ADAPTER_AUDIT_NOT_RUN_NOT_IMPLEMENTED`

| metric | status | observed values |
|---|---|---|
| mmlu_pro | NOT_RUN_NOT_IMPLEMENTED | [] |
| gpqa | NOT_RUN_NOT_IMPLEMENTED | [] |
| bbh | NOT_RUN_NOT_IMPLEMENTED | [] |
| musr | NOT_RUN_NOT_IMPLEMENTED | [] |
| math_lvl_5 | NOT_RUN_NOT_IMPLEMENTED | [] |
| ifeval | NOT_RUN_NOT_IMPLEMENTED | [] |
| arc_challenge | NOT_RUN_NOT_IMPLEMENTED | [] |
| hellaswag | NOT_RUN_NOT_IMPLEMENTED | [] |
| truthfulqa | NOT_RUN_NOT_IMPLEMENTED | [] |
| winogrande | NOT_RUN_NOT_IMPLEMENTED | [] |
| boolq | NOT_RUN_NOT_IMPLEMENTED | [] |
| gsm8k | NOT_RUN_NOT_IMPLEMENTED | [] |
| humaneval_plus_pass_at_1 | NOT_RUN_NOT_IMPLEMENTED | [] |
| mbpp_plus_pass_at_1 | NOT_RUN_NOT_IMPLEMENTED | [] |
| bigcodebench_complete | NOT_RUN_NOT_IMPLEMENTED | [] |
| bigcodebench_instruct | NOT_RUN_NOT_IMPLEMENTED | [] |
| livecodebench_pass_at_1 | NOT_RUN_NOT_IMPLEMENTED | [] |
| repobench_r_recall_at_k | NOT_RUN_NOT_IMPLEMENTED | [] |

```json
{
  "benchmark_evidence": false,
  "benchmark_evidence_scorecard_count": 0,
  "blocked_claims": [
    "PVR_OFFICIAL_BROAD_NLP_SUPPORTED",
    "PVR_OFFICIAL_CODE_BENCH_SUPPORTED"
  ],
  "created_at": "2026-06-18T17:42:31.704989+00:00",
  "decision_rule": "Support requires implemented official-style broad NLP and code metrics with real benchmark evidence. Declared eval-suite names alone do not count as implemented adapters.",
  "declared_config_suite_coverage": [
    {
      "config_path": "benchmark/configs/generated/dense_transformer_700m.yaml",
      "declared_official_code": [
        "bigcodebench_complete",
        "bigcodebench_instruct",
        "humaneval_plus",
        "livecodebench",
        "mbpp_plus",
        "repobench"
      ],
      "declared_official_nlp": [
        "arc_challenge",
        "bbh",
        "boolq",
        "gpqa",
        "gsm8k",
        "hellaswag",
        "ifeval",
        "math_lvl_5",
        "mmlu_pro",
        "musr",
        "truthfulqa",
        "winogrande"
      ],
      "model_variant": "dense_transformer_700m"
    },
    {
      "config_path": "benchmark/configs/generated/vanilla_switch_top1_reference_700m.yaml",
      "declared_official_code": [
        "bigcodebench_complete",
        "bigcodebench_instruct",
        "humaneval_plus",
        "livecodebench",
        "mbpp_plus",
        "repobench"
      ],
      "declared_official_nlp": [
        "arc_challenge",
        "bbh",
        "boolq",
        "gpqa",
        "gsm8k",
        "hellaswag",
        "ifeval",
        "math_lvl_5",
        "mmlu_pro",
        "musr",
        "truthfulqa",
        "winogrande"
      ],
      "model_variant": "vanilla_switch_top1_reference_700m"
    },
    {
      "config_path": "benchmark/configs/generated/generic_top2_moe_reference_700m.yaml",
      "declared_official_code": [
        "bigcodebench_complete",
        "bigcodebench_instruct",
        "humaneval_plus",
        "livecodebench",
        "mbpp_plus",
        "repobench"
      ],
      "declared_official_nlp": [
        "arc_challenge",
        "bbh",
        "boolq",
        "gpqa",
        "gsm8k",
        "hellaswag",
        "ifeval",
        "math_lvl_5",
        "mmlu_pro",
        "musr",
        "truthfulqa",
        "winogrande"
      ],
      "model_variant": "generic_top2_moe_reference_700m"
    },
    {
      "config_path": "benchmark/configs/generated/pvr_ec_o_full_700m.yaml",
      "declared_official_code": [
        "bigcodebench_complete",
        "bigcodebench_instruct",
        "humaneval_plus",
        "livecodebench",
        "mbpp_plus",
        "repobench"
      ],
      "declared_official_nlp": [
        "arc_challenge",
        "bbh",
        "boolq",
        "gpqa",
        "gsm8k",
        "hellaswag",
        "ifeval",
        "math_lvl_5",
        "mmlu_pro",
        "musr",
        "truthfulqa",
        "winogrande"
      ],
      "model_variant": "pvr_ec_o_full_700m"
    }
  ],
  "experiment": "PVR_OFFICIAL_STYLE_BROAD_NLP_CODE_ADAPTER_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "implemented_metric_count": 0,
  "metric_rows": [
    {
      "implemented": false,
      "metric": "mmlu_pro",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "gpqa",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "bbh",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "musr",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "math_lvl_5",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "ifeval",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "arc_challenge",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "hellaswag",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "truthfulqa",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "winogrande",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "boolq",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "gsm8k",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "humaneval_plus_pass_at_1",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "mbpp_plus_pass_at_1",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "bigcodebench_complete",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "bigcodebench_instruct",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "livecodebench_pass_at_1",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    },
    {
      "implemented": false,
      "metric": "repobench_r_recall_at_k",
      "observed_values": [],
      "status": "NOT_RUN_NOT_IMPLEMENTED"
    }
  ],
  "required_metric_count": 18,
  "schema_version": "1.0",
  "scorecard_count": 24,
  "scorecard_roots": [
    "benchmark/reports/generated/benchmark_700m_run_docker/scorecards",
    "benchmark/reports/generated/training_300m_real_4k"
  ],
  "status": "PVR_OFFICIAL_STYLE_BROAD_NLP_CODE_ADAPTER_AUDIT_NOT_RUN_NOT_IMPLEMENTED"
}
```
