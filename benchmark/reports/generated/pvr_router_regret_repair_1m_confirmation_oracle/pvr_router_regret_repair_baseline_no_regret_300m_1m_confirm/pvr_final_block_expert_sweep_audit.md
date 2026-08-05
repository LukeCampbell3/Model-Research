# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `14.397207260131836`
Shared-only loss: `14.568434034075056`
Oracle loss: `13.819837978907994`
Mean wrong loss: `14.597298622131348`
Shifted wrong loss: `14.584815161568779`
Random wrong loss: `14.610214505876813`
Shuffled residual loss: `14.402964047023229`
Random residual loss: `14.809074674333845`
Mean router regret: `0.5773689632301934`
95th-percentile router regret: `1.741575002670288`
Selected-is-oracle rate: `0.296875`
Selected-is-top2 rate: `0.40848214285714285`

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
| boolean_qa.jsonl | 17.779342651367188 | 17.983102798461914 | 17.174461364746094 | 18.015338897705078 | 17.987728118896484 | 18.074024200439453 | 0.6048799372510985 | 0.328125 | 0.453125 |
| code_generation.jsonl | 13.73910903930664 | 13.902631759643555 | 13.16487979888916 | 13.925328254699707 | 13.903261184692383 | 13.917425155639648 | 0.5742290508569567 | 0.28125 | 0.40625 |
| commonsense_completion.jsonl | 12.68628215789795 | 12.782947540283203 | 12.074337005615234 | 12.81757926940918 | 12.841644287109375 | 12.877504348754883 | 0.6119455429725349 | 0.234375 | 0.375 |
| general_knowledge.jsonl | 14.186077117919922 | 14.338741302490234 | 13.596867561340332 | 14.372718811035156 | 14.332117080688477 | 14.395854949951172 | 0.5892094171140343 | 0.296875 | 0.40625 |
| mathematics.jsonl | 16.454641342163086 | 16.708515167236328 | 15.914848327636719 | 16.733760833740234 | 16.765432357788086 | 16.697046279907227 | 0.5397918355301954 | 0.328125 | 0.4375 |
| multiple_choice_reasoning.jsonl | 13.268645286560059 | 13.42587661743164 | 12.685070991516113 | 13.448368072509766 | 13.44166374206543 | 13.453532218933105 | 0.5835735304281116 | 0.296875 | 0.375 |
| pronoun_coreference.jsonl | 12.666353225708008 | 12.837223052978516 | 12.128400802612305 | 12.867996215820312 | 12.821859359741211 | 12.856114387512207 | 0.5379534284584224 | 0.3125 | 0.40625 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
