# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.585 | 3.992 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.797 | 4.380 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.672 | 4.029 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.611 | 4.025 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.575 | 6.439 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 8.796 | 9.784 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 4.122 | 4.941 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 8.660 | 9.964 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 14.548 | 15.860 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.576 | 6.260 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 14.522 | 15.665 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 26.445 | 27.794 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 8.519 | 9.973 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 26.456 | 27.586 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 45.206 | 52.940 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 3.942 | 4.318 | 0.91x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 4.035 | 4.455 | 0.94x | 12.34 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 3.987 | 4.354 | 0.92x | 14.83 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 3.988 | 4.299 | 0.91x | 14.83 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 4.060 | 4.584 | 1.37x | 29.75 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 4.244 | 4.951 | 2.03x | 49.65 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 4.353 | 4.830 | 0.96x | 20.94 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 4.415 | 5.167 | 1.93x | 49.65 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 4.388 | 5.138 | 3.25x | 89.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 4.317 | 5.016 | 1.27x | 32.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.582 | 5.394 | 3.11x | 89.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 5.731 | 6.386 | 4.91x | 169.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 4.277 | 4.840 | 1.99x | 54.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.820 | 5.326 | 5.40x | 169.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 5.897 | 6.384 | 8.47x | 328.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 3.969 | 4.510 | 0.89x | 23.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 4.307 | 4.730 | 0.89x | 14.73 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 4.233 | 4.620 | 0.86x | 19.24 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 4.212 | 4.695 | 0.85x | 19.24 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 4.266 | 4.666 | 1.32x | 46.25 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 4.317 | 4.768 | 2.02x | 82.28 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 4.591 | 5.530 | 0.90x | 29.37 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 4.339 | 5.019 | 1.97x | 82.27 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 4.943 | 5.657 | 2.90x | 154.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 4.369 | 4.911 | 1.27x | 48.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 4.969 | 5.725 | 2.89x | 154.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 5.829 | 6.382 | 4.50x | 298.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 4.268 | 4.770 | 1.99x | 86.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 5.757 | 6.217 | 4.55x | 298.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 7.597 | 8.102 | 6.63x | 586.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.