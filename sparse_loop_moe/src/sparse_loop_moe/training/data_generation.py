"""Synthetic data generation for Stage A and Stage B tasks.

Stage A: Synthetic Algorithmic Tasks
- addition with distractors
- sorting small lists
- parentheses matching
- multi-hop lookup
- path finding
- rule induction
- hidden constraint tasks
- noisy instruction tasks

Stage B: Toy Coding Transformation Tasks
- unsafe SQL → parameterized query
- sync API → async API
- buggy cache → correct LRU cache
- REST → GraphQL schema
- insecure auth → safer auth flow
- legacy function → typed modular version

Each task includes metadata for:
- uncertainty level
- ambiguity level
- risk level
- hidden constraints
- expected difficulty
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any

import torch


@dataclass
class TaskSample:
    """A single task sample with metadata."""

    input_ids: torch.Tensor
    target_ids: torch.Tensor
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def uncertainty(self) -> float:
        return self.metadata.get("uncertainty", 0.5)

    @property
    def ambiguity(self) -> float:
        return self.metadata.get("ambiguity", 0.5)

    @property
    def risk(self) -> float:
        return self.metadata.get("risk", 0.5)

    @property
    def has_hidden_constraints(self) -> bool:
        return self.metadata.get("has_hidden_constraints", False)

    @property
    def difficulty(self) -> str:
        return self.metadata.get("difficulty", "medium")


class SyntheticTaskGenerator:
    """Generates synthetic algorithmic tasks (Stage A).

    All tasks have automatic correctness labels and controlled
    uncertainty/ambiguity/risk levels.
    """

    def __init__(
        self,
        vocab_size: int = 512,
        max_seq_len: int = 256,
        seed: int = 42,
    ):
        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.rng = random.Random(seed)

        # Reserve special tokens
        self.PAD = 0
        self.BOS = 1
        self.EOS = 2
        self.SEP = 3
        self.NUM_SPECIAL = 4

    def generate_addition_task(
        self,
        num_digits: int = 3,
        num_distractors: int = 0,
        ambiguous: bool = False,
    ) -> TaskSample:
        """Generate an addition task with optional distractors.

        Example: "12 + 34 = 46"
        With distractors: "12 + 34 [noise tokens] = 46"
        """
        max_val = 10**num_digits - 1
        a = self.rng.randint(0, max_val)
        b = self.rng.randint(0, max_val)
        result = a + b

        # Encode numbers as token sequences
        a_tokens = self._encode_number(a)
        b_tokens = self._encode_number(b)
        result_tokens = self._encode_number(result)

        # Add operator tokens
        PLUS = self.NUM_SPECIAL + 10  # After digit tokens
        EQUALS = self.NUM_SPECIAL + 11

        input_seq = [self.BOS] + a_tokens + [PLUS] + b_tokens

        # Add distractors
        if num_distractors > 0:
            distractors = [
                self.rng.randint(self.NUM_SPECIAL + 20, self.vocab_size - 1)
                for _ in range(num_distractors)
            ]
            input_seq.extend(distractors)

        input_seq.append(EQUALS)
        target_seq = input_seq[1:] + result_tokens + [self.EOS]
        input_seq = input_seq + result_tokens

        # Pad to max_seq_len
        input_seq, target_seq = self._pad_sequences(input_seq, target_seq)

        metadata = {
            "task_type": "addition",
            "difficulty": "easy" if num_digits <= 2 else "medium" if num_digits <= 4 else "hard",
            "uncertainty": 0.1 + 0.1 * num_distractors,
            "ambiguity": 0.5 if ambiguous else 0.1,
            "risk": 0.1,
            "has_hidden_constraints": False,
            "num_distractors": num_distractors,
        }

        return TaskSample(
            input_ids=torch.tensor(input_seq, dtype=torch.long),
            target_ids=torch.tensor(target_seq, dtype=torch.long),
            metadata=metadata,
        )

    def generate_sorting_task(
        self, list_length: int = 5, value_range: int = 50
    ) -> TaskSample:
        """Generate a sorting task.

        Example: "3 1 4 1 5 → 1 1 3 4 5"
        """
        values = [self.rng.randint(0, value_range) for _ in range(list_length)]
        sorted_values = sorted(values)

        input_tokens = [self.BOS]
        for v in values:
            input_tokens.extend(self._encode_number(v))
            input_tokens.append(self.SEP)

        ARROW = self.NUM_SPECIAL + 12
        input_tokens.append(ARROW)

        target_tokens = []
        for v in sorted_values:
            target_tokens.extend(self._encode_number(v))
            target_tokens.append(self.SEP)
        target_tokens.append(self.EOS)

        full_input = input_tokens + target_tokens[:-1]
        full_target = input_tokens[1:] + target_tokens

        full_input, full_target = self._pad_sequences(full_input, full_target)

        metadata = {
            "task_type": "sorting",
            "difficulty": "easy" if list_length <= 3 else "medium" if list_length <= 6 else "hard",
            "uncertainty": 0.1,
            "ambiguity": 0.1,
            "risk": 0.2,
            "has_hidden_constraints": False,
            "list_length": list_length,
        }

        return TaskSample(
            input_ids=torch.tensor(full_input, dtype=torch.long),
            target_ids=torch.tensor(full_target, dtype=torch.long),
            metadata=metadata,
        )

    def generate_parentheses_task(
        self, max_depth: int = 4, include_noise: bool = False
    ) -> TaskSample:
        """Generate a parentheses matching/validation task.

        Input: sequence of brackets
        Target: 1 if balanced, 0 if not
        """
        balanced = self.rng.random() > 0.5
        seq = self._generate_bracket_sequence(max_depth, balanced)

        OPEN = self.NUM_SPECIAL + 13
        CLOSE = self.NUM_SPECIAL + 14
        TRUE_TOK = self.NUM_SPECIAL + 15
        FALSE_TOK = self.NUM_SPECIAL + 16

        input_tokens = [self.BOS]
        for ch in seq:
            input_tokens.append(OPEN if ch == "(" else CLOSE)

        if include_noise:
            noise_count = self.rng.randint(1, 3)
            noise = [
                self.rng.randint(self.NUM_SPECIAL + 20, self.vocab_size - 1)
                for _ in range(noise_count)
            ]
            input_tokens.extend(noise)

        input_tokens.append(self.SEP)
        answer_token = TRUE_TOK if balanced else FALSE_TOK
        input_tokens.append(answer_token)

        target_tokens = input_tokens[1:] + [self.EOS]

        input_tokens, target_tokens = self._pad_sequences(input_tokens, target_tokens)

        metadata = {
            "task_type": "parentheses",
            "difficulty": "easy" if max_depth <= 2 else "medium" if max_depth <= 4 else "hard",
            "uncertainty": 0.2 if include_noise else 0.1,
            "ambiguity": 0.1,
            "risk": 0.3,
            "has_hidden_constraints": include_noise,
            "balanced": balanced,
        }

        return TaskSample(
            input_ids=torch.tensor(input_tokens, dtype=torch.long),
            target_ids=torch.tensor(target_tokens, dtype=torch.long),
            metadata=metadata,
        )

    def generate_multi_hop_lookup(
        self, num_hops: int = 3, table_size: int = 10
    ) -> TaskSample:
        """Generate a multi-hop lookup task.

        Creates a lookup table and a query that requires following
        multiple references to find the answer.
        """
        # Create lookup table: key -> value (some values are keys to other entries)
        table: dict[int, int] = {}
        keys = self.rng.sample(range(20, 20 + table_size * 2), table_size)

        # Create chain
        chain = self.rng.sample(keys, min(num_hops + 1, len(keys)))
        for i in range(len(chain) - 1):
            table[chain[i]] = chain[i + 1]

        # Final answer
        final_answer = self.rng.randint(100, 200)
        table[chain[-1]] = final_answer

        # Fill remaining entries with random values
        for k in keys:
            if k not in table:
                table[k] = self.rng.randint(100, 200)

        # Encode: table entries followed by query
        MAP_TOK = self.NUM_SPECIAL + 17
        QUERY_TOK = self.NUM_SPECIAL + 18

        input_tokens = [self.BOS]
        for k, v in table.items():
            input_tokens.extend(self._encode_number(k))
            input_tokens.append(MAP_TOK)
            input_tokens.extend(self._encode_number(v))
            input_tokens.append(self.SEP)

        input_tokens.append(QUERY_TOK)
        input_tokens.extend(self._encode_number(chain[0]))
        input_tokens.append(self.SEP)

        answer_tokens = self._encode_number(final_answer) + [self.EOS]
        full_input = input_tokens + answer_tokens[:-1]
        full_target = input_tokens[1:] + answer_tokens

        full_input, full_target = self._pad_sequences(full_input, full_target)

        metadata = {
            "task_type": "multi_hop_lookup",
            "difficulty": "easy" if num_hops <= 2 else "medium" if num_hops <= 4 else "hard",
            "uncertainty": 0.2 + 0.1 * num_hops,
            "ambiguity": 0.2,
            "risk": 0.3,
            "has_hidden_constraints": False,
            "num_hops": num_hops,
        }

        return TaskSample(
            input_ids=torch.tensor(full_input, dtype=torch.long),
            target_ids=torch.tensor(full_target, dtype=torch.long),
            metadata=metadata,
        )

    def generate_hidden_constraint_task(self) -> TaskSample:
        """Generate a task with hidden constraints.

        The task appears simple but has an unstated rule that must be
        discovered from the pattern of examples.
        """
        # Hidden rule: output is input * 2, BUT if input > 50, output is input - 10
        threshold = 50
        num_examples = 4

        input_tokens = [self.BOS]
        for _ in range(num_examples):
            val = self.rng.randint(1, 100)
            if val > threshold:
                result = val - 10
            else:
                result = val * 2
            input_tokens.extend(self._encode_number(val))
            input_tokens.append(self.SEP)
            input_tokens.extend(self._encode_number(result))
            input_tokens.append(self.SEP)

        # Query
        QUERY_TOK = self.NUM_SPECIAL + 18
        query_val = self.rng.randint(1, 100)
        if query_val > threshold:
            answer = query_val - 10
        else:
            answer = query_val * 2

        input_tokens.append(QUERY_TOK)
        input_tokens.extend(self._encode_number(query_val))
        input_tokens.append(self.SEP)

        answer_tokens = self._encode_number(answer) + [self.EOS]
        full_input = input_tokens + answer_tokens[:-1]
        full_target = input_tokens[1:] + answer_tokens

        full_input, full_target = self._pad_sequences(full_input, full_target)

        metadata = {
            "task_type": "hidden_constraint",
            "difficulty": "hard",
            "uncertainty": 0.7,
            "ambiguity": 0.6,
            "risk": 0.5,
            "has_hidden_constraints": True,
            "hidden_rule": f"if x > {threshold}: x - 10, else: x * 2",
        }

        return TaskSample(
            input_ids=torch.tensor(full_input, dtype=torch.long),
            target_ids=torch.tensor(full_target, dtype=torch.long),
            metadata=metadata,
        )

    def generate_batch(
        self,
        batch_size: int = 32,
        task_mix: dict[str, float] | None = None,
    ) -> list[TaskSample]:
        """Generate a batch of mixed tasks.

        Args:
            batch_size: Number of samples
            task_mix: Dictionary of task_type -> probability
        """
        if task_mix is None:
            task_mix = {
                "addition": 0.2,
                "addition_distractor": 0.1,
                "sorting": 0.2,
                "parentheses": 0.15,
                "multi_hop": 0.2,
                "hidden_constraint": 0.15,
            }

        tasks = list(task_mix.keys())
        weights = list(task_mix.values())
        batch = []

        for _ in range(batch_size):
            task_type = self.rng.choices(tasks, weights=weights, k=1)[0]

            if task_type == "addition":
                sample = self.generate_addition_task(
                    num_digits=self.rng.randint(1, 4)
                )
            elif task_type == "addition_distractor":
                sample = self.generate_addition_task(
                    num_digits=self.rng.randint(2, 4),
                    num_distractors=self.rng.randint(1, 5),
                )
            elif task_type == "sorting":
                sample = self.generate_sorting_task(
                    list_length=self.rng.randint(3, 8)
                )
            elif task_type == "parentheses":
                sample = self.generate_parentheses_task(
                    max_depth=self.rng.randint(2, 6),
                    include_noise=self.rng.random() > 0.5,
                )
            elif task_type == "multi_hop":
                sample = self.generate_multi_hop_lookup(
                    num_hops=self.rng.randint(2, 5)
                )
            elif task_type == "hidden_constraint":
                sample = self.generate_hidden_constraint_task()
            else:
                sample = self.generate_addition_task()

            batch.append(sample)

        return batch

    def _encode_number(self, n: int) -> list[int]:
        """Encode a number as a sequence of digit tokens."""
        digits = str(abs(n))
        return [self.NUM_SPECIAL + int(d) for d in digits]

    def _pad_sequences(
        self, input_seq: list[int], target_seq: list[int]
    ) -> tuple[list[int], list[int]]:
        """Pad sequences to max_seq_len."""
        # Truncate if too long
        input_seq = input_seq[: self.max_seq_len]
        target_seq = target_seq[: self.max_seq_len]

        # Pad
        input_pad = self.max_seq_len - len(input_seq)
        target_pad = self.max_seq_len - len(target_seq)

        input_seq = input_seq + [self.PAD] * input_pad
        target_seq = target_seq + [self.PAD] * target_pad

        return input_seq, target_seq

    def _generate_bracket_sequence(
        self, max_depth: int, balanced: bool
    ) -> str:
        """Generate a bracket sequence."""
        if balanced:
            seq = self._random_balanced_brackets(max_depth)
        else:
            seq = self._random_balanced_brackets(max_depth)
            # Corrupt it
            idx = self.rng.randint(0, len(seq) - 1)
            seq = seq[:idx] + (")" if seq[idx] == "(" else "(") + seq[idx + 1:]
        return seq

    def _random_balanced_brackets(self, max_depth: int) -> str:
        """Generate random balanced brackets."""
        result = []
        depth = 0
        length = self.rng.randint(2, max_depth * 2)

        for _ in range(length):
            if depth == 0:
                result.append("(")
                depth += 1
            elif depth >= max_depth:
                result.append(")")
                depth -= 1
            else:
                if self.rng.random() > 0.5:
                    result.append("(")
                    depth += 1
                else:
                    result.append(")")
                    depth -= 1

        # Close remaining
        while depth > 0:
            result.append(")")
            depth -= 1

        return "".join(result)
