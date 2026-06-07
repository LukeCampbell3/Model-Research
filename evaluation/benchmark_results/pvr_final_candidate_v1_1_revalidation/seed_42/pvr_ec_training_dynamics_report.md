# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T20:08:01.397829",
    "run_id": "algo_20260607_200559_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1_1 --enable-ownership-map --ownership-map-mode frozen --run-final-candidate-revalidation --output-dir evaluation/benchmark_results/pvr_final_candidate_v1_1_revalidation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_deploy_top1",
      "pvr_ec_ownership_top1_final_candidate_v1_1"
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
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_multiseed_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        42
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": []
    },
    "source": "trained_benchmark"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE"
  ],
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.21254643518477678,
      "accuracy": 0.49845454545454543
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19413983263075352,
      "accuracy": 0.524896510940272
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19540273770689964,
      "accuracy": 0.54045683313976
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 1.3568207398056984,
      "accuracy": 0.22077739706790991
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.19047189597040415,
      "accuracy": 0.1043172898161537
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.27171850576996803,
      "accuracy": 0.07577118897873615
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.4121997430920601,
      "accuracy": 0.02989242863053372
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.13683609664440155,
      "eval_loss": 0.2755616481105487,
      "accuracy": 0.07405940594059406
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.27750235982239246,
      "accuracy": 0.1831818181818182
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2479988867416978,
      "accuracy": 0.19101123595505617
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2770938128232956,
      "accuracy": 0.13985675571041425
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 1.589727409183979,
      "accuracy": 0.08681121159355165
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2083501284942031,
      "accuracy": 0.01094815120842801
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2918624170124531,
      "accuracy": 0.005390835579514825
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.42143215239048004,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.17677822709083557,
      "eval_loss": 0.2938684672117233,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2684176554903388,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2337717628106475,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2541435593739152,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3323042541742325,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.21845487412065268,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.30021874606609344,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.42397674173116684,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.29410430788993835,
      "accuracy": 0.06158415841584158
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.6666666666666666,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```