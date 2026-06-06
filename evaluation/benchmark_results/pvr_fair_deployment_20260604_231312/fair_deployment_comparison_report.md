# Fair Deployment Comparison

**Status:** PVR_EC_DEPLOY_CANDIDATE

| Model | Batch | Seq | p50 ms | p95 ms | Speedup vs fixed_vec | Max Mem MB | Loss | Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_moe_looped_reference | 1 | 32 | 10.660 | 10.971 | 0.33x | 13.20 | 5.5341 | 0.0000 |
| fixed_moe_looped_reference | 1 | 64 | 10.719 | 10.964 | 0.34x | 13.46 | 5.6102 | 0.0000 |
| fixed_moe_looped_reference | 1 | 128 | 11.419 | 11.876 | 0.31x | 13.96 | 5.5984 | 0.0000 |
| fixed_moe_looped_reference | 8 | 32 | 12.581 | 13.813 | 0.31x | 14.96 | 5.5621 | 0.0078 |
| fixed_moe_looped_reference | 8 | 64 | 11.343 | 11.912 | 0.46x | 16.98 | 5.5665 | 0.0078 |
| fixed_moe_looped_reference | 8 | 128 | 11.424 | 12.077 | 0.69x | 21.00 | 5.5760 | 0.0068 |
| fixed_moe_looped_reference | 32 | 32 | 11.399 | 11.642 | 0.70x | 21.00 | 5.5774 | 0.0020 |
| fixed_moe_looped_reference | 32 | 64 | 11.468 | 11.635 | 1.15x | 29.05 | 5.5678 | 0.0049 |
| fixed_moe_looped_reference | 32 | 128 | 11.227 | 11.669 | 2.10x | 46.14 | 5.5758 | 0.0044 |
| fixed_moe_looped_reference | 64 | 32 | 11.366 | 11.675 | 1.16x | 32.06 | 5.5796 | 0.0029 |
| fixed_moe_looped_reference | 64 | 64 | 11.362 | 11.724 | 2.08x | 46.14 | 5.5743 | 0.0037 |
| fixed_moe_looped_reference | 64 | 128 | 11.730 | 11.953 | 3.78x | 80.33 | 5.5738 | 0.0043 |
| fixed_moe_vectorized | 1 | 32 | 3.519 | 3.757 | 1.00x | 49.29 | 5.5341 | 0.0000 |
| fixed_moe_vectorized | 1 | 64 | 3.537 | 3.942 | 1.00x | 61.59 | 5.6102 | 0.0000 |
| fixed_moe_vectorized | 1 | 128 | 3.464 | 3.594 | 1.00x | 110.22 | 5.5984 | 0.0000 |
| fixed_moe_vectorized | 8 | 32 | 3.783 | 4.179 | 1.00x | 207.48 | 5.5621 | 0.0078 |
| fixed_moe_vectorized | 8 | 64 | 5.128 | 5.623 | 1.00x | 402.01 | 5.5665 | 0.0078 |
| fixed_moe_vectorized | 8 | 128 | 7.882 | 8.239 | 1.00x | 791.06 | 5.5760 | 0.0068 |
| fixed_moe_vectorized | 32 | 32 | 7.823 | 8.250 | 1.00x | 791.06 | 5.5774 | 0.0020 |
| fixed_moe_vectorized | 32 | 64 | 13.145 | 13.395 | 1.00x | 1569.16 | 5.5678 | 0.0049 |
| fixed_moe_vectorized | 32 | 128 | 23.630 | 23.801 | 1.00x | 3125.36 | 5.5758 | 0.0044 |
| fixed_moe_vectorized | 64 | 32 | 13.085 | 13.362 | 1.00x | 1572.17 | 5.5796 | 0.0029 |
| fixed_moe_vectorized | 64 | 64 | 23.247 | 23.747 | 1.00x | 3125.36 | 5.5743 | 0.0037 |
| fixed_moe_vectorized | 64 | 128 | 44.115 | 44.334 | 1.00x | 6237.77 | 5.5738 | 0.0043 |
| pvr_ec_deploy_top1 | 1 | 32 | 2.879 | 3.162 | 1.21x | 24.45 | 5.5958 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 64 | 2.839 | 3.055 | 1.25x | 14.64 | 5.6107 | 0.0000 |
| pvr_ec_deploy_top1 | 1 | 128 | 2.838 | 3.142 | 1.20x | 19.05 | 5.5763 | 0.0000 |
| pvr_ec_deploy_top1 | 8 | 32 | 2.875 | 3.001 | 1.34x | 27.86 | 5.5515 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 64 | 2.821 | 2.979 | 1.84x | 45.50 | 5.5698 | 0.0039 |
| pvr_ec_deploy_top1 | 8 | 128 | 2.839 | 3.142 | 2.75x | 80.77 | 5.5633 | 0.0049 |
| pvr_ec_deploy_top1 | 32 | 32 | 2.814 | 2.916 | 2.79x | 80.77 | 5.5835 | 0.0039 |
| pvr_ec_deploy_top1 | 32 | 64 | 3.451 | 3.819 | 3.73x | 151.31 | 5.5705 | 0.0034 |
| pvr_ec_deploy_top1 | 32 | 128 | 4.339 | 4.833 | 5.26x | 292.39 | 5.5717 | 0.0049 |
| pvr_ec_deploy_top1 | 64 | 32 | 3.419 | 3.811 | 3.72x | 154.32 | 5.5738 | 0.0034 |
| pvr_ec_deploy_top1 | 64 | 64 | 4.424 | 4.851 | 5.19x | 292.39 | 5.5748 | 0.0039 |
| pvr_ec_deploy_top1 | 64 | 128 | 6.215 | 6.765 | 6.95x | 574.54 | 5.5720 | 0.0037 |
| pvr_ec_deploy_top2 | 1 | 32 | 3.059 | 3.109 | 1.16x | 28.45 | 5.5955 | 0.0000 |
| pvr_ec_deploy_top2 | 1 | 64 | 2.993 | 3.271 | 1.18x | 22.64 | 5.6115 | 0.0000 |
| pvr_ec_deploy_top2 | 1 | 128 | 2.983 | 3.246 | 1.15x | 35.05 | 5.5719 | 0.0000 |
| pvr_ec_deploy_top2 | 8 | 32 | 3.010 | 3.405 | 1.26x | 59.87 | 5.5514 | 0.0039 |
| pvr_ec_deploy_top2 | 8 | 64 | 3.400 | 3.630 | 1.56x | 109.51 | 5.5670 | 0.0039 |
| pvr_ec_deploy_top2 | 8 | 128 | 4.296 | 4.494 | 1.84x | 208.78 | 5.5628 | 0.0049 |
| pvr_ec_deploy_top2 | 32 | 32 | 4.338 | 4.715 | 1.79x | 208.78 | 5.5837 | 0.0049 |
| pvr_ec_deploy_top2 | 32 | 64 | 5.930 | 6.433 | 2.19x | 407.33 | 5.5706 | 0.0039 |
| pvr_ec_deploy_top2 | 32 | 128 | 8.585 | 8.940 | 2.74x | 804.43 | 5.5715 | 0.0049 |
| pvr_ec_deploy_top2 | 64 | 32 | 5.325 | 5.821 | 2.42x | 410.35 | 5.5738 | 0.0034 |
| pvr_ec_deploy_top2 | 64 | 64 | 8.059 | 8.281 | 2.90x | 804.43 | 5.5748 | 0.0034 |
| pvr_ec_deploy_top2 | 64 | 128 | 13.411 | 13.571 | 3.30x | 1598.64 | 5.5720 | 0.0038 |
| pvr_ec_deploy_bucketed | 1 | 32 | 3.185 | 3.586 | 1.09x | 34.52 | 5.5939 | 0.0000 |
| pvr_ec_deploy_bucketed | 1 | 64 | 3.213 | 3.408 | 1.11x | 34.77 | 5.6081 | 0.0000 |
| pvr_ec_deploy_bucketed | 1 | 128 | 3.196 | 3.232 | 1.09x | 59.31 | 5.5722 | 0.0000 |
| pvr_ec_deploy_bucketed | 8 | 32 | 3.160 | 3.555 | 1.20x | 108.38 | 5.5527 | 0.0039 |
| pvr_ec_deploy_bucketed | 8 | 64 | 3.462 | 3.828 | 1.49x | 206.52 | 5.5668 | 0.0039 |
| pvr_ec_deploy_bucketed | 8 | 128 | 4.898 | 5.603 | 1.59x | 402.82 | 5.5613 | 0.0068 |
| pvr_ec_deploy_bucketed | 32 | 32 | 4.803 | 5.408 | 1.60x | 402.82 | 5.5842 | 0.0049 |
| pvr_ec_deploy_bucketed | 32 | 64 | 7.471 | 7.835 | 1.75x | 795.41 | 5.5704 | 0.0039 |
| pvr_ec_deploy_bucketed | 32 | 128 | 12.889 | 13.022 | 1.84x | 1580.58 | 5.5710 | 0.0056 |
| pvr_ec_deploy_bucketed | 64 | 32 | 7.399 | 7.930 | 1.73x | 798.42 | 5.5739 | 0.0024 |
| pvr_ec_deploy_bucketed | 64 | 64 | 12.904 | 13.058 | 1.82x | 1580.58 | 5.5746 | 0.0037 |
| pvr_ec_deploy_bucketed | 64 | 128 | 23.583 | 23.757 | 1.87x | 3150.93 | 5.5724 | 0.0040 |
| pvr_ec_deploy_dense_masked_control | 1 | 32 | 3.028 | 3.319 | 1.16x | 34.51 | 5.5961 | 0.0000 |
| pvr_ec_deploy_dense_masked_control | 1 | 64 | 3.025 | 3.281 | 1.17x | 34.77 | 5.6093 | 0.0000 |
| pvr_ec_deploy_dense_masked_control | 1 | 128 | 3.031 | 3.507 | 1.11x | 59.30 | 5.5698 | 0.0000 |
| pvr_ec_deploy_dense_masked_control | 8 | 32 | 3.170 | 3.650 | 1.19x | 108.37 | 5.5524 | 0.0039 |
| pvr_ec_deploy_dense_masked_control | 8 | 64 | 3.813 | 4.347 | 1.34x | 206.51 | 5.5676 | 0.0039 |
| pvr_ec_deploy_dense_masked_control | 8 | 128 | 5.314 | 5.415 | 1.49x | 402.78 | 5.5630 | 0.0059 |
| pvr_ec_deploy_dense_masked_control | 32 | 32 | 5.303 | 5.795 | 1.46x | 402.78 | 5.5843 | 0.0049 |
| pvr_ec_deploy_dense_masked_control | 32 | 64 | 8.052 | 8.384 | 1.62x | 795.33 | 5.5703 | 0.0029 |
| pvr_ec_deploy_dense_masked_control | 32 | 128 | 13.337 | 13.600 | 1.78x | 1580.43 | 5.5714 | 0.0049 |
| pvr_ec_deploy_dense_masked_control | 64 | 32 | 7.957 | 8.251 | 1.63x | 798.35 | 5.5740 | 0.0039 |
| pvr_ec_deploy_dense_masked_control | 64 | 64 | 13.300 | 13.494 | 1.76x | 1580.43 | 5.5746 | 0.0029 |
| pvr_ec_deploy_dense_masked_control | 64 | 128 | 23.811 | 24.720 | 1.84x | 3150.64 | 5.5718 | 0.0040 |

Fair speedup claims use `fixed_moe_vectorized` as the baseline when available.