# Self-Instilled EAN Geometry Head 300M Matched-Volume Screen

Screen: `PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE`
Decision: `PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED`

| model | tokens | steps | eval windows | LM loss | Top1 clean |
|---|---:|---:|---:|---:|---|
| pvr_full_scratch_300m_matched | 1126400 | 1100 | 11 | 4.152685380711848 | True |
| pvr_shared_warmup_no_geometry_head_300m_matched | 1126400 | 1100 | 11 | 4.145141032277321 | True |
| pvr_self_instilled_uniformity_geometry_head_v1_300m_matched | 1126400 | 1100 | 11 | 4.146520776408059 | True |
| pvr_teacher_ean_300m_matched | 1126400 | 1100 | 11 | 3.110029940702477 | True |

```json
{
  "budget": {
    "effective_batch_tokens": 1024,
    "eval_tokens_per_window": 1024,
    "eval_windows_per_model": 11,
    "heldout_score_limit": 196,
    "optimizer_steps": 1100,
    "training_tokens_per_model": 1126400
  },
  "candidate": "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
  "claim_scope": "300M local matched-volume screen; teacher-EAN is a transfer reference, not a teacher-independent candidate.",
  "created_at": "2026-06-19T20:17:45.560356+00:00",
  "decision_rule": "Support requires exact matched volume, clean strict Top1, geometry health, and the geometry variant to beat both plain scratch PVR and the identical no-head warmup schedule. Narrowing requires closing at least 50% of the scratch-to-teacher-EAN loss gap. Closing requires matching EAN without loading a teacher into the candidate and confirmation over at least two seeds.",
  "experiment": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_300M_MATCHED_VOLUME_SCREEN",
  "geometry_health": {
    "active_start": {
      "activation_norm_cv": 0.18962052464485168,
      "activation_norm_mean": 1.8757541179656982,
      "activation_norm_std": 0.35568147897720337,
      "alignment_loss": 3.1967792892828584e-05,
      "covariance_loss": 7.906524115242064e-05,
      "covariance_offdiag_energy": 6.225609467946924e-07,
      "downweighted_sample_fraction": 0.013671875,
      "effective_batch_tokens": 1024,
      "effective_rank": 37.069515228271484,
      "geometry_head_gradient_norm": 0.010392506782437555,
      "geometry_weight_scale": 1.0,
      "head_active": true,
      "isotropy_score": 0.6944379210472107,
      "layerwise_variance_floor": 1.9754647016525269,
      "lm_loss": 416.978515625,
      "loss": 416.9736022949219,
      "norm_scale_loss": 0.036710694432258606,
      "optimizer_step": 1,
      "phase": "geometry_active",
      "sample_count": 1024,
      "shared_only_execution": true,
      "shared_trunk_gradient_norm": 363.09857212302455,
      "step": 1,
      "structured_sample_fraction": 0.146484375,
      "total_geometry_loss": -0.004916853737086058,
      "training_tokens_seen": 1024,
      "uniformity_loss": -2.9285972118377686,
      "variance_loss": 0.9218979477882385
    },
    "all_health_gates_pass": true,
    "conditions": {
      "activation_norm_stable": true,
      "covariance_bounded": true,
      "effective_rank_not_collapsed": true,
      "geometry_head_received_gradients": true,
      "geometry_metrics_finite": true,
      "geometry_metrics_present": true,
      "isotropy_not_collapsed": true,
      "layerwise_variance_positive": true,
      "post_decay_geometry_metrics_present": true,
      "shared_trunk_received_gradients": true
    },
    "post_decay_final": {
      "activation_norm_cv": 0.9490143060684204,
      "activation_norm_mean": 9.34047794342041,
      "activation_norm_std": 8.86424732208252,
      "alignment_loss": 2.935323936981149e-05,
      "covariance_loss": 0.0001988429285120219,
      "covariance_offdiag_energy": 1.5656924006179906e-06,
      "downweighted_sample_fraction": 0.03515625,
      "effective_rank": 38.55106735229492,
      "geometry_head_gradient_norm": 0.0,
      "geometry_weight_scale": 0.0,
      "head_active": false,
      "isotropy_score": 0.5776965022087097,
      "layerwise_variance_floor": 1.9138438701629639,
      "measurement_only": true,
      "norm_scale_loss": 0.9047778248786926,
      "phase": "expert_specialization",
      "sample_count": 1024,
      "shared_trunk_gradient_norm": 0.0,
      "step": "post_decay_final",
      "structured_sample_fraction": 0.255859375,
      "total_geometry_loss": -0.004849943332374096,
      "uniformity_loss": -3.109318494796753,
      "variance_loss": 0.9161361455917358
    },
    "pre_decay_end": {
      "activation_norm_cv": 0.9119976162910461,
      "activation_norm_mean": 9.184435844421387,
      "activation_norm_std": 8.37618350982666,
      "alignment_loss": 3.9657817978877574e-05,
      "covariance_loss": 0.00015000562416389585,
      "covariance_offdiag_energy": 1.1811466720246244e-06,
      "downweighted_sample_fraction": 0.0205078125,
      "effective_batch_tokens": 1024,
      "effective_rank": 50.29499435424805,
      "geometry_head_gradient_norm": 8.72881104585321e-05,
      "geometry_weight_scale": 0.0024999999999999467,
      "head_active": true,
      "isotropy_score": 0.6665239334106445,
      "layerwise_variance_floor": 1.9121991395950317,
      "lm_loss": 3.2967793941497803,
      "loss": 3.2967641353607178,
      "norm_scale_loss": 0.8259499073028564,
      "optimizer_step": 799,
      "phase": "geometry_decay",
      "sample_count": 1024,
      "shared_only_execution": true,
      "shared_trunk_gradient_norm": 21.620282732470816,
      "step": 799,
      "structured_sample_fraction": 0.1005859375,
      "total_geometry_loss": -0.006135782692581415,
      "training_tokens_seen": 818176,
      "uniformity_loss": -3.7301597595214844,
      "variance_loss": 0.911418080329895
    }
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "phase_eval_summary": {
    "pvr_full_scratch_300m_matched": {
      "full_training": {
        "final_eval_loss": 12.821065917611122,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 17.017356032674964,
        "window_count": 11
      }
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": {
      "expert_specialization": {
        "final_eval_loss": 12.381235122680664,
        "head_active": false,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 12.602232828736305,
        "window_count": 3
      },
      "geometry_active": {
        "final_eval_loss": 18.032039165496826,
        "head_active": true,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 27.770137801766396,
        "window_count": 4
      },
      "geometry_decay": {
        "final_eval_loss": 14.933623343706131,
        "head_active": true,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 15.876769110560417,
        "window_count": 4
      }
    },
    "pvr_shared_warmup_no_geometry_head_300m_matched": {
      "expert_specialization": {
        "final_eval_loss": 12.378830254077911,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 12.60284193356832,
        "window_count": 3
      },
      "geometry_active": {
        "final_eval_loss": 18.032000869512558,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 27.77053179591894,
        "window_count": 4
      },
      "geometry_decay": {
        "final_eval_loss": 14.932948172092438,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 15.875797882676125,
        "window_count": 4
      }
    },
    "pvr_teacher_ean_300m_matched": {
      "full_training": {
        "final_eval_loss": 9.185667872428894,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 9.848963131958788,
        "window_count": 11
      }
    }
  },
  "post_decay_geometry_probe": {
    "created_at": "2026-06-19T20:16:37.193100+00:00",
    "head_used_for_inference": false,
    "metrics": {
      "activation_norm_cv": 0.9490143060684204,
      "activation_norm_mean": 9.34047794342041,
      "activation_norm_std": 8.86424732208252,
      "alignment_loss": 2.935323936981149e-05,
      "covariance_loss": 0.0001988429285120219,
      "covariance_offdiag_energy": 1.5656924006179906e-06,
      "downweighted_sample_fraction": 0.03515625,
      "effective_rank": 38.55106735229492,
      "geometry_head_gradient_norm": 0.0,
      "geometry_weight_scale": 0.0,
      "head_active": false,
      "isotropy_score": 0.5776965022087097,
      "layerwise_variance_floor": 1.9138438701629639,
      "measurement_only": true,
      "norm_scale_loss": 0.9047778248786926,
      "phase": "expert_specialization",
      "sample_count": 1024,
      "shared_trunk_gradient_norm": 0.0,
      "step": "post_decay_final",
      "structured_sample_fraction": 0.255859375,
      "total_geometry_loss": -0.004849943332374096,
      "uniformity_loss": -3.109318494796753,
      "variance_loss": 0.9161361455917358
    },
    "schema_version": "1.0",
    "status": "POST_DECAY_GEOMETRY_PROBE_COMPLETE"
  },
  "routing_clean": {
    "pvr_full_scratch_300m_matched": true,
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": true,
    "pvr_shared_warmup_no_geometry_head_300m_matched": true,
    "pvr_teacher_ean_300m_matched": true
  },
  "routing_health": {
    "all_routing_health_gates_pass": true,
    "conditions": {
      "full_vs_shared_benefit_positive": true,
      "owner_churn_measured": true,
      "owner_entropy_positive": true,
      "prototype_monopoly_bounded": true,
      "routing_windows_complete": true,
      "structured_token_benefit_positive": true,
      "wrong_expert_harm_positive": true
    },
    "final": {
      "expert_utilization": [
        137,
        142,
        155,
        140,
        306,
        170,
        286,
        200
      ],
      "full_vs_shared_benefit": 0.9060992002487183,
      "optimizer_step": 1100,
      "owner_churn": 0.022786458333333332,
      "owner_entropy": 2.0289254762039217,
      "owners_per_token": 1.0,
      "phase": "expert_specialization",
      "prototype_entropy": 2.0289254762039217,
      "prototype_margin": 0.4712773829911991,
      "prototype_monopoly_rate": 0.19921875,
      "runtime_dynamic_k_count": 0,
      "runtime_expert_choice_count": 0,
      "step": 1100,
      "structured_token_benefit": 1.3892558813095093,
      "top2_execution_count": 0,
      "top4_execution_count": 0,
      "wrong_expert_harm": 1.3789029121398926
    }
  },
  "rows": {
    "pvr_full_scratch_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints\\self_instilled_ean_geometry_head_300m_matched_volume_screen\\pvr_full_scratch_300m_matched\\checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_full_scratch_300m_matched",
      "lm_loss": 4.152685380711848,
      "model_variant": "pvr_full_scratch_300m_matched",
      "perplexity": 63.604573663708,
      "quality_per_active_flop": 3.8223497370501356e-10,
      "quality_per_active_param": 2.2934098422300814e-09,
      "tokens_per_second": 1100.83345898865,
      "top1_invariants_clean": true,
      "vram_peak": 1971427328
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints\\self_instilled_ean_geometry_head_300m_matched_volume_screen\\pvr_self_instilled_uniformity_geometry_head_v1_300m_matched\\checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
      "lm_loss": 4.146520776408059,
      "model_variant": "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
      "perplexity": 63.21368271706305,
      "quality_per_active_flop": 3.828032398469239e-10,
      "quality_per_active_param": 2.2968194390815432e-09,
      "tokens_per_second": 1137.9983245928597,
      "top1_invariants_clean": true,
      "vram_peak": 1182379008
    },
    "pvr_shared_warmup_no_geometry_head_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints\\self_instilled_ean_geometry_head_300m_matched_volume_screen\\pvr_shared_warmup_no_geometry_head_300m_matched\\checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_shared_warmup_no_geometry_head_300m_matched",
      "lm_loss": 4.145141032277321,
      "model_variant": "pvr_shared_warmup_no_geometry_head_300m_matched",
      "perplexity": 63.126524151438446,
      "quality_per_active_flop": 3.829306590394902e-10,
      "quality_per_active_param": 2.2975839542369414e-09,
      "tokens_per_second": 1133.723037780935,
      "top1_invariants_clean": true,
      "vram_peak": 1182379008
    },
    "pvr_teacher_ean_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints\\self_instilled_ean_geometry_head_300m_matched_volume_screen\\pvr_teacher_ean_300m_matched\\checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_teacher_ean_300m_matched",
      "lm_loss": 3.110029940702477,
      "model_variant": "pvr_teacher_ean_300m_matched",
      "perplexity": 22.4217157126157,
      "quality_per_active_flop": 5.103814489139793e-10,
      "quality_per_active_param": 3.0622886934838754e-09,
      "tokens_per_second": 1184.565685898699,
      "top1_invariants_clean": true,
      "vram_peak": 1182379008
    }
  },
  "schedule": {
    "expert_specialization_steps": 300,
    "geometry_active_steps": 400,
    "geometry_decay_steps": 400
  },
  "schema_version": "1.0",
  "screen_status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
  "seed": 123,
  "status": "PVR_TEACHER_EAN_SCAFFOLD_STILL_REQUIRED",
  "supported_conditions": {
    "all_top1_invariants_clean": true,
    "all_training_volumes_exactly_matched": true,
    "closes_at_least_half_teacher_gap": false,
    "confirmed_seed_count": 1,
    "geometry_beats_no_head_warmup": false,
    "geometry_beats_plain_pvr": true,
    "geometry_health_gates_pass": true,
    "heldout_eval_tokens_matched": true,
    "matches_or_beats_teacher_ean": false,
    "no_teacher_checkpoint_loaded_into_geometry_candidate": true,
    "routing_health_gates_pass": true,
    "scorecard_eval_tokens_matched": true,
    "teacher_gap_closed_fraction": 0.005912407941527643
  },
  "training_manifests": {
    "pvr_full_scratch_300m_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "ac3199918385a55f87927ce8c4f3f7033ba9dba5ac0993544e08300dd8fa1183",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_full_scratch_300m_matched/checkpoint.pt",
      "created_at": "2026-06-19T19:08:19.251160+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_full_scratch_300m_matched",
      "optimizer_steps": 1100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 11,
        "completed_steps": 1100,
        "completed_training_tokens": 1126400,
        "estimated_steps_needed": 1100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 11,
        "target_training_tokens": 1126400
      },
      "routing_window_count": 11,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "matched_volume_screen",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "1c8c90d6552cfff4f5a5751b1691edee2965e527a98e2eca168f27bc4f26a0df",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_self_instilled_uniformity_geometry_head_v1_300m_matched/checkpoint.pt",
      "created_at": "2026-06-19T19:20:40.492854+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
      "optimizer_steps": 1100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 11,
        "completed_steps": 1100,
        "completed_training_tokens": 1126400,
        "estimated_steps_needed": 1100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 11,
        "target_training_tokens": 1126400
      },
      "routing_window_count": 11,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "matched_volume_screen",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_shared_warmup_no_geometry_head_300m_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "19205629b6319c675620536babe83b78f00b597737e483974e7eea790fb6d005",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_shared_warmup_no_geometry_head_300m_matched/checkpoint.pt",
      "created_at": "2026-06-19T19:14:21.598519+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_shared_warmup_no_geometry_head_300m_matched",
      "optimizer_steps": 1100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 11,
        "completed_steps": 1100,
        "completed_training_tokens": 1126400,
        "estimated_steps_needed": 1100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 11,
        "target_training_tokens": 1126400
      },
      "routing_window_count": 11,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "matched_volume_screen",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_teacher_ean_300m_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "e11f33418625f73dcb111a3cd418d53f1dfc94a7af558c6115ac1df40e9fa611",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_teacher_ean_300m_matched/checkpoint.pt",
      "created_at": "2026-06-19T19:28:41.051360+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_teacher_ean_300m_matched",
      "optimizer_steps": 1100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 11,
        "completed_steps": 1100,
        "completed_training_tokens": 1126400,
        "estimated_steps_needed": 1100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 11,
        "target_training_tokens": 1126400
      },
      "routing_window_count": 11,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "matched_volume_screen",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    }
  },
  "training_rows": {},
  "variant_diagnostics": {},
  "variants": [
    "pvr_full_scratch_300m_matched",
    "pvr_shared_warmup_no_geometry_head_300m_matched",
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched",
    "pvr_teacher_ean_300m_matched"
  ]
}
```
