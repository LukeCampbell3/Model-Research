# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `20.515610013689315`
Shared-only loss: `22.412247794015066`
Oracle loss: `18.396947179521835`
Mean wrong loss: `27.016403198242188`
Shifted wrong loss: `30.20492935180664`
Random wrong loss: `27.446792602539062`
Shuffled residual loss: `21.014494487217494`
Random residual loss: `26.6069461277553`
Mean router regret: `2.118663217606289`
95th-percentile router regret: `5.44728946685791`
Selected-is-oracle rate: `0.17410714285714285`
Selected-is-top2 rate: `0.40625`

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
| boolean_qa.jsonl | 25.492782592773438 | 27.06200408935547 | 22.776578903198242 | 31.732343673706055 | 34.61227035522461 | 32.336891174316406 | 2.7162035442888737 | 0.140625 | 0.359375 |
| code_generation.jsonl | 19.890357971191406 | 21.799821853637695 | 17.907751083374023 | 26.444072723388672 | 29.614673614501953 | 27.352405548095703 | 1.9826083658263087 | 0.171875 | 0.4375 |
| commonsense_completion.jsonl | 17.89037322998047 | 19.848346710205078 | 16.056346893310547 | 24.49536895751953 | 28.092369079589844 | 24.784385681152344 | 1.8340261224657297 | 0.140625 | 0.390625 |
| general_knowledge.jsonl | 20.204679489135742 | 21.92905044555664 | 18.088903427124023 | 26.676475524902344 | 30.370582580566406 | 27.11608123779297 | 2.1157765490934253 | 0.140625 | 0.421875 |
| mathematics.jsonl | 24.77188491821289 | 26.617897033691406 | 22.353721618652344 | 30.887277603149414 | 33.656105041503906 | 31.442764282226562 | 2.41816259175539 | 0.21875 | 0.34375 |
| multiple_choice_reasoning.jsonl | 17.766414642333984 | 19.940330505371094 | 15.867213249206543 | 24.50934410095215 | 28.02927589416504 | 25.44507598876953 | 1.899201993830502 | 0.1875 | 0.46875 |
| pronoun_coreference.jsonl | 17.592777252197266 | 19.688283920288086 | 15.72811508178711 | 24.36993980407715 | 27.059228897094727 | 23.649944305419922 | 1.8646633559837937 | 0.21875 | 0.421875 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
