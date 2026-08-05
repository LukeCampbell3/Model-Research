# PVR Claim Proof Battery Audit

Status: `PVR_CLAIM_PROOF_BATTERY_PARTIAL_SUPPORTED`

## Route Margin

```json
{
  "benefit_by_margin_quartile": [
    1.4305277972227664,
    1.1581822187649335,
    1.249198821288708,
    1.3210634720576084
  ],
  "high_margin_mean_benefit": 1.285131146673158,
  "low_margin_mean_benefit": 1.29435500799385,
  "quartile_monotonic_non_decreasing": false,
  "route_margin_vs_expert_benefit_correlation": -0.014088498830870655
}
```

## Semantic Owner Geometry

```json
{
  "loss_bucket_nmi_lift_vs_shuffle": 0.006637766725560508,
  "owner_loss_bucket_nmi": 0.007702028354570472,
  "owner_syntax_region_nmi": 0.03142220850864993,
  "owner_token_class_nmi": 0.03948897024673264,
  "shuffled_owner_loss_bucket_nmi": 0.0010642616290099634,
  "shuffled_owner_syntax_region_nmi": 0.004913466284749939,
  "shuffled_owner_token_class_nmi": 0.005834628735651575,
  "syntax_region_nmi_lift_vs_shuffle": 0.02650874222389999,
  "token_class_nmi_lift_vs_shuffle": 0.033654341511081064
}
```

## Expert Delta Causality

```json
{
  "high_benefit_wrong_expert_harm": 2.0742133428091125,
  "mean_full_vs_shared_benefit": 1.289743077333504,
  "mean_wrong_expert_harm": 1.2417185518132754,
  "structured_full_vs_shared_benefit": 2.404115576166546,
  "structured_wrong_expert_harm": 2.017081891326066,
  "structured_wrong_expert_worse_than_full_rate": 0.8435430463576159,
  "wrong_expert_worse_than_full_rate": 0.7513020833333334
}
```

## Conditions

```json
{
  "causal::full_beats_shared": true,
  "causal::structured_full_beats_shared": true,
  "causal::structured_wrong_expert_harms": true,
  "causal::wrong_expert_harms": true,
  "causal::wrong_expert_worse_rate_high": true,
  "expert_delta_causality_supported": true,
  "margin::high_margin_beats_low_margin": false,
  "margin::margin_correlation_positive": false,
  "margin::margin_quartiles_monotonic": false,
  "route_margin_interpretability_supported": false,
  "semantic::owner_loss_bucket_lift_vs_shuffle": false,
  "semantic::owner_syntax_lift_vs_shuffle": true,
  "semantic::owner_token_class_lift_vs_shuffle": true,
  "semantic::owner_token_class_nmi_substantial": false,
  "semantic_owner_geometry_supported": false,
  "top1_invariants_clean": true
}
```
