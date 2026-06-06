# PVR-EC Deployment Report

**Status:** PVR_EC_DEPLOY_CANDIDATE

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 32 | 64 | 13.118 | 13.561 | 1.00x | 5.5678 | 0.000448 | 0.000004 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 5.280 | 5.743 | 0.41x | 5.5672 | 0.000820 | 0.000011 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.