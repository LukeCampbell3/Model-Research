# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `23.61526189531599`
Shared-only loss: `27.74079159327916`
Oracle loss: `23.260616030011857`
Mean wrong loss: `27.91482707432338`
Shifted wrong loss: `27.60651206970215`
Random wrong loss: `27.893758501325333`
Shuffled residual loss: `23.699845995221818`
Random residual loss: `29.11426407950265`
Mean router regret: `0.35464565304573625`
95th-percentile router regret: `2.95306396484375`
Selected-is-oracle rate: `0.8102678571428571`
Selected-is-top2 rate: `0.84375`

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
| boolean_qa.jsonl | 29.648479461669922 | 33.88728332519531 | 29.37078285217285 | 34.04884338378906 | 33.75155258178711 | 34.03031539916992 | 0.2776963321957737 | 0.828125 | 0.859375 |
| code_generation.jsonl | 22.700550079345703 | 26.895809173583984 | 22.39926528930664 | 27.05304718017578 | 26.771469116210938 | 27.048643112182617 | 0.30128377804066986 | 0.828125 | 0.84375 |
| commonsense_completion.jsonl | 20.418987274169922 | 24.43303680419922 | 19.99140739440918 | 24.609149932861328 | 24.22677993774414 | 24.730709075927734 | 0.42758110258728266 | 0.75 | 0.828125 |
| general_knowledge.jsonl | 23.21930503845215 | 27.406139373779297 | 22.895671844482422 | 27.572589874267578 | 27.351383209228516 | 27.385339736938477 | 0.32363421097397804 | 0.828125 | 0.84375 |
| mathematics.jsonl | 27.011823654174805 | 31.14487648010254 | 26.650619506835938 | 31.332416534423828 | 30.972373962402344 | 31.328617095947266 | 0.36120377480983734 | 0.8125 | 0.859375 |
| multiple_choice_reasoning.jsonl | 21.42426300048828 | 25.49041748046875 | 20.971193313598633 | 25.68560791015625 | 25.30996322631836 | 25.71661376953125 | 0.453067297115922 | 0.8125 | 0.828125 |
| pronoun_coreference.jsonl | 20.883424758911133 | 24.927978515625 | 20.545372009277344 | 25.102134704589844 | 24.862062454223633 | 25.016071319580078 | 0.3380530755966902 | 0.8125 | 0.84375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
