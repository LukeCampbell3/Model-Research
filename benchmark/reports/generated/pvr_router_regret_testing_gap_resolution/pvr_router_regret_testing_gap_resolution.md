# PVR Router Regret Testing Gap Resolution

Status: `PVR_ROUTER_REGRET_TESTING_GAP_RESOLUTION_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_REGRET0P01_NOT_SUPPORTED_FOR_PROMOTION`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

## Summary

Training final-eval delta: `0.04692554473876953`
Final-block router-regret delta: `-0.20840166567670942`
Raw JSON 1-block micro delta / wins: `-0.9712870461600165` / `7/7`
Raw JSON 2-block micro delta / wins: `0.888661929539273` / `0/7`
Text-only micro delta / wins: `-0.07709789276123047` / `3/7`

## Full-Network Greedy Oracle Comparison

| metric | regret0p01 - baseline |
|---|---:|
| selected_loss_delta | -0.9712867736816406 |
| greedy_oracle_loss_delta | -1.387683255331856 |
| mean_router_regret_delta | 0.024413152609054994 |
| selected_is_oracle_rate_delta | -0.01953125 |
| selected_is_top2_rate_delta | -0.017206101190476164 |

## Resolved Gaps

- report_or_checkpoint_inconsistency: RESOLVED_NOT_CAUSAL; exact checkpoints, no resume events, matched tokens/windows.
- final_block_oracle_rate: RESOLVED; regret0p01 improves final-block selected-is-oracle rate and final-block regret.
- lm_eval_reason: RESOLVED; old four-window LM gate was under-sampled, but broader content-aware gates still do not support robust promotion.
- raw_json_wrapper_bias: RESOLVED; regret0p01 strongly helps first JSONL metadata blocks but fails after content begins.
- official_like_text_content: RESOLVED_MIXED; small micro improvement, only 3/7 file wins, math regression.
- full_network_oracle: RESOLVED; greedy full-network oracle still shows large headroom and regret0p01 does not reduce full-network regret versus no-regret baseline.

## Status Labels

- `PVR_ROUTER_REGRET_TESTING_GAPS_RESOLVED`
- `PVR_ROUTER_REGRET_REPAIR_FINAL_BLOCK_METRIC_IMPROVEMENT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_RAW_JSON_PREFIX_SUPPORTED_ONLY`
- `PVR_ROUTER_REGRET_REPAIR_RAW_JSON_TWO_BLOCK_NOT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_TEXT_CONTENT_BROAD_SUPPORT_NOT_ESTABLISHED`
- `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_REGRET_REDUCTION_NOT_SUPPORTED`
- `PVR_ROUTER_REGRET_REPAIR_REGRET0P01_DO_NOT_PROMOTE`

## Recommendation

Stop regret0p01 as a promotion candidate. If router repair continues, use lower/annealed regret weights with explicit entropy/monopoly retention and a text-field official-like micro+macro gate; do not use raw JSONL wrapper loss or four single-window eval loss as the promotion gate.
