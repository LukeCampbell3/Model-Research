"""Storage and ledgers for the cognitive microkernel.

Step 2: Implement storage backends with SQLite for metadata and filesystem for artifacts.
"""

import json
import sqlite3
import hashlib
import shutil
from pathlib import Path
from typing import Any, Optional, Iterator
from contextlib import contextmanager

from .schemas import (
    ProcessDescriptor, ProcessNode, Artifact, CanonicalState,
    EvidenceRecord, Claim, BranchProcess, SpeculationLedgerEntry,
    Transaction, ReplayTrace, ExpertKnowledgeStore, LearnedPolicy,
)


class ArtifactStore:
    """Content-addressed artifact storage with filesystem backend."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    def store_artifact(self, content: bytes, artifact_type: str, created_by_process: str) -> Artifact:
        """Store content and return artifact reference."""
        content_hash = hashlib.sha256(content).hexdigest()
        
        # Create artifact directory structure
        artifact_dir = self.base_dir / content_hash[:2] / content_hash[2:4]
        artifact_dir.mkdir(parents=True, exist_ok=True)
        artifact_path = artifact_dir / content_hash
        
        # Write content if not exists
        if not artifact_path.exists():
            artifact_path.write_bytes(content)
        
        # Create artifact record
        artifact = Artifact(
            content_hash=content_hash,
            artifact_type=artifact_type,
            storage_uri=str(artifact_path.absolute()),
            created_by_process=created_by_process,
        )
        
        return artifact
    
    def retrieve_artifact(self, content_hash: str) -> Optional[bytes]:
        """Retrieve artifact content by hash."""
        artifact_path = self.base_dir / content_hash[:2] / content_hash[2:4] / content_hash
        if artifact_path.exists():
            return artifact_path.read_bytes()
        return None
    
    def get_artifact_uri(self, content_hash: str) -> Optional[str]:
        """Get artifact URI by hash."""
        artifact_path = self.base_dir / content_hash[:2] / content_hash[2:4] / content_hash
        if artifact_path.exists():
            return str(artifact_path.absolute())
        return None


class ProcessRegistry:
    """Process registry with SQLite backend."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize database schema."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS process_descriptors (
                    process_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_process_parent_state 
                ON process_descriptors(json_extract(data, '$.parent_state_hash'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_process_cache_key 
                ON process_descriptors(json_extract(data, '$.cache_key'))
            """)
            conn.commit()
    
    def register_process(self, process: ProcessDescriptor) -> None:
        """Register a process descriptor."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO process_descriptors 
                (process_id, data, created_at, updated_at) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    process.process_id,
                    process.model_dump_json(),
                    process.created_at.isoformat(),
                    process.updated_at.isoformat(),
                )
            )
            conn.commit()
    
    def get_process(self, process_id: str) -> Optional[ProcessDescriptor]:
        """Get a process descriptor by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM process_descriptors WHERE process_id = ?",
                (process_id,)
            )
            row = cursor.fetchone()
            if row:
                return ProcessDescriptor.model_validate_json(row[0])
        return None
    
    def get_processes_by_parent_state(self, parent_state_hash: str) -> list[ProcessDescriptor]:
        """Get all processes for a parent state hash."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                SELECT data FROM process_descriptors 
                WHERE json_extract(data, '$.parent_state_hash') = ?
                ORDER BY json_extract(data, '$.created_at') DESC
                """,
                (parent_state_hash,)
            )
            return [
                ProcessDescriptor.model_validate_json(row[0])
                for row in cursor.fetchall()
            ]
    
    def find_by_cache_key(self, cache_key: str) -> Optional[ProcessDescriptor]:
        """Find process by cache key (for reuse)."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                SELECT data FROM process_descriptors 
                WHERE json_extract(data, '$.cache_key') = ?
                AND json_extract(data, '$.status') = 'completed'
                ORDER BY json_extract(data, '$.created_at') DESC
                LIMIT 1
                """,
                (cache_key,)
            )
            row = cursor.fetchone()
            if row:
                return ProcessDescriptor.model_validate_json(row[0])
        return None


class ProcessDAG:
    """Process Directed Acyclic Graph for replay and audit."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize DAG database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS process_nodes (
                    process_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS process_edges (
                    parent_id TEXT NOT NULL,
                    child_id TEXT NOT NULL,
                    PRIMARY KEY (parent_id, child_id),
                    FOREIGN KEY (parent_id) REFERENCES process_nodes(process_id),
                    FOREIGN KEY (child_id) REFERENCES process_nodes(process_id)
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_state_before 
                ON process_nodes(json_extract(data, '$.state_hash_before'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_state_after 
                ON process_nodes(json_extract(data, '$.state_hash_after'))
            """)
            conn.commit()
    
    def add_node(self, node: ProcessNode) -> None:
        """Add a process node to the DAG."""
        with sqlite3.connect(self.db_path) as conn:
            # Insert node
            conn.execute(
                """
                INSERT OR REPLACE INTO process_nodes 
                (process_id, data, created_at, updated_at) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    node.process_id,
                    node.model_dump_json(),
                    node.start_time.isoformat() if node.start_time else "",
                    node.end_time.isoformat() if node.end_time else "",
                )
            )
            
            # Insert edges
            for parent_id in node.parent_process_ids:
                conn.execute(
                    """
                    INSERT OR IGNORE INTO process_edges (parent_id, child_id) 
                    VALUES (?, ?)
                    """,
                    (parent_id, node.process_id)
                )
            
            for child_id in node.child_process_ids:
                conn.execute(
                    """
                    INSERT OR IGNORE INTO process_edges (parent_id, child_id) 
                    VALUES (?, ?)
                    """,
                    (node.process_id, child_id)
                )
            
            conn.commit()
    
    def get_node(self, process_id: str) -> Optional[ProcessNode]:
        """Get a process node by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM process_nodes WHERE process_id = ?",
                (process_id,)
            )
            row = cursor.fetchone()
            if row:
                return ProcessNode.model_validate_json(row[0])
        return None
    
    def get_ancestors(self, process_id: str, depth: int = -1) -> list[ProcessNode]:
        """Get all ancestor nodes."""
        visited = set()
        ancestors = []
        
        def _collect(node_id: str, current_depth: int):
            if node_id in visited:
                return
            visited.add(node_id)
            
            node = self.get_node(node_id)
            if node:
                ancestors.append(node)
                
                if depth == -1 or current_depth < depth:
                    for parent_id in node.parent_process_ids:
                        _collect(parent_id, current_depth + 1)
        
        _collect(process_id, 0)
        return ancestors
    
    def get_descendants(self, process_id: str, depth: int = -1) -> list[ProcessNode]:
        """Get all descendant nodes."""
        visited = set()
        descendants = []
        
        def _collect(node_id: str, current_depth: int):
            if node_id in visited:
                return
            visited.add(node_id)
            
            node = self.get_node(node_id)
            if node:
                descendants.append(node)
                
                if depth == -1 or current_depth < depth:
                    # Get children from edges
                    with sqlite3.connect(self.db_path) as conn:
                        cursor = conn.execute(
                            "SELECT child_id FROM process_edges WHERE parent_id = ?",
                            (node_id,)
                        )
                        for (child_id,) in cursor.fetchall():
                            _collect(child_id, current_depth + 1)
        
        _collect(process_id, 0)
        return descendants
    
    def get_process_path(self, root_process_id: str) -> list[ProcessNode]:
        """Get the execution path from root to leaves."""
        # Simple BFS to get all nodes reachable from root
        visited = set()
        queue = [root_process_id]
        path = []
        
        while queue:
            current_id = queue.pop(0)
            if current_id in visited:
                continue
            visited.add(current_id)
            
            node = self.get_node(current_id)
            if node:
                path.append(node)
                
                # Get children
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.execute(
                        "SELECT child_id FROM process_edges WHERE parent_id = ?",
                        (current_id,)
                    )
                    for (child_id,) in cursor.fetchall():
                        if child_id not in visited:
                            queue.append(child_id)
        
        return path


class StateLedger:
    """State ledger for versioned state management."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize state ledger database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS canonical_states (
                    canonical_state_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS idx_root_state_hash 
                ON canonical_states(json_extract(data, '$.root_state_hash'))
            """)
            conn.commit()
    
    def register_state(self, state: CanonicalState) -> None:
        """Register a canonical state."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO canonical_states 
                (canonical_state_id, data, created_at, updated_at) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    state.canonical_state_id,
                    state.model_dump_json(),
                    state.created_at.isoformat(),
                    state.updated_at.isoformat(),
                )
            )
            conn.commit()
    
    def get_state_by_hash(self, root_state_hash: str) -> Optional[CanonicalState]:
        """Get canonical state by root hash."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                SELECT data FROM canonical_states 
                WHERE json_extract(data, '$.root_state_hash') = ?
                ORDER BY json_extract(data, '$.created_at') DESC
                LIMIT 1
                """,
                (root_state_hash,)
            )
            row = cursor.fetchone()
            if row:
                return CanonicalState.model_validate_json(row[0])
        return None
    
    def get_latest_state(self) -> Optional[CanonicalState]:
        """Get the most recent canonical state."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                SELECT data FROM canonical_states 
                ORDER BY json_extract(data, '$.created_at') DESC
                LIMIT 1
                """,
            )
            row = cursor.fetchone()
            if row:
                return CanonicalState.model_validate_json(row[0])
        return None


