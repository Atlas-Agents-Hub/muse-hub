"""Admit Muse Hub captures and the mark by reviewed hash and geometry."""
from __future__ import annotations

import json
from pathlib import Path
import re

from .site_social import valid_social_card

# These are previously recorded browser screenshots of the actual Muse Planner,
# not synthesized interface imagery. The reviewed website inventory pins bytes.
PRODUCT_CAPTURE_SPECS = {
    "hub/site/planner-desktop.png": (980, 745),
    "hub/site/planner-mobile.png": (390, 490),
    "hub/site/muse-mark.png": (384, 384),
}

def reviewed_product_capture_digests(root: Path) -> dict[str, str]:
    """Resolve explicit reviewed PNG bytes; absent pair is permitted in test fixtures."""
    root = Path(root)
    if not any((root / path).exists() or (root / path).is_symlink()
               for path in PRODUCT_CAPTURE_SPECS):
        return {}
    inventory = json.loads((root / "hub/site/INTEGRITY.json").read_text(encoding="utf8"))
    if inventory.get("schema") != "muse-hub/public-website-overlay/v1":
        raise ValueError("PRODUCT_CAPTURE_INVENTORY_SCHEMA")
    entries = inventory.get("files")
    if not isinstance(entries, dict):
        raise ValueError("PRODUCT_CAPTURE_INVENTORY_INVALID")
    digests: dict[str,str] = {}
    for path, dimensions in PRODUCT_CAPTURE_SPECS.items():
        image = root / path
        if not image.is_file() or image.is_symlink():
            raise ValueError("PRODUCT_CAPTURE_MISSING_OR_UNSAFE")
        name = path.removeprefix("hub/site/")
        row = entries.get(name)
        if not isinstance(row, dict):
            raise ValueError("PRODUCT_CAPTURE_NOT_IN_INVENTORY")
        digest = row.get("sha256")
        if (not isinstance(digest,str) or not re.fullmatch(r"[a-f0-9]{64}",digest)
            or type(row.get("bytes")) is not int or row["bytes"]<1):
            raise ValueError("PRODUCT_CAPTURE_INVENTORY_HASH_INVALID")
        raw = image.read_bytes()
        if len(raw) != row["bytes"] or not valid_social_card(raw,digest,dimensions=dimensions):
            raise ValueError("PRODUCT_CAPTURE_BYTES_MISMATCH")
        digests[path] = digest
    return digests

def valid_product_capture(path: str, data: bytes, digest: str | None) -> bool:
    """Fail closed for a changed, malformed, oversized or wrongly sized capture."""
    dimensions = PRODUCT_CAPTURE_SPECS.get(path)
    return dimensions is not None and valid_social_card(data,digest,dimensions=dimensions)
