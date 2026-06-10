# PVR-EC Final Deployment Gate Report

**Status:** PVR_EC_DEPLOY_CANDIDATE_CONFIRMED

**Statuses:** OK, PVR_EC_DEPLOY_CANDIDATE_CONFIRMED

```json
{
  "metadata": {
    "seed": 42,
    "input_dirs": [
      "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0"
    ],
    "command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line"
  },
  "status": "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
  "statuses": [
    "OK",
    "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED"
  ],
  "passed": true,
  "promotion_ready": true,
  "forward_purity_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_final_forward_purity_report.json"
  },
  "multi_seed_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_multiseed_confirmation_report.json"
  },
  "longer_training_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_longer_training_confirmation_report.json"
  },
  "matched_step_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_matched_step_report.json"
  },
  "matched_wall_clock_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_matched_wall_clock_report.json"
  },
  "calibration_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_final_calibration_sweep_report.json"
  },
  "family_regression_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_family_regression_gate_report.json"
  },
  "quality_per_ms_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_quality_per_ms_memory_gate_report.json"
  },
  "memory_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_quality_per_ms_memory_gate_report.json"
  },
  "reliability_proxy_gate": {
    "status": "OK",
    "statuses": [
      "OK"
    ],
    "passed": true,
    "_path": "/tmp/pytest-of-root/pytest-0/test_promotion_gate_passes_on_0/pvr_ec_reliability_proxy_gate_report.json"
  },
  "overall_verdict": "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
  "promotion_status": "PVR_EC_DEPLOY_CANDIDATE_CONFIRMED",
  "blocked_reasons": [],
  "missing_reports": [],
  "recommended_next_action": "promote to deploy-candidate shadow rollout"
}
```