"""Create an official-like development set without using final official files."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from benchmark.common import utc_now, write_json


EXAMPLES: dict[str, list[str]] = {
    "multiple_choice_reasoning": [
        "Question: A battery powers a lamp. Which change most likely makes the lamp dimmer? A. add resistance B. shorten wire C. use fresh battery D. close switch. Answer: A.",
        "Question: A plant in a dark closet becomes pale. Which explanation fits best? A. too much wind B. less light for chlorophyll C. more soil D. colder water. Answer: B.",
        "Question: Which object has the greatest inertia? A. feather B. tennis ball C. bicycle D. truck. Answer: D.",
        "Question: If all dax are blue and this item is a dax, what follows? A. it is blue B. it is red C. it is unknown D. it is green. Answer: A.",
    ],
    "boolean_qa": [
        "Passage: Mira locked the door before leaving. Question: Was the door unlocked when she left? Answer: no.",
        "Passage: The recipe says to bake after mixing flour and water. Question: Does baking happen before mixing? Answer: no.",
        "Passage: The package arrived on Tuesday, two days after shipment. Question: Was it shipped on Sunday? Answer: yes.",
        "Passage: Lemons are sour fruits used in drinks. Question: Are lemons usually sweet like candy? Answer: no.",
    ],
    "mathematics": [
        "Compute: 17 + 28 = 45. Therefore the final answer is 45.",
        "A box has 6 rows of 7 bolts. Total bolts: 6 * 7 = 42.",
        "If a train travels 30 miles in half an hour, its speed is 60 miles per hour.",
        "Solve for x: x + 9 = 14. Subtract 9 from both sides, x = 5.",
    ],
    "commonsense_completion": [
        "The glass fell from the table and shattered because it hit the hard floor.",
        "After walking in heavy rain, the jacket was wet and needed to dry.",
        "She put the ice cream in the freezer so that it would not melt.",
        "He whispered in the library because people nearby were reading quietly.",
    ],
    "code_generation": [
        "def add_pair(a, b):\n    return a + b\n",
        "def is_even(n):\n    return n % 2 == 0\n",
        "items = [3, 1, 2]\nitems.sort()\nprint(items)\n",
        "def count_keys(obj):\n    return len(obj.keys())\n",
    ],
    "general_knowledge": [
        "Photosynthesis lets many plants convert light, water, and carbon dioxide into sugars.",
        "A compass needle points roughly toward magnetic north because of Earth's magnetic field.",
        "The Pacific Ocean is larger than the Atlantic Ocean.",
        "Evaporation changes liquid water into water vapor.",
    ],
    "pronoun_coreference": [
        "Nora thanked Lina because she had helped with the report. In this sentence, she refers to Lina.",
        "The trophy did not fit in the suitcase because it was too large. It refers to the trophy.",
        "Omar called Ken after he finished dinner. He refers to Omar.",
        "The cabinet would not hold the binder because it was too narrow. It refers to the cabinet.",
    ],
}


def _sha(text: str) -> str:
    return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()


def _official_hashes(root: Path) -> set[str]:
    hashes: set[str] = set()
    for path in root.glob("*.jsonl"):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                hashes.add(_sha(line))
    return hashes


def run(*, output_root: str = "data/eval/official_like_dev", official_root: str = "data/eval/official_300m_bounded") -> dict[str, Any]:
    out = Path(output_root)
    out.mkdir(parents=True, exist_ok=True)
    official = _official_hashes(Path(official_root))
    rows: list[dict[str, Any]] = []
    overlaps = 0
    for category, examples in EXAMPLES.items():
        path = out / f"{category}.jsonl"
        with path.open("w", encoding="utf-8") as handle:
            for idx, text in enumerate(examples):
                line = {
                    "id": f"{category}_{idx:03d}",
                    "category": category,
                    "text": text,
                    "source": "synthetic_official_like_dev_v1",
                    "may_guide_training": True,
                    "final_official_eval": False,
                }
                serialized = json.dumps(line, sort_keys=True)
                overlaps += int(_sha(serialized) in official or _sha(text) in official)
                handle.write(serialized + "\n")
        rows.append({"category": category, "path": str(path.as_posix()), "examples": len(examples)})
    payload = {
        "schema_version": "1.0",
        "created_at": utc_now(),
        "status": "OFFICIAL_LIKE_DEVELOPMENT_SET_MATERIALIZED",
        "output_root": output_root,
        "final_official_root": official_root,
        "category_count": len(EXAMPLES),
        "example_count": sum(len(items) for items in EXAMPLES.values()),
        "categories": rows,
        "assertions": {
            "may_guide_training": True,
            "final_official_eval": False,
            "exact_line_or_text_overlap_with_final_official": overlaps,
            "no_exact_overlap_with_final_official": overlaps == 0,
        },
    }
    write_json(out / "official_like_dev_manifest.json", payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="data/eval/official_like_dev")
    parser.add_argument("--official-root", default="data/eval/official_300m_bounded")
    args = parser.parse_args()
    print(json.dumps(run(output_root=args.output_root, official_root=args.official_root), indent=2))


if __name__ == "__main__":
    main()
