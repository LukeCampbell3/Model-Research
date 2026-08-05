# PVR Router Regret Repair Screen

Status: `PVR_ROUTER_REGRET_REPAIR_SCREEN_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Bounded 500K-token router-regret repair screen on broad_nlp_train with official_like_dev evaluation. Final official bounded files are not used.

## Claim Gates

- all_variants_completed: `True`
- final_block_oracle_audits_present: `True`
- strict_top1_clean_for_completed_pvr: `True`
- winner_improves_eval: `True`
- winner_reduces_final_block_regret: `True`
- official_final_files_used: `False`

## Result Table

| variant | regret w | KL w | final eval | mean eval | final train | train regret | train oracle rate | final-block regret | oracle rate | top2 rate | Top1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| pvr_router_regret_repair_baseline_no_regret_300m | 0.0 | 0.0 | 22.264923095703125 | 24.669730186462402 | 5.85903787612915 | None | None | 0.6765053497760424 | 0.24776785714285715 | 0.31473214285714285 | True |
| pvr_router_regret_repair_regret0p001_300m | 0.001 | 0.0 | 20.462602615356445 | 22.507500648498535 | 6.05907678604126 | 0.5426557064056396 | 0.3046875 | 0.817077138109458 | 0.23883928571428573 | 0.30357142857142855 | True |
| pvr_router_regret_repair_regret0p005_300m | 0.005 | 0.0 | 18.578182220458984 | 21.39474391937256 | 5.8607892990112305 | 0.5856536626815796 | 0.142578125 | 0.5073771975295196 | 0.27232142857142855 | 0.3794642857142857 | True |
| pvr_router_regret_repair_regret0p01_300m | 0.01 | 0.0 | 18.416173934936523 | 22.347695350646973 | 6.124988079071045 | 0.5783126354217529 | 0.169921875 | 0.5959349535346519 | 0.19419642857142858 | 0.3325892857142857 | True |
| pvr_router_regret_repair_kl0p005_300m | 0.0 | 0.005 | 22.01137351989746 | 24.884034156799316 | 6.453537464141846 | 0.6223104000091553 | 0.435546875 | 0.8571702269737541 | 0.29910714285714285 | 0.3705357142857143 | True |
| pvr_router_regret_repair_regret0p005_kl0p001_300m | 0.005 | 0.001 | 24.9868106842041 | 27.40040111541748 | 6.035043239593506 | 0.6082741618156433 | 0.1630859375 | 0.6753054587065728 | 0.16071428571428573 | 0.18973214285714285 | True |

## Winner

Winner: `pvr_router_regret_repair_regret0p01_300m`
Eval delta vs baseline: `-3.8487491607666016`
Final-block regret delta vs baseline: `-0.08057039624139051`

## Interpretation Boundary

This is a bounded final-block regret repair screen. It does not prove full-network router repair, official benchmark advantage, or teacher independence.
