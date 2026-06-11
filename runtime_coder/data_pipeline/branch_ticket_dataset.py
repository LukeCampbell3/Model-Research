"""BranchTicket SFT dataset generation for Phase 2.

Generates diverse BranchTicket training examples from TaskPacket+ContextPacket inputs.
Covers all branch_types, privilege_levels, and task categories.
Includes invalid examples for rejection training.
"""

import dataclasses
import json
import random
from typing import List, Optional, Tuple

from runtime_coder.schemas.branch_ticket import (
    ALLOWED_BRANCH_TYPES,
    ALLOWED_PRIVILEGE_LEVELS,
    BranchTicket,
)
from runtime_coder.schemas.context_packet import ContextPacket
from runtime_coder.schemas.task_packet import TaskPacket
from runtime_coder.tokenizer.runtime_special_tokens import (
    BRANCH_TOKENS,
    CONTEXT_TOKENS,
    TASK_TOKENS,
)


# Task categories with associated templates
TASK_CATEGORIES = {
    "bug_fix": {
        "descriptions": [
            "Fix null pointer exception in user authentication",
            "Resolve race condition in cache invalidation",
            "Fix off-by-one error in pagination logic",
            "Patch memory leak in event listener cleanup",
            "Fix incorrect timezone conversion in scheduler",
        ],
        "constraints": [
            ["must not break existing tests", "single file change preferred"],
            ["regression test required", "preserve backward compatibility"],
            ["minimal diff", "add test for the specific bug"],
        ],
    },
    "test_generation": {
        "descriptions": [
            "Generate unit tests for the payment processing module",
            "Add integration tests for REST API endpoints",
            "Write property-based tests for data serialization",
            "Create edge-case tests for input validation",
            "Generate test coverage for error handling paths",
        ],
        "constraints": [
            ["achieve 80% coverage", "use existing test framework"],
            ["include negative test cases", "mock external dependencies"],
            ["test edge cases", "follow AAA pattern"],
        ],
    },
    "refactor": {
        "descriptions": [
            "Extract common validation logic into shared utility",
            "Refactor monolithic handler into strategy pattern",
            "Decompose large class into smaller focused modules",
            "Convert callback-based code to async/await",
            "Replace manual type checking with TypeGuard pattern",
        ],
        "constraints": [
            ["behavior must be identical", "no new dependencies"],
            ["all tests must pass", "improve readability"],
            ["reduce cyclomatic complexity", "maintain public API"],
        ],
    },
    "api_migration": {
        "descriptions": [
            "Migrate from REST v1 to v2 endpoint format",
            "Update deprecated library calls to new API",
            "Convert synchronous API to async interface",
            "Migrate database queries from raw SQL to ORM",
            "Update authentication from session to JWT tokens",
        ],
        "constraints": [
            ["backward compatible", "add deprecation warnings"],
            ["update all callers", "migration guide needed"],
            ["dual-mode support during transition", "version header required"],
        ],
    },
    "type_fix": {
        "descriptions": [
            "Add type annotations to the data processing pipeline",
            "Fix type errors flagged by mypy strict mode",
            "Convert Any types to proper generics",
            "Add overload signatures for polymorphic functions",
            "Fix variance errors in generic container types",
        ],
        "constraints": [
            ["no runtime behavior change", "pass mypy strict"],
            ["use Protocol for structural typing", "avoid cast()"],
            ["preserve existing type: ignore comments with reason", "add missing return types"],
        ],
    },
    "performance_patch": {
        "descriptions": [
            "Optimize hot loop with vectorized operations",
            "Add caching layer for repeated database queries",
            "Reduce memory allocation in data pipeline",
            "Optimize serialization path for large payloads",
            "Fix N+1 query issue in relationship loading",
        ],
        "constraints": [
            ["must show measurable improvement", "add benchmark"],
            ["no correctness regression", "memory budget unchanged"],
            ["latency target: 50ms p99", "document tradeoffs"],
        ],
    },
    "config_fix": {
        "descriptions": [
            "Fix incorrect environment variable loading order",
            "Update CI configuration for new build targets",
            "Correct Docker compose port mapping conflict",
            "Fix CORS configuration for production origins",
            "Update dependency versions for security patches",
        ],
        "constraints": [
            ["validate in staging first", "no downtime"],
            ["backward compatible with existing deploys", "add validation"],
            ["document the change", "add config schema validation"],
        ],
    },
}

