# PVR-EC Family Regression Gate Report

**Status:** PVR_EC_FAMILY_REGRESSION_PASSED

**Statuses:** PVR_EC_FAMILY_REGRESSION_PASSED, PVR_EC_DO_NOT_PROMOTE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:36:17.135621",
    "run_id": "algo_20260607_183400_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-family-regression-gate --output-dir evaluation/benchmark_results/pvr_final_family_regression_gate",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 500,
    "sample_limit": 1000,
    "mode": "benchmark-lite",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null
  },
  "status": "PVR_EC_FAMILY_REGRESSION_PASSED",
  "statuses": [
    "PVR_EC_FAMILY_REGRESSION_PASSED",
    "PVR_EC_DO_NOT_PROMOTE"
  ],
  "promotion_ready": false,
  "passed": true,
  "catastrophic_family_collapse_count": 0,
  "per_family": {
    "clrs_style": {
      "loss": 0.22689872390280166,
      "accuracy": 0.502520822937563,
      "fixed_moe_loss": 0.20069633579502502,
      "fixed_moe_accuracy": 0.5212692965115258,
      "deploy_top1_loss": 0.26753168646246195,
      "deploy_top1_accuracy": 0.1713499366157629,
      "loss_gap_vs_fixed": 0.026202388107776642,
      "accuracy_gap_vs_fixed": -0.01874847357396281,
      "residual_help_rate": null,
      "residual_harm_rate": null,
      "calibration_proxy": 0.2683550492077147,
      "decision_token_help_rate": null,
      "token_to_sequence_transfer_ratio": null,
      "collapsed": false
    },
    "dyck": {
      "loss": 0.3387145114441713,
      "accuracy": 0.048634445778049054,
      "fixed_moe_loss": 0.3438807002579173,
      "fixed_moe_accuracy": 0.05197591728556389,
      "deploy_top1_loss": 0.3576503098011017,
      "deploy_top1_accuracy": 0.0,
      "loss_gap_vs_fixed": -0.0051661888137459755,
      "accuracy_gap_vs_fixed": -0.0033414715075148343,
      "residual_help_rate": null,
      "residual_harm_rate": null,
      "calibration_proxy": 0.01645183980060691,
      "decision_token_help_rate": null,
      "token_to_sequence_transfer_ratio": null,
      "collapsed": false
    },
    "listops": {
      "loss": 1.3296168148517609,
      "accuracy": 0.22673144975565915,
      "fixed_moe_loss": 1.3568206988275051,
      "fixed_moe_accuracy": 0.22077739706790991,
      "deploy_top1_loss": 1.589727409183979,
      "deploy_top1_accuracy": 0.08681121159355165,
      "loss_gap_vs_fixed": -0.027203883975744247,
      "accuracy_gap_vs_fixed": 0.005954052687749234,
      "residual_help_rate": null,
      "residual_harm_rate": null,
      "calibration_proxy": 0.09255414808465412,
      "decision_token_help_rate": null,
      "token_to_sequence_transfer_ratio": null,
      "collapsed": false
    },
    "scan_style": {
      "loss": 0.23926996998488903,
      "accuracy": 0.07071569531960922,
      "fixed_moe_loss": 0.23109520599246025,
      "fixed_moe_accuracy": 0.09004423939744492,
      "deploy_top1_loss": 0.2501062727533281,
      "deploy_top1_accuracy": 0.008169493393971418,
      "loss_gap_vs_fixed": 0.00817476399242878,
      "accuracy_gap_vs_fixed": -0.0193285440778357,
      "residual_help_rate": null,
      "residual_harm_rate": null,
      "calibration_proxy": 0.030651795944902048,
      "decision_token_help_rate": null,
      "token_to_sequence_transfer_ratio": null,
      "collapsed": false
    }
  },
  "model_table": {
    "fixed_moe_vectorized": {
      "params": 1001092,
      "avg_accuracy": 0.25857819999606313,
      "avg_exact_match": 0.00925,
      "avg_loss": 0.38860768983916694,
      "avg_qpc": 0.12928909999803156,
      "avg_loops": 1.0
    },
    "pvr_ec_deploy_top1": {
      "params": 614274,
      "avg_accuracy": 0.0771500010285979,
      "avg_exact_match": 0.0,
      "avg_loss": 0.45097945421002805,
      "avg_qpc": 0.0771500010285979,
      "avg_loops": 1.0
    },
    "pvr_ec_ownership_top1_final_candidate_v1": {
      "params": 482690,
      "avg_accuracy": 0.24662427509545803,
      "avg_exact_match": 0.0,
      "avg_loss": 0.39578524367728585,
      "avg_qpc": 0.24662427509545803,
      "avg_loops": 1.0
    }
  }
}
```