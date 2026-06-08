# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.585 | 3.992 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.797 | 4.380 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.672 | 4.029 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.611 | 4.025 | 1.00x | 5.5746 | 0.002128 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.575 | 6.439 | 1.00x | 5.5720 | 0.000685 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 8.796 | 9.784 | 1.00x | 5.5459 | 0.000991 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 4.122 | 4.941 | 1.00x | 5.5560 | 0.000923 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 8.660 | 9.964 | 1.00x | 5.5819 | 0.000444 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 14.548 | 15.860 | 1.00x | 5.5689 | 0.000165 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.576 | 6.260 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 14.522 | 15.665 | 1.00x | 5.5686 | 0.000233 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 26.445 | 27.794 | 1.00x | 5.5754 | 0.000128 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 8.519 | 9.973 | 1.00x | 5.5833 | 0.000225 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 26.456 | 27.586 | 1.00x | 5.5759 | 0.000184 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 45.206 | 52.940 | 1.00x | 5.5728 | 0.000070 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 3.942 | 4.318 | 1.09x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 4.035 | 4.455 | 1.06x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 3.987 | 4.354 | 1.09x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 3.988 | 4.299 | 1.10x | 5.5745 | 0.001939 | 0.000527 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 4.060 | 4.584 | 0.73x | 5.5899 | 0.000941 | 0.000131 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 4.244 | 4.951 | 0.49x | 5.5786 | 0.002010 | 0.000177 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 4.353 | 4.830 | 1.04x | 5.5682 | 0.000886 | 0.000187 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 4.415 | 5.167 | 0.52x | 5.5908 | 0.000857 | 0.000079 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 4.388 | 5.138 | 0.31x | 5.5772 | 0.000537 | 0.000027 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 4.317 | 5.016 | 0.79x | 5.5827 | 0.000440 | 0.000061 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 4.582 | 5.394 | 0.32x | 5.5750 | 0.000827 | 0.000044 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 5.731 | 6.386 | 0.20x | 5.5767 | 0.000628 | 0.000020 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 4.277 | 4.840 | 0.50x | 5.5811 | 0.000894 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.820 | 5.326 | 0.19x | 5.5764 | 0.000893 | 0.000026 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 5.897 | 6.384 | 0.12x | 5.5769 | 0.000591 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 3.969 | 4.510 | 1.12x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 4.307 | 4.730 | 1.12x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 4.233 | 4.620 | 1.16x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 4.212 | 4.695 | 1.17x | 5.5744 | 0.001817 | 0.000406 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 4.266 | 4.666 | 0.76x | 5.5785 | 0.000904 | 0.000084 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 4.317 | 4.768 | 0.50x | 5.5624 | 0.002000 | 0.000107 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 4.591 | 5.530 | 1.12x | 5.5474 | 0.000828 | 0.000133 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 4.339 | 5.019 | 0.51x | 5.5935 | 0.000875 | 0.000047 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 4.943 | 5.657 | 0.34x | 5.5783 | 0.000479 | 0.000016 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 4.369 | 4.911 | 0.79x | 5.5807 | 0.000439 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 4.969 | 5.725 | 0.35x | 5.5685 | 0.000769 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 5.829 | 6.382 | 0.22x | 5.5730 | 0.000576 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 4.268 | 4.770 | 0.50x | 5.5710 | 0.000895 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 5.757 | 6.217 | 0.22x | 5.5680 | 0.000752 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 7.597 | 8.102 | 0.15x | 5.5752 | 0.000463 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.