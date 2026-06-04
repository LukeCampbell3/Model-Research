"""Trace collection for learning readiness.

Step 8: Implement trace collection, labeling, and replay log writing.
Do not train policies yet - just collect traces for future learning.
"""

import json
import hashlib
from datetime import datetime
from typing import Any, Optional
from pathlib import Path

from .schemas import (
    ProcessDescriptor, ProcessNode, EvidenceRecord, Claim, Transaction,
    ReplayTrace, SupportStatus,
)
from .storage import StorageManager


class LearningTraceCollector:
    """Collect traces for future learning."""
    
    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.active_traces = {}
    
    def start_trace(self, process: ProcessDescriptor) -> str:
        """Start collecting a trace for a process."""
        trace_id = f"trace_{hashlib.sha256(process.process_id.encode()).hexdigest()[:16]}"
        
        self.active_traces[trace_id] = {
            "process_id": process.process_id,
            "start_time": datetime.utcnow(),
            "events": [],
            "artifacts": [],
            "evidence": [],
            "claims": [],
            "decisions": [],
        }
        
        # Record start event
        self._record_event(trace_id, "process_start", {
            "process_type": process.process_type,
            "parent_state_hash": process.parent_state_hash,
            "side_effect_policy": process.side_effect_policy.value,
            "expected_output_schema": process.expected_output_schema,
        })
        
        return trace_id
    
    def record_expert_call(
        self,
        trace_id: str,
        expert_id: str,
        input_data: dict[str, Any],
        output_data: dict[str, Any],
    ) -> None:
        """Record an expert call in the trace."""
        self._record_event(trace_id, "expert_call", {
            "expert_id": expert_id,
            "input_hash": hashlib.sha256(json.dumps(input_data, sort_keys=True).encode()).hexdigest()[:16],
            "output_summary": str(output_data)[:200],
            "timestamp": datetime.utcnow().isoformat(),
        })
    
    def record_evidence_creation(
        self,
        trace_id: str,
        evidence: EvidenceRecord,
    ) -> None:
        """Record evidence creation in trace."""
        if trace_id in self.active_traces:
            self.active_traces[trace_id]["evidence"].append(evidence.evidence_id)
        
        self._record_event(trace_id, "evidence_created", {
            "evidence_id": evidence.evidence_id,
            "source_type": evidence.source_type.value,
            "summary": evidence.summary[:100],
            "reliability": evidence.reliability,
        })
    
    def record_claim_extraction(
        self,
        trace_id: str,
        claim: Claim,
    ) -> None:
        """Record claim extraction in trace."""
        if trace_id in self.active_traces:
            self.active_traces[trace_id]["claims"].append(claim.claim_id)
        
        self._record_event(trace_id, "claim_extracted", {
            "claim_id": claim.claim_id,
            "support_status": claim.support_status.value,
            "scope": claim.scope,
            "confidence": claim.confidence,
        })
    
    def record_branch_decision(
        self,
        trace_id: str,
        branch_id: str,
        decision: str,
        reason: str,
        alternatives: list[str],
    ) -> None:
        """Record a branch decision in trace."""
        if trace_id in self.active_traces:
            self.active_traces[trace_id]["decisions"].append({
                "branch_id": branch_id,
                "decision": decision,
                "reason": reason,
                "alternatives": alternatives,
                "timestamp": datetime.utcnow().isoformat(),
            })
        
        self._record_event(trace_id, "branch_decision", {
            "branch_id": branch_id,
            "decision": decision,
            "reason": reason,
            "alternative_count": len(alternatives),
        })
    
    def record_transaction(
        self,
        trace_id: str,
        transaction: Transaction,
        outcome: str,
        new_state_hash: Optional[str] = None,
    ) -> None:
        """Record a transaction in trace."""
        self._record_event(trace_id, "transaction", {
            "transaction_id": transaction.transaction_id,
            "status": transaction.status.value,
            "outcome": outcome,
            "new_state_hash": new_state_hash,
            "verification_refs": len(transaction.verification_refs),
        })
    
    def end_trace(
        self,
        trace_id: str,
        process: ProcessDescriptor,
        outcome: str,
        metrics: dict[str, Any],
    ) -> dict[str, Any]:
        """End trace collection and return trace data."""
        if trace_id not in self.active_traces:
            return {}
        
        trace_data = self.active_traces[trace_id]
        trace_data["end_time"] = datetime.utcnow()
        trace_data["process_outcome"] = outcome
        trace_data["metrics"] = metrics
        trace_data["duration_seconds"] = (
            trace_data["end_time"] - trace_data["start_time"]
        ).total_seconds()
        
        # Record end event
        self._record_event(trace_id, "process_end", {
            "outcome": outcome,
            "final_status": process.status.value,
            "duration_seconds": trace_data["duration_seconds"],
        })
        
        # Finalize trace
        finalized_trace = trace_data.copy()
        
        # Remove from active traces
        del self.active_traces[trace_id]
        
        return finalized_trace
    
    def _record_event(self, trace_id: str, event_type: str, data: dict[str, Any]) -> None:
        """Record an event in the trace."""
        if trace_id in self.active_traces:
            self.active_traces[trace_id]["events"].append({
                "type": event_type,
                "timestamp": datetime.utcnow().isoformat(),
                "data": data,
            })


