# PVR Router Regret Repair Screen

Status: `PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_NOT_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Bounded 500K-token router-regret repair screen on broad_nlp_train with official_like_dev evaluation. Final official bounded files are not used.

## Claim Gates

- all_variants_completed: `True`
- final_block_oracle_audits_present: `True`
- strict_top1_clean_for_completed_pvr: `True`
- winner_improves_eval: `False`
- winner_reduces_final_block_regret: `False`
- official_final_files_used: `False`

## Result Table

| variant | regret w | KL w | final eval | mean eval | final train | train regret | train oracle rate | final-block regret | oracle rate | top2 rate | Top1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| pvr_router_regret_repair_baseline_no_regret_300m_1m_confirm | 0.0 | 0.0 | 12.02232837677002 | 17.494673490524292 | 4.959540367126465 | None | None | 0.5773689632301934 | 0.296875 | 0.40848214285714285 | True |
| pvr_router_regret_repair_regret0p01_300m_1m_confirm | 0.01 | 0.0 | 12.069253921508789 | 17.79215121269226 | 4.853570938110352 | 0.43504470586776733 | 0.3515625 | 0.36896729755348395 | 0.36830357142857145 | 0.5044642857142857 | True |

## Winner

Winner: `pvr_router_regret_repair_baseline_no_regret_300m_1m_confirm`
Eval delta vs baseline: `0.0`
Final-block regret delta vs baseline: `0.0`

## Interpretation Boundary

This is a bounded final-block regret repair screen. It does not prove full-network router repair, official benchmark advantage, or teacher independence.
