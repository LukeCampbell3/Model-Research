# PVR Final-Block Expert Sweep and Router-Regret Audit

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

## Overall

Selected loss: `10.188022635877132`
Shared-only loss: `13.41137558221817`
Oracle loss: `8.718795716762543`
Mean wrong loss: `17.686156630516052`
Shifted wrong loss: `22.860915899276733`
Random wrong loss: `17.708617389202118`
Shuffled residual loss: `10.28586482256651`
Random residual loss: `20.23269349336624`
Mean router regret: `1.469227062610173`
95th-percentile router regret: `5.583189487457275`
Selected-is-oracle rate: `0.17779541015625`
Selected-is-top2 rate: `0.34967041015625`

## Claim Gates

- selected_beats_shared_only: `True`
- selected_beats_mean_wrong: `True`
- selected_beats_shuffled_residual: `True`
- selected_beats_random_residual: `True`
- selected_intervention_gate_pass: `True`
- final_block_oracle_beats_switch_top1: `True`
- final_block_oracle_beats_generic_top2: `True`

## Final-Block Oracle vs Comparators

Compares final-block oracle intervention loss to independently evaluated comparator micro losses on the same official file/block budget. This is diagnostic capacity evidence, not a deployable full-network oracle model.

| comparator | comparator micro loss | oracle - comparator |
|---|---:|---:|
| dense_sparse_v2_300m_matched | 10.875021406449378 | -2.156225689686835 |
| switch_top1_sparse_v2_300m_matched | 9.429242825135589 | -0.7104471083730459 |
| generic_top2_sparse_v2_300m_matched | 9.727309678681195 | -1.008513961918652 |

## Per File

| file | selected | shared | oracle | mean wrong | shifted wrong | random wrong | regret | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| arc_challenge.jsonl | 11.146246671676636 | 14.723727703094482 | 9.728120684623718 | 19.02572202682495 | 24.49974489212036 | 19.110618114471436 | 1.41812602034679 | 0.20947265625 | 0.3857421875 |
| boolq.jsonl | 5.249226868152618 | 7.946238279342651 | 3.9772796630859375 | 12.186613082885742 | 17.5457763671875 | 12.114495038986206 | 1.2719474066359453 | 0.14501953125 | 0.33056640625 |
| gsm8k.jsonl | 11.530145168304443 | 14.577737092971802 | 10.036239624023438 | 18.830865383148193 | 24.11257028579712 | 18.837098598480225 | 1.4939062037524309 | 0.1708984375 | 0.330078125 |
| hellaswag.jsonl | 8.094555497169495 | 11.42107605934143 | 6.83783745765686 | 15.687824249267578 | 21.010676383972168 | 15.78612232208252 | 1.2567181476633777 | 0.1669921875 | 0.35400390625 |
| humaneval.jsonl | 13.105716705322266 | 16.18241810798645 | 11.382455945014954 | 20.399721384048462 | 25.351381301879883 | 20.419406414031982 | 1.7232608049671398 | 0.1552734375 | 0.31396484375 |
| mbpp.jsonl | 13.78136420249939 | 17.0184907913208 | 11.982801914215088 | 21.392043113708496 | 25.919256687164307 | 21.416580200195312 | 1.7985622700944077 | 0.185546875 | 0.35107421875 |
| mmlu.jsonl | 8.303616523742676 | 11.652148485183716 | 6.958513021469116 | 15.872840166091919 | 21.185224533081055 | 16.026430368423462 | 1.3451036610042593 | 0.1845703125 | 0.3701171875 |
| winogrande.jsonl | 10.293309450149536 | 13.769168138504028 | 8.84711742401123 | 18.093623638153076 | 23.262696743011475 | 17.9581880569458 | 1.446191986417034 | 0.20458984375 | 0.36181640625 |

Full-network oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`
Full-network oracle improvement over Switch/Top2: `NOT_RUN_NOT_IMPLEMENTED`
