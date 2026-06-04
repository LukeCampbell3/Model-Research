"""Process scheduler for v1.

Step 6: Implement priority scheduling, budget management, and timing collection.
"""

import heapq
import time
from typing import Optional, Any
from datetime import datetime, timedelta
from enum import Enum

from .schemas import (
    ProcessDescriptor, ProcessStatus, SideEffectPolicy,
)


class QueueType(str, Enum):
    """Queue types for scheduling."""
    INTERRUPT = "interrupt_queue"
    COMMIT_VERIFICATION = "commit_verification_queue"
    NORMAL_PROCESS = "normal_process_queue"
    SPECULATIVE_PROCESS = "speculative_process_queue"
    OFFLINE_TRACE = "offline_trace_queue"


class ProcessQueueManager:
    """Manage process queues with priority scheduling."""
    
    def __init__(self):
        # Priority queues: (-priority, insertion_order, process)
        self.queues = {
            QueueType.INTERRUPT: [],
            QueueType.COMMIT_VERIFICATION: [],
            QueueType.NORMAL_PROCESS: [],
            QueueType.SPECULATIVE_PROCESS: [],
            QueueType.OFFLINE_TRACE: [],
        }
        self.insertion_counter = 0
        self.process_registry = {}  # process_id -> ProcessDescriptor
    
    def enqueue(self, process: ProcessDescriptor, queue_type: QueueType) -> None:
        """Enqueue a process with priority."""
        # Calculate priority score
        priority_score = self._calculate_priority(process, queue_type)
        
        # Use negative priority for min-heap (higher priority = more negative)
        heap_entry = (-priority_score, self.insertion_counter, process.process_id)
        
        self.queues[queue_type].append(heap_entry)
        heapq.heapify(self.queues[queue_type])
        
        self.process_registry[process.process_id] = process
        self.insertion_counter += 1
    
    def dequeue(self, queue_type: QueueType) -> Optional[ProcessDescriptor]:
        """Dequeue highest priority process from queue."""
        if not self.queues[queue_type]:
            return None
        
        _, _, process_id = heapq.heappop(self.queues[queue_type])
        process = self.process_registry.pop(process_id, None)
        
        return process
    
    def peek(self, queue_type: QueueType) -> Optional[ProcessDescriptor]:
        """Peek at highest priority process without removing."""
        if not self.queues[queue_type]:
            return None
        
        _, _, process_id = self.queues[queue_type][0][2]  # Third element is process_id
        return self.process_registry.get(process_id)
    
    def remove(self, process_id: str) -> bool:
        """Remove a process from all queues."""
        removed = False
        
        for queue_type in self.queues:
            # Find and remove from this queue
            new_queue = []
            for entry in self.queues[queue_type]:
                if entry[2] != process_id:  # process_id is third element
                    new_queue.append(entry)
                else:
                    removed = True
            
            if len(new_queue) != len(self.queues[queue_type]):
                self.queues[queue_type] = new_queue
                heapq.heapify(self.queues[queue_type])
        
        # Remove from registry
        if process_id in self.process_registry:
            del self.process_registry[process_id]
            removed = True
        
        return removed
    
    def _calculate_priority(self, process: ProcessDescriptor, queue_type: QueueType) -> float:
        """Calculate priority score for a process."""
        base_priority = process.priority
        
        # Queue type modifiers
        if queue_type == QueueType.INTERRUPT:
            base_priority += 2.0
        elif queue_type == QueueType.COMMIT_VERIFICATION:
            base_priority += 1.5
        elif queue_type == QueueType.NORMAL_PROCESS:
            base_priority += 0.5
        
        # Side-effect policy modifiers
        if process.side_effect_policy == SideEffectPolicy.READ_ONLY:
            base_priority += 0.2  # Read-only can run more aggressively
        
        # Age bonus (prevent starvation)
        age_hours = (datetime.utcnow() - process.created_at).total_seconds() / 3600
        age_bonus = min(0.5, age_hours * 0.1)  # Max 0.5 bonus after 5 hours
        base_priority += age_bonus
        
        # Budget remaining bonus
        budget_bonus = process.budget_remaining * 0.3
        base_priority += budget_bonus
        
        return max(0.0, min(1.0, base_priority))
    
    def get_queue_stats(self) -> dict[str, Any]:
        """Get queue statistics."""
        stats = {}
        for queue_type, queue in self.queues.items():
            stats[queue_type.value] = {
                "size": len(queue),
                "top_priority": None,
            }
            if queue:
                top_priority = -queue[0][0]  # Negative of heap priority
                stats[queue_type.value]["top_priority"] = top_priority
        
        return stats


