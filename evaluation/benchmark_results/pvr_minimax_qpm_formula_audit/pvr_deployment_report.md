# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.404 | 3.761 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.462 | 3.869 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.413 | 3.864 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.395 | 3.916 | 1.00x | 5.5746 | 0.002239 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.045 | 5.622 | 1.00x | 5.5720 | 0.000757 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 7.747 | 8.230 | 1.00x | 5.5459 | 0.001126 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 3.810 | 4.129 | 1.00x | 5.5560 | 0.001008 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 7.697 | 8.261 | 1.00x | 5.5819 | 0.000500 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 13.018 | 13.295 | 1.00x | 5.5689 | 0.000188 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.084 | 5.624 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 12.957 | 13.220 | 1.00x | 5.5686 | 0.000265 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 23.098 | 23.522 | 1.00x | 5.5754 | 0.000148 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 7.745 | 8.227 | 1.00x | 5.5833 | 0.000250 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 23.113 | 23.480 | 1.00x | 5.5759 | 0.000211 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 43.814 | 44.295 | 1.00x | 5.5728 | 0.000081 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 3.697 | 4.283 | 1.10x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 3.951 | 4.462 | 1.14x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 3.968 | 4.325 | 1.16x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 3.910 | 4.414 | 1.15x | 5.5745 | 0.001951 | 0.000527 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 3.951 | 4.440 | 0.78x | 5.5899 | 0.000973 | 0.000131 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 3.956 | 4.252 | 0.51x | 5.5786 | 0.002199 | 0.000177 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 3.969 | 4.508 | 1.04x | 5.5682 | 0.000967 | 0.000187 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 4.050 | 4.695 | 0.53x | 5.5908 | 0.000946 | 0.000079 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 4.013 | 4.672 | 0.32x | 5.5772 | 0.000593 | 0.000027 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 3.981 | 4.547 | 0.79x | 5.5827 | 0.000478 | 0.000061 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 4.168 | 4.845 | 0.33x | 5.5750 | 0.000911 | 0.000044 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 4.615 | 5.263 | 0.20x | 5.5767 | 0.000725 | 0.000020 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 3.989 | 4.583 | 0.53x | 5.5811 | 0.000951 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.479 | 5.156 | 0.20x | 5.5764 | 0.000955 | 0.000026 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 5.556 | 6.298 | 0.13x | 5.5769 | 0.000623 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 3.716 | 4.159 | 1.09x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 3.987 | 4.468 | 1.15x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 3.942 | 4.330 | 1.15x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 3.956 | 4.280 | 1.15x | 5.5744 | 0.001950 | 0.000406 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 3.923 | 4.304 | 0.77x | 5.5785 | 0.000979 | 0.000084 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 3.989 | 4.537 | 0.52x | 5.5624 | 0.002148 | 0.000107 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 3.939 | 4.260 | 1.03x | 5.5474 | 0.000977 | 0.000133 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 4.029 | 4.740 | 0.53x | 5.5935 | 0.000934 | 0.000047 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 4.581 | 5.203 | 0.36x | 5.5783 | 0.000520 | 0.000016 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 3.966 | 4.382 | 0.78x | 5.5807 | 0.000486 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 4.576 | 5.224 | 0.36x | 5.5685 | 0.000830 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 5.450 | 6.051 | 0.24x | 5.5730 | 0.000615 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 3.959 | 4.482 | 0.52x | 5.5710 | 0.000967 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 5.454 | 5.991 | 0.24x | 5.5680 | 0.000791 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 7.220 | 7.822 | 0.17x | 5.5752 | 0.000483 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.