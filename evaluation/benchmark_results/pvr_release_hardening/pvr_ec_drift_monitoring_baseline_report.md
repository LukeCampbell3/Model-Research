# pvr_ec_drift_monitoring_baseline_report
```json
{
  "status": "PVR_EC_DRIFT_MONITORING_BASELINES_CREATED",
  "baselines": {
    "descriptor_control_margin": {
      "baseline_mean": 0.187,
      "baseline_std": 0.05,
      "warning_threshold": 0.08,
      "critical_threshold": 0.05,
      "rollback_threshold": 0.03
    },
    "owners_per_token": {
      "baseline_mean": 1.0,
      "rollback_threshold": "!=1.0"
    },
    "top2_executions": {
      "baseline_mean": 0,
      "rollback_threshold": ">0"
    },
    "calibration_proxy": {
      "baseline_mean": 0.009,
      "baseline_std": 0.005,
      "warning_threshold": 0.019,
      "critical_threshold": 0.029,
      "rollback_threshold": 0.039
    },
    "qpm_tokens_per_second": {
      "baseline_mean": 50000,
      "warning_threshold": 45000,
      "critical_threshold": 40000,
      "rollback_threshold": 35000
    },
    "memory_peak_mb": {
      "baseline_mean": 500,
      "warning_threshold": 550,
      "critical_threshold": 600,
      "rollback_threshold": 650
    },
    "unknown_failure_count": {
      "baseline_mean": 0,
      "warning_threshold": 1,
      "rollback_threshold": 1
    }
  }
}
```