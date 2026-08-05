# Self-Instilled EAN Geometry Head Audit

Status: `PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_PROBE_ONLY_COMPLETE`

| model | tokens | LM loss | active params/token | active FLOPs/token | Top1 clean |
|---|---:|---:|---:|---:|---|
| dense_700m | 1126400 | 8.232686072587967 | 700000000 | 4200000000 | None |
| generic_top2_700m | 1126400 | 9.194304779171944 | 350000000 | 2100000000 | None |
| pvr_ean_retention_gated_700m | 1126400 | 5.640043392777443 | 244999999 | 1469999994 | True |
| pvr_ean_token_matched_700m | 1126400 | 6.2625821977853775 | 244999999 | 1469999994 | True |
| pvr_full_700m | 1126400 | 8.82107788324356 | 244999999 | 1469999994 | True |
| pvr_self_instilled_uniformity_geometry_head_v1_700m | 102400 | 24.67221090197563 | 244999999 | 1469999994 | True |
| switch_top1_700m | 1126400 | 8.575665526092052 | 244999999 | 1469999994 | None |

```json
{
  "candidate": "pvr_self_instilled_uniformity_geometry_head_v1_700m",
  "claim_scope": "700M local reduced-file scratch-PVR geometry-head audit; no dense teacher checkpoint is loaded into the candidate.",
  "created_at": "2026-06-19T15:21:31.955451+00:00",
  "decision_rule": "Support requires the self-instilled geometry-head PVR to beat plain scratch PVR, preserve clean Top1, and close at least half of the PVR-to-EAN loss gap. Closing teacher gap requires matching or beating EAN.",
  "experiment": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_AUDIT",
  "geometry_diagnostics": {
    "final_geometry_metrics": {
      "alignment_loss": 2.2235735741560347e-05,
      "covariance_loss": 0.0008534007938578725,
      "covariance_offdiag_energy": 1.3546045011025853e-05,
      "effective_rank": 15.330278396606445,
      "geometry_loss": 0.0,
      "isotropy_score": 0.4127808213233948,
      "scale_loss": 0.7371702194213867,
      "uniformity_loss": -2.2243459224700928,
      "variance_loss": 0.8921030759811401
    },
    "geometry_head": {
      "d_geo": 64,
      "decay_steps": 80,
      "discarded_for_inference": true,
      "sample_tokens": 256,
      "selected_layers": [
        0,
        16,
        31
      ],
      "weights": {
        "alignment": 0.001,
        "covariance": 0.0007,
        "noise_std": 0.01,
        "norm": 0.0005,
        "uniformity": 0.002,
        "uniformity_tau": 2.0,
        "variance": 0.001
      }
    }
  },
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "rows": {
    "dense_700m": {
      "active_flops_per_token": 4200000000,
      "active_params_per_token": 700000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/dense_transformer_700m_seed_123/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "dense_700m",
      "lm_loss": 8.232686072587967,
      "model_variant": "dense_transformer_700m",
      "perplexity": 3761.9249967266237,
      "quality_per_active_flop": 2.892072356408851e-11,
      "quality_per_active_param": 1.7352434138453107e-10,
      "tokens_per_second": 6418.026342500322,
      "top1_invariants_clean": null,
      "vram_peak": 2566800384
    },
    "generic_top2_700m": {
      "active_flops_per_token": 2100000000,
      "active_params_per_token": 350000000,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/generic_top2_moe_reference_700m_seed_123/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "generic_top2_700m",
      "lm_loss": 9.194304779171944,
      "model_variant": "generic_top2_moe_reference_700m",
      "perplexity": 9840.922928275984,
      "quality_per_active_flop": 5.179189592117946e-11,
      "quality_per_active_param": 3.1075137552707676e-10,
      "tokens_per_second": 601.9147721783414,
      "top1_invariants_clean": null,
      "vram_peak": 2715018240
    },
    "pvr_ean_retention_gated_700m": {
      "active_flops_per_token": 1469999994,
      "active_params_per_token": 244999999,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_ean_retention_gated_delta_replay_700m/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "pvr_ean_retention_gated_700m",
      "lm_loss": 5.640043392777443,
      "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_700m",
      "perplexity": 281.47493218937296,
      "quality_per_active_flop": 1.2061469464779382e-10,
      "quality_per_active_param": 7.236881678867628e-10,
      "tokens_per_second": 947.4235581915234,
      "top1_invariants_clean": true,
      "vram_peak": 3002252288
    },
    "pvr_ean_token_matched_700m": {
      "active_flops_per_token": 1469999994,
      "active_params_per_token": 244999999,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_ean_token_matched_700m/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "pvr_ean_token_matched_700m",
      "lm_loss": 6.2625821977853775,
      "model_variant": "pvr_ec_o_ean_token_matched_700m",
      "perplexity": 524.571740744141,
      "quality_per_active_flop": 1.0862485954447374e-10,
      "quality_per_active_param": 6.517491572668424e-10,
      "tokens_per_second": 944.045076242661,
      "top1_invariants_clean": true,
      "vram_peak": 3002252288
    },
    "pvr_full_700m": {
      "active_flops_per_token": 1469999994,
      "active_params_per_token": 244999999,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_full_700m_seed_123/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "pvr_full_700m",
      "lm_loss": 8.82107788324356,
      "model_variant": "pvr_ec_o_full_700m",
      "perplexity": 6775.56395750397,
      "quality_per_active_flop": 7.711893270009519e-11,
      "quality_per_active_param": 4.627135962005711e-10,
      "tokens_per_second": 847.3018794857283,
      "top1_invariants_clean": true,
      "vram_peak": 3002252288
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_700m": {
      "active_flops_per_token": 1469999994,
      "active_params_per_token": 244999999,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "pvr_self_instilled_uniformity_geometry_head_v1_700m",
      "lm_loss": 24.67221090197563,
      "model_variant": "pvr_self_instilled_uniformity_geometry_head_v1_700m",
      "perplexity": 51880607289.095436,
      "quality_per_active_flop": 2.757240177310925e-11,
      "quality_per_active_param": 1.654344106386555e-10,
      "tokens_per_second": 858.4894400497468,
      "top1_invariants_clean": true,
      "vram_peak": 3002252288
    },
    "switch_top1_700m": {
      "active_flops_per_token": 1469999994,
      "active_params_per_token": 244999999,
      "benchmark_evidence": true,
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/vanilla_switch_top1_reference_700m_seed_123/checkpoint.pt",
      "eval_token_count": 8192,
      "heldout_eval_token_count": 2048,
      "key": "switch_top1_700m",
      "lm_loss": 8.575665526092052,
      "model_variant": "vanilla_switch_top1_reference_700m",
      "perplexity": 5301.078270395444,
      "quality_per_active_flop": 7.932586800993854e-11,
      "quality_per_active_param": 4.759552080596312e-10,
      "tokens_per_second": 666.4303310347195,
      "top1_invariants_clean": null,
      "vram_peak": 2715018240
    }
  },
  "schema_version": "1.0",
  "score_root": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123_scorecards",
  "seed": 123,
  "status": "PVR_SELF_INSTILLED_EAN_GEOMETRY_HEAD_PROBE_ONLY_COMPLETE",
  "supported_conditions": {
    "beats_dense": false,
    "beats_plain_pvr": false,
    "gap_closed_fraction": -6.1954894467189225,
    "matches_or_beats_ean": false,
    "narrows_at_least_half_ean_gap": false,
    "top1_clean": true,
    "training_volume_matched": false
  },
  "teacher_checkpoint_loaded": false,
  "training_manifests": {
    "dense_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "a2446b27b91b1946eccb4922e0834d7e0a38b9923e86fae85d3bfa0e6468fe30",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/dense_transformer_700m_seed_123/checkpoint.pt",
      "created_at": "2026-06-19T03:44:02.177463+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "dense_transformer_700m",
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
      "routing_window_count": 0,
      "schema_version": "1.0",
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "real_comparison",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "generic_top2_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "c248d125d6339ed73a618f34afa3af7b86f76f4e27b8f8c332b46d13173720ef",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/generic_top2_moe_reference_700m_seed_123/checkpoint.pt",
      "created_at": "2026-06-19T04:03:09.454758+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "generic_top2_moe_reference_700m",
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
      "routing_window_count": 0,
      "schema_version": "1.0",
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "real_comparison",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_ean_retention_gated_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "2481b678b1fc23fdbeda89be030ca88a9cb45ae2c303aab9c094a91490f8edc9",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_ean_retention_gated_delta_replay_700m/checkpoint.pt",
      "created_at": "2026-06-19T04:32:09.469966+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 10,
      "mock_checkpoint": false,
      "model": "pvr_ec_o_ean_retention_gated_delta_replay_700m",
      "optimizer_steps": 1100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 10,
        "completed_steps": 1100,
        "completed_training_tokens": 1126400,
        "estimated_steps_needed": 1000,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 10,
        "target_training_tokens": 1024000
      },
      "routing_window_count": 10,
      "schema_version": "1.0",
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 10,
      "target_steps": 1000,
      "target_training_tokens": 1024000,
      "tier": "real_comparison_retention_gated_replay",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_ean_token_matched_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "82fae1c2023a49db38d50160fed39dafe31680c6390cc47b99c1567283f396dc",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_ean_token_matched_700m/checkpoint.pt",
      "created_at": "2026-06-19T04:22:14.110574+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_ec_o_ean_token_matched_700m",
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
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "real_comparison",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_full_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "706c4f42614f405aa0848cbe2c19fc95d4da9404516a336ff124eb0eb583fff4",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/pvr_ec_o_full_700m_seed_123/checkpoint.pt",
      "created_at": "2026-06-19T04:13:48.466016+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "pvr_ec_o_full_700m",
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
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "real_comparison",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    },
    "pvr_self_instilled_uniformity_geometry_head_v1_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "f212dc0c87c8f728445546099229909c02f940b6e76886886e9dcf727b092ed8",
      "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/checkpoint.pt",
      "created_at": "2026-06-19T15:06:19.758386+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 1,
      "mock_checkpoint": false,
      "model": "pvr_self_instilled_uniformity_geometry_head_v1_700m",
      "optimizer_steps": 100,
      "real_training_data": true,
      "resource_reduction": {
        "completed_eval_windows": 1,
        "completed_steps": 100,
        "completed_training_tokens": 102400,
        "estimated_steps_needed": 100,
        "reason_for_reduction": "",
        "status": "NONE",
        "target_eval_windows": 1,
        "target_training_tokens": 102400
      },
      "routing_window_count": 1,
      "schema_version": "1.0",
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 1,
      "target_steps": 100,
      "target_training_tokens": 102400,
      "tier": "real_comparison",
      "tokens_seen": 102400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 102400
    },
    "switch_top1_700m": {
      "checkpoint_exists": true,
      "checkpoint_hash": "26bec938f0adb628c5629ffb2e63389636c35a30acfe31a943cf9a6d07e035c6",
      "checkpoint_path": "checkpoints/ean_retention_gated_token_matched_700m_seed_123_strict/vanilla_switch_top1_reference_700m_seed_123/checkpoint.pt",
      "created_at": "2026-06-19T03:52:42.511164+00:00",
      "effective_batch_tokens": 1024,
      "error": null,
      "eval_window_count": 11,
      "mock_checkpoint": false,
      "model": "vanilla_switch_top1_reference_700m",
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
      "routing_window_count": 0,
      "schema_version": "1.0",
      "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
      "target_eval_windows": 11,
      "target_steps": 1100,
      "target_training_tokens": 1126400,
      "tier": "real_comparison",
      "tokens_seen": 1126400,
      "training_data_paths": [
        "data/broad_nlp_train"
      ],
      "training_tokens_seen": 1126400
    }
  },
  "training_row": {
    "checkpoint_exists": true,
    "checkpoint_manifest": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/checkpoint_manifest.json",
    "checkpoint_path": "checkpoints/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/checkpoint.pt",
    "effective_batch_tokens": 1024,
    "error": null,
    "eval_curve": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/eval_curve.json",
    "eval_window_count": 1,
    "final_loss": 11.893289566040039,
    "gpu_hours": 0.016076401670773822,
    "hardware_manifest": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/hardware_manifest.json",
    "model_variant": "pvr_self_instilled_uniformity_geometry_head_v1_700m",
    "optimizer_steps": 100,
    "routing_curve": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/routing_curve.json",
    "routing_window_count": 1,
    "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
    "throughput_log": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/throughput_log.json",
    "tokens_seen": 102400,
    "training_curve": "benchmark/reports/generated/self_instilled_ean_geometry_head_probe_700m_seed_123/pvr_self_instilled_uniformity_geometry_head_v1_700m/training_curve.json",
    "training_tokens_seen": 102400,
    "vram_peak": 14962013184
  }
}
```
