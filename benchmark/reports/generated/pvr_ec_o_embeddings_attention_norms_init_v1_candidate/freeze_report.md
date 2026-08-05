# PVR-EC-O EAN Init v1 Freeze

Status: `PVR_EAN_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED`

```json
{
  "active_compute_audit": {
    "rankings": {
      "lm_loss_ascending": [
        {
          "lm_loss": 3.010810148715973,
          "model": "pvr_ec_o_embeddings_attention_norms_init_v1_seed_42"
        },
        {
          "lm_loss": 3.0127717781066896,
          "model": "pvr_ec_o_full_compatible_shared_copy_seed_42"
        },
        {
          "lm_loss": 3.305846790075302,
          "model": "dense_transformer_300m"
        },
        {
          "lm_loss": 3.319429429769516,
          "model": "vanilla_switch_top1_reference_300m"
        },
        {
          "lm_loss": 3.3654595971107484,
          "model": "generic_top2_moe_reference_300m"
        },
        {
          "lm_loss": 3.422222343683243,
          "model": "pvr_ec_o_full_300m_baseline_seed_42"
        }
      ],
      "quality_per_active_flop_descending": [
        {
          "model": "pvr_ec_o_embeddings_attention_norms_init_v1_seed_42",
          "quality_per_active_flop": 5.272008226684526e-10
        },
        {
          "model": "pvr_ec_o_full_compatible_shared_copy_seed_42",
          "quality_per_active_flop": 5.268575598179203e-10
        },
        {
          "model": "vanilla_switch_top1_reference_300m",
          "quality_per_active_flop": 4.781850679114456e-10
        },
        {
          "model": "pvr_ec_o_full_300m_baseline_seed_42",
          "quality_per_active_flop": 4.638218759314215e-10
        },
        {
          "model": "generic_top2_moe_reference_300m",
          "quality_per_active_flop": 3.301513742922368e-10
        },
        {
          "model": "dense_transformer_300m",
          "quality_per_active_flop": 1.68052420706073e-10
        }
      ],
      "quality_per_active_param_descending": [
        {
          "model": "pvr_ec_o_embeddings_attention_norms_init_v1_seed_42",
          "quality_per_active_param": 3.163204936010716e-09
        },
        {
          "model": "pvr_ec_o_full_compatible_shared_copy_seed_42",
          "quality_per_active_param": 3.161145358907522e-09
        },
        {
          "model": "vanilla_switch_top1_reference_300m",
          "quality_per_active_param": 2.8691104074686737e-09
        },
        {
          "model": "pvr_ec_o_full_300m_baseline_seed_42",
          "quality_per_active_param": 2.7829312555885286e-09
        },
        {
          "model": "generic_top2_moe_reference_300m",
          "quality_per_active_param": 1.9809082457534208e-09
        },
        {
          "model": "dense_transformer_300m",
          "quality_per_active_param": 1.0083145242364378e-09
        }
      ]
    },
    "rows": [
      {
        "active_flops_per_token": 630000000,
        "active_params_per_token": 105000000,
        "lm_loss": 3.010810148715973,
        "model": "pvr_ec_o_embeddings_attention_norms_init_v1_seed_42",
        "quality_per_active_flop": 5.272008226684526e-10,
        "quality_per_active_param": 3.163204936010716e-09,
        "source": "ean_init_300m_repeat_seed_42",
        "tokens_per_second": 1337.2612152468616,
        "vram_peak": 1182379008
      },
      {
        "active_flops_per_token": 630000000,
        "active_params_per_token": 105000000,
        "lm_loss": 3.0127717781066896,
        "model": "pvr_ec_o_full_compatible_shared_copy_seed_42",
        "quality_per_active_flop": 5.268575598179203e-10,
        "quality_per_active_param": 3.161145358907522e-09,
        "source": "shared_trunk_init_300m_repeat_seed_42",
        "tokens_per_second": 1315.0728316762484,
        "vram_peak": 1173859328
      },
      {
        "active_flops_per_token": 1800000000,
        "active_params_per_token": 300000000,
        "lm_loss": 3.305846790075302,
        "model": "dense_transformer_300m",
        "quality_per_active_flop": 1.68052420706073e-10,
        "quality_per_active_param": 1.0083145242364378e-09,
        "source": "comparison_300m_real_4k",
        "tokens_per_second": 9285.982897748594,
        "vram_peak": 1028209664
      },
      {
        "active_flops_per_token": 630000000,
        "active_params_per_token": 105000000,
        "lm_loss": 3.319429429769516,
        "model": "vanilla_switch_top1_reference_300m",
        "quality_per_active_flop": 4.781850679114456e-10,
        "quality_per_active_param": 2.8691104074686737e-09,
        "source": "comparison_300m_real_4k",
        "tokens_per_second": 916.3825388346461,
        "vram_peak": 1075235840
      },
      {
        "active_flops_per_token": 900000000,
        "active_params_per_token": 150000000,
        "lm_loss": 3.3654595971107484,
        "model": "generic_top2_moe_reference_300m",
        "quality_per_active_flop": 3.301513742922368e-10,
        "quality_per_active_param": 1.9809082457534208e-09,
        "source": "comparison_300m_real_4k",
        "tokens_per_second": 852.4066809218992,
        "vram_peak": 1075235840
      },
      {
        "active_flops_per_token": 630000000,
        "active_params_per_token": 105000000,
        "lm_loss": 3.422222343683243,
        "model": "pvr_ec_o_full_300m_baseline_seed_42",
        "quality_per_active_flop": 4.638218759314215e-10,
        "quality_per_active_param": 2.7829312555885286e-09,
        "source": "shared_trunk_init_300m_repeat_seed_42",
        "tokens_per_second": 1185.5932915766498,
        "vram_peak": 1173859328
      }
    ]
  },
  "candidate": "pvr_ec_o_embeddings_attention_norms_init_v1",
  "candidate_config": "benchmark/configs/generated/pvr_ec_o_embeddings_attention_norms_init_v1_300m.yaml",
  "created_at": "2026-06-17T02:03:59.996868+00:00",
  "decision": {
    "baseline_pvr_lm_loss": 3.422222343683243,
    "dense_reference_lm_loss": 3.305846790075302,
    "eval_curve_material_regression": true,
    "full_copy_lm_loss": 3.0127717781066896,
    "init_minus_baseline_final_train_loss": -0.23779559135437012,
    "init_minus_baseline_lm_loss": -0.4114121949672698,
    "init_minus_baseline_mean_eval_loss": 0.12875699996948242,
    "init_minus_dense_lm_loss": -0.29503664135932883,
    "init_minus_full_copy_lm_loss": -0.001961629390716535,
    "lm_loss": 3.010810148715973,
    "scorecard_supported": true
  },
  "fallback_candidate": "pvr_ec_o_full_shared_trunk_init_v1",
  "git_commit": "d18165e32bec94cea3ca836937c81f6a0f3dc5f7",
  "not_fully_supported": [
    "300M repeat is clean across all eval views",
    "from-scratch PVR dominance",
    "teacher independence",
    "full-compatible shared copy is always optimal"
  ],
  "route_stability": {
    "mean_owner_entropy_delta_vs_baseline": 0.026722983922166765,
    "mean_prototype_monopoly_rate_delta_vs_baseline": -0.02226562500000001,
    "mean_route_margin_delta_vs_baseline": 0.03928592702516953,
    "route_stable": true,
    "top1_invariants_clean": true
  },
  "schema_version": "1.0",
  "source_reports": {
    "baseline_scorecard": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_baseline_seed_42_nlp_scorecard.json",
    "comparison_report": "benchmark/reports/generated/comparison_300m_real_4k/benchmark_comparison_report.json",
    "ean_repeat": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/copy_scope_ablation_report.json",
    "ean_scorecard": "benchmark/reports/generated/ean_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_v1_scope_embeddings_attention_norms_seed_42_nlp_scorecard.json",
    "full_copy_scorecard": "benchmark/reports/generated/shared_trunk_init_300m_repeat_seed_42/lm_eval/pvr_ec_o_full_300m_shared_trunk_init_from_dense_seed_42_nlp_scorecard.json"
  },
  "status": "PVR_EAN_INIT_300M_REPEAT_SCORECARD_SUPPORTED_EVAL_CURVE_MIXED",
  "supported_claim": "Embeddings+attention+norms dense-compatible initialization is the main observed transfer carrier and repeats the 300M reduced LM scorecard dense-gap closure with strict Top1 routing."
}
```
