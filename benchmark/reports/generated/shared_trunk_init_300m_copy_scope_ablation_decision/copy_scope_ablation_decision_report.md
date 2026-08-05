# Shared-Trunk Copy-Scope Ablation Decision

Status: `PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_EMBEDDINGS_ATTENTION_NORMS_SUPPORTED`

Best scope: `embeddings_attention_norms`

```json
{
  "best_scope": "embeddings_attention_norms",
  "best_vs_full_compatible": {
    "final_train_loss_delta": 0.008172035217285156,
    "lm_loss_delta": -0.0033113431930540393,
    "mean_eval_loss_delta": -0.008507823944091442
  },
  "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
  "created_at": "2026-06-16T22:48:42.678879+00:00",
  "decision": {
    "attention_only_is_not_sufficient": true,
    "embeddings_only_is_helpful_but_not_sufficient": true,
    "full_compatible_shared_copy_still_supported": true,
    "primary_carrier": "embeddings_attention_norms",
    "shared_ffn_bias_not_required_for_main_gain": true
  },
  "git_commit": "243422e88483ef7ff3ae133eb8cbd77a7b2f2fce",
  "interpretation": "The dense-to-PVR transfer gain is concentrated in shared token/position embeddings, attention, and norms. Full compatible shared copy remains supported, but its extra copied shared FFN bias does not explain the win and is slightly worse than embeddings+attention+norms on reduced LM loss in this seed.",
  "rankings": {
    "lm_loss_ascending": [
      {
        "copy_scope": "embeddings_attention_norms",
        "lm_loss": 3.0279019391536712
      },
      {
        "copy_scope": "full_compatible_shared_copy",
        "lm_loss": 3.0312132823467253
      },
      {
        "copy_scope": "attention_only",
        "lm_loss": 3.384330289363861
      },
      {
        "copy_scope": "embeddings_only",
        "lm_loss": 3.403685820102692
      },
      {
        "copy_scope": "shared_ffn_bias_only",
        "lm_loss": 3.4958942592144013
      },
      {
        "copy_scope": "norms_only",
        "lm_loss": 3.4968364417552946
      }
    ],
    "mean_eval_loss_ascending": [
      {
        "copy_scope": "embeddings_attention_norms",
        "mean_eval_loss": 4.97853536605835
      },
      {
        "copy_scope": "full_compatible_shared_copy",
        "mean_eval_loss": 4.987043190002441
      },
      {
        "copy_scope": "shared_ffn_bias_only",
        "mean_eval_loss": 5.410947728157043
      },
      {
        "copy_scope": "embeddings_only",
        "mean_eval_loss": 5.471221661567688
      },
      {
        "copy_scope": "norms_only",
        "mean_eval_loss": 5.513810610771179
      },
      {
        "copy_scope": "attention_only",
        "mean_eval_loss": 5.751970911026001
      }
    ]
  },
  "schema_version": "1.0",
  "source_report": "benchmark/reports/generated/shared_trunk_init_300m_copy_scope_ablation/copy_scope_ablation_report.json",
  "status": "PVR_SHARED_TRUNK_COPY_SCOPE_ABLATION_EMBEDDINGS_ATTENTION_NORMS_SUPPORTED",
  "supported_scopes": [
    "embeddings_only",
    "norms_only",
    "shared_ffn_bias_only",
    "embeddings_attention_norms",
    "full_compatible_shared_copy"
  ]
}
```