class PriorityScheduler:
    """Main scheduler that selects processes from queues."""
    
    def __init__(self, queue_manager: ProcessQueueManager):
        self.queue_manager = queue_manager
        self.current_process = None
        self.scheduling_history = []
    
    def select_next_process(self) -> Optional[ProcessDescriptor]:
        """Select next process to execute based on priority."""
        
        # Check queues in priority order
        for queue_type in [
            QueueType.INTERRUPT,
            QueueType.COMMIT_VERIFICATION,
            QueueType.NORMAL_PROCESS,
            QueueType.SPECULATIVE_PROCESS,
            QueueType.OFFLINE_TRACE,
        ]:
            process = self.queue_manager.dequeue(queue_type)
            if process:
                self.current_process = process
                
                # Record scheduling decision
                self.scheduling_history.append({
                    "timestamp": datetime.utcnow(),
                    "process_id": process.process_id,
                    "queue_type": queue_type,
                    "priority": process.priority,
                })
                
                return process
        
        self.current_process = None
        return None
    
    def cancel_low_priority_speculative(self, pressure_level: float = 0.8) -> int:
        """Cancel low priority speculative processes under pressure.
        
        Args:
            pressure_level: 0-1 where 1 is maximum pressure
            
        Returns:
            Number of processes cancelled
        """
        cancelled = 0
        
        # Get all speculative processes
        speculative_queue = self.queue_manager.queues[QueueType.SPECULATIVE_PROCESS]
        
        # Sort by priority (ascending since heap stores negative priority)
        sorted_processes = sorted(speculative_queue, key=lambda x: x[0])  # x[0] is negative priority
        
        # Cancel lowest priority processes
        cancel_threshold = max(1, int(len(sorted_processes) * pressure_level))
        
        for i in range(min(cancel_threshold, len(sorted_processes))):
            _, _, process_id = sorted_processes[i]
            if self.queue_manager.remove(process_id):
                cancelled += 1
        
        return cancelled
    
    def refresh_stale_processes(self, max_age_minutes: int = 30) -> int:
        """Refresh or cancel stale processes.
        
        Returns:
            Number of processes refreshed/cancelled
        """
        refreshed = 0
        now = datetime.utcnow()
        
        for process_id, process in list(self.queue_manager.process_registry.items()):
            age_minutes = (now - process.created_at).total_seconds() / 60
            
            if age_minutes > max_age_minutes:
                # Check if process is stale (parent state changed)
                # In a real implementation, we would check current state hash
                # For v1, we simulate by cancelling old processes
                if self.queue_manager.remove(process_id):
                    refreshed += 1
        
        return refreshed


class BudgetManager:
    """Manage process budgets and cost accounting."""
    
    def __init__(self):
        self.process_budgets = {}  # process_id -> remaining_budget
        self.total_costs = {}
    
    def allocate_budget(self, process: ProcessDescriptor) -> bool:
        """Allocate budget for a process."""
        if process.budget_remaining <= 0:
            return False
        
        self.process_budgets[process.process_id] = process.budget_remaining
        self.total_costs[process.process_id] = 0.0
        return True
    
    def consume_budget(self, process_id: str, cost: float) -> bool:
        """Consume budget for a process."""
        if process_id not in self.process_budgets:
            return False
        
        remaining = self.process_budgets[process_id]
        if cost > remaining:
            return False
        
        self.process_budgets[process_id] = remaining - cost
        self.total_costs[process_id] += cost
        return True
    
    def get_remaining_budget(self, process_id: str) -> float:
        """Get remaining budget for a process."""
        return self.process_budgets.get(process_id, 0.0)
    
    def get_total_cost(self, process_id: str) -> float:
        """Get total cost consumed by a process."""
        return self.total_costs.get(process_id, 0.0)
    
    def revoke_budget(self, process_id: str) -> float:
        """Revoke remaining budget and return amount."""
        remaining = self.process_budgets.pop(process_id, 0.0)
        self.total_costs.pop(process_id, None)
        return remaining
    
    def get_budget_stats(self) -> dict[str, Any]:
        """Get budget statistics."""
        total_allocated = sum(self.process_budgets.values())
        total_consumed = sum(self.total_costs.values())
        
        return {
            "active_processes": len(self.process_budgets),
            "total_allocated": total_allocated,
            "total_consumed": total_consumed,
            "budget_utilization": total_consumed / (total_consumed + total_allocated + 1e-8),
        }


