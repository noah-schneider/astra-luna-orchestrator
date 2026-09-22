#!/usr/bin/env python3
"""Check the native Codex configuration without making model requests."""
from __future__ import annotations
import argparse
import json
import sys
sys.dont_write_bytecode = True
from local_config import SetupError, default_locations, inspect


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home")
    parser.add_argument("--codex-home")
    parser.add_argument("--profile")
    args = parser.parse_args()
    try:
        home, codex_home = default_locations(args.home, args.codex_home)
        report = inspect(home, codex_home, args.profile)
        print(json.dumps(report, indent=2))
        return 0
    except SetupError as exc:
        print(f"CHECK FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