class EvidenceLedger:
    """Evidence ledger for traceable knowledge."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize evidence ledger database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS evidence_records (
                    evidence_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_evidence_state 
                ON evidence_records(json_extract(data, '$.state_hash'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_evidence_process 
                ON evidence_records(json_extract(data, '$.process_id'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_evidence_claim 
                ON evidence_records(
                    json_extract(data, '$.claim_supported'),
                    json_extract(data, '$.claim_contradicted')
                )
            """)
            conn.commit()
    
    def record_evidence(self, evidence: EvidenceRecord) -> None:
        """Record evidence."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO evidence_records 
                (evidence_id, data, created_at, updated_at) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    evidence.evidence_id,
                    evidence.model_dump_json(),
                    evidence.created_at.isoformat(),
                    evidence.created_at.isoformat(),  # updated_at same as created for immutable evidence
                )
            )
            conn.commit()
    
    def get_evidence(self, evidence_id: str) -> Optional[EvidenceRecord]:
        """Get evidence by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM evidence_records WHERE evidence_id = ?",
                (evidence_id,)
            )
            row = cursor.fetchone()
            if row:
                return EvidenceRecord.model_validate_json(row[0])
        return None
    
    def get_evidence_for_claim(self, claim_id: str) -> list[EvidenceRecord]:
        """Get all evidence supporting or contradicting a claim."""
        evidence_list = []
        
        with sqlite3.connect(self.db_path) as conn:
            # Evidence supporting the claim
            cursor = conn.execute(
                """
                SELECT data FROM evidence_records 
                WHERE json_array_contains(json_extract(data, '$.claim_supported'), ?)
                """,
                (claim_id,)
            )
            for (data,) in cursor.fetchall():
                evidence_list.append(EvidenceRecord.model_validate_json(data))
            
            # Evidence contradicting the claim
            cursor = conn.execute(
                """
                SELECT data FROM evidence_records 
                WHERE json_array_contains(json_extract(data, '$.claim_contradicted'), ?)
                """,
                (claim_id,)
            )
            for (data,) in cursor.fetchall():
                evidence_list.append(EvidenceRecord.model_validate_json(data))
        
        return evidence_list


