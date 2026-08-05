"""CLI entry point for dense-approximation diagnostics."""

from __future__ import annotations

import argparse

from benchmark.analysis.dense_approximation import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run PVR dense-approximation diagnostics")
    parser.add_argument("--size", default="300m")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    payload = run(size=args.size, output=args.output)
    print(payload["status"])


if __name__ == "__main__":
    main()

