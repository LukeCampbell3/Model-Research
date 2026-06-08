# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-08T00:21:18.689732",
    "run_id": "algo_20260608_001512_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
        123
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
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.21594616118818521,
      "accuracy": 0.49127272727272725
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1755795106291771,
      "accuracy": 0.5577925153955471
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.20173880364745855,
      "accuracy": 0.5481997677119629
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 1.5207750350236893,
      "accuracy": 0.16809486952675806
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.1994481198489666,
      "accuracy": 0.08578584846587352
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2926559578627348,
      "accuracy": 0.040863981319322826
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.4141271449625492,
      "accuracy": 0.022579970729667574
    },
    {
      "model": "fixed_moe_vectorized",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15063753724098206,
      "eval_loss": 0.2827530813713868,
      "accuracy": 0.058148893360160964
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.24557558353990316,
      "accuracy": 0.40745454545454546
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.21421056613326073,
      "accuracy": 0.33183325438180955
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.23660874646157026,
      "accuracy": 0.39285714285714285
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 1.366411667317152,
      "accuracy": 0.24765037593984962
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.18763386271893978,
      "accuracy": 0.139845543727823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.2797365952283144,
      "accuracy": 0.08114419147694103
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.3952231612056494,
      "accuracy": 0.03972402257997073
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__baseline_v1_1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.263217909882466,
      "accuracy": 0.06680080482897384
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_sampling",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__family_balanced_loss_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_1_0",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.20277386251837015,
      "accuracy": 0.618909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.18432505428791046,
      "accuracy": 0.5995973472288015
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.18540660478174686,
      "accuracy": 0.6640534262485482
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 1.4058020897209644,
      "accuracy": 0.24566010614772224
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.18570956028997898,
      "accuracy": 0.1279482362763515
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.2747783176600933,
      "accuracy": 0.08873321657910099
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.39102606661617756,
      "accuracy": 0.06376750993100565
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__gradient_clip_0_5",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.15183982253074646,
      "eval_loss": 0.25925932079553604,
      "accuracy": 0.09195171026156941
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.23432537633925676,
      "accuracy": 0.512
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.20293582323938608,
      "accuracy": 0.4887494078635718
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.22218600939959288,
      "accuracy": 0.4927409988385598
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 1.439219817519188,
      "accuracy": 0.23081601061477222
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.18401156552135944,
      "accuracy": 0.15153412648716344
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.2755289897322655,
      "accuracy": 0.08639813193228255
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.38981466740369797,
      "accuracy": 0.03554254651892118
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1774877905845642,
      "eval_loss": 0.2554126890997092,
      "accuracy": 0.07645875251509054
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.24557558353990316,
      "accuracy": 0.40745454545454546
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.21421056613326073,
      "accuracy": 0.33183325438180955
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.23660874646157026,
      "accuracy": 0.39285714285714285
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 1.366411667317152,
      "accuracy": 0.24765037593984962
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.18763386271893978,
      "accuracy": 0.139845543727823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.2797365952283144,
      "accuracy": 0.08114419147694103
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.3952231612056494,
      "accuracy": 0.03972402257997073
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__logit_norm_cap_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.263217909882466,
      "accuracy": 0.06680080482897384
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.236926912330091,
      "accuracy": 0.4853636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.20705788303166628,
      "accuracy": 0.44895783988630983
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.2228590026497841,
      "accuracy": 0.48819202477739065
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 1.4015562199056149,
      "accuracy": 0.23432662538699692
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.18804624769836664,
      "accuracy": 0.13880192026716762
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.2793717011809349,
      "accuracy": 0.08318739054290718
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.390536867082119,
      "accuracy": 0.04515994145933515
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_01",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1778622567653656,
      "eval_loss": 0.2610722879568736,
      "accuracy": 0.07303822937625755
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.23915866389870644,
      "accuracy": 0.49472727272727274
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.20647018495947123,
      "accuracy": 0.4335622927522501
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.22675594594329596,
      "accuracy": 0.46680216802168023
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 1.3547816649079323,
      "accuracy": 0.2392470145953118
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.1857362287119031,
      "accuracy": 0.17658108954289292
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.2781687881797552,
      "accuracy": 0.1187974314068885
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.3895478192716837,
      "accuracy": 0.06544010035542547
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__wrong_suppress_0_03",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17714901268482208,
      "eval_loss": 0.25785765672723454,
      "accuracy": 0.11770623742454728
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2627595020458102,
      "accuracy": 0.33181818181818185
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.22552137449383736,
      "accuracy": 0.2651586925627665
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2573909731581807,
      "accuracy": 0.29239256678281067
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 1.4244181253015995,
      "accuracy": 0.23678681999115436
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.18696640711277723,
      "accuracy": 0.15424754748486746
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.28013191744685173,
      "accuracy": 0.09106830122591944
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.39315312169492245,
      "accuracy": 0.030524775245661717
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_instead_of_0_05",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.26214908560117084,
      "accuracy": 0.06056338028169014
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.24394039530307055,
      "accuracy": 0.4042727272727273
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.21666722279042006,
      "accuracy": 0.388915206063477
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.2371072517707944,
      "accuracy": 0.3759194734804491
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 1.497996710240841,
      "accuracy": 0.191452896948253
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.18872935231775045,
      "accuracy": 0.10561469421832603
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.2812607157975435,
      "accuracy": 0.06042031523642732
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.3961493782699108,
      "accuracy": 0.02707505749529584
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_03",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1850237250328064,
      "eval_loss": 0.2633521383007367,
      "accuracy": 0.05714285714285714
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.2444391706958413,
      "accuracy": 0.39836363636363636
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.21722033061087132,
      "accuracy": 0.3689009947891994
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.23776783142238855,
      "accuracy": 0.3696283391405343
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 1.497329119592905,
      "accuracy": 0.19170168067226892
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.18891681358218193,
      "accuracy": 0.10540596952619495
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.2815331183373928,
      "accuracy": 0.0595446584938704
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.3961515314877033,
      "accuracy": 0.02550700397240226
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_with_decay_to_0_01",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.18491336703300476,
      "eval_loss": 0.2632392458617687,
      "accuracy": 0.055130784708249496
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9285714285714286,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```