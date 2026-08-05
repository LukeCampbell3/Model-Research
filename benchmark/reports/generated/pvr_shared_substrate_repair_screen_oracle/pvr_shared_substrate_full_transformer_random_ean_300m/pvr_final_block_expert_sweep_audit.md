# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `13.453469412667411`
Shared-only loss: `13.7130400793893`
Oracle loss: `12.826674461364746`
Mean wrong loss: `13.763294492449079`
Shifted wrong loss: `13.750157764979772`
Random wrong loss: `13.803884369986397`
Shuffled residual loss: `13.455906186785016`
Random residual loss: `13.97846167428153`
Mean router regret: `0.6267948352864811`
95th-percentile router regret: `1.9070664644241333`
Selected-is-oracle rate: `0.3013392857142857`
Selected-is-top2 rate: `0.3638392857142857`

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
| boolean_qa.jsonl | 16.298206329345703 | 16.647594451904297 | 15.701971054077148 | 16.68688201904297 | 16.659393310546875 | 16.750478744506836 | 0.5962365646846592 | 0.328125 | 0.359375 |
| code_generation.jsonl | 12.97913932800293 | 13.246587753295898 | 12.339092254638672 | 13.297565460205078 | 13.276214599609375 | 13.317773818969727 | 0.6400466505438089 | 0.328125 | 0.40625 |
| commonsense_completion.jsonl | 11.95568561553955 | 12.209607124328613 | 11.330207824707031 | 12.266416549682617 | 12.266971588134766 | 12.36534309387207 | 0.625477293971926 | 0.25 | 0.296875 |
| general_knowledge.jsonl | 13.448003768920898 | 13.670961380004883 | 12.823894500732422 | 13.72039794921875 | 13.719411849975586 | 13.749424934387207 | 0.6241092849522829 | 0.34375 | 0.390625 |
| mathematics.jsonl | 15.239079475402832 | 15.518500328063965 | 14.645339012145996 | 15.559319496154785 | 15.484752655029297 | 15.52391242980957 | 0.5937398923560977 | 0.328125 | 0.40625 |
| multiple_choice_reasoning.jsonl | 12.459260940551758 | 12.666496276855469 | 11.794994354248047 | 12.717765808105469 | 12.690681457519531 | 12.843729972839355 | 0.6642665797844529 | 0.234375 | 0.34375 |
| pronoun_coreference.jsonl | 11.794910430908203 | 12.031533241271973 | 11.151222229003906 | 12.094714164733887 | 12.153678894042969 | 12.07652759552002 | 0.6436875807121396 | 0.296875 | 0.34375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
