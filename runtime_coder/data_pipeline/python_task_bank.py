"""Bank of 50+ Python task templates for RuntimeCoder training.

Each task template includes a TaskPacket, ContextPacket, and target BranchTicket
with required schema_hash, runtime_contract_version, and target_kind fields.
"""

import hashlib
from typing import Dict, List, Any

from runtime_coder.schema.canonical_schema_loader import compute_schema_hash

_SCHEMA_HASH = compute_schema_hash()
_CONTRACT_VERSION = "1.0"
_TARGET_KIND = "python"

# Task categories
TASK_TYPES = [
    "bug_fix", "test_gen", "type_fix", "import_fix",
    "refactor", "documentation", "performance", "security",
]


def _make_ticket(task_id: str, branch_type: str, desc: str,
                 read_set: List[str], write_set: List[str],
                 verifier_targets: List[str] = None,
                 constraints: List[str] = None) -> Dict[str, Any]:
    """Create a BranchTicket dict with required runtime fields."""
    return {
        "ticket_id": task_id,
        "branch_type": branch_type,
        "privilege_level": "read_write",
        "description": desc,
        "read_set": read_set,
        "write_set": write_set,
        "verifier_targets": verifier_targets or [],
        "constraints": constraints or [],
        "schema_hash": _SCHEMA_HASH,
        "runtime_contract_version": _CONTRACT_VERSION,
        "target_kind": _TARGET_KIND,
    }


def _make_task(task_id: str, task_type: str, desc: str,
               context_refs: List[str] = None) -> Dict[str, Any]:
    """Create a TaskPacket dict."""
    return {
        "task_id": task_id,
        "task_type": task_type,
        "description": desc,
        "constraints": [],
        "context_refs": context_refs or [],
        "priority": 1,
    }


def _make_context(ctx_id: str, file_path: str, content: str,
                  symbols: List[str] = None) -> Dict[str, Any]:
    """Create a ContextPacket dict."""
    return {
        "context_id": ctx_id,
        "source_type": "file",
        "content": content,
        "file_path": file_path,
        "language": "python",
        "symbols": symbols or [],
        "dependencies": [],
    }


# ============================================================================
# Bug Fix tasks (10 templates)
# ============================================================================

