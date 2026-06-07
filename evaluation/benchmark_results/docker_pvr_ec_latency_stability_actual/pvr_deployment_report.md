# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 4.650 | 5.636 | 1.00x | 5.5075 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 12.888 | 14.432 | 1.00x | 5.5773 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 20.832 | 25.714 | 1.00x | 5.5558 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 60.447 | 63.075 | 1.00x | 5.5661 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 2.767 | 3.698 | 0.59x | 5.4871 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 3.869 | 4.752 | 0.29x | 5.5398 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 6.781 | 7.372 | 0.29x | 5.5475 | 0.001236 | 781250.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 7.148 | 18.520 | 0.15x | 5.5581 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_medium | top1 | 1 | 16 | 2.651 | 3.713 | 0.58x | 5.5730 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_medium | top1 | 1 | 64 | 3.652 | 4.677 | 0.29x | 5.5396 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_medium | top1 | 8 | 16 | 3.556 | 5.080 | 0.18x | 5.5649 | 0.002060 | 781250.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_medium | top1 | 8 | 64 | 8.027 | 9.427 | 0.13x | 5.5592 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 1 | 16 | 3.719 | 4.613 | 0.78x | 5.4289 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 1 | 64 | 4.187 | 5.645 | 0.33x | 5.5459 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 8 | 16 | 5.373 | 6.423 | 0.24x | 5.5828 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 8 | 64 | 25.301 | 28.475 | 0.42x | 5.5569 | 0.000151 | 390625.000000 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.