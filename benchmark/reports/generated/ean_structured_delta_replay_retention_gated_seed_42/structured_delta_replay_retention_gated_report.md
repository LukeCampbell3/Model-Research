# EAN Structured Delta Replay Retention-Gated

Status: `PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED`
Candidate: `pvr_ec_o_ean_retention_gated_delta_replay_v1`
Best step: `100`

| model | broad LM | code-heavy | json/schema | unseen structured | Top1 clean |
|---|---:|---:|---:|---:|---|
| dense_300m | 2.776603478938341 | 15.14897346496582 | 14.023216485977173 | 14.586094975471497 | None |
| switch_top1_300m | 2.781601406633854 | 12.925040006637573 | 10.560967445373535 | 11.743003726005554 | None |
| pvr_baseline_300m | 2.824210923165083 | 10.372926354408264 | 10.401772260665894 | 10.387349307537079 | True |
| pvr_ean_300m | 2.595274433493614 | 12.958750128746033 | 12.983597993850708 | 12.97117406129837 | True |
| pvr_ean_retention_gated_delta_replay_300m | 2.571919046342373 | 11.644206404685974 | 10.820296287536621 | 11.232251346111298 | True |

```json
{
  "benchmark_evidence_caveat": "Reduced retention-gated repair audit only. It tests whether replay can recover structured residual skill without sacrificing broad/prose retention; it is not official benchmark promotion evidence.",
  "best_gate": {
    "accepted": true,
    "broad_delta_vs_ean": -0.023355387151241302,
    "broad_limit": 2.625274433493614,
    "broad_lm": 2.571919046342373,
    "reason": "retention_gate_passed",
    "step": 100,
    "structured_delta_vs_ean": -1.7389227151870728,
    "structured_unseen": 11.232251346111298
  },
  "best_step": 100,
  "broad_tolerance": 0.03,
  "candidate": "pvr_ec_o_ean_retention_gated_delta_replay_v1",
  "created_at": "2026-06-17T04:11:51.604400+00:00",
  "decision_rule": "Support requires structured heldout improvement versus EAN, broad/prose loss within EAN + tolerance, broad loss still beating dense/Switch/PVR baseline, and clean strict Top1 invariants.",
  "experiment": "PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED",
  "gate_curve": [
    {
      "accepted": true,
      "broad_delta_vs_ean": 0.010610491037368774,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.605884924530983,
      "step": 10,
      "structured_delta_vs_ean": -0.8168269395828247,
      "structured_unseen": 12.154347121715546
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.02459278702735901,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.570681646466255,
      "step": 20,
      "structured_delta_vs_ean": -1.143365204334259,
      "structured_unseen": 11.827808856964111
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.018382050096988678,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.5768923833966255,
      "step": 30,
      "structured_delta_vs_ean": -1.2706230878829956,
      "structured_unseen": 11.700550973415375
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": 0.0032692179083824158,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.5985436514019966,
      "step": 40,
      "structured_delta_vs_ean": -1.300184726715088,
      "structured_unseen": 11.670989334583282
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.007941212505102158,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.587333220988512,
      "step": 50,
      "structured_delta_vs_ean": -1.3612546920776367,
      "structured_unseen": 11.609919369220734
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.007302585989236832,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.5879718475043774,
      "step": 60,
      "structured_delta_vs_ean": -1.4109246134757996,
      "structured_unseen": 11.56024944782257
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.025155480951070786,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.5701189525425434,
      "step": 70,
      "structured_delta_vs_ean": -1.4599303603172302,
      "structured_unseen": 11.51124370098114
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.028540417551994324,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.56673401594162,
      "step": 80,
      "structured_delta_vs_ean": -1.5017138123512268,
      "structured_unseen": 11.469460248947144
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.020785152912139893,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.5744892805814743,
      "step": 90,
      "structured_delta_vs_ean": -1.633427381515503,
      "structured_unseen": 11.337746679782867
    },
    {
      "accepted": true,
      "broad_delta_vs_ean": -0.023355387151241302,
      "broad_limit": 2.625274433493614,
      "broad_lm": 2.571919046342373,
      "step": 100,
      "structured_delta_vs_ean": -1.7389227151870728,
      "structured_unseen": 11.232251346111298
    }
  ],
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "lrs": {
    "expert_lr": 1e-05,
    "router_lr": 0.0,
    "trunk_lr": 0.0
  },
  "max_steps": 100,
  "parameter_counts": {
    "expert_delta": 81632064,
    "frozen": 202928848,
    "router": 196608,
    "trunk": 0
  },
  "retention_paths": [
    "data/broad_nlp_train/gutenberg_alice_wonderland.txt",
    "data/broad_nlp_train/gutenberg_pride_and_prejudice.txt",
    "data/broad_nlp_train/gutenberg_sherlock_holmes.txt"
  ],
  "retention_weight": 2.0,
  "rows": {
    "dense_300m": {
      "active_flops_estimate": 1800000000,
      "active_params_per_token": 300000000,
      "checkpoint_path": "checkpoints/benchmark_300m/dense_transformer_300m/checkpoint.pt",
      "config_path": "benchmark/reports/generated/training_300m_real_4k/dense_transformer_300m/run_config.yaml",
      "model_family": "dense_transformer",
      "model_variant": "dense_transformer_300m",
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
      "top1_invariants_clean": null
    },
    "pvr_baseline_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/checkpoint.pt",
      "config_path": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/pvr_ec_o_full_300m_baseline_seed_42/run_config.yaml",
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
      "top1_invariants_clean": true
    },
    "pvr_ean_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/checkpoint.pt",
      "config_path": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42/run_config.yaml",
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
      "top1_invariants_clean": true
    },
    "pvr_ean_retention_gated_delta_replay_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/checkpoint.pt",
      "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
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
      "top1_invariants_clean": true
    },
    "switch_top1_300m": {
      "active_flops_estimate": 630000000,
      "active_params_per_token": 105000000,
      "checkpoint_path": "checkpoints/benchmark_300m/vanilla_switch_top1_reference_300m/checkpoint.pt",
      "config_path": "benchmark/reports/generated/training_300m_real_4k/vanilla_switch_top1_reference_300m/run_config.yaml",
      "model_family": "vanilla_switch_top1_reference",
      "model_variant": "vanilla_switch_top1_reference_300m",
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
      "top1_invariants_clean": null
    }
  },
  "schema_version": "1.0",
  "seed": 42,
  "seeded_replay_sampling": {
    "enabled": true,
    "offset_formula": "step_idx + seed * 1009 + stream * 1000003",
    "retention_stream": 1,
    "seed": 42,
    "structured_stream": 0
  },
  "status": "PVR_EAN_STRUCTURED_DELTA_REPLAY_RETENTION_GATED_SUPPORTED",
  "structured_replay_exclusion": {
    "heldout_spans": [
      {
        "end": 42990,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_0",
        "start": 42861
      },
      {
        "end": 85852,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_1",
        "start": 85723
      },
      {
        "end": 128714,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_2",
        "start": 128585
      },
      {
        "end": 171576,
        "family": "humaneval_like",
        "path": "data/eval/coding/humaneval_base.jsonl",
        "span_id": "humaneval_like_3",
        "start": 171447
      },
      {
        "end": 2784,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_0",
        "start": 2655
      },
      {
        "end": 5440,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_1",
        "start": 5311
      },
      {
        "end": 8096,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_2",
        "start": 7967
      },
      {
        "end": 10752,
        "family": "json_schema",
        "path": "data/eval/broad_nlp/json_schema_test_suite_type.txt",
        "span_id": "json_schema_3",
        "start": 10623
      }
    ],
    "structured_replay_byte_count_after_exclusion": 243422
  },
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
  "training_row": {
    "checkpoint_exists": true,
    "checkpoint_manifest": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/checkpoint_manifest.json",
    "checkpoint_path": "checkpoints/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/checkpoint.pt",
    "effective_batch_tokens": 512,
    "error": null,
    "eval_curve": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/eval_curve.json",
    "eval_window_count": 10,
    "final_loss": 11.55847454071045,
    "gpu_hours": 0.054601823687553404,
    "hardware_manifest": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/hardware_manifest.json",
    "model_variant": "pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42",
    "optimizer_steps": 100,
    "routing_curve": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/routing_curve.json",
    "routing_window_count": 10,
    "status": "GENUINE_REDUCED_TRAINING_COMPLETE",
    "throughput_log": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/throughput_log.json",
    "tokens_seen": 51200,
    "training_curve": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_seed_42/training_curve.json",
    "training_tokens_seen": 51200,
    "vram_peak": 4034086912
  }
}
```
