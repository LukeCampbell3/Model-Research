# Fair Deployment Comparison

**Status:** PVR_EC_DEPLOY_CANDIDATE

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 32 | 64 | 13.118 | 13.561 | 1.00x | 1570.16 | 5.5678 | 0.0059 |
| pvr_ec_deploy_top2 | 32 | 64 | 5.280 | 5.743 | 2.44x | 408.33 | 5.5672 | 0.0044 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.