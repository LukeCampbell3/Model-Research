# PVR Router Regret Full-Network Alignment Audit

Status: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_AUDIT_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_NOT_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Full-network LM loss on official-like development files only. Uses bounded first-block file coverage to align with the oracle/regret audit without touching final official bounded files.

## Aggregate

Baseline micro loss: `14.361885888235909`
Regret0p01 micro loss: `15.250547817775182`
Micro delta: `0.888661929539273`
Macro delta: `0.888661929539273`
File wins: `0/7`

## Per File

| file | tokens | baseline | regret0p01 | delta |
|---|---:|---:|---:|---:|
| boolean_qa.jsonl | 128 | 16.18043613433838 | 16.688803672790527 | 0.5083675384521484 |
| code_generation.jsonl | 128 | 14.914155006408691 | 15.66997241973877 | 0.7558174133300781 |
| commonsense_completion.jsonl | 128 | 13.24062204360962 | 14.39100980758667 | 1.1503877639770508 |
| general_knowledge.jsonl | 128 | 14.327849864959717 | 15.424842834472656 | 1.0969929695129395 |
| mathematics.jsonl | 128 | 15.078142642974854 | 15.654743194580078 | 0.5766005516052246 |
| multiple_choice_reasoning.jsonl | 128 | 12.99281120300293 | 14.10064172744751 | 1.10783052444458 |
| pronoun_coreference.jsonl | 128 | 13.799184322357178 | 14.823821067810059 | 1.0246367454528809 |
