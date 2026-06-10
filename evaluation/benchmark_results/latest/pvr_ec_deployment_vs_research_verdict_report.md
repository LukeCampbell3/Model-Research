# PVR-EC Deployment vs Research Verdict Report

**Status:** PVR_EC_REPEATABILITY_BLOCKED

**Statuses:** PVR_EC_ALGORITHMIC_STAGE_COMPLETE, PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE, PVR_EC_DO_NOT_PROMOTE, PVR_EC_NLP_BRIDGE_LADDER_REQUIRED, PVR_EC_NLP_BRIDGE_STAGE_1_READY, PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS, PVR_EC_REPEATABILITY_BLOCKED

```json
{
  "metadata": {
    "seed": 42,
    "input_dirs": [
      "/tmp/pytest-of-root/pytest-0/test_qpm_blocked_but_classifie0"
    ],
    "command": "/opt/conda/lib/python3.10/site-packages/pytest/__main__.py sparse_loop_moe/tests/test_pvr_ec.py sparse_loop_moe/tests/test_pvr_ec_ownership.py sparse_loop_moe/tests/test_pvr_ec_family_preservation.py sparse_loop_moe/tests/test_pvr_ec_final_deployment_gate.py sparse_loop_moe/tests/test_pvr_ec_descriptor_semantic_identity_repair.py sparse_loop_moe/tests/test_pvr_ec_same_input_wrong_descriptor.py -q --tb=line"
  },
  "status": "PVR_EC_REPEATABILITY_BLOCKED",
  "deployment_verdict": "PVR_EC_REPEATABILITY_BLOCKED",
  "research_verdict": "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
  "statuses": [
    "PVR_EC_ALGORITHMIC_STAGE_COMPLETE",
    "PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_NLP_BRIDGE_LADDER_REQUIRED",
    "PVR_EC_NLP_BRIDGE_STAGE_1_READY",
    "PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS",
    "PVR_EC_REPEATABILITY_BLOCKED"
  ],
  "promotion_ready": false,
  "research_ready": true,
  "collapse_count": 1,
  "unexplained_collapse_count": 0,
  "qpm_classified": true,
  "calibration_measured": true,
  "mean_competitive": true,
  "forward_purity": true,
  "missing_reports": []
}
```