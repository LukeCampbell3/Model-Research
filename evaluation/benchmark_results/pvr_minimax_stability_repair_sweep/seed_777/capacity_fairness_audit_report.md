# PVR-EC Capacity Fairness Audit

**Status:** PVR_EC_CAPACITY_FAIRNESS_AUDIT_READY

- same_seed: True
- same_train_eval_split: True
- same_labels_objective: True
- same_benchmark_family: True
- same_target_preprocessing: True
- same_loss_computation: True
- same_batch_size: True
- same_amp_mode: True
- same_number_of_train_steps: True
- same_optimizer_schedule: True
- same_eval_mode: True
- same_ownership_map_mode: True
- same_route_policy_ownership_top1: True
- exactly_one_owner: True
- top2_executions_zero: True
- top4_executions_zero: True
- no_hidden_dense_all_expert_execution: True
- no_oracle_owner_used_at_inference: True
- no_forced_action_path_used_in_deploy: True
- no_replay_probe_data_used_as_eval_labels: True