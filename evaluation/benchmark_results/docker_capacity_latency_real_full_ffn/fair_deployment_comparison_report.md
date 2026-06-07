# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 32 | 64 | 41.633 | 43.547 | 1.00x | 1570.16 | 5.5686 | 0.0034 |
| pvr_ec_ownership_top1_delta_large | 32 | 64 | 20.684 | 129.525 | 1.18x | 282.06 | 5.5773 | 0.0039 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 32 | 64 | 134.351 | 210.790 | 0.31x | 541.57 | 5.5685 | 0.0044 |
| pvr_ec_ownership_top1_micro_ffn_1_0x | 32 | 64 | 138.934 | 174.808 | 0.30x | 541.57 | 5.5726 | 0.0039 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.