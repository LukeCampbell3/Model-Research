# PVR-EC Capacity Architecture Report

**Status:** PENDING_PVR_EC_CAPACITY_FAIRNESS_AUDIT

| Model | Expert Type | Architecture | Inner | Rank | Params/Expert | Fingerprint | Aliases |
|---|---|---|---:|---:|---:|---|---|
| fixed_moe_vectorized |  |  | 0 | 0 | 0 |  |  |
| pvr_ec_ownership_top1_delta_rank_16 | delta_rank_16 | delta_rank_16 | 16 | 16 | 4240 | 3c96380c7cd45fb1 |  |
| pvr_ec_ownership_top1_delta_rank_64 | delta_rank_64 | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_scale_schedule_1_to_4 |
| pvr_ec_ownership_top1_scale_schedule_1_to_4 | delta_rank_64 | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_delta_rank_64 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8 | delta_rank_64 | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_delta_rank_64 |
| pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4 | delta_rank_64 | delta_rank_64 | 64 | 64 | 16576 | bd2b089688f3661f | pvr_ec_ownership_top1_delta_rank_64 |