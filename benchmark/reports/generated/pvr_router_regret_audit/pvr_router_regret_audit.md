# PVR Router Regret Audit

Status: `PVR_ROUTER_REGRET_BOTTLENECK_DIAGNOSTIC_SUPPORTED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

Consolidates existing final-block frozen-official and greedy full-network official-like development audits. No training and no final official-file tuning.

## Frozen Official Final-Block Sweep

This uses identical final-block hidden states and evaluates every final-block expert. It is not a full-network oracle.

Selected loss: `10.188022635877132`
Shared-only loss: `13.41137558221817`
Oracle loss: `8.718795716762543`
Mean wrong loss: `17.686156630516052`
Mean router regret: `1.469227062610173`
Selected-is-oracle rate: `0.17779541015625`
Selected-is-top2 rate: `0.34967041015625`

## Official-Like Development Full-Network Greedy Oracle

This uses official-like development data only and greedily chooses per-block oracle experts. It is not exhaustive.

Selected loss: `9.797280992780413`
Greedy oracle loss: `5.548307282584054`
Greedy oracle improvement: `-4.248973710196359`
Mean router regret across block decisions: `0.5827385857234335`
Selected-is-oracle rate: `0.15187872023809523`
Selected-is-top2 rate: `0.2560453869047619`

## Diagnosis

Router regret is material in diagnostic audits. Expert-bank capacity exists under oracle-style interventions, so router repair should precede scaling. Because the full-network audit is greedy and development-only, this does not prove a deployable oracle model or an official benchmark advantage.

## Blocked / Not Run

- local_paired_heldout_full_network_oracle: `NOT_RUN_NOT_IMPLEMENTED`
- frozen_official_full_network_oracle: `NOT_RUN_NOT_IMPLEMENTED`
- oracle_vs_comparators_on_identical_official_like_windows: `PARTIAL_DIAGNOSTIC_ONLY`
