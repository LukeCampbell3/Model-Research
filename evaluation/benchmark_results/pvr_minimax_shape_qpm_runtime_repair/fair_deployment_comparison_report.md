# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.372 | 3.849 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.461 | 3.879 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.392 | 3.730 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.434 | 3.789 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.103 | 5.596 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 7.698 | 8.149 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 3.758 | 4.256 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 7.870 | 8.331 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 12.992 | 13.494 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.035 | 5.503 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 12.952 | 13.134 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 23.105 | 23.759 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 7.779 | 8.185 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 23.059 | 23.579 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 43.788 | 44.333 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 3.743 | 4.268 | 0.90x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 4.017 | 4.444 | 0.87x | 12.34 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 3.944 | 4.343 | 0.86x | 14.83 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 3.952 | 4.292 | 0.87x | 14.83 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 3.973 | 4.364 | 1.29x | 29.75 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 3.954 | 4.514 | 1.92x | 49.65 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 4.017 | 4.351 | 0.95x | 20.94 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 4.018 | 4.655 | 1.90x | 49.65 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 4.008 | 4.641 | 3.15x | 89.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 4.014 | 4.524 | 1.26x | 32.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.184 | 4.895 | 2.98x | 89.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 4.491 | 5.536 | 4.95x | 169.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 4.007 | 4.490 | 1.92x | 54.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.446 | 5.065 | 5.10x | 169.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 5.570 | 6.122 | 7.71x | 328.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 3.705 | 4.345 | 0.90x | 23.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 3.976 | 4.468 | 0.88x | 14.73 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 3.957 | 4.309 | 0.86x | 19.24 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 3.965 | 4.180 | 0.87x | 19.24 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 3.960 | 4.411 | 1.29x | 46.25 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 4.004 | 4.540 | 1.90x | 82.28 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 4.046 | 4.451 | 0.94x | 29.37 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 4.032 | 4.677 | 1.90x | 82.27 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 4.647 | 5.392 | 2.69x | 154.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 4.002 | 4.525 | 1.26x | 48.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 4.641 | 5.249 | 2.71x | 154.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 5.454 | 6.060 | 4.15x | 298.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 4.004 | 4.279 | 1.92x | 86.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 5.529 | 6.511 | 4.05x | 298.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 7.281 | 7.758 | 5.95x | 586.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.