# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.642 | 4.128 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.756 | 4.769 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.752 | 4.295 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.723 | 4.361 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.808 | 6.629 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 8.697 | 9.970 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 4.261 | 4.871 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 8.778 | 9.592 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 14.686 | 16.205 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.764 | 6.529 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 14.658 | 15.840 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 26.678 | 27.985 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 8.683 | 9.795 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 26.804 | 28.077 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 51.047 | 51.680 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 4.305 | 5.018 | 0.84x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 4.650 | 5.243 | 0.83x | 12.34 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 4.586 | 5.420 | 0.81x | 14.83 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 4.718 | 5.442 | 0.80x | 14.83 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 4.582 | 4.947 | 1.29x | 29.75 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 4.532 | 5.070 | 1.92x | 49.65 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 4.621 | 5.489 | 0.92x | 20.94 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 4.806 | 5.469 | 1.84x | 49.65 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 4.893 | 5.764 | 3.03x | 89.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 4.711 | 5.380 | 1.21x | 32.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.828 | 5.538 | 3.03x | 89.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 5.382 | 6.684 | 4.90x | 169.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 4.634 | 5.324 | 1.88x | 54.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 5.279 | 6.186 | 5.03x | 169.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 6.555 | 7.064 | 7.66x | 328.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 4.320 | 4.808 | 0.86x | 23.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 4.606 | 5.117 | 0.85x | 14.73 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 4.637 | 5.292 | 0.80x | 19.24 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 4.638 | 5.499 | 0.81x | 19.24 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 4.688 | 5.212 | 1.25x | 46.25 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 4.696 | 5.271 | 1.87x | 82.28 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 4.789 | 5.225 | 0.90x | 29.37 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 4.810 | 5.354 | 1.83x | 82.27 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 5.294 | 6.312 | 2.77x | 154.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 4.628 | 5.153 | 1.24x | 48.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 5.325 | 6.105 | 2.73x | 154.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 6.425 | 7.624 | 4.09x | 298.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 4.634 | 5.143 | 1.90x | 86.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 6.424 | 7.045 | 4.16x | 298.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 8.341 | 9.534 | 6.02x | 586.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.