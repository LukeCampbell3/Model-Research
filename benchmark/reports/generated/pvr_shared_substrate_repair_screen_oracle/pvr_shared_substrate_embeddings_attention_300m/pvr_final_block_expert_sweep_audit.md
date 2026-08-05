# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `16.76168414524623`
Shared-only loss: `16.76308740888323`
Oracle loss: `16.73219530923026`
Mean wrong loss: `16.763585908072336`
Shifted wrong loss: `16.762473378862655`
Random wrong loss: `16.764434814453125`
Shuffled residual loss: `16.76169627053397`
Random residual loss: `16.76182746887207`
Mean router regret: `0.02948880514928273`
95th-percentile router regret: `0.064300537109375`
Selected-is-oracle rate: `0.026785714285714284`
Selected-is-top2 rate: `0.10044642857142858`

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
| boolean_qa.jsonl | 20.10796546936035 | 20.110740661621094 | 20.079792022705078 | 20.111499786376953 | 20.1103515625 | 20.10875701904297 | 0.02817133627831936 | 0.015625 | 0.171875 |
| code_generation.jsonl | 16.385284423828125 | 16.38677215576172 | 16.35554313659668 | 16.387378692626953 | 16.385866165161133 | 16.38916778564453 | 0.029742266982793808 | 0.03125 | 0.09375 |
| commonsense_completion.jsonl | 14.778188705444336 | 14.777697563171387 | 14.74728775024414 | 14.778356552124023 | 14.776988983154297 | 14.7767915725708 | 0.030901318415999413 | 0.03125 | 0.0625 |
| general_knowledge.jsonl | 16.495433807373047 | 16.497350692749023 | 16.466781616210938 | 16.497840881347656 | 16.49692153930664 | 16.498931884765625 | 0.02865302562713623 | 0.03125 | 0.109375 |
| mathematics.jsonl | 19.896705627441406 | 19.898452758789062 | 19.867441177368164 | 19.899023056030273 | 19.89711570739746 | 19.900951385498047 | 0.029263775795698166 | 0.03125 | 0.109375 |
| multiple_choice_reasoning.jsonl | 14.846342086791992 | 14.847261428833008 | 14.816712379455566 | 14.847675323486328 | 14.847558975219727 | 14.85120677947998 | 0.0296299010515213 | 0.015625 | 0.0625 |
| pronoun_coreference.jsonl | 14.821868896484375 | 14.823336601257324 | 14.79180908203125 | 14.82332706451416 | 14.822510719299316 | 14.825237274169922 | 0.03006001189351082 | 0.03125 | 0.09375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
