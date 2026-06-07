# PVR-EC-O Capacity Fairness Matrix

**Status:** PVR_EC_FULL_EXPERT_CONTROL_DISTINCT

| Model | Variant | Params | Active Params | Owners/Token | p50 ms | p95 ms | Loss | Acc | Q/ms |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pvr_ec_ownership_top1_delta_large | delta_large | 614,274 | 416,130 | 1.00 | 20.684 | 129.525 | 5.5773 | 0.0039 | 0.000111 |
| pvr_ec_ownership_top1_full_expert_ffn_control | full_expert_ffn | 877,442 | 481,922 | 1.00 | 134.351 | 210.790 | 5.5685 | 0.0044 | 0.000033 |
| pvr_ec_ownership_top1_micro_ffn_1_0x | micro_ffn_1.0x | 877,442 | 481,922 | 1.00 | 138.934 | 174.808 | 5.5726 | 0.0039 | 0.000028 |
| fixed_moe_vectorized |  | 1,001,092 | 1,001,092 | N/A | 41.633 | 43.547 | 5.5686 | 0.0034 | 0.000082 |

Promotion remains blocked until fairness and repeatability gates are clean.