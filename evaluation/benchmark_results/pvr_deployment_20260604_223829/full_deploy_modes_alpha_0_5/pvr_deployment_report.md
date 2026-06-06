# PVR-EC Deployment Report

**Status:** PVR_EC_READY_FOR_LONGER_CAPABILITY_RUN

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown | Loss | QPM | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe | off | 1 | 64 | 10.874 | 11.281 | 1.00x | 5.5383 | 0.000000 | LOOPED |
| fixed_moe | off | 32 | 64 | 11.049 | 12.059 | 1.00x | 5.5639 | 0.000352 | LOOPED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 2.483 | 2.915 | 0.23x | 5.5653 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 2.436 | 2.825 | 0.22x | 5.5614 | 0.001367 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.586 | 2.966 | 0.24x | 5.5663 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 2.777 | 2.910 | 0.25x | 5.5610 | 0.001216 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 1 | 64 | 2.798 | 2.901 | 0.26x | 5.5642 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 32 | 64 | 3.265 | 3.772 | 0.30x | 5.5606 | 0.000876 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 1 | 64 | 2.602 | 2.998 | 0.24x | 5.5654 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 32 | 64 | 3.492 | 4.003 | 0.32x | 5.5607 | 0.000685 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.