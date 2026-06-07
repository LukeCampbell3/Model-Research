# Fair Deployment Comparison

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_vectorized | 1 | 16 | 3.640 | 3.982 | 1.00x | 25.12 | 5.6273 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.786 | 4.338 | 1.00x | 61.59 | 5.5621 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.699 | 4.101 | 1.00x | 110.22 | 5.5757 | 0.0000 |
| fixed_moe_vectorized | 8 | 16 | 3.650 | 3.978 | 1.00x | 110.22 | 5.5746 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.685 | 6.205 | 1.00x | 402.01 | 5.5720 | 0.0039 |
| fixed_moe_vectorized | 8 | 128 | 8.714 | 9.849 | 1.00x | 791.06 | 5.5459 | 0.0088 |
| fixed_moe_vectorized | 16 | 16 | 4.214 | 4.911 | 1.00x | 208.61 | 5.5560 | 0.0039 |
| fixed_moe_vectorized | 16 | 64 | 8.648 | 9.885 | 1.00x | 791.06 | 5.5819 | 0.0039 |
| fixed_moe_vectorized | 16 | 128 | 14.566 | 15.913 | 1.00x | 1569.16 | 5.5689 | 0.0024 |
| fixed_moe_vectorized | 32 | 16 | 5.655 | 6.188 | 1.00x | 404.27 | 5.5648 | 0.0000 |
| fixed_moe_vectorized | 32 | 64 | 14.576 | 16.267 | 1.00x | 1569.16 | 5.5686 | 0.0034 |
| fixed_moe_vectorized | 32 | 128 | 26.523 | 28.228 | 1.00x | 3125.36 | 5.5754 | 0.0034 |
| fixed_moe_vectorized | 64 | 16 | 8.617 | 9.507 | 1.00x | 795.58 | 5.5833 | 0.0020 |
| fixed_moe_vectorized | 64 | 64 | 26.734 | 28.455 | 1.00x | 3125.36 | 5.5759 | 0.0049 |
| fixed_moe_vectorized | 64 | 128 | 51.114 | 51.526 | 1.00x | 6237.77 | 5.5728 | 0.0035 |
| pvr_ec_deploy_top1 | 1 | 16 | 4.025 | 4.531 | 0.91x | 22.88 | 5.6673 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 4.419 | 4.806 | 0.87x | 12.62 | 5.5747 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 4.395 | 4.849 | 0.84x | 15.39 | 5.5885 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 16 | 4.499 | 5.199 | 0.81x | 15.39 | 5.5745 | 0.0078 |
| pvr_ec_deploy_top1 | 8 | 64 | 4.387 | 4.786 | 1.30x | 32.00 | 5.5899 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 4.382 | 5.761 | 1.95x | 54.15 | 5.5786 | 0.0088 |
| pvr_ec_deploy_top1 | 16 | 16 | 4.320 | 4.938 | 0.97x | 25.44 | 5.5682 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 64 | 4.360 | 5.322 | 1.98x | 54.15 | 5.5908 | 0.0039 |
| pvr_ec_deploy_top1 | 16 | 128 | 4.530 | 5.178 | 3.23x | 98.44 | 5.5772 | 0.0024 |
| pvr_ec_deploy_top1 | 32 | 16 | 4.401 | 5.132 | 1.27x | 41.01 | 5.5827 | 0.0020 |
| pvr_ec_deploy_top1 | 32 | 64 | 4.524 | 5.424 | 3.25x | 98.44 | 5.5750 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 128 | 5.123 | 5.748 | 5.18x | 187.03 | 5.5767 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 16 | 4.264 | 4.857 | 1.99x | 72.17 | 5.5811 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.883 | 5.727 | 5.47x | 187.03 | 5.5764 | 0.0044 |
| pvr_ec_deploy_top1 | 64 | 128 | 6.171 | 6.997 | 8.14x | 364.20 | 5.5769 | 0.0035 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 16 | 5.019 | 5.488 | 0.73x | 59.40 | 5.5354 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 64 | 5.273 | 6.083 | 0.73x | 15.02 | 5.5647 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 1 | 128 | 5.327 | 6.012 | 0.69x | 19.80 | 5.5705 | 0.0000 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 16 | 5.312 | 6.029 | 0.69x | 19.80 | 5.5744 | 0.0078 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 64 | 5.439 | 6.709 | 1.02x | 48.50 | 5.5785 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 8 | 128 | 5.419 | 5.934 | 1.61x | 86.78 | 5.5624 | 0.0088 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 16 | 5.463 | 6.298 | 0.77x | 33.87 | 5.5474 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 64 | 5.647 | 6.164 | 1.56x | 86.78 | 5.5935 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 16 | 128 | 6.308 | 7.278 | 2.31x | 163.32 | 5.5783 | 0.0024 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 16 | 5.662 | 6.569 | 0.99x | 57.52 | 5.5807 | 0.0020 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 64 | 6.252 | 7.304 | 2.31x | 163.32 | 5.5685 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 32 | 128 | 7.374 | 8.097 | 3.60x | 316.40 | 5.5730 | 0.0034 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 16 | 5.343 | 6.117 | 1.60x | 104.80 | 5.5710 | 0.0039 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 64 | 7.342 | 8.324 | 3.63x | 316.40 | 5.5680 | 0.0044 |
| pvr_ec_ownership_top1_final_candidate_v1 | 64 | 128 | 9.397 | 10.582 | 5.33x | 622.58 | 5.5752 | 0.0035 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.