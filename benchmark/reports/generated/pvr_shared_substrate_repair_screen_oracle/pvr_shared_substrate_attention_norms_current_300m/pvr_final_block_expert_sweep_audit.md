# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `13.060628754752022`
Shared-only loss: `16.537790298461914`
Oracle loss: `10.6698397227696`
Mean wrong loss: `19.861526216779435`
Shifted wrong loss: `20.062491008213588`
Random wrong loss: `19.768508093697683`
Shuffled residual loss: `13.5785585130964`
Random residual loss: `21.705602645874023`
Mean router regret: `2.3907891116146596`
95th-percentile router regret: `7.912445068359375`
Selected-is-oracle rate: `0.20758928571428573`
Selected-is-top2 rate: `0.4263392857142857`

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
| boolean_qa.jsonl | 15.245681762695312 | 18.79872703552246 | 12.988715171813965 | 22.169269561767578 | 23.070980072021484 | 22.166179656982422 | 2.256967237801291 | 0.21875 | 0.390625 |
| code_generation.jsonl | 12.820114135742188 | 16.1689510345459 | 10.367792129516602 | 19.476882934570312 | 19.343324661254883 | 20.123798370361328 | 2.4523213946376927 | 0.203125 | 0.40625 |
| commonsense_completion.jsonl | 12.235008239746094 | 15.465764999389648 | 9.78131103515625 | 18.898365020751953 | 19.795438766479492 | 18.40523910522461 | 2.4536966946325265 | 0.203125 | 0.421875 |
| general_knowledge.jsonl | 12.588228225708008 | 15.918932914733887 | 10.04068374633789 | 19.203458786010742 | 19.63186264038086 | 18.593137741088867 | 2.547544939472573 | 0.171875 | 0.375 |
| mathematics.jsonl | 14.476984024047852 | 18.437503814697266 | 12.470190048217773 | 21.7114200592041 | 21.807262420654297 | 21.35773468017578 | 2.0067938492284156 | 0.25 | 0.4375 |
| multiple_choice_reasoning.jsonl | 11.889254570007324 | 15.521504402160645 | 9.543617248535156 | 18.793563842773438 | 18.015283584594727 | 19.050338745117188 | 2.3456377486581914 | 0.203125 | 0.484375 |
| pronoun_coreference.jsonl | 12.169130325317383 | 15.453147888183594 | 9.49656867980957 | 18.77772331237793 | 18.773284912109375 | 18.683128356933594 | 2.6725619168719277 | 0.203125 | 0.46875 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
