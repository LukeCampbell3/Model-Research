# PVR-EC Deployment Report

**Status:** PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown | Loss | QPM | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe | off | 1 | 64 | 11.199 | 11.355 | 1.00x | 5.5383 | 0.000000 | LOOPED |
| fixed_moe | off | 32 | 64 | 11.201 | 11.883 | 1.00x | 5.5639 | 0.000348 | LOOPED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.622 | 3.037 | 0.24x | 5.5654 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 2.778 | 3.248 | 0.25x | 5.5607 | 0.000855 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.