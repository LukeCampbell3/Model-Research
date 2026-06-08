# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.595 | 4.546 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.434 | 4.019 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.428 | 3.861 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.400 | 3.826 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.083 | 5.615 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 7.691 | 8.193 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 3.790 | 4.269 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 7.700 | 8.208 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 12.973 | 13.205 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.058 | 5.543 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 12.907 | 13.111 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 23.059 | 23.523 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 7.685 | 8.249 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 23.160 | 23.643 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 43.763 | 44.193 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 3.671 | 4.122 | 1.00x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 3.961 | 4.444 | 0.87x | 12.34 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 3.920 | 4.341 | 0.88x | 14.83 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 3.930 | 4.326 | 0.87x | 14.83 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 3.921 | 4.461 | 1.29x | 29.75 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 3.937 | 4.339 | 1.95x | 49.65 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 3.897 | 4.391 | 0.96x | 20.94 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 3.973 | 4.577 | 1.90x | 49.65 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 3.993 | 4.517 | 3.17x | 89.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 3.982 | 4.482 | 1.27x | 32.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.167 | 4.907 | 2.98x | 89.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 4.520 | 5.248 | 4.98x | 169.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 3.977 | 4.523 | 1.92x | 54.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.475 | 5.219 | 5.03x | 169.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 5.519 | 6.117 | 7.73x | 328.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 3.680 | 4.184 | 0.99x | 23.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 3.971 | 4.222 | 0.88x | 14.73 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 3.935 | 4.269 | 0.88x | 19.24 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 3.941 | 4.410 | 0.86x | 19.24 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 3.980 | 4.199 | 1.29x | 46.25 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 3.954 | 4.349 | 1.95x | 82.28 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 3.939 | 4.267 | 0.96x | 29.37 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 3.971 | 4.535 | 1.92x | 82.27 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 4.611 | 5.247 | 2.74x | 154.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 3.964 | 4.396 | 1.28x | 48.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 4.537 | 5.079 | 2.76x | 154.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 5.424 | 6.079 | 4.17x | 298.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 3.934 | 4.388 | 1.93x | 86.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 5.522 | 6.329 | 4.09x | 298.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 7.261 | 7.770 | 5.94x | 586.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.