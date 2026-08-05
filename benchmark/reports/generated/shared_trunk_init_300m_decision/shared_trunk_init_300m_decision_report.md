# Shared-Trunk Init 300M Decision

Status: `PVR_SHARED_TRUNK_INIT_300M_DENSE_GAP_CLOSED`

Training eval-curve comparison:
- dense reference mean eval loss: `5.800183653831482`
- PVR baseline mean eval loss: `5.518721175193787`
- PVR shared-init mean eval loss: `4.99695086479187`
- shared-init minus baseline: `-0.5217703104019167`
- shared-init minus dense: `-0.8032327890396118`

Reduced LM scorecard comparison:
- dense reference LM loss: `3.305846790075302`
- PVR baseline LM loss: `3.5067039370536803`
- PVR shared-init LM loss: `3.0314649403095246`
- shared-init minus baseline: `-0.4752389967441557`
- shared-init minus dense: `-0.2743818497657773`

Route stability:
- Top1 invariants clean: `True`
- route stable: `True`
- route margin delta: `0.010296393473314902`

Scope: this supports teacher-initialized sparse transfer/compression, not from-scratch PVR dominance.