# Context templates by language
CONTEXT_TEMPLATES = {
    "python": [
        ("src/auth/handler.py", "def authenticate(request):\n    token = request.headers.get('Authorization')\n    if not token:\n        raise UnauthorizedError()\n    return validate_token(token)\n"),
        ("src/data/processor.py", "class DataProcessor:\n    def __init__(self, config):\n        self.config = config\n        self._cache = {}\n\n    def process(self, data):\n        return self._transform(data)\n"),
        ("src/api/routes.py", "from flask import Blueprint\n\napi = Blueprint('api', __name__)\n\n@api.route('/users', methods=['GET'])\ndef list_users():\n    return jsonify(get_all_users())\n"),
        ("tests/test_handler.py", "import pytest\n\ndef test_authenticate_valid_token():\n    request = MockRequest(headers={'Authorization': 'Bearer valid'})\n    result = authenticate(request)\n    assert result.is_valid\n"),
        ("src/utils/cache.py", "from functools import lru_cache\nfrom typing import Dict, Any\n\ndef cached_lookup(key: str) -> Any:\n    return _backend.get(key)\n"),
    ],
    "typescript": [
        ("src/services/auth.ts", "export class AuthService {\n  async validateToken(token: string): Promise<User> {\n    const decoded = jwt.verify(token, this.secret);\n    return this.userRepo.findById(decoded.sub);\n  }\n}\n"),
        ("src/api/middleware.ts", "export function rateLimiter(limit: number) {\n  const counter = new Map<string, number>();\n  return (req: Request, res: Response, next: NextFunction) => {\n    // implementation\n  };\n}\n"),
        ("src/models/user.ts", "export interface User {\n  id: string;\n  email: string;\n  role: 'admin' | 'user' | 'guest';\n  createdAt: Date;\n}\n"),
    ],
}


@dataclasses.dataclass
class BranchTicketSFTExample:
    """A single SFT training example for BranchTicket generation."""

    task_packet: TaskPacket
    context_packet: ContextPacket
    target_branch_ticket: BranchTicket
    task_type: str  # One of TASK_CATEGORIES keys
    difficulty: str  # "easy", "medium", "hard"
    is_valid: bool = True  # False for rejection training examples
    invalid_reason: str = ""  # Why it's invalid (for rejection examples)

    def format_input(self) -> str:
        """Format task + context into model input with special tokens."""
        parts = []
        # Task section
        parts.append(TASK_TOKENS[0])  # <|task_start|>
        parts.append(f"{TASK_TOKENS[2]}{self.task_packet.task_id}")  # <|task_id|>
        parts.append(f"{TASK_TOKENS[3]}{self.task_packet.task_type}")  # <|task_type|>
        parts.append(f"Description: {self.task_packet.description}")
        if self.task_packet.constraints:
            parts.append(f"{TASK_TOKENS[5]}{'; '.join(self.task_packet.constraints)}")
        parts.append(TASK_TOKENS[1])  # <|task_end|>

        # Context section
        parts.append(CONTEXT_TOKENS[0])  # <|context_start|>
        parts.append(f"{CONTEXT_TOKENS[2]}{self.context_packet.file_path}")  # <|context_file|>
        parts.append(f"{CONTEXT_TOKENS[6]}{self.context_packet.language}")  # <|context_language|>
        parts.append(f"{CONTEXT_TOKENS[4]}{self.context_packet.content}")  # <|context_snippet|>
        if self.context_packet.symbols:
            parts.append(f"{CONTEXT_TOKENS[3]}{', '.join(self.context_packet.symbols)}")
        parts.append(CONTEXT_TOKENS[1])  # <|context_end|>

        return "\n".join(parts)

    def format_target(self) -> str:
        """Format target BranchTicket as JSON output."""
        return self.target_branch_ticket.to_json()

    def format_full(self) -> str:
        """Format complete input->output training example."""
        return f"{self.format_input()}\n{BRANCH_TOKENS[0]}\n{self.format_target()}\n{BRANCH_TOKENS[1]}"


def _make_read_set(task_type: str, file_path: str) -> List[str]:
    """Generate appropriate read_set based on task type."""
    base = [file_path]
    if task_type in ("bug_fix", "refactor", "performance_patch"):
        base.append(file_path.replace("src/", "tests/test_"))
    if task_type == "api_migration":
        base.append("docs/api_spec.yaml")
    if task_type == "type_fix":
        base.append("pyproject.toml")
    return base


def _make_write_set(task_type: str, file_path: str) -> List[str]:
    """Generate appropriate write_set based on task type."""
    if task_type == "test_generation":
        return [file_path.replace("src/", "tests/test_")]
    if task_type == "config_fix":
        return [file_path]
    return [file_path]


def _make_verifier_targets(task_type: str, file_path: str) -> List[str]:
    """Generate verifier targets based on task type."""
    test_path = file_path.replace("src/", "tests/test_")
    if task_type == "test_generation":
        return [f"{test_path}::test_coverage_check"]
    if task_type == "type_fix":
        return ["mypy::strict_check"]
    if task_type == "performance_patch":
        return [f"{test_path}::test_performance", "benchmark::latency_check"]
    return [f"{test_path}::test_main"]


