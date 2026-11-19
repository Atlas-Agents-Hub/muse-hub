"""Bounded source limits for generated indexes in a large resource library."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

LIBRARY_ASSET_CATALOG = 'collections/library/catalog.json'
# A catalog edit must be reviewed before it can admit new support-file bytes.
LIBRARY_ASSET_CATALOG_SHA256 = '9e0c347346b66304cf90c08462d3340b8144921b22115ddd6836bb0f605024be'

CATALOG_FILES = frozenset({
    'PUBLIC_SOURCE_MANIFEST.json',
    'collections/library/catalog.json',
    'collections/library/workflows.json',
    'collections/library/SOURCES.json',
    'collections/muse-starters-v1/starters.json',
    'hub/site/downloads.json',
    'docs/connectors/catalog.json',
    'docs/connectors/ADAPTER_SOURCES.json',
})
LARGE_DOCUMENTS = frozenset({
    'hub/site/downloads.html',
    'collections/muse-starters-v1/SKILL_INDEX.md',
    'collections/muse-starters-v1/CATALOG.md',
})


def source_file_limit(name: str, default: int = 2_000_000) -> int:
    if name in CATALOG_FILES:
        return 64_000_000
    if name in LARGE_DOCUMENTS:
        return 16_000_000
    return default


def reviewed_library_assets(root: Path) -> dict[str, str]:
    """Return exact library paths and digests from the reviewed catalog bytes.

    This inventory only admits support files under their own skill package.
    It does not bypass sensitive-file, UTF-8, size, or content checks.
    """
    root = Path(root)
    path = root / LIBRARY_ASSET_CATALOG
    for member in (path, *path.parents):
        if member == root:
            break
        if member.is_symlink() or (member.exists() and
                getattr(member.lstat(), 'st_file_attributes', 0) & 0x400):
            raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
    if not path.exists():
        return {}
    if not path.is_file() or path.stat().st_size > source_file_limit(LIBRARY_ASSET_CATALOG):
        raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != LIBRARY_ASSET_CATALOG_SHA256:
        raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')

    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
            result[key] = value
        return result

    document = json.loads(raw, object_pairs_hook=unique_keys)
    if (not isinstance(document, dict) or set(document) != {'schema', 'skills'} or
            document['schema'] != 'muse-skill-library/v1' or
            not isinstance(document['skills'], list)):
        raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
    result = {}
    for skill in document['skills']:
        if (not isinstance(skill, dict) or not isinstance(skill.get('id'), str) or
                re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', skill['id']) is None or
                skill.get('path') != 'skills/' + skill['id'] or
                not isinstance(skill.get('files'), dict)):
            raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
        for name, digest in skill['files'].items():
            if (not isinstance(name, str) or not name or '\\' in name or ':' in name or
                    any(part in {'', '.', '..'} for part in name.split('/')) or
                    not isinstance(digest, str) or
                    re.fullmatch('[0-9a-f]{64}', digest) is None):
                raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
            relative = 'collections/library/' + skill['path'] + '/' + name
            if relative in result:
                raise ValueError('INVALID_LIBRARY_ASSET_CATALOG')
            result[relative] = digest
    return result
