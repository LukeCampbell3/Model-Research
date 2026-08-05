# PVR-EC-O Shared Trunk Init Copy-Scope Ablation Plan

Status: `PVR_SHARED_TRUNK_INIT_COPY_SCOPE_ABLATION_READY_NOT_RUN`

```json
{
  "candidate": "pvr_ec_o_full_shared_trunk_init_v1",
  "copy_scopes": [
    "embeddings_only",
    "attention_only",
    "norms_only",
    "shared_ffn_bias_only",
    "embeddings_attention_norms",
    "full_compatible_shared_copy"
  ],
  "created_at": "2026-06-14T17:56:45.588052+00:00",
  "decision_rule": "A scope is supported only if it improves mean eval loss versus matched PVR baseline, does not materially regress final train loss, keeps Top1 invariants clean, and preserves route stability.",
  "git_commit": "5c61a4cb1d93ca182847b75483687d1c344bc328",
  "reason_not_run": "The high-value 300M confirmation is complete; this artifact freezes the ablation matrix without launching six additional 300M 4k-step jobs.",
  "required_budget_per_scope": {
    "effective_batch_tokens": 256,
    "eval_windows": 10,
    "optimizer_steps": 4000,
    "routing_windows_for_pvr": 10,
    "training_tokens_seen": 1024000
  },
  "runner_support": {
    "copy_scope_argument": true,
    "function": "benchmark.runners.run_shared_approximation_bottleneck.copy_compatible_dense_weights_to_pvr"
  },
  "schema_version": "1.0",
  "status": "PVR_SHARED_TRUNK_INIT_COPY_SCOPE_ABLATION_READY_NOT_RUN"
}
```
