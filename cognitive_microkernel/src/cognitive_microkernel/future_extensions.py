"""Future extension stubs (inactive in v1).

Step 9: Add inactive interfaces for learned policies, expert knowledge stores,
and other advanced features that will be activated after v1 produces validated traces.
"""

from typing import Any, Optional
from abc import ABC, abstractmethod

from .schemas import (
    LearnedPolicy, ExpertKnowledgeStore,
    ProcessDescriptor, BranchProcess, EvidenceRecord, Claim,
)


# ============================================================================
# Learned Policy Interfaces (shadow-only in v1)
# ============================================================================

class LearnedPolicyInterface(ABC):
    """Base interface for learned policies (inactive in v1)."""
    
    def __init__(self, policy_id: str):
        self.policy_id = policy_id
        self.active = False  # Always False in v1
    
    @abstractmethod
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        """Make shadow predictions (no effect on execution)."""
        pass
    
    def can_activate(self) -> bool:
        """Check if policy can be activated (always False in v1)."""
        return False


class LearnedExpertRouter(LearnedPolicyInterface):
    """Learned expert router (shadow-only in v1)."""
    
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        # Shadow prediction for logging only
        return {
            "recommended_expert": "planner_v1",  # Default
            "confidence": 0.5,
            "features_used": list(features.keys()),
            "shadow_only": True,
        }


class LearnedBranchValueModel(LearnedPolicyInterface):
    """Learned branch value scorer (shadow-only in v1)."""
    
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        return {
            "predicted_value": 0.5,
            "uncertainty": 0.3,
            "recommendation": "expand",
            "shadow_only": True,
        }


class LearnedContextSelector(LearnedPolicyInterface):
    """Learned context selector (shadow-only in v1)."""
    
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        return {
            "recommended_context_refs": [],
            "relevance_scores": {},
            "shadow_only": True,
        }


class LearnedDepthPolicy(LearnedPolicyInterface):
    """Learned depth/compute allocation policy (shadow-only in v1)."""
    
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        return {
            "recommended_depth": 2,
            "recommended_width": 1,
            "budget_allocation": 0.5,
            "shadow_only": True,
        }


class LearnedResearchTrigger(LearnedPolicyInterface):
    """Learned research trigger (shadow-only in v1)."""
    
    def predict_shadow(self, features: dict[str, Any]) -> dict[str, Any]:
        return {
            "research_needed": False,
            "confidence": 0.8,
            "recommended_topics": [],
            "shadow_only": True,
        }


# ============================================================================
# Expert Knowledge Management (inactive in v1)
# ============================================================================

class ExpertKnowledgeManager:
    """Manage expert knowledge (inactive in v1)."""
    
    def __init__(self):
        self.active = False
    
    def store_trace(self, trace_data: dict[str, Any]) -> bool:
        """Store trace for future learning (no-op in v1)."""
        return False  # Not active
    
    def retrieve_knowledge(self, query: str) -> list[dict[str, Any]]:
        """Retrieve knowledge (returns empty in v1)."""
        return []
    
    def can_train_adapters(self) -> bool:
        """Check if adapter training is possible (False in v1)."""
        return False


class ExpertReplayBuffer:
    """Replay buffer for expert training (inactive in v1)."""
    
    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.buffer = []
        self.active = False
    
    def add_experience(self, experience: dict[str, Any]) -> None:
        """Add experience to buffer (no-op in v1)."""
        pass  # Not active
    
    def sample_batch(self, batch_size: int) -> list[dict[str, Any]]:
        """Sample batch for training (returns empty in v1)."""
        return []
    
    def is_ready_for_training(self) -> bool:
        """Check if buffer has enough data (False in v1)."""
        return False


class ExpertAdapterRegistry:
    """Registry for expert adapters (inactive in v1)."""
    
    def __init__(self):
        self.adapters = {}
        self.active = False
    
    def register_adapter(self, adapter_id: str, adapter_data: dict[str, Any]) -> bool:
        """Register an adapter (no-op in v1)."""
        return False  # Not active
    
    def get_adapter(self, adapter_id: str) -> Optional[dict[str, Any]]:
        """Get adapter (returns None in v1)."""
        return None
    
    def list_adapters(self) -> list[str]:
        """List available adapters (empty in v1)."""
        return []