class TraceLabeler:
    """Label traces with outcomes for learning."""
    
    @staticmethod
    def label_trace(trace_data: dict[str, Any], ground_truth: Optional[Any] = None) -> dict[str, Any]:
        """Label a trace with outcome information."""
        
        labeled_trace = trace_data.copy()
        
        # Extract labels from trace events
        labels = {
            "success": False,
            "efficient": False,
            "safe": True,
            "useful_for_learning": False,
        }
        
        # Determine success from process outcome
        outcome = trace_data.get("process_outcome", "")
        if "success" in outcome.lower() or "completed" in outcome.lower():
            labels["success"] = True
        
        # Check efficiency
        duration = trace_data.get("duration_seconds", 0)
        event_count = len(trace_data.get("events", []))
        if event_count > 0 and duration / event_count < 5.0:  # Less than 5 seconds per event
            labels["efficient"] = True
        
        # Check safety (no unsupported claims, no rejected transactions)
        events = trace_data.get("events", [])
        for event in events:
            if event["type"] == "claim_extracted":
                if event["data"].get("support_status") == SupportStatus.UNSUPPORTED.value:
                    labels["safe"] = False
            elif event["type"] == "transaction":
                if event["data"].get("status") == "rejected":
                    labels["safe"] = False
        
        # Determine if useful for learning
        if labels["success"] and trace_data.get("evidence", []):
            labels["useful_for_learning"] = True
        
        labeled_trace["labels"] = labels
        
        # Add ground truth if provided
        if ground_truth is not None:
            labeled_trace["ground_truth"] = ground_truth
        
        return labeled_trace
    
    @staticmethod
    def create_negative_trace(
        original_trace: dict[str, Any],
        failure_reason: str,
        corrective_actions: list[str],
    ) -> dict[str, Any]:
        """Create a negative trace from a failed process."""
        
        negative_trace = original_trace.copy()
        
        # Override labels for negative example
        negative_trace["labels"] = {
            "success": False,
            "efficient": False,
            "safe": False,
            "useful_for_learning": True,  # Negative examples are useful for learning
        }
        
        # Add failure analysis
        negative_trace["failure_analysis"] = {
            "reason": failure_reason,
            "corrective_actions": corrective_actions,
            "created_at": datetime.utcnow().isoformat(),
        }
        
        # Mark as negative example
        negative_trace["example_type"] = "negative"
        
        return negative_trace


