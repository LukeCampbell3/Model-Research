# Cognitive Microkernel v1

A minimal, safe, extensible runtime for recursive branch/fork cognitive processes.

## Core Doctrine

- **The LLM is not the system** — The runtime is the system
- **State is immutable or copy-on-write**
- **Claims require evidence**
- **Speculation is cheap, not fact**
- **Commits are transactional**
- **Everything is replayable**
- **Experts are interchangeable**
- **Learned policies are advisory (inactive in v1)**

## V1 Features

- ✅ Process descriptors with parent state hashes
- ✅ Content-addressed artifact store
- ✅ Evidence ledger with traceability
- ✅ Claim registry with support status tracking
- ✅ Branch generation and pruning
- ✅ Transactional commits with rollback
- ✅ Deterministic expert routing
- ✅ Replay from stored artifacts (no model calls)
- ✅ Side-effect policy enforcement
- ✅ Cache keys with state hash invalidation

## V1 Limitations

- ❌ No durable memory promotion (blocked by default)
- ❌ No active learned policies (shadow-only)
- ❌ No autonomous research (inactive by default)
- ❌ No expert adapter updates (offline only)
- ❌ No irreversible actions (requires explicit approval)
- ❌ No distributed execution (local-first)

## Architecture

```
CanonicalState
├── ArtifactStore (content-addressed)
├── EvidenceLedger
├── ClaimRegistry
├── ProcessDAG
├── TransactionLog
└── SpeculationLedger

Process Lifecycle:
1. Observe → create ProcessDescriptor
2. Page context → reference artifacts
3. Generate branch seeds
4. Expand branch sketch
5. Route to expert → get claims
6. Write evidence records
7. Verify commit candidate
8. Create transaction
9. Commit or rollback
10. Archive/replay
```

## Running

```bash
pip install -e .
pytest tests/ -v
python -m cognitive_microkernel.demo.run_demos
python -m cognitive_microkernel.demo.replay_trace <trace_id>
```

## Demo Tasks

1. **Simple planning** — Shows branch generation, evidence collection, verification
2. **Contradicted claim** — Shows claim downgrading, negative evidence storage
3. **Rollback** — Shows transaction rejection and state restoration
4. **Replay** — Shows artifact-based reconstruction without model calls

## V1 Completion Criteria

✅ Root task creates ProcessDescriptor before any execution  
✅ Process executes observe→branch→expert→claim→evidence→verify→transaction→commit/rollback  
✅ Every expert output converted to claims/evidence before affecting decisions  
✅ Branch cannot mutate canonical state directly  
✅ Verified commit creates new canonical_state_hash  
✅ Rollback restores previous canonical_state_hash  
✅ ProcessDAG can replay decision path from artifacts  
✅ Unsupported claims blocked from canonical state  
✅ Stale parent_state_hash blocks commit  
✅ Learned policies exist as inactive stubs  
✅ Durable memory promotion blocked by default  
✅ Autonomous research inactive by default  
✅ Required test suite passes  
✅ Demo tasks prove branch→claim→evidence→verify→transaction→commit/rollback→replay
