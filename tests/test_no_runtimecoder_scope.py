from pathlib import Path


FORBIDDEN_TERMS = [
    "RuntimeCoder",
    "BranchTicket",
    "TaskPacket",
    "ContextPacket",
    "BranchIR",
    "run_runtime_native_eval.py",
    "run_branch_ticket_eval.py",
    "run_verifier_repair_eval.py",
]


def test_no_runtimecoder_or_runtime_workflow_scope_in_benchmark():
    paths = [p for p in Path("benchmark").rglob("*") if p.is_file()]
    names = {p.name for p in paths}
    assert "run_runtime_native_eval.py" not in names
    assert "run_branch_ticket_eval.py" not in names
    assert "run_verifier_repair_eval.py" not in names
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in FORBIDDEN_TERMS[:5]:
            assert term not in text