# ============================================================================
# Policy Shadow Runner (logs only, no execution control)
# ============================================================================

class PolicyShadowRunner:
    """Run policies in shadow mode for evaluation."""
    
    def __init__(self):
        self.policies = {
            "expert_router": LearnedExpertRouter("shadow_router_v1"),
            "branch_value": LearnedBranchValueModel("shadow_branch_value_v1"),
            "context_selector": LearnedContextSelector("shadow_context_v1"),
            "depth_policy": LearnedDepthPolicy("shadow_depth_v1"),
            "research_trigger": LearnedResearchTrigger("shadow_research_v1"),
        }
        self.shadow_logs = []
    
    def run_shadow_evaluation(
        self,
        process: ProcessDescriptor,
        heuristic_result: dict[str, Any],
    ) -> dict[str, Any]:
        """Run shadow evaluation and log differences."""
        
        shadow_results = {}
        
        for policy_name, policy in self.policies.items():
            # Create features for policy
            features = self._extract_features(process, heuristic_result)
            
            # Get shadow prediction
            shadow_pred = policy.predict_shadow(features)
            shadow_results[policy_name] = shadow_pred
            
            # Log difference from heuristic
            diff = self._compute_difference(heuristic_result, shadow_pred)
            if diff:
                self.shadow_logs.append({
                    "timestamp": "2024-01-01T00:00:00Z",  # Placeholder
                    "process_id": process.process_id,
                    "policy": policy_name,
                    "heuristic_result": heuristic_result,
                    "shadow_prediction": shadow_pred,
                    "difference": diff,
                })
        
        return shadow_results
    
    def _extract_features(
        self,
        process: ProcessDescriptor,
        heuristic_result: dict[str, Any],
    ) -> dict[str, Any]:
        """Extract features for policy evaluation."""
        return {
            "process_type": process.process_type,
            "side_effect_policy": process.side_effect_policy.value,
            "budget_remaining": process.budget_remaining,
            "heuristic_decision": heuristic_result.get("decision", ""),
            "heuristic_confidence": heuristic_result.get("confidence", 0.5),
        }
    
    def _compute_difference(
        self,
        heuristic: dict[str, Any],
        shadow: dict[str, Any],
    ) -> dict[str, Any]:
        """Compute difference between heuristic and shadow results."""
        diff = {}
        
        for key in set(heuristic.keys()) & set(shadow.keys()):
            if isinstance(heuristic[key], (int, float)) and isinstance(shadow[key], (int, float)):
                diff[f"{key}_diff"] = shadow[key] - heuristic[key]
        
        return diff
    
    def get_shadow_logs(self) -> list[dict[str, Any]]:
        """Get shadow evaluation logs."""
        return self.shadow_logs.copy()


# ============================================================================
# Promotion Gates (blocked by default in v1)
# ============================================================================

