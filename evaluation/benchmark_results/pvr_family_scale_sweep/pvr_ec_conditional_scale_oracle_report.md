# PVR-EC Conditional Scale Oracle Report

**Status:** PVR_EC_BENCHMARK_TRANSFER_BLOCKER

**Statuses:** PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED, PVR_EC_BENCHMARK_TRANSFER_BLOCKER, PVR_EC_DO_NOT_PROMOTE, PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER, PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:08:45.615666",
    "run_id": "algo_20260607_020501_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --device cuda --amp --models pvr_ec_ownership_top1_constant_1,pvr_ec_ownership_top1_constant_2,pvr_ec_ownership_top1_constant_4,pvr_ec_ownership_top1_constant_8,pvr_ec_ownership_top1_scale_schedule_1_to_4,pvr_ec_ownership_top1_scale_schedule_1_to_8,pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4,pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2,pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2 --enable-ownership-map --ownership-map-mode frozen --run-family-scale-sweep --output-dir evaluation/benchmark_results/pvr_family_scale_sweep",
    "model_variants": [
      "pvr_ec_ownership_top1_constant_1",
      "pvr_ec_ownership_top1_constant_2",
      "pvr_ec_ownership_top1_constant_4",
      "pvr_ec_ownership_top1_constant_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2"
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
  "status": "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
  "statuses": [
    "PVR_EC_BENCHMARK_CAPABILITY_NOT_IMPROVED",
    "PVR_EC_BENCHMARK_TRANSFER_BLOCKER",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_EXPERT_RESIDUAL_ALIGNMENT_BLOCKER",
    "PVR_EC_RESIDUAL_ALIGNED_TO_BENCHMARK"
  ],
  "promotion_ready": false,
  "diagnostic_only": true,
  "conditional_scale_modes": [],
  "best_scale_by_family": {
    "clrs_style": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.29691687412559986,
      "accuracy": 0.11316433984218958,
      "quality_per_ms": 0.11316433984218958,
      "residual_help_rate": 0.8264945422609647,
      "residual_harm_rate": 0.17344332796831927,
      "expert_delta_contribution_pct": 0.9216747024683851,
      "shared_sparse_ratio": 0.11632063938304782,
      "logit_norm": 32.57727567354838,
      "prediction_entropy": 3.0151160607735314,
      "ECE_proxy": 0.07585505674053726,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "dyck": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.34985795958588517,
      "accuracy": 0.007735737371833997,
      "quality_per_ms": 0.007735737371833997,
      "residual_help_rate": 0.617033274223407,
      "residual_harm_rate": 0.3824177350228032,
      "expert_delta_contribution_pct": 0.9213600238542581,
      "shared_sparse_ratio": 0.11626412473075712,
      "logit_norm": 17.142101327578224,
      "prediction_entropy": 5.081983139117559,
      "ECE_proxy": 0.10213169811900635,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "listops": {
      "model": "pvr_ec_ownership_top1_constant_2",
      "scale": "constant_2",
      "loss": 1.6185197569429874,
      "accuracy": 0.09079930348817615,
      "quality_per_ms": 0.09079930348817615,
      "residual_help_rate": 0.6672876924276352,
      "residual_harm_rate": 0.3324915114790201,
      "expert_delta_contribution_pct": 0.5445934543660846,
      "shared_sparse_ratio": 0.8705231212079525,
      "logit_norm": 30.531910181045532,
      "prediction_entropy": 4.2816182076931,
      "ECE_proxy": 0.07973070513570683,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    },
    "scan_style": {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "scale": "warmup_hold_1_to_8",
      "loss": 0.24619679944589734,
      "accuracy": 0.01726854679620559,
      "quality_per_ms": 0.01726854679620559,
      "residual_help_rate": 0.4335414683446288,
      "residual_harm_rate": 0.5661997655406594,
      "expert_delta_contribution_pct": 0.920954350327362,
      "shared_sparse_ratio": 0.1170818216050975,
      "logit_norm": 17.200514554977417,
      "prediction_entropy": 5.044208720326424,
      "ECE_proxy": 0.09508745422584278,
      "owner_stability": 1.0,
      "prototype_owner_entropy": 0.0
    }
  },
  "best_scale_by_prototype": {
    "diagnostic_bucket_all": {
      "clrs_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.29691687412559986,
        "accuracy": 0.11316433984218958,
        "quality_per_ms": 0.11316433984218958,
        "residual_help_rate": 0.8264945422609647,
        "residual_harm_rate": 0.17344332796831927,
        "expert_delta_contribution_pct": 0.9216747024683851,
        "shared_sparse_ratio": 0.11632063938304782,
        "logit_norm": 32.57727567354838,
        "prediction_entropy": 3.0151160607735314,
        "ECE_proxy": 0.07585505674053726,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "dyck": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.34985795958588517,
        "accuracy": 0.007735737371833997,
        "quality_per_ms": 0.007735737371833997,
        "residual_help_rate": 0.617033274223407,
        "residual_harm_rate": 0.3824177350228032,
        "expert_delta_contribution_pct": 0.9213600238542581,
        "shared_sparse_ratio": 0.11626412473075712,
        "logit_norm": 17.142101327578224,
        "prediction_entropy": 5.081983139117559,
        "ECE_proxy": 0.10213169811900635,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "listops": {
        "model": "pvr_ec_ownership_top1_constant_2",
        "scale": "constant_2",
        "loss": 1.6185197569429874,
        "accuracy": 0.09079930348817615,
        "quality_per_ms": 0.09079930348817615,
        "residual_help_rate": 0.6672876924276352,
        "residual_harm_rate": 0.3324915114790201,
        "expert_delta_contribution_pct": 0.5445934543660846,
        "shared_sparse_ratio": 0.8705231212079525,
        "logit_norm": 30.531910181045532,
        "prediction_entropy": 4.2816182076931,
        "ECE_proxy": 0.07973070513570683,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "scan_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.24619679944589734,
        "accuracy": 0.01726854679620559,
        "quality_per_ms": 0.01726854679620559,
        "residual_help_rate": 0.4335414683446288,
        "residual_harm_rate": 0.5661997655406594,
        "expert_delta_contribution_pct": 0.920954350327362,
        "shared_sparse_ratio": 0.1170818216050975,
        "logit_norm": 17.200514554977417,
        "prediction_entropy": 5.044208720326424,
        "ECE_proxy": 0.09508745422584278,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      }
    }
  },
  "best_scale_by_owner": {
    "diagnostic_owner_all": {
      "clrs_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.29691687412559986,
        "accuracy": 0.11316433984218958,
        "quality_per_ms": 0.11316433984218958,
        "residual_help_rate": 0.8264945422609647,
        "residual_harm_rate": 0.17344332796831927,
        "expert_delta_contribution_pct": 0.9216747024683851,
        "shared_sparse_ratio": 0.11632063938304782,
        "logit_norm": 32.57727567354838,
        "prediction_entropy": 3.0151160607735314,
        "ECE_proxy": 0.07585505674053726,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "dyck": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.34985795958588517,
        "accuracy": 0.007735737371833997,
        "quality_per_ms": 0.007735737371833997,
        "residual_help_rate": 0.617033274223407,
        "residual_harm_rate": 0.3824177350228032,
        "expert_delta_contribution_pct": 0.9213600238542581,
        "shared_sparse_ratio": 0.11626412473075712,
        "logit_norm": 17.142101327578224,
        "prediction_entropy": 5.081983139117559,
        "ECE_proxy": 0.10213169811900635,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "listops": {
        "model": "pvr_ec_ownership_top1_constant_2",
        "scale": "constant_2",
        "loss": 1.6185197569429874,
        "accuracy": 0.09079930348817615,
        "quality_per_ms": 0.09079930348817615,
        "residual_help_rate": 0.6672876924276352,
        "residual_harm_rate": 0.3324915114790201,
        "expert_delta_contribution_pct": 0.5445934543660846,
        "shared_sparse_ratio": 0.8705231212079525,
        "logit_norm": 30.531910181045532,
        "prediction_entropy": 4.2816182076931,
        "ECE_proxy": 0.07973070513570683,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      },
      "scan_style": {
        "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
        "scale": "warmup_hold_1_to_8",
        "loss": 0.24619679944589734,
        "accuracy": 0.01726854679620559,
        "quality_per_ms": 0.01726854679620559,
        "residual_help_rate": 0.4335414683446288,
        "residual_harm_rate": 0.5661997655406594,
        "expert_delta_contribution_pct": 0.920954350327362,
        "shared_sparse_ratio": 0.1170818216050975,
        "logit_norm": 17.200514554977417,
        "prediction_entropy": 5.044208720326424,
        "ECE_proxy": 0.09508745422584278,
        "owner_stability": 1.0,
        "prototype_owner_entropy": 0.0
      }
    }
  },
  "conditional_scale_gain_over_global": -0.16438918584026396,
  "conditional_scale_overfit_risk": "high: oracle selected from validation rows; diagnostic only",
  "global_best_loss": 0.46348366168482846
}
```