# PVR Full-Network Greedy Oracle Audit

Status: `PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE`

Official-like development set only. Greedy blockwise full-network oracle; not exhaustive combinatorial oracle.

## Overall

Selected loss: `9.797280992780413`
Greedy full-network oracle loss: `5.548307282584054`
Greedy oracle improvement over selected: `-4.248973710196359`
Mean router regret across block decisions: `0.5827385857234335`
Selected-is-oracle rate across block decisions: `0.15187872023809523`
Selected-is-top2 rate across block decisions: `0.2560453869047619`

## Per File

| file | selected | greedy oracle | delta | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | 11.519908905029297 | 6.9465436935424805 | -4.573365211486816 | 0.14713541666666666 | 0.22916666666666666 |
| code_generation.jsonl | 9.461551666259766 | 5.420115947723389 | -4.041435718536377 | 0.146484375 | 0.2584635416666667 |
| commonsense_completion.jsonl | 8.599151611328125 | 4.778065204620361 | -3.8210864067077637 | 0.162109375 | 0.2662760416666667 |
| general_knowledge.jsonl | 9.94315242767334 | 5.498633861541748 | -4.444518566131592 | 0.14518229166666666 | 0.251953125 |
| mathematics.jsonl | 11.186300277709961 | 6.930014610290527 | -4.256285667419434 | 0.14973958333333334 | 0.263671875 |
| multiple_choice_reasoning.jsonl | 8.970507621765137 | 4.625448226928711 | -4.345059394836426 | 0.16015625 | 0.2591145833333333 |
| pronoun_coreference.jsonl | 8.900394439697266 | 4.639329433441162 | -4.2610650062561035 | 0.15234375 | 0.263671875 |
