# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T18:01:24.148585",
    "run_id": "algo_20260607_175654_benchmark-lite",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps-list 500,1000,2000 --seed-list 42,123,777 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-longer-training-confirmation-gate --output-dir evaluation/benchmark_results/pvr_final_longer_training_confirmation",
    "model_variants": [
      "fixed_moe_vectorized",
      "pvr_ec_ownership_top1_final_candidate_v1"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 1000,
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
      "run_longer_training_confirmation_gate": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        1000
      ],
      "seed_list": [
        123
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "max_train_seconds": null
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
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.06896085757762194,
      "accuracy": 0.8514545454545455
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.092287452891469,
      "accuracy": 0.7284462340123165
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.06754930270835757,
      "accuracy": 0.8501742160278746
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 1.377507422119379,
      "accuracy": 0.27568000884564353
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.17386889271438122,
      "accuracy": 0.12398246712586099
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.25961677357554436,
      "accuracy": 0.09690601284296556
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.37253675051033497,
      "accuracy": 0.1000418147606105
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.03698534891009331,
      "eval_loss": 0.244341142475605,
      "accuracy": 0.14929577464788732
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.0790882152505219,
      "accuracy": 0.8412727272727273
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.09240335645154119,
      "accuracy": 0.7466840360018948
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.07883149944245815,
      "accuracy": 0.8519163763066202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 1.2492872700095177,
      "accuracy": 0.34981755860238833
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.1764768846333027,
      "accuracy": 0.21227301189730746
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.2583855129778385,
      "accuracy": 0.2069468768242849
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.3615901656448841,
      "accuracy": 0.3448672381350617
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 1000,
      "train_loss": 0.04325160011649132,
      "eval_loss": 0.241717167198658,
      "accuracy": 0.3420523138832998
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.5,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```