def _select_branch_type(task_type: str, idx: int) -> str:
    """Select branch_type cycling through all types across examples."""
    branch_types = sorted(ALLOWED_BRANCH_TYPES)
    # Map task types to preferred branch types but cycle
    preference_map = {
        "bug_fix": ["fix", "patch"],
        "test_generation": ["test", "patch"],
        "refactor": ["refactor", "patch"],
        "api_migration": ["patch", "refactor"],
        "type_fix": ["fix", "patch"],
        "performance_patch": ["patch", "fix"],
        "config_fix": ["fix", "patch"],
    }
    prefs = preference_map.get(task_type, branch_types)
    # Use index to cycle so we cover all types
    all_options = prefs + [bt for bt in branch_types if bt not in prefs]
    return all_options[idx % len(all_options)]


def _select_privilege_level(task_type: str, idx: int) -> str:
    """Select privilege level cycling to cover all levels."""
    levels = sorted(ALLOWED_PRIVILEGE_LEVELS)
    # Some tasks need higher privilege
    if task_type in ("api_migration", "config_fix") and idx % 3 == 0:
        return "admin"
    if task_type == "test_generation" and idx % 4 == 0:
        return "read_only"
    return levels[idx % len(levels)]


def _select_difficulty(idx: int) -> str:
    """Assign difficulty based on index cycling."""
    difficulties = ["easy", "medium", "hard"]
    return difficulties[idx % 3]


def generate_diverse_examples(count: int = 100, seed: int = 42) -> List[BranchTicketSFTExample]:
    """Generate diverse BranchTicket SFT training examples.

    Ensures coverage of:
    - All 7 task categories
    - All branch_types (patch, refactor, test, documentation, exploration, fix)
    - All privilege_levels (read_only, read_write, admin, sandboxed)

    Args:
        count: Number of examples to generate (minimum 35 for full coverage)
        seed: Random seed for reproducibility

    Returns:
        List of BranchTicketSFTExample instances
    """
    rng = random.Random(seed)
    examples = []
    task_types = sorted(TASK_CATEGORIES.keys())

    for i in range(count):
        task_type = task_types[i % len(task_types)]
        category = TASK_CATEGORIES[task_type]

        # Pick description and constraints
        desc = category["descriptions"][i % len(category["descriptions"])]
        constraints = category["constraints"][i % len(category["constraints"])]

        # Pick context
        lang = "python" if i % 3 != 2 else "typescript"
        ctx_templates = CONTEXT_TEMPLATES[lang]
        ctx_file, ctx_content = ctx_templates[i % len(ctx_templates)]

        # Build TaskPacket
        task_packet = TaskPacket(
            task_id=f"task_{i:04d}",
            task_type=task_type,
            description=desc,
            constraints=constraints,
            context_refs=[f"ctx_{i:04d}"],
            priority=rng.randint(0, 5),
            metadata={"category": task_type, "index": i},
        )

        # Build ContextPacket
        symbols = []
        for line in ctx_content.split("\n"):
            if "def " in line:
                name = line.split("def ")[1].split("(")[0]
                symbols.append(name)
            elif "class " in line:
                name = line.split("class ")[1].split("(")[0].split(":")[0]
                symbols.append(name)
        context_packet = ContextPacket(
            context_id=f"ctx_{i:04d}",
            source_type="file",
            content=ctx_content,
            file_path=ctx_file,
            language=lang,
            symbols=symbols,
            dependencies=["typing"] if lang == "python" else ["express"],
            metadata={"line_start": 1, "line_end": ctx_content.count("\n") + 1},
        )

        # Build target BranchTicket
        branch_type = _select_branch_type(task_type, i)
        privilege_level = _select_privilege_level(task_type, i)
        read_set = _make_read_set(task_type, ctx_file)
        write_set = _make_write_set(task_type, ctx_file)
        verifier_targets = _make_verifier_targets(task_type, ctx_file)

        target_ticket = BranchTicket(
            ticket_id=f"branch_{i:04d}",
            branch_type=branch_type,
            privilege_level=privilege_level,
            description=desc,
            read_set=read_set,
            write_set=write_set,
            verifier_targets=verifier_targets,
            constraints=constraints,
            parent_ticket_id=None,
            metadata={"task_type": task_type, "difficulty": _select_difficulty(i)},
        )

        difficulty = _select_difficulty(i)

        example = BranchTicketSFTExample(
            task_packet=task_packet,
            context_packet=context_packet,
            target_branch_ticket=target_ticket,
            task_type=task_type,
            difficulty=difficulty,
            is_valid=True,
        )
        examples.append(example)

    return examples


