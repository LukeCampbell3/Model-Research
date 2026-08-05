# EAN Alignment Decision

Status: `PVR_EAN_EVAL_ALIGNMENT_MISMATCH_CONFIRMED`
Detail: `SCORECARD_WINS_WITH_TRAINING_WINDOW_OUTLIER_REGRESSION`

| model | scorecard wins | scorecard mean delta | final-window wins | final-window mean delta | recorded wins | recorded mean delta |
|---|---:|---:|---:|---:|---:|---:|
| ean_seed42 | 199/200 | -0.4114121949672699 | 8/10 | 0.5333416700363159 | 7/10 | 0.12875699996948242 |
| full_copy_seed42 | 199/200 | -0.40945056557655335 | 8/10 | 0.5423141241073608 | 7/10 | 0.1312023162841797 |
| dense_300m | 170/200 | -0.11637555360794068 | 6/10 | 0.8468944311141968 | 2/10 | 0.9435068130493164 |

```json
{
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
  "correlations": {
    "scorecard_delta_vs_final_training_window_delta_vs_baseline": 0.9998126206249922,
    "scorecard_delta_vs_recorded_training_curve_delta_vs_baseline": 0.9999949627700085,
    "scorecard_style_vs_final_training_window_mean_across_models": -0.4060783987708795,
    "scorecard_style_vs_recorded_training_curve_mean_across_models": 0.24151866899016702
  },
  "created_at": "2026-06-17T02:11:52.765656+00:00",
  "decision": {
    "ean_scorecard_window_support_is_strong": true,
    "ean_training_window_mean_regresses": true,
    "ean_training_window_regression_is_outlier_sensitive": true,
    "scorecard_eval_and_training_eval_are_not_aligned": true
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "interpretation": "The mixed eval-curve result is not a broad EAN failure. EAN beats the matched PVR baseline on nearly all scorecard-style heldout windows and most training-style final-checkpoint windows, but a small number of high-loss training windows flips the training-window mean positive. The next diagnostic should inspect the bad training-window token spans before changing architecture.",
  "model_summaries": {
    "dense_300m": {
      "mean_deltas": {
        "recorded_during_training_eval_curve_mean": 0.943506813049316,
        "scorecard_style_final_checkpoint_mean": -0.11637555360794094,
        "training_window_style_final_checkpoint_mean": 0.8468944311141966
      },
      "recorded_during_training_eval_curve": {
        "loss_count": 8,
        "max_delta": 5.258472442626953,
        "mean_delta": 0.9435068130493164,
        "min_delta": -0.7909774780273438,
        "win_count": 2,
        "window_count": 10
      },
      "scorecard_style_general": {
        "loss_count": 30,
        "max_delta": 2.314793586730957,
        "mean_delta": -0.11637555360794068,
        "min_delta": -3.837541103363037,
        "win_count": 170,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_count": 4,
        "max_delta": 5.258472442626953,
        "mean_delta": 0.8468944311141968,
        "min_delta": -0.1245737075805664,
        "win_count": 6,
        "window_count": 10
      }
    },
    "ean_seed42": {
      "mean_deltas": {
        "recorded_during_training_eval_curve_mean": 0.12875699996948242,
        "scorecard_style_final_checkpoint_mean": -0.4114121949672698,
        "training_window_style_final_checkpoint_mean": 0.5333416700363163
      },
      "recorded_during_training_eval_curve": {
        "loss_count": 3,
        "max_delta": 3.838240623474121,
        "mean_delta": 0.12875699996948242,
        "min_delta": -2.4512956142425537,
        "win_count": 7,
        "window_count": 10
      },
      "scorecard_style_general": {
        "loss_count": 1,
        "max_delta": 0.3143186569213867,
        "mean_delta": -0.4114121949672699,
        "min_delta": -7.054422378540039,
        "win_count": 199,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_count": 2,
        "max_delta": 3.838240623474121,
        "mean_delta": 0.5333416700363159,
        "min_delta": -0.23374342918395996,
        "win_count": 8,
        "window_count": 10
      }
    },
    "full_copy_seed42": {
      "mean_deltas": {
        "recorded_during_training_eval_curve_mean": 0.13120231628417933,
        "scorecard_style_final_checkpoint_mean": -0.40945056557655324,
        "training_window_style_final_checkpoint_mean": 0.542314124107361
      },
      "recorded_during_training_eval_curve": {
        "loss_count": 3,
        "max_delta": 3.873575210571289,
        "mean_delta": 0.1312023162841797,
        "min_delta": -2.473436117172241,
        "win_count": 7,
        "window_count": 10
      },
      "scorecard_style_general": {
        "loss_count": 1,
        "max_delta": 0.3156709671020508,
        "mean_delta": -0.40945056557655335,
        "min_delta": -7.016213417053223,
        "win_count": 199,
        "window_count": 200
      },
      "training_window_style_final_checkpoint": {
        "loss_count": 2,
        "max_delta": 3.873575210571289,
        "mean_delta": 0.5423141241073608,
        "min_delta": -0.241074800491333,
        "win_count": 8,
        "window_count": 10
      }
    }
  },
  "schema_version": "1.0",
  "source_report": "benchmark/reports/generated/ean_scorecard_eval_curve_alignment_audit/alignment_audit_report.json",
  "status": "PVR_EAN_EVAL_ALIGNMENT_MISMATCH_CONFIRMED",
  "status_detail": "SCORECARD_WINS_WITH_TRAINING_WINDOW_OUTLIER_REGRESSION"
}
```
