# PVR-EC Root Baseline Matrix

**Status:** PVR_EC_ROOT_BASELINE_MATRIX_RECORDED

**Statuses:** PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_CAPACITY_NOT_PRIMARY_BLOCKER, PVR_EC_LATENCY_VARIANCE_BLOCKER, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

| Model | Count | Loss | Accuracy | p95/p50 |
|---|---:|---:|---:|---:|
| fixed_moe_vectorized | 54 | 3.3168480456749228 | 0.013055277902018212 | 1.0505546600425062 |
| pvr_ec_deploy_top1 | 32 | 3.494287111534504 | 0.01866195964052158 | 1.1401722000325307 |
| pvr_ec_ownership_top1_delta_medium | 52 | 3.269205698241981 | 0.023378428322742197 | 1.1070127303474813 |
| pvr_ec_ownership_top1_delta_large | 42 | 2.7213443982015764 | 0.027879236118890025 | 1.4047667320494404 |
| pvr_ec_ownership_top1_full_expert_ffn_control | 54 | 3.354046075317411 | 0.014747656035358537 | 1.1017553835238882 |
| pvr_ec_ownership_top1_delta_small | 16 | 0.44623174669686705 | 0.045237814207317054 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_25x | 16 | 0.45390737045090646 | 0.07354605605085013 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_5x | 16 | 0.45332588984941447 | 0.07269471356208632 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_1_0x | 18 | 1.0112792746750294 | 0.04635833279061893 | 1.0516417942576468 |
| pvr_ec_ownership_top1_delta_rank_8 | 16 | 0.4452838960569352 | 0.0686038787474148 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_16 | 16 | 0.4435656647353122 | 0.06873072569665975 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_32 | 16 | 0.4462317478222152 | 0.045237814207317054 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_64 | 16 | 0.45390736940316856 | 0.07354605605085013 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_128 | 16 | 0.4533294859187057 | 0.07267324177698795 | 1.0 |