_BUG_FIX_TEMPLATES = [
    {
        "task": _make_task("bf_001", "bug_fix", "Fix off-by-one in binary search"),
        "context": _make_context("ctx_bf_001", "src/search.py",
            "def binary_search(arr, target):\n    left, right = 0, len(arr)\n    while left < right:\n        mid = (left + right) / 2\n        if arr[mid] == target:\n            return mid\n    return -1\n",
            ["binary_search"]),
        "ticket": _make_ticket("bf_001", "bug_fix", "Fix integer division and bounds",
            ["src/search.py"], ["src/search.py"],
            ["tests/test_search.py::test_binary_search"]),
    },
    {
        "task": _make_task("bf_002", "bug_fix", "Fix KeyError in dict access"),
        "context": _make_context("ctx_bf_002", "src/config.py",
            "def get_setting(config, key):\n    return config[key]\n",
            ["get_setting"]),
        "ticket": _make_ticket("bf_002", "bug_fix", "Add .get() with default",
            ["src/config.py"], ["src/config.py"]),
    },
    {
        "task": _make_task("bf_003", "bug_fix", "Fix None comparison with =="),
        "context": _make_context("ctx_bf_003", "src/validator.py",
            "def check_value(val):\n    if val == None:\n        return False\n    return True\n",
            ["check_value"]),
        "ticket": _make_ticket("bf_003", "bug_fix", "Use 'is None' instead of '== None'",
            ["src/validator.py"], ["src/validator.py"]),
    },
    {
        "task": _make_task("bf_004", "bug_fix", "Fix mutable default argument"),
        "context": _make_context("ctx_bf_004", "src/collector.py",
            "def add_item(item, items=[]):\n    items.append(item)\n    return items\n",
            ["add_item"]),
        "ticket": _make_ticket("bf_004", "bug_fix", "Replace mutable default with None",
            ["src/collector.py"], ["src/collector.py"]),
    },
    {
        "task": _make_task("bf_005", "bug_fix", "Fix unclosed file handle"),
        "context": _make_context("ctx_bf_005", "src/reader.py",
            "def read_file(path):\n    f = open(path)\n    data = f.read()\n    return data\n",
            ["read_file"]),
        "ticket": _make_ticket("bf_005", "bug_fix", "Use context manager for file",
            ["src/reader.py"], ["src/reader.py"]),
    },
    {
        "task": _make_task("bf_006", "bug_fix", "Fix incorrect string concatenation in loop"),
        "context": _make_context("ctx_bf_006", "src/formatter.py",
            "def join_items(items):\n    result = ''\n    for item in items:\n        result = result + str(item) + ', '\n    return result\n",
            ["join_items"]),
        "ticket": _make_ticket("bf_006", "bug_fix", "Use str.join for efficiency",
            ["src/formatter.py"], ["src/formatter.py"]),
    },
    {
        "task": _make_task("bf_007", "bug_fix", "Fix catch-all except clause"),
        "context": _make_context("ctx_bf_007", "src/parser.py",
            "def safe_parse(text):\n    try:\n        return int(text)\n    except:\n        return None\n",
            ["safe_parse"]),
        "ticket": _make_ticket("bf_007", "bug_fix", "Catch specific ValueError",
            ["src/parser.py"], ["src/parser.py"]),
    },
    {
        "task": _make_task("bf_008", "bug_fix", "Fix variable shadowing builtin"),
        "context": _make_context("ctx_bf_008", "src/utils.py",
            "def process(list):\n    return len(list)\n",
            ["process"]),
        "ticket": _make_ticket("bf_008", "bug_fix", "Rename parameter to avoid shadowing 'list'",
            ["src/utils.py"], ["src/utils.py"]),
    },
    {
        "task": _make_task("bf_009", "bug_fix", "Fix infinite loop in retry logic"),
        "context": _make_context("ctx_bf_009", "src/client.py",
            "def fetch_with_retry(url):\n    while True:\n        resp = request(url)\n        if resp.ok:\n            return resp\n",
            ["fetch_with_retry"]),
        "ticket": _make_ticket("bf_009", "bug_fix", "Add max retries counter",
            ["src/client.py"], ["src/client.py"]),
    },
    {
        "task": _make_task("bf_010", "bug_fix", "Fix race condition in counter"),
        "context": _make_context("ctx_bf_010", "src/counter.py",
            "count = 0\ndef increment():\n    global count\n    count += 1\n",
            ["increment"]),
        "ticket": _make_ticket("bf_010", "bug_fix", "Add threading lock",
            ["src/counter.py"], ["src/counter.py"]),
    },
]

# ============================================================================
# Test Generation tasks (8 templates)
# ============================================================================

