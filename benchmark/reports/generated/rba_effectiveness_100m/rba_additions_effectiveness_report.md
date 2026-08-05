# RBA Additions Effectiveness Report

Status: `RBA_ADDITIONS_NOT_EFFECTIVE_UNDER_MATCHED_ABLATION`

Matched 100M diagnostic intervention, same seed/data/budget:

| model | final train loss | mean eval loss | final eval loss | mean owner in-bounds | route margin |
|---|---:|---:|---:|---:|---:|
| baseline | 4.962242 | 15.059596 | 5.335077 | 0.538915 | 0.452910 |
| route_conf_reg_0_01 | 4.990982 | 15.204321 | 5.354288 | 0.585626 | 0.352082 |

Deltas are regularized minus baseline:

- final train loss delta: `0.028739`
- mean eval loss delta: `0.144725`
- final eval loss delta: `0.019211`
- mean owner in-bounds delta: `0.046711`
- route margin delta: `-0.100828`
- regularized confidence/loss correlation over active steps: `-0.03835492312338522`

Conclusion: the additions are not proven effective for capability under this matched ablation. They are effective as instrumentation: the confidence head is bounded, the regularizer activates, confidence changes, and Top1 invariants remain intact. They are not yet effective as a repair because loss did not improve and route margin regressed.
