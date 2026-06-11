"""Phase 3: Research Gateway, Evidence v2, Context Compiler, Adjudicator, Policy Memory.

Adds:
- ResearchGateway: bounded autonomous research initiation
- PromptInjectionBoundary: input sanitization at expert boundary
- EvidencePacket v2: structured evidence with provenance chains
- ReplayPatternMemory: learn from replay traces
- PolicyMemory with decay: time-decayed learned heuristics
- ContextCompiler: compile context pages for expert inputs
- Adjudicator: resolve conflicts between branch outcomes
- PromotionGate: evidence-gated capability upgrades
- RuntimeAuditReporter: structured audit trail generation

Phase 3 does NOT violate Phase 2 invariants:
- Compiler authority boundary remains frozen
- BranchPlan remains advisory (not commit authority)
- CommitManager remains sole state mutator
"""

from .research_gateway import ResearchGateway, ResearchRequest, ResearchBounds
from .prompt_injection_boundary import PromptInjectionBoundary, SanitizationResult
from .evidence_packet import EvidencePacket, ProvenanceChain, ProvenanceNode
from .replay_pattern_memory import ReplayPatternMemory, ReplayPattern
from .policy_memory import PolicyMemory, PolicyEntry, DecaySchedule
from .context_compiler import ContextCompiler, ContextPage, ContextBudget
from .adjudicator import Adjudicator, AdjudicationResult, ConflictResolution
from .promotion_gate import PromotionGate, PromotionRequest, PromotionVerdict
from .audit_reporter import RuntimeAuditReporter, AuditEvent, AuditReport

__all__ = [
    "ResearchGateway", "ResearchRequest", "ResearchBounds",
    "PromptInjectionBoundary", "SanitizationResult",
    "EvidencePacket", "ProvenanceChain", "ProvenanceNode",
    "ReplayPatternMemory", "ReplayPattern",
    "PolicyMemory", "PolicyEntry", "DecaySchedule",
    "ContextCompiler", "ContextPage", "ContextBudget",
    "Adjudicator", "AdjudicationResult", "ConflictResolution",
    "PromotionGate", "PromotionRequest", "PromotionVerdict",
    "RuntimeAuditReporter", "AuditEvent", "AuditReport",
]
