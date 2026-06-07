# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 4.650 | 5.636 | 1.00x | 0.00 | 5.5075 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 12.888 | 14.432 | 1.00x | 0.00 | 5.5773 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 20.832 | 25.714 | 1.00x | 0.00 | 5.5558 | 0.0000 |
| fixed_moe_vectorized | 8 | 64 | 60.447 | 63.075 | 1.00x | 0.00 | 5.5661 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 16 | 2.767 | 3.698 | 1.69x | 0.00 | 5.4871 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 3.869 | 4.752 | 3.41x | 0.00 | 5.5398 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 6.781 | 7.372 | 3.42x | 0.00 | 5.5475 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 7.148 | 18.520 | 6.58x | 0.00 | 5.5581 | 0.0000 |
| pvr_ec_ownership_top1_delta_medium | 1 | 16 | 2.651 | 3.713 | 1.73x | 0.00 | 5.5730 | 0.0000 |
| pvr_ec_ownership_top1_delta_medium | 1 | 64 | 3.652 | 4.677 | 3.49x | 0.00 | 5.5396 | 0.0000 |
| pvr_ec_ownership_top1_delta_medium | 8 | 16 | 3.556 | 5.080 | 5.71x | 0.00 | 5.5649 | 0.0078 |
| pvr_ec_ownership_top1_delta_medium | 8 | 64 | 8.027 | 9.427 | 7.48x | 0.00 | 5.5592 | 0.0000 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 1 | 16 | 3.719 | 4.613 | 1.28x | 0.00 | 5.4289 | 0.0000 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 1 | 64 | 4.187 | 5.645 | 3.00x | 0.00 | 5.5459 | 0.0000 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 8 | 16 | 5.373 | 6.423 | 4.21x | 0.00 | 5.5828 | 0.0000 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 8 | 64 | 25.301 | 28.475 | 2.36x | 0.00 | 5.5569 | 0.0039 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.