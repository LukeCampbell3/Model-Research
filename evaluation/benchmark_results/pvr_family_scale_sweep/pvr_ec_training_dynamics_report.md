# PVR-EC Training Dynamics Report

**Status:** PVR_EC_ROOT_CAUSE_INCONCLUSIVE

**Statuses:** PVR_EC_DIAGNOSTIC_INFRASTRUCTURE_READY, PVR_EC_DO_NOT_PROMOTE, PVR_EC_ROOT_CAUSE_INCONCLUSIVE

```json
{
  "metadata": {
    "timestamp": "2026-06-07T02:08:45.467132",
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
    "pvr_expert_delta_scale_decay": null,
    "root_cause_flags": {
      "run_root_baseline_matrix": false,
      "run_training_dynamics_diagnostic": false,
      "run_ownership_integration_diagnostic": false,
      "run_shared_sparse_ablation": false,
      "run_learning_separation_diagnostic": false,
      "run_loss_calibration_diagnostic": false,
      "run_task_fit_diagnostic": false,
      "run_latency_stability_diagnostic": false,
      "run_gradient_flow_diagnostic": false,
      "run_optimizer_update_diagnostic": false,
      "run_expert_contribution_diagnostic": false,
      "run_loss_target_sanity": false,
      "run_shared_absorption_diagnostic": false,
      "run_expert_initialization_diagnostic": false,
      "run_after_repair_confirmation": false,
      "run_nonlinear_overfit_diagnostic": false,
      "run_fixed_owner_parity_diagnostic": false,
      "run_parity_scale_sweep": false,
      "run_nonlinear_overfit_confirmation": false,
      "run_after_nonlinear_repair_confirmation": false,
      "run_expert_delta_scale_schedule_diagnostic": false,
      "run_expert_delta_scale_schedule_confirmation": false,
      "run_residual_alignment_diagnostic": false,
      "run_family_scale_sweep": true,
      "run_conditional_scale_oracle": false,
      "run_benchmark_transfer_confirmation": false
    },
    "diagnostic_sweeps": {
      "train_steps_list": [
        500
      ],
      "seed_list": [
        42
      ],
      "ownership_schedule_sweep": [],
      "shared_scale_sweep": [],
      "expert_delta_scale_sweep": [],
      "loss_schedule_sweep": [],
      "task_loss_schedule_sweep": [],
      "batch_size_list": [
        1,
        32
      ],
      "seq_len_list": [
        64
      ],
      "pvr_overfit_tasks": [
        "toy_identity"
      ],
      "pvr_overfit_steps": 100,
      "pvr_overfit_batch_size": 16,
      "pvr_overfit_single_batch": false,
      "pvr_shared_scale_sweep": [],
      "pvr_expert_delta_scale_sweep": [],
      "pvr_expert_init_sweep": [],
      "pvr_expert_delta_scale_schedule": "constant",
      "pvr_expert_delta_scale_start": null,
      "pvr_expert_delta_scale_end": null,
      "pvr_expert_delta_scale_warmup_steps": null,
      "pvr_expert_delta_scale_hold_steps": null,
      "pvr_expert_delta_scale_decay": null,
      "conditional_scale_modes": []
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
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3074029963463545,
      "accuracy": 0.1378181818181818
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.28325783275067806,
      "accuracy": 0.07344766410408042
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3238312490284443,
      "accuracy": 0.08091366627951994
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 1.6209645047783852,
      "accuracy": 0.11464359939336068
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.21884552482515574,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.3002347759902477,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.4245618898421526,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_1",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18775048851966858,
      "eval_loss": 0.29722652584314346,
      "accuracy": 0.0007920792079207921
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.3076569028198719,
      "accuracy": 0.1330909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.2810562737286091,
      "accuracy": 0.11448846836191602
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.3253525197505951,
      "accuracy": 0.07955865272938444
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 1.6185197569429874,
      "accuracy": 0.09079930348817615
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.21439531724900007,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.295294813811779,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.42294713109731674,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18774420022964478,
      "eval_loss": 0.2936844527721405,
      "accuracy": 0.001188118811881188
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.30516638047993183,
      "accuracy": 0.14481818181818182
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.28202829137444496,
      "accuracy": 0.10065050266114725
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.3265083581209183,
      "accuracy": 0.07994579945799458
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 1.6789878457784653,
      "accuracy": 0.07479076560130316
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.21670475415885448,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.2968834191560745,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.4244465231895447,
      "accuracy": 0.0
    },
    {
      "model": "pvr_ec_ownership_top1_constant_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19066591560840607,
      "eval_loss": 0.2950296724836032,
      "accuracy": 0.0015841584158415843
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.3094241339713335,
      "accuracy": 0.09281818181818181
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.2800898663699627,
      "accuracy": 0.08681253696037848
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.3262499198317528,
      "accuracy": 0.08681765389082462
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 1.6921329833567142,
      "accuracy": 0.030837499297871145
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.20806483924388885,
      "accuracy": 0.0012394133443503407
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.2882545590400696,
      "accuracy": 0.002994908655286014
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.4189610630273819,
      "accuracy": 0.00258585022755482
    },
    {
      "model": "pvr_ec_ownership_top1_constant_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18762831389904022,
      "eval_loss": 0.2866389329234759,
      "accuracy": 0.008514851485148515
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.31199880689382553,
      "accuracy": 0.09845454545454546
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.27507228776812553,
      "accuracy": 0.1023063276167948
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.3237336054444313,
      "accuracy": 0.07684862562911343
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 1.654180008918047,
      "accuracy": 0.05190136493849351
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.20812654402107,
      "accuracy": 0.0037182400330510227
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.28934575244784355,
      "accuracy": 0.001497454327643007
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.4181022644042969,
      "accuracy": 0.0018618121638394704
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.1893884539604187,
      "eval_loss": 0.2869880584379037,
      "accuracy": 0.0035643564356435645
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.30222402699291706,
      "accuracy": 0.13763636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.27271723560988903,
      "accuracy": 0.10313424009461857
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.3158093597739935,
      "accuracy": 0.09872241579558652
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 1.6250091530382633,
      "accuracy": 0.09487165084536314
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.20576439518481493,
      "accuracy": 0.023755422433381534
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.28662920370697975,
      "accuracy": 0.01078167115902965
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.41453822143375874,
      "accuracy": 0.007550682664460074
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18761539459228516,
      "eval_loss": 0.28517769773801166,
      "accuracy": 0.007920792079207921
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.30518035776913166,
      "accuracy": 0.1338181818181818
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.2751125209033489,
      "accuracy": 0.10218805440567712
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.316677575930953,
      "accuracy": 0.10627177700348432
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 1.6396962478756905,
      "accuracy": 0.09402909621973825
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.20685867499560118,
      "accuracy": 0.024375129105556705
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.2873171344399452,
      "accuracy": 0.011380652890086853
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.41523584350943565,
      "accuracy": 0.007550682664460074
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_4",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18822705745697021,
      "eval_loss": 0.2861823116739591,
      "accuracy": 0.00891089108910891
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.311616325750947,
      "accuracy": 0.12290909090909091
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.2791007086634636,
      "accuracy": 0.056652868125369606
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.31949686631560326,
      "accuracy": 0.11072396438250097
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 1.6604201905429363,
      "accuracy": 0.09020951525023872
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.20878901239484549,
      "accuracy": 0.024168560214831648
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.2886418588459492,
      "accuracy": 0.011680143755615454
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.41706929728388786,
      "accuracy": 0.008171286719073231
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_8_to_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.19143113493919373,
      "eval_loss": 0.2884698199729125,
      "accuracy": 0.009702970297029703
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.3130939658731222,
      "accuracy": 0.10363636363636364
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.2770928852260113,
      "accuracy": 0.08775872264931993
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "clrs_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.32374848425388336,
      "accuracy": 0.08468834688346884
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "listops",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 1.67607506737113,
      "accuracy": 0.047323484805931584
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.20928913541138172,
      "accuracy": 0.005990497831026648
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "scan_style",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.29002100974321365,
      "accuracy": 0.0032943995208146153
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.41910065710544586,
      "accuracy": 0.0018618121638394704
    },
    {
      "model": "pvr_ec_ownership_top1_scale_schedule_1_to_4_to_2",
      "family": "dyck",
      "seed": 42,
      "train_steps": 500,
      "train_loss": 0.18987217545509338,
      "eval_loss": 0.28787930061419803,
      "accuracy": 0.007722772277227723
    }
  ],
  "specialization_metrics": {
    "expert_utilization": 1.0,
    "expert_gradient_norm_by_expert": {},
    "expert_output_norm_by_expert": {}
  }
}
```