def generate_invalid_examples(count: int = 30, seed: int = 123) -> List[BranchTicketSFTExample]:
    """Generate INVALID BranchTicket examples for rejection training.

    Invalid examples have specific known errors:
    - Missing read_set on patch branches
    - Missing verifier_targets on patch branches
    - Invalid branch_type
    - Invalid privilege_level
    - Empty ticket_id
    - Broad rewrite without explicit flag

    Args:
        count: Number of invalid examples to generate
        seed: Random seed

    Returns:
        List of BranchTicketSFTExample with is_valid=False
    """
    rng = random.Random(seed)
    examples = []
    task_types = sorted(TASK_CATEGORIES.keys())

    invalid_patterns = [
        ("missing_read_set", "read_set must be non-empty for patch branches"),
        ("missing_verifier", "verifier_targets must be present for patch branches"),
        ("invalid_branch_type", "branch_type"),
        ("invalid_privilege", "privilege_level"),
        ("empty_ticket_id", "ticket_id must not be empty"),
        ("missing_write_set", "write_set must be present for patch branches"),
    ]

    for i in range(count):
        task_type = task_types[i % len(task_types)]
        category = TASK_CATEGORIES[task_type]
        pattern_name, _ = invalid_patterns[i % len(invalid_patterns)]

        desc = category["descriptions"][i % len(category["descriptions"])]
        constraints = category["constraints"][0]

        # Build task and context
        ctx_templates = CONTEXT_TEMPLATES["python"]
        ctx_file, ctx_content = ctx_templates[i % len(ctx_templates)]

        task_packet = TaskPacket(
            task_id=f"task_inv_{i:04d}",
            task_type=task_type,
            description=desc,
            constraints=constraints,
            context_refs=[f"ctx_inv_{i:04d}"],
            priority=1,
        )

        context_packet = ContextPacket(
            context_id=f"ctx_inv_{i:04d}",
            source_type="file",
            content=ctx_content,
            file_path=ctx_file,
            language="python",
            symbols=[],
        )

        # Build intentionally invalid ticket
        if pattern_name == "missing_read_set":
            ticket = BranchTicket(
                ticket_id=f"inv_{i:04d}",
                branch_type="patch",
                privilege_level="read_write",
                description=desc,
                read_set=[],  # Invalid: empty for patch
                write_set=[ctx_file],
                verifier_targets=["tests/test_x.py::test_main"],
                constraints=constraints,
            )
            reason = "read_set must be non-empty for patch branches"

        elif pattern_name == "missing_verifier":
            ticket = BranchTicket(
                ticket_id=f"inv_{i:04d}",
                branch_type="patch",
                privilege_level="read_write",
                description=desc,
                read_set=[ctx_file],
                write_set=[ctx_file],
                verifier_targets=[],  # Invalid: empty for patch
                constraints=constraints,
            )
            reason = "verifier_targets must be present for patch branches"

        elif pattern_name == "invalid_branch_type":
            ticket = BranchTicket(
                ticket_id=f"inv_{i:04d}",
                branch_type="invalid_type",  # Invalid
                privilege_level="read_write",
                description=desc,
                read_set=[ctx_file],
                write_set=[ctx_file],
                verifier_targets=["tests/test_x.py::test_main"],
                constraints=constraints,
            )
            reason = "branch_type 'invalid_type' not in allowed set"

        elif pattern_name == "invalid_privilege":
            ticket = BranchTicket(
                ticket_id=f"inv_{i:04d}",
                branch_type="patch",
                privilege_level="superuser",  # Invalid
                description=desc,
                read_set=[ctx_file],
                write_set=[ctx_file],
                verifier_targets=["tests/test_x.py::test_main"],
                constraints=constraints,
            )
            reason = "privilege_level 'superuser' not in allowed set"

        elif pattern_name == "empty_ticket_id":
            ticket = BranchTicket(
                ticket_id="",  # Invalid: empty
                branch_type="patch",
                privilege_level="read_write",
                description=desc,
                read_set=[ctx_file],
                write_set=[ctx_file],
                verifier_targets=["tests/test_x.py::test_main"],
                constraints=constraints,
            )
            reason = "ticket_id must not be empty"

        elif pattern_name == "missing_write_set":
            ticket = BranchTicket(
                ticket_id=f"inv_{i:04d}",
                branch_type="patch",
                privilege_level="read_write",
                description=desc,
                read_set=[ctx_file],
                write_set=[],  # Invalid: empty for patch
                verifier_targets=["tests/test_x.py::test_main"],
                constraints=constraints,
            )
            reason = "write_set must be present for patch branches"

        else:
            # Shouldn't reach here but fallback
            ticket = BranchTicket(ticket_id="", branch_type="patch")
            reason = "invalid example"

        example = BranchTicketSFTExample(
            task_packet=task_packet,
            context_packet=context_packet,
            target_branch_ticket=ticket,
            task_type=task_type,
            difficulty="hard",
            is_valid=False,
            invalid_reason=reason,
        )
        examples.append(example)

    return examples
