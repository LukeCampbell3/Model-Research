# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `19.153899601527623`
Shared-only loss: `19.33378301348005`
Oracle loss: `18.477394376482284`
Mean wrong loss: `19.33493368966239`
Shifted wrong loss: `19.367131096976145`
Random wrong loss: `19.334237779889786`
Shuffled residual loss: `19.159148352486746`
Random residual loss: `19.520755767822266`
Mean router regret: `0.6765053497760424`
95th-percentile router regret: `1.9508662223815918`
Selected-is-oracle rate: `0.24776785714285715`
Selected-is-top2 rate: `0.31473214285714285`

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
| boolean_qa.jsonl | 23.222869873046875 | 23.35381317138672 | 22.501102447509766 | 23.353893280029297 | 23.364355087280273 | 23.33085823059082 | 0.7217684234492481 | 0.21875 | 0.265625 |
| code_generation.jsonl | 18.655662536621094 | 18.8002986907959 | 17.964380264282227 | 18.80851173400879 | 18.833595275878906 | 18.850421905517578 | 0.6912811361253262 | 0.25 | 0.3125 |
| commonsense_completion.jsonl | 17.23159408569336 | 17.40243911743164 | 16.523591995239258 | 17.39574432373047 | 17.401023864746094 | 17.341690063476562 | 0.7080013966187835 | 0.21875 | 0.296875 |
| general_knowledge.jsonl | 19.01563262939453 | 19.282360076904297 | 18.381376266479492 | 19.278989791870117 | 19.323165893554688 | 19.203035354614258 | 0.6342552085407078 | 0.328125 | 0.375 |
| mathematics.jsonl | 21.290002822875977 | 21.37216567993164 | 20.56932258605957 | 21.376428604125977 | 21.420787811279297 | 21.397064208984375 | 0.7206815094687045 | 0.171875 | 0.234375 |
| multiple_choice_reasoning.jsonl | 17.693132400512695 | 17.913366317749023 | 17.052736282348633 | 17.91394805908203 | 17.938617706298828 | 17.92308807373047 | 0.6403964878991246 | 0.296875 | 0.359375 |
| pronoun_coreference.jsonl | 16.968402862548828 | 17.212038040161133 | 16.34925079345703 | 17.21702003479004 | 17.288372039794922 | 17.293506622314453 | 0.6191532863304019 | 0.25 | 0.359375 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
