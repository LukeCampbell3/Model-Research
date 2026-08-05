# Self-Instilled EAN Geometry Head V2 Objective Screen

Screen: `PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_V2_OBJECTIVE_SCREEN_COMPLETE`
Decision: `PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_V2_NOT_SUPPORTED`
Best candidate: `pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m`

| model | tokens | LM loss | Top1 clean |
|---|---:|---:|---|
| pvr_full_scratch_300m_matched | 1126400 | 4.152685380711848 | None |
| pvr_shared_warmup_no_geometry_head_300m_matched | 1126400 | 4.145141032277321 | None |
| pvr_self_instilled_uniformity_geometry_head_v1_300m_matched | 1126400 | 4.146520776408059 | None |
| pvr_teacher_ean_300m_matched | 1126400 | 3.110029940702477 | None |
| pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m | 1126400 | 4.143822378041793 | True |
| pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m | 1126400 | 4.145980190257637 | True |

```json
{
  "best_candidate": "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m",
  "budget": {
    "effective_batch_tokens": 1024,
    "eval_windows_per_model": 11,
    "optimizer_steps": 1100,
    "training_tokens_per_model": 1126400
  },
  "candidate_conditions": {
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "beats_no_head_control": true,
      "beats_plain": true,
      "closes_half_gap": false,
      "geometry_health_clean": false,
      "matches_or_beats_teacher": false,
      "routing_health_clean": true,
      "teacher_checkpoint_loaded": false,
      "teacher_gap_closed_fraction": 0.008500413780007206
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "beats_no_head_control": false,
      "beats_plain": true,
      "closes_half_gap": false,
      "geometry_health_clean": false,
      "matches_or_beats_teacher": false,
      "routing_health_clean": true,
      "teacher_checkpoint_loaded": false,
      "teacher_gap_closed_fraction": 0.006430878502058692
    }
  },
  "compute_accounting_caveat": "Teacher-EAN inherits a dense checkpoint trained for 1,024,000 tokens before its matched 1,126,400-token PVR run. This screen matches downstream PVR tokens, not total inherited recipe compute.",
  "created_at": "2026-06-19T21:23:05.462611+00:00",
  "decision_rule": "V2 support requires beating plain scratch and the no-head warmup under matched volume with clean geometry/routing health. Narrowing requires closing at least 50% of the plain-to-teacher-EAN gap.",
  "experiment": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_V2_OBJECTIVE_SCREEN",
  "geometry_health": {
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "all_health_gates_pass": false,
      "conditions": {
        "activation_norm_stable": true,
        "covariance_bounded": true,
        "effective_rank_not_collapsed": false,
        "head_received_gradients": true,
        "isotropy_not_collapsed": true,
        "layerwise_variance_positive": true,
        "metrics_finite": true,
        "metrics_present": true,
        "post_decay_probe_present": true
      },
      "post_decay": {
        "activation_norm_cv": 0.943938672542572,
        "activation_norm_mean": 9.400886535644531,
        "activation_norm_std": 8.873860359191895,
        "covariance_loss": 0.03407251834869385,
        "covariance_offdiag_energy": 2.079621481243521e-06,
        "cross_layer_predictive_loss": 0.3743981719017029,
        "effective_rank": 13.200300216674805,
        "geometry_head_gradient_norm": 0.0,
        "geometry_weight_scale": 0.0,
        "head_active": false,
        "isotropy_score": 0.6889229416847229,
        "layerwise_variance_floor": 1.9138436317443848,
        "measurement_only": true,
        "norm_scale_loss": 0.8907301425933838,
        "phase": "expert_specialization",
        "reconstruction_loss": 0.9475418925285339,
        "redundancy_reduction_loss": 0.03063836321234703,
        "sample_count": 3072,
        "shared_trunk_gradient_norm": 0.0,
        "spectral_loss": 0.1345445215702057,
        "step": "post_decay_final",
        "temporal_predictive_loss": 0.15540055930614471,
        "total_geometry_loss": 0.016693076118826866,
        "variance_loss": 0.003011438762769103
      },
      "start": {
        "activation_norm_cv": 0.1935146301984787,
        "activation_norm_mean": 1.8764312267303467,
        "activation_norm_std": 0.36311689019203186,
        "covariance_loss": 0.012498515658080578,
        "covariance_offdiag_energy": 7.628488560840196e-07,
        "cross_layer_predictive_loss": 1.0098981857299805,
        "effective_batch_tokens": 1024,
        "effective_rank": 40.78481674194336,
        "geometry_head_gradient_norm": 0.028350029861790877,
        "geometry_weight_scale": 1.0,
        "head_active": true,
        "isotropy_score": 0.663565456867218,
        "layerwise_variance_floor": 1.9754647016525269,
        "lm_loss": 416.978515625,
        "loss": 417.0146484375,
        "norm_scale_loss": 0.03743571788072586,
        "optimizer_step": 1,
        "phase": "geometry_active",
        "reconstruction_loss": 1.004952311515808,
        "redundancy_reduction_loss": 0.018092211335897446,
        "sample_count": 3072,
        "shared_only_execution": true,
        "shared_trunk_gradient_norm": 363.099377448398,
        "spectral_loss": 0.048501498997211456,
        "step": 1,
        "temporal_predictive_loss": 1.007317066192627,
        "total_geometry_loss": 0.036125943064689636,
        "training_tokens_seen": 1024,
        "variance_loss": 0.00016901544586289674
      }
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "all_health_gates_pass": false,
      "conditions": {
        "activation_norm_stable": true,
        "covariance_bounded": true,
        "effective_rank_not_collapsed": false,
        "head_received_gradients": true,
        "isotropy_not_collapsed": true,
        "layerwise_variance_positive": true,
        "metrics_finite": true,
        "metrics_present": true,
        "post_decay_probe_present": true
      },
      "post_decay": {
        "activation_norm_cv": 0.9439072608947754,
        "activation_norm_mean": 9.401798248291016,
        "activation_norm_std": 8.874425888061523,
        "covariance_loss": 0.023483017459511757,
        "covariance_offdiag_energy": 1.4332896398627781e-06,
        "cross_layer_predictive_loss": 0.19868920743465424,
        "effective_rank": 4.523388385772705,
        "geometry_head_gradient_norm": 0.0,
        "geometry_weight_scale": 0.0,
        "head_active": false,
        "isotropy_score": 0.49960577487945557,
        "layerwise_variance_floor": 1.9138407707214355,
        "measurement_only": true,
        "norm_scale_loss": 0.890670895576477,
        "phase": "expert_specialization",
        "reconstruction_loss": 0.936430811882019,
        "redundancy_reduction_loss": 0.03431873023509979,
        "sample_count": 3072,
        "shared_trunk_gradient_norm": 0.0,
        "spectral_loss": 0.40172111988067627,
        "step": "post_decay_final",
        "temporal_predictive_loss": 0.09875043481588364,
        "total_geometry_loss": 0.026186680421233177,
        "variance_loss": 0.14742302894592285
      },
      "start": {
        "activation_norm_cv": 0.1935146301984787,
        "activation_norm_mean": 1.8764312267303467,
        "activation_norm_std": 0.36311689019203186,
        "covariance_loss": 0.012498515658080578,
        "covariance_offdiag_energy": 7.628488560840196e-07,
        "cross_layer_predictive_loss": 1.0098981857299805,
        "effective_batch_tokens": 1024,
        "effective_rank": 40.78481674194336,
        "geometry_head_gradient_norm": 0.0746166372375824,
        "geometry_weight_scale": 1.0,
        "head_active": true,
        "isotropy_score": 0.663565456867218,
        "layerwise_variance_floor": 1.9754647016525269,
        "lm_loss": 416.978515625,
        "loss": 417.0697021484375,
        "norm_scale_loss": 0.03743571788072586,
        "optimizer_step": 1,
        "phase": "geometry_active",
        "reconstruction_loss": 1.004952311515808,
        "redundancy_reduction_loss": 0.018092211335897446,
        "sample_count": 3072,
        "shared_only_execution": true,
        "shared_trunk_gradient_norm": 363.0992665910208,
        "spectral_loss": 0.048501498997211456,
        "step": 1,
        "temporal_predictive_loss": 1.007317066192627,
        "total_geometry_loss": 0.09119769185781479,
        "training_tokens_seen": 1024,
        "variance_loss": 0.00016901544586289674
      }
    }
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "objective": {
    "components": [
      "spectral_diagonal_target",
      "variance_floor",
      "covariance_reduction",
      "cross_layer_prediction",
      "barlow_redundancy_reduction",
      "next_position_prediction",
      "hidden_reconstruction",
      "norm_scale_stability"
    ],
    "pure_uniformity_removed": true,
    "variance_target_matches_hypersphere_scale": true,
    "weight_sets": {
      "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
        "covariance": 0.01,
        "cross_layer": 0.02,
        "norm": 0.001,
        "reconstruction": 0.005,
        "redundancy": 0.01,
        "spectral": 0.01,
        "temporal": 0.01,
        "variance": 0.01
      },
      "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
        "covariance": 0.005,
        "cross_layer": 0.05,
        "norm": 0.001,
        "reconstruction": 0.01,
        "redundancy": 0.005,
        "spectral": 0.005,
        "temporal": 0.03,
        "variance": 0.005
      }
    }
  },
  "phase_eval_summary": {
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "expert_specialization": {
        "final_eval_loss": 12.378956004977226,
        "head_active": false,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 12.604039028286934,
        "window_count": 3
      },
      "geometry_active": {
        "final_eval_loss": 18.03168347477913,
        "head_active": true,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 27.77092605084181,
        "window_count": 4
      },
      "geometry_decay": {
        "final_eval_loss": 14.934327960014343,
        "head_active": true,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 15.87716956436634,
        "window_count": 4
      }
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "expert_specialization": {
        "final_eval_loss": 12.377762004733086,
        "head_active": false,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 12.602620214223862,
        "window_count": 3
      },
      "geometry_active": {
        "final_eval_loss": 18.030995190143585,
        "head_active": true,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 27.771985933184624,
        "window_count": 4
      },
      "geometry_decay": {
        "final_eval_loss": 14.933726221323013,
        "head_active": true,
        "head_off_retained_geometry_eval": true,
        "mean_eval_loss": 15.876345664262772,
        "window_count": 4
      }
    }
  },
  "post_decay_geometry_probes": {
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "created_at": "2026-06-19T21:06:21.947254+00:00",
      "head_used_for_inference": false,
      "metrics": {
        "activation_norm_cv": 0.943938672542572,
        "activation_norm_mean": 9.400886535644531,
        "activation_norm_std": 8.873860359191895,
        "covariance_loss": 0.03407251834869385,
        "covariance_offdiag_energy": 2.079621481243521e-06,
        "cross_layer_predictive_loss": 0.3743981719017029,
        "effective_rank": 13.200300216674805,
        "geometry_head_gradient_norm": 0.0,
        "geometry_weight_scale": 0.0,
        "head_active": false,
        "isotropy_score": 0.6889229416847229,
        "layerwise_variance_floor": 1.9138436317443848,
        "measurement_only": true,
        "norm_scale_loss": 0.8907301425933838,
        "phase": "expert_specialization",
        "reconstruction_loss": 0.9475418925285339,
        "redundancy_reduction_loss": 0.03063836321234703,
        "sample_count": 3072,
        "shared_trunk_gradient_norm": 0.0,
        "spectral_loss": 0.1345445215702057,
        "step": "post_decay_final",
        "temporal_predictive_loss": 0.15540055930614471,
        "total_geometry_loss": 0.016693076118826866,
        "variance_loss": 0.003011438762769103
      },
      "schema_version": "1.0",
      "status": "POST_DECAY_GEOMETRY_PROBE_COMPLETE"
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "created_at": "2026-06-19T21:07:02.539070+00:00",
      "head_used_for_inference": false,
      "metrics": {
        "activation_norm_cv": 0.9439072608947754,
        "activation_norm_mean": 9.401798248291016,
        "activation_norm_std": 8.874425888061523,
        "covariance_loss": 0.023483017459511757,
        "covariance_offdiag_energy": 1.4332896398627781e-06,
        "cross_layer_predictive_loss": 0.19868920743465424,
        "effective_rank": 4.523388385772705,
        "geometry_head_gradient_norm": 0.0,
        "geometry_weight_scale": 0.0,
        "head_active": false,
        "isotropy_score": 0.49960577487945557,
        "layerwise_variance_floor": 1.9138407707214355,
        "measurement_only": true,
        "norm_scale_loss": 0.890670895576477,
        "phase": "expert_specialization",
        "reconstruction_loss": 0.936430811882019,
        "redundancy_reduction_loss": 0.03431873023509979,
        "sample_count": 3072,
        "shared_trunk_gradient_norm": 0.0,
        "spectral_loss": 0.40172111988067627,
        "step": "post_decay_final",
        "temporal_predictive_loss": 0.09875043481588364,
        "total_geometry_loss": 0.026186680421233177,
        "variance_loss": 0.14742302894592285
      },
      "schema_version": "1.0",
      "status": "POST_DECAY_GEOMETRY_PROBE_COMPLETE"
    }
  },
  "routing_health": {
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
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
          154,
          140,
          307,
          170,
          286,
          200
        ],
        "full_vs_shared_benefit": 0.9101648926734924,
        "optimizer_step": 1100,
        "owner_churn": 0.0234375,
        "owner_entropy": 2.0284794964115673,
        "owners_per_token": 1.0,
        "phase": "expert_specialization",
        "prototype_entropy": 2.0284794964115673,
        "prototype_margin": 0.4712392303335946,
        "prototype_monopoly_rate": 0.19986979166666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "step": 1100,
        "structured_token_benefit": 1.3821780681610107,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "wrong_expert_harm": 1.384403944015503
      },
      "top1_clean": true
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
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
          154,
          140,
          307,
          170,
          286,
          200
        ],
        "full_vs_shared_benefit": 0.9122015237808228,
        "optimizer_step": 1100,
        "owner_churn": 0.0234375,
        "owner_entropy": 2.0284794964115673,
        "owners_per_token": 1.0,
        "phase": "expert_specialization",
        "prototype_entropy": 2.0284794964115673,
        "prototype_margin": 0.47126592863787664,
        "prototype_monopoly_rate": 0.19986979166666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "step": 1100,
        "structured_token_benefit": 1.3886903524398804,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "wrong_expert_harm": 1.3855657577514648
      },
      "top1_clean": true
    }
  },
  "rows": {
    "pvr_full_scratch_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_full_scratch_300m_matched/checkpoint.pt",
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
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_v2_300m_screen/pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m/checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m",
      "lm_loss": 4.143822378041793,
      "model_variant": "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m",
      "perplexity": 63.04333695262216,
      "quality_per_active_flop": 3.8305251588792366e-10,
      "quality_per_active_param": 2.2983150953275418e-09,
      "tokens_per_second": 766.8479178893858,
      "top1_invariants_clean": true,
      "vram_peak": 1182379008
    },
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_v2_300m_screen/pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m/checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m",
      "lm_loss": 4.145980190257637,
      "model_variant": "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m",
      "perplexity": 63.17951951057912,
      "quality_per_active_flop": 3.828531528036438e-10,
      "quality_per_active_param": 2.2971189168218627e-09,
      "tokens_per_second": 865.9989738046967,
      "top1_invariants_clean": true,
      "vram_peak": 1182379008
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_300m_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_self_instilled_uniformity_geometry_head_v1_300m_matched/checkpoint.pt",
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
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_shared_warmup_no_geometry_head_300m_matched/checkpoint.pt",
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
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_300m_matched_volume_screen/pvr_teacher_ean_300m_matched/checkpoint.pt",
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
  "schema_version": "1.0",
  "screen_status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_V2_OBJECTIVE_SCREEN_COMPLETE",
  "seed": 123,
  "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_V2_NOT_SUPPORTED",
  "teacher_checkpoint_loaded_into_candidates": false,
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
    "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "d9845eaa4b06a74990cc7cc8a69ab20ff0145a9cefbd65b32d4abbc640bb4335",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_v2_300m_screen/pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m/checkpoint.pt",
      "created_at": "2026-06-19T20:57:03.100055+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_spectral_predictive_geometry_v2_balanced_300m",
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
    "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "7e6a1caeb6f10e329c68aa59ceac7458226fa28113cdf0344e2096b60f32434f",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_v2_300m_screen/pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m/checkpoint.pt",
      "created_at": "2026-06-19T21:05:40.423619+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_spectral_predictive_geometry_v2_predictive_300m",
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
  }
}
```
