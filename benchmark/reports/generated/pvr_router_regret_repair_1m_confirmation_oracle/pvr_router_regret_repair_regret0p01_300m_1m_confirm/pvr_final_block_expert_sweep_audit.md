# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `13.425919532775879`
Shared-only loss: `13.776915686471122`
Oracle loss: `13.056952340262276`
Mean wrong loss: `13.838479723249163`
Shifted wrong loss: `13.811635834830147`
Random wrong loss: `13.816878863743373`
Shuffled residual loss: `13.427950995309013`
Random residual loss: `13.978005681719099`
Mean router regret: `0.36896729755348395`
95th-percentile router regret: `1.4463565349578857`
Selected-is-oracle rate: `0.36830357142857145`
Selected-is-top2 rate: `0.5044642857142857`

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
| boolean_qa.jsonl | 16.088638305664062 | 16.502975463867188 | 15.714996337890625 | 16.568096160888672 | 16.51997947692871 | 16.520381927490234 | 0.3736426685936749 | 0.421875 | 0.515625 |
| code_generation.jsonl | 12.95207691192627 | 13.317920684814453 | 12.607497215270996 | 13.380815505981445 | 13.365140914916992 | 13.391825675964355 | 0.3445800859481096 | 0.375 | 0.515625 |
| commonsense_completion.jsonl | 12.101964950561523 | 12.475883483886719 | 11.774511337280273 | 12.541295051574707 | 12.520011901855469 | 12.521242141723633 | 0.32745354319922626 | 0.359375 | 0.5 |
| general_knowledge.jsonl | 13.388019561767578 | 13.735881805419922 | 13.019899368286133 | 13.797048568725586 | 13.758920669555664 | 13.760442733764648 | 0.3681202670559287 | 0.375 | 0.546875 |
| mathematics.jsonl | 15.113578796386719 | 15.454298973083496 | 14.713751792907715 | 15.505802154541016 | 15.456016540527344 | 15.547971725463867 | 0.3998264679685235 | 0.328125 | 0.484375 |
| multiple_choice_reasoning.jsonl | 12.464468002319336 | 12.769774436950684 | 12.060205459594727 | 12.825451850891113 | 12.809941291809082 | 12.796451568603516 | 0.4042631380725652 | 0.34375 | 0.484375 |
| pronoun_coreference.jsonl | 11.872690200805664 | 12.18167495727539 | 11.507804870605469 | 12.250848770141602 | 12.251440048217773 | 12.17983627319336 | 0.3648849120363593 | 0.375 | 0.484375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
