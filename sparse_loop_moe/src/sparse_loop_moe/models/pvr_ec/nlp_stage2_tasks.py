"""NLP Stage 2 Tasks: Controlled Language-Structure Generalization.

8 tasks testing composition, dependency, negation, ambiguity, coreference,
instruction-following, multi-sentence memory, and paraphrase invariance.
"""

from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import Any
import torch

# Vocab layout (within 256)
PAD, BOS, EOS, SEP = 0, 1, 2, 3
QUERY = 4
COLON, PIPE, EQUALS, ARROW = 5, 6, 7, 8
NOT_TOKEN = 9
# Words: 10-99 (small controlled vocab)
W_THE, W_A = 10, 11
W_CAT, W_DOG, W_FOX, W_BIRD, W_ROBOT, W_BOX = 12, 13, 14, 15, 16, 17
W_KEY, W_DOOR, W_MAP, W_PATH, W_TOOL, W_LIGHT = 18, 19, 20, 21, 22, 23
W_RED, W_BLUE, W_SMALL, W_BIG, W_OLD, W_NEW = 24, 25, 26, 27, 28, 29
W_RUNS, W_SEES, W_MOVES, W_OPENS, W_FINDS, W_FIXES = 30, 31, 32, 33, 34, 35
W_RUN, W_SIT, W_IS, W_ARE, W_HAS, W_HAVE = 36, 37, 38, 39, 40, 41
W_ON, W_IN, W_OPEN, W_CLOSED, W_ALICE, W_BOB = 42, 43, 44, 45, 46, 47
W_SHE, W_HE, W_IT, W_CATS, W_DOGS, W_ROBOTS = 48, 49, 50, 51, 52, 53
W_BANK, W_MOUSE, W_PROGRAM, W_RIVER, W_MONEY, W_CHEESE = 54, 55, 56, 57, 58, 59
W_ICON, W_CLICK, W_FAST, W_HOLDS, W_EATS, W_NEAR = 60, 61, 62, 63, 64, 65
# Instructions: 70-79
W_COPY, W_REVERSE, W_SHIFT, W_REPEAT = 70, 71, 72, 73
# Generic char tokens: 80-105
CHAR_A = 80  # a=80, b=81, ..., z=105

SUBJECTS = [W_CAT, W_DOG, W_FOX, W_BIRD, W_ROBOT]
ADJECTIVES = [W_RED, W_BLUE, W_SMALL, W_BIG, W_OLD, W_NEW]
OBJECTS = [W_BOX, W_KEY, W_DOOR, W_MAP, W_PATH, W_TOOL]
VERBS = [W_RUNS, W_SEES, W_MOVES, W_OPENS, W_FINDS, W_FIXES]

NLP_STAGE2_TASKS = (
    "compositional_grammar",
    "agreement_dependency",
    "negation_polarity",
    "ambiguous_word_sense",
    "coreference_memory",
    "instruction_micro",
    "multisentence_delimiter",
    "paraphrase_invariance",
)


def generate_stage2_batch(task: str, batch_size: int = 32, seq_len: int = 32,
                          max_seq_len: int = 64, seed: int = 42
                          ) -> tuple[torch.Tensor, torch.Tensor, list[dict]]:
    """Generate padded batch for an NLP Stage 2 task."""
    generators = {
        "compositional_grammar": _gen_compositional_grammar,
        "agreement_dependency": _gen_agreement_dependency,
        "negation_polarity": _gen_negation_polarity,
        "ambiguous_word_sense": _gen_ambiguous_word_sense,
        "coreference_memory": _gen_coreference_memory,
        "instruction_micro": _gen_instruction_micro,
        "multisentence_delimiter": _gen_multisentence_delimiter,
        "paraphrase_invariance": _gen_paraphrase_invariance,
    }
    if task not in generators:
        raise ValueError(f"Unknown Stage 2 task: {task}")

    gen = generators[task]
    inputs, targets, metas = [], [], []
    for i in range(batch_size):
        inp, tgt, meta = gen(seed + i)
        inputs.append(inp)
        targets.append(tgt)
        metas.append(meta)

    # Pad
    x = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    y = torch.zeros(batch_size, max_seq_len, dtype=torch.long)
    for i, (inp, tgt) in enumerate(zip(inputs, targets)):
        n = min(len(inp), max_seq_len)
        x[i, :n] = torch.tensor(inp[:n], dtype=torch.long)
        m = min(len(tgt), max_seq_len)
        y[i, :m] = torch.tensor(tgt[:m], dtype=torch.long)
    return x, y, metas


# === Task Generators ===

