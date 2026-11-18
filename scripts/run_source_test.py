#!/usr/bin/env python3
"""Run one advertised local source test without an installed package.

This explicit command runs source regressions only. The journey planner itself
does not invoke it or authorize native provider actions.
"""
import argparse
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from hub_journeys import TESTS


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run one reviewed Muse Hub source test")
    parser.add_argument("test_file", choices=sorted({Path(path).name for path in TESTS.values()}))
    args = parser.parse_args(argv)
    sys.path.insert(0, str(ROOT / "src"))
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern=args.test_file)
    if suite.countTestCases() == 0:
        print("SOURCE_TESTS_MISSING", file=sys.stderr)
        return 2
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
