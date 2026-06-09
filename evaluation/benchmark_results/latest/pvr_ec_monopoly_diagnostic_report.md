# PVR-EC-O Monopoly Specialization-vs-Collapse Diagnostic

**Primary Verdict:** PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE

## Verdicts
- PVR_EC_PROTOTYPE_MONOPOLY_COLLAPSE
- PVR_EC_FAMILY_REPAIR_SAFE_BUT_UNDERACTIVE
- PVR_EC_OWNERSHIP_REFRESH_REQUIRED
- PVR_EC_DO_NOT_PROMOTE

## Evidence
- Monopolized protos (8) have HIGH oracle gap (2.2912)
- Canary changed 2 protos but total monopolized is 8
- Challenger disagrees with current owner in 52.5% of monopolized tokens

## Group Summaries

### monopolized (n=8)
- oracle_gap_proxy: 2.2912
- loss: 2.7391
- accuracy: 0.7658
- owner_entropy: 0.0354
- challenger_disagree: 0.5250
- canary_change: 0.118729

### non_monopolized (n=4)
- oracle_gap_proxy: 3.1352
- loss: 4.3711
- accuracy: 0.5735
- owner_entropy: 0.5916
- challenger_disagree: 0.7139
- canary_change: 0.250000

### low_confidence_boundary (n=12)
- oracle_gap_proxy: 2.5726
- loss: 3.2831
- accuracy: 0.7017
- owner_entropy: 0.2208
- challenger_disagree: 0.5880
- canary_change: 0.162486

### canary_changed_owner (n=2)
- oracle_gap_proxy: 1.1204
- loss: 2.0729
- accuracy: 0.8025
- owner_entropy: 0.5552
- challenger_disagree: 0.3638
- canary_change: 0.974916

### challenger_disagreed (n=9)
- oracle_gap_proxy: 3.4214
- loss: 4.1927
- accuracy: 0.6170
- owner_entropy: 0.2629
- challenger_disagree: 0.7720
- canary_change: 0.111111

## Hard Invariants
- owners/token = 1.0
- Top2 executions = 0
- Top4 executions = 0
- Production map mutated = False

## Total Time: 35.6s