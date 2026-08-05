# Self-Instilled Trunk Total-Compute-Matched 300M Screen

Screen: `PVR_SELF_INSTILLED_TRUNK_TOTAL_COMPUTE_MATCHED_SCREEN_COMPLETE`
Decision: `PVR_SELF_INSTILLED_TRUNK_TOTAL_COMPUTE_MATCHED_SUPPORTED`

| model | training tokens | LM loss | Top1 clean |
|---|---:|---:|---|
| pvr_full_scratch_300m_matched | 1126400 | 4.152685380711848 | None |
| pvr_teacher_ean_300m_matched | 2150400 | 3.110029940702477 | None |
| pvr_full_scratch_300m_total_compute_matched | 2150400 | 3.460306534961778 | True |
| pvr_self_instilled_trunk_curriculum_300m_total_compute_matched | 2150400 | 3.434945747560384 | True |

```json
{
  "accounting": {
    "candidate_shared_pretrain_tokens": 1024000,
    "candidate_specialization_tokens": 1126400,
    "candidate_total_tokens": 2150400,
    "effective_batch_tokens": 1024,
    "teacher_downstream_tokens": 1126400,
    "teacher_inherited_dense_tokens": 1024000,
    "teacher_total_tokens": 2150400
  },
  "candidate": "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched",
  "created_at": "2026-06-19T22:12:23.088294+00:00",
  "decision_rule": "Teacher-gap closure requires the teacher-free curriculum to match or beat teacher-EAN after matching the teacher recipe's inherited dense tokens plus downstream PVR tokens, with clean strict Top1 routing. Teacher independence is not promoted until this survives at least two seeds.",
  "experiment": "PVR_SELF_INSTILLED_TRUNK_TOTAL_COMPUTE_MATCHED_SCREEN",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "phase_eval_summary": {
    "pvr_full_scratch_300m_total_compute_matched": {
      "full_training": {
        "final_eval_loss": 10.618630811572075,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 14.362849366806802,
        "window_count": 21
      }
    },
    "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched": {
      "shared_trunk_pretrain": {
        "final_eval_loss": 13.94543382525444,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 20.307022616267204,
        "window_count": 10
      },
      "strict_top1_specialization": {
        "final_eval_loss": 10.060413137078285,
        "head_active": false,
        "head_off_retained_geometry_eval": false,
        "mean_eval_loss": 11.12831080908125,
        "window_count": 11
      }
    }
  },
  "routing_health": {
    "pvr_full_scratch_300m_total_compute_matched": {
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
          152,
          209,
          176,
          140,
          280,
          137,
          234,
          208
        ],
        "full_vs_shared_benefit": 7.613570690155029,
        "optimizer_step": 2100,
        "owner_churn": 0.020833333333333332,
        "owner_entropy": 2.0501241810131408,
        "owners_per_token": 1.0,
        "phase": "full_training",
        "prototype_entropy": 2.0501241810131408,
        "prototype_margin": 0.3863371284023742,
        "prototype_monopoly_rate": 0.18229166666666666,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "step": 2100,
        "structured_token_benefit": 1.9212507009506226,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "wrong_expert_harm": 6.164541244506836
      },
      "top1_clean": true
    },
    "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched": {
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
          126,
          134,
          153,
          156,
          311,
          158,
          300,
          198
        ],
        "full_vs_shared_benefit": 0.749389111995697,
        "optimizer_step": 2100,
        "owner_churn": 0.025390625,
        "owner_entropy": 2.0203393759773705,
        "owners_per_token": 1.0,
        "phase": "strict_top1_specialization",
        "prototype_entropy": 2.0203393759773705,
        "prototype_margin": 0.46914647380860214,
        "prototype_monopoly_rate": 0.20247395833333334,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "step": 2100,
        "structured_token_benefit": 0.8453640341758728,
        "top2_execution_count": 0,
        "top4_execution_count": 0,
        "wrong_expert_harm": 1.60670804977417
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
    "pvr_full_scratch_300m_total_compute_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_trunk_total_compute_matched_300m/pvr_full_scratch_300m_total_compute_matched/checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_full_scratch_300m_total_compute_matched",
      "lm_loss": 3.460306534961778,
      "model_variant": "pvr_full_scratch_300m_total_compute_matched",
      "perplexity": 31.826731025320402,
      "quality_per_active_flop": 4.5871704465024236e-10,
      "quality_per_active_param": 2.752302267901454e-09,
      "tokens_per_second": 1016.2799406243262,
      "top1_invariants_clean": true,
      "vram_peak": 1981632512
    },
    "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_trunk_total_compute_matched_300m/pvr_self_instilled_trunk_curriculum_300m_total_compute_matched/checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched",
      "lm_loss": 3.434945747560384,
      "model_variant": "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched",
      "perplexity": 31.029729081358642,
      "quality_per_active_flop": 4.6210383044010035e-10,
      "quality_per_active_param": 2.772622982640602e-09,
      "tokens_per_second": 1023.211241596597,
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
  "screen_status": "PVR_SELF_INSTILLED_TRUNK_TOTAL_COMPUTE_MATCHED_SCREEN_COMPLETE",
  "seed": 123,
  "status": "PVR_SELF_INSTILLED_TRUNK_TOTAL_COMPUTE_MATCHED_SUPPORTED",
  "supported_conditions": {
    "candidate_downstream_specialization_tokens_match_teacher": true,
    "curriculum_beats_full_scratch_total_compute": true,
    "curriculum_beats_plain_short_budget": true,
    "curriculum_matches_or_beats_teacher_ean": false,
    "no_teacher_checkpoint_loaded": true,
    "routing_health_clean": true,
    "teacher_gap_closed_fraction": 0.688376625306835,
    "top1_clean": true,
    "total_recipe_tokens_matched": true
  },
  "teacher_checkpoint_loaded_into_candidate": false,
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
    "pvr_full_scratch_300m_total_compute_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "8ca4fab2dd003fbc3aeedf01e987452d5eb06e2f1ca476fbcba7590c455538b4",
      "checkpoint_path": "checkpoints/self_instilled_trunk_total_compute_matched_300m/pvr_full_scratch_300m_total_compute_matched/checkpoint.pt",
      "created_at": "2026-06-19T21:43:56.373156+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 21,
      "mock_checkpoint": false,
      "model": "pvr_full_scratch_300m_total_compute_matched",
      "optimizer_steps": 2100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 21,
        "completed_steps": 2100,
        "completed_training_tokens": 2150400,
        "estimated_steps_needed": 2100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 21,
        "target_training_tokens": 2150400
      },
      "routing_window_count": 21,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 21,
      "target_steps": 2100,
      "target_training_tokens": 2150400,
      "tier": "matched_volume_screen",
      "tokens_seen": 2150400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 2150400
    },
    "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "327fd3ec478480102dd0f2794187fca70f67a61855b986e24ef9010d177e058d",
      "checkpoint_path": "checkpoints/self_instilled_trunk_total_compute_matched_300m/pvr_self_instilled_trunk_curriculum_300m_total_compute_matched/checkpoint.pt",
      "created_at": "2026-06-19T21:58:00.164228+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 21,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_trunk_curriculum_300m_total_compute_matched",
      "optimizer_steps": 2100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 21,
        "completed_steps": 2100,
        "completed_training_tokens": 2150400,
        "estimated_steps_needed": 2100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 21,
        "target_training_tokens": 2150400
      },
      "routing_window_count": 21,
      "schema_version": "1.0",
      "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_MATCHED_VOLUME_SCREEN_COMPLETE",
      "target_eval_windows": 21,
      "target_steps": 2100,
      "target_training_tokens": 2150400,
      "tier": "matched_volume_screen",
      "tokens_seen": 2150400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 2150400
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
