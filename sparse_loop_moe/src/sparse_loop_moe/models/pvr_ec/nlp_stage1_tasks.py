"""NLP Stage 1 Task Set for PVR-EC-O Family Preservation Testing.

These tasks are language-like enough to stress ambiguity, context, sequence
structure, and routing, but controlled enough to classify failures.

Tasks:
1. char_copy - Copy input character sequence
2. char_reverse - Reverse input character sequence
3. char_shift - Caesar-shift each character by fixed offset
4. bracketed_copy - Copy only content inside brackets
5. small_vocab_grammar_lm - Predict next token in S-V-O grammar
6. delimiter_memory_probe - Remember key-value pairs, answer queries
7. length_generalization_probe - Tasks at varying sequence lengths
8. ambiguous_token_context_probe - Same token, different meaning by context

Each task returns (input_ids, target_ids, metadata) where metadata includes
token_role labels for family-preservation analysis.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import random

import torch


# Token allocation within vocab 256
PAD = 0
BOS = 1
EOS = 2
SEP = 3
QUERY = 4
# Characters a-z: 5-30
CHAR_BASE = 5
NUM_CHARS = 26
# Brackets: 31-34
OPEN_BRACKET = 31
CLOSE_BRACKET = 32
OPEN_ANGLE = 33
CLOSE_ANGLE = 34
# Delimiters: 35-38
COLON = 35
COMMA = 36
EQUALS = 37
PIPE = 38
# Grammar tokens: 40-80
GRAMMAR_BASE = 40


@dataclass
class NLPStage1Sample:
    """A single NLP Stage 1 sample with role annotations."""
    input_ids: torch.Tensor
    target_ids: torch.Tensor
    task: str
    token_roles: list[str]  # per-position role label
    context_label: str = ""  # for context-sensitive tasks
    seq_len: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


def _char_to_id(c: str) -> int:
    return CHAR_BASE + ord(c) - ord('a')


def _id_to_char(i: int) -> str:
    return chr(i - CHAR_BASE + ord('a'))


# =============================================================================
# Task 1: char_copy
# =============================================================================


def generate_char_copy(
    seq_len: int = 16,
    seed: int = 42,
) -> NLPStage1Sample:
    """Copy: input is random chars, target is same chars."""
    rng = random.Random(seed)
    chars = [rng.randint(0, NUM_CHARS - 1) for _ in range(seq_len)]
    input_tokens = [BOS] + [CHAR_BASE + c for c in chars] + [SEP]
    target_tokens = [CHAR_BASE + c for c in chars] + [EOS]

    # Pad to equal length
    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens
    roles = ["bos"] + ["source"] * seq_len + ["sep"] + ["target"] * (seq_len - 1) + ["eos"]

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="char_copy",
        token_roles=roles[:len(full_input)],
        seq_len=len(full_input),
    )


# =============================================================================
# Task 2: char_reverse
# =============================================================================


def generate_char_reverse(
    seq_len: int = 16,
    seed: int = 42,
) -> NLPStage1Sample:
    """Reverse: input is random chars, target is reversed chars."""
    rng = random.Random(seed)
    chars = [rng.randint(0, NUM_CHARS - 1) for _ in range(seq_len)]
    reversed_chars = chars[::-1]

    input_tokens = [BOS] + [CHAR_BASE + c for c in chars] + [SEP]
    target_tokens = [CHAR_BASE + c for c in reversed_chars] + [EOS]

    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens
    roles = ["bos"] + ["source"] * seq_len + ["sep"] + ["target"] * (seq_len - 1) + ["eos"]

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="char_reverse",
        token_roles=roles[:len(full_input)],
        seq_len=len(full_input),
    )


# =============================================================================
# Task 3: char_shift
# =============================================================================


def generate_char_shift(
    seq_len: int = 16,
    shift: int = 3,
    seed: int = 42,
) -> NLPStage1Sample:
    """Caesar shift: each character shifted by fixed offset mod 26."""
    rng = random.Random(seed)
    chars = [rng.randint(0, NUM_CHARS - 1) for _ in range(seq_len)]
    shifted = [(c + shift) % NUM_CHARS for c in chars]

    input_tokens = [BOS] + [CHAR_BASE + c for c in chars] + [SEP]
    target_tokens = [CHAR_BASE + c for c in shifted] + [EOS]

    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens
    roles = ["bos"] + ["source"] * seq_len + ["sep"] + ["target"] * (seq_len - 1) + ["eos"]

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="char_shift",
        token_roles=roles[:len(full_input)],
        seq_len=len(full_input),
    )


# =============================================================================
# Task 4: bracketed_copy
# =============================================================================


def generate_bracketed_copy(
    content_len: int = 6,
    prefix_len: int = 4,
    suffix_len: int = 4,
    seed: int = 42,
) -> NLPStage1Sample:
    """Copy only content inside brackets: prefix [content] suffix → content."""
    rng = random.Random(seed)
    prefix = [CHAR_BASE + rng.randint(0, NUM_CHARS - 1) for _ in range(prefix_len)]
    content = [CHAR_BASE + rng.randint(0, NUM_CHARS - 1) for _ in range(content_len)]
    suffix = [CHAR_BASE + rng.randint(0, NUM_CHARS - 1) for _ in range(suffix_len)]

    input_tokens = [BOS] + prefix + [OPEN_BRACKET] + content + [CLOSE_BRACKET] + suffix + [SEP]
    target_tokens = content + [EOS]

    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens

    roles = (
        ["bos"]
        + ["prefix"] * prefix_len
        + ["open_bracket"]
        + ["content"] * content_len
        + ["close_bracket"]
        + ["suffix"] * suffix_len
        + ["sep"]
        + ["target"] * (content_len - 1)
        + ["eos"]
    )

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="bracketed_copy",
        token_roles=roles[:len(full_input)],
        seq_len=len(full_input),
    )


# =============================================================================
# Task 5: small_vocab_grammar_lm
# =============================================================================

# Simple S-V-O grammar with small vocab
SUBJECTS = list(range(GRAMMAR_BASE, GRAMMAR_BASE + 5))       # 5 subjects
VERBS = list(range(GRAMMAR_BASE + 5, GRAMMAR_BASE + 10))     # 5 verbs
OBJECTS = list(range(GRAMMAR_BASE + 10, GRAMMAR_BASE + 15))  # 5 objects
GRAMMAR_EOS = GRAMMAR_BASE + 15


def generate_small_vocab_grammar_lm(
    num_sentences: int = 4,
    seed: int = 42,
) -> NLPStage1Sample:
    """Next-token prediction on S-V-O sentences.

    Grammar: S V O [SEP] S V O [SEP] ...
    Target: predict next token given prefix.
    """
    rng = random.Random(seed)
    tokens = [BOS]
    roles = ["bos"]

    for _ in range(num_sentences):
        s = rng.choice(SUBJECTS)
        v = rng.choice(VERBS)
        o = rng.choice(OBJECTS)
        tokens.extend([s, v, o, SEP])
        roles.extend(["subject", "verb", "object", "sep"])

    tokens.append(GRAMMAR_EOS)
    roles.append("eos")

    # For LM: input is tokens[:-1], target is tokens[1:]
    input_ids = torch.tensor(tokens[:-1], dtype=torch.long)
    target_ids = torch.tensor(tokens[1:], dtype=torch.long)

    return NLPStage1Sample(
        input_ids=input_ids,
        target_ids=target_ids,
        task="small_vocab_grammar_lm",
        token_roles=roles[:-1],
        seq_len=len(tokens) - 1,
    )


# =============================================================================
# Task 6: delimiter_memory_probe
# =============================================================================


def generate_delimiter_memory_probe(
    num_pairs: int = 4,
    seed: int = 42,
) -> NLPStage1Sample:
    """Key-value memory: k1=v1|k2=v2|...|query:k2 → v2.

    Tests whether routing preserves state across delimiter boundaries.
    """
    rng = random.Random(seed)
    keys = rng.sample(range(CHAR_BASE, CHAR_BASE + NUM_CHARS), num_pairs)
    values = [CHAR_BASE + rng.randint(0, NUM_CHARS - 1) for _ in range(num_pairs)]
    query_idx = rng.randint(0, num_pairs - 1)

    # Build input: k1=v1|k2=v2|...|?k_query
    input_tokens = [BOS]
    roles = ["bos"]
    for i, (k, v) in enumerate(zip(keys, values)):
        input_tokens.extend([k, EQUALS, v])
        roles.extend(["key", "equals", "value"])
        if i < num_pairs - 1:
            input_tokens.append(PIPE)
            roles.append("delimiter")

    input_tokens.extend([QUERY, keys[query_idx]])
    roles.extend(["query_marker", "query_key"])

    # Target: the corresponding value
    target_value = values[query_idx]
    input_tokens.append(SEP)
    roles.append("sep")

    target_tokens = [target_value, EOS]
    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens
    roles_full = roles + ["target"]

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="delimiter_memory_probe",
        token_roles=roles_full[:len(full_input)],
        seq_len=len(full_input),
        metadata={"query_key": keys[query_idx], "expected_value": target_value},
    )


# =============================================================================
# Task 7: length_generalization_probe
# =============================================================================


def generate_length_generalization_probe(
    seq_len: int = 16,
    seed: int = 42,
) -> NLPStage1Sample:
    """Copy task at variable lengths — tests length generalization."""
    # Same as char_copy but parameterized for length sweeps
    return generate_char_copy(seq_len=seq_len, seed=seed)


# =============================================================================
# Task 8: ambiguous_token_context_probe
# =============================================================================

# Ambiguous tokens: same ID, different meaning based on context
AMBIG_TOKEN_RUN = CHAR_BASE + 17       # "run" - could be code or motion
AMBIG_TOKEN_BANK = CHAR_BASE + 18      # "bank" - finance or river
CONTEXT_CODE = GRAMMAR_BASE + 20       # code context marker
CONTEXT_MOTION = GRAMMAR_BASE + 21     # motion context marker
CONTEXT_FINANCE = GRAMMAR_BASE + 22    # finance context marker
CONTEXT_NATURE = GRAMMAR_BASE + 23     # nature context marker
TARGET_CODE_RUN = GRAMMAR_BASE + 24    # "execute"
TARGET_MOTION_RUN = GRAMMAR_BASE + 25  # "sprint"
TARGET_FINANCE_BANK = GRAMMAR_BASE + 26  # "account"
TARGET_NATURE_BANK = GRAMMAR_BASE + 27   # "shore"


def generate_ambiguous_token_context_probe(
    context_type: str = "code",
    seed: int = 42,
) -> NLPStage1Sample:
    """Ambiguous token must be resolved differently based on context.

    Tests: does the router route the same token differently based on context?
    """
    rng = random.Random(seed)

    if context_type == "code":
        context_marker = CONTEXT_CODE
        ambig_token = AMBIG_TOKEN_RUN
        target_token = TARGET_CODE_RUN
        context_label = "run_code"
    elif context_type == "motion":
        context_marker = CONTEXT_MOTION
        ambig_token = AMBIG_TOKEN_RUN
        target_token = TARGET_MOTION_RUN
        context_label = "run_motion"
    elif context_type == "finance":
        context_marker = CONTEXT_FINANCE
        ambig_token = AMBIG_TOKEN_BANK
        target_token = TARGET_FINANCE_BANK
        context_label = "bank_finance"
    elif context_type == "nature":
        context_marker = CONTEXT_NATURE
        ambig_token = AMBIG_TOKEN_BANK
        target_token = TARGET_NATURE_BANK
        context_label = "bank_river"
    else:
        raise ValueError(f"Unknown context type: {context_type}")

    # Build: [BOS] [context_filler...] [context_marker] [ambig_token] [SEP] → [target]
    filler_len = rng.randint(3, 8)
    filler = [CHAR_BASE + rng.randint(0, NUM_CHARS - 1) for _ in range(filler_len)]

    input_tokens = [BOS] + filler + [context_marker, ambig_token, SEP]
    target_tokens = [target_token, EOS]

    full_input = input_tokens + target_tokens[:-1]
    full_target = input_tokens[1:] + target_tokens
    roles = (
        ["bos"]
        + ["filler"] * filler_len
        + ["context_marker", "ambiguous_token", "sep"]
        + ["target"]
    )

    return NLPStage1Sample(
        input_ids=torch.tensor(full_input, dtype=torch.long),
        target_ids=torch.tensor(full_target, dtype=torch.long),
        task="ambiguous_token_context_probe",
        token_roles=roles[:len(full_input)],
        context_label=context_label,
        seq_len=len(full_input),
        metadata={"context_type": context_type, "ambig_token": ambig_token},
    )


# =============================================================================
# Batch Generation
# =============================================================================


def generate_nlp_stage1_batch(
    task: str,
    batch_size: int = 32,
    seq_len: int = 16,
    max_seq_len: int = 64,
    seed: int = 42,
) -> tuple[torch.Tensor, torch.Tensor, list[dict[str, Any]]]:
    """Generate a padded batch for a given NLP Stage 1 task.

    Returns (input_ids, target_ids, sample_metadata) where:
    - input_ids: [batch_size, max_seq_len]
    - target_ids: [batch_size, max_seq_len]
    - sample_metadata: list of per-sample metadata dicts
    """
    generators = {
        "char_copy": lambda s: generate_char_copy(seq_len=seq_len, seed=s),
        "char_reverse": lambda s: generate_char_reverse(seq_len=seq_len, seed=s),
        "char_shift": lambda s: generate_char_shift(seq_len=seq_len, seed=s),
        "bracketed_copy": lambda s: generate_bracketed_copy(seed=s),
        "small_vocab_grammar_lm": lambda s: generate_small_vocab_grammar_lm(seed=s),
        "delimiter_memory_probe": lambda s: generate_delimiter_memory_probe(seed=s),
        "length_generalization_probe": lambda s: generate_length_generalization_probe(seq_len=seq_len, seed=s),
        "ambiguous_token_context_probe": lambda s: generate_ambiguous_token_context_probe(
            context_type=["code", "motion", "finance", "nature"][s % 4], seed=s
        ),
    }

    if task not in generators:
        raise ValueError(f"Unknown NLP Stage 1 task: {task}. Available: {list(generators.keys())}")

    gen_fn = generators[task]
    samples = [gen_fn(seed + i) for i in range(batch_size)]

    # Pad to max_seq_len
    input_batch = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    target_batch = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    metadata_list = []

    for i, sample in enumerate(samples):
        inp_len = min(sample.input_ids.shape[0], max_seq_len)
        tgt_len = min(sample.target_ids.shape[0], max_seq_len)
        input_batch[i, :inp_len] = sample.input_ids[:inp_len]
        target_batch[i, :tgt_len] = sample.target_ids[:tgt_len]
        metadata_list.append({
            "task": sample.task,
            "token_roles": sample.token_roles[:inp_len],
            "context_label": sample.context_label,
            "seq_len": sample.seq_len,
        })

    return input_batch, target_batch, metadata_list


NLP_STAGE1_TASKS = (
    "char_copy",
    "char_reverse",
    "char_shift",
    "bracketed_copy",
    "small_vocab_grammar_lm",
    "delimiter_memory_probe",
    "length_generalization_probe",
    "ambiguous_token_context_probe",
)
