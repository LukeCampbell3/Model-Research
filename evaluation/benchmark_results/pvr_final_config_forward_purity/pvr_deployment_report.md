# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 28.381 | 29.547 | N/A | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 29.422 | 30.708 | N/A | 5.5685 | 0.000132 | 0.000024 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.