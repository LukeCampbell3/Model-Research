# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pvr_ec_ownership_top1_delta_large | 1 | 64 | 109.939 | 155.392 | N/A | 19.42 | 5.5760 | 0.0000 |
| pvr_ec_ownership_top1_delta_large | 32 | 64 | 28.125 | 144.675 | N/A | 281.06 | 5.5773 | 0.0039 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 1 | 64 | 94.131 | 146.662 | N/A | 31.91 | 5.5733 | 0.0000 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 32 | 64 | 13.232 | 169.207 | N/A | 540.57 | 5.5685 | 0.0044 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.