def _gen_compositional_grammar(seed):
    """det adj noun verb det noun -> next token prediction."""
    rng = random.Random(seed)
    det1 = rng.choice([W_THE, W_A])
    adj = rng.choice(ADJECTIVES)
    subj = rng.choice(SUBJECTS)
    verb = rng.choice(VERBS)
    det2 = rng.choice([W_THE, W_A])
    obj = rng.choice(OBJECTS)
    tokens = [BOS, det1, adj, subj, verb, det2, obj, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    roles = ["bos", "determiner", "adjective", "subject", "verb", "determiner", "object"]
    return inp, tgt, {"task": "compositional_grammar", "roles": roles}


def _gen_agreement_dependency(seed):
    """Singular/plural agreement: the cat runs / the cats run."""
    rng = random.Random(seed)
    singular = rng.choice([True, False])
    if singular:
        subj = rng.choice([W_CAT, W_DOG, W_FOX, W_ROBOT])
        verb = W_RUNS if rng.random() > 0.5 else W_IS
    else:
        subj = rng.choice([W_CATS, W_DOGS, W_ROBOTS])
        verb = W_RUN if rng.random() > 0.5 else W_ARE
    tokens = [BOS, W_THE, subj, verb, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "agreement_dependency", "singular": singular}


def _gen_negation_polarity(seed):
    """the door is [not] open -> polarity classification via next token."""
    rng = random.Random(seed)
    negated = rng.choice([True, False])
    subj = rng.choice([W_DOOR, W_LIGHT, W_BOX])
    state = rng.choice([W_OPEN, W_CLOSED])
    if negated:
        tokens = [BOS, W_THE, subj, W_IS, NOT_TOKEN, state, EOS]
    else:
        tokens = [BOS, W_THE, subj, W_IS, state, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "negation_polarity", "negated": negated}


def _gen_ambiguous_word_sense(seed):
    """Same token (bank/mouse/run) with context -> different next token."""
    rng = random.Random(seed)
    sense = rng.choice(["bank_river", "bank_money", "mouse_animal", "mouse_device",
                        "run_code", "run_motion"])
    if sense == "bank_river":
        tokens = [BOS, W_NEAR, W_RIVER, W_BANK, SEP, W_RIVER, EOS]
    elif sense == "bank_money":
        tokens = [BOS, W_HOLDS, W_MONEY, W_BANK, SEP, W_MONEY, EOS]
    elif sense == "mouse_animal":
        tokens = [BOS, W_SMALL, W_MOUSE, W_EATS, W_CHEESE, SEP, W_CHEESE, EOS]
    elif sense == "mouse_device":
        tokens = [BOS, W_CLICK, W_MOUSE, W_ICON, SEP, W_ICON, EOS]
    elif sense == "run_code":
        tokens = [BOS, W_RUN, W_PROGRAM, SEP, W_PROGRAM, EOS]
    else:  # run_motion
        tokens = [BOS, W_RUN, W_FAST, SEP, W_FAST, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "ambiguous_word_sense", "sense": sense}


def _gen_coreference_memory(seed):
    """Entity intro + pronoun resolution: Alice has key. She opens door."""
    rng = random.Random(seed)
    entity = rng.choice([(W_ALICE, W_SHE), (W_BOB, W_HE), (W_ROBOT, W_IT)])
    name, pronoun = entity
    obj1 = rng.choice([W_KEY, W_MAP, W_TOOL])
    verb2 = rng.choice([W_OPENS, W_FINDS, W_FIXES])
    obj2 = rng.choice([W_DOOR, W_PATH, W_BOX])
    tokens = [BOS, name, W_HAS, obj1, SEP, pronoun, verb2, obj2, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "coreference_memory", "entity": name, "pronoun": pronoun}


def _gen_instruction_micro(seed):
    """instruction: content -> transformed output."""
    rng = random.Random(seed)
    content = [CHAR_A + rng.randint(0, 5) for _ in range(4)]
    instruction = rng.choice(["copy", "reverse", "shift", "repeat"])
    if instruction == "copy":
        instr_tok = W_COPY
        output = content[:]
    elif instruction == "reverse":
        instr_tok = W_REVERSE
        output = content[::-1]
    elif instruction == "shift":
        instr_tok = W_SHIFT
        output = [((c - CHAR_A + 1) % 6) + CHAR_A for c in content]
    else:  # repeat
        instr_tok = W_REPEAT
        output = content + content
    tokens = [BOS, instr_tok, COLON] + content + [ARROW] + output + [EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "instruction_micro", "instruction": instruction}


def _gen_multisentence_delimiter(seed):
    """key:value pairs with query -> recall."""
    rng = random.Random(seed)
    num_pairs = rng.randint(2, 4)
    keys = rng.sample(range(CHAR_A, CHAR_A + 10), num_pairs)
    values = [CHAR_A + rng.randint(10, 20) for _ in range(num_pairs)]
    query_idx = rng.randint(0, num_pairs - 1)

    tokens = [BOS]
    for i, (k, v) in enumerate(zip(keys, values)):
        tokens.extend([k, COLON, v])
        if i < num_pairs - 1:
            tokens.append(PIPE)
    tokens.extend([SEP, QUERY, keys[query_idx], ARROW, values[query_idx], EOS])
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "multisentence_delimiter", "answer": values[query_idx]}


def _gen_paraphrase_invariance(seed):
    """Two surface forms, same meaning -> same next token."""
    rng = random.Random(seed)
    form = rng.choice(["active", "passive"])
    subj = rng.choice(SUBJECTS)
    verb = rng.choice([W_MOVES, W_SEES, W_FINDS])
    obj = rng.choice(OBJECTS)
    if form == "active":
        tokens = [BOS, W_THE, subj, verb, W_THE, obj, EOS]
    else:
        # Passive: the obj is verb-ed by the subj (simplified)
        tokens = [BOS, W_THE, obj, W_IS, verb, W_THE, subj, EOS]
    inp = tokens[:-1]
    tgt = tokens[1:]
    return inp, tgt, {"task": "paraphrase_invariance", "form": form}