_TEST_GEN_TEMPLATES = [
    {
        "task": _make_task("tg_001", "test_gen", "Generate unit tests for Stack class"),
        "context": _make_context("ctx_tg_001", "src/stack.py",
            "class Stack:\n    def __init__(self):\n        self._items = []\n    def push(self, item):\n        self._items.append(item)\n    def pop(self):\n        return self._items.pop()\n    def is_empty(self):\n        return len(self._items) == 0\n",
            ["Stack", "push", "pop", "is_empty"]),
        "ticket": _make_ticket("tg_001", "test", "Generate tests for Stack class",
            ["src/stack.py"], ["tests/test_stack.py"],
            ["tests/test_stack.py"]),
    },
    {
        "task": _make_task("tg_002", "test_gen", "Generate tests for calculator"),
        "context": _make_context("ctx_tg_002", "src/calc.py",
            "def add(a, b): return a + b\ndef divide(a, b): return a / b\n",
            ["add", "divide"]),
        "ticket": _make_ticket("tg_002", "test", "Test calculator functions including division by zero",
            ["src/calc.py"], ["tests/test_calc.py"]),
    },
    {
        "task": _make_task("tg_003", "test_gen", "Generate edge case tests for sort"),
        "context": _make_context("ctx_tg_003", "src/sort.py",
            "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[0]\n    left = [x for x in arr[1:] if x <= pivot]\n    right = [x for x in arr[1:] if x > pivot]\n    return quicksort(left) + [pivot] + quicksort(right)\n",
            ["quicksort"]),
        "ticket": _make_ticket("tg_003", "test", "Test quicksort with empty, single, duplicates",
            ["src/sort.py"], ["tests/test_sort.py"]),
    },
    {
        "task": _make_task("tg_004", "test_gen", "Generate tests for file parser"),
        "context": _make_context("ctx_tg_004", "src/parser.py",
            "def parse_csv(text):\n    lines = text.strip().split('\\n')\n    return [line.split(',') for line in lines]\n",
            ["parse_csv"]),
        "ticket": _make_ticket("tg_004", "test", "Test CSV parser with edge cases",
            ["src/parser.py"], ["tests/test_parser.py"]),
    },
    {
        "task": _make_task("tg_005", "test_gen", "Generate tests for rate limiter"),
        "context": _make_context("ctx_tg_005", "src/limiter.py",
            "import time\nclass RateLimiter:\n    def __init__(self, max_calls, period):\n        self.max_calls = max_calls\n        self.period = period\n        self.calls = []\n    def allow(self):\n        now = time.time()\n        self.calls = [t for t in self.calls if now - t < self.period]\n        if len(self.calls) < self.max_calls:\n            self.calls.append(now)\n            return True\n        return False\n",
            ["RateLimiter", "allow"]),
        "ticket": _make_ticket("tg_005", "test", "Test rate limiter boundary conditions",
            ["src/limiter.py"], ["tests/test_limiter.py"]),
    },
    {
        "task": _make_task("tg_006", "test_gen", "Generate tests for tree traversal"),
        "context": _make_context("ctx_tg_006", "src/tree.py",
            "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\ndef inorder(node):\n    if not node:\n        return []\n    return inorder(node.left) + [node.val] + inorder(node.right)\n",
            ["Node", "inorder"]),
        "ticket": _make_ticket("tg_006", "test", "Test tree traversal with empty and balanced trees",
            ["src/tree.py"], ["tests/test_tree.py"]),
    },
    {
        "task": _make_task("tg_007", "test_gen", "Generate integration tests for API client"),
        "context": _make_context("ctx_tg_007", "src/api_client.py",
            "class APIClient:\n    def __init__(self, base_url):\n        self.base_url = base_url\n    def get(self, path):\n        import requests\n        return requests.get(f'{self.base_url}{path}')\n",
            ["APIClient", "get"]),
        "ticket": _make_ticket("tg_007", "test", "Test API client with mocked responses",
            ["src/api_client.py"], ["tests/test_api_client.py"]),
    },
    {
        "task": _make_task("tg_008", "test_gen", "Generate property-based tests for encoder"),
        "context": _make_context("ctx_tg_008", "src/encoder.py",
            "import base64\ndef encode(data: bytes) -> str:\n    return base64.b64encode(data).decode()\ndef decode(text: str) -> bytes:\n    return base64.b64decode(text.encode())\n",
            ["encode", "decode"]),
        "ticket": _make_ticket("tg_008", "test", "Property: decode(encode(x)) == x for all bytes",
            ["src/encoder.py"], ["tests/test_encoder.py"]),
    },
]

# ============================================================================
# Type Fix tasks (7 templates)
# ============================================================================

