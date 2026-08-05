# PVR Router Regret Full-Network Alignment Audit

Status: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_AUDIT_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Full-network LM loss on official-like development files only. Uses bounded first-block file coverage to align with the oracle/regret audit without touching final official bounded files.

## Aggregate

Baseline micro loss: `14.397206851414271`
Regret0p01 micro loss: `13.425919805254255`
Micro delta: `-0.9712870461600165`
Macro delta: `-0.9712870461600165`
File wins: `7/7`

## Per File

| file | tokens | baseline | regret0p01 | delta |
|---|---:|---:|---:|---:|
| boolean_qa.jsonl | 64 | 17.779340744018555 | 16.088638305664062 | -1.6907024383544922 |
| code_generation.jsonl | 64 | 13.739110946655273 | 12.952077865600586 | -0.7870330810546875 |
| commonsense_completion.jsonl | 64 | 12.686284065246582 | 12.101963996887207 | -0.584320068359375 |
| general_knowledge.jsonl | 64 | 14.186076164245605 | 13.388019561767578 | -0.7980566024780273 |
| mathematics.jsonl | 64 | 16.454639434814453 | 15.113580703735352 | -1.3410587310791016 |
| multiple_choice_reasoning.jsonl | 64 | 13.268646240234375 | 12.464466094970703 | -0.8041801452636719 |
| pronoun_coreference.jsonl | 64 | 12.666350364685059 | 11.872692108154297 | -0.7936582565307617 |
