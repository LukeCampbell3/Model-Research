"""Evaluate BranchTicket validity across a set of tickets."""

from typing import List, Dict, Any

from runtime_coder.schemas.branch_ticket import BranchTicket


def validate_branch_tickets(tickets: List[BranchTicket]) -> Dict[str, Any]:
    """Validate a list of BranchTickets and return summary metrics.

    Returns:
        Dict with keys: total, valid, invalid, error_details
    """
    results = {
        "total": len(tickets),
        "valid": 0,
        "invalid": 0,
        "error_details": [],
    }

    for ticket in tickets:
        errors = ticket.validate()
        if not errors:
            results["valid"] += 1
        else:
            results["invalid"] += 1
            results["error_details"].append({
                "ticket_id": ticket.ticket_id,
                "errors": errors,
            })

    results["validity_rate"] = results["valid"] / max(results["total"], 1)
    return results
