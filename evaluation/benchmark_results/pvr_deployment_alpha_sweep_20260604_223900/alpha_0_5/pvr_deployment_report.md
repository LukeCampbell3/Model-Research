# PVR-EC Deployment Report

**Status:** PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown | Loss | QPM | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe | off | 1 | 64 | 11.310 | 11.780 | 1.00x | 5.5383 | 0.000000 | LOOPED |
| fixed_moe | off | 32 | 64 | 11.035 | 11.482 | 1.00x | 5.5639 | 0.000354 | LOOPED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.606 | 2.878 | 0.24x | 5.5663 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 2.799 | 3.025 | 0.26x | 5.5610 | 0.001203 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.