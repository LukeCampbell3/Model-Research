# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.372 | 3.849 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.461 | 3.879 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.392 | 3.730 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.434 | 3.789 | 1.00x | 5.5746 | 0.002239 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.103 | 5.596 | 1.00x | 5.5720 | 0.000751 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 7.698 | 8.149 | 1.00x | 5.5459 | 0.001131 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 3.758 | 4.256 | 1.00x | 5.5560 | 0.001012 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 7.870 | 8.331 | 1.00x | 5.5819 | 0.000498 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 12.992 | 13.494 | 1.00x | 5.5689 | 0.000188 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.035 | 5.503 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 12.952 | 13.134 | 1.00x | 5.5686 | 0.000265 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 23.105 | 23.759 | 1.00x | 5.5754 | 0.000147 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 7.779 | 8.185 | 1.00x | 5.5833 | 0.000252 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 23.059 | 23.579 | 1.00x | 5.5759 | 0.000211 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 43.788 | 44.333 | 1.00x | 5.5728 | 0.000081 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 3.743 | 4.268 | 1.11x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 4.017 | 4.444 | 1.15x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 3.944 | 4.343 | 1.16x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 3.952 | 4.292 | 1.14x | 5.5745 | 0.001958 | 0.000527 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 3.973 | 4.364 | 0.77x | 5.5899 | 0.000972 | 0.000131 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 3.954 | 4.514 | 0.52x | 5.5786 | 0.002169 | 0.000177 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 4.017 | 4.351 | 1.05x | 5.5682 | 0.000966 | 0.000187 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 4.018 | 4.655 | 0.53x | 5.5908 | 0.000948 | 0.000079 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 4.008 | 4.641 | 0.32x | 5.5772 | 0.000593 | 0.000027 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 4.014 | 4.524 | 0.79x | 5.5827 | 0.000480 | 0.000061 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 4.184 | 4.895 | 0.34x | 5.5750 | 0.000903 | 0.000044 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 4.491 | 5.536 | 0.20x | 5.5767 | 0.000729 | 0.000020 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 4.007 | 4.490 | 0.52x | 5.5811 | 0.000966 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.446 | 5.065 | 0.20x | 5.5764 | 0.000966 | 0.000026 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 5.570 | 6.122 | 0.13x | 5.5769 | 0.000624 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 3.705 | 4.345 | 1.11x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 3.976 | 4.468 | 1.14x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 3.957 | 4.309 | 1.16x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 3.965 | 4.180 | 1.14x | 5.5744 | 0.001957 | 0.000406 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 3.960 | 4.411 | 0.77x | 5.5785 | 0.000971 | 0.000084 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 4.004 | 4.540 | 0.53x | 5.5624 | 0.002150 | 0.000107 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 4.046 | 4.451 | 1.06x | 5.5474 | 0.000955 | 0.000133 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 4.032 | 4.677 | 0.53x | 5.5935 | 0.000947 | 0.000047 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 4.647 | 5.392 | 0.37x | 5.5783 | 0.000506 | 0.000016 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 4.002 | 4.525 | 0.79x | 5.5807 | 0.000480 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 4.641 | 5.249 | 0.37x | 5.5685 | 0.000823 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 5.454 | 6.060 | 0.24x | 5.5730 | 0.000612 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 4.004 | 4.279 | 0.52x | 5.5710 | 0.000969 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 5.529 | 6.511 | 0.25x | 5.5680 | 0.000768 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 7.281 | 7.758 | 0.17x | 5.5752 | 0.000481 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.