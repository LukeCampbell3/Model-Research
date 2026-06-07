# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE, PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY, PVR_EC_ROOT_CAUSE_INCONCLUSIVE, PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER

```json
{
  "metadata": {
    "timestamp": "2026-06-06T19:14:50.813281",
    "run_id": "algo_20260606_191450_smoke",
    "git_commit": "7d9af3bfed5260baa5c415658eb9206f52f3fc21",
    "docker_image": "N/A",
    "cuda_available": false,
    "gpu_name": "",
    "amp_enabled": false,
    "seed": 42,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --summarize-pvr-root-cause --input-dirs evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual --output-dir evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual",
    "model_variants": [
      "dense_baseline",
      "fixed_moe",
      "fixed_moe_looped_reference",
      "fixed_moe_vectorized",
      "adaptive_moe",
      "looped_moe",
      "full_system",
      "pvr_ec",
      "pvr_ec_matched",
      "pvr_ec_fixed_top2",
      "pvr_ec_no_prototypes",
      "pvr_ec_no_load_bias",
      "pvr_ec_no_extra_experts",
      "pvr_ec_deploy_top1",
      "pvr_ec_deploy_top2",
      "pvr_ec_deploy_bucketed",
      "pvr_ec_deploy_dense_masked_control",
      "pvr_ec_ownership_top1_frozen_candidate",
      "pvr_ec_ownership_top1_delta_small",
      "pvr_ec_ownership_top1_delta_medium",
      "pvr_ec_ownership_top1_delta_large",
      "pvr_ec_ownership_top1_full_expert_ffn_control",
      "pvr_ec_ownership_top1_rank_8",
      "pvr_ec_ownership_top1_rank_16",
      "pvr_ec_ownership_top1_rank_32",
      "pvr_ec_ownership_top1_rank_64",
      "pvr_ec_ownership_top1_rank_128",
      "pvr_ec_ownership_top1_micro_ffn_0_25x",
      "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "pvr_ec_ownership_top1_micro_ffn_1_0x",
      "pvr_ec_ownership_top1_delta_rank_8",
      "pvr_ec_ownership_top1_delta_rank_16",
      "pvr_ec_ownership_top1_delta_rank_32",
      "pvr_ec_ownership_top1_delta_rank_64",
      "pvr_ec_ownership_top1_delta_rank_128",
      "pvr_ec_learning_full",
      "pvr_ec_learning_shared_only",
      "pvr_ec_learning_sparse_only",
      "pvr_ec_learning_shared_scale_0_5",
      "pvr_ec_learning_expert_delta_scale_2_0",
      "pvr_ec_ownership_top1_delayed_candidate"
    ],
    "batch_sizes": [
      1,
      32
    ],
    "sequence_lengths": [
      64
    ],
    "train_steps": 30,
    "sample_limit": null,
    "mode": "smoke",
    "scale": "small",
    "families": [
      "clrs",
      "listops",
      "scan",
      "dyck"
    ],
    "input_dirs": [
      "evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual"
    ],
    "loaded_reports": [
      "evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual/per_dataset_metrics.json",
      "evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual/capacity_fairness_matrix_report.json",
      "evaluation/benchmark_results/docker_pvr_ec_learning_separation_actual/pvr_ec_root_baseline_matrix.json"
    ],
    "missing_dirs": [],
    "root_cause_flags": {
      "summarize_pvr_root_cause": true
    },
    "diagnostic_sweeps": {},
    "source": "root_summary"
  },
  "status": "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
  "statuses": [
    "PVR_EC_CAPABILITY_SIGNAL_TOO_WEAK_FOR_FINAL_ROOT_CAUSE",
    "PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY",
    "PVR_EC_DO_NOT_PROMOTE",
    "PVR_EC_LEARNING_SEPARATION_DIAGNOSTIC_READY",
    "PVR_EC_ROOT_CAUSE_INCONCLUSIVE",
    "PVR_EC_ROUTED_EXPERT_UNDERCONTRIBUTION_BLOCKER"
  ],
  "loss_curve": [
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.055410861968994,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.011942625045776,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.034436225891113,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.747157096862793,
      "accuracy": 0.012764801738185769
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.94768750667572,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.0001912117004395,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.115329027175903,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.9854363203048706,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.040038347244263,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.991278648376465,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.027424097061157,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.7537620067596436,
      "accuracy": 0.0021727322107550242
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.919965147972107,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.971233606338501,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.095717906951904,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.9625184535980225,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085163116455078,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162401199341,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354335784912,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.098124265670776,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.056512117385864,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.089036464691162,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.83061408996582,
      "accuracy": 0.0029875067897881585
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 3.997021198272705,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.045191287994385,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.165095090866089,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.036712646484375,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.137073040008545,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.094534397125244,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.119474411010742,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.764558792114258,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.035966396331787,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.086653232574463,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.186255216598511,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.066424131393433,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.132497549057007,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.089495658874512,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.11450719833374,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.759883642196655,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.031054496765137,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.081964015960693,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.18165135383606,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.0613112449646,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.135800838470459,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.092825651168823,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.117736101150513,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.764676094055176,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.033411979675293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.084055423736572,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.183526992797852,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.063687324523926,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.110387563705444,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756090879440308,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.040038347244263,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.991278648376465,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.027424097061157,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.7537620067596436,
      "accuracy": 0.0021727322107550242
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.919965147972107,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.971233606338501,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.095717906951904,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.9625184535980225,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085163116455078,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.110387563705444,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756090879440308,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.055410861968994,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.011942625045776,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.034436225891113,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.747157096862793,
      "accuracy": 0.012764801738185769
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.94768750667572,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.0001912117004395,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.115329027175903,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 30,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.9854363203048706,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.055410861968994,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.011942625045776,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.034436225891113,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.747157096862793,
      "accuracy": 0.012764801738185769
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.94768750667572,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.0001912117004395,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 4.115329027175903,
      "accuracy": 0.0
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.188356876373291,
      "eval_loss": 3.9854363203048706,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_micro_ffn_0_5x",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.040038347244263,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.991278648376465,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.027424097061157,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.7537620067596436,
      "accuracy": 0.0021727322107550242
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.919965147972107,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.971233606338501,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 4.095717906951904,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_16",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.193276882171631,
      "eval_loss": 3.9625184535980225,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085163116455078,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delta_rank_64",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162401199341,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.1103880405426025,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756091594696045,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354335784912,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_full",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.098124265670776,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.056512117385864,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.089036464691162,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.83061408996582,
      "accuracy": 0.0029875067897881585
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 3.997021198272705,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.045191287994385,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.165095090866089,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.260725021362305,
      "eval_loss": 4.036712646484375,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.137073040008545,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.094534397125244,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.119474411010742,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.764558792114258,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.035966396331787,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.086653232574463,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.186255216598511,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_sparse_only",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.2847065925598145,
      "eval_loss": 4.066424131393433,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.132497549057007,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.089495658874512,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.11450719833374,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.759883642196655,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.031054496765137,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.081964015960693,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.18165135383606,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_shared_scale_0_5",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.276189804077148,
      "eval_loss": 4.0613112449646,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.135800838470459,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.092825651168823,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.117736101150513,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.764676094055176,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.033411979675293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.084055423736572,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.183526992797852,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_learning_expert_delta_scale_2_0",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.281823635101318,
      "eval_loss": 4.063687324523926,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.12855339050293,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.085162878036499,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.110387563705444,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "listops",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.756090879440308,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.026487350463867,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.077600002288818,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.177354097366333,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_delayed_candidate",
      "family": "dyck",
      "seed": 42,
      "train_steps": 40,
      "train_loss": 4.269286155700684,
      "eval_loss": 4.056642293930054,
      "accuracy": 0.0
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```