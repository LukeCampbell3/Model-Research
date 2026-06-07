# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.640 | 3.982 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.786 | 4.338 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.699 | 4.101 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.650 | 3.978 | 1.00x | 5.5746 | 0.002114 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.685 | 6.205 | 1.00x | 5.5720 | 0.000683 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 8.714 | 9.849 | 1.00x | 5.5459 | 0.000997 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 4.214 | 4.911 | 1.00x | 5.5560 | 0.000916 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 8.648 | 9.885 | 1.00x | 5.5819 | 0.000444 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 14.566 | 15.913 | 1.00x | 5.5689 | 0.000165 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.655 | 6.188 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 14.576 | 16.267 | 1.00x | 5.5686 | 0.000230 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 26.523 | 28.228 | 1.00x | 5.5754 | 0.000127 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 8.617 | 9.507 | 1.00x | 5.5833 | 0.000225 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 26.734 | 28.455 | 1.00x | 5.5759 | 0.000181 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 51.114 | 51.526 | 1.00x | 5.5728 | 0.000070 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 4.025 | 4.531 | 1.10x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 4.419 | 4.806 | 1.15x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 4.395 | 4.849 | 1.18x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 4.499 | 5.199 | 1.23x | 5.5745 | 0.001716 | 0.000508 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 4.387 | 4.786 | 0.77x | 5.5899 | 0.000887 | 0.000122 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 4.382 | 5.761 | 0.51x | 5.5786 | 0.001944 | 0.000162 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 4.320 | 4.938 | 1.03x | 5.5682 | 0.000888 | 0.000154 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 4.360 | 5.322 | 0.51x | 5.5908 | 0.000879 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 4.530 | 5.178 | 0.31x | 5.5772 | 0.000533 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 4.401 | 5.132 | 0.79x | 5.5827 | 0.000436 | 0.000048 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 4.524 | 5.424 | 0.31x | 5.5750 | 0.000855 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 5.123 | 5.748 | 0.19x | 5.5767 | 0.000660 | 0.000018 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 4.264 | 4.857 | 0.50x | 5.5811 | 0.000895 | 0.000054 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.883 | 5.727 | 0.18x | 5.5764 | 0.000892 | 0.000023 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 6.171 | 6.997 | 0.12x | 5.5769 | 0.000567 | 0.000010 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 5.019 | 5.488 | 1.38x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 5.273 | 6.083 | 1.38x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 5.327 | 6.012 | 1.44x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 5.312 | 6.029 | 1.46x | 5.5744 | 0.001452 | 0.000395 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 5.439 | 6.709 | 0.98x | 5.5785 | 0.000698 | 0.000081 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 5.419 | 5.934 | 0.62x | 5.5624 | 0.001604 | 0.000101 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 5.463 | 6.298 | 1.30x | 5.5474 | 0.000704 | 0.000115 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 5.647 | 6.164 | 0.64x | 5.5935 | 0.000692 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 6.308 | 7.278 | 0.43x | 5.5783 | 0.000382 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 5.662 | 6.569 | 1.01x | 5.5807 | 0.000339 | 0.000034 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 6.252 | 7.304 | 0.43x | 5.5685 | 0.000608 | 0.000024 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 7.374 | 8.097 | 0.28x | 5.5730 | 0.000458 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 5.343 | 6.117 | 0.63x | 5.5710 | 0.000717 | 0.000037 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 7.342 | 8.324 | 0.28x | 5.5680 | 0.000592 | 0.000014 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 9.397 | 10.582 | 0.19x | 5.5752 | 0.000371 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.