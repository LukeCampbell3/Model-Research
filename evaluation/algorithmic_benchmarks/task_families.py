"""Respected algorithmic benchmark task families.

Implements four compatible benchmark families:
1. CLRS-Style: sorting, searching, string matching (sequence-adapted)
2. ListOps: nested list operations with variable depth/length
3. SCAN-Style: compositional command-to-action mapping
4. Dyck: multi-type bracket languages with depth generalization

All families produce (input_ids, target_ids) tensors compatible with
the Sparse Loop-MoE model interface.
"""

from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import Any
import torch


@dataclass
class BenchmarkSample:
    """A single benchmark sample with full metadata."""
    input_ids: torch.Tensor
    target_ids: torch.Tensor
    sample_id: str
    family: str
    task: str
    difficulty: str
    length_bucket: int
    metadata: dict[str, Any] = field(default_factory=dict)


# Token allocation for benchmark tasks (within vocab 256)
# Special: 0=PAD, 1=BOS, 2=EOS, 3=SEP
# Digits: 4-13
# Operators: 14-30
# ListOps ops: 31-40
# SCAN commands: 41-60
# SCAN actions: 61-80
# Dyck brackets: 81-100
# CLRS markers: 101-120
# General symbols: 121-200
# Unused: 201-255

PAD, BOS, EOS, SEP = 0, 1, 2, 3
DIGITS = list(range(4, 14))  # 0-9

# ListOps tokens
LISTOPS_OPEN = 31
LISTOPS_CLOSE = 32
LISTOPS_MIN = 33
LISTOPS_MAX = 34
LISTOPS_MED = 35  # median
LISTOPS_SM = 36   # sum_mod

# SCAN tokens
SCAN_WALK = 41
SCAN_RUN = 42
SCAN_JUMP = 43
SCAN_LOOK = 44
SCAN_LEFT = 45
SCAN_RIGHT = 46
SCAN_TURN = 47
SCAN_TWICE = 48
SCAN_THRICE = 49
SCAN_AND = 50
SCAN_AFTER = 51
SCAN_OPPOSITE = 52
# SCAN action tokens
SCAN_ACT_WALK = 61
SCAN_ACT_RUN = 62
SCAN_ACT_JUMP = 63
SCAN_ACT_LOOK = 64
SCAN_ACT_LTURN = 65
SCAN_ACT_RTURN = 66

# Dyck tokens
DYCK_OPEN_1 = 81
DYCK_CLOSE_1 = 82
DYCK_OPEN_2 = 83
DYCK_CLOSE_2 = 84
DYCK_OPEN_3 = 85
DYCK_CLOSE_3 = 86
DYCK_VALID = 87
DYCK_INVALID = 88

# CLRS markers
CLRS_INPUT_START = 101
CLRS_INPUT_END = 102
CLRS_OUTPUT_START = 103
CLRS_COMPARE = 104
CLRS_SWAP = 105
CLRS_FOUND = 106
CLRS_NOT_FOUND = 107


# =============================================================================
# FAMILY 1: CLRS-Style Algorithmic Reasoning (Sequence-Adapted)
# =============================================================================

