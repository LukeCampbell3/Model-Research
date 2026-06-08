# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.404 | 3.761 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.462 | 3.869 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.413 | 3.864 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.395 | 3.916 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.045 | 5.622 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 7.747 | 8.230 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 3.810 | 4.129 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 7.697 | 8.261 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 13.018 | 13.295 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.084 | 5.624 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 12.957 | 13.220 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 23.098 | 23.522 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 7.745 | 8.227 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 23.113 | 23.480 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 43.814 | 44.295 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 3.697 | 4.283 | 0.91x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 3.951 | 4.462 | 0.88x | 12.34 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 3.968 | 4.325 | 0.86x | 14.83 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 3.910 | 4.414 | 0.87x | 14.83 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 3.951 | 4.440 | 1.29x | 29.75 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 3.956 | 4.252 | 1.95x | 49.65 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 3.969 | 4.508 | 0.96x | 20.94 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 4.050 | 4.695 | 1.89x | 49.65 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 4.013 | 4.672 | 3.16x | 89.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 3.981 | 4.547 | 1.26x | 32.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.168 | 4.845 | 3.01x | 89.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 4.615 | 5.263 | 4.91x | 169.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 3.989 | 4.583 | 1.90x | 54.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.479 | 5.156 | 5.03x | 169.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 5.556 | 6.298 | 7.70x | 328.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 3.716 | 4.159 | 0.92x | 23.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 3.987 | 4.468 | 0.87x | 14.73 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 3.942 | 4.330 | 0.87x | 19.24 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 3.956 | 4.280 | 0.87x | 19.24 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 3.923 | 4.304 | 1.29x | 46.25 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 3.989 | 4.537 | 1.91x | 82.28 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 3.939 | 4.260 | 0.97x | 29.37 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 4.029 | 4.740 | 1.87x | 82.27 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 4.581 | 5.203 | 2.77x | 154.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 3.966 | 4.382 | 1.29x | 48.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 4.576 | 5.224 | 2.74x | 154.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 5.450 | 6.051 | 4.17x | 298.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 3.959 | 4.482 | 1.94x | 86.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 5.454 | 5.991 | 4.17x | 298.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 7.220 | 7.822 | 5.98x | 586.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.