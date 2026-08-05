# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `16.500033378601074`
Shared-only loss: `16.54817513057164`
Oracle loss: `15.68295669555664`
Mean wrong loss: `16.65194375174386`
Shifted wrong loss: `16.63655608040946`
Random wrong loss: `16.619507244655065`
Shuffled residual loss: `16.49724428994315`
Random residual loss: `16.752554893493652`
Mean router regret: `0.817077138109458`
95th-percentile router regret: `2.3033652305603027`
Selected-is-oracle rate: `0.23883928571428573`
Selected-is-top2 rate: `0.30357142857142855`

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
| boolean_qa.jsonl | 19.696319580078125 | 19.70899200439453 | 18.82553482055664 | 19.812137603759766 | 19.886428833007812 | 19.805389404296875 | 0.8707858166017104 | 0.265625 | 0.296875 |
| code_generation.jsonl | 15.929912567138672 | 15.91270923614502 | 15.082975387573242 | 16.018083572387695 | 15.990318298339844 | 15.982522964477539 | 0.846936538713635 | 0.203125 | 0.265625 |
| commonsense_completion.jsonl | 14.735891342163086 | 14.778387069702148 | 13.922693252563477 | 14.881874084472656 | 14.822021484375 | 14.80881118774414 | 0.8131984354695305 | 0.234375 | 0.296875 |
| general_knowledge.jsonl | 16.700824737548828 | 16.754703521728516 | 15.857006072998047 | 16.85554313659668 | 16.824052810668945 | 16.96421241760254 | 0.843818592333264 | 0.265625 | 0.3125 |
| mathematics.jsonl | 17.987661361694336 | 18.098583221435547 | 17.298974990844727 | 18.207752227783203 | 18.21337890625 | 18.19324493408203 | 0.688687574944197 | 0.234375 | 0.3125 |
| multiple_choice_reasoning.jsonl | 15.70540714263916 | 15.87826919555664 | 14.953656196594238 | 15.978679656982422 | 15.94918441772461 | 15.876983642578125 | 0.7517524239019622 | 0.296875 | 0.421875 |
| pronoun_coreference.jsonl | 14.744216918945312 | 14.705581665039062 | 13.839856147766113 | 14.80953598022461 | 14.7705078125 | 14.7053861618042 | 0.904360584801907 | 0.171875 | 0.21875 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
