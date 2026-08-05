# PVR Router Regret Repair 1M Refinement

Status: `PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_INCOMPLETE_OR_INVALID`
Decision: `PVR_ROUTER_REGRET_REPAIR_1M_REFINEMENT_NOT_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Bounded 1M-token lower-weight router-regret refinement on broad_nlp_train with official_like_dev evaluation. The 1M no-regret baseline is reused from the completed confirmation report; final official bounded files are not used.

## Baseline Reference

Variant: `pvr_router_regret_repair_baseline_no_regret_300m_1m_confirm`
Final eval: `12.02232837677002`
Final-block regret: `0.5773689632301934`

## Claim Gates

- all_variants_completed: `False`
- final_block_oracle_audits_present: `True`
- strict_top1_clean_for_completed_pvr: `True`
- winner_improves_eval: `False`
- winner_reduces_final_block_regret: `False`
- official_final_files_used: `False`

## Result Table

| variant | regret w | final eval | mean eval | final train | train regret | final-block regret | oracle rate | top2 rate | Top1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|

## Interpretation Boundary

This report tests whether lower regret weights can improve official-like LM loss while reducing final-block regret. It does not use final official bounded files and does not support teacher independence or architecture superiority by itself.
