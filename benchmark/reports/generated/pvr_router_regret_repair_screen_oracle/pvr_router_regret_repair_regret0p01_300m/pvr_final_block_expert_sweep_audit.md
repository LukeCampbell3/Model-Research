# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `14.7618807383946`
Shared-only loss: `14.99790586744036`
Oracle loss: `14.16594546181815`
Mean wrong loss: `15.026529720851354`
Shifted wrong loss: `14.991778237479073`
Random wrong loss: `15.007925987243652`
Shuffled residual loss: `14.759500912257604`
Random residual loss: `15.185238429478236`
Mean router regret: `0.5959349535346519`
95th-percentile router regret: `1.5209178924560547`
Selected-is-oracle rate: `0.19419642857142858`
Selected-is-top2 rate: `0.3325892857142857`

## Claim Gates

- selected_beats_shared_only: `True`
- selected_beats_mean_wrong: `True`
- selected_beats_shuffled_residual: `False`
- selected_beats_random_residual: `True`
- selected_intervention_gate_pass: `False`
- final_block_oracle_beats_switch_top1: `False`
- final_block_oracle_beats_generic_top2: `False`

## Final-Block Oracle vs Comparators

Compares final-block oracle intervention loss to independently evaluated comparator micro losses on the same official file/block budget. This is diagnostic capacity evidence, not a deployable full-network oracle model.

| comparator | comparator micro loss | oracle - comparator |
|---|---:|---:|

## Per File

| file | selected | shared | oracle | mean wrong | shifted wrong | random wrong | regret | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | 17.682857513427734 | 17.956811904907227 | 17.075483322143555 | 17.96891212463379 | 17.8975830078125 | 17.846912384033203 | 0.6073725659916818 | 0.203125 | 0.390625 |
| code_generation.jsonl | 14.217506408691406 | 14.44021987915039 | 13.64616584777832 | 14.468672752380371 | 14.437553405761719 | 14.529237747192383 | 0.5713402805267833 | 0.171875 | 0.359375 |
| commonsense_completion.jsonl | 13.291984558105469 | 13.537942886352539 | 12.721274375915527 | 13.574283599853516 | 13.543254852294922 | 13.47354507446289 | 0.5707104527391493 | 0.203125 | 0.3125 |
| general_knowledge.jsonl | 14.347089767456055 | 14.605005264282227 | 13.75278091430664 | 14.645999908447266 | 14.65670394897461 | 14.615657806396484 | 0.594309834663818 | 0.1875 | 0.328125 |
| mathematics.jsonl | 15.579700469970703 | 15.72193431854248 | 14.899415969848633 | 15.749839782714844 | 15.73158073425293 | 15.798200607299805 | 0.6802837528703094 | 0.171875 | 0.28125 |
| multiple_choice_reasoning.jsonl | 14.670259475708008 | 14.886798858642578 | 14.075572967529297 | 14.900160789489746 | 14.829113006591797 | 14.97620677947998 | 0.5946861433330923 | 0.1875 | 0.296875 |
| pronoun_coreference.jsonl | 13.543766975402832 | 13.836627960205078 | 12.990924835205078 | 13.877839088439941 | 13.846658706665039 | 13.81572151184082 | 0.5528416446177289 | 0.234375 | 0.359375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
