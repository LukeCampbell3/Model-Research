# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `18.791342326572963`
Shared-only loss: `18.892627716064453`
Oracle loss: `17.93417249407087`
Mean wrong loss: `18.992572784423828`
Shifted wrong loss: `19.200699397495814`
Random wrong loss: `18.96263858250209`
Shuffled residual loss: `18.793712615966797`
Random residual loss: `19.127822058541433`
Mean router regret: `0.8571702269737541`
95th-percentile router regret: `2.7539238929748535`
Selected-is-oracle rate: `0.29910714285714285`
Selected-is-top2 rate: `0.3705357142857143`

## Claim Gates

- selected_beats_shared_only: `True`
- selected_beats_mean_wrong: `True`
- selected_beats_shuffled_residual: `True`
- selected_beats_random_residual: `True`
- selected_intervention_gate_pass: `True`
- final_block_oracle_beats_switch_top1: `False`
- final_block_oracle_beats_generic_top2: `False`

## Final-Block Oracle vs Comparators

Compares final-block oracle intervention loss to independently evaluated comparator micro losses on the same official file/block budget. This is diagnostic capacity evidence, not a deployable full-network oracle model.

| comparator | comparator micro loss | oracle - comparator |
|---|---:|---:|

## Per File

| file | selected | shared | oracle | mean wrong | shifted wrong | random wrong | regret | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | 23.104637145996094 | 23.161766052246094 | 22.125282287597656 | 23.240598678588867 | 23.48209571838379 | 23.239442825317383 | 0.9793538955163967 | 0.296875 | 0.34375 |
| code_generation.jsonl | 17.896059036254883 | 17.931774139404297 | 16.989418029785156 | 18.020477294921875 | 18.24757194519043 | 17.949851989746094 | 0.9066430163948098 | 0.265625 | 0.3125 |
| commonsense_completion.jsonl | 16.639902114868164 | 16.797704696655273 | 15.81136703491211 | 16.903209686279297 | 17.080286026000977 | 16.90081024169922 | 0.8285344210453331 | 0.34375 | 0.359375 |
| general_knowledge.jsonl | 18.554527282714844 | 18.773977279663086 | 17.800952911376953 | 18.907093048095703 | 19.052898406982422 | 18.749757766723633 | 0.7535765578143128 | 0.3125 | 0.4375 |
| mathematics.jsonl | 20.652820587158203 | 20.70680046081543 | 19.754560470581055 | 20.802783966064453 | 21.055191040039062 | 20.76073455810547 | 0.8982604559023457 | 0.296875 | 0.34375 |
| multiple_choice_reasoning.jsonl | 18.00986671447754 | 18.108640670776367 | 17.158275604248047 | 18.19959259033203 | 18.403949737548828 | 18.36502456665039 | 0.8515920210629702 | 0.328125 | 0.453125 |
| pronoun_coreference.jsonl | 16.681583404541016 | 16.767730712890625 | 15.899351119995117 | 16.87425422668457 | 17.082902908325195 | 16.77284812927246 | 0.7822312210801101 | 0.25 | 0.34375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
