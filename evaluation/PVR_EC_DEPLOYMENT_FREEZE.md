# PVR-EC Descriptor Curriculum Deployment — FROZEN

**Frozen:** 2026-06-21
**Status:** PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED
**Release:** PVR_EC_RELEASE_READY_FOR_CANARY
**Tests:** 638 pass

---

## Scope Separation

This result is frozen as a **descriptor-curriculum deployment result**.

It is NOT merged into:
- PVR-EC-O 300M/700M LM frontier claims
- EAN retention-gated delta replay results
- Self-instilled uniformity geometry head results

These are separate research branches with different evidence bases.

---

## What Is Confirmed

The descriptor-controlled candidate creates a **controllable semantic routing/identity channel** under strict Top1 execution.

| Evidence | Value |
|----------|-------|
| Mean descriptor accuracy (5 seeds) | 95.1% |
| Descriptor control margin | 18.7% |
| Min seed margin | 5.2% (seed 42) |
| Max seed margin | 52.7% (seed 777) |
| Descriptor removed accuracy | 26.6% |
| Heldout task-family accuracy | 80.9% |
| Production shape profile | 100% pass |
| Top1 purity | Clean |
| Forward purity counters | All zero |
| Tests confirmed | 638 |

The ablation is the critical signal:
- **Descriptor present:** ~95% accuracy
- **Descriptor removed:** 26.6% accuracy

The descriptor is not decorative. It is a real control path.

---

## Deployment Gates (All Pass)

| Gate | Status |
|------|--------|
| Forward purity | ✓ |
| Multi-seed repeatability | ✓ |
| QPM/memory | ✓ |
| Calibration/reliability | ✓ |
| Descriptor control | ✓ |
| Family/task regression | ✓ |
| Failure observatory | ✓ |

---

## What This Does NOT Prove

- ✗ 300M/700M LM frontier capability
- ✗ Teacher-EAN independence at scale
- ✗ Self-instilled uniformity head capability
- ✗ Broad SWE-bench-class coding
- ✗ Multi-language coding model readiness
- ✗ Production deployment at scale

---

## Relationship to Other Branches

### Uniformity Geometry Head (300M)
- Mechanically healthy geometry
- Capability weak
- Does NOT beat no-head warmup
- Teacher EAN still required

### Descriptor Curriculum (this branch)
- Semantically meaningful
- Ablation-supported
- Multi-seed stable
- Deployment-gated
- Canary-ready in small production profile

### EAN Retention-Gated (700M)
- Active-compute frontier
- Local reduced-file LM evaluation
- Separate evidence base

---

## Research Hypothesis Update

The uniformity head failed to replace EAN because it created geometric regularity without useful capability.

The descriptor curriculum is different: it creates **usable semantic control**, not just geometric regularity.

The next research hypothesis shifts from:
> "Can pure uniformity create EAN-like geometry?"

to:
> "Can descriptor-conditioned curriculum create self-instilled routeable geometry that reduces EAN dependence?"

---

## Recommended Next Experiment

```
PVR_DESCRIPTOR_CURRICULUM_AS_SELF_INSTILLED_EAN_SCAFFOLD_SCREEN
```

Variants:
1. `pvr_full_scratch_300m` — no teacher, no head
2. `pvr_shared_warmup_no_head_300m` — shared init, no geometry head
3. `pvr_uniformity_geometry_head_300m` — uniformity head (current)
4. `pvr_descriptor_curriculum_head_300m` — descriptor curriculum as geometry head
5. `pvr_descriptor_plus_uniformity_head_300m` — combined
6. `pvr_teacher_ean_300m` — teacher EAN baseline

**Key question:** Does descriptor curriculum close more of the teacher-EAN gap than pure uniformity?

**Success label:** `PVR_DESCRIPTOR_CURRICULUM_NARROWS_EAN_GAP`
**Strong label:** `PVR_DESCRIPTOR_CURRICULUM_REPLACES_EAN_SCAFFOLD` (only if it matches/beats teacher-EAN without importing a dense checkpoint)

---

## Bottom Line

| Branch | Status | Next |
|--------|--------|------|
| Deployment (descriptor) | ✓ Canary-ready | Ship to 1% canary |
| Research (uniformity head) | ✗ Insufficient | Replace with descriptor curriculum |
| Research (EAN frontier) | ✓ Active | Bridge to descriptor self-instillation |

The descriptor system is currently the best evidence that PVR can learn a controllable routing basis without relying purely on imported dense EAN geometry.
