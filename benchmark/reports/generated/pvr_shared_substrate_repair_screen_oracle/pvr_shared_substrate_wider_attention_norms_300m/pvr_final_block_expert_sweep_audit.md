# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `23.644671031406947`
Shared-only loss: `29.635169982910156`
Oracle loss: `21.801632744925364`
Mean wrong loss: `33.187565667288645`
Shifted wrong loss: `32.545291083199636`
Random wrong loss: `33.57323401314871`
Shuffled residual loss: `23.869871956961497`
Random residual loss: `33.42492594037737`
Mean router regret: `1.8430385900927442`
95th-percentile router regret: `7.113739013671875`
Selected-is-oracle rate: `0.25223214285714285`
Selected-is-top2 rate: `0.6183035714285714`

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
| boolean_qa.jsonl | 28.957386016845703 | 34.84682846069336 | 26.74783706665039 | 38.42741775512695 | 36.93336486816406 | 39.270164489746094 | 2.2095496198162436 | 0.234375 | 0.65625 |
| code_generation.jsonl | 22.781417846679688 | 28.86876678466797 | 21.069461822509766 | 32.53498458862305 | 32.3947868347168 | 33.407135009765625 | 1.7119539501145482 | 0.28125 | 0.640625 |
| commonsense_completion.jsonl | 20.773054122924805 | 26.633487701416016 | 19.10029411315918 | 30.37567710876465 | 29.071083068847656 | 30.830490112304688 | 1.6727613895200193 | 0.265625 | 0.625 |
| general_knowledge.jsonl | 22.967124938964844 | 29.141841888427734 | 21.177751541137695 | 32.622344970703125 | 32.172462463378906 | 32.8910026550293 | 1.7893749279901385 | 0.25 | 0.578125 |
| mathematics.jsonl | 28.686725616455078 | 34.30857849121094 | 26.815025329589844 | 37.84187698364258 | 36.590126037597656 | 39.73260498046875 | 1.8717007180675864 | 0.234375 | 0.59375 |
| multiple_choice_reasoning.jsonl | 20.661041259765625 | 26.67359161376953 | 18.83555793762207 | 30.052846908569336 | 30.224027633666992 | 30.406475067138672 | 1.8254811065271497 | 0.203125 | 0.59375 |
| pronoun_coreference.jsonl | 20.68594741821289 | 26.973094940185547 | 18.865501403808594 | 30.45781135559082 | 30.43118667602539 | 28.47476577758789 | 1.8204484186135232 | 0.296875 | 0.640625 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
