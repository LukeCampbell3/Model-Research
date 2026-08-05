# EAN Retention-Gated Delta Replay Repeat

Status: `PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_SUPPORTED`
Candidate: `pvr_ec_o_ean_retention_gated_delta_replay_v1`

| seed | status | broad delta | code delta | json delta | unseen structured delta | Top1 clean |
|---:|---|---:|---:|---:|---:|---|
| 42 | PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED | -0.023355387151241302 | -1.3145437240600586 | -2.163301706314087 | -1.7389227151870728 | True |
| 123 | PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED | -0.047335829585790634 | -1.7631248235702515 | -2.1051650047302246 | -1.934144914150238 | True |

```json
{
  "all_top1_invariants_clean": true,
  "benchmark_evidence_caveat": "Reduced repeat/promotion audit evidence only. Do not label as official broad benchmark promotion until full adapters run.",
  "candidate": "pvr_ec_o_ean_retention_gated_delta_replay_v1",
  "created_at": "2026-06-17T04:11:59.172472+00:00",
  "decision_rule": "Repeat support requires at least two distinct seeds, each with retention-gated support status and clean Top1 invariants.",
  "do_not_promote": [
    "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_OFFICIAL_PROMOTION_SUPPORTED",
    "PVR_EAN_FULL_BENCHMARK_PROMOTION_SUPPORTED",
    "PVR_FROM_SCRATCH_DENSE_GAP_CLOSED",
    "PVR_TEACHER_INDEPENDENCE_SUPPORTED"
  ],
  "experiment": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "reports": [
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/structured_delta_replay_retention_gated_report.json",
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/structured_delta_replay_retention_gated_report.json"
  ],
  "schema_version": "1.0",
  "seed_count": 2,
  "seed_summaries": [
    {
      "best_step": 100,
      "broad_delta_vs_ean": -0.023355387151241302,
      "broad_lm": 2.571919046342373,
      "code_delta_vs_ean": -1.3145437240600586,
      "code_heavy": 11.644206404685974,
      "json_delta_vs_ean": -2.163301706314087,
      "json_schema": 10.820296287536621,
      "seed": 42,
      "seeded_replay_sampling": {
        "enabled": true,
        "offset_formula": "step_idx + seed * 1009 + stream * 1000003",
        "retention_stream": 1,
        "seed": 42,
        "structured_stream": 0
      },
      "status": "PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED",
      "supported_conditions": {
        "broad_lm_beats_dense": true,
        "broad_lm_beats_pvr_baseline": true,
        "broad_lm_beats_switch_top1": true,
        "broad_lm_within_tolerance_vs_ean": true,
        "code_heavy_improves_vs_ean": true,
        "gutenberg_prose_within_tolerance_vs_ean": true,
        "json_schema_improves_vs_ean": true,
        "replay_examples_excluded_from_final_structured_eval": true,
        "top1_invariants_clean": true,
        "unseen_structured_spans_improve_vs_ean": true
      },
      "top1_invariants_clean": true,
      "unseen_structured": 11.232251346111298,
      "unseen_structured_delta_vs_ean": -1.7389227151870728
    },
    {
      "best_step": 100,
      "broad_delta_vs_ean": -0.047335829585790634,
      "broad_lm": 2.5479386039078236,
      "code_delta_vs_ean": -1.7631248235702515,
      "code_heavy": 11.195625305175781,
      "json_delta_vs_ean": -2.1051650047302246,
      "json_schema": 10.878432989120483,
      "seed": 123,
      "seeded_replay_sampling": {
        "enabled": true,
        "offset_formula": "step_idx + seed * 1009 + stream * 1000003",
        "retention_stream": 1,
        "seed": 123,
        "structured_stream": 0
      },
      "status": "PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED",
      "supported_conditions": {
        "broad_lm_beats_dense": true,
        "broad_lm_beats_pvr_baseline": true,
        "broad_lm_beats_switch_top1": true,
        "broad_lm_within_tolerance_vs_ean": true,
        "code_heavy_improves_vs_ean": true,
        "gutenberg_prose_within_tolerance_vs_ean": true,
        "json_schema_improves_vs_ean": true,
        "replay_examples_excluded_from_final_structured_eval": true,
        "top1_invariants_clean": true,
        "unseen_structured_spans_improve_vs_ean": true
      },
      "top1_invariants_clean": true,
      "unseen_structured": 11.037029147148132,
      "unseen_structured_delta_vs_ean": -1.934144914150238
    }
  ],
  "status": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_PROMOTION_REPEAT_SUPPORTED",
  "supported_seed_count": 2
}
```
