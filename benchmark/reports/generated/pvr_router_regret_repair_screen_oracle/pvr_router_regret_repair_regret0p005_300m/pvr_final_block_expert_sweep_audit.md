# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `14.707979883466448`
Shared-only loss: `15.110454968043737`
Oracle loss: `14.200603076389857`
Mean wrong loss: `15.116447857448033`
Shifted wrong loss: `15.108393941606794`
Random wrong loss: `15.12393569946289`
Shuffled residual loss: `14.711934634617396`
Random residual loss: `15.209429468427386`
Mean router regret: `0.5073771975295196`
95th-percentile router regret: `1.5931625366210938`
Selected-is-oracle rate: `0.27232142857142855`
Selected-is-top2 rate: `0.3794642857142857`

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
| boolean_qa.jsonl | 17.37662124633789 | 17.691757202148438 | 16.784934997558594 | 17.697431564331055 | 17.676712036132812 | 17.742109298706055 | 0.5916880197097498 | 0.25 | 0.34375 |
| code_generation.jsonl | 14.008564949035645 | 14.422487258911133 | 13.531352996826172 | 14.433164596557617 | 14.412479400634766 | 14.495309829711914 | 0.4772127155410999 | 0.265625 | 0.40625 |
| commonsense_completion.jsonl | 13.572813034057617 | 13.970932006835938 | 13.055315017700195 | 13.967756271362305 | 13.976303100585938 | 13.997526168823242 | 0.517498561697721 | 0.28125 | 0.359375 |
| general_knowledge.jsonl | 14.725199699401855 | 15.148277282714844 | 14.218950271606445 | 15.142558097839355 | 15.119901657104492 | 15.121158599853516 | 0.50624947816857 | 0.28125 | 0.375 |
| mathematics.jsonl | 15.536772727966309 | 15.908918380737305 | 15.04071044921875 | 15.936628341674805 | 15.9241361618042 | 15.940755844116211 | 0.49606190370946024 | 0.296875 | 0.390625 |
| multiple_choice_reasoning.jsonl | 14.427433013916016 | 14.840866088867188 | 13.923757553100586 | 14.839317321777344 | 14.833695411682129 | 14.756390571594238 | 0.5036751965262738 | 0.25 | 0.359375 |
| pronoun_coreference.jsonl | 13.308454513549805 | 13.789946556091309 | 12.849200248718262 | 13.79827880859375 | 13.815529823303223 | 13.814299583435059 | 0.45925450735376216 | 0.28125 | 0.421875 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
