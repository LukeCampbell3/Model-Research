# PVR-EC Deployment Report

**Status:** PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown | Loss | QPM | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe | off | 1 | 64 | 11.214 | 11.491 | 1.00x | 5.5383 | 0.000000 | LOOPED |
| fixed_moe | off | 32 | 64 | 11.249 | 11.681 | 1.00x | 5.5639 | 0.000349 | LOOPED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.645 | 3.054 | 0.24x | 5.5653 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 2.800 | 3.014 | 0.25x | 5.5614 | 0.001216 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.