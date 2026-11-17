"""Export or verify a source-pinned, offline-only Family Link handoff ZIP."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from muse_presets.family_sourcekit import (
    FamilySourcekitError, export_family_sourcekit, verify_family_sourcekit,
)

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--to", type=Path, help="new ZIP destination; no overwrite")
    mode.add_argument("--verify", type=Path, help="existing ZIP file to check")
    parser.add_argument("--sha256", help="trusted external ZIP SHA-256, mandatory for verification")
    options = parser.parse_args(argv)
    try:
        if options.to is not None:
            if options.sha256 is not None:
                raise FamilySourcekitError("ZIP_PIN_ONLY_ACCEPTED_DURING_VERIFY")
            result = export_family_sourcekit(ROOT, options.to)
        else:
            if options.sha256 is None:
                raise FamilySourcekitError("EXTERNAL_ZIP_SHA256_REQUIRED")
            result = verify_family_sourcekit(options.verify, options.sha256)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (FamilySourcekitError, FileExistsError, FileNotFoundError, OSError) as exc:
        print(json.dumps({
            "status": "REFUSED",
            "reason": type(exc).__name__ + ":" + str(exc)[:200],
            "native_installed": False,
            "effect_authorized": False,
        }, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
