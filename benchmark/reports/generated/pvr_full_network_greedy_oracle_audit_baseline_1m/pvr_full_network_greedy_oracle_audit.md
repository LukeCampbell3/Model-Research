# PVR Full-Network Greedy Oracle Audit

Status: `PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE`

Official-like development set only. Greedy blockwise full-network oracle; not exhaustive combinatorial oracle.

## Overall

Selected loss: `14.397206442696708`
Greedy full-network oracle loss: `9.663185937064034`
Greedy oracle improvement over selected: `-4.734020505632673`
Mean router regret across block decisions: `0.21931452417834413`
Selected-is-oracle rate across block decisions: `0.3756510416666667`
Selected-is-top2 rate across block decisions: `0.4732142857142857`

## Per File

| file | selected | greedy oracle | delta | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | 17.779340744018555 | 12.33748722076416 | -5.4418535232543945 | 0.3723958333333333 | 0.4654947916666667 |
| code_generation.jsonl | 13.739109992980957 | 9.16604232788086 | -4.573067665100098 | 0.3736979166666667 | 0.47265625 |
| commonsense_completion.jsonl | 12.68628215789795 | 8.271618843078613 | -4.414663314819336 | 0.3841145833333333 | 0.478515625 |
| general_knowledge.jsonl | 14.186077117919922 | 9.280488014221191 | -4.9055891036987305 | 0.3743489583333333 | 0.4694010416666667 |
| mathematics.jsonl | 16.454639434814453 | 11.52812385559082 | -4.926515579223633 | 0.3795572916666667 | 0.47265625 |
| multiple_choice_reasoning.jsonl | 13.268644332885742 | 8.6172513961792 | -4.651392936706543 | 0.3704427083333333 | 0.470703125 |
| pronoun_coreference.jsonl | 12.666351318359375 | 8.441289901733398 | -4.225061416625977 | 0.375 | 0.4830729166666667 |