class ClaimRegistry:
    """Claim registry with evidence linkage."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize claim registry database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS claims (
                    claim_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_claim_status 
                ON claims(json_extract(data, '$.support_status'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_claim_scope 
                ON claims(json_extract(data, '$.scope'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_claim_evidence 
                ON claims(
                    json_extract(data, '$.evidence_refs'),
                    json_extract(data, '$.contradiction_refs')
                )
            """)
            conn.commit()
    
    def register_claim(self, claim: Claim) -> None:
        """Register a claim."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO claims 
                (claim_id, data, created_at, updated_at) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    claim.claim_id,
                    claim.model_dump_json(),
                    claim.freshness,  # Use freshness as timestamp proxy
                    claim.freshness,
                )
            )
            conn.commit()
    
    def get_claim(self, claim_id: str) -> Optional[Claim]:
        """Get claim by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM claims WHERE claim_id = ?",
                (claim_id,)
            )
            row = cursor.fetchone()
            if row:
                return Claim.model_validate_json(row[0])
        return None
    
    def get_claims_by_evidence(self, evidence_id: str) -> list[Claim]:
        """Get all claims related to evidence."""
        claims = []
        
        with sqlite3.connect(self.db_path) as conn:
            # Claims supported by evidence
            cursor = conn.execute(
                """
                SELECT data FROM claims 
                WHERE json_array_contains(json_extract(data, '$.evidence_refs'), ?)
                """,
                (evidence_id,)
            )
            for (data,) in cursor.fetchall():
                claims.append(Claim.model_validate_json(data))
            
            # Claims contradicted by evidence
            cursor = conn.execute(
                """
                SELECT data FROM claims 
                WHERE json_array_contains(json_extract(data, '$.contradiction_refs'), ?)
                """,
                (evidence_id,)
            )
            for (data,) in cursor.fetchall():
                claims.append(Claim.model_validate_json(data))
        
        return claims


