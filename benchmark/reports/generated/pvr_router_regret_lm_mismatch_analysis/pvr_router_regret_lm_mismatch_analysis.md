# PVR Router Regret / LM Mismatch Analysis

Status: `PVR_ROUTER_REGRET_LM_MISMATCH_ANALYSIS_COMPLETE`
Decision: `PVR_REGRET_REPAIR_ROUTER_METRIC_IMPROVEMENT_LM_GATE_MISMATCH_CONFIRMED`
Git commit: `bce74c6d7a7bd91cbe8b197f6bc5d37b6b22c457`

## Key Deltas

Final eval delta: `0.04692554473876953`
Mean eval delta: `0.29747772216796875`
Oracle selected-loss delta: `-0.971287727355957`
Oracle shared-only delta: `-0.7915183476039331`
Oracle router-regret delta: `-0.20840166567670942`
Selected-is-oracle delta: `0.07142857142857145`

## Eval Windows

| step | tokens | baseline | regret0p01 | delta |
|---:|---:|---:|---:|---:|
| 244 | 249856 | 25.925764083862305 | 26.456392288208008 | 0.5306282043457031 |
| 488 | 499712 | 19.938337326049805 | 20.444303512573242 | 0.5059661865234375 |
| 732 | 749568 | 12.092264175415039 | 12.198655128479004 | 0.10639095306396484 |
| 976 | 999424 | 12.02232837677002 | 12.069253921508789 | 0.04692554473876953 |

## Routing Curve Side Effect

Mean owner-entropy delta: `-0.08465312244175416`
Mean monopoly-rate delta: `0.09318033854166666`

## Oracle Per-File Deltas

| file | selected delta | shared delta | oracle delta | regret delta | oracle-rate delta | top2-rate delta |
|---|---:|---:|---:|---:|---:|---:|
| boolean_qa.jsonl | -1.690704345703125 | -1.4801273345947266 | -1.4594650268554688 | -0.23123726865742356 | 0.09375 | 0.0625 |
| code_generation.jsonl | -0.7870321273803711 | -0.5847110748291016 | -0.5573825836181641 | -0.22964896490884712 | 0.09375 | 0.109375 |
| commonsense_completion.jsonl | -0.5843172073364258 | -0.3070640563964844 | -0.29982566833496094 | -0.28449199977330863 | 0.125 | 0.125 |
| general_knowledge.jsonl | -0.7980575561523438 | -0.6028594970703125 | -0.5769681930541992 | -0.2210891500581056 | 0.078125 | 0.140625 |
| mathematics.jsonl | -1.3410625457763672 | -1.254216194152832 | -1.201096534729004 | -0.13996536756167188 | 0.0 | 0.046875 |
| multiple_choice_reasoning.jsonl | -0.8041772842407227 | -0.656102180480957 | -0.6248655319213867 | -0.17931039235554636 | 0.046875 | 0.109375 |
| pronoun_coreference.jsonl | -0.7936630249023438 | -0.655548095703125 | -0.6205959320068359 | -0.1730685164220631 | 0.0625 | 0.078125 |

## Diagnosis

The regret objective improves final-block expert selection on the oracle-audit distribution but over-concentrates owner utilization and does not transfer to the tiny training-eval windows. The block is therefore an evaluation-alignment plus over-regularized-routing problem, not a useless-expert problem.

## Recommendation

Do not promote regret0p01. Replace the four-window LM gate with a full official-like micro/macro gate, then test lower or annealed regret weights with an entropy/monopoly retention constraint.
