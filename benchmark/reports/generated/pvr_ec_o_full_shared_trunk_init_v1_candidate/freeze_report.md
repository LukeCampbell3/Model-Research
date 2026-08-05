# PVR-EC-O Shared Trunk Init v1 Freeze

Status: `PVR_SHARED_TRUNK_INIT_REPAIR_CANDIDATE`

```json
{
  "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
  "candidate_config": "benchmark/configs/generated/pvr_ec_o_full_shared_trunk_init_v1_300m.yaml",
  "copy_scope": {
    "copied_compatible_weight_count": 244,
    "copied_sample": [
      "token_emb.weight",
      "pos_emb.weight",
      "ln_f.weight",
      "ln_f.bias",
      "attn.0.self_attn.in_proj_weight",
      "attn.0.self_attn.in_proj_bias",
      "attn.0.self_attn.out_proj.weight",
      "attn.0.self_attn.out_proj.bias",
      "attn.0.linear2.bias",
      "attn.0.norm1.weight",
      "attn.0.norm1.bias",
      "attn.0.norm2.weight",
      "attn.0.norm2.bias",
      "blocks.0.shared.w2.bias",
      "attn.1.self_attn.in_proj_weight",
      "attn.1.self_attn.in_proj_bias",
      "attn.1.self_attn.out_proj.weight",
      "attn.1.self_attn.out_proj.bias",
      "attn.1.linear2.bias",
      "attn.1.norm1.weight"
    ],
    "name": "full_compatible_shared_copy",
    "skipped_incompatible_weight_count": 145,
    "skipped_sample": [
      "head.weight",
      "attn.0.linear1.weight",
      "attn.0.linear1.bias",
      "attn.0.linear2.weight",
      "blocks.0.shared.w1.weight",
      "blocks.0.shared.w1.bias",
      "blocks.0.shared.w2.weight",
      "attn.1.linear1.weight",
      "attn.1.linear1.bias",
      "attn.1.linear2.weight",
      "blocks.1.shared.w1.weight",
      "blocks.1.shared.w1.bias",
      "blocks.1.shared.w2.weight",
      "attn.2.linear1.weight",
      "attn.2.linear1.bias",
      "attn.2.linear2.weight",
      "blocks.2.shared.w1.weight",
      "blocks.2.shared.w1.bias",
      "blocks.2.shared.w2.weight",
      "attn.3.linear1.weight"
    ]
  },
  "created_at": "2026-06-14T17:56:45.478214+00:00",
  "decision_report": {
    "created_at": "2026-06-14T14:35:35.561183+00:00",
    "git_commit": "5c61a4cb1d93ca182847b75483687d1c344bc328",
    "init_scope": {
      "copied_compatible_weight_count": 244,
      "from_scratch_dense_dominance_proven": false,
      "skipped_incompatible_weight_count": 145,
      "teacher_initialized_sparse_transfer": true
    },
    "reduced_lm_scorecard_decision": {
      "baseline_pvr_lm_loss": 3.5067039370536803,
      "dense_reference_lm_loss": 3.305846790075302,
      "eval_token_count": 51200,
      "heldout_eval_token_count": 12800,
      "init_minus_baseline_lm_loss": -0.4752389967441557,
      "init_minus_dense_lm_loss": -0.2743818497657773,
      "paths": {
        "baseline": "benchmark\\reports\\generated\\shared_trunk_init_300m_confirmation\\lm_eval\\pvr_ec_o_full_300m_baseline_seed_20260614_nlp_scorecard.json",
        "shared_trunk_init": "benchmark\\reports\\generated\\shared_trunk_init_300m_confirmation\\lm_eval\\pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_20260614_nlp_scorecard.json"
      },
      "scorecard_dense_gap_closed": true,
      "shared_trunk_init_pvr_lm_loss": 3.0314649403095246,
      "status": "COMPLETED"
    },
    "route_stability": {
      "mean_owner_entropy_delta_vs_baseline": 0.02867260400388827,
      "mean_prototype_monopoly_rate_delta_vs_baseline": -0.03831380208333335,
      "mean_route_margin_delta_vs_baseline": 0.010296393473314902,
      "route_stable": true,
      "top1_invariants_clean": true
    },
    "schema_version": "1.0",
    "seed_report": "benchmark\\reports\\generated\\shared_trunk_init_300m_confirmation\\shared_trunk_init_seed_report.json",
    "status": "PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED",
    "training_eval_curve_decision": {
      "baseline_pvr_mean_eval_loss": 5.518721175193787,
      "dense_reference_mean_eval_loss": 5.800183653831482,
      "init_minus_baseline_mean_eval_loss": -0.5217703104019167,
      "init_minus_dense_mean_eval_loss": -0.8032327890396118,
      "shared_trunk_init_mean_eval_loss": 4.99695086479187,
      "status": "PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED"
    }
  },
  "deprecated_paths_not_used": [
    "in_bounds_probability_head_as_previously_implemented",
    "route_confidence_regularization_0_01",
    "persistent_global_dense_kl"
  ],
  "evidence_statuses": [
    "PVR_SHARED_TRUNK_INIT_CONFIRMED",
    "PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED",
    "PVR_ROUTING_NOT_MAIN_BOTTLENECK"
  ],
  "git_commit": "5c61a4cb1d93ca182847b75483687d1c344bc328",
  "not_proven_claim": "PVR-EC-O from scratch beats dense under equal total training conditions.",
  "schema_version": "1.0",
  "status": "PVR_SHARED_TRUNK_INIT_REPAIR_CANDIDATE",
  "supported_claim": "Dense-compatible shared-trunk initialization materially improves 300M PVR-EC-O while preserving strict Top1 routing."
}
```