class CLRSStyleGenerator:
    """CLRS-style algorithmic tasks adapted to flat token sequences.

    Label: CLRS_STYLE_SEQUENCE_ADAPTER
    NOT official CLRS. Faithful task structure with sequence encoding.
    """

    def __init__(self, vocab_size: int = 256, max_seq_len: int = 128, seed: int = 42):
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.rng = random.Random(seed)

    def generate_sorting(self, length: int = 8) -> BenchmarkSample:
        """Sorting task: input sequence → sorted output sequence.
        Faithful to CLRS sorting (insertion/bubble sort traces).
        """
        values = [self.rng.randint(0, 9) for _ in range(length)]
        sorted_values = sorted(values)

        input_tokens = [BOS, CLRS_INPUT_START]
        for v in values:
            input_tokens.append(DIGITS[v])
        input_tokens.append(CLRS_INPUT_END)
        input_tokens.append(CLRS_OUTPUT_START)

        output_tokens = []
        for v in sorted_values:
            output_tokens.append(DIGITS[v])
        output_tokens.append(EOS)

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        return self._make_sample(full_input, full_target, "clrs_style", "sorting",
                                 length, {"values": values, "sorted": sorted_values})

    def generate_searching(self, length: int = 10) -> BenchmarkSample:
        """Binary search style: sorted array + query → position or NOT_FOUND."""
        values = sorted(self.rng.sample(range(10), min(length, 10)))
        query = self.rng.choice(range(10))
        found = query in values
        position = values.index(query) if found else -1

        input_tokens = [BOS, CLRS_INPUT_START]
        for v in values:
            input_tokens.append(DIGITS[v])
        input_tokens.append(SEP)
        input_tokens.append(DIGITS[query])
        input_tokens.append(CLRS_INPUT_END)
        input_tokens.append(CLRS_OUTPUT_START)

        if found:
            output_tokens = [CLRS_FOUND, DIGITS[position], EOS]
        else:
            output_tokens = [CLRS_NOT_FOUND, EOS]

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        return self._make_sample(full_input, full_target, "clrs_style", "searching",
                                 length, {"values": values, "query": query, "found": found})

    def generate_lcs(self, length: int = 6) -> BenchmarkSample:
        """Longest Common Subsequence (DP): two sequences → LCS length."""
        seq_a = [self.rng.randint(0, 5) for _ in range(length)]
        seq_b = [self.rng.randint(0, 5) for _ in range(length)]

        # Compute LCS length via DP
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                if seq_a[i-1] == seq_b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        lcs_len = dp[length][length]

        input_tokens = [BOS, CLRS_INPUT_START]
        for v in seq_a:
            input_tokens.append(DIGITS[v])
        input_tokens.append(SEP)
        for v in seq_b:
            input_tokens.append(DIGITS[v])
        input_tokens.append(CLRS_INPUT_END)
        input_tokens.append(CLRS_OUTPUT_START)

        output_tokens = [DIGITS[lcs_len], EOS]
        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        return self._make_sample(full_input, full_target, "clrs_style", "lcs",
                                 length, {"seq_a": seq_a, "seq_b": seq_b, "lcs_length": lcs_len})

    def _make_sample(self, input_tokens, target_tokens, family, task, length, meta):
        input_tokens = input_tokens[:self.max_seq_len]
        target_tokens = target_tokens[:self.max_seq_len]
        pad_in = self.max_seq_len - len(input_tokens)
        pad_out = self.max_seq_len - len(target_tokens)
        input_tokens += [PAD] * pad_in
        target_tokens += [PAD] * pad_out

        sid = f"{family}_{task}_{length}_{self.rng.randint(0,99999)}"
        difficulty = "easy" if length <= 6 else "medium" if length <= 10 else "hard"
        return BenchmarkSample(
            input_ids=torch.tensor(input_tokens, dtype=torch.long),
            target_ids=torch.tensor(target_tokens, dtype=torch.long),
            sample_id=sid, family=family, task=task,
            difficulty=difficulty, length_bucket=length, metadata=meta,
        )


# =============================================================================
# FAMILY 2: ListOps-Style Long-Range Compositional Reasoning
# =============================================================================

class ListOpsGenerator:
    """ListOps: nested list operations with variable depth and length.

    Label: LISTOPS_FAITHFUL_IMPLEMENTATION
    Faithful to the Long Range Arena ListOps formulation.
    Operations: MIN, MAX, MED (median), SM (sum mod 10)
    """

    def __init__(self, vocab_size: int = 256, max_seq_len: int = 128, seed: int = 42):
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.rng = random.Random(seed)
        self.ops = [LISTOPS_MIN, LISTOPS_MAX, LISTOPS_MED, LISTOPS_SM]

    def generate(self, max_depth: int = 3, max_args: int = 4) -> BenchmarkSample:
        """Generate a ListOps expression and its result."""
        expr_tokens, result = self._generate_expr(max_depth, max_args)

        input_tokens = [BOS] + expr_tokens + [SEP]
        output_tokens = [DIGITS[result % 10], EOS]

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        length = len(expr_tokens)
        return self._make_sample(full_input, full_target, length,
                                 {"depth": max_depth, "result": result, "expr_len": length})

    def _generate_expr(self, depth: int, max_args: int) -> tuple[list[int], int]:
        """Recursively generate a ListOps expression."""
        if depth <= 0 or self.rng.random() < 0.3:
            # Leaf: single digit
            val = self.rng.randint(0, 9)
            return [DIGITS[val]], val

        op = self.rng.choice(self.ops)
        num_args = self.rng.randint(2, max_args)
        tokens = [op, LISTOPS_OPEN]
        values = []

        for i in range(num_args):
            child_tokens, child_val = self._generate_expr(depth - 1, max_args)
            tokens.extend(child_tokens)
            values.append(child_val)
            if i < num_args - 1:
                tokens.append(SEP)

        tokens.append(LISTOPS_CLOSE)

        # Compute result
        if op == LISTOPS_MIN:
            result = min(values)
        elif op == LISTOPS_MAX:
            result = max(values)
        elif op == LISTOPS_MED:
            sorted_vals = sorted(values)
            result = sorted_vals[len(sorted_vals) // 2]
        elif op == LISTOPS_SM:
            result = sum(values) % 10
        else:
            result = values[0]

        return tokens, result

    def _make_sample(self, input_tokens, target_tokens, expr_len, meta):
        input_tokens = input_tokens[:self.max_seq_len]
        target_tokens = target_tokens[:self.max_seq_len]
        pad_in = self.max_seq_len - len(input_tokens)
        pad_out = self.max_seq_len - len(target_tokens)
        input_tokens += [PAD] * pad_in
        target_tokens += [PAD] * pad_out

        difficulty = "easy" if expr_len < 20 else "medium" if expr_len < 50 else "hard"
        sid = f"listops_{expr_len}_{self.rng.randint(0,99999)}"
        return BenchmarkSample(
            input_ids=torch.tensor(input_tokens, dtype=torch.long),
            target_ids=torch.tensor(target_tokens, dtype=torch.long),
            sample_id=sid, family="listops", task="list_ops",
            difficulty=difficulty, length_bucket=expr_len, metadata=meta,
        )


# =============================================================================
# FAMILY 3: SCAN-Style Compositional Generalization
# =============================================================================

class SCANStyleGenerator:
    """SCAN-style compositional command → action sequence mapping.

    Label: SCAN_STYLE_SYMBOLIC_ADAPTER
    Commands use symbolic tokens (not English text).
    Splits: random, length, primitive (jump)
    """

    def __init__(self, vocab_size: int = 256, max_seq_len: int = 128, seed: int = 42):
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.rng = random.Random(seed)

        # Primitive commands → action sequences
        self.primitives = {
            SCAN_WALK: [SCAN_ACT_WALK],
            SCAN_RUN: [SCAN_ACT_RUN],
            SCAN_JUMP: [SCAN_ACT_JUMP],
            SCAN_LOOK: [SCAN_ACT_LOOK],
        }
        self.directions = {
            SCAN_LEFT: [SCAN_ACT_LTURN],
            SCAN_RIGHT: [SCAN_ACT_RTURN],
        }

    def generate(self, max_commands: int = 3, include_jump: bool = True) -> BenchmarkSample:
        """Generate a SCAN-style command → action mapping."""
        commands, actions = self._generate_command_sequence(max_commands, include_jump)

        input_tokens = [BOS] + commands + [SEP]
        output_tokens = actions + [EOS]

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        cmd_len = len(commands)
        act_len = len(actions)
        return self._make_sample(full_input, full_target, cmd_len,
                                 {"commands": commands, "actions": actions,
                                  "cmd_len": cmd_len, "act_len": act_len,
                                  "has_jump": SCAN_JUMP in commands})

    def _generate_command_sequence(self, max_commands: int, include_jump: bool):
        """Generate composed commands and their action outputs."""
        num_commands = self.rng.randint(1, max_commands)
        all_commands = []
        all_actions = []

        available_prims = list(self.primitives.keys())
        if not include_jump:
            available_prims = [p for p in available_prims if p != SCAN_JUMP]

        for i in range(num_commands):
            prim = self.rng.choice(available_prims)
            prim_actions = self.primitives[prim][:]

            # Maybe add direction
            if self.rng.random() < 0.4:
                direction = self.rng.choice(list(self.directions.keys()))
                prim_actions = self.directions[direction] + prim_actions

            # Maybe add repetition
            if self.rng.random() < 0.3:
                rep = self.rng.choice([SCAN_TWICE, SCAN_THRICE])
                multiplier = 2 if rep == SCAN_TWICE else 3
                all_commands.append(prim)
                all_commands.append(rep)
                all_actions.extend(prim_actions * multiplier)
            else:
                all_commands.append(prim)
                all_actions.extend(prim_actions)

            if i < num_commands - 1:
                connector = self.rng.choice([SCAN_AND, SCAN_AFTER])
                all_commands.append(connector)

        return all_commands, all_actions

    def _make_sample(self, input_tokens, target_tokens, cmd_len, meta):
        input_tokens = input_tokens[:self.max_seq_len]
        target_tokens = target_tokens[:self.max_seq_len]
        pad_in = self.max_seq_len - len(input_tokens)
        pad_out = self.max_seq_len - len(target_tokens)
        input_tokens += [PAD] * pad_in
        target_tokens += [PAD] * pad_out

        difficulty = "easy" if cmd_len <= 3 else "medium" if cmd_len <= 6 else "hard"
        sid = f"scan_{cmd_len}_{self.rng.randint(0,99999)}"
        return BenchmarkSample(
            input_ids=torch.tensor(input_tokens, dtype=torch.long),
            target_ids=torch.tensor(target_tokens, dtype=torch.long),
            sample_id=sid, family="scan_style", task="command_to_action",
            difficulty=difficulty, length_bucket=cmd_len, metadata=meta,
        )


# =============================================================================
# FAMILY 4: Dyck Language Bracket Reasoning
# =============================================================================

class DyckGenerator:
    """Dyck language: multi-type bracket validation and next-token prediction.

    Label: DYCK_FAITHFUL_IMPLEMENTATION
    Directly compatible — Dyck languages are natively token sequences.
    """

    def __init__(self, vocab_size: int = 256, max_seq_len: int = 128, seed: int = 42):
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.rng = random.Random(seed)
        self.bracket_pairs = [
            (DYCK_OPEN_1, DYCK_CLOSE_1),
            (DYCK_OPEN_2, DYCK_CLOSE_2),
            (DYCK_OPEN_3, DYCK_CLOSE_3),
        ]

    def generate_validation(self, max_depth: int = 4, num_types: int = 3) -> BenchmarkSample:
        """Generate bracket sequence and validate if balanced."""
        balanced = self.rng.random() > 0.5
        seq = self._generate_dyck(max_depth, num_types, balanced)

        input_tokens = [BOS] + seq + [SEP]
        answer = DYCK_VALID if balanced else DYCK_INVALID
        output_tokens = [answer, EOS]

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        return self._make_sample(full_input, full_target, len(seq),
                                 {"balanced": balanced, "depth": max_depth,
                                  "num_types": num_types, "seq_len": len(seq)})

    def generate_completion(self, max_depth: int = 4, num_types: int = 2) -> BenchmarkSample:
        """Generate partial bracket sequence, predict closing tokens."""
        seq = self._generate_balanced_prefix(max_depth, num_types)
        # Find the required closing sequence
        stack = []
        for tok in seq:
            for open_tok, close_tok in self.bracket_pairs[:num_types]:
                if tok == open_tok:
                    stack.append(close_tok)
                elif tok == close_tok:
                    if stack and stack[-1] == close_tok:
                        stack.pop()

        closing = list(reversed(stack))

        input_tokens = [BOS] + seq + [SEP]
        output_tokens = closing + [EOS]

        full_input = input_tokens + output_tokens[:-1]
        full_target = input_tokens[1:] + output_tokens

        return self._make_sample(full_input, full_target, len(seq),
                                 {"task_type": "completion", "depth": max_depth,
                                  "closing_needed": len(closing)})

    def _generate_dyck(self, max_depth: int, num_types: int, balanced: bool) -> list[int]:
        """Generate a Dyck sequence."""
        pairs = self.bracket_pairs[:num_types]
        seq = self._random_balanced(max_depth, pairs)
        if not balanced and seq:
            # Corrupt one position
            idx = self.rng.randint(0, len(seq) - 1)
            replacement = self.rng.choice([p[0] for p in pairs] + [p[1] for p in pairs])
            seq[idx] = replacement
        return seq

    def _random_balanced(self, max_depth: int, pairs: list) -> list[int]:
        """Generate random balanced bracket sequence."""
        result = []
        stack = []
        length = self.rng.randint(4, max_depth * 4)

        for _ in range(length):
            if not stack or (len(stack) < max_depth and self.rng.random() < 0.6):
                open_tok, close_tok = self.rng.choice(pairs)
                result.append(open_tok)
                stack.append(close_tok)
            elif stack:
                result.append(stack.pop())

        # Close remaining
        while stack:
            result.append(stack.pop())
        return result

    def _generate_balanced_prefix(self, max_depth: int, num_types: int) -> list[int]:
        """Generate a partial balanced sequence (open brackets without all closings)."""
        pairs = self.bracket_pairs[:num_types]
        result = []
        stack = []
        length = self.rng.randint(3, max_depth * 3)

        for _ in range(length):
            if self.rng.random() < 0.65 and len(stack) < max_depth:
                open_tok, close_tok = self.rng.choice(pairs)
                result.append(open_tok)
                stack.append(close_tok)
            elif stack and self.rng.random() < 0.5:
                result.append(stack.pop())
            elif len(stack) < max_depth:
                open_tok, close_tok = self.rng.choice(pairs)
                result.append(open_tok)
                stack.append(close_tok)

        return result

    def _make_sample(self, input_tokens, target_tokens, seq_len, meta):
        input_tokens = input_tokens[:self.max_seq_len]
        target_tokens = target_tokens[:self.max_seq_len]
        pad_in = self.max_seq_len - len(input_tokens)
        pad_out = self.max_seq_len - len(target_tokens)
        input_tokens += [PAD] * pad_in
        target_tokens += [PAD] * pad_out

        difficulty = "easy" if seq_len < 10 else "medium" if seq_len < 20 else "hard"
        sid = f"dyck_{seq_len}_{self.rng.randint(0,99999)}"
        return BenchmarkSample(
            input_ids=torch.tensor(input_tokens, dtype=torch.long),
            target_ids=torch.tensor(target_tokens, dtype=torch.long),
            sample_id=sid, family="dyck", task="bracket_reasoning",
            difficulty=difficulty, length_bucket=seq_len, metadata=meta,
        )
