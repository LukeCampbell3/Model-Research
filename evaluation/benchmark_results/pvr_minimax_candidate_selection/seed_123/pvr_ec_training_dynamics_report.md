# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T23:54:16.323129",
    "run_id": "algo_20260607_234918_benchmark-lite",
    "git_commit": "51e443da02bdc0a13c33b86368b863343ae036a2",
    "docker_image": "sparse-loop-moe-gpu",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 4080 SUPER",
    "amp_enabled": true,
    "seed": 123,
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
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2900001537054777,
      "accuracy": 0.14772727272727273
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2672149548307061,
      "accuracy": 0.09438654666035054
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.3000552002340555,
      "accuracy": 0.0886566008517228
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 1.6239676922559738,
      "accuracy": 0.07245134896063689
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.21062343753874302,
      "accuracy": 0.03235232728031726
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.3023117482662201,
      "accuracy": 0.012259194395796848
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.4242316372692585,
      "accuracy": 0.00010453690152623876
    },
    {
      "model": "pvr_ec_deploy_top1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.2083549052476883,
      "eval_loss": 0.2954108292857806,
      "accuracy": 0.001006036217303823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.24557558353990316,
      "accuracy": 0.40745454545454546
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.21421056613326073,
      "accuracy": 0.33183325438180955
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.23660874646157026,
      "accuracy": 0.39285714285714285
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 1.366411667317152,
      "accuracy": 0.24765037593984962
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.18763386271893978,
      "accuracy": 0.139845543727823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.2797365952283144,
      "accuracy": 0.08114419147694103
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.3952231612056494,
      "accuracy": 0.03972402257997073
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__v1_1_logit_norm_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.263217909882466,
      "accuracy": 0.06680080482897384
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2627595020458102,
      "accuracy": 0.33181818181818185
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.22552137449383736,
      "accuracy": 0.2651586925627665
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2573909731581807,
      "accuracy": 0.29239256678281067
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 1.4244181253015995,
      "accuracy": 0.23678681999115436
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.18696640711277723,
      "accuracy": 0.15424754748486746
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.28013191744685173,
      "accuracy": 0.09106830122591944
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.39315312169492245,
      "accuracy": 0.030524775245661717
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.26214908560117084,
      "accuracy": 0.06056338028169014
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2435163501650095,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.21343904361128807,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23340520728379488,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.398505061864853,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.1875611413270235,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.27947625145316124,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.3927343413233757,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26141560822725296,
      "accuracy": 0.06800804828973843
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.24557558353990316,
      "accuracy": 0.40745454545454546
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.21421056613326073,
      "accuracy": 0.33183325438180955
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.23660874646157026,
      "accuracy": 0.39285714285714285
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 1.366411667317152,
      "accuracy": 0.24765037593984962
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.18763386271893978,
      "accuracy": 0.139845543727823
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.2797365952283144,
      "accuracy": 0.08114419147694103
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.3952231612056494,
      "accuracy": 0.03972402257997073
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_logit_norm_medium",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1846141815185547,
      "eval_loss": 0.263217909882466,
      "accuracy": 0.06680080482897384
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.25827869586646557,
      "accuracy": 0.37545454545454543
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.22593434806913137,
      "accuracy": 0.33349123638086214
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.2540537668392062,
      "accuracy": 0.3347851335656214
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 1.4080132655799389,
      "accuracy": 0.24325519681556834
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.18838609009981155,
      "accuracy": 0.14652473387601753
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.2807487491518259,
      "accuracy": 0.09544658493870403
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.39751287549734116,
      "accuracy": 0.04798243780054359
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19041119515895844,
      "eval_loss": 0.2638963038722674,
      "accuracy": 0.08329979879275654
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.23776818998157978,
      "accuracy": 0.4738181818181818
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.20689369924366474,
      "accuracy": 0.40999526290857413
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.2274450147524476,
      "accuracy": 0.4424119241192412
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 1.356879971921444,
      "accuracy": 0.2426470588235294
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.18610165733844042,
      "accuracy": 0.16405760801502817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.2783388290554285,
      "accuracy": 0.10332749562171628
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.39051733165979385,
      "accuracy": 0.04975956512648965
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_wrong_suppress_0_01_plus_logit_norm_light",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.17814171314239502,
      "eval_loss": 0.2583194797237714,
      "accuracy": 0.0925553319919517
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2821823786944151,
      "accuracy": 0.33181818181818185
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2420401405543089,
      "accuracy": 0.2651586925627665
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.2730230623856187,
      "accuracy": 0.29239256678281067
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 1.4129029475152493,
      "accuracy": 0.23678681999115436
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.20519765745848417,
      "accuracy": 0.15424754748486746
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.29751808010041714,
      "accuracy": 0.09106830122591944
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.4122994840145111,
      "accuracy": 0.030524775245661717
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_03_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.19408826529979706,
      "eval_loss": 0.28152358159422874,
      "accuracy": 0.06056338028169014
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.26725670229643583,
      "accuracy": 0.43618181818181817
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.23323369026184082,
      "accuracy": 0.4347465656087163
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "clrs_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.25374074652791023,
      "accuracy": 0.4263453348819202
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "listops",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 1.3914664909243584,
      "accuracy": 0.24107142857142858
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.20673090778291225,
      "accuracy": 0.1427676894176581
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "scan_style",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2980278246104717,
      "accuracy": 0.0840630472854641
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.41283420100808144,
      "accuracy": 0.03846957976165587
    },
    {
      "model": "pvr_ec_ownership_top1_final_candidate_v1__repair__sparse_ce_0_05_plus_temperature_T_1_2",
      "family": "dyck",
      "seed": 123,
      "train_steps": 500,
      "train_loss": 0.1834246814250946,
      "eval_loss": 0.2819095104932785,
      "accuracy": 0.06800804828973843
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 0.9090909090909091,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```