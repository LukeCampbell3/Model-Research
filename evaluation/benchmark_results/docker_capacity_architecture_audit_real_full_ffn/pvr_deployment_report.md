# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| pvr_ec_ownership_top1_delta_large | top1 | 1 | 64 | 109.939 | 155.392 | N/A | 5.5760 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_delta_large | top1 | 32 | 64 | 28.125 | 144.675 | N/A | 5.5773 | 0.000070 | 0.000014 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 1 | 64 | 94.131 | 146.662 | N/A | 5.5733 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_full_expert_ffn_control | top1 | 32 | 64 | 13.232 | 169.207 | N/A | 5.5685 | 0.000064 | 0.000008 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.