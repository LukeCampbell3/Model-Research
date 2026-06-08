# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:27:16.348820",
    "run_id": "algo_20260608_002119_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 777,
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
        777
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
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.25702635291963816,
      "accuracy": 0.2720909090909091
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.2398307528346777,
      "accuracy": 0.19011002011120312
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.24611769802868366,
      "accuracy": 0.3308168795973674
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 1.4206876046955585,
      "accuracy": 0.18241412937479684
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.1956030959263444,
      "accuracy": 0.09416473562249841
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.28213198482990265,
      "accuracy": 0.05716851242143071
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.4017317108809948,
      "accuracy": 0.019055684946008893
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16213898360729218,
      "eval_loss": 0.27079928169647854,
      "accuracy": 0.0786761791518034
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21892981510609388,
      "accuracy": 0.5381818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21400899160653353,
      "accuracy": 0.4650419969241689
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21387974172830582,
      "accuracy": 0.490418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 1.5707997642457485,
      "accuracy": 0.18249539495069889
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.1930565619841218,
      "accuracy": 0.13440067410996417
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2756177671253681,
      "accuracy": 0.10865010475905418
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.39493958465754986,
      "accuracy": 0.08003387677323735
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2752813609937827,
      "accuracy": 0.10939357907253269
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.2361530400812626,
      "accuracy": 0.43736363636363634
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.23344013094902039,
      "accuracy": 0.3302969359990536
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.23184300865978003,
      "accuracy": 0.4005032907471932
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 1.5328350886702538,
      "accuracy": 0.1628020370571026
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.19698609970510006,
      "accuracy": 0.10153781335580367
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.27807280234992504,
      "accuracy": 0.06914097575576175
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.39166842587292194,
      "accuracy": 0.04933305102688969
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.2755308076739311,
      "accuracy": 0.07649623464130004
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21892981510609388,
      "accuracy": 0.5381818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21400899160653353,
      "accuracy": 0.4650419969241689
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21387974172830582,
      "accuracy": 0.490418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 1.5707997642457485,
      "accuracy": 0.18249539495069889
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.1930565619841218,
      "accuracy": 0.13440067410996417
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2756177671253681,
      "accuracy": 0.10865010475905418
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.39493958465754986,
      "accuracy": 0.08003387677323735
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2752813609937827,
      "accuracy": 0.10939357907253269
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21892981510609388,
      "accuracy": 0.5381818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21400899160653353,
      "accuracy": 0.4650419969241689
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21387974172830582,
      "accuracy": 0.490418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 1.5707997642457485,
      "accuracy": 0.18249539495069889
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.1930565619841218,
      "accuracy": 0.13440067410996417
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2756177671253681,
      "accuracy": 0.10865010475905418
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.39493958465754986,
      "accuracy": 0.08003387677323735
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2752813609937827,
      "accuracy": 0.10939357907253269
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21892981510609388,
      "accuracy": 0.5381818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21400899160653353,
      "accuracy": 0.4650419969241689
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.21387974172830582,
      "accuracy": 0.490418118466899
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 1.5707997642457485,
      "accuracy": 0.18249539495069889
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.1930565619841218,
      "accuracy": 0.13440067410996417
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2756177671253681,
      "accuracy": 0.10865010475905418
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.39493958465754986,
      "accuracy": 0.08003387677323735
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16685862839221954,
      "eval_loss": 0.2752813609937827,
      "accuracy": 0.10939357907253269
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.18144366797059774,
      "accuracy": 0.6721818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.18543914705514908,
      "accuracy": 0.5884301431444457
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.1753043197095394,
      "accuracy": 0.648664343786295
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 1.5613963939249516,
      "accuracy": 0.1790551522375122
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.18922056537121534,
      "accuracy": 0.11628396882241415
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.2716834247112274,
      "accuracy": 0.0847051780903921
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.38673717714846134,
      "accuracy": 0.10395934787211518
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1356501430273056,
      "eval_loss": 0.2688266175488631,
      "accuracy": 0.12088783194609591
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.22658134810626507,
      "accuracy": 0.4880909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.22670124005526304,
      "accuracy": 0.3810481485863007
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.22073042020201683,
      "accuracy": 0.45267131242741
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 1.5516797937452793,
      "accuracy": 0.17052226676779716
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.1966289160773158,
      "accuracy": 0.11291341900147461
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.2784329876303673,
      "accuracy": 0.07752170008979348
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.3943926226347685,
      "accuracy": 0.07283506246030065
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1698697954416275,
      "eval_loss": 0.27543176089723903,
      "accuracy": 0.10681728101466507
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.2361530400812626,
      "accuracy": 0.43736363636363634
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.23344013094902039,
      "accuracy": 0.3302969359990536
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.23184300865978003,
      "accuracy": 0.4005032907471932
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 1.5328350886702538,
      "accuracy": 0.1628020370571026
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.19698609970510006,
      "accuracy": 0.10153781335580367
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.27807280234992504,
      "accuracy": 0.06914097575576175
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.39166842587292194,
      "accuracy": 0.04933305102688969
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17292802035808563,
      "eval_loss": 0.2755308076739311,
      "accuracy": 0.07649623464130004
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.2226250721141696,
      "accuracy": 0.513090909090909
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.22145077120512724,
      "accuracy": 0.4249378918727079
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.2188510922715068,
      "accuracy": 0.46012388695315526
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 1.542273834347725,
      "accuracy": 0.16477949940405245
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.18884149193763733,
      "accuracy": 0.141352433115652
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.2709689997136593,
      "accuracy": 0.10505836575875487
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.3921972643584013,
      "accuracy": 0.06203684099089562
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.16838225722312927,
      "eval_loss": 0.27218838160236675,
      "accuracy": 0.10840269520412207
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.23658199328929186,
      "accuracy": 0.42145454545454547
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.23200887069106102,
      "accuracy": 0.2984739145865373
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.23235825821757317,
      "accuracy": 0.3829849012775842
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 1.5056815259158611,
      "accuracy": 0.1412937479683606
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.1917078858241439,
      "accuracy": 0.11438803454813566
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.27354273945093155,
      "accuracy": 0.09398383717449865
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.3920583836734295,
      "accuracy": 0.06468346390006352
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17091207206249237,
      "eval_loss": 0.27307746807734173,
      "accuracy": 0.10087197780420135
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.28645225800573826,
      "accuracy": 0.10481818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.25390366837382317,
      "accuracy": 0.09807169052407429
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.2836766904219985,
      "accuracy": 0.13588850174216027
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 1.5912101529538631,
      "accuracy": 0.13108137393000324
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.210370815359056,
      "accuracy": 0.050768906677901834
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.2921659089624882,
      "accuracy": 0.03561807841963484
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.4038615319877863,
      "accuracy": 0.027524878255346177
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1921829879283905,
      "eval_loss": 0.2902560904622078,
      "accuracy": 0.04102259215219976
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.2433349434286356,
      "accuracy": 0.3678181818181818
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.2461176123470068,
      "accuracy": 0.2116408375724595
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.25086803175508976,
      "accuracy": 0.32665505226480834
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 1.7085285186767578,
      "accuracy": 0.17439592588579478
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.20322539936751127,
      "accuracy": 0.07225616178639141
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.2853133734315634,
      "accuracy": 0.058964381921580364
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.405632596462965,
      "accuracy": 0.037370315477450775
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.17578615248203278,
      "eval_loss": 0.28669382135073346,
      "accuracy": 0.06817281014665082
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.24279037863016129,
      "accuracy": 0.36854545454545456
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.24574467819184065,
      "accuracy": 0.19614338104814857
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.2509433552622795,
      "accuracy": 0.3258807588075881
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "listops",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 1.698901541531086,
      "accuracy": 0.17087441759670605
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.20269973203539848,
      "accuracy": 0.07036022751211292
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.28481171280145645,
      "accuracy": 0.052978150254414845
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.4051278829574585,
      "accuracy": 0.036840990895617196
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 777,
      "train_steps": 500,
      "train_loss": 0.1757964789867401,
      "eval_loss": 0.28628695880373317,
      "accuracy": 0.06282203725723345
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9285714285714286,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```