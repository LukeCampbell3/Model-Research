# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:49:17.579238",
    "run_id": "algo_20260607_234431_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 42,
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
        42
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
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.24142212327569723,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.20873637683689594,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.23053767159581184,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3296168148517609,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.19809814915060997,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2804417908191681,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.4041307009756565,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.27329832191268605,
      "accuracy": 0.06158415841584158
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2415832933038473,
      "accuracy": 0.4769090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.20936035551130772,
      "accuracy": 0.4998225901833235
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2303548539057374,
      "accuracy": 0.4626403406891212
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 1.3107546344399452,
      "accuracy": 0.22451272257484695
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.19833189900964499,
      "accuracy": 0.08221441850857261
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.28078920394182205,
      "accuracy": 0.05390835579514825
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.40399774350225925,
      "accuracy": 0.03103020273065784
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2743444989124934,
      "accuracy": 0.053465346534653464
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.26534003019332886,
      "accuracy": 0.36563636363636365
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.22786620538681746,
      "accuracy": 0.3348314606741573
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.26019474398344755,
      "accuracy": 0.3147502903600465
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 1.3443554043769836,
      "accuracy": 0.22358591248665954
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.2005924517288804,
      "accuracy": 0.09440198306135096
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.28284819796681404,
      "accuracy": 0.06229410002994909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.404697110876441,
      "accuracy": 0.046235002068680184
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.27479483808080357,
      "accuracy": 0.07247524752475247
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.24142212327569723,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.20873637683689594,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.23053767159581184,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3296168148517609,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.19809814915060997,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2804417908191681,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.4041307009756565,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.27329832191268605,
      "accuracy": 0.06158415841584158
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2415832933038473,
      "accuracy": 0.4769090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.20936035551130772,
      "accuracy": 0.4998225901833235
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2303548539057374,
      "accuracy": 0.4626403406891212
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 1.3107546344399452,
      "accuracy": 0.22451272257484695
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.19833189900964499,
      "accuracy": 0.08221441850857261
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.28078920394182205,
      "accuracy": 0.05390835579514825
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.40399774350225925,
      "accuracy": 0.03103020273065784
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1511673480272293,
      "eval_loss": 0.2743444989124934,
      "accuracy": 0.053465346534653464
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.26792365591973066,
      "accuracy": 0.346
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.2305002138018608,
      "accuracy": 0.2984033116499113
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.2622102424502373,
      "accuracy": 0.3037166085946574
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 1.3364790938794613,
      "accuracy": 0.22434421164972196
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.20371340587735176,
      "accuracy": 0.08076843627349721
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.286036167293787,
      "accuracy": 0.053009883198562445
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.4085437227040529,
      "accuracy": 0.041580471659081505
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16339507699012756,
      "eval_loss": 0.27915434911847115,
      "accuracy": 0.06099009900990099
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.24417043570429087,
      "accuracy": 0.4812727272727273
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.21370424330234528,
      "accuracy": 0.5049083382613838
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2341784816235304,
      "accuracy": 0.4699961285327139
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 1.31748728454113,
      "accuracy": 0.21662079424816041
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.1997331902384758,
      "accuracy": 0.07539764511464574
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2825468145310879,
      "accuracy": 0.04791853848457622
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.40497460030019283,
      "accuracy": 0.027099710384774513
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.14932295680046082,
      "eval_loss": 0.2754017934203148,
      "accuracy": 0.048712871287128715
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.2863199729472399,
      "accuracy": 0.36563636363636365
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.24736089073121548,
      "accuracy": 0.3348314606741573
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.27724758721888065,
      "accuracy": 0.3147502903600465
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 1.3371113277971745,
      "accuracy": 0.22358591248665954
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.21948457416146994,
      "accuracy": 0.09440198306135096
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.30099258199334145,
      "accuracy": 0.06229410002994909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.4228495731949806,
      "accuracy": 0.046235002068680184
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.16285622119903564,
      "eval_loss": 0.29429832597573596,
      "accuracy": 0.07247524752475247
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2684176620095968,
      "accuracy": 0.49918181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.23377175815403461,
      "accuracy": 0.5117681845062093
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.2541435621678829,
      "accuracy": 0.49661246612466126
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 1.3323042653501034,
      "accuracy": 0.22673144975565915
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.21845487412065268,
      "accuracy": 0.08572608965089858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.30021874606609344,
      "accuracy": 0.055705300988319856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.42397673800587654,
      "accuracy": 0.03568473314025652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1481063961982727,
      "eval_loss": 0.29410430540641147,
      "accuracy": 0.06158415841584158
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9090909090909091,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```