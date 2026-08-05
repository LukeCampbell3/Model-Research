# EAN Structured Span Route Decision

Status: `PVR_EAN_STRUCTURED_SPAN_ROUTE_SHIFT_DELTA_HELP_LOSS_CONFIRMED`

| window | owner disagreement | EAN expert help | baseline expert help | route-shift high-loss tokens |
|---|---:|---:|---:|---:|
| step_4000 | 0.8984375000000002 | 0.05393740313593298 | -1.81053360257647 | 21 |
| step_3600 | 0.9205729166666669 | 0.028751575970090926 | -2.5194241813442204 | 13 |

```json
{
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
  "created_at": "2026-06-17T02:35:27.347110+00:00",
  "decision": {
    "baseline_expert_deltas_help_more_than_ean": true,
    "broad_architecture_change_recommended": false,
    "preferred_next_repair_if_any": "structured_span_route_stability_or_delta_warmup_only",
    "quote_and_opening_structure_tokens_dominate_bad_loss": true,
    "structured_span_route_shift_confirmed": true
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "interpretation": "EAN's bad structured windows are explained by large owner-boundary shifts plus loss of scratch-PVR expert delta help on quote/opening-structure tokens. This supports a narrow structured-span stabilization path, not a broad routing redesign or rejection of EAN.",
  "schema_version": "1.0",
  "source_report": "benchmark/reports/generated/ean_structured_span_route_audit/structured_span_route_audit_report.json",
  "status": "PVR_EAN_STRUCTURED_SPAN_ROUTE_SHIFT_DELTA_HELP_LOSS_CONFIRMED",
  "windows": [
    {
      "baseline_expert_help_delta": -1.81053360257647,
      "delta": 3.838240623474121,
      "ean_expert_help_delta": 0.05393740313593298,
      "expert_harm_token_count": 48,
      "owner_disagreement_rate": 0.8984375000000002,
      "route_shift_high_loss_token_count": 21,
      "source": {
        "offset_in_source": 36970,
        "path": "data/eval/coding/humaneval_base.jsonl"
      },
      "window_id": "step_4000",
      "worst_token_types": [
        {
          "count": 7,
          "mean_ean_minus_baseline_loss": 60.200753348214285,
          "mean_owner_disagreement_rate": 0.9166666666666667,
          "token_type": "quote"
        },
        {
          "count": 5,
          "mean_ean_minus_baseline_loss": 35.588531494140625,
          "mean_owner_disagreement_rate": 0.9083333333333334,
          "token_type": "other"
        },
        {
          "count": 37,
          "mean_ean_minus_baseline_loss": -0.1278847645263414,
          "mean_owner_disagreement_rate": 0.8997747747747747,
          "token_type": "indent_or_space"
        },
        {
          "count": 47,
          "mean_ean_minus_baseline_loss": -0.2572501758311657,
          "mean_owner_disagreement_rate": 0.8945035460992906,
          "token_type": "schema_key_or_value"
        }
      ]
    },
    {
      "baseline_expert_help_delta": -2.5194241813442204,
      "delta": 2.7385520935058594,
      "ean_expert_help_delta": 0.028751575970090926,
      "expert_harm_token_count": 57,
      "owner_disagreement_rate": 0.9205729166666669,
      "route_shift_high_loss_token_count": 13,
      "source": {
        "offset_in_source": 1804,
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt"
      },
      "window_id": "step_3600",
      "worst_token_types": [
        {
          "count": 6,
          "mean_ean_minus_baseline_loss": 61.93519846598307,
          "mean_owner_disagreement_rate": 0.9097222222222222,
          "token_type": "quote"
        },
        {
          "count": 3,
          "mean_ean_minus_baseline_loss": 19.764291445414226,
          "mean_owner_disagreement_rate": 0.9027777777777778,
          "token_type": "brace_bracket_paren"
        },
        {
          "count": 1,
          "mean_ean_minus_baseline_loss": 3.4853920936584473,
          "mean_owner_disagreement_rate": 0.9583333333333334,
          "token_type": "other"
        },
        {
          "count": 47,
          "mean_ean_minus_baseline_loss": -0.1929099439306462,
          "mean_owner_disagreement_rate": 0.9343971631205675,
          "token_type": "indent_or_space"
        }
      ]
    }
  ]
}
```
