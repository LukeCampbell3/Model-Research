# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `22.66265732901437`
Shared-only loss: `22.711912972586497`
Oracle loss: `21.98735100882394`
Mean wrong loss: `22.81475911821638`
Shifted wrong loss: `22.8520633152553`
Random wrong loss: `22.836245128086635`
Shuffled residual loss: `22.672306060791016`
Random residual loss: `22.780595506940568`
Mean router regret: `0.6753054587065728`
95th-percentile router regret: `1.5308685302734375`
Selected-is-oracle rate: `0.16071428571428573`
Selected-is-top2 rate: `0.18973214285714285`

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
| boolean_qa.jsonl | 28.081457138061523 | 28.10029411315918 | 27.36260223388672 | 28.207225799560547 | 28.201190948486328 | 28.16016960144043 | 0.7188542386757035 | 0.15625 | 0.1875 |
| code_generation.jsonl | 21.434555053710938 | 21.4941349029541 | 20.759361267089844 | 21.588760375976562 | 21.629085540771484 | 21.60150718688965 | 0.6751926839806401 | 0.171875 | 0.1875 |
| commonsense_completion.jsonl | 19.871002197265625 | 19.937225341796875 | 19.20100212097168 | 20.047557830810547 | 20.12961769104004 | 20.115110397338867 | 0.6699998740805313 | 0.1875 | 0.21875 |
| general_knowledge.jsonl | 22.175535202026367 | 22.176591873168945 | 21.512006759643555 | 22.27553939819336 | 22.28241729736328 | 22.32141876220703 | 0.663527326338226 | 0.109375 | 0.125 |
| mathematics.jsonl | 25.61936378479004 | 25.669002532958984 | 24.98249626159668 | 25.793376922607422 | 25.791439056396484 | 25.87596321105957 | 0.6368682586715977 | 0.15625 | 0.21875 |
| multiple_choice_reasoning.jsonl | 21.299610137939453 | 21.403423309326172 | 20.651151657104492 | 21.505231857299805 | 21.57248878479004 | 21.444351196289062 | 0.6484568856876649 | 0.203125 | 0.21875 |
| pronoun_coreference.jsonl | 20.15707778930664 | 20.20271873474121 | 19.44283676147461 | 20.285621643066406 | 20.358203887939453 | 20.335195541381836 | 0.7142389435116456 | 0.140625 | 0.171875 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
