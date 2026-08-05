# Shared Approximation Bottleneck Report

Status: `PVR_SHARED_TRUNK_INIT_SUPPORTED`
Secondary status: `PVR_ROUTING_NOT_MAIN_BOTTLENECK`

| variant | final train delta | mean eval delta | route margin delta | route stable |
|---|---:|---:|---:|---|
| baseline | 0.0 | 0.0 | 0.0 | True |
| gated_teacher_low_confidence_only | 0.0005259513854980469 | -0.003212976455688299 | 0.0005040076430304907 | True |
| shared_capacity_plus | 0.11414194107055664 | -0.31337451934814453 | -0.17272194760298587 | True |
| shared_trunk_init_from_dense | -0.10579204559326172 | -1.69472804069519 | -0.27187080219785764 | True |

Deprecated paths were not used: prior in-bounds head, route-confidence regularizer, and persistent global dense KL.