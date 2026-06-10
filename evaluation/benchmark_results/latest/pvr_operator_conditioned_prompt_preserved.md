# PVR-EC-O Operator-Conditioned Top1 Router Refresh — Preserved Prompt

**Status:** PRESERVED
**Date:** 2026-06-09
**Base geometry candidate:** contrastive_light
**Default mode:** shadow

## Core Concept

The operator-conditioned router adds semantic operator evidence (negation, instruction, delimiter, etc.) to the single-owner Top1 scoring before final argmax, without changing the execution invariant of one owner per token.

## Pipeline

```
state → shared context encoding → soft family/prototype evidence
→ operator + scope evidence → operator-conditioned route refresh
→ family-preserving Top1 owner → execute one expert delta
```

## Operator Schema

- none, negation, instruction_action, conditional, delimiter, role_marker
- polarity_positive, polarity_negative, copy_command, reverse_command
- shift_command, before_after, unless_exception

## Score Formula

```
operator_family_bias_expected[i, e] =
    Σ_o Σ_f P(operator=o|i) · P(family=f|i) · scope_weight[i,o] · operator_family_owner_bias[o,f,e]

owner_score[i, e] =
    router_logits[i, e]
  + prototype_bias[i, e]
  + ownership_bias[p_i, e]
  + family_preservation_bias[i, e]
  + operator_family_bias_expected[i, e]
  + clipped_balance_bias[e]
  - stale_owner_penalty[p_i, e]
  - monopoly_penalty[p_i, e]

owner_score[i, ~compatible_mask_i] = -inf
owner_i = argmax_e owner_score(i, e)
```

## Hard Invariants

- owners/token = 1.0
- Top2/Top4 execution = 0
- No runtime dynamic-K or Expert Choice
- No oracle in forward
- No map mutation in forward
