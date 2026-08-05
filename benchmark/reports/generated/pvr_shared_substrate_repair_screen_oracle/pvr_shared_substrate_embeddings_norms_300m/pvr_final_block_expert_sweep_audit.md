# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `17.04397882734026`
Shared-only loss: `21.732930864606583`
Oracle loss: `14.523618970598493`
Mean wrong loss: `26.887859344482422`
Shifted wrong loss: `27.898268835885183`
Random wrong loss: `26.688485554286412`
Shuffled residual loss: `17.28224781581334`
Random residual loss: `31.076216288975306`
Mean router regret: `2.5203601606897013`
95th-percentile router regret: `13.646324157714844`
Selected-is-oracle rate: `0.24330357142857142`
Selected-is-top2 rate: `0.5357142857142857`

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
| boolean_qa.jsonl | 20.57494354248047 | 25.213912963867188 | 17.686208724975586 | 30.189868927001953 | 31.177425384521484 | 29.12896156311035 | 2.8887374580372125 | 0.203125 | 0.546875 |
| code_generation.jsonl | 16.856212615966797 | 21.272912979125977 | 14.11226749420166 | 26.3037109375 | 27.316545486450195 | 27.601707458496094 | 2.743945395370247 | 0.203125 | 0.5 |
| commonsense_completion.jsonl | 14.884931564331055 | 19.74518585205078 | 12.488748550415039 | 24.853830337524414 | 25.231971740722656 | 23.504011154174805 | 2.3961828001774848 | 0.296875 | 0.578125 |
| general_knowledge.jsonl | 16.805387496948242 | 21.47150421142578 | 14.456807136535645 | 26.696401596069336 | 28.698585510253906 | 26.56039810180664 | 2.3485806576209143 | 0.25 | 0.515625 |
| mathematics.jsonl | 20.423538208007812 | 25.10024070739746 | 17.787160873413086 | 30.39817237854004 | 31.45207977294922 | 31.44853973388672 | 2.636376297683455 | 0.25 | 0.53125 |
| multiple_choice_reasoning.jsonl | 14.824003219604492 | 19.474863052368164 | 12.550009727478027 | 24.865663528442383 | 25.591556549072266 | 24.40097999572754 | 2.273993310984224 | 0.234375 | 0.515625 |
| pronoun_coreference.jsonl | 14.938835144042969 | 19.851896286010742 | 12.58413028717041 | 24.907367706298828 | 25.819717407226562 | 24.174800872802734 | 2.354705204954371 | 0.265625 | 0.5625 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
