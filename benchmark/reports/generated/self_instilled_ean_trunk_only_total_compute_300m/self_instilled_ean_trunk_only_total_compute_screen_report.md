# Self-Instilled EAN Trunk-Only Total-Compute Screen

Screen: `PVR_SELF_INSTILLED_EAN_TRUNK_ONLY_TOTAL_COMPUTE_SCREEN_COMPLETE`
Decision: `PVR_SELF_INSTILLED_EAN_TRUNK_ONLY_NARROWS_TEACHER_GAP`

| model | LM loss |
|---|---:|
| pvr_full_scratch_300m_matched | 4.152685380711848 |
| pvr_teacher_ean_300m_matched | 3.110029940702477 |
| pvr_full_scratch_300m_total_compute_matched | 3.460306534961778 |
| pvr_self_instilled_trunk_curriculum_300m_total_compute_matched | 3.434945747560384 |
| pvr_self_instilled_ean_trunk_only_300m_total_compute_matched | 3.1338969700190487 |

```json
{
  "accounting": {
    "candidate_specialization_tokens": 1126400,
    "candidate_total_tokens": 2150400,
    "candidate_trunk_only_pretrain_tokens": 1024000,
    "effective_batch_tokens": 1024,
    "teacher_downstream_tokens": 1126400,
    "teacher_inherited_dense_tokens": 1024000,
    "teacher_total_tokens": 2150400
  },
  "candidate": "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched",
  "created_at": "2026-06-20T01:34:48.597527+00:00",
  "decision_rule": "Single-seed closure requires the teacher-free trunk-only curriculum to match or beat teacher-EAN under matched total recipe tokens, matched downstream specialization tokens, optimizer reset, and clean Top1.",
  "experiment": "PVR_SELF_INSTILLED_EAN_TRUNK_ONLY_TOTAL_COMPUTE_SCREEN",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "phase_eval_summary": {
    "ean_trunk_only_pretrain": {
      "final_eval_loss": 12.11053290963173,
      "head_active": false,
      "head_off_retained_geometry_eval": false,
      "mean_eval_loss": 24.621906426548957,
      "window_count": 10
    },
    "strict_top1_specialization": {
      "final_eval_loss": 7.840873941779137,
      "head_active": false,
      "head_off_retained_geometry_eval": false,
      "mean_eval_loss": 8.997933535413308,
      "window_count": 11
    }
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
        174,
        221,
        230,
        57,
        232,
        139,
        235,
        248
      ],
      "full_vs_shared_benefit": 0.740192711353302,
      "optimizer_step": 2100,
      "owner_churn": 0.028645833333333332,
      "owner_entropy": 2.0167874252817066,
      "owners_per_token": 1.0,
      "phase": "strict_top1_specialization",
      "prototype_entropy": 2.0167874252817066,
      "prototype_margin": 0.3369319068782109,
      "prototype_monopoly_rate": 0.16145833333333334,
      "runtime_dynamic_k_count": 0,
      "runtime_expert_choice_count": 0,
      "step": 2100,
      "structured_token_benefit": 1.411523461341858,
      "top2_execution_count": 0,
      "top4_execution_count": 0,
      "wrong_expert_harm": 0.8259739875793457
    },
    "top1_clean": true
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
    "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched": {
      "active_flops_per_token": 630000000,
      "active_params_per_token": 105000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_trunk_only_total_compute_300m/pvr_self_instilled_ean_trunk_only_300m_total_compute_matched/checkpoint.pt",
      "eval_token_count": 50176,
      "heldout_eval_token_count": 12544,
      "key": "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched",
      "lm_loss": 3.1338969700190487,
      "model_variant": "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched",
      "perplexity": 22.963292667190238,
      "quality_per_active_flop": 5.064945026868383e-10,
      "quality_per_active_param": 3.03896701612103e-09,
      "tokens_per_second": 958.3455709013296,
      "top1_invariants_clean": true,
      "vram_peak": 1969726464
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
  "screen_status": "PVR_SELF_INSTILLED_EAN_TRUNK_ONLY_TOTAL_COMPUTE_SCREEN_COMPLETE",
  "seed": 123,
  "status": "PVR_SELF_INSTILLED_EAN_TRUNK_ONLY_NARROWS_TEACHER_GAP",
  "supported_conditions": {
    "beats_full_scratch_total_compute": true,
    "beats_shared_block_curriculum": true,
    "matches_or_beats_teacher_ean": false,
    "no_teacher_checkpoint_loaded": true,
    "optimizer_reset_at_transfer_boundary": true,
    "routing_health_clean": true,
    "specialization_tokens_match_teacher": true,
    "teacher_gap_closed_fraction": 0.9771093801454132,
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
    "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched": {
      "checkpoint_exists": true,
      "checkpoint_hash": "09fd63b53f0e06e2c4770bbe2acf0ee47b060bc0b9bc70b4bcade68f5d092c44",
      "checkpoint_path": "checkpoints/self_instilled_ean_trunk_only_total_compute_300m/pvr_self_instilled_ean_trunk_only_300m_total_compute_matched/checkpoint.pt",
      "created_at": "2026-06-20T01:27:43.208663+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 21,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_ean_trunk_only_300m_total_compute_matched",
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
