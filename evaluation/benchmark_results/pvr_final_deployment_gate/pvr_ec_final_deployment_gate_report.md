# pvr_ec_final_deployment_gate_report
```json
{
  "status": "PVR_EC_DEPLOYMENT_BLOCKED_DESCRIPTOR_CONTROL",
  "deployment_verdict": "PVR_EC_DEPLOYMENT_BLOCKED_DESCRIPTOR_CONTROL",
  "research_verdict": "PVR_EC_RESEARCH_CANDIDATE_CONFIRMED_WITH_BLOCKERS",
  "hard_invariants": {
    "owners_per_token": 1.0,
    "top2_executions": 0,
    "top4_executions": 0,
    "production_map_mutated": false,
    "file_writes_in_forward": 0,
    "cpu_gpu_syncs_in_forward": 0
  },
  "gates": {
    "forward_purity": true,
    "multiseed_repeatability": true,
    "qpm_memory": true,
    "calibration_reliability": true,
    "descriptor_control": false,
    "family_task_regression": true,
    "failure_observatory": true
  },
  "metrics": {
    "mean_accuracy": 0.8344592278202375,
    "std_accuracy": 0.054568236382334934,
    "qpm_pass_rate": 1.0,
    "high_confidence_failure_rate": 0.008886810102899906,
    "descriptor_control_margin": 0.012359023094177246,
    "collapsed_tasks": []
  },
  "unknown_failures": 0,
  "total_time_s": 822.2330164909363
}
```