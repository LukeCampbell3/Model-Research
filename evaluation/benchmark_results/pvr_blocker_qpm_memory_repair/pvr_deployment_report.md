# PVR-EC Deployment Report

**Status:** PARTIAL_PVR_EC_FAIR_DEPLOYMENT_VALIDATION

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_vectorized | off | 1 | 16 | 3.756 | 4.514 | 1.00x | 5.6273 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.905 | 4.803 | 1.00x | 5.5621 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.846 | 4.531 | 1.00x | 5.5757 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 16 | 3.694 | 4.316 | 1.00x | 5.5746 | 0.002049 | 0.000071 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.750 | 6.888 | 1.00x | 5.5720 | 0.000663 | 0.000010 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 8.710 | 10.096 | 1.00x | 5.5459 | 0.000986 | 0.000011 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 16 | 4.241 | 4.680 | 1.00x | 5.5560 | 0.000911 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 64 | 8.785 | 9.960 | 1.00x | 5.5819 | 0.000439 | 0.000005 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 16 | 128 | 14.679 | 16.064 | 1.00x | 5.5689 | 0.000164 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 16 | 5.591 | 6.292 | 1.00x | 5.5648 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 14.692 | 15.931 | 1.00x | 5.5686 | 0.000230 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 26.802 | 28.020 | 1.00x | 5.5754 | 0.000127 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 16 | 8.767 | 9.928 | 1.00x | 5.5833 | 0.000219 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 26.746 | 28.114 | 1.00x | 5.5759 | 0.000181 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 51.366 | 52.142 | 1.00x | 5.5728 | 0.000069 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 16 | 4.352 | 4.899 | 1.14x | 5.6673 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 4.638 | 5.241 | 1.17x | 5.5747 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 4.706 | 5.325 | 1.22x | 5.5885 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 16 | 4.726 | 5.229 | 1.25x | 5.5745 | 0.001645 | 0.000527 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 4.643 | 5.115 | 0.81x | 5.5899 | 0.000823 | 0.000131 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 4.639 | 5.229 | 0.52x | 5.5786 | 0.001881 | 0.000177 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 16 | 4.756 | 5.188 | 1.12x | 5.5682 | 0.000814 | 0.000187 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 64 | 5.088 | 6.245 | 0.58x | 5.5908 | 0.000753 | 0.000079 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 16 | 128 | 4.972 | 5.789 | 0.34x | 5.5772 | 0.000485 | 0.000027 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 16 | 4.898 | 5.790 | 0.88x | 5.5827 | 0.000391 | 0.000061 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 5.251 | 6.239 | 0.36x | 5.5750 | 0.000730 | 0.000044 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 6.039 | 7.729 | 0.23x | 5.5767 | 0.000547 | 0.000020 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 16 | 5.161 | 6.259 | 0.59x | 5.5811 | 0.000737 | 0.000072 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 5.449 | 6.223 | 0.20x | 5.5764 | 0.000798 | 0.000026 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 6.735 | 7.679 | 0.13x | 5.5769 | 0.000516 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 16 | 4.499 | 5.083 | 1.19x | 5.5354 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 64 | 4.601 | 5.115 | 1.17x | 5.5647 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 1 | 128 | 4.859 | 5.745 | 1.30x | 5.5705 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 16 | 4.677 | 5.274 | 1.23x | 5.5744 | 0.001660 | 0.000406 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 64 | 5.018 | 5.735 | 0.85x | 5.5785 | 0.000780 | 0.000084 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 8 | 128 | 4.780 | 5.308 | 0.54x | 5.5624 | 0.001819 | 0.000107 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 16 | 4.777 | 5.771 | 1.14x | 5.5474 | 0.000796 | 0.000133 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 64 | 4.790 | 5.489 | 0.55x | 5.5935 | 0.000805 | 0.000047 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 16 | 128 | 5.435 | 6.262 | 0.37x | 5.5783 | 0.000440 | 0.000016 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 16 | 4.703 | 5.457 | 0.84x | 5.5807 | 0.000410 | 0.000040 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 64 | 5.497 | 6.397 | 0.38x | 5.5685 | 0.000698 | 0.000025 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 32 | 128 | 6.348 | 7.246 | 0.24x | 5.5730 | 0.000529 | 0.000011 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 16 | 4.617 | 5.164 | 0.52x | 5.5710 | 0.000838 | 0.000045 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 64 | 6.426 | 7.261 | 0.24x | 5.5680 | 0.000673 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_ownership_top1_final_candidate_v1 | top1 | 64 | 128 | 8.394 | 9.286 | 0.17x | 5.5752 | 0.000418 | 0.000006 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.