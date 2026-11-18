"""Build and verify a self-contained Software Engineer runtime ZIP.

The exporter creates a temporary package, checks its complete file inventory,
and writes a new archive at the requested destination."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile

from muse_presets.engineering_pack import (
    _require_new, inspect_engineer_pack, stage_engineer_pack,
)
from muse_presets.engineer_sourcekit import export_engineer_sourcekit


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--to", required=True, type=Path,
                        help="new absolute destination .zip; existing files refused")
    args = parser.parse_args(argv)
    try:
        target = _require_new(args.to)
        if target.suffix.lower() != ".zip":
            raise ValueError("SOURCEKIT_OUTPUT_MUST_BE_ZIP")
        with tempfile.TemporaryDirectory(prefix="r56-engineer-sourcekit-") as scratch:
            pristine = Path(scratch) / "software-engineer"
            staged = stage_engineer_pack(pristine)
            if (staged["status"] != "LOCAL_ENGINE_PACK_STAGED"
                    or inspect_engineer_pack(pristine)["status"] != "LOCAL_MATCH"):
                raise ValueError("SOURCEKIT_PRISTINE_PRECONDITION_FAILED")
            report = export_engineer_sourcekit(pristine, target)
        print(json.dumps(report, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
        print(json.dumps({
            "status": "REFUSED", "reason": str(exc),
            "native_installed": False, "external_effect_authorized": False
        }, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
