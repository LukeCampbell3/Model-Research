# PVR-EC-O Routing Diagnostics Report Template

Hard invariants:

- owners_per_token == 1.0
- top2_execution_count == 0
- top4_execution_count == 0
- runtime_dynamic_k_count == 0
- runtime_expert_choice_count == 0
- production_map_mutated == false

Required diagnostics:

- prototype_entropy
- prototype_margin
- owner_entropy
- owner_churn
- expert_utilization
- expert_gini
- prototype_monopoly_rate
- high_gap_monopoly_rate
- challenger_disagreement_rate
- stale_owner_rate
- descriptor_control_margin
- operator_control_margin
- family_owner_accuracy_proxy
- failure_mode_distribution

If scores improve while invariants break, the result does not validate PVR-EC-O.

