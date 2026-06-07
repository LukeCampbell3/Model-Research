# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 28.381 | 29.547 | N/A | 15.02 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 29.422 | 30.708 | N/A | 163.32 | 5.5685 | 0.0039 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.