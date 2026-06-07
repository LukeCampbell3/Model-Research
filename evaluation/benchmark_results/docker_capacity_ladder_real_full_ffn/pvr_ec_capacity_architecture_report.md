# PVR-EC Capacity Architecture Report

**Status:** PVR_EC_FULL_EXPERT_CONTROL_DISTINCT

| Model | Expert Type | Architecture | Inner | Rank | Params/Expert | Fingerprint | Aliases |
|---|---|---|---:|---:|---:|---|---|
| fixed_moe_vectorized |  |  | 0 | 0 | 0 |  |  |
| pvr_ec_ownership_top1_delta_large | delta_large | delta_rank_128 | 128 | 128 | 33024 | 9d2b2c0fe2d58ef1 | pvr_ec_ownership_top1_delta_rank_128 |
| pvr_ec_ownership_top1_delta_medium | delta_medium | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_delta_rank_64 |
| pvr_ec_ownership_top1_delta_rank_128 | delta_rank_128 | delta_rank_128 | 128 | 128 | 33024 | 9d2b2c0fe2d58ef1 | pvr_ec_ownership_top1_delta_large |
| pvr_ec_ownership_top1_delta_rank_16 | delta_rank_16 | delta_rank_16 | 16 | 16 | 4240 | 3c96380c7cd45fb1 |  |
| pvr_ec_ownership_top1_delta_rank_32 | delta_rank_32 | delta_rank_32 | 32 | 32 | 8352 | 9d470ee716580c22 | pvr_ec_ownership_top1_delta_small |
| pvr_ec_ownership_top1_delta_rank_64 | delta_rank_64 | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_delta_medium |
| pvr_ec_ownership_top1_delta_rank_8 | delta_rank_8 | delta_rank_8 | 8 | 8 | 2184 | c3f7350b2934f41c |  |
| pvr_ec_ownership_top1_delta_small | delta_small | delta_rank_32 | 32 | 32 | 8352 | 9d470ee716580c22 | pvr_ec_ownership_top1_delta_rank_32 |
| pvr_ec_ownership_top1_full_expert_ffn_control | full_expert_ffn_control | full_expert_ffn | 256 | 0 | 65920 | a0944b3bc51b2c6b |  |
| pvr_ec_ownership_top1_micro_ffn_0_25x | micro_ffn_0_25x | micro_ffn_0_25x | 64 | 0 | 16576 | bee3debb70b57ff4 |  |
| pvr_ec_ownership_top1_micro_ffn_0_5x | micro_ffn_0_5x | micro_ffn_0_5x | 128 | 0 | 33024 | 4f5705698b024477 |  |
| pvr_ec_ownership_top1_micro_ffn_1_0x | micro_ffn_1_0x | micro_ffn_1_0x | 256 | 0 | 65920 | 380ab507f442d658 |  |