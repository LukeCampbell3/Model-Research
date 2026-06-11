"""All special tokens for the RuntimeCoder protocol (~70 tokens)."""

# Task tokens
TASK_TOKENS = [
    "<|task_start|>",
    "<|task_end|>",
    "<|task_id|>",
    "<|task_type|>",
    "<|task_priority|>",
    "<|task_constraints|>",
]

# Context tokens
CONTEXT_TOKENS = [
    "<|context_start|>",
    "<|context_end|>",
    "<|context_file|>",
    "<|context_symbol|>",
    "<|context_snippet|>",
    "<|context_deps|>",
    "<|context_language|>",
]

# Branch tokens
BRANCH_TOKENS = [
    "<|branch_start|>",
    "<|branch_end|>",
    "<|branch_ticket|>",
    "<|branch_type|>",
    "<|branch_privilege|>",
    "<|branch_read_set|>",
    "<|branch_write_set|>",
    "<|branch_ir|>",
    "<|branch_step|>",
    "<|branch_merge|>",
]

# Patch tokens
PATCH_TOKENS = [
    "<|patch_start|>",
    "<|patch_end|>",
    "<|patch_hunk|>",
    "<|patch_add|>",
    "<|patch_del|>",
    "<|patch_context|>",
    "<|patch_file|>",
]

# Evidence tokens
EVIDENCE_TOKENS = [
    "<|evidence_start|>",
    "<|evidence_end|>",
    "<|evidence_type|>",
    "<|evidence_confidence|>",
    "<|evidence_data|>",
    "<|evidence_claim|>",
]

# Verifier tokens
VERIFIER_TOKENS = [
    "<|verifier_start|>",
    "<|verifier_end|>",
    "<|verifier_pass|>",
    "<|verifier_fail|>",
    "<|verifier_score|>",
    "<|verifier_error|>",
    "<|verifier_target|>",
]

# Replay tokens
REPLAY_TOKENS = [
    "<|replay_start|>",
    "<|replay_end|>",
    "<|replay_step|>",
    "<|replay_input|>",
    "<|replay_output|>",
    "<|replay_checkpoint|>",
]

# Commit tokens
COMMIT_TOKENS = [
    "<|commit_start|>",
    "<|commit_end|>",
    "<|commit_accept|>",
    "<|commit_reject|>",
    "<|commit_rollback|>",
    "<|commit_files|>",
]

# FIM (Fill-in-the-Middle) tokens
FIM_TOKENS = [
    "<|fim_prefix|>",
    "<|fim_middle|>",
    "<|fim_suffix|>",
    "<|fim_pad|>",
]

# Mode tokens
MODE_TOKENS = [
    "<|mode_generate|>",
    "<|mode_verify|>",
    "<|mode_refactor|>",
    "<|mode_explain|>",
    "<|mode_test|>",
]

# Descriptor tokens
DESCRIPTOR_TOKENS = [
    "<|desc_function|>",
    "<|desc_class|>",
    "<|desc_module|>",
    "<|desc_variable|>",
    "<|desc_type|>",
]

# Operator tokens
OPERATOR_TOKENS = [
    "<|op_compose|>",
    "<|op_sequence|>",
    "<|op_parallel|>",
    "<|op_conditional|>",
    "<|op_loop|>",
    "<|op_terminate|>",
]

# File boundary tokens (for multi-file context)
FILE_BOUNDARY_TOKENS = [
    "<|file_sep|>",
    "<|path|>",
    "<|file_start|>",
]

# Collect all categories
SPECIAL_TOKEN_CATEGORIES = {
    "task": TASK_TOKENS,
    "context": CONTEXT_TOKENS,
    "branch": BRANCH_TOKENS,
    "patch": PATCH_TOKENS,
    "evidence": EVIDENCE_TOKENS,
    "verifier": VERIFIER_TOKENS,
    "replay": REPLAY_TOKENS,
    "commit": COMMIT_TOKENS,
    "fim": FIM_TOKENS,
    "mode": MODE_TOKENS,
    "descriptor": DESCRIPTOR_TOKENS,
    "operator": OPERATOR_TOKENS,
    "file_boundary": FILE_BOUNDARY_TOKENS,
}


def get_all_special_tokens() -> list:
    """Return flat list of all special tokens."""
    tokens = []
    for category_tokens in SPECIAL_TOKEN_CATEGORIES.values():
        tokens.extend(category_tokens)
    return tokens


# Flat list for convenience
SPECIAL_TOKENS = get_all_special_tokens()

# Base offset for special token IDs
SPECIAL_TOKEN_ID_OFFSET = 50000
