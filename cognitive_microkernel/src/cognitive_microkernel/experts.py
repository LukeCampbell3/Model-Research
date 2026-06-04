"""Expert ABI and deterministic routing.

Step 4: Implement expert interface, ABI validator, and deterministic heuristic routing.
"""

import json
import hashlib
from typing import Optional, Any
from abc import ABC, abstractmethod

from .schemas import (
    ExpertInput, ExpertOutput, ProcessDescriptor, Claim, EvidenceRecord,
    SupportStatus, SideEffectPolicy, EvidenceSourceType, ArtifactType,
)


class Expert(ABC):
    """Abstract base class for interchangeable experts."""
    
    def __init__(self, expert_id: str, expert_version: str = "v1"):
        self.expert_id = expert_id
        self.expert_version = expert_version
    
    @abstractmethod
    def execute(self, input_data: ExpertInput) -> ExpertOutput:
        """Execute expert work and return output."""
        pass
    
    @property
    def capabilities(self) -> dict[str, Any]:
        """Get expert capabilities."""
        return {
            "expert_id": self.expert_id,
            "version": self.expert_version,
            "supported_output_schemas": [],
            "max_token_budget": 10000,
            "supported_tools": [],
            "risk_levels": ["low", "medium", "high"],
            "requires_verification": True,
        }


class PlannerExpert(Expert):
    """Planner expert for generating branch seeds and sketches."""
    
    def execute(self, input_data: ExpertInput) -> ExpertOutput:
        # In a real implementation, this would call an LLM
        # For v1, we return a deterministic mock response
        
        claims = [
            "The task requires multiple steps",
            "The solution should be modular",
            "Testing is required before deployment",
        ]
        
        return ExpertOutput(
            expert_id=self.expert_id,
            expert_version=self.expert_version,
            output_type="branch_seeds",
            claims=claims,
            confidence=0.7,
            uncertainty=0.3,
            evidence_refs_used=input_data.evidence_refs,
            claim_refs_used=input_data.claim_refs,
            support_tags=["inferred", "speculative"],
            detected_risks=["scope_creep", "missing_constraints"],
            expected_value_delta=0.5,
            cost_used=0.1,
            recommended_next_processes=["verifier", "context_retriever"],
            validation_required=True,
            raw_output_ref="planner_output_artifact",
        )


class VerifierExpert(Expert):
    """Verifier expert for validating claims and evidence."""
    
    def execute(self, input_data: ExpertInput) -> ExpertOutput:
        return ExpertOutput(
            expert_id=self.expert_id,
            expert_version=self.expert_version,
            output_type="verification_report",
            claims=["All claims are plausible given current evidence"],
            confidence=0.8,
            uncertainty=0.2,
            evidence_refs_used=input_data.evidence_refs,
            claim_refs_used=input_data.claim_refs,
            support_tags=["supported"],
            detected_risks=["insufficient_evidence"],
            expected_value_delta=0.2,
            cost_used=0.05,
            recommended_next_processes=[],
            validation_required=False,
            raw_output_ref="verifier_output_artifact",
        )


class ClaimExtractorExpert(Expert):
    """Expert for extracting claims from expert outputs."""
    
    def execute(self, input_data: ExpertInput) -> ExpertOutput:
        claims = [
            "Expert confidence level is medium",
            "Further verification recommended",
            "Multiple approaches possible",
        ]
        
        return ExpertOutput(
            expert_id=self.expert_id,
            expert_version=self.expert_version,
            output_type="extracted_claims",
            claims=claims,
            confidence=0.9,
            uncertainty=0.1,
            evidence_refs_used=input_data.evidence_refs,
            claim_refs_used=input_data.claim_refs,
            support_tags=["inferred"],
            detected_risks=["claim_overgeneralization"],
            expected_value_delta=0.1,
            cost_used=0.02,
            recommended_next_processes=["verifier"],
            validation_required=True,
            raw_output_ref="claim_extractor_output_artifact",
        )