class TimingCollector:
    """Collect timing metrics for processes."""
    
    def __init__(self):
        self.process_timings = {}  # process_id -> timing_data
        self.queue_timings = {}  # queue_type -> timing_data
    
    def record_process_start(self, process_id: str, queue_type: QueueType) -> None:
        """Record when a process starts execution."""
        self.process_timings[process_id] = {
            "start_time": time.time(),
            "queue_type": queue_type,
            "end_time": None,
            "duration": None,
        }
    
    def record_process_end(self, process_id: str) -> Optional[float]:
        """Record when a process ends execution and return duration."""
        if process_id not in self.process_timings:
            return None
        
        end_time = time.time()
        timing_data = self.process_timings[process_id]
        timing_data["end_time"] = end_time
        timing_data["duration"] = end_time - timing_data["start_time"]
        
        # Also record queue timing
        queue_type = timing_data["queue_type"]
        if queue_type not in self.queue_timings:
            self.queue_timings[queue_type] = []
        self.queue_timings[queue_type].append(timing_data["duration"])
        
        return timing_data["duration"]
    
    def get_process_timing(self, process_id: str) -> Optional[dict[str, Any]]:
        """Get timing data for a process."""
        return self.process_timings.get(process_id)
    
    def get_queue_timing_stats(self) -> dict[str, Any]:
        """Get timing statistics by queue."""
        stats = {}
        
        for queue_type, durations in self.queue_timings.items():
            if durations:
                stats[queue_type.value] = {
                    "count": len(durations),
                    "avg_duration": sum(durations) / len(durations),
                    "min_duration": min(durations),
                    "max_duration": max(durations),
                    "p95_duration": sorted(durations)[int(len(durations) * 0.95)] if len(durations) >= 20 else None,
                }
        
        return stats


class RuntimeProfiler:
    """Collect runtime metrics for monitoring."""
    
    def __init__(self):
        self.metrics = {
            "processes_created": 0,
            "processes_completed": 0,
            "processes_cancelled": 0,
            "cache_hit_rate": 0.0,
            "context_tokens_used": 0,
            "strong_model_calls": 0,
            "branch_seeds_generated": 0,
            "branches_expanded": 0,
            "branches_committed": 0,
            "branches_archived": 0,
            "speculations_retained": 0,
            "rollback_count": 0,
            "verified_commit_rate": 0.0,
            "verifier_rejection_rate": 0.0,
            "unsupported_claim_count": 0,
            "contradicted_claim_count": 0,
            "memory_write_attempts": 0,
            "memory_write_rejections": 0,
            "stale_process_cancellations": 0,
            "state_hash_conflict_count": 0,
            "evidence_records_created": 0,
            "claims_with_evidence_ratio": 0.0,
            "replay_success_rate": 0.0,
        }
        self.start_time = time.time()
    
    def increment(self, metric: str, amount: int = 1) -> None:
        """Increment a metric."""
        if metric in self.metrics:
            if isinstance(self.metrics[metric], (int, float)):
                self.metrics[metric] += amount
    
    def set(self, metric: str, value: float) -> None:
        """Set a metric value."""
        if metric in self.metrics:
            self.metrics[metric] = value
    
    def record_cache_hit(self, hit: bool) -> None:
        """Record a cache hit or miss."""
        self.metrics["cache_hit_rate"] = (
            (self.metrics["cache_hit_rate"] * self.metrics["processes_completed"] + (1 if hit else 0))
            / (self.metrics["processes_completed"] + 1 + 1e-8)
        )
    
    def record_claim_support(self, has_evidence: bool) -> None:
        """Record whether a claim has evidence."""
        total_claims = self.metrics["claims_with_evidence_ratio"] * self.metrics.get("total_claims_tracked", 0)
        if has_evidence:
            total_claims += 1
        self.metrics["claims_with_evidence_ratio"] = total_claims / (self.metrics.get("total_claims_tracked", 0) + 1 + 1e-8)
        self.metrics["total_claims_tracked"] = self.metrics.get("total_claims_tracked", 0) + 1
    
    def get_metrics(self) -> dict[str, Any]:
        """Get all metrics with runtime duration."""
        runtime_seconds = time.time() - self.start_time
        
        metrics = self.metrics.copy()
        metrics["runtime_seconds"] = runtime_seconds
        metrics["processes_per_second"] = self.metrics["processes_completed"] / max(runtime_seconds, 1)
        
        return metrics
    
    def get_efficiency_metrics(self) -> dict[str, float]:
        """Get efficiency-focused metrics."""
        return {
            "cache_hit_rate": self.metrics["cache_hit_rate"],
            "verified_commit_rate": self.metrics["verified_commit_rate"],
            "claims_with_evidence_ratio": self.metrics["claims_with_evidence_ratio"],
            "processes_per_second": self.metrics.get("processes_completed", 0) / max(time.time() - self.start_time, 1),
        }
    
    def get_safety_metrics(self) -> dict[str, float]:
        """Get safety-focused metrics."""
        return {
            "verifier_rejection_rate": self.metrics["verifier_rejection_rate"],
            "unsupported_claim_promotion_rate": self.metrics.get("unsupported_claim_count", 0) / max(self.metrics.get("total_claims_tracked", 1), 1),
            "memory_write_rejection_rate": self.metrics["memory_write_rejections"] / max(self.metrics["memory_write_attempts"], 1),
            "rollback_rate": self.metrics["rollback_count"] / max(self.metrics["branches_committed"], 1),
        }