class SpeculationLedger:
    """Speculation ledger for dormant possibilities."""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize speculation ledger."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS speculations (
                    speculation_id TEXT PRIMARY KEY,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    last_reviewed TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_speculation_status 
                ON speculations(json_extract(data, '$.status'))
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_speculation_parent 
                ON speculations(json_extract(data, '$.parent_state_hash'))
            """)
            conn.commit()
    
    def record_speculation(self, speculation: SpeculationLedgerEntry) -> None:
        """Record a speculation."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO speculations 
                (speculation_id, data, created_at, last_reviewed) 
                VALUES (?, ?, ?, ?)
                """,
                (
                    speculation.speculation_id,
                    speculation.model_dump_json(),
                    speculation.last_reviewed_step.isoformat() if speculation.last_reviewed_step else "",
                    speculation.last_reviewed_step.isoformat() if speculation.last_reviewed_step else None,
                )
            )
            conn.commit()
    
    def get_speculation(self, speculation_id: str) -> Optional[SpeculationLedgerEntry]:
        """Get speculation by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT data FROM speculations WHERE speculation_id = ?",
                (speculation_id,)
            )
            row = cursor.fetchone()
            if row:
                return SpeculationLedgerEntry.model_validate_json(row[0])
        return None


class StorageManager:
    """Unified storage manager for the microkernel."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize all storage components
        self.artifact_store = ArtifactStore(base_dir / "artifacts")
        self.process_registry = ProcessRegistry(base_dir / "processes.db")
        self.process_dag = ProcessDAG(base_dir / "dag.db")
        self.state_ledger = StateLedger(base_dir / "states.db")
        self.evidence_ledger = EvidenceLedger(base_dir / "evidence.db")
        self.claim_registry = ClaimRegistry(base_dir / "claims.db")
        self.speculation_ledger = SpeculationLedger(base_dir / "speculations.db")
    
    def clear(self) -> None:
        """Clear all storage (for testing)."""
        if self.base_dir.exists():
            shutil.rmtree(self.base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Reinitialize
        self.__init__(self.base_dir)