_TYPE_FIX_TEMPLATES = [
    {
        "task": _make_task("tf_001", "type_fix", "Add type annotations to function"),
        "context": _make_context("ctx_tf_001", "src/math_utils.py",
            "def average(numbers):\n    return sum(numbers) / len(numbers)\n",
            ["average"]),
        "ticket": _make_ticket("tf_001", "type_fix", "Add List[float] -> float annotation",
            ["src/math_utils.py"], ["src/math_utils.py"]),
    },
    {
        "task": _make_task("tf_002", "type_fix", "Fix Optional type not handled"),
        "context": _make_context("ctx_tf_002", "src/user.py",
            "def get_name(user) -> str:\n    return user.name\n",
            ["get_name"]),
        "ticket": _make_ticket("tf_002", "type_fix", "Handle Optional[User] parameter",
            ["src/user.py"], ["src/user.py"]),
    },
    {
        "task": _make_task("tf_003", "type_fix", "Fix incompatible return type"),
        "context": _make_context("ctx_tf_003", "src/lookup.py",
            "from typing import Dict\ndef find(d: Dict[str, int], key: str) -> int:\n    return d.get(key)\n",
            ["find"]),
        "ticket": _make_ticket("tf_003", "type_fix", "Return Optional[int] or provide default",
            ["src/lookup.py"], ["src/lookup.py"]),
    },
    {
        "task": _make_task("tf_004", "type_fix", "Add generic type to container"),
        "context": _make_context("ctx_tf_004", "src/container.py",
            "class Cache:\n    def __init__(self):\n        self.data = {}\n    def get(self, key):\n        return self.data.get(key)\n    def set(self, key, value):\n        self.data[key] = value\n",
            ["Cache", "get", "set"]),
        "ticket": _make_ticket("tf_004", "type_fix", "Add Generic[KT, VT] typing",
            ["src/container.py"], ["src/container.py"]),
    },
    {
        "task": _make_task("tf_005", "type_fix", "Fix Union type narrowing"),
        "context": _make_context("ctx_tf_005", "src/handler.py",
            "from typing import Union\ndef handle(val: Union[str, int]):\n    return val.upper()\n",
            ["handle"]),
        "ticket": _make_ticket("tf_005", "type_fix", "Add isinstance check before str method",
            ["src/handler.py"], ["src/handler.py"]),
    },
    {
        "task": _make_task("tf_006", "type_fix", "Add Protocol type for duck typing"),
        "context": _make_context("ctx_tf_006", "src/serializer.py",
            "def serialize(obj):\n    return obj.to_dict()\n",
            ["serialize"]),
        "ticket": _make_ticket("tf_006", "type_fix", "Define Serializable Protocol",
            ["src/serializer.py"], ["src/serializer.py"]),
    },
    {
        "task": _make_task("tf_007", "type_fix", "Fix TypeVar bound constraint"),
        "context": _make_context("ctx_tf_007", "src/comparable.py",
            "def max_val(a, b):\n    return a if a > b else b\n",
            ["max_val"]),
        "ticket": _make_ticket("tf_007", "type_fix", "Add TypeVar with Comparable bound",
            ["src/comparable.py"], ["src/comparable.py"]),
    },
]

# ============================================================================
# Import Fix tasks (7 templates)
# ============================================================================