class PolicyPromotionGate:
    """Gate for promoting policies from shadow to active (blocked in v1)."""
    
    def __init__(self):
        self.promotion_criteria = {
            "min_validated_traces": 1000,
            "max_false_accept_rate": 0.05,
            "min_improvement_over_heuristic": 0.1,
            "requires_human_approval": True,
        }
    
    def evaluate_for_promotion(
        self,
        policy_id: str,
        shadow_metrics: dict[str, Any],
        validation_traces: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Evaluate policy for promotion (always rejects in v1)."""
        
        return {
            "can_promote": False,
            "reason": "Policy promotion not enabled in v1",
            "criteria_met": {},
            "validation_passed": False,
            "requires_manual_review": True,
            "blocked_by_default": True,  # Key v1 constraint
        }
    
    def request_promotion(self, policy_id: str) -> bool:
        """Request promotion (always False in v1)."""
        return False


class MemoryPromotionGate:
    """Gate for promoting items to durable memory (blocked in v1)."""
    
    def __init__(self):
        self.active = False  # Always False in v1
    
    def evaluate_memory_promotion(
        self,
        item: dict[str, Any],
        evidence_refs: list[str],
        usage_history: dict[str, Any],
    ) -> dict[str, Any]:
        """Evaluate item for memory promotion (always rejects in v1)."""
        
        return {
            "can_promote": False,
            "reason": "Durable memory promotion not enabled in v1",
            "evidence_sufficient": False,
            "usage_justified": False,
            "safety_check_passed": False,
            "blocked_by_default": True,  # Key v1 constraint
        }
    
    def is_promotion_allowed(self) -> bool:
        """Check if memory promotion is allowed (False in v1)."""
        return False


# ============================================================================
# Research Process Manager (inactive by default in v1)
# ============================================================================

class ResearchProcessManager:
    """Manager for research processes (inactive by default in v1)."""
    
    def __init__(self):
        self.active = False  # Inactive by default in v1
        self.research_queue = []
    
    def can_initiate_research(
        self,
        topic: str,
        justification: str,
    ) -> dict[str, Any]:
        """Check if research can be initiated (False in v1)."""
        
        return {
            "allowed": False,
            "reason": "Autonomous research not enabled in v1",
            "requires_manual_enable": True,
            "queue_position": len(self.research_queue),
            "estimated_cost": 0.0,
            "blocked_by_default": True,  # Key v1 constraint
        }
    
    def initiate_research(
        self,
        topic: str,
        justification: str,
        budget: float,
    ) -> Optional[str]:
        """Initiate research (returns None in v1)."""
        return None  # Not active
    
    def get_research_status(self) -> dict[str, Any]:
        """Get research status (inactive in v1)."""
        return {
            "active": False,
            "queue_size": 0,
            "current_research": None,
            "total_completed": 0,
            "enabled": False,
        }


# ============================================================================
# Future Extension Registry
# ============================================================================

class FutureExtensionRegistry:
    """Registry of future extensions (all inactive in v1)."""
    
    def __init__(self):
        self.extensions = {
            "learned_policies": {
                "expert_router": LearnedExpertRouter("shadow_router_v1"),
                "branch_value": LearnedBranchValueModel("shadow_branch_value_v1"),
                "context_selector": LearnedContextSelector("shadow_context_v1"),
                "depth_policy": LearnedDepthPolicy("shadow_depth_v1"),
                "research_trigger": LearnedResearchTrigger("shadow_research_v1"),
                "active": False,
            },
            "expert_knowledge": {
                "manager": ExpertKnowledgeManager(),
                "replay_buffer": ExpertReplayBuffer(),
                "adapter_registry": ExpertAdapterRegistry(),
                "active": False,
            },
            "policy_shadow": {
                "runner": PolicyShadowRunner(),
                "active": True,  # Shadow running is allowed for logging
            },
            "promotion_gates": {
                "policy_promotion": PolicyPromotionGate(),
                "memory_promotion": MemoryPromotionGate(),
                "active": False,
            },
            "research": {
                "manager": ResearchProcessManager(),
                "active": False,
            },
        }
    
    def get_extension(self, category: str, name: str) -> Optional[Any]:
        """Get an extension by category and name."""
        category_data = self.extensions.get(category, {})
        return category_data.get(name)
    
    def is_active(self, category: str) -> bool:
        """Check if an extension category is active."""
        category_data = self.extensions.get(category, {})
        return category_data.get("active", False)
    
    def list_extensions(self) -> dict[str, Any]:
        """List all extensions with status."""
        status = {}
        
        for category, data in self.extensions.items():
            status[category] = {
                "active": data.get("active", False),
                "components": [k for k in data.keys() if k != "active"],
                "can_activate": False,  # Cannot activate in v1
            }
        
        return status
    
    def can_activate_extension(self, category: str) -> bool:
        """Check if an extension can be activated (False in v1)."""
        return False  # No extensions can be activated in v1
