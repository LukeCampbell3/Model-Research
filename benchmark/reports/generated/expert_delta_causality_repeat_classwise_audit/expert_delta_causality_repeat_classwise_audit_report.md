# Expert Delta Causality Repeat and Classwise Audit

Status: `PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED`
Missing seeds: `['777']`

| seed | status | full-shared benefit | wrong-expert harm | structured harm | wrong worse rate |
|---|---|---:|---:|---:|---:|
| 42 | PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED | 1.289743077333504 | 1.2417185518132754 | 2.017081891326066 | 0.7513020833333334 |
| 123 | PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED | 1.463166709370757 | 1.3812738008129095 | 2.2558057758002534 | 0.7322591145833334 |
| 777 | NOT_RUN_MISSING_ARTIFACT | None | None | None | None |

```json
{
  "benchmark_evidence_caveat": "Local reduced-file repeat/classwise causality audit; seed 777 is reported missing if no artifact exists.",
  "created_at": "2026-06-18T16:12:51.815302+00:00",
  "decision_rule": "Support requires the expert-delta causality proof to pass for every completed seed, at least the required number of completed seeds, clean Top1 invariants, and classwise causality across most structured token classes.",
  "device": "cuda",
  "expected_seeds": [
    "42",
    "123",
    "777"
  ],
  "experiment": "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_AND_CLASSWISE_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "missing_seeds": [
    "777"
  ],
  "required_repeats": 2,
  "schema_version": "1.0",
  "seed_results": [
    {
      "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "metrics": {
        "causal": {
          "high_benefit_wrong_expert_harm": 2.0742133428091125,
          "mean_full_vs_shared_benefit": 1.289743077333504,
          "mean_wrong_expert_harm": 1.2417185518132754,
          "structured_full_vs_shared_benefit": 2.404115576166546,
          "structured_wrong_expert_harm": 2.017081891326066,
          "structured_wrong_expert_worse_than_full_rate": 0.8435430463576159,
          "wrong_expert_worse_than_full_rate": 0.7513020833333334
        },
        "classwise": {
          "brace_bracket_paren": {
            "count": 122,
            "full_vs_shared_benefit": 4.415328039558696,
            "wrong_expert_harm": 4.031733043858262,
            "wrong_expert_worse_than_full_rate": 0.9672131147540983
          },
          "comma_colon_semicolon": {
            "count": 173,
            "full_vs_shared_benefit": 2.2773670729874187,
            "wrong_expert_harm": 2.4735121141279364,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "function_signature": {
            "count": 115,
            "full_vs_shared_benefit": 2.747845725391222,
            "wrong_expert_harm": 2.3667118829229605,
            "wrong_expert_worse_than_full_rate": 0.8782608695652174
          },
          "identifier": {
            "count": 1095,
            "full_vs_shared_benefit": 1.2172723113946173,
            "wrong_expert_harm": 1.058485042991023,
            "wrong_expert_worse_than_full_rate": 0.7844748858447489
          },
          "indentation": {
            "count": 909,
            "full_vs_shared_benefit": -0.2915292372281599,
            "wrong_expert_harm": 0.24394568038245765,
            "wrong_expert_worse_than_full_rate": 0.7887788778877888
          },
          "json_key": {
            "count": 217,
            "full_vs_shared_benefit": 1.8746470358514566,
            "wrong_expert_harm": 1.509096859786917,
            "wrong_expert_worse_than_full_rate": 0.8755760368663594
          },
          "json_value": {
            "count": 214,
            "full_vs_shared_benefit": 1.2543968973141686,
            "wrong_expert_harm": 1.036916845208295,
            "wrong_expert_worse_than_full_rate": 0.7663551401869159
          },
          "newline": {
            "count": 137,
            "full_vs_shared_benefit": 4.506152820477475,
            "wrong_expert_harm": 2.769893382519356,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "number": {
            "count": 71,
            "full_vs_shared_benefit": 3.237140588357415,
            "wrong_expert_harm": 2.668139121901821,
            "wrong_expert_worse_than_full_rate": 0.9295774647887324
          },
          "operator": {
            "count": 45,
            "full_vs_shared_benefit": 4.307893371582031,
            "wrong_expert_harm": 3.492708863152398,
            "wrong_expert_worse_than_full_rate": 0.9333333333333333
          },
          "other": {
            "count": 122,
            "full_vs_shared_benefit": 5.2361088570029155,
            "wrong_expert_harm": 4.332579488997833,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "prose_word": {
            "count": 1596,
            "full_vs_shared_benefit": 1.1481621274234433,
            "wrong_expert_harm": 1.0535751502788193,
            "wrong_expert_worse_than_full_rate": 0.7763157894736842
          },
          "quote": {
            "count": 204,
            "full_vs_shared_benefit": 7.4690834307203104,
            "wrong_expert_harm": 6.667674139434216,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "space": {
            "count": 928,
            "full_vs_shared_benefit": -0.5220024006356935,
            "wrong_expert_harm": -0.11195681445854555,
            "wrong_expert_worse_than_full_rate": 0.35237068965517243
          },
          "string_literal": {
            "count": 196,
            "full_vs_shared_benefit": 1.942807598077521,
            "wrong_expert_harm": 1.6046964881979688,
            "wrong_expert_worse_than_full_rate": 0.8010204081632653
          }
        },
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
        "top1_invariants_clean": true
      },
      "seed": "42",
      "status": "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
      "supported_conditions": {
        "full_beats_shared": true,
        "most_structured_classes_causal": true,
        "space_indentation_not_primary_causal_claim": true,
        "structured_class_coverage": true,
        "structured_full_beats_shared": true,
        "structured_wrong_expert_harms": true,
        "top1_invariants_clean": true,
        "wrong_expert_harms": true,
        "wrong_expert_worse_rate_high": true
      }
    },
    {
      "config_path": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_123/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
      "metrics": {
        "causal": {
          "high_benefit_wrong_expert_harm": 2.3457036181963073,
          "mean_full_vs_shared_benefit": 1.463166709370757,
          "mean_wrong_expert_harm": 1.3812738008129095,
          "structured_full_vs_shared_benefit": 2.6533614143299236,
          "structured_wrong_expert_harm": 2.2558057758002534,
          "structured_wrong_expert_worse_than_full_rate": 0.8642384105960265,
          "wrong_expert_worse_than_full_rate": 0.7322591145833334
        },
        "classwise": {
          "brace_bracket_paren": {
            "count": 122,
            "full_vs_shared_benefit": 4.628513504613618,
            "wrong_expert_harm": 4.179983042058398,
            "wrong_expert_worse_than_full_rate": 0.9754098360655737
          },
          "comma_colon_semicolon": {
            "count": 173,
            "full_vs_shared_benefit": 1.8649700418373063,
            "wrong_expert_harm": 2.0458040182301076,
            "wrong_expert_worse_than_full_rate": 0.9942196531791907
          },
          "function_signature": {
            "count": 115,
            "full_vs_shared_benefit": 3.5214036786037943,
            "wrong_expert_harm": 3.0740668379742164,
            "wrong_expert_worse_than_full_rate": 0.9304347826086956
          },
          "identifier": {
            "count": 1095,
            "full_vs_shared_benefit": 1.257006938408499,
            "wrong_expert_harm": 1.118535072339452,
            "wrong_expert_worse_than_full_rate": 0.8082191780821918
          },
          "indentation": {
            "count": 909,
            "full_vs_shared_benefit": -0.4063836032539049,
            "wrong_expert_harm": 0.04154224093794429,
            "wrong_expert_worse_than_full_rate": 0.5973597359735974
          },
          "json_key": {
            "count": 217,
            "full_vs_shared_benefit": 1.7967489251892688,
            "wrong_expert_harm": 1.4000689488951512,
            "wrong_expert_worse_than_full_rate": 0.8940092165898618
          },
          "json_value": {
            "count": 214,
            "full_vs_shared_benefit": 1.3015370157103394,
            "wrong_expert_harm": 1.109584384084305,
            "wrong_expert_worse_than_full_rate": 0.8037383177570093
          },
          "newline": {
            "count": 137,
            "full_vs_shared_benefit": 3.348206437099442,
            "wrong_expert_harm": 1.8208586028046854,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "number": {
            "count": 71,
            "full_vs_shared_benefit": 4.0332116610567335,
            "wrong_expert_harm": 3.3405908732347087,
            "wrong_expert_worse_than_full_rate": 0.9295774647887324
          },
          "operator": {
            "count": 45,
            "full_vs_shared_benefit": 4.283075502183702,
            "wrong_expert_harm": 3.488100443945991,
            "wrong_expert_worse_than_full_rate": 0.9111111111111111
          },
          "other": {
            "count": 122,
            "full_vs_shared_benefit": 10.027226511298247,
            "wrong_expert_harm": 8.511552475760075,
            "wrong_expert_worse_than_full_rate": 0.9918032786885246
          },
          "prose_word": {
            "count": 1596,
            "full_vs_shared_benefit": 1.1817596956812089,
            "wrong_expert_harm": 1.136382961772933,
            "wrong_expert_worse_than_full_rate": 0.8013784461152882
          },
          "quote": {
            "count": 204,
            "full_vs_shared_benefit": 9.358716553332759,
            "wrong_expert_harm": 8.369879853491689,
            "wrong_expert_worse_than_full_rate": 1.0
          },
          "space": {
            "count": 928,
            "full_vs_shared_benefit": -0.5209829151000153,
            "wrong_expert_harm": -0.22332233118278713,
            "wrong_expert_worse_than_full_rate": 0.31896551724137934
          },
          "string_literal": {
            "count": 196,
            "full_vs_shared_benefit": 2.8013070736612593,
            "wrong_expert_harm": 2.395049091048387,
            "wrong_expert_worse_than_full_rate": 0.8316326530612245
          }
        },
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
        "top1_invariants_clean": true
      },
      "seed": "123",
      "status": "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
      "supported_conditions": {
        "full_beats_shared": true,
        "most_structured_classes_causal": true,
        "space_indentation_not_primary_causal_claim": true,
        "structured_class_coverage": true,
        "structured_full_beats_shared": true,
        "structured_wrong_expert_harms": true,
        "top1_invariants_clean": true,
        "wrong_expert_harms": true,
        "wrong_expert_worse_rate_high": true
      }
    },
    {
      "config_path": null,
      "metrics": {},
      "seed": "777",
      "status": "NOT_RUN_MISSING_ARTIFACT",
      "supported_conditions": {}
    }
  ],
  "seq_len": 128,
  "spans_per_family": 16,
  "status": "PVR_EXPERT_DELTA_CAUSALITY_REPEAT_SUPPORTED",
  "supported_conditions": {
    "all_completed_seeds_supported": true,
    "minimum_repeat_count_met": true,
    "no_invariant_failure": true
  }
}
```
