#!/usr/bin/env python3
"""Run a named Muse Hub test from the project checkout."""
import argparse
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from hub_journeys import load_features


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    test_files = {Path(path).name for feature in load_features(ROOT) for path in feature["tests"]}
    parser.add_argument("test_file", choices=sorted(test_files))
    args = parser.parse_args(argv)
    sys.path.insert(0, str(ROOT / "src"))
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern=args.test_file)
    if suite.countTestCases() == 0:
        print("SOURCE_TESTS_MISSING", file=sys.stderr)
        return 2
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
