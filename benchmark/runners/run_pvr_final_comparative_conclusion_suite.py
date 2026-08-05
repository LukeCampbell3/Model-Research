"""CLI for the final PVR comparative conclusion suite."""

from __future__ import annotations

import argparse

from benchmark.analysis.pvr_final_comparative_conclusion import DEFAULT_OUTPUT, build_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the final PVR comparative conclusion report.")
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--use-existing", action="store_true", help="Use existing valid reports; this is the default behavior.")
    parser.add_argument("--rerun-300m-scaffold", action="store_true", help="Reserved; reruns are intentionally not implicit.")
    parser.add_argument("--rerun-700m-frontier", action="store_true", help="Reserved; reruns are intentionally not implicit.")
    parser.add_argument("--rerun-causality", action="store_true", help="Reserved; reruns are intentionally not implicit.")
    parser.add_argument("--rerun-descriptor-deployment", action="store_true", help="Reserved; reruns are intentionally not implicit.")
    parser.add_argument("--seeds", nargs="+", default=["42", "123"])
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--fail-on-missing-required", action="store_true")
    parser.add_argument("--allow-partial", action="store_true")
    args = parser.parse_args()

    report = build_report(
        args.output,
        seeds=args.seeds,
        use_existing=True,
        strict=args.strict,
        fail_on_missing_required=args.fail_on_missing_required,
        allow_partial=args.allow_partial or not args.strict,
    )
    print(report["final_conclusion"]["strongest_supported_local_story"])
    print(f"json={report['json_report_path']}")
    print(f"markdown={report['markdown_report_path']}")


if __name__ == "__main__":
    main()

