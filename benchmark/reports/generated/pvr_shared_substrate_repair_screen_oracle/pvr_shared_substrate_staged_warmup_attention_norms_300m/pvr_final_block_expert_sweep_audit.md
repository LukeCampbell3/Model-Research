# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `15.438885688781738`
Shared-only loss: `17.38714095524379`
Oracle loss: `13.770956039428711`
Mean wrong loss: `20.854692186628068`
Shifted wrong loss: `20.23649733407157`
Random wrong loss: `20.164568764822825`
Shuffled residual loss: `15.682280540466309`
Random residual loss: `21.90017291477748`
Mean router regret: `1.6679293577575922`
95th-percentile router regret: `5.4933013916015625`
Selected-is-oracle rate: `0.12053571428571429`
Selected-is-top2 rate: `0.28125`

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
| boolean_qa.jsonl | 18.56195640563965 | 20.830162048339844 | 16.88290786743164 | 24.30977439880371 | 23.812829971313477 | 23.93265151977539 | 1.679048085177783 | 0.171875 | 0.265625 |
| code_generation.jsonl | 15.061333656311035 | 16.964479446411133 | 13.564322471618652 | 20.57082748413086 | 20.17383575439453 | 19.43803596496582 | 1.497011455358006 | 0.125 | 0.328125 |
| commonsense_completion.jsonl | 13.335343360900879 | 15.055975914001465 | 11.71290397644043 | 18.552438735961914 | 17.94839859008789 | 18.75484848022461 | 1.6224390538409352 | 0.140625 | 0.34375 |
| general_knowledge.jsonl | 15.319936752319336 | 17.33187484741211 | 13.595760345458984 | 20.63355255126953 | 20.252317428588867 | 19.469707489013672 | 1.7241775854490697 | 0.125 | 0.265625 |
| mathematics.jsonl | 18.40178871154785 | 20.111698150634766 | 16.559459686279297 | 23.661516189575195 | 22.87091064453125 | 22.36858367919922 | 1.842327810358256 | 0.078125 | 0.265625 |
| multiple_choice_reasoning.jsonl | 13.807168960571289 | 15.636062622070312 | 12.108965873718262 | 19.082338333129883 | 18.29865837097168 | 18.30227279663086 | 1.6982027739286423 | 0.09375 | 0.21875 |
| pronoun_coreference.jsonl | 13.584671974182129 | 15.779733657836914 | 11.972372055053711 | 19.17239761352539 | 18.29853057861328 | 18.885881423950195 | 1.6122987401904538 | 0.109375 | 0.28125 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
