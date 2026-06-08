# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:33:32.988294",
    "run_id": "algo_20260608_002717_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 2026,
    "benchmark_command": "evaluation/run_algorithmic_benchmarks.py --mode benchmark-lite --scale small --sample-limit 1000 --train-steps 500 --seed-list 42,123,777,2026,9001 --device cuda --amp --models fixed_moe_vectorized,pvr_ec_ownership_top1_final_candidate_v1 --enable-ownership-map --ownership-map-mode frozen --run-stability-repair-sweep --stability-repair-variants baseline_v1,baseline_v1_1,family_balanced_sampling,family_balanced_loss_light,gradient_clip_1_0,gradient_clip_0_5,logit_norm_cap_light,logit_norm_cap_medium,wrong_suppress_0_01,wrong_suppress_0_03,sparse_ce_0_03_instead_of_0_05,sparse_ce_0_05_with_decay_to_0_03,sparse_ce_0_05_with_decay_to_0_01 --output-dir evaluation/benchmark_results/pvr_minimax_stability_repair_sweep",
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
      "run_stability_repair_sweep": true
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        2026
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
      "minimax_variants": [],
      "stability_repair_variants": [
        "baseline_v1",
        "baseline_v1_1",
        "family_balanced_sampling",
        "family_balanced_loss_light",
        "gradient_clip_1_0",
        "gradient_clip_0_5",
        "logit_norm_cap_light",
        "logit_norm_cap_medium",
        "wrong_suppress_0_01",
        "wrong_suppress_0_03",
        "sparse_ce_0_03_instead_of_0_05",
        "sparse_ce_0_05_with_decay_to_0_03",
        "sparse_ce_0_05_with_decay_to_0_01"
      ]
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
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.22179481573402882,
      "accuracy": 0.44536363636363635
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.19380450248718262,
      "accuracy": 0.5106055219812774
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.21609133575111628,
      "accuracy": 0.509388308168796
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 1.4335313439369202,
      "accuracy": 0.11938288591586405
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.19737683236598969,
      "accuracy": 0.08391038696537678
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.300133652985096,
      "accuracy": 0.03688297282307266
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.40572931431233883,
      "accuracy": 0.0037359900373599006
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.17266248166561127,
      "eval_loss": 0.2726064858337243,
      "accuracy": 0.03406853091768413
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.18395077250897884,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.17868976388126612,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.1796662723645568,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 1.286568507552147,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.19539925176650286,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.29588529095053673,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.40159808844327927,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.2721534085770448,
      "accuracy": 0.10456872784560851
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.19397222343832254,
      "accuracy": 0.6609090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.18018643651157618,
      "accuracy": 0.5372674487498519
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.189482681453228,
      "accuracy": 0.6668602400309718
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 1.268459677696228,
      "accuracy": 0.2502415176088293
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.1955755352973938,
      "accuracy": 0.119959266802444
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.29617478512227535,
      "accuracy": 0.0829173599556295
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.40053038485348225,
      "accuracy": 0.06454960564549606
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.2723686782022317,
      "accuracy": 0.09551004332414337
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.18395077250897884,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.17868976388126612,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.1796662723645568,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 1.286568507552147,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.19539925176650286,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.29588529095053673,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.40159808844327927,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.2721534085770448,
      "accuracy": 0.10456872784560851
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.18395077250897884,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.17868976388126612,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.1796662723645568,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 1.286568507552147,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.19539925176650286,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.29588529095053673,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.40159808844327927,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224745869636536,
      "eval_loss": 0.2721534085770448,
      "accuracy": 0.10456872784560851
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.18395076971501112,
      "accuracy": 0.693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.17868976946920156,
      "accuracy": 0.5263656831378125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.17966626770794392,
      "accuracy": 0.6953155245838173
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 1.2865684852004051,
      "accuracy": 0.2292221669252613
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.19539925456047058,
      "accuracy": 0.1154786150712831
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.2958852984011173,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.4015980865806341,
      "accuracy": 0.05904939809049398
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15224744379520416,
      "eval_loss": 0.27215340981880826,
      "accuracy": 0.10456872784560851
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.15850003715604544,
      "accuracy": 0.747
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.15937781613320112,
      "accuracy": 0.6030335347790022
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.15875329542905092,
      "accuracy": 0.7264808362369338
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 1.2914245538413525,
      "accuracy": 0.25990222196200125
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.1911167735233903,
      "accuracy": 0.12627291242362526
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.2907214295119047,
      "accuracy": 0.08347199112590127
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.39438276179134846,
      "accuracy": 0.059568285595682856
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.13076791167259216,
      "eval_loss": 0.26651447142163914,
      "accuracy": 0.09866089011421819
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.18370244838297367,
      "accuracy": 0.6933636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.1785900853574276,
      "accuracy": 0.5249437137101552
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.17980389297008514,
      "accuracy": 0.6886372435152923
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 1.285137452185154,
      "accuracy": 0.23563336163236628
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.19459543377161026,
      "accuracy": 0.1295315682281059
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.2953562904149294,
      "accuracy": 0.08957293399889074
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.40209970623254776,
      "accuracy": 0.055002075550020756
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15281754732131958,
      "eval_loss": 0.2706865295767784,
      "accuracy": 0.11067349350137849
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.19397222343832254,
      "accuracy": 0.6609090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.18018643651157618,
      "accuracy": 0.5372674487498519
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.189482681453228,
      "accuracy": 0.6668602400309718
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 1.268459677696228,
      "accuracy": 0.2502415176088293
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.1955755352973938,
      "accuracy": 0.119959266802444
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.29617478512227535,
      "accuracy": 0.0829173599556295
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.40053038485348225,
      "accuracy": 0.06454960564549606
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16059164702892303,
      "eval_loss": 0.2723686782022317,
      "accuracy": 0.09551004332414337
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.18029537796974182,
      "accuracy": 0.7062727272727273
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.1742737265303731,
      "accuracy": 0.5363194691314137
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.17594688571989536,
      "accuracy": 0.6939605110336817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 1.303678646683693,
      "accuracy": 0.20264059252320032
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.19802652671933174,
      "accuracy": 0.09531568228105906
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.29683911241590977,
      "accuracy": 0.07071547420965059
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.40615513175725937,
      "accuracy": 0.055417185554171855
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15010498464107513,
      "eval_loss": 0.2760951742529869,
      "accuracy": 0.0994486018117369
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.17770044039934874,
      "accuracy": 0.7026363636363636
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.1711502345278859,
      "accuracy": 0.5325275506576609
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.17372415959835052,
      "accuracy": 0.6896051103368177
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 1.2550580725073814,
      "accuracy": 0.24672853420767588
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.1973612355068326,
      "accuracy": 0.11120162932790224
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.29836985655128956,
      "accuracy": 0.07986688851913477
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.40178051218390465,
      "accuracy": 0.07337069323370693
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.14776919782161713,
      "eval_loss": 0.2748144504924615,
      "accuracy": 0.10850728633320204
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.20938309282064438,
      "accuracy": 0.5408181818181819
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.1967696724459529,
      "accuracy": 0.4979262945846664
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.2036430025473237,
      "accuracy": 0.5536198219125048
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 1.2610450610518456,
      "accuracy": 0.257882256506338
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.2006836123764515,
      "accuracy": 0.09246435845213849
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.30162383429706097,
      "accuracy": 0.06267332224070993
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.40807685628533363,
      "accuracy": 0.045454545454545456
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.16951239109039307,
      "eval_loss": 0.2786519241829713,
      "accuracy": 0.08605750295391887
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.2001887485384941,
      "accuracy": 0.5948181818181818
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.1897205961868167,
      "accuracy": 0.5200853181656594
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.1907058386132121,
      "accuracy": 0.6135307781649245
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 1.372327271848917,
      "accuracy": 0.17898650428876722
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.19696211069822311,
      "accuracy": 0.12932790224032586
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.2969941534101963,
      "accuracy": 0.08236272878535773
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.40724080987274647,
      "accuracy": 0.046699875466998754
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.15717807412147522,
      "eval_loss": 0.27262480432788533,
      "accuracy": 0.10909807010634108
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.20053736120462418,
      "accuracy": 0.5899090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.19003786239773035,
      "accuracy": 0.5204408105225737
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.19156372267752886,
      "accuracy": 0.6059814169570267
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "listops",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 1.3683088012039661,
      "accuracy": 0.1798647501390556
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.19710993114858866,
      "accuracy": 0.1340122199592668
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.29712621308863163,
      "accuracy": 0.08735440931780367
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.40724228881299496,
      "accuracy": 0.04877542548775426
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 2026,
      "train_steps": 500,
      "train_loss": 0.157006174325943,
      "eval_loss": 0.2726643830537796,
      "accuracy": 0.11244584482079559
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9285714285714286,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```