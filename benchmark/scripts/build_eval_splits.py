"""Build or refresh evaluation splits for the genuine benchmark data layer."""

from __future__ import annotations

from benchmark.scripts.prepare_real_data import run as prepare_real_data


def main() -> None:
    payload = prepare_real_data()
    print(payload["status"])


if __name__ == "__main__":
    main()