class ReplayLogWriter:
    """Write replay logs for artifact-based reconstruction."""
    
    def __init__(self, storage: StorageManager, log_dir: Path):
        self.storage = storage
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
    
    def write_replay_log(self, trace_data: dict[str, Any]) -> str:
        """Write a replay log file."""
        
        # Create replay log structure
        replay_log = {
            "metadata": {
                "trace_id": f"replay_{hashlib.sha256(json.dumps(trace_data).encode()).hexdigest()[:16]}",
                "created_at": datetime.utcnow().isoformat(),
                "schema_version": "v1",
            },
            "process_info": {
                "process_id": trace_data.get("process_id"),
                "start_time": trace_data.get("start_time").isoformat() if trace_data.get("start_time") else None,
                "end_time": trace_data.get("end_time").isoformat() if trace_data.get("end_time") else None,
                "duration_seconds": trace_data.get("duration_seconds"),
            },
            "artifacts": self._resolve_artifacts(trace_data),
            "evidence_chain": self._build_evidence_chain(trace_data),
            "claim_timeline": self._build_claim_timeline(trace_data),
            "decision_points": trace_data.get("decisions", []),
            "events": trace_data.get("events", []),
            "labels": trace_data.get("labels", {}),
        }
        
        # Write to file
        log_filename = f"{replay_log['metadata']['trace_id']}.json"
        log_path = self.log_dir / log_filename
        
        with open(log_path, 'w') as f:
            json.dump(replay_log, f, indent=2, default=str)
        
        return log_filename
    
    def _resolve_artifacts(self, trace_data: dict[str, Any]) -> dict[str, Any]:
        """Resolve artifact references for replay."""
        artifacts = {
            "evidence_refs": trace_data.get("evidence", []),
            "claim_refs": trace_data.get("claims", []),
        }
        
        # In a real implementation, we would retrieve artifact content
        # For v1, we just return references
        return artifacts
    
    def _build_evidence_chain(self, trace_data: dict[str, Any]) -> list[dict[str, Any]]:
        """Build evidence chain for replay."""
        evidence_chain = []
        
        for evidence_id in trace_data.get("evidence", []):
            evidence = self.storage.evidence_ledger.get_evidence(evidence_id)
            if evidence:
                evidence_chain.append({
                    "evidence_id": evidence.evidence_id,
                    "source_type": evidence.source_type.value,
                    "summary": evidence.summary,
                    "reliability": evidence.reliability,
                    "supported_claims": evidence.claim_supported,
                    "contradicted_claims": evidence.claim_contradicted,
                })
        
        return evidence_chain
    
    def _build_claim_timeline(self, trace_data: dict[str, Any]) -> list[dict[str, Any]]:
        """Build claim timeline for replay."""
        claim_timeline = []
        
        for claim_id in trace_data.get("claims", []):
            claim = self.storage.claim_registry.get_claim(claim_id)
            if claim:
                claim_timeline.append({
                    "claim_id": claim.claim_id,
                    "text": claim.text[:200] + "..." if len(claim.text) > 200 else claim.text,
                    "support_status": claim.support_status.value,
                    "confidence": claim.confidence,
                    "scope": claim.scope,
                    "evidence_refs": claim.evidence_refs,
                })
        
        return claim_timeline
    
    def read_replay_log(self, log_filename: str) -> Optional[dict[str, Any]]:
        """Read a replay log file."""
        log_path = self.log_dir / log_filename
        
        if not log_path.exists():
            return None
        
        with open(log_path, 'r') as f:
            return json.load(f)
    
    def validate_replay_log(self, log_data: dict[str, Any]) -> tuple[bool, list[str]]:
        """Validate a replay log for completeness."""
        errors = []
        
        # Check required sections
        required_sections = ["metadata", "process_info", "evidence_chain", "claim_timeline"]
        for section in required_sections:
            if section not in log_data:
                errors.append(f"Missing section: {section}")
        
        # Check metadata
        metadata = log_data.get("metadata", {})
        if "schema_version" not in metadata:
            errors.append("Missing schema_version in metadata")
        
        # Check evidence chain references
        evidence_chain = log_data.get("evidence_chain", [])
        for evidence in evidence_chain:
            if "evidence_id" not in evidence:
                errors.append("Evidence missing evidence_id")
        
        return len(errors) == 0, errors
