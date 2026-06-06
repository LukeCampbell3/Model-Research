# PVR-EC Deployment Report

**Status:** PVR_EC_DEPLOY_CANDIDATE

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 32 | 64 | 13.065 | 13.251 | 1.00x | 5.5678 | 0.000450 | 0.000004 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 5.807 | 6.246 | 0.45x | 5.5672 | 0.000746 | 0.000011 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.