_IMPORT_FIX_TEMPLATES = [
    {
        "task": _make_task("if_001", "import_fix", "Fix missing import for dataclass"),
        "context": _make_context("ctx_if_001", "src/models.py",
            "@dataclass\nclass User:\n    name: str\n    age: int\n",
            ["User"]),
        "ticket": _make_ticket("if_001", "import_fix", "Add 'from dataclasses import dataclass'",
            ["src/models.py"], ["src/models.py"]),
    },
    {
        "task": _make_task("if_002", "import_fix", "Fix circular import"),
        "context": _make_context("ctx_if_002", "src/a.py",
            "from src.b import B\nclass A:\n    def get_b(self) -> B:\n        return B()\n",
            ["A"]),
        "ticket": _make_ticket("if_002", "import_fix", "Use TYPE_CHECKING guard",
            ["src/a.py", "src/b.py"], ["src/a.py"]),
    },
    {
        "task": _make_task("if_003", "import_fix", "Fix wildcard import"),
        "context": _make_context("ctx_if_003", "src/main.py",
            "from os.path import *\nresult = join('a', 'b')\n",
            []),
        "ticket": _make_ticket("if_003", "import_fix", "Replace with explicit 'from os.path import join'",
            ["src/main.py"], ["src/main.py"]),
    },
    {
        "task": _make_task("if_004", "import_fix", "Fix unused imports"),
        "context": _make_context("ctx_if_004", "src/app.py",
            "import os\nimport sys\nimport json\nimport math\n\ndef run():\n    print(json.dumps({}))\n",
            ["run"]),
        "ticket": _make_ticket("if_004", "import_fix", "Remove unused os, sys, math imports",
            ["src/app.py"], ["src/app.py"]),
    },
    {
        "task": _make_task("if_005", "import_fix", "Fix relative vs absolute import"),
        "context": _make_context("ctx_if_005", "src/pkg/module.py",
            "from ..utils import helper\n",
            []),
        "ticket": _make_ticket("if_005", "import_fix", "Convert to absolute import path",
            ["src/pkg/module.py"], ["src/pkg/module.py"]),
    },
    {
        "task": _make_task("if_006", "import_fix", "Fix deprecated import"),
        "context": _make_context("ctx_if_006", "src/collections_use.py",
            "from collections import Mapping\n",
            []),
        "ticket": _make_ticket("if_006", "import_fix", "Use collections.abc.Mapping instead",
            ["src/collections_use.py"], ["src/collections_use.py"]),
    },
    {
        "task": _make_task("if_007", "import_fix", "Fix import order (isort)"),
        "context": _make_context("ctx_if_007", "src/mixed.py",
            "from my_module import thing\nimport os\nfrom typing import List\nimport sys\n",
            []),
        "ticket": _make_ticket("if_007", "import_fix", "Reorder: stdlib, third-party, local",
            ["src/mixed.py"], ["src/mixed.py"]),
    },
]

# ============================================================================
# Refactor tasks (7 templates)
# ============================================================================

_REFACTOR_TEMPLATES = [
    {
        "task": _make_task("rf_001", "refactor", "Extract method from long function"),
        "context": _make_context("ctx_rf_001", "src/processor.py",
            "def process(data):\n    # validate\n    if not data:\n        raise ValueError('empty')\n    # transform\n    result = [x * 2 for x in data]\n    # filter\n    result = [x for x in result if x > 0]\n    return result\n",
            ["process"]),
        "ticket": _make_ticket("rf_001", "refactor", "Extract validate, transform, filter methods",
            ["src/processor.py"], ["src/processor.py"]),
    },
    {
        "task": _make_task("rf_002", "refactor", "Replace inheritance with composition"),
        "context": _make_context("ctx_rf_002", "src/shapes.py",
            "class Shape:\n    def area(self): pass\nclass Circle(Shape):\n    def __init__(self, r):\n        self.r = r\n    def area(self):\n        return 3.14 * self.r ** 2\n",
            ["Shape", "Circle"]),
        "ticket": _make_ticket("rf_002", "refactor", "Use Protocol instead of base class",
            ["src/shapes.py"], ["src/shapes.py"]),
    },
    {
        "task": _make_task("rf_003", "refactor", "Convert class to dataclass"),
        "context": _make_context("ctx_rf_003", "src/point.py",
            "class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __eq__(self, other):\n        return self.x == other.x and self.y == other.y\n",
            ["Point"]),
        "ticket": _make_ticket("rf_003", "refactor", "Convert to @dataclass",
            ["src/point.py"], ["src/point.py"]),
    },
    {
        "task": _make_task("rf_004", "refactor", "Replace nested ifs with guard clauses"),
        "context": _make_context("ctx_rf_004", "src/auth.py",
            "def login(user, password):\n    if user:\n        if password:\n            if verify(user, password):\n                return True\n    return False\n",
            ["login"]),
        "ticket": _make_ticket("rf_004", "refactor", "Use early returns for validation",
            ["src/auth.py"], ["src/auth.py"]),
    },
    {
        "task": _make_task("rf_005", "refactor", "Extract constants from magic numbers"),
        "context": _make_context("ctx_rf_005", "src/physics.py",
            "def kinetic_energy(mass, velocity):\n    return 0.5 * mass * velocity ** 2\ndef gravitational_force(m1, m2, r):\n    return 6.674e-11 * m1 * m2 / r ** 2\n",
            ["kinetic_energy", "gravitational_force"]),
        "ticket": _make_ticket("rf_005", "refactor", "Define G constant and KE_FACTOR",
            ["src/physics.py"], ["src/physics.py"]),
    },
    {
        "task": _make_task("rf_006", "refactor", "Replace dict with TypedDict"),
        "context": _make_context("ctx_rf_006", "src/response.py",
            "def make_response(status, body):\n    return {'status': status, 'body': body, 'headers': {}}\n",
            ["make_response"]),
        "ticket": _make_ticket("rf_006", "refactor", "Define Response TypedDict",
            ["src/response.py"], ["src/response.py"]),
    },
    {
        "task": _make_task("rf_007", "refactor", "Simplify comprehension with walrus operator"),
        "context": _make_context("ctx_rf_007", "src/filter.py",
            "def filter_valid(items):\n    results = []\n    for item in items:\n        val = compute(item)\n        if val is not None:\n            results.append(val)\n    return results\n",
            ["filter_valid"]),
        "ticket": _make_ticket("rf_007", "refactor", "Use list comprehension with :=",
            ["src/filter.py"], ["src/filter.py"]),
    },
]

# ============================================================================
# Documentation tasks (5 templates)
# ============================================================================

_DOC_TEMPLATES = [
    {
        "task": _make_task("dc_001", "documentation", "Add docstring to module"),
        "context": _make_context("ctx_dc_001", "src/utils.py",
            "def clamp(val, lo, hi):\n    return max(lo, min(val, hi))\n",
            ["clamp"]),
        "ticket": _make_ticket("dc_001", "documentation", "Add Google-style docstring",
            ["src/utils.py"], ["src/utils.py"]),
    },
    {
        "task": _make_task("dc_002", "documentation", "Add type stubs for legacy module"),
        "context": _make_context("ctx_dc_002", "src/legacy.py",
            "def transform(data, opts=None):\n    if opts and 'mode' in opts:\n        return process(data, opts['mode'])\n    return data\n",
            ["transform"]),
        "ticket": _make_ticket("dc_002", "documentation", "Create .pyi stub file",
            ["src/legacy.py"], ["src/legacy.pyi"]),
    },
    {
        "task": _make_task("dc_003", "documentation", "Add examples to docstring"),
        "context": _make_context("ctx_dc_003", "src/text.py",
            "def slugify(text: str) -> str:\n    \"\"\"Convert text to URL slug.\"\"\"\n    import re\n    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')\n",
            ["slugify"]),
        "ticket": _make_ticket("dc_003", "documentation", "Add Examples section with doctests",
            ["src/text.py"], ["src/text.py"]),
    },
    {
        "task": _make_task("dc_004", "documentation", "Document exception behavior"),
        "context": _make_context("ctx_dc_004", "src/io_ops.py",
            "def load_json(path: str) -> dict:\n    with open(path) as f:\n        return json.load(f)\n",
            ["load_json"]),
        "ticket": _make_ticket("dc_004", "documentation", "Document FileNotFoundError and JSONDecodeError",
            ["src/io_ops.py"], ["src/io_ops.py"]),
    },
    {
        "task": _make_task("dc_005", "documentation", "Add README usage examples"),
        "context": _make_context("ctx_dc_005", "src/cli.py",
            "import argparse\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--input', required=True)\n    args = parser.parse_args()\n    process(args.input)\n",
            ["main"]),
        "ticket": _make_ticket("dc_005", "documentation", "Write CLI usage section in README",
            ["src/cli.py"], ["README.md"]),
    },
]

# ============================================================================
# Performance tasks (5 templates)
# ============================================================================

_PERF_TEMPLATES = [
    {
        "task": _make_task("pf_001", "performance", "Replace list with generator"),
        "context": _make_context("ctx_pf_001", "src/data.py",
            "def get_even(numbers):\n    return [x for x in numbers if x % 2 == 0]\n",
            ["get_even"]),
        "ticket": _make_ticket("pf_001", "refactor", "Use generator for lazy evaluation",
            ["src/data.py"], ["src/data.py"]),
    },
    {
        "task": _make_task("pf_002", "performance", "Add LRU cache to recursive function"),
        "context": _make_context("ctx_pf_002", "src/fib.py",
            "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n",
            ["fibonacci"]),
        "ticket": _make_ticket("pf_002", "refactor", "Add @lru_cache decorator",
            ["src/fib.py"], ["src/fib.py"]),
    },
    {
        "task": _make_task("pf_003", "performance", "Use set for membership testing"),
        "context": _make_context("ctx_pf_003", "src/filter.py",
            "def filter_allowed(items, allowed_list):\n    return [x for x in items if x in allowed_list]\n",
            ["filter_allowed"]),
        "ticket": _make_ticket("pf_003", "refactor", "Convert allowed_list to set first",
            ["src/filter.py"], ["src/filter.py"]),
    },
    {
        "task": _make_task("pf_004", "performance", "Batch database queries"),
        "context": _make_context("ctx_pf_004", "src/db.py",
            "def get_users(ids):\n    results = []\n    for uid in ids:\n        results.append(db.query(f'SELECT * FROM users WHERE id={uid}'))\n    return results\n",
            ["get_users"]),
        "ticket": _make_ticket("pf_004", "refactor", "Use single IN clause query",
            ["src/db.py"], ["src/db.py"]),
    },
    {
        "task": _make_task("pf_005", "performance", "Use slots in data class"),
        "context": _make_context("ctx_pf_005", "src/event.py",
            "class Event:\n    def __init__(self, name, timestamp):\n        self.name = name\n        self.timestamp = timestamp\n",
            ["Event"]),
        "ticket": _make_ticket("pf_005", "refactor", "Add __slots__ for memory efficiency",
            ["src/event.py"], ["src/event.py"]),
    },
]

# ============================================================================
# Security tasks (5 templates)
# ============================================================================

_SECURITY_TEMPLATES = [
    {
        "task": _make_task("sc_001", "security", "Fix SQL injection vulnerability"),
        "context": _make_context("ctx_sc_001", "src/db.py",
            "def find_user(name):\n    query = f\"SELECT * FROM users WHERE name='{name}'\"\n    return db.execute(query)\n",
            ["find_user"]),
        "ticket": _make_ticket("sc_001", "fix", "Use parameterized query",
            ["src/db.py"], ["src/db.py"],
            constraints=["no_string_interpolation_in_sql"]),
    },
    {
        "task": _make_task("sc_002", "security", "Fix path traversal"),
        "context": _make_context("ctx_sc_002", "src/files.py",
            "def serve_file(filename):\n    path = f'/data/{filename}'\n    return open(path).read()\n",
            ["serve_file"]),
        "ticket": _make_ticket("sc_002", "fix", "Validate path doesn't escape /data/",
            ["src/files.py"], ["src/files.py"]),
    },
    {
        "task": _make_task("sc_003", "security", "Fix hardcoded secret"),
        "context": _make_context("ctx_sc_003", "src/auth.py",
            "API_KEY = 'sk-1234567890abcdef'\ndef authenticate(key):\n    return key == API_KEY\n",
            ["authenticate"]),
        "ticket": _make_ticket("sc_003", "fix", "Load secret from environment variable",
            ["src/auth.py"], ["src/auth.py"],
            constraints=["no_secrets_in_source"]),
    },
    {
        "task": _make_task("sc_004", "security", "Fix unsafe deserialization"),
        "context": _make_context("ctx_sc_004", "src/loader.py",
            "import pickle\ndef load_data(path):\n    with open(path, 'rb') as f:\n        return pickle.load(f)\n",
            ["load_data"]),
        "ticket": _make_ticket("sc_004", "fix", "Replace pickle with json or validate source",
            ["src/loader.py"], ["src/loader.py"]),
    },
    {
        "task": _make_task("sc_005", "security", "Fix insecure random usage"),
        "context": _make_context("ctx_sc_005", "src/token_gen.py",
            "import random\ndef generate_token():\n    return ''.join(random.choices('abcdef0123456789', k=32))\n",
            ["generate_token"]),
        "ticket": _make_ticket("sc_005", "fix", "Use secrets module for crypto-safe randomness",
            ["src/token_gen.py"], ["src/token_gen.py"]),
    },
]

# ============================================================================
# Exploration tasks (4 templates)
# ============================================================================

_EXPLORATION_TEMPLATES = [
    {
        "task": _make_task("ex_001", "exploration", "Explore async refactor feasibility"),
        "context": _make_context("ctx_ex_001", "src/sync_client.py",
            "import requests\ndef fetch_all(urls):\n    return [requests.get(u).json() for u in urls]\n",
            ["fetch_all"]),
        "ticket": _make_ticket("ex_001", "exploration", "Assess asyncio/aiohttp migration",
            ["src/sync_client.py"], [],
            constraints=["read_only_exploration"]),
    },
    {
        "task": _make_task("ex_002", "exploration", "Explore caching strategy"),
        "context": _make_context("ctx_ex_002", "src/api.py",
            "def get_user_profile(user_id):\n    return db.query('SELECT * FROM profiles WHERE id=?', user_id)\n",
            ["get_user_profile"]),
        "ticket": _make_ticket("ex_002", "exploration", "Evaluate Redis vs in-memory cache",
            ["src/api.py"], [],
            constraints=["read_only_exploration"]),
    },
    {
        "task": _make_task("ex_003", "exploration", "Explore type coverage gaps"),
        "context": _make_context("ctx_ex_003", "src/legacy_module.py",
            "def process(data, config=None):\n    result = transform(data)\n    if config:\n        result = apply_config(result, config)\n    return result\n",
            ["process"]),
        "ticket": _make_ticket("ex_003", "exploration", "Map untyped functions and prioritize",
            ["src/legacy_module.py"], [],
            constraints=["read_only_exploration"]),
    },
    {
        "task": _make_task("ex_004", "exploration", "Explore test coverage gaps"),
        "context": _make_context("ctx_ex_004", "src/core.py",
            "class Engine:\n    def start(self): pass\n    def stop(self): pass\n    def restart(self): self.stop(); self.start()\n",
            ["Engine"]),
        "ticket": _make_ticket("ex_004", "exploration", "Identify untested paths in Engine",
            ["src/core.py", "tests/"], [],
            constraints=["read_only_exploration"]),
    },
]


def get_all_task_templates() -> List[Dict[str, Any]]:
    """Return all 53 task templates."""
    all_templates = (
        _BUG_FIX_TEMPLATES
        + _TEST_GEN_TEMPLATES
        + _TYPE_FIX_TEMPLATES
        + _IMPORT_FIX_TEMPLATES
        + _REFACTOR_TEMPLATES
        + _DOC_TEMPLATES
        + _PERF_TEMPLATES
        + _SECURITY_TEMPLATES
        + _EXPLORATION_TEMPLATES
    )
    return all_templates


def get_task_types() -> List[str]:
    """Return all supported task type strings."""
    return TASK_TYPES


def get_templates_by_type(task_type: str) -> List[Dict[str, Any]]:
    """Filter templates by task type."""
    return [t for t in get_all_task_templates() if t["task"]["task_type"] == task_type]
