"""Strictly admit one reviewed social-preview PNG into the static site."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import struct
import zlib

SOCIAL_CARD_PATH = "hub/site/social-card.png"
SOCIAL_CARD_SITE_PATH = "social-card.png"
_SOCIAL_SIZE = (1200, 630)
_MAX_SOCIAL_BYTES = 1_000_000
_PNG = b"\x89PNG\r\n\x1a\n"


def reviewed_social_digest(root: Path) -> str | None:
    """Return the site inventory digest when the social card exists."""
    image = root / SOCIAL_CARD_PATH
    if not image.exists() and not image.is_symlink():
        return None
    manifest = json.loads((root / "hub/site/INTEGRITY.json").read_text(encoding="utf-8"))
    row = manifest["files"][SOCIAL_CARD_SITE_PATH]
    digest = row["sha256"]
    if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
        raise ValueError("SOCIAL_PREVIEW_DIGEST_INVALID")
    if not isinstance(row.get("bytes"), int) or row["bytes"] < 1:
        raise ValueError("SOCIAL_PREVIEW_SIZE_INVALID")
    return digest


def valid_social_card(data: bytes, digest: str | None) -> bool:
    """Validate dimensions, chunk checksums, framing and reviewed hash."""
    if (
        not digest
        or len(data) > _MAX_SOCIAL_BYTES
        or len(data) < 60
        or not data.startswith(_PNG)
        or hashlib.sha256(data).hexdigest() != digest
    ):
        return False
    offset = len(_PNG)
    seen_header = False
    seen_image = False
    seen_end = False
    while offset + 12 <= len(data):
        n = struct.unpack_from(">I", data, offset)[0]
        if n > _MAX_SOCIAL_BYTES or offset + n + 12 > len(data):
            return False
        kind = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + n]
        stored = struct.unpack_from(">I", data, offset + 8 + n)[0]
        if zlib.crc32(kind + payload) & 0xFFFFFFFF != stored:
            return False
        if not seen_header:
            if kind != b"IHDR" or n != 13:
                return False
            width, height, depth, color_type, comp, filt, interlace = struct.unpack(">IIBBBBB", payload)
            if ((width, height) != _SOCIAL_SIZE or depth != 8 or color_type not in (2, 6)
                or comp != 0 or filt != 0 or interlace != 0):
                return False
            seen_header = True
        elif kind == b"IHDR":
            return False
        elif kind == b"IDAT":
            seen_image = True
        elif kind == b"IEND":
            if n != 0 or not seen_image:
                return False
            seen_end = True
            offset += n + 12
            break
        offset += n + 12
    return seen_header and seen_image and seen_end and offset == len(data)
