# PVR-EC-O + Cognitive Microkernel: Forward Roadmap

## Current State

| Component | Status |
|-----------|--------|
| PVR-EC-O Model | `PVR_EC_DEPLOYMENT_CANDIDATE_CONFIRMED` |
| Release Hardening | `PVR_EC_RELEASE_READY_FOR_CANARY` |
| Cognitive Microkernel | V1 Complete |
| Integration | Not started |

## Phases

### [Phase 1: Integration Foundation](phase1.md)
Connect PVR-EC-O as the cognitive microkernel's first expert backend.
- Expert interface adapter
- Evidence translation layer
- Descriptor-to-process mapping
- Trace replay compatibility
- Forward purity enforcement

### [Phase 2: Learned Policy Activation](phase2.md)
Promote microkernel policies from shadow-only to conditionally-active.
- Policy training from PVR-EC-O traces
- Evidence-gated promotion pipeline
- Expert router, branch value, depth policies
- Auto-rollback on regression
- Drift monitoring for policies

### [Phase 3: Multi-Expert Orchestration](phase3.md)
Evolve to multi-expert system with durable memory and research.
- Multiple specialized experts
- Durable memory promotion (evidence-gated)
- Controlled autonomous research (bounded)
- Expert adapter training (offline)
- Full cognitive architecture active

## Doctrine

1. **PVR-EC-O remains Top1-only** — no runtime Top2/Top4 in any phase
2. **Evidence gates all state changes** — claims need support, promotions need validation
3. **Everything is replayable** — full audit trail from traces
4. **Rollback is always possible** — no irreversible mutations
5. **Safety layers are additive** — each phase adds constraints, never removes them
6. **Research and deployment verdicts are separate** — research success ≠ production readiness
