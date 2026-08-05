# EAN Retention-Gated Delta Replay Full Promotion Audit

Status: `PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT_SUPPORTED`
Broad windows: `3506`

```json
{
  "benchmark_evidence_caveat": "Full local reduced-file audit only. Official benchmark adapters remain separate.",
  "broad_tolerance": 0.03,
  "broad_windows": 3506,
  "candidate_configs": [
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json"
  ],
  "candidate_results": [
    {
      "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "rows": {
        "dense_300m": {
          "active_flops_estimate": 1800000000,
          "active_params_per_token": 300000000,
          "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
          "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
          "key": "dense_300m",
          "model_family": "dense_transformer",
          "model_variant": "dense_transformer_300m",
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.49954605102539,
              "mean_loss": 2.694834201048934,
              "min_loss": 2.0842881202697754,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.49954605102539,
              "mean_loss": 2.694834201048934,
              "min_loss": 2.0842881202697754,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 16.16033935546875,
              "mean_loss": 14.023216485977173,
              "min_loss": 13.100582122802734,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 19.473281860351562,
              "mean_loss": 14.586094975471497,
              "min_loss": 9.624191284179688,
              "window_count": 8
            }
          },
          "top1_invariants_clean": null
        },
        "pvr_baseline_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
          "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
          "key": "pvr_baseline_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.4764863158367613,
              "expert_utilization": [
                265,
                400,
                363,
                158,
                546,
                323,
                389,
                628
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20442708333333334,
              "operator_control_margin": 0.4764863158367613,
              "owner_churn": null,
              "owner_entropy": 2.0118771550900942,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0118771550900942,
              "prototype_margin": 0.4764863158367613,
              "prototype_monopoly_rate": 0.20442708333333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.47544338050526375,
              "expert_utilization": [
                275,
                389,
                362,
                135,
                547,
                393,
                398,
                573
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.1865234375,
              "operator_control_margin": 0.47544338050526375,
              "owner_churn": null,
              "owner_entropy": 2.015325695027265,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.015325695027265,
              "prototype_margin": 0.47544338050526375,
              "prototype_monopoly_rate": 0.1865234375,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.477010672443915,
              "expert_utilization": [
                288,
                399,
                363,
                149,
                571,
                374,
                388,
                540
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.18587239583333334,
              "operator_control_margin": 0.477010672443915,
              "owner_churn": null,
              "owner_entropy": 2.022228376128187,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.022228376128187,
              "prototype_margin": 0.477010672443915,
              "prototype_monopoly_rate": 0.18587239583333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.46924798957722186,
              "expert_utilization": [
                285,
                409,
                347,
                145,
                540,
                330,
                393,
                623
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20279947916666666,
              "operator_control_margin": 0.46924798957722186,
              "owner_churn": null,
              "owner_entropy": 2.011370364940322,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.011370364940322,
              "prototype_margin": 0.46924798957722186,
              "prototype_monopoly_rate": 0.20279947916666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 13.596904754638672,
              "mean_loss": 2.7352521221636366,
              "min_loss": 2.1119062900543213,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 13.596904754638672,
              "mean_loss": 2.7352521221636366,
              "min_loss": 2.1119062900543213,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 11.232419967651367,
              "mean_loss": 10.401772260665894,
              "min_loss": 9.930900573730469,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.387349307537079,
              "min_loss": 7.083217144012451,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "pvr_ean_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
          "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
          "key": "pvr_ean_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5172737978258132,
              "expert_utilization": [
                360,
                274,
                487,
                602,
                243,
                406,
                348,
                352
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.19596354166666666,
              "operator_control_margin": 0.5172737978258132,
              "owner_churn": null,
              "owner_entropy": 2.0412845783848734,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0412845783848734,
              "prototype_margin": 0.5172737978258132,
              "prototype_monopoly_rate": 0.19596354166666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5109380982272947,
              "expert_utilization": [
                313,
                353,
                509,
                665,
                219,
                411,
                280,
                322
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.21647135416666666,
              "operator_control_margin": 0.5109380982272947,
              "owner_churn": null,
              "owner_entropy": 2.0225663690926488,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0225663690926488,
              "prototype_margin": 0.5109380982272947,
              "prototype_monopoly_rate": 0.21647135416666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5111386253023132,
              "expert_utilization": [
                295,
                323,
                503,
                702,
                235,
                421,
                278,
                315
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.228515625,
              "operator_control_margin": 0.5111386253023132,
              "owner_churn": null,
              "owner_entropy": 2.01538760815178,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.01538760815178,
              "prototype_margin": 0.5111386253023132,
              "prototype_monopoly_rate": 0.228515625,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5051761796882298,
              "expert_utilization": [
                391,
                276,
                527,
                609,
                242,
                373,
                332,
                322
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.1982421875,
              "operator_control_margin": 0.5051761796882298,
              "owner_churn": null,
              "owner_entropy": 2.0351656708914323,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0351656708914323,
              "prototype_margin": 0.5051761796882298,
              "prototype_monopoly_rate": 0.1982421875,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 9.722999572753906,
              "mean_loss": 2.5450201097108676,
              "min_loss": 1.9412856101989746,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 9.722999572753906,
              "mean_loss": 2.5450201097108676,
              "min_loss": 1.9412856101989746,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 15.211018562316895,
              "mean_loss": 12.983597993850708,
              "min_loss": 12.034255027770996,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.97117406129837,
              "min_loss": 7.81622838973999,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "pvr_ean_retention_gated_delta_replay_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/checkpoint.pt",
          "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
          "key": "pvr_ean_retention_gated_delta_replay_300m_seed_0",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_v1_300m",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5183323635040628,
              "expert_utilization": [
                349,
                270,
                485,
                620,
                241,
                404,
                345,
                358
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20182291666666666,
              "operator_control_margin": 0.5183323635040628,
              "owner_churn": null,
              "owner_entropy": 2.037768461799472,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.037768461799472,
              "prototype_margin": 0.5183323635040628,
              "prototype_monopoly_rate": 0.20182291666666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5130888865387533,
              "expert_utilization": [
                302,
                329,
                512,
                701,
                223,
                409,
                272,
                324
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.22819010416666666,
              "operator_control_margin": 0.5130888865387533,
              "owner_churn": null,
              "owner_entropy": 2.013830819174193,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.013830819174193,
              "prototype_margin": 0.5130888865387533,
              "prototype_monopoly_rate": 0.22819010416666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5152230673314383,
              "expert_utilization": [
                288,
                296,
                501,
                728,
                238,
                427,
                277,
                317
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.23697916666666666,
              "operator_control_margin": 0.5152230673314383,
              "owner_churn": null,
              "owner_entropy": 2.0080757147085775,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0080757147085775,
              "prototype_margin": 0.5152230673314383,
              "prototype_monopoly_rate": 0.23697916666666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5068799492582912,
              "expert_utilization": [
                372,
                274,
                519,
                631,
                242,
                375,
                321,
                338
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20540364583333334,
              "operator_control_margin": 0.5068799492582912,
              "owner_churn": null,
              "owner_entropy": 2.0325072608582655,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0325072608582655,
              "prototype_margin": 0.5068799492582912,
              "prototype_monopoly_rate": 0.20540364583333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 9.481813430786133,
              "mean_loss": 2.518769474656529,
              "min_loss": 1.9557989835739136,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 14.813945770263672,
              "mean_loss": 11.644206404685974,
              "min_loss": 6.976099491119385,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 9.481813430786133,
              "mean_loss": 2.518769474656529,
              "min_loss": 1.9557989835739136,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 14.813945770263672,
              "mean_loss": 11.644206404685974,
              "min_loss": 6.976099491119385,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 13.323134422302246,
              "mean_loss": 10.820296287536621,
              "min_loss": 9.668989181518555,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 14.813945770263672,
              "mean_loss": 11.232251346111298,
              "min_loss": 6.976099491119385,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "switch_top1_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
          "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
          "key": "switch_top1_300m",
          "model_family": "vanilla_switch_top1_reference",
          "model_variant": "vanilla_switch_top1_reference_300m",
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 13.460567474365234,
              "mean_loss": 2.691827536649318,
              "min_loss": 2.069028377532959,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 13.460567474365234,
              "mean_loss": 2.691827536649318,
              "min_loss": 2.069028377532959,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 11.368138313293457,
              "mean_loss": 10.560967445373535,
              "min_loss": 10.17562198638916,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 15.58360767364502,
              "mean_loss": 11.743003726005554,
              "min_loss": 9.247726440429688,
              "window_count": 8
            }
          },
          "top1_invariants_clean": null
        }
      },
      "status": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT_SUPPORTED",
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
      }
    },
    {
      "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "rows": {
        "dense_300m": {
          "active_flops_estimate": 1800000000,
          "active_params_per_token": 300000000,
          "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
          "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
          "key": "dense_300m",
          "model_family": "dense_transformer",
          "model_variant": "dense_transformer_300m",
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.49954605102539,
              "mean_loss": 2.694834201048934,
              "min_loss": 2.0842881202697754,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.49954605102539,
              "mean_loss": 2.694834201048934,
              "min_loss": 2.0842881202697754,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 16.16033935546875,
              "mean_loss": 14.023216485977173,
              "min_loss": 13.100582122802734,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 19.473281860351562,
              "mean_loss": 14.586094975471497,
              "min_loss": 9.624191284179688,
              "window_count": 8
            }
          },
          "top1_invariants_clean": null
        },
        "pvr_baseline_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
          "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
          "key": "pvr_baseline_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.4764863158367613,
              "expert_utilization": [
                265,
                400,
                363,
                158,
                546,
                323,
                389,
                628
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20442708333333334,
              "operator_control_margin": 0.4764863158367613,
              "owner_churn": null,
              "owner_entropy": 2.0118771550900942,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0118771550900942,
              "prototype_margin": 0.4764863158367613,
              "prototype_monopoly_rate": 0.20442708333333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.47544338050526375,
              "expert_utilization": [
                275,
                389,
                362,
                135,
                547,
                393,
                398,
                573
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.1865234375,
              "operator_control_margin": 0.47544338050526375,
              "owner_churn": null,
              "owner_entropy": 2.015325695027265,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.015325695027265,
              "prototype_margin": 0.47544338050526375,
              "prototype_monopoly_rate": 0.1865234375,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.477010672443915,
              "expert_utilization": [
                288,
                399,
                363,
                149,
                571,
                374,
                388,
                540
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.18587239583333334,
              "operator_control_margin": 0.477010672443915,
              "owner_churn": null,
              "owner_entropy": 2.022228376128187,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.022228376128187,
              "prototype_margin": 0.477010672443915,
              "prototype_monopoly_rate": 0.18587239583333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.46924798957722186,
              "expert_utilization": [
                285,
                409,
                347,
                145,
                540,
                330,
                393,
                623
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.20279947916666666,
              "operator_control_margin": 0.46924798957722186,
              "owner_churn": null,
              "owner_entropy": 2.011370364940322,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.011370364940322,
              "prototype_margin": 0.46924798957722186,
              "prototype_monopoly_rate": 0.20279947916666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 13.596904754638672,
              "mean_loss": 2.7352521221636366,
              "min_loss": 2.1119062900543213,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 13.596904754638672,
              "mean_loss": 2.7352521221636366,
              "min_loss": 2.1119062900543213,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 11.232419967651367,
              "mean_loss": 10.401772260665894,
              "min_loss": 9.930900573730469,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.387349307537079,
              "min_loss": 7.083217144012451,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "pvr_ean_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
          "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
          "key": "pvr_ean_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5172737978258132,
              "expert_utilization": [
                360,
                274,
                487,
                602,
                243,
                406,
                348,
                352
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.19596354166666666,
              "operator_control_margin": 0.5172737978258132,
              "owner_churn": null,
              "owner_entropy": 2.0412845783848734,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0412845783848734,
              "prototype_margin": 0.5172737978258132,
              "prototype_monopoly_rate": 0.19596354166666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5109380982272947,
              "expert_utilization": [
                313,
                353,
                509,
                665,
                219,
                411,
                280,
                322
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.21647135416666666,
              "operator_control_margin": 0.5109380982272947,
              "owner_churn": null,
              "owner_entropy": 2.0225663690926488,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0225663690926488,
              "prototype_margin": 0.5109380982272947,
              "prototype_monopoly_rate": 0.21647135416666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5111386253023132,
              "expert_utilization": [
                295,
                323,
                503,
                702,
                235,
                421,
                278,
                315
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.228515625,
              "operator_control_margin": 0.5111386253023132,
              "owner_churn": null,
              "owner_entropy": 2.01538760815178,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.01538760815178,
              "prototype_margin": 0.5111386253023132,
              "prototype_monopoly_rate": 0.228515625,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5051761796882298,
              "expert_utilization": [
                391,
                276,
                527,
                609,
                242,
                373,
                332,
                322
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.1982421875,
              "operator_control_margin": 0.5051761796882298,
              "owner_churn": null,
              "owner_entropy": 2.0351656708914323,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0351656708914323,
              "prototype_margin": 0.5051761796882298,
              "prototype_monopoly_rate": 0.1982421875,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 9.722999572753906,
              "mean_loss": 2.5450201097108676,
              "min_loss": 1.9412856101989746,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 9.722999572753906,
              "mean_loss": 2.5450201097108676,
              "min_loss": 1.9412856101989746,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 15.211018562316895,
              "mean_loss": 12.983597993850708,
              "min_loss": 12.034255027770996,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.97117406129837,
              "min_loss": 7.81622838973999,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "pvr_ean_retention_gated_delta_replay_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_123/checkpoint.pt",
          "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
          "key": "pvr_ean_retention_gated_delta_replay_300m_seed_1",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_v1_300m",
          "routing_snapshots": [
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5208660841090023,
              "expert_utilization": [
                337,
                272,
                488,
                630,
                241,
                395,
                347,
                362
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.205078125,
              "operator_control_margin": 0.5208660841090023,
              "owner_churn": null,
              "owner_entropy": 2.0360052025813036,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0360052025813036,
              "prototype_margin": 0.5208660841090023,
              "prototype_monopoly_rate": 0.205078125,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 0,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.5166136846091831,
              "expert_utilization": [
                294,
                330,
                521,
                701,
                226,
                397,
                275,
                328
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.22819010416666666,
              "operator_control_margin": 0.5166136846091831,
              "owner_churn": null,
              "owner_entropy": 2.0136091734306634,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.0136091734306634,
              "prototype_margin": 0.5166136846091831,
              "prototype_monopoly_rate": 0.22819010416666666,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 25,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.518854224474732,
              "expert_utilization": [
                275,
                295,
                514,
                733,
                235,
                417,
                281,
                322
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.23860677083333334,
              "operator_control_margin": 0.518854224474732,
              "owner_churn": null,
              "owner_entropy": 2.004998433470856,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.004998433470856,
              "prototype_margin": 0.518854224474732,
              "prototype_monopoly_rate": 0.23860677083333334,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 50,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            },
            {
              "challenger_disagreement_rate": null,
              "descriptor_control_margin": 0.50918774640013,
              "expert_utilization": [
                365,
                276,
                523,
                639,
                241,
                367,
                320,
                341
              ],
              "failure_mode_distribution": {},
              "high_gap_monopoly_rate": 0.2080078125,
              "operator_control_margin": 0.50918774640013,
              "owner_churn": null,
              "owner_entropy": 2.030744339168701,
              "owners_per_token": 1.0,
              "production_map_mutated": false,
              "prototype_entropy": 2.030744339168701,
              "prototype_margin": 0.50918774640013,
              "prototype_monopoly_rate": 0.2080078125,
              "runtime_dynamic_k_count": 0,
              "runtime_expert_choice_count": 0,
              "stale_owner_rate": null,
              "step": 75,
              "top2_execution_count": 0,
              "top4_execution_count": 0
            }
          ],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 9.35163402557373,
              "mean_loss": 2.4956349462219736,
              "min_loss": 1.9244532585144043,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 14.284897804260254,
              "mean_loss": 11.195625305175781,
              "min_loss": 6.689387321472168,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 9.35163402557373,
              "mean_loss": 2.4956349462219736,
              "min_loss": 1.9244532585144043,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 14.284897804260254,
              "mean_loss": 11.195625305175781,
              "min_loss": 6.689387321472168,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 13.332083702087402,
              "mean_loss": 10.878432989120483,
              "min_loss": 9.792902946472168,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 14.284897804260254,
              "mean_loss": 11.037029147148132,
              "min_loss": 6.689387321472168,
              "window_count": 8
            }
          },
          "top1_invariants_clean": true
        },
        "switch_top1_300m": {
          "active_flops_estimate": 630000000,
          "active_params_per_token": 105000000,
          "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
          "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
          "key": "switch_top1_300m",
          "model_family": "vanilla_switch_top1_reference",
          "model_variant": "vanilla_switch_top1_reference_300m",
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 13.460567474365234,
              "mean_loss": 2.691827536649318,
              "min_loss": 2.069028377532959,
              "window_count": 3506
            },
            "code_heavy": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 13.460567474365234,
              "mean_loss": 2.691827536649318,
              "min_loss": 2.069028377532959,
              "window_count": 3506
            },
            "humaneval_like_heldout": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 11.368138313293457,
              "mean_loss": 10.560967445373535,
              "min_loss": 10.17562198638916,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 15.58360767364502,
              "mean_loss": 11.743003726005554,
              "min_loss": 9.247726440429688,
              "window_count": 8
            }
          },
          "top1_invariants_clean": null
        }
      },
      "status": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT_SUPPORTED",
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
      }
    }
  ],
  "created_at": "2026-06-17T20:10:00.993151+00:00",
  "device": "cuda",
  "experiment": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "reference_configs": {
    "dense_300m": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
    "pvr_baseline_300m": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
    "pvr_ean_300m": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
    "switch_top1_300m": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml"
  },
  "schema_version": "1.0",
  "seq_len": 128,
  "status": "PVR_EAN_RETENTION_GATED_DELTA_REPLAY_FULL_PROMOTION_AUDIT_SUPPORTED"
}
```