class ExpertABIValidator:
    """Validate expert outputs against ABI requirements."""
    
    @staticmethod
    def validate_output(output: ExpertOutput) -> tuple[bool, list[str]]:
        """Validate expert output.
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        # Check required fields
        if not output.expert_id:
            errors.append("Missing expert_id")
        
        if not output.output_type:
            errors.append("Missing output_type")
        
        # Check support tags
        if not output.support_tags:
            errors.append("Missing support_tags")
        
        # Check raw output ref (for non-trivial outputs)
        if output.output_type not in ["simple_ack", "empty"] and not output.raw_output_ref:
            errors.append("Missing raw_output_ref for significant output")
        
        # Check claim format
        for claim in output.claims:
            if not isinstance(claim, str) or len(claim) > 1000:
                errors.append(f"Invalid claim format: {claim[:100]}...")
        
        # Check confidence bounds
        if not 0 <= output.confidence <= 1:
            errors.append(f"Confidence out of bounds: {output.confidence}")
        
        if not 0 <= output.uncertainty <= 1:
            errors.append(f"Uncertainty out of bounds: {output.uncertainty}")
        
        # Check cost used
        if output.cost_used < 0:
            errors.append(f"Negative cost used: {output.cost_used}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def check_compatibility(process: ProcessDescriptor, expert: Expert) -> tuple[bool, str]:
        """Check if expert is compatible with process requirements.
        
        In v1, compatibility is based on process type matching rather than
        strict schema validation since experts use deterministic heuristic routing.
        """
        # Check output schema compatibility (if expert declares supported schemas)
        expected_schema = process.expected_output_schema
        supported_schemas = expert.capabilities.get("supported_output_schemas", [])
        
        if supported_schemas and expected_schema not in supported_schemas:
            return False, f"Expert does not support output schema: {expected_schema}"
        
        # Check budget compatibility
        max_expert_budget = expert.capabilities.get("max_token_budget", 0)
        if max_expert_budget > 0 and process.max_tokens > max_expert_budget:
            return False, f"Process budget ({process.max_tokens}) exceeds expert capacity ({max_expert_budget})"
        
        # Check side-effect policy compatibility
        if process.side_effect_policy in [
            SideEffectPolicy.EXTERNAL_REVERSIBLE_ACTION,
            SideEffectPolicy.EXTERNAL_IRREVERSIBLE_ACTION,
        ]:
            if "external_tools" not in expert.capabilities.get("supported_tools", []):
                return False, "Expert does not support external actions"
        
        return True, "Compatible"


class SupportTagValidator:
    """Validate support tags on expert outputs and claims."""
    
    @staticmethod
    def validate_tags(tags: list[str]) -> bool:
        """Validate support tags."""
        valid_tags = {"supported", "inferred", "speculative", "unsupported", "contradicted"}
        return all(tag in valid_tags for tag in tags)
    
    @staticmethod
    def get_claim_support_status(tags: list[str]) -> SupportStatus:
        """Convert support tags to claim support status."""
        if "contradicted" in tags:
            return SupportStatus.CONTRADICTED
        elif "unsupported" in tags:
            return SupportStatus.UNSUPPORTED
        elif "speculative" in tags:
            return SupportStatus.SPECULATIVE
        elif "inferred" in tags:
            return SupportStatus.INFERRED
        elif "supported" in tags:
            return SupportStatus.SUPPORTED
        else:
            return SupportStatus.UNSUPPORTED


class EvidenceRefValidator:
    """Validate evidence references."""
    
    def __init__(self, storage):
        self.storage = storage
    
    def validate_refs(self, evidence_refs: list[str]) -> tuple[bool, list[str]]:
        """Validate evidence references exist."""
        valid = True
        missing = []
        
        for ref in evidence_refs:
            evidence = self.storage.evidence_ledger.get_evidence(ref)
            if not evidence:
                valid = False
                missing.append(ref)
        
        return valid, missing


class ExpertRouter:
    """Deterministic heuristic router for v1."""
    
    def __init__(self):
        self.experts = {
            "planner_v1": PlannerExpert("planner_v1"),
            "verifier_v1": VerifierExpert("verifier_v1"),
            "claim_extractor_v1": ClaimExtractorExpert("claim_extractor_v1"),
        }
    
    def route(
        self,
        process: ProcessDescriptor,
        required_context_refs: list[str],
    ) -> tuple[Optional[str], dict[str, Any]]:
        """Route process to compatible expert using deterministic heuristics.
        
        Returns:
            Tuple of (selected_expert_id, routing_result)
        """
        routing_result = {
            "compatibility_result": {},
            "reason_selected": "",
            "fallback_expert_id": None,
            "requires_verification": True,
        }
        
        # Simple heuristic routing based on process type
        process_type = process.process_type
        
        if "plan" in process_type or "branch" in process_type:
            candidate = "planner_v1"
            reason = "Process requires planning/branch generation"
        
        elif "verify" in process_type or "validate" in process_type:
            candidate = "verifier_v1"
            reason = "Process requires verification"
        
        elif "extract" in process_type or "claim" in process_type:
            candidate = "claim_extractor_v1"
            reason = "Process requires claim extraction"
        
        else:
            # Default to planner
            candidate = "planner_v1"
            reason = "Default routing to planner"
        
        # Check compatibility
        expert = self.experts.get(candidate)
        if not expert:
            routing_result["reason_selected"] = f"No expert found: {candidate}"
            return None, routing_result
        
        compatible, compat_reason = ExpertABIValidator.check_compatibility(process, expert)
        routing_result["compatibility_result"][candidate] = {
            "compatible": compatible,
            "reason": compat_reason,
        }
        
        if not compatible:
            # Try fallback
            for expert_id, fallback_expert in self.experts.items():
                if expert_id == candidate:
                    continue
                
                compatible, compat_reason = ExpertABIValidator.check_compatibility(process, fallback_expert)
                routing_result["compatibility_result"][expert_id] = {
                    "compatible": compatible,
                    "reason": compat_reason,
                }
                
                if compatible:
                    candidate = expert_id
                    reason = f"Fallback: {compat_reason}"
                    routing_result["fallback_expert_id"] = expert_id
                    break
        
        if not compatible:
            routing_result["reason_selected"] = "No compatible expert found"
            return None, routing_result
        
        # Set verification requirement based on expert
        routing_result["requires_verification"] = expert.capabilities.get("requires_verification", True)
        routing_result["reason_selected"] = reason
        
        return candidate, routing_result


class ExpertCompatibilityTester:
    """Test expert compatibility with processes."""
    
    def __init__(self, router: ExpertRouter):
        self.router = router
    
    def test_compatibility(self, process: ProcessDescriptor) -> dict[str, Any]:
        """Test compatibility with all experts."""
        results = {}
        
        for expert_id, expert in self.router.experts.items():
            compatible, reason = ExpertABIValidator.check_compatibility(process, expert)
            results[expert_id] = {
                "compatible": compatible,
                "reason": reason,
                "capabilities": expert.capabilities,
            }
        
        return results
