# EAN Structured Delta Adaptation Sweep

Status: `PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SHORT_REPLAY_SUPPORTED`
Secondary: `PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_LONGER_REPLAY_OVERFITS`

| steps | status | LM loss | vs EAN | vs dense | structured improved |
|---:|---|---:|---:|---:|---|
| 100 | PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SUPPORTED | 3.0021095263957975 | -0.008700622320175544 | -0.3037372636795044 | True |
| 250 | PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED | 3.182013305425644 | 0.1712031567096708 | -0.12383348464965804 | True |
| 1000 | PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED | 3.217206156253815 | 0.2063960075378417 | -0.08864063382148712 | True |

```json
{
  "best_supported": {
    "lm_loss": 3.0021095263957975,
    "optimizer_steps": 100,
    "repaired_minus_baseline_lm_loss": -0.4201128172874453,
    "repaired_minus_baseline_mean_eval_loss": 2.4508179187774655,
    "repaired_minus_dense_lm_loss": -0.3037372636795044,
    "repaired_minus_ean_lm_loss": -0.008700622320175544,
    "scorecard_preserved_within_0_01": true,
    "source_report": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps100/structured_span_delta_adaptation_report.json",
    "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SUPPORTED",
    "structured_outliers_improved": true,
    "structured_window_deltas": {
      "3600": {
        "ean_delta_vs_baseline": 2.7385520935058594,
        "repair_minus_ean_delta": -1.8721771240234375,
        "repaired_delta_vs_baseline": 0.8663749694824219
      },
      "4000": {
        "ean_delta_vs_baseline": 3.838240623474121,
        "repair_minus_ean_delta": -3.216623306274414,
        "repaired_delta_vs_baseline": 0.621617317199707
      }
    },
    "top1_invariants_clean": true,
    "training_tokens_seen": 25600
  },
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1_structured_delta_adaptation",
  "created_at": "2026-06-17T03:27:38.979581+00:00",
  "decision": {
    "architecture_change_recommended": false,
    "longer_replay_overfits_broad_scorecard": true,
    "owner_preservation_still_not_supported": true,
    "recommended_recipe": "EAN init + short structured expert-delta replay; stop early before scorecard drift",
    "short_replay_supported": true
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "interpretation": "Short structured expert-delta replay recovers the bad code/JSON spans while preserving or slightly improving the EAN scorecard. Longer replay continues improving structured windows but overfits the replay distribution and regresses broad LM scorecard.",
  "rows": [
    {
      "lm_loss": 3.0021095263957975,
      "optimizer_steps": 100,
      "repaired_minus_baseline_lm_loss": -0.4201128172874453,
      "repaired_minus_baseline_mean_eval_loss": 2.4508179187774655,
      "repaired_minus_dense_lm_loss": -0.3037372636795044,
      "repaired_minus_ean_lm_loss": -0.008700622320175544,
      "scorecard_preserved_within_0_01": true,
      "source_report": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps100/structured_span_delta_adaptation_report.json",
      "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SUPPORTED",
      "structured_outliers_improved": true,
      "structured_window_deltas": {
        "3600": {
          "ean_delta_vs_baseline": 2.7385520935058594,
          "repair_minus_ean_delta": -1.8721771240234375,
          "repaired_delta_vs_baseline": 0.8663749694824219
        },
        "4000": {
          "ean_delta_vs_baseline": 3.838240623474121,
          "repair_minus_ean_delta": -3.216623306274414,
          "repaired_delta_vs_baseline": 0.621617317199707
        }
      },
      "top1_invariants_clean": true,
      "training_tokens_seen": 25600
    },
    {
      "lm_loss": 3.182013305425644,
      "optimizer_steps": 250,
      "repaired_minus_baseline_lm_loss": -0.24020903825759898,
      "repaired_minus_baseline_mean_eval_loss": -0.535938715934754,
      "repaired_minus_dense_lm_loss": -0.12383348464965804,
      "repaired_minus_ean_lm_loss": 0.1712031567096708,
      "scorecard_preserved_within_0_01": false,
      "source_report": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42_steps250/structured_span_delta_adaptation_report.json",
      "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED",
      "structured_outliers_improved": true,
      "structured_window_deltas": {
        "3600": {
          "ean_delta_vs_baseline": 2.7385520935058594,
          "repair_minus_ean_delta": -4.310294151306152,
          "repaired_delta_vs_baseline": -1.571742057800293
        },
        "4000": {
          "ean_delta_vs_baseline": 3.838240623474121,
          "repair_minus_ean_delta": -7.904540061950684,
          "repaired_delta_vs_baseline": -4.0662994384765625
        }
      },
      "top1_invariants_clean": true,
      "training_tokens_seen": 64000
    },
    {
      "lm_loss": 3.217206156253815,
      "optimizer_steps": 1000,
      "repaired_minus_baseline_lm_loss": -0.20501618742942807,
      "repaired_minus_baseline_mean_eval_loss": -1.313542437553406,
      "repaired_minus_dense_lm_loss": -0.08864063382148712,
      "repaired_minus_ean_lm_loss": 0.2063960075378417,
      "scorecard_preserved_within_0_01": false,
      "source_report": "benchmark/reports/generated/ean_structured_span_delta_adaptation_seed_42/structured_span_delta_adaptation_report.json",
      "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_NOT_SUPPORTED",
      "structured_outliers_improved": true,
      "structured_window_deltas": {
        "3600": {
          "ean_delta_vs_baseline": 2.7385520935058594,
          "repair_minus_ean_delta": -7.982359886169434,
          "repaired_delta_vs_baseline": -5.243807792663574
        },
        "4000": {
          "ean_delta_vs_baseline": 3.838240623474121,
          "repair_minus_ean_delta": -11.937903881072998,
          "repaired_delta_vs_baseline": -8.099663257598877
        }
      },
      "top1_invariants_clean": true,
      "training_tokens_seen": 256000
    }
  ],
  "schema_version": "1.0",
  "secondary_status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_LONGER_REPLAY_OVERFITS",
  "status": "PVR_EAN_STRUCTURED_SPAN_DELTA_ADAPTATION_SHORT_REPLAY_SUPPORTED"
}
```
