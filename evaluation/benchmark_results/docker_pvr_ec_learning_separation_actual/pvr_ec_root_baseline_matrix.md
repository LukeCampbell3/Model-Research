# PVR-EC Root Baseline Matrix

**Status:** PVR_EC_ROOT_BASELINE_MATRIX_RECORDED

**Statuses:** PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE, PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY, PVR_EC_ROOT_CAUSE_INCONCLUSIVE, PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER

| Model | Count | Loss | Accuracy | p95/p50 |
|---|---:|---:|---:|---:|
| fixed_moe_vectorized | 24 | 4.112198859453201 | 0.001595600217273221 | 1.0 |
| pvr_ec_ownership_top1_micro_ffn_0_5x | 24 | 4.1772849559783936 | 0.0 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_16 | 24 | 4.095242276787758 | 0.00027159152634437803 | 1.0 |
| pvr_ec_ownership_top1_delta_rank_64 | 24 | 4.177284985780716 | 0.0 | 1.0 |
| pvr_ec_learning_full | 16 | 4.177284926176071 | 0.0 | 1.0 |
| pvr_ec_learning_shared_only | 16 | 4.164788395166397 | 0.0003734383487235198 | 1.0 |
| pvr_ec_learning_sparse_only | 16 | 4.186367452144623 | 0.0 | 1.0 |
| pvr_ec_learning_shared_scale_0_5 | 16 | 4.18154564499855 | 0.0 | 1.0 |
| pvr_ec_learning_expert_delta_scale_2_0 | 16 | 4.184465050697327 | 0.0 | 1.0 |
| pvr_ec_ownership_top1_delayed_candidate | 24 | 4.177284806966782 | 0.0 | 1.0 |