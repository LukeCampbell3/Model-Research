# Benefit-Weighted Route Geometry Induction Audit

Status: `PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_NOT_SUPPORTED`

| metric | before | after | delta |
|---|---:|---:|---:|
| benefit_weighted_owner_token_class_nmi | 0.03838016134068867 | 0.02955430443592247 | -0.008825856904766196 |
| high_benefit_token_owner_consistency | 0.5887289083448888 | 0.529842364305384 | -0.05888654403950477 |
| structured_mean_expert_benefit | 2.186260147786843 | 2.2429832111472794 | 0.05672306336043631 |
| broad_stability_mean_expert_benefit | 0.32475940225576966 | 0.1343260565888787 | -0.19043334566689096 |
| broad_lm | 2.571919046342373 | 2.562825072556734 | -0.00909397378563881 |

```json
{
  "adapted_config": "benchmark/reports/generated/benefit_weighted_route_geometry_induction_audit/pvr_benefit_weighted_route_geometry_induction_config.json",
  "benchmark_evidence_caveat": "Diagnostic router-only induction branch over local reduced files; not an official promoted candidate.",
  "candidate_config": "benchmark/reports/generated/ean_structured_delta_replay_retention_gated_seed_42/pvr_ec_o_ean_retention_gated_delta_replay_v1_300m_config.json",
  "checkpoint_path": "checkpoints/benefit_weighted_route_geometry_induction_audit/pvr_benefit_weighted_route_geometry_induction/checkpoint.pt",
  "created_at": "2026-06-18T14:28:19.862261+00:00",
  "decision_rule": "Support requires benefit-weighted owner/token-class NMI and high-benefit consistency to improve, structured benefit and broad stability to be preserved, broad LM to remain within tolerance, Top1 to remain clean, and active-compute Pareto status to survive.",
  "device": "cuda",
  "experiment": "PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_AUDIT",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "lr": 1e-05,
  "metrics": {
    "after": {
      "benefit_weighted_owner_token_class_nmi": 0.02955430443592247,
      "broad_stability_mean_expert_benefit": 0.1343260565888787,
      "high_benefit_token_owner_consistency": 0.529842364305384,
      "mean_expert_benefit": 1.140916328524057,
      "owner_token_class_nmi": 0.03220487378044937,
      "positive_benefit_rate": 0.6427951388888888,
      "structured_mean_expert_benefit": 2.2429832111472794
    },
    "before": {
      "benefit_weighted_owner_token_class_nmi": 0.03838016134068867,
      "broad_stability_mean_expert_benefit": 0.32475940225576966,
      "high_benefit_token_owner_consistency": 0.5887289083448888,
      "mean_expert_benefit": 1.2218325913220633,
      "owner_token_class_nmi": 0.04417959406761065,
      "positive_benefit_rate": 0.6527777777777778,
      "structured_mean_expert_benefit": 2.186260147786843
    },
    "broad_lm_after": 2.562825072556734,
    "broad_lm_before": 2.571919046342373,
    "broad_lm_delta": -0.00909397378563881,
    "deltas": {
      "benefit_weighted_owner_token_class_nmi": -0.008825856904766196,
      "broad_stability_mean_expert_benefit": -0.19043334566689096,
      "high_benefit_token_owner_consistency": -0.05888654403950477,
      "structured_mean_expert_benefit": 0.05672306336043631
    },
    "frontier_conditions": {
      "candidate_beats_dense_loss": true,
      "candidate_beats_switch_loss": true,
      "candidate_beats_top2_loss": true,
      "candidate_pareto_efficient_active_flops": true,
      "candidate_pareto_efficient_active_params": true,
      "candidate_top1_clean": true
    },
    "frontier_status": "PVR_ACTIVE_COMPUTE_PARETO_ADVANTAGE_SUPPORTED",
    "routing_snapshots": [
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 1.1789206774168026,
        "expert_utilization": [
          296,
          273,
          556,
          633,
          261,
          382,
          348,
          323
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.2060546875,
        "operator_control_margin": 1.1789206774168026,
        "owner_churn": null,
        "owner_entropy": 2.027653817722194,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.027653817722194,
        "prototype_margin": 1.1789206774168026,
        "prototype_monopoly_rate": 0.2060546875,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 0,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 1.1959064762825922,
        "expert_utilization": [
          285,
          307,
          567,
          669,
          234,
          366,
          332,
          312
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.2177734375,
        "operator_control_margin": 1.1959064762825922,
        "owner_churn": null,
        "owner_entropy": 2.0169051614483275,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.0169051614483275,
        "prototype_margin": 1.1959064762825922,
        "prototype_monopoly_rate": 0.2177734375,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 25,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 1.18974146686863,
        "expert_utilization": [
          276,
          294,
          585,
          679,
          236,
          359,
          339,
          304
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.22102864583333334,
        "operator_control_margin": 1.18974146686863,
        "owner_churn": null,
        "owner_entropy": 2.010661806552297,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.010661806552297,
        "prototype_margin": 1.18974146686863,
        "prototype_monopoly_rate": 0.22102864583333334,
        "runtime_dynamic_k_count": 0,
        "runtime_expert_choice_count": 0,
        "stale_owner_rate": null,
        "step": 50,
        "top2_execution_count": 0,
        "top4_execution_count": 0
      },
      {
        "challenger_disagreement_rate": null,
        "descriptor_control_margin": 1.1814832126668382,
        "expert_utilization": [
          320,
          290,
          586,
          622,
          264,
          338,
          336,
          316
        ],
        "failure_mode_distribution": {},
        "high_gap_monopoly_rate": 0.20247395833333334,
        "operator_control_margin": 1.1814832126668382,
        "owner_churn": null,
        "owner_entropy": 2.0275494960126,
        "owners_per_token": 1.0,
        "production_map_mutated": false,
        "prototype_entropy": 2.0275494960126,
        "prototype_margin": 1.1814832126668382,
        "prototype_monopoly_rate": 0.20247395833333334,
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
  "router_geometry_targets": {
    "0": {
      "brace_bracket_paren": 1,
      "function_signature": 0,
      "identifier": 0,
      "json_key": 4,
      "newline": 1,
      "number": 0,
      "operator": 2,
      "quote": 0
    },
    "1": {
      "brace_bracket_paren": 5,
      "function_signature": 0,
      "identifier": 6,
      "json_key": 0,
      "newline": 6,
      "number": 4,
      "operator": 4,
      "quote": 4
    },
    "2": {
      "brace_bracket_paren": 7,
      "function_signature": 6,
      "identifier": 2,
      "json_key": 4,
      "newline": 5,
      "number": 7,
      "operator": 7,
      "quote": 2
    },
    "3": {
      "brace_bracket_paren": 5,
      "function_signature": 1,
      "identifier": 0,
      "json_key": 5,
      "newline": 4,
      "number": 0,
      "operator": 5,
      "quote": 0
    },
    "4": {
      "brace_bracket_paren": 0,
      "function_signature": 0,
      "identifier": 0,
      "json_key": 0,
      "newline": 5,
      "number": 6,
      "operator": 3,
      "quote": 1
    },
    "5": {
      "brace_bracket_paren": 3,
      "function_signature": 0,
      "identifier": 3,
      "json_key": 3,
      "newline": 3,
      "number": 3,
      "operator": 3,
      "quote": 3
    },
    "6": {
      "brace_bracket_paren": 1,
      "function_signature": 4,
      "identifier": 1,
      "json_key": 1,
      "newline": 4,
      "number": 1,
      "operator": 1,
      "quote": 1
    },
    "7": {
      "brace_bracket_paren": 2,
      "function_signature": 2,
      "identifier": 2,
      "json_key": 2,
      "newline": 2,
      "number": 2,
      "operator": 2,
      "quote": 2
    },
    "8": {
      "brace_bracket_paren": 5,
      "function_signature": 5,
      "identifier": 5,
      "json_key": 5,
      "newline": 5,
      "number": 5,
      "operator": 5,
      "quote": 5
    },
    "9": {
      "brace_bracket_paren": 2,
      "function_signature": 2,
      "identifier": 2,
      "json_key": 2,
      "newline": 2,
      "number": 2,
      "operator": 2,
      "quote": 2
    },
    "10": {
      "brace_bracket_paren": 6,
      "function_signature": 6,
      "identifier": 6,
      "json_key": 6,
      "newline": 6,
      "number": 3,
      "operator": 6,
      "quote": 3
    },
    "11": {
      "brace_bracket_paren": 7,
      "function_signature": 7,
      "identifier": 7,
      "json_key": 7,
      "newline": 7,
      "number": 7,
      "operator": 7,
      "quote": 7
    },
    "12": {
      "brace_bracket_paren": 0,
      "function_signature": 0,
      "identifier": 0,
      "json_key": 0,
      "newline": 0,
      "number": 0,
      "operator": 0,
      "quote": 0
    },
    "13": {
      "brace_bracket_paren": 2,
      "function_signature": 2,
      "identifier": 2,
      "json_key": 2,
      "newline": 2,
      "number": 2,
      "operator": 2,
      "quote": 2
    },
    "14": {
      "brace_bracket_paren": 4,
      "function_signature": 4,
      "identifier": 4,
      "json_key": 4,
      "newline": 4,
      "number": 4,
      "operator": 4,
      "quote": 4
    },
    "15": {
      "brace_bracket_paren": 3,
      "function_signature": 3,
      "identifier": 3,
      "json_key": 3,
      "newline": 3,
      "number": 3,
      "operator": 3,
      "quote": 3
    },
    "16": {
      "brace_bracket_paren": 3,
      "function_signature": 0,
      "identifier": 3,
      "json_key": 3,
      "newline": 3,
      "number": 3,
      "operator": 3,
      "quote": 3
    },
    "17": {
      "brace_bracket_paren": 5,
      "function_signature": 5,
      "identifier": 5,
      "json_key": 5,
      "newline": 5,
      "number": 5,
      "operator": 5,
      "quote": 5
    },
    "18": {
      "brace_bracket_paren": 2,
      "function_signature": 2,
      "identifier": 2,
      "json_key": 2,
      "newline": 2,
      "number": 2,
      "operator": 2,
      "quote": 2
    },
    "19": {
      "brace_bracket_paren": 1,
      "function_signature": 1,
      "identifier": 1,
      "json_key": 1,
      "newline": 1,
      "number": 1,
      "operator": 1,
      "quote": 1
    },
    "20": {
      "brace_bracket_paren": 3,
      "function_signature": 3,
      "identifier": 3,
      "json_key": 3,
      "newline": 3,
      "number": 3,
      "operator": 3,
      "quote": 3
    },
    "21": {
      "brace_bracket_paren": 3,
      "function_signature": 3,
      "identifier": 3,
      "json_key": 3,
      "newline": 3,
      "number": 3,
      "operator": 3,
      "quote": 3
    },
    "22": {
      "brace_bracket_paren": 7,
      "function_signature": 7,
      "identifier": 7,
      "json_key": 7,
      "newline": 7,
      "number": 7,
      "operator": 7,
      "quote": 7
    },
    "23": {
      "brace_bracket_paren": 6,
      "function_signature": 6,
      "identifier": 6,
      "json_key": 6,
      "newline": 6,
      "number": 6,
      "operator": 6,
      "quote": 6
    }
  },
  "schema_version": "1.0",
  "seq_len": 128,
  "spans_per_family": 12,
  "status": "PVR_BENEFIT_WEIGHTED_ROUTE_GEOMETRY_INDUCTION_NOT_SUPPORTED",
  "steps": 50,
  "supported_conditions": {
    "active_compute_pareto_survives": true,
    "benefit_weighted_nmi_improves": false,
    "broad_lm_within_tolerance": true,
    "broad_stability_preserved": false,
    "high_benefit_consistency_improves": false,
    "structured_benefit_preserved": true,
    "top1_invariants_clean": true
  },
  "target_classes": [
    "brace_bracket_paren",
    "function_signature",
    "identifier",
    "json_key",
    "newline",
    "number",
    "operator",
    "quote"
  ],
  "training_curve": [
    {
      "route_geometry_loss": 1.4136943817138672,
      "step": 1
    },
    {
      "route_geometry_loss": 1.3219566345214844,
      "step": 2
    },
    {
      "route_geometry_loss": 1.3758158683776855,
      "step": 3
    },
    {
      "route_geometry_loss": 1.317931056022644,
      "step": 4
    },
    {
      "route_geometry_loss": 1.3383640050888062,
      "step": 5
    },
    {
      "route_geometry_loss": 1.3154839277267456,
      "step": 6
    },
    {
      "route_geometry_loss": 1.258283019065857,
      "step": 7
    },
    {
      "route_geometry_loss": 1.271714448928833,
      "step": 8
    },
    {
      "route_geometry_loss": 1.2462321519851685,
      "step": 9
    },
    {
      "route_geometry_loss": 1.2147547006607056,
      "step": 10
    },
    {
      "route_geometry_loss": 1.250464677810669,
      "step": 11
    },
    {
      "route_geometry_loss": 1.2803094387054443,
      "step": 12
    },
    {
      "route_geometry_loss": 1.2850749492645264,
      "step": 13
    },
    {
      "route_geometry_loss": 1.3013060092926025,
      "step": 14
    },
    {
      "route_geometry_loss": 1.253366231918335,
      "step": 15
    },
    {
      "route_geometry_loss": 1.2293931245803833,
      "step": 16
    },
    {
      "route_geometry_loss": 1.2457822561264038,
      "step": 17
    },
    {
      "route_geometry_loss": 1.2471433877944946,
      "step": 18
    },
    {
      "route_geometry_loss": 1.2033321857452393,
      "step": 19
    },
    {
      "route_geometry_loss": 1.205954909324646,
      "step": 20
    },
    {
      "route_geometry_loss": 1.1922204494476318,
      "step": 21
    },
    {
      "route_geometry_loss": 1.193632960319519,
      "step": 22
    },
    {
      "route_geometry_loss": 1.1553666591644287,
      "step": 23
    },
    {
      "route_geometry_loss": 1.1843466758728027,
      "step": 24
    },
    {
      "route_geometry_loss": 1.1557337045669556,
      "step": 25
    },
    {
      "route_geometry_loss": 1.123128890991211,
      "step": 26
    },
    {
      "route_geometry_loss": 1.1158537864685059,
      "step": 27
    },
    {
      "route_geometry_loss": 1.1177659034729004,
      "step": 28
    },
    {
      "route_geometry_loss": 1.1157715320587158,
      "step": 29
    },
    {
      "route_geometry_loss": 1.0955662727355957,
      "step": 30
    },
    {
      "route_geometry_loss": 1.0710028409957886,
      "step": 31
    },
    {
      "route_geometry_loss": 1.071171760559082,
      "step": 32
    },
    {
      "route_geometry_loss": 1.1008975505828857,
      "step": 33
    },
    {
      "route_geometry_loss": 1.0429673194885254,
      "step": 34
    },
    {
      "route_geometry_loss": 1.0433459281921387,
      "step": 35
    },
    {
      "route_geometry_loss": 1.0889313220977783,
      "step": 36
    },
    {
      "route_geometry_loss": 1.0760170221328735,
      "step": 37
    },
    {
      "route_geometry_loss": 0.9806746244430542,
      "step": 38
    },
    {
      "route_geometry_loss": 1.0425426959991455,
      "step": 39
    },
    {
      "route_geometry_loss": 0.9956836104393005,
      "step": 40
    },
    {
      "route_geometry_loss": 1.0157674551010132,
      "step": 41
    },
    {
      "route_geometry_loss": 0.9941603541374207,
      "step": 42
    },
    {
      "route_geometry_loss": 0.9478485584259033,
      "step": 43
    },
    {
      "route_geometry_loss": 0.9602751731872559,
      "step": 44
    },
    {
      "route_geometry_loss": 0.9476706385612488,
      "step": 45
    },
    {
      "route_geometry_loss": 0.9170610904693604,
      "step": 46
    },
    {
      "route_geometry_loss": 0.9521533846855164,
      "step": 47
    },
    {
      "route_geometry_loss": 0.9885377287864685,
      "step": 48
    },
    {
      "route_geometry_loss": 1.0253350734710693,
      "step": 49
    },
    {
      "route_geometry_loss": 1.0349721908569336,
      "step": 50
    }
  ]
}
```
