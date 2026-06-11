"""Tests for the Python task bank."""

import pytest

from runtime_coder.data_pipeline.python_task_bank import (
    get_all_task_templates,
    get_task_types,
    get_templates_by_type,
    TASK_TYPES,
)
from runtime_coder.schema.canonical_schema_loader import compute_schema_hash


class TestPythonTaskBank:
    """Tests for task bank completeness and validity."""

    def test_has_50_plus_tasks(self):
        """Task bank has at least 50 task templates."""
        templates = get_all_task_templates()
        assert len(templates) >= 50, f"Only {len(templates)} templates"

    def test_all_task_types_covered(self):
        """All declared task types have at least one template."""
        templates = get_all_task_templates()
        found_types = {t["task"]["task_type"] for t in templates}
        for tt in TASK_TYPES:
            assert tt in found_types, f"Task type '{tt}' has no templates"

    def test_all_templates_have_required_structure(self):
        """Every template has task, context, and ticket dicts."""
        for template in get_all_task_templates():
            assert "task" in template
            assert "context" in template
            assert "ticket" in template

    def test_all_tickets_have_schema_hash(self):
        """Every ticket includes schema_hash."""
        expected_hash = compute_schema_hash()
        for template in get_all_task_templates():
            ticket = template["ticket"]
            assert "schema_hash" in ticket
            assert ticket["schema_hash"] == expected_hash

    def test_all_tickets_have_runtime_contract_version(self):
        """Every ticket includes runtime_contract_version."""
        for template in get_all_task_templates():
            ticket = template["ticket"]
            assert "runtime_contract_version" in ticket
            assert ticket["runtime_contract_version"] == "1.0"

    def test_all_tickets_have_target_kind(self):
        """Every ticket includes target_kind=python."""
        for template in get_all_task_templates():
            ticket = template["ticket"]
            assert "target_kind" in ticket
            assert ticket["target_kind"] == "python"

    def test_all_contexts_are_python(self):
        """All context packets have language=python."""
        for template in get_all_task_templates():
            ctx = template["context"]
            assert ctx["language"] == "python"

    def test_task_ids_are_unique(self):
        """All task IDs are unique across the bank."""
        templates = get_all_task_templates()
        ids = [t["task"]["task_id"] for t in templates]
        assert len(ids) == len(set(ids)), "Duplicate task IDs found"

    def test_get_templates_by_type(self):
        """Filtering by type returns correct subset."""
        bug_fixes = get_templates_by_type("bug_fix")
        assert len(bug_fixes) > 0
        for t in bug_fixes:
            assert t["task"]["task_type"] == "bug_fix"

    def test_tickets_have_read_set(self):
        """All tickets have non-empty read_set (except exploration)."""
        for template in get_all_task_templates():
            ticket = template["ticket"]
            task_type = template["task"]["task_type"]
            if task_type != "exploration":
                assert ticket["read_set"], f"Empty read_set for {ticket['ticket_id']}"
