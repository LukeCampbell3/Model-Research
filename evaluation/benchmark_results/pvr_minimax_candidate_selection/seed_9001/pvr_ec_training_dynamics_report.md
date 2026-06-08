# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:09:13.405937",
    "run_id": "algo_20260608_000419_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 9001,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_deploy_top1,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-minimax-candidate-selection --minimax-variants v1,v1_1_logit_norm_medium,sparse_ce_0_03_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_light,sparse_ce_0_05_plus_logit_norm_medium,sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light,sparse_ce_0_03_plus_temperature_T_1_2,sparse_ce_0_05_plus_temperature_T_1_2 --output-dir evaluation/benchmark_results/pvr_minimax_candidate_selection",
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
      "dyck",
      "listops",
      "scan"
    ],
    "pvr_expert_delta_scale": null,
    "pvr_expert_delta_scale_schedule": "constant",
    "pvr_expert_delta_scale_start": null,
    "pvr_expert_delta_scale_end": null,
    "pvr_expert_delta_scale_warmup_steps": null,
    "pvr_expert_delta_scale_hold_steps": null,
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_minimax_candidate_selection": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        9001
      ],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "shape_pairs": [],
      "max_train_seconds": null,
      "repeatability_repair_variants": [],
      "calibration_repair_variants": [],
      "minimax_variants": [
        "v1",
        "v1_1_logit_norm_medium",
        "sparse_ce_0_03_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_light",
        "sparse_ce_0_05_plus_logit_norm_medium",
        "sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
        "sparse_ce_0_03_plus_temperature_T_1_2",
        "sparse_ce_0_05_plus_temperature_T_1_2"
      ],
      "stability_repair_variants": []
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
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.2734601888805628,
      "accuracy": 0.2060909090909091
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.2501998506486416,
      "accuracy": 0.12647893989588263
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.2661430248990655,
      "accuracy": 0.20121951219512196
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 1.4469235464930534,
      "accuracy": 0.16431558405352661
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.20035526901483536,
      "accuracy": 0.039898132427843805
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.3095713369548321,
      "accuracy": 0.017948717948717947
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.4265357404947281,
      "accuracy": 0.0051094890510948905
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.21663734316825867,
      "eval_loss": 0.29674165695905685,
      "accuracy": 0.005964214711729622
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.31883946247398853,
      "accuracy": 0.06190909090909091
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.26595548912882805,
      "accuracy": 0.13014671083767157
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.3045526444911957,
      "accuracy": 0.11788617886178862
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 1.4543479792773724,
      "accuracy": 0.09333705045999442
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.1965663619339466,
      "accuracy": 0.0632427843803056
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.3031237870454788,
      "accuracy": 0.022792022792022793
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.4195854552090168,
      "accuracy": 0.005005213764337852
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.23124676942825317,
      "eval_loss": 0.2891395427286625,
      "accuracy": 0.015109343936381709
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.18465076573193073,
      "accuracy": 0.6717272727272727
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.15848463959991932,
      "accuracy": 0.6961665877898722
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.1655649822205305,
      "accuracy": 0.740418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 1.3665190674364567,
      "accuracy": 0.22974630610538055
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.18681376799941063,
      "accuracy": 0.1133276740237691
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.29086403734982014,
      "accuracy": 0.0737891737891738
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.39376775547862053,
      "accuracy": 0.06319082377476538
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.26814668998122215,
      "accuracy": 0.09940357852882704
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.18785096798092127,
      "accuracy": 0.6850909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.16310950182378292,
      "accuracy": 0.7055134879318504
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.16840767674148083,
      "accuracy": 0.7478706929926442
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 1.3361185565590858,
      "accuracy": 0.235321996097017
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.18679546657949686,
      "accuracy": 0.11863327674023769
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.2912413068115711,
      "accuracy": 0.07891737891737892
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.39197209291160107,
      "accuracy": 0.06100104275286757
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.2666246195634206,
      "accuracy": 0.09025844930417495
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.2157498337328434,
      "accuracy": 0.488
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.1802997225895524,
      "accuracy": 0.5179839091339328
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.20616925694048405,
      "accuracy": 0.544425087108014
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 1.3886786438524723,
      "accuracy": 0.1815723445776415
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.19191314559429884,
      "accuracy": 0.10908319185059423
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.2967529222369194,
      "accuracy": 0.07122507122507123
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.40048934891819954,
      "accuracy": 0.05234619395203337
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.2760479847590129,
      "accuracy": 0.07117296222664016
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.18465076573193073,
      "accuracy": 0.6717272727272727
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.15848463959991932,
      "accuracy": 0.6961665877898722
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.1655649822205305,
      "accuracy": 0.740418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 1.3665190674364567,
      "accuracy": 0.22974630610538055
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.18681376799941063,
      "accuracy": 0.1133276740237691
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.29086403734982014,
      "accuracy": 0.0737891737891738
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.39376775547862053,
      "accuracy": 0.06319082377476538
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.26814668998122215,
      "accuracy": 0.09940357852882704
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.18785096798092127,
      "accuracy": 0.6850909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.16310950182378292,
      "accuracy": 0.7055134879318504
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.16840767674148083,
      "accuracy": 0.7478706929926442
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 1.3361185565590858,
      "accuracy": 0.235321996097017
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.18679546657949686,
      "accuracy": 0.11863327674023769
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.2912413068115711,
      "accuracy": 0.07891737891737892
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.39197209291160107,
      "accuracy": 0.06100104275286757
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18648390471935272,
      "eval_loss": 0.2666246195634206,
      "accuracy": 0.09025844930417495
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.22885482758283615,
      "accuracy": 0.4576363636363636
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.19133334327489138,
      "accuracy": 0.5179839091339328
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.22089056856930256,
      "accuracy": 0.4981610530391018
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 1.3845932073891163,
      "accuracy": 0.17931419013102873
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.19168713968247175,
      "accuracy": 0.11544991511035653
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.2972062546759844,
      "accuracy": 0.07065527065527065
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.4017120823264122,
      "accuracy": 0.05307612095933264
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.2060525119304657,
      "eval_loss": 0.27543962995211285,
      "accuracy": 0.07375745526838966
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.17978218756616116,
      "accuracy": 0.6880909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.15587026439607143,
      "accuracy": 0.7079981069569332
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.16035291086882353,
      "accuracy": 0.7563879210220673
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 1.3206367902457714,
      "accuracy": 0.240674658488988
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.18693546671420336,
      "accuracy": 0.11375212224108659
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.2917536050081253,
      "accuracy": 0.0754985754985755
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.3929861579090357,
      "accuracy": 0.052763295099061525
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.17750969529151917,
      "eval_loss": 0.26710785056153935,
      "accuracy": 0.07972166998011929
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.24294262286275625,
      "accuracy": 0.488
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.20657976157963276,
      "accuracy": 0.5179839091339328
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.2292172946035862,
      "accuracy": 0.544425087108014
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 1.3917895294725895,
      "accuracy": 0.1815723445776415
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.20975750032812357,
      "accuracy": 0.10908319185059423
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.3138614185154438,
      "accuracy": 0.07122507122507123
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.4192661661654711,
      "accuracy": 0.05234619395203337
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.19993677735328674,
      "eval_loss": 0.29504520321885747,
      "accuracy": 0.07117296222664016
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.2191731659695506,
      "accuracy": 0.6717272727272727
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.18857755046337843,
      "accuracy": 0.6961665877898722
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.19716421328485012,
      "accuracy": 0.740418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 1.3774103112518787,
      "accuracy": 0.22974630610538055
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.20656359754502773,
      "accuracy": 0.1133276740237691
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.3102692514657974,
      "accuracy": 0.0737891737891738
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.41481802612543106,
      "accuracy": 0.06319082377476538
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 9001,
      "train_steps": 500,
      "train_loss": 0.18353383243083954,
      "eval_loss": 0.2894914907713731,
      "accuracy": 0.09940357852882704
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9090909090909091,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```