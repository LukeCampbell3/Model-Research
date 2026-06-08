# PVR-EC Deployment vs Research Verdict Report

**Status:** PVR_EC_REPEATABILITY_BLOCKED

**Statuses:** PVR_EC_ALGORITHMIC_STAGE_COMPLETE, PVR_EC_DEPLOYMENT_BLOCKED_BUT_RESEARCHABLE, PVR_EC_DO_NOT_PROMOTE, PVR_EC_NLP_BRIDGE_LADDER_REQUIRED, PVR_EC_NLP_BRIDGE_STAGE_1_READY, PVR_EC_NLP_RESEARCH_READY_WITH_BLOCKERS, PVR_EC_REPEATABILITY_BLOCKED

```json
{
  "metadata": {
    "seed": 42,
    "input_dirs": [
      "C:\\Users\\jcthi\\AppData\\Local\\Temp\\pytest-of-jcthi\\pytest-144\\test_qpm_blocked_but_classifie0"
    ],
    "command": "C:\\Users\\jcthi\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts\\pytest -q sparse_loop_moe/tests/test_pvr_ec.py -k minimax or nlp_research or qpm or collapse"
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