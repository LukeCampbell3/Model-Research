# Matched Information Routing Attribution Validation

Status: `MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION_PARTIAL_COMPLETE`
Decision: `PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_BOUNDED_ADVANTAGE_NOT_SUPPORTED`

## Main Result

Local paired heldout supports a teacher-independent sparse-v2 comparative advantage over tested sparse baselines, but the bounded official-data scorecard does not support an official bounded advantage.

## Paired Local Heldout

| baseline | candidate-baseline loss | 95% CI | significant win | active-param delta |
|---|---:|---|---|---:|
| dense_sparse_v2_300m_matched | 0.10677952994592488 | [0.08234965684823692, 0.13011069991625845] | False | -110278176 |
| switch_top1_sparse_v2_300m_matched | -0.07805347559042275 | [-0.1025221892632544, -0.051330351969227195] | True | 16350144 |
| generic_top2_sparse_v2_300m_matched | -0.13574328343383968 | [-0.1553028777707368, -0.11656093806959689] | True | -1574496 |

## Official Evaluation Boundary

Status: `OFFICIAL_EVALUATION_BOUNDARY_FROZEN`

- current_local_roots_have_no_exact_line_overlap_with_final: `True`
- final_official_files_present: `True`
- final_official_may_guide_training: `False`
- official_like_development_set_ready: `True`

Official-like development data is not yet materialized, so router-regret/substrate repair training must not use the final eight official bounded files.


## Bounded Official LM Rank

| rank | variant | lm_loss | compile_rate | strict PVR Top1 clean |
|---:|---|---:|---:|---|
| 1 | generic_top2_sparse_v2_300m_matched | 10.238743431866169 | 0.375 | not_applicable |
| 2 | dense_sparse_v2_300m_matched | 10.717340417206287 | 0.3125 | not_applicable |
| 3 | switch_top1_sparse_v2_300m_matched | 11.077159017324448 | 0.1875 | not_applicable |
| 4 | pvr_teacher_independent_sparse_v2_300m | 11.146245710551739 | 0.25 | True |

## Bounded Official Paired/File Bootstrap

| baseline | block delta | block 95% CI | file delta | file 95% CI | file wins | significant file win |
|---|---:|---|---:|---|---:|---|
| dense_sparse_v2_300m_matched | -0.6869987417012453 | [-0.9439331293106079, -0.441188040189445] | -0.6869987417012453 | [-1.4469890538603067, -0.08235012833029032] | 7/8 | True |
| switch_top1_sparse_v2_300m_matched | 0.7587798396125436 | [0.5656211078166962, 0.9475187631323934] | 0.7587798396125436 | [0.3976497817784548, 1.147539421916008] | 0/8 | False |
| generic_top2_sparse_v2_300m_matched | 0.46071298606693745 | [0.14120180811733007, 0.7928766654804349] | 0.46071298606693745 | [-0.4916243888437748, 1.4173840023577213] | 3/8 | False |

## Comparator Integrity

| variant | family | configured active experts | strict PVR invariants applicable | declared Top1 comparator | dynamic Top-K audited | capacity/fallback audited |
|---|---|---:|---|---|---|---|
| dense_sparse_v2_300m_matched | dense_transformer | 0 | False | False | False | False |
| switch_top1_sparse_v2_300m_matched | vanilla_switch_top1_reference | 1 | False | True | False | False |
| generic_top2_sparse_v2_300m_matched | generic_top2_moe_reference | 2 | False | False | False | False |
| pvr_teacher_independent_sparse_v2_300m | pvr_ec_o | 1 | True | True | True | False |

## Aggregation Reversal Audit

The scorecard `lm_loss` and the paired all-file audit use different aggregation definitions. The scorecard path evaluates limited windows of selected concatenated text; the aggregation audit evaluates up to 32 blocks per official JSONL file and reports both token-weighted and file-balanced results.

### PVR vs dense_sparse_v2_300m_matched

- Micro delta: `-0.6869987417012453`
- Macro file delta: `-0.6869987417012453`
- File wins: `7/8`
- Exact sign-test p: `0.0703125`
- Exact sign-flip p: `0.078125`

### PVR vs switch_top1_sparse_v2_300m_matched

- Micro delta: `0.7587798396125436`
- Macro file delta: `0.7587798396125436`
- File wins: `0/8`
- Exact sign-test p: `0.0078125`
- Exact sign-flip p: `0.0078125`

### PVR vs generic_top2_sparse_v2_300m_matched

- Micro delta: `0.46071298606693745`
- Macro file delta: `0.46071298606693745`
- File wins: `3/8`
- Exact sign-test p: `0.7265625`
- Exact sign-flip p: `0.3671875`


## PVR Official Shared/Expert Decomposition

Status: `PVR_OFFICIAL_DECOMPOSITION_SELECTED_EXPERT_HELP_SUPPORTED`
Mean full-minus-shared: `-4.417329599149525`
Mean wrong-shift-minus-full: `13.963873096741736`
Full beats shared files: `8/8`
Wrong-shift harms files: `8/8`
Oracle expert selection: `NOT_RUN_NOT_IMPLEMENTED`


## PVR Final-Block All-Expert Sweep

Status: `PVR_OFFICIAL_ORACLE_EXPERT_REGRET_AUDIT_COMPLETE`

Final PVR block only; every expert is evaluated from identical final-block hidden states. Full-network oracle routing remains NOT_RUN_NOT_IMPLEMENTED.

Selected loss: `10.188022635877132`
Shared-only loss: `13.41137558221817`
Oracle loss: `8.718795716762543`
Mean wrong loss: `17.686156630516052`
Shuffled residual loss: `10.28586482256651`
Random residual loss: `20.23269349336624`
Mean router regret: `1.469227062610173`
95th-percentile router regret: `5.583189487457275`
Selected-is-oracle rate: `0.17779541015625`
Selected-is-top2 rate: `0.34967041015625`

Final-block oracle vs comparators:

| comparator | oracle - comparator micro loss |
|---|---:|
| dense_sparse_v2_300m_matched | -2.156225689686835 |
| generic_top2_sparse_v2_300m_matched | -1.008513961918652 |
| switch_top1_sparse_v2_300m_matched | -0.7104471083730459 |

Interpretation: selected experts are useful, but final-block oracle expert selection is materially better than the trained router selection. This supports a router-regret diagnosis for the available final-block expert bank while keeping full-network oracle selection marked `NOT_RUN_NOT_IMPLEMENTED`.

Claim gates:

- final_block_oracle_beats_generic_top2: `True`
- final_block_oracle_beats_switch_top1: `True`
- selected_beats_mean_wrong: `True`
- selected_beats_random_residual: `True`
- selected_beats_shared_only: `True`
- selected_beats_shuffled_residual: `True`
- selected_intervention_gate_pass: `True`


## PVR Full-Network Greedy Oracle Audit

Status: `PVR_FULL_NETWORK_GREEDY_ORACLE_EXPERT_SELECTION_COMPLETE`

Official-like development set only. Greedy blockwise full-network oracle; not exhaustive combinatorial oracle.

Selected loss: `9.797280992780413`
Greedy full-network oracle loss: `5.548307282584054`
Greedy oracle improvement over selected: `-4.248973710196359`
Selected-is-oracle rate across block decisions: `0.15187872023809523`

## Sparse Comparator Runtime Integrity

Status: `SPARSE_COMPARATOR_RUNTIME_INTEGRITY_AUDIT_COMPLETE`

- all_sparse_comparators_valid: `True`
- official_final_files_used: `False`

## Official-Like Router Auxiliary Sweep

Status: `PVR_OFFICIAL_LIKE_ROUTER_AUX_SWEEP_COMPLETE`
Winner: `pvr_sparse_v2_official_like_aux0p0005_100m`
Winner aux weight: `0.0005`
Winner final loss: `9.030747413635254`

## Phase 3-14 Bounded Completion

Status: `PVR_PHASE_3_14_BOUNDED_EXECUTION_COMPLETE`

## 300M 5M Long-Curve Validation

Status: `PVR_300M_5M_LONG_CURVE_VALIDATION_COMPLETE_WITH_AUX_FAILURE`
Decision: `PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_NOT_SUPPORTED`
Winner: `generic_top2_sparse_v2_300m_matched_long_curve`
Candidate mean eval: `11.337301993370057`
Winner mean eval: `10.32124400138855`


## Compile-Rate Interpretation

The bounded code-oriented compile check uses only 16 samples, so it is reported as descriptive evidence with Wilson intervals, not broad code capability.

| variant | compile rate | successes / samples | Wilson 95% CI |
|---|---:|---:|---|
| dense_sparse_v2_300m_matched | 0.3125 | 5 / 16 | [0.14164643854782039, 0.5559564416525933] |
| switch_top1_sparse_v2_300m_matched | 0.1875 | 3 / 16 | [0.06591599071428142, 0.4300888096197414] |
| generic_top2_sparse_v2_300m_matched | 0.375 | 6 / 16 | [0.18481232558863633, 0.6135895945449727] |
| pvr_teacher_independent_sparse_v2_300m | 0.25 | 4 / 16 | [0.10182067491213048, 0.49498316535508774] |

## Blocked Claims

- `MATCHED_INFORMATION_ROUTING_ATTRIBUTION_VALIDATION_COMPLETE`
- `PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_DENSE_GAP_CLOSED`
- `PVR_TEACHER_INDEPENDENT_SPARSE_V2_300M_OFFICIAL_BOUNDED_ADVANTAGE_SUPPORTED`
- `PVR_OFFICIAL_BROAD_NLP_SUPPORTED`
- `PVR_OFFICIAL_CODE_BENCH_SUPPORTED`
- `PVR_FROM_SCRATCH_DENSE_GAP_CLOSED`
- `PVR_TEACHER_INDEPENDENCE_SUPPORTED`
- `PVR_OFFICIAL_ROUTER_NEAR_ORACLE_SUPPORTED`
- `PVR_OFFICIAL_FULL_NETWORK_ORACLE_EXPERT_SELECTION_SUPPORTED`
- `PVR_PHASE_3_14_PROMOTION_SCALE_COMPLETE`
- `PVR_LARGER_BUDGET_CURVES_COMPLETE`
- `PVR_TEACHER_INDEPENDENT_300M_5M_OFFICIAL_LIKE_ADVANTAGE_SUPPORTED`

## Missing Strong-Claim Comparators

- Original teacher
- Dense continuation
- Dense-EAN
- Shared trunk + dense residual adapter
- Standard sparse upcycling
- Same-teacher Switch Top1
- Plain OneDelta/PVR
- OneDelta/PVR-EAN
- OneDelta/PVR-EAN-RG
- Token-matched and profiler compute-matched views
- Separately trained Top1/Top2/Top4
- Full EAN factorial with frozen/randomized/shuffled controls
