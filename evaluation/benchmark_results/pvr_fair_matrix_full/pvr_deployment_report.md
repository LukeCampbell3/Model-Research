# PVR-EC Deployment Report

**Status:** PVR_EC_DEPLOY_CANDIDATE

| Model | Mode | Batch | Seq | p50 ms | p95 ms | Slowdown vs fixed_vec | Loss | QPM | Q/Mem | Expert Exec |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| fixed_moe_looped_reference | off | 1 | 32 | 10.660 | 10.971 | 3.00x | 5.5341 | 0.000000 | 0.000000 | LOOPED |
| fixed_moe_looped_reference | off | 1 | 64 | 10.719 | 10.964 | 2.98x | 5.6102 | 0.000000 | 0.000000 | LOOPED |
| fixed_moe_looped_reference | off | 1 | 128 | 11.419 | 11.876 | 3.27x | 5.5984 | 0.000000 | 0.000000 | LOOPED |
| fixed_moe_looped_reference | off | 8 | 32 | 12.581 | 13.813 | 3.25x | 5.5621 | 0.000620 | 0.000522 | LOOPED |
| fixed_moe_looped_reference | off | 8 | 64 | 11.343 | 11.912 | 2.17x | 5.5665 | 0.000687 | 0.000460 | LOOPED |
| fixed_moe_looped_reference | off | 8 | 128 | 11.424 | 12.077 | 1.44x | 5.5760 | 0.000597 | 0.000326 | LOOPED |
| fixed_moe_looped_reference | off | 32 | 32 | 11.399 | 11.642 | 1.43x | 5.5774 | 0.000172 | 0.000093 | LOOPED |
| fixed_moe_looped_reference | off | 32 | 64 | 11.468 | 11.635 | 0.87x | 5.5678 | 0.000430 | 0.000168 | LOOPED |
| fixed_moe_looped_reference | off | 32 | 128 | 11.227 | 11.669 | 0.48x | 5.5758 | 0.000392 | 0.000095 | LOOPED |
| fixed_moe_looped_reference | off | 64 | 32 | 11.366 | 11.675 | 0.86x | 5.5796 | 0.000260 | 0.000091 | LOOPED |
| fixed_moe_looped_reference | off | 64 | 64 | 11.362 | 11.724 | 0.48x | 5.5743 | 0.000325 | 0.000079 | LOOPED |
| fixed_moe_looped_reference | off | 64 | 128 | 11.730 | 11.953 | 0.26x | 5.5738 | 0.000366 | 0.000053 | LOOPED |
| fixed_moe_vectorized | off | 1 | 32 | 3.519 | 3.757 | 1.00x | 5.5341 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 64 | 3.537 | 3.942 | 1.00x | 5.6102 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 1 | 128 | 3.464 | 3.594 | 1.00x | 5.5984 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 32 | 3.783 | 4.179 | 1.00x | 5.5621 | 0.002019 | 0.000038 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 64 | 5.128 | 5.623 | 1.00x | 5.5665 | 0.001492 | 0.000019 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 8 | 128 | 7.882 | 8.239 | 1.00x | 5.5760 | 0.000863 | 0.000009 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 32 | 7.823 | 8.250 | 1.00x | 5.5774 | 0.000247 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 64 | 13.145 | 13.395 | 1.00x | 5.5678 | 0.000373 | 0.000003 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 32 | 128 | 23.630 | 23.801 | 1.00x | 5.5758 | 0.000186 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 32 | 13.085 | 13.362 | 1.00x | 5.5796 | 0.000224 | 0.000002 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 64 | 23.247 | 23.747 | 1.00x | 5.5743 | 0.000157 | 0.000001 | FULLY_VECTORIZED |
| fixed_moe_vectorized | off | 64 | 128 | 44.115 | 44.334 | 1.00x | 5.5738 | 0.000097 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 32 | 2.879 | 3.162 | 0.82x | 5.5958 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 64 | 2.839 | 3.055 | 0.80x | 5.6107 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 1 | 128 | 2.838 | 3.142 | 0.83x | 5.5763 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 32 | 2.875 | 3.001 | 0.74x | 5.5515 | 0.001356 | 0.000140 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 64 | 2.821 | 2.979 | 0.54x | 5.5698 | 0.001373 | 0.000086 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 8 | 128 | 2.839 | 3.142 | 0.36x | 5.5633 | 0.001695 | 0.000060 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 32 | 2.814 | 2.916 | 0.36x | 5.5835 | 0.001380 | 0.000048 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 64 | 3.451 | 3.819 | 0.27x | 5.5705 | 0.000974 | 0.000023 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 32 | 128 | 4.339 | 4.833 | 0.19x | 5.5717 | 0.001090 | 0.000017 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 32 | 3.419 | 3.811 | 0.27x | 5.5738 | 0.000973 | 0.000022 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 64 | 4.424 | 4.851 | 0.19x | 5.5748 | 0.000868 | 0.000013 | FULLY_VECTORIZED |
| pvr_ec_deploy_top1 | top1 | 64 | 128 | 6.215 | 6.765 | 0.14x | 5.5720 | 0.000577 | 0.000006 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 1 | 32 | 3.059 | 3.109 | 0.86x | 5.5955 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 1 | 64 | 2.993 | 3.271 | 0.85x | 5.6115 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 1 | 128 | 2.983 | 3.246 | 0.87x | 5.5719 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 8 | 32 | 3.010 | 3.405 | 0.80x | 5.5514 | 0.001269 | 0.000065 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 8 | 64 | 3.400 | 3.630 | 0.64x | 5.5670 | 0.001166 | 0.000036 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 8 | 128 | 4.296 | 4.494 | 0.54x | 5.5628 | 0.001132 | 0.000023 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 32 | 4.338 | 4.715 | 0.56x | 5.5837 | 0.001104 | 0.000023 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 64 | 5.930 | 6.433 | 0.46x | 5.5706 | 0.000653 | 0.000010 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 32 | 128 | 8.585 | 8.940 | 0.37x | 5.5715 | 0.000567 | 0.000006 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 64 | 32 | 5.325 | 5.821 | 0.41x | 5.5738 | 0.000632 | 0.000008 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 64 | 64 | 8.059 | 8.281 | 0.34x | 5.5748 | 0.000424 | 0.000004 | FULLY_VECTORIZED |
| pvr_ec_deploy_top2 | top2 | 64 | 128 | 13.411 | 13.571 | 0.30x | 5.5720 | 0.000283 | 0.000002 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 1 | 32 | 3.185 | 3.586 | 0.92x | 5.5939 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 1 | 64 | 3.213 | 3.408 | 0.90x | 5.6081 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 1 | 128 | 3.196 | 3.232 | 0.92x | 5.5722 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 8 | 32 | 3.160 | 3.555 | 0.84x | 5.5527 | 0.001208 | 0.000036 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 8 | 64 | 3.462 | 3.828 | 0.67x | 5.5668 | 0.001109 | 0.000019 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 8 | 128 | 4.898 | 5.603 | 0.63x | 5.5613 | 0.001371 | 0.000017 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 32 | 32 | 4.803 | 5.408 | 0.62x | 5.5842 | 0.000989 | 0.000012 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 32 | 64 | 7.471 | 7.835 | 0.57x | 5.5704 | 0.000521 | 0.000005 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 32 | 128 | 12.889 | 13.022 | 0.54x | 5.5710 | 0.000439 | 0.000004 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 64 | 32 | 7.399 | 7.930 | 0.58x | 5.5739 | 0.000324 | 0.000003 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 64 | 64 | 12.904 | 13.058 | 0.55x | 5.5746 | 0.000286 | 0.000002 | FULLY_VECTORIZED |
| pvr_ec_deploy_bucketed | bucketed | 64 | 128 | 23.583 | 23.757 | 0.53x | 5.5724 | 0.000171 | 0.000001 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 1 | 32 | 3.028 | 3.319 | 0.87x | 5.5961 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 1 | 64 | 3.025 | 3.281 | 0.85x | 5.6093 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 1 | 128 | 3.031 | 3.507 | 0.90x | 5.5698 | 0.000000 | 0.000000 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 8 | 32 | 3.170 | 3.650 | 0.84x | 5.5524 | 0.001198 | 0.000036 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 8 | 64 | 3.813 | 4.347 | 0.75x | 5.5676 | 0.000996 | 0.000019 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 8 | 128 | 5.314 | 5.415 | 0.67x | 5.5630 | 0.001105 | 0.000015 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 32 | 32 | 5.303 | 5.795 | 0.69x | 5.5843 | 0.000901 | 0.000012 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 32 | 64 | 8.052 | 8.384 | 0.62x | 5.5703 | 0.000363 | 0.000004 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 32 | 128 | 13.337 | 13.600 | 0.56x | 5.5714 | 0.000368 | 0.000003 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 64 | 32 | 7.957 | 8.251 | 0.61x | 5.5740 | 0.000488 | 0.000005 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 64 | 64 | 13.300 | 13.494 | 0.57x | 5.5746 | 0.000221 | 0.000002 | FULLY_VECTORIZED |
| pvr_ec_deploy_dense_masked_control | dense_masked_control | 64 | 128 | 23.811 | 24.720 | 0.54x | 5.5718 | 0.000168 | 0.000001 | FULLY_VECTORIZED |

Hard runtime branching is disabled. Branch tickets are disabled in the deployment hot path.