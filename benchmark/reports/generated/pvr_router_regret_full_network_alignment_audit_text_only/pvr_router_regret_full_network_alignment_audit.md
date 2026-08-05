# PVR Router Regret Full-Network Alignment Audit

Status: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_AUDIT_COMPLETE`
Decision: `PVR_ROUTER_REGRET_REPAIR_FULL_NETWORK_ALIGNMENT_NOT_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Full-network LM loss on official-like development files only. Uses bounded file coverage to align with the oracle/regret audit without touching final official bounded files.
JSONL text field: `text`

## Aggregate

Baseline micro loss: `7.328907796314785`
Regret0p01 micro loss: `7.251809903553554`
Micro delta: `-0.07709789276123047`
Macro delta: `-0.07709789276123047`
File wins: `3/7`

## Per File

| file | tokens | baseline | regret0p01 | delta |
|---|---:|---:|---:|---:|
| boolean_qa.jsonl | 64 | 5.3582916259765625 | 4.901805877685547 | -0.4564857482910156 |
| code_generation.jsonl | 64 | 15.673322677612305 | 13.396895408630371 | -2.2764272689819336 |
| commonsense_completion.jsonl | 64 | 2.5688135623931885 | 2.4242489337921143 | -0.14456462860107422 |
| general_knowledge.jsonl | 64 | 3.0157980918884277 | 3.1334850788116455 | 0.11768698692321777 |
| mathematics.jsonl | 64 | 17.68661117553711 | 19.675323486328125 | 1.9887123107910156 |
| multiple_choice_reasoning.jsonl | 64 | 4.214886665344238 | 4.37178897857666 | 0.15690231323242188 |
| pronoun_coreference.jsonl | 64 | 2.78463077545166 | 2.859121561050415 | 0.07449078559875488 |
