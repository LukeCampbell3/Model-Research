# Active Compute Frontier 300M Repeat

Status: `PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_REPEAT_SUPPORTED`
Missing seeds: `['777']`

| seed | status | broad LM | active params/token | active FLOPs/token | Top1 clean |
|---|---|---:|---:|---:|---|
| 42 | PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED | 2.571919046342373 | 105000000 | 630000000 | True |
| 123 | PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED | 2.5479386039078236 | 105000000 | 630000000 | True |
| 777 | NOT_RUN_MISSING_ARTIFACT | None | None | None | None |

```json
{
  "benchmark_evidence_caveat": "Local reduced-file repeat audit. Missing seeds are reported as missing artifacts, not inferred.",
  "broad_windows": 64,
  "candidate": "pvr_ean_retention_gated_delta_replay_v1_300m",
  "candidate_configs": [
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
    "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json"
  ],
  "created_at": "2026-06-18T13:18:50.369809+00:00",
  "decision_rule": "Repeat support requires at least the required number of completed candidate seeds, each completed seed to satisfy the single-run active-compute Pareto gate, and no Top1 invariant failure.",
  "device": "cuda",
  "expected_seeds": [
    "42",
    "123",
    "777"
  ],
  "experiment": "PVR_ACTIVE_COMPUTE_FRONTIER_300M_REPEAT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "missing_seeds": [
    "777"
  ],
  "reference_configs": {
    "dense_300m": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
    "generic_top2_300m": "benchmark/reports/generated/training_300m_real_4k/generic_top2_moe_reference_300m/run_config.yaml",
    "pvr_baseline_300m": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
    "pvr_ean_300m": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
    "switch_top1_300m": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml"
  },
  "repeat_results": [
    {
      "candidate_config": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "rows": {
        "dense_300m": {
          "active_flops_per_token": 1800000000,
          "active_params_per_token": 300000000,
          "broad_lm_loss": 2.776603478938341,
          "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
          "code_heavy_loss": 15.14897346496582,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
          "elapsed_seconds": 2.066941976547241,
          "gutenberg_prose_loss": 2.776603478938341,
          "json_schema_loss": 14.023216485977173,
          "key": "dense_300m",
          "model_family": "dense_transformer",
          "model_variant": "dense_transformer_300m",
          "perplexity": 16.06436538696289,
          "quality_per_active_flop": 2.000845852746598e-10,
          "quality_per_active_param": 1.2005075116479587e-09,
          "quality_per_ms": 3.3008784801955673,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 10.864638328552246,
              "mean_loss": 2.776603478938341,
              "min_loss": 2.2984459400177,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 10.864638328552246,
              "mean_loss": 2.776603478938341,
              "min_loss": 2.2984459400177,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 9165.230671663716,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 14.586094975471497,
          "vram_peak": 1053412864
        },
        "generic_top2_300m": {
          "active_flops_per_token": 900000000,
          "active_params_per_token": 150000000,
          "broad_lm_loss": 2.779079955071211,
          "checkpoint_path": "checkpoints/benchmark_300m/generic_top2_moe_reference_300m/checkpoint.pt",
          "code_heavy_loss": 14.226502180099487,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/generic_top2_moe_reference_300m/run_config.yaml",
          "elapsed_seconds": 15.839828252792358,
          "gutenberg_prose_loss": 2.779079955071211,
          "json_schema_loss": 12.023830652236938,
          "key": "generic_top2_300m",
          "model_family": "generic_top2_moe_reference",
          "model_variant": "generic_top2_moe_reference_300m",
          "perplexity": 16.104196548461914,
          "quality_per_active_flop": 3.998125743318674e-10,
          "quality_per_active_param": 2.398875445991204e-09,
          "quality_per_ms": 0.430348382478637,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.768226623535156,
              "mean_loss": 2.779079955071211,
              "min_loss": 2.3202052116394043,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 18.6014404296875,
              "mean_loss": 14.226502180099487,
              "min_loss": 8.91202163696289,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.768226623535156,
              "mean_loss": 2.779079955071211,
              "min_loss": 2.3202052116394043,
              "window_count": 64
            },
            "humaneval_like_heldout": {
              "max_loss": 18.6014404296875,
              "mean_loss": 14.226502180099487,
              "min_loss": 8.91202163696289,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 13.130805969238281,
              "mean_loss": 12.023830652236938,
              "min_loss": 11.496522903442383,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 18.6014404296875,
              "mean_loss": 13.125166416168213,
              "min_loss": 8.91202163696289,
              "window_count": 8
            }
          },
          "tokens_evaluated": 18944,
          "tokens_per_second": 1195.9725634436986,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 13.125166416168213,
          "vram_peak": 1100439040
        },
        "pvr_baseline_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.824210923165083,
          "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
          "code_heavy_loss": 10.372926354408264,
          "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
          "elapsed_seconds": 13.653971433639526,
          "gutenberg_prose_loss": 2.824210923165083,
          "json_schema_loss": 10.401772260665894,
          "key": "pvr_baseline_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
          "perplexity": 16.847644805908203,
          "quality_per_active_flop": 5.620336548810965e-10,
          "quality_per_active_param": 3.372201929286579e-09,
          "quality_per_ms": 0.49126470889316565,
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
              "max_loss": 12.159866333007812,
              "mean_loss": 2.824210923165083,
              "min_loss": 2.3216283321380615,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.159866333007812,
              "mean_loss": 2.824210923165083,
              "min_loss": 2.3216283321380615,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1387.4351570215929,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 10.387349307537079,
          "vram_peak": 1199062528
        },
        "pvr_ean_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.595274433493614,
          "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
          "code_heavy_loss": 12.958750128746033,
          "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
          "elapsed_seconds": 10.395873546600342,
          "gutenberg_prose_loss": 2.595274433493614,
          "json_schema_loss": 12.983597993850708,
          "key": "pvr_ean_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
          "perplexity": 13.400264739990234,
          "quality_per_active_flop": 6.116122313757972e-10,
          "quality_per_active_param": 3.669673388254783e-09,
          "quality_per_ms": 0.7021459714111674,
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
              "max_loss": 7.311913013458252,
              "mean_loss": 2.595274433493614,
              "min_loss": 2.263871908187866,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 7.311913013458252,
              "mean_loss": 2.595274433493614,
              "min_loss": 2.263871908187866,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1822.2614881839406,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 12.97117406129837,
          "vram_peak": 1199062528
        },
        "pvr_ean_retention_gated_delta_replay_v1_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.571919046342373,
          "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/checkpoint.pt",
          "code_heavy_loss": 11.644206404685974,
          "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
          "elapsed_seconds": 8.132604360580444,
          "gutenberg_prose_loss": 2.571919046342373,
          "json_schema_loss": 10.820296287536621,
          "key": "pvr_ean_retention_gated_delta_replay_v1_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_v1_300m",
          "perplexity": 13.090921401977539,
          "quality_per_active_flop": 6.171662321794114e-10,
          "quality_per_active_param": 3.7029973930764686e-09,
          "quality_per_ms": 0.9057007875876254,
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
              "max_loss": 6.863420009613037,
              "mean_loss": 2.571919046342373,
              "min_loss": 2.273947238922119,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 14.813945770263672,
              "mean_loss": 11.644206404685974,
              "min_loss": 6.976099491119385,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 6.863420009613037,
              "mean_loss": 2.571919046342373,
              "min_loss": 2.273947238922119,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 2329.3891058839017,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 11.232251346111298,
          "vram_peak": 1199062528
        },
        "switch_top1_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.781601406633854,
          "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
          "code_heavy_loss": 12.925040006637573,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
          "elapsed_seconds": 11.779411315917969,
          "gutenberg_prose_loss": 2.781601406633854,
          "json_schema_loss": 10.560967445373535,
          "key": "switch_top1_300m",
          "model_family": "vanilla_switch_top1_reference",
          "model_variant": "vanilla_switch_top1_reference_300m",
          "perplexity": 16.144855499267578,
          "quality_per_active_flop": 5.706430775868981e-10,
          "quality_per_active_param": 3.4238584655213888e-09,
          "quality_per_ms": 0.5781668682996631,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.778247833251953,
              "mean_loss": 2.781601406633854,
              "min_loss": 2.336674690246582,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.778247833251953,
              "mean_loss": 2.781601406633854,
              "min_loss": 2.336674690246582,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1608.229774131433,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 11.743003726005554,
          "vram_peak": 1100439040
        }
      },
      "seed": "42",
      "status": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED",
      "supported_conditions": {
        "candidate_beats_dense_loss": true,
        "candidate_beats_switch_loss": true,
        "candidate_beats_top2_loss": true,
        "candidate_pareto_efficient_active_flops": true,
        "candidate_pareto_efficient_active_params": true,
        "candidate_top1_clean": true
      }
    },
    {
      "candidate_config": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "rows": {
        "dense_300m": {
          "active_flops_per_token": 1800000000,
          "active_params_per_token": 300000000,
          "broad_lm_loss": 2.776603478938341,
          "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
          "code_heavy_loss": 15.14897346496582,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
          "elapsed_seconds": 2.066941976547241,
          "gutenberg_prose_loss": 2.776603478938341,
          "json_schema_loss": 14.023216485977173,
          "key": "dense_300m",
          "model_family": "dense_transformer",
          "model_variant": "dense_transformer_300m",
          "perplexity": 16.06436538696289,
          "quality_per_active_flop": 2.000845852746598e-10,
          "quality_per_active_param": 1.2005075116479587e-09,
          "quality_per_ms": 3.3008784801955673,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 10.864638328552246,
              "mean_loss": 2.776603478938341,
              "min_loss": 2.2984459400177,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 19.473281860351562,
              "mean_loss": 15.14897346496582,
              "min_loss": 9.624191284179688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 10.864638328552246,
              "mean_loss": 2.776603478938341,
              "min_loss": 2.2984459400177,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 9165.230671663716,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 14.586094975471497,
          "vram_peak": 1053412864
        },
        "generic_top2_300m": {
          "active_flops_per_token": 900000000,
          "active_params_per_token": 150000000,
          "broad_lm_loss": 2.779079955071211,
          "checkpoint_path": "checkpoints/benchmark_300m/generic_top2_moe_reference_300m/checkpoint.pt",
          "code_heavy_loss": 14.226502180099487,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/generic_top2_moe_reference_300m/run_config.yaml",
          "elapsed_seconds": 15.839828252792358,
          "gutenberg_prose_loss": 2.779079955071211,
          "json_schema_loss": 12.023830652236938,
          "key": "generic_top2_300m",
          "model_family": "generic_top2_moe_reference",
          "model_variant": "generic_top2_moe_reference_300m",
          "perplexity": 16.104196548461914,
          "quality_per_active_flop": 3.998125743318674e-10,
          "quality_per_active_param": 2.398875445991204e-09,
          "quality_per_ms": 0.430348382478637,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.768226623535156,
              "mean_loss": 2.779079955071211,
              "min_loss": 2.3202052116394043,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 18.6014404296875,
              "mean_loss": 14.226502180099487,
              "min_loss": 8.91202163696289,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.768226623535156,
              "mean_loss": 2.779079955071211,
              "min_loss": 2.3202052116394043,
              "window_count": 64
            },
            "humaneval_like_heldout": {
              "max_loss": 18.6014404296875,
              "mean_loss": 14.226502180099487,
              "min_loss": 8.91202163696289,
              "window_count": 4
            },
            "json_schema": {
              "max_loss": 13.130805969238281,
              "mean_loss": 12.023830652236938,
              "min_loss": 11.496522903442383,
              "window_count": 4
            },
            "unseen_structured_spans": {
              "max_loss": 18.6014404296875,
              "mean_loss": 13.125166416168213,
              "min_loss": 8.91202163696289,
              "window_count": 8
            }
          },
          "tokens_evaluated": 18944,
          "tokens_per_second": 1195.9725634436986,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 13.125166416168213,
          "vram_peak": 1100439040
        },
        "pvr_baseline_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.824210923165083,
          "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
          "code_heavy_loss": 10.372926354408264,
          "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
          "elapsed_seconds": 13.653971433639526,
          "gutenberg_prose_loss": 2.824210923165083,
          "json_schema_loss": 10.401772260665894,
          "key": "pvr_baseline_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_baseline_seed_42",
          "perplexity": 16.847644805908203,
          "quality_per_active_flop": 5.620336548810965e-10,
          "quality_per_active_param": 3.372201929286579e-09,
          "quality_per_ms": 0.49126470889316565,
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
              "max_loss": 12.159866333007812,
              "mean_loss": 2.824210923165083,
              "min_loss": 2.3216283321380615,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 13.306273460388184,
              "mean_loss": 10.372926354408264,
              "min_loss": 7.083217144012451,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.159866333007812,
              "mean_loss": 2.824210923165083,
              "min_loss": 2.3216283321380615,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1387.4351570215929,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 10.387349307537079,
          "vram_peak": 1199062528
        },
        "pvr_ean_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.595274433493614,
          "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
          "code_heavy_loss": 12.958750128746033,
          "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
          "elapsed_seconds": 10.395873546600342,
          "gutenberg_prose_loss": 2.595274433493614,
          "json_schema_loss": 12.983597993850708,
          "key": "pvr_ean_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42",
          "perplexity": 13.400264739990234,
          "quality_per_active_flop": 6.116122313757972e-10,
          "quality_per_active_param": 3.669673388254783e-09,
          "quality_per_ms": 0.7021459714111674,
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
              "max_loss": 7.311913013458252,
              "mean_loss": 2.595274433493614,
              "min_loss": 2.263871908187866,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 16.904939651489258,
              "mean_loss": 12.958750128746033,
              "min_loss": 7.81622838973999,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 7.311913013458252,
              "mean_loss": 2.595274433493614,
              "min_loss": 2.263871908187866,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1822.2614881839406,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 12.97117406129837,
          "vram_peak": 1199062528
        },
        "pvr_ean_retention_gated_delta_replay_v1_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.5479386039078236,
          "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_123/checkpoint.pt",
          "code_heavy_loss": 11.195625305175781,
          "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
          "elapsed_seconds": 8.240744352340698,
          "gutenberg_prose_loss": 2.5479386039078236,
          "json_schema_loss": 10.878432989120483,
          "key": "pvr_ean_retention_gated_delta_replay_v1_300m",
          "model_family": "pvr_ec_o",
          "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_v1_300m",
          "perplexity": 12.780730247497559,
          "quality_per_active_flop": 6.229748177083669e-10,
          "quality_per_active_param": 3.7378489062502015e-09,
          "quality_per_ms": 0.9022279661288798,
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
              "max_loss": 6.890679359436035,
              "mean_loss": 2.5479386039078236,
              "min_loss": 2.26733136177063,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 14.284897804260254,
              "mean_loss": 11.195625305175781,
              "min_loss": 6.689387321472168,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 6.890679359436035,
              "mean_loss": 2.5479386039078236,
              "min_loss": 2.26733136177063,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 2298.821464425013,
          "top1_invariants_clean": true,
          "total_params": 300000000,
          "unseen_structured_loss": 11.037029147148132,
          "vram_peak": 1199062528
        },
        "switch_top1_300m": {
          "active_flops_per_token": 630000000,
          "active_params_per_token": 105000000,
          "broad_lm_loss": 2.781601406633854,
          "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
          "code_heavy_loss": 12.925040006637573,
          "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
          "elapsed_seconds": 11.779411315917969,
          "gutenberg_prose_loss": 2.781601406633854,
          "json_schema_loss": 10.560967445373535,
          "key": "switch_top1_300m",
          "model_family": "vanilla_switch_top1_reference",
          "model_variant": "vanilla_switch_top1_reference_300m",
          "perplexity": 16.144855499267578,
          "quality_per_active_flop": 5.706430775868981e-10,
          "quality_per_active_param": 3.4238584655213888e-09,
          "quality_per_ms": 0.5781668682996631,
          "routing_snapshots": [],
          "slice_summary": {
            "broad_lm": {
              "max_loss": 12.778247833251953,
              "mean_loss": 2.781601406633854,
              "min_loss": 2.336674690246582,
              "window_count": 64
            },
            "code_heavy": {
              "max_loss": 15.58360767364502,
              "mean_loss": 12.925040006637573,
              "min_loss": 9.247726440429688,
              "window_count": 4
            },
            "gutenberg_prose": {
              "max_loss": 12.778247833251953,
              "mean_loss": 2.781601406633854,
              "min_loss": 2.336674690246582,
              "window_count": 64
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
          "tokens_evaluated": 18944,
          "tokens_per_second": 1608.229774131433,
          "top1_invariants_clean": null,
          "total_params": 300000000,
          "unseen_structured_loss": 11.743003726005554,
          "vram_peak": 1100439040
        }
      },
      "seed": "123",
      "status": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED",
      "supported_conditions": {
        "candidate_beats_dense_loss": true,
        "candidate_beats_switch_loss": true,
        "candidate_beats_top2_loss": true,
        "candidate_pareto_efficient_active_flops": true,
        "candidate_pareto_efficient_active_params": true,
        "candidate_top1_clean": true
      }
    },
    {
      "candidate_config": null,
      "rows": {},
      "seed": "777",
      "status": "NOT_RUN_MISSING_ARTIFACT",
      "supported_conditions": {}
    }
  ],
  "required_repeats": 2,
  "schema_version": "1.0",
  "seq_len": 128,
  "status": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_REPEAT_SUPPORTED",
  "supported_conditions": {
    "all_completed_repeats_supported": true,
    "minimum_repeat_count_met": true,
    "no_completed_repeat_invariant_failed": true
  }
}
```
