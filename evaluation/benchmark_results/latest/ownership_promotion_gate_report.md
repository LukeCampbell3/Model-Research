# Ownership Promotion Gate Report

**Status:** PVR_EC_OWNERSHIP_PROMOTION_GATE_NOT_CLEAN

## Blocked Reasons
- LOSS_REGRESSION
- ORACLE_GAP_REGRESSION
- OWNER_CHANGE_SUCCESS_TOO_LOW
- OWNER_CHANGE_TOO_RARE

## Data
```json
{
  "promotion_decision": false,
  "promotion_blocked_reasons": [
    "LOSS_REGRESSION",
    "ORACLE_GAP_REGRESSION",
    "OWNER_CHANGE_SUCCESS_TOO_LOW",
    "OWNER_CHANGE_TOO_RARE"
  ],
  "loss_gate_passed": false,
  "oracle_gap_gate_passed": false,
  "quality_per_ms_gate_passed": true,
  "latency_gate_passed": true,
  "owner_change_success_gate_passed": false,
  "candidate_recall_gate_passed": true,
  "confidence_calibration_gate_passed": true,
  "prototype_monopoly_gate_passed": true,
  "reproduction_gate_passed": true,
  "seed_repeatability_gate_passed": true,
  "status": "PVR_EC_OWNERSHIP_PROMOTION_GATE_NOT_CLEAN"
}
```