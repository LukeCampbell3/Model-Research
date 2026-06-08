# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.595 | 4.546 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.434 | 4.019 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.428 | 3.861 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.400 | 3.826 | 1.00x | 5.5746 | 0.002262 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.083 | 5.615 | 1.00x | 5.5720 | 0.000754 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 7.691 | 8.193 | 1.00x | 5.5459 | 0.001128 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 3.790 | 4.269 | 1.00x | 5.5560 | 0.001015 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 7.700 | 8.208 | 1.00x | 5.5819 | 0.000502 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 12.973 | 13.205 | 1.00x | 5.5689 | 0.000189 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.058 | 5.543 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 12.907 | 13.111 | 1.00x | 5.5686 | 0.000266 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 23.059 | 23.523 | 1.00x | 5.5754 | 0.000148 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 7.685 | 8.249 | 1.00x | 5.5833 | 0.000252 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 23.160 | 23.643 | 1.00x | 5.5759 | 0.000210 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 43.763 | 44.193 | 1.00x | 5.5728 | 0.000081 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 3.671 | 4.122 | 1.00x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 3.961 | 4.444 | 1.14x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 3.920 | 4.341 | 1.14x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 3.930 | 4.326 | 1.15x | 5.5745 | 0.001964 | 0.000527 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 3.921 | 4.461 | 0.78x | 5.5899 | 0.000972 | 0.000131 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 3.937 | 4.339 | 0.51x | 5.5786 | 0.002196 | 0.000177 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 3.897 | 4.391 | 1.04x | 5.5682 | 0.000979 | 0.000187 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 3.973 | 4.577 | 0.53x | 5.5908 | 0.000953 | 0.000079 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 3.993 | 4.517 | 0.32x | 5.5772 | 0.000599 | 0.000027 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 3.982 | 4.482 | 0.79x | 5.5827 | 0.000481 | 0.000061 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 4.167 | 4.907 | 0.34x | 5.5750 | 0.000906 | 0.000044 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 4.520 | 5.248 | 0.20x | 5.5767 | 0.000736 | 0.000020 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 3.977 | 4.523 | 0.52x | 5.5811 | 0.000966 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.475 | 5.219 | 0.20x | 5.5764 | 0.000953 | 0.000026 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 5.519 | 6.117 | 0.13x | 5.5769 | 0.000626 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 3.680 | 4.184 | 1.01x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 3.971 | 4.222 | 1.13x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 3.935 | 4.269 | 1.14x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 3.941 | 4.410 | 1.16x | 5.5744 | 0.001946 | 0.000406 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 3.980 | 4.199 | 0.78x | 5.5785 | 0.000972 | 0.000084 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 3.954 | 4.349 | 0.51x | 5.5624 | 0.002193 | 0.000107 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 3.939 | 4.267 | 1.04x | 5.5474 | 0.000978 | 0.000133 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 3.971 | 4.535 | 0.52x | 5.5935 | 0.000962 | 0.000047 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 4.611 | 5.247 | 0.36x | 5.5783 | 0.000518 | 0.000016 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 3.964 | 4.396 | 0.78x | 5.5807 | 0.000484 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 4.537 | 5.079 | 0.36x | 5.5685 | 0.000840 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 5.424 | 6.079 | 0.24x | 5.5730 | 0.000616 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 3.934 | 4.388 | 0.52x | 5.5710 | 0.000972 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 5.522 | 6.329 | 0.24x | 5.5680 | 0.000774 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 7.261 | 7.770 | 0.17x | 5.5752 | 0.000481 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.