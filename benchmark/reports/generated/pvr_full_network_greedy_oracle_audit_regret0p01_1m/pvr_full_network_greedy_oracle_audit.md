# PVR Full-Network Greedy Oracle Audit

Status: `PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE`

Official-like development set only. Greedy blockwise full-network oracle; not exhaustive combinatorial oracle.

## Overall

Selected loss: `13.425919669015068`
Greedy full-network oracle loss: `8.275502681732178`
Greedy oracle improvement over selected: `-5.150416987282889`
Mean router regret across block decisions: `0.24372767678739912`
Selected-is-oracle rate across block decisions: `0.3561197916666667`
Selected-is-top2 rate across block decisions: `0.45600818452380953`

## Per File

| file | selected | greedy oracle | delta | oracle rate | top2 rate |
|---|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | 16.088640213012695 | 10.401402473449707 | -5.687237739562988 | 0.3463541666666667 | 0.4453125 |
| code_generation.jsonl | 12.952077865600586 | 7.962888717651367 | -4.989189147949219 | 0.3567708333333333 | 0.4563802083333333 |
| commonsense_completion.jsonl | 12.10196304321289 | 7.143885135650635 | -4.958077907562256 | 0.3619791666666667 | 0.4563802083333333 |
| general_knowledge.jsonl | 13.388018608093262 | 8.146272659301758 | -5.241745948791504 | 0.3548177083333333 | 0.455078125 |
| mathematics.jsonl | 15.113577842712402 | 9.944528579711914 | -5.169049263000488 | 0.35546875 | 0.45703125 |
| multiple_choice_reasoning.jsonl | 12.464468002319336 | 7.199006080627441 | -5.2654619216918945 | 0.3489583333333333 | 0.4537760416666667 |
| pronoun_coreference.jsonl | 11.872692108154297 | 7.130535125732422 | -4.742156982421875 | 0.3684895833333333 | 0.4680989583333333 |
