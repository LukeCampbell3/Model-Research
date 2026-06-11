"""Runtime compliance metrics for evaluating model outputs."""

from typing import Dict, Any, List

from runtime_coder.schemas.branch_ticket import BranchTicket, ALLOWED_BRANCH_TYPES, ALLOWED_PRIVILEGE_LEVELS
from runtime_coder.schemas.verifier_result import VerifierResult


def compute_runtime_compliance(
    tickets: List[BranchTicket],
    verifier_results: List[VerifierResult],
) -> Dict[str, Any]:
    """Compute runtime compliance metrics.

    Checks:
    - Branch type compliance: all branch_types in allowed set
    - Privilege compliance: all privilege_levels in allowed set
    - Verifier pass rate: fraction of verifier results that passed
    - Write-set coverage: fraction of tickets with non-empty write_set
    - Evidence linkage: fraction of verifier results with evidence_refs
    """
    metrics = {}

    # Branch type compliance
    valid_types = sum(1 for t in tickets if t.branch_type in ALLOWED_BRANCH_TYPES)
    metrics["branch_type_compliance"] = valid_types / max(len(tickets), 1)

    # Privilege compliance
    valid_privs = sum(1 for t in tickets if t.privilege_level in ALLOWED_PRIVILEGE_LEVELS)
    metrics["privilege_compliance"] = valid_privs / max(len(tickets), 1)

    # Verifier pass rate
    passed = sum(1 for v in verifier_results if v.passed)
    metrics["verifier_pass_rate"] = passed / max(len(verifier_results), 1)

    # Write-set coverage
    has_write = sum(1 for t in tickets if t.write_set)
    metrics["write_set_coverage"] = has_write / max(len(tickets), 1)

    # Evidence linkage
    has_evidence = sum(1 for v in verifier_results if v.evidence_refs)
    metrics["evidence_linkage"] = has_evidence / max(len(verifier_results), 1)

    # Overall compliance score (average of all metrics)
    metrics["overall_compliance"] = sum(metrics.values()) / len(metrics)

    return metrics
