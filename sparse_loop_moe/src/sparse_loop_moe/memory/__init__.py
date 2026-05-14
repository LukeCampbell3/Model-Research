"""Phase 8: Memory Architecture.

Layered memory system:
- Fast memory: disposable task-local scratchpad
- Episodic memory: stores task attempts, failures, repairs, outcomes
- Semantic memory: stores distilled reusable rules
- Adapter memory: stores domain-specific temporary skill patches
- Sparse memory slots: isolated knowledge updates
- Consolidation layer: promotes repeated validated lessons
"""

from sparse_loop_moe.memory.memory_store import (
    FastMemory,
    EpisodicMemory,
    SemanticMemory,
    AdapterMemory,
    MemoryStore,
)

__all__ = [
    "FastMemory",
    "EpisodicMemory",
    "SemanticMemory",
    "AdapterMemory",
    "MemoryStore",
]
