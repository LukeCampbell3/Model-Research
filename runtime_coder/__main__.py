"""Allow running as python -m runtime_coder."""

from runtime_coder.cli import main
import sys

if __name__ == "__main__":
    sys.exit(main())
