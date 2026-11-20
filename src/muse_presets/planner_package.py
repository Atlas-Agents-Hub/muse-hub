"""Select the complete reviewed Muse Planner app for portable downloads."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat

ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = 'examples/gtd_space'
PACKAGE_PATH = 'spaces/planner'
INVENTORY_PATH = 'src/muse_presets/planner_sources.json'
INVENTORY_SHA256 = '51de7e209680a4ae7027fb4da85bf6338d3ddb89e11df4d9f16bdf4f5331c99b'
SOURCE_FILE_COUNT = 64
MAX_FILE_BYTES = 2_000_000
MAX_TOTAL_BYTES = 5_000_000
ROLES = ('coordinator', 'personal-companion')
SCHEMA = 'muse-planner-source/v1'
_HEX = re.compile(r'[0-9a-f]{64}\Z')
_PART = re.compile(r'[A-Za-z0-9_.-]+\Z')
_RESERVED = re.compile(r'(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?\Z', re.I)
_RUNTIME_DIRS = frozenset({
    '.sdk', 'node_modules', '__pycache__', '.pytest_cache', '.bun', '.bun-cache',
    '.space-build', '.space-build-cvm', '.harness', 'audits',
})
_BUILD_DIRS = frozenset({'client/dist', 'client/dist-cvm', 'server/dist'})


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _name(value: object) -> str:
    if (not isinstance(value, str) or not value or len(value) > 240 or
            any(part in {'', '.', '..'} or not _PART.fullmatch(part) or
                part.endswith(('.', ' ')) or _RESERVED.fullmatch(part)
                for part in value.split('/'))):
        raise ValueError('PLANNER_UNSAFE_SOURCE_PATH')
    return value


def _safe_node(path: Path) -> os.stat_result:
    try:
        info = path.lstat()
    except OSError as exc:
        raise ValueError('PLANNER_MISSING_SOURCE:' + path.name) from exc
    if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
        raise ValueError('PLANNER_LINKED_SOURCE_REFUSED')
    return info


def _read(root: Path, name: str, limit: int = MAX_FILE_BYTES) -> bytes:
    current = root
    _safe_node(current)
    for part in _name(name).split('/'):
        current /= part
        info = _safe_node(current)
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > limit:
        raise ValueError('PLANNER_UNSAFE_SOURCE_FILE:' + name)
    with current.open('rb') as stream:
        raw = stream.read(limit + 1)
    if len(raw) > limit or b'\0' in raw:
        raise ValueError('PLANNER_UNSAFE_SOURCE_BYTES:' + name)
    try:
        raw.decode('utf-8')
    except UnicodeError as exc:
        raise ValueError('PLANNER_SOURCE_NOT_UTF8:' + name) from exc
    return raw


def _runtime(name: str) -> bool:
    parts = name.split('/')
    if any(part in _RUNTIME_DIRS for part in parts):
        return True
    if any(name == directory or name.startswith(directory + '/') for directory in _BUILD_DIRS):
        return True
    leaf = parts[-1]
    return (leaf == 'app.db' or leaf.startswith('app.db-') or
            leaf.endswith(('.sqlite', '.sqlite-shm', '.sqlite-wal', '.tsbuildinfo')) or
            leaf.startswith('.tsbuildinfo'))


def _inventory(root: Path) -> tuple[bytes, dict[str, str]]:
    raw = _read(root, INVENTORY_PATH, 100_000)
    if _sha(raw) != INVENTORY_SHA256:
        raise ValueError('PLANNER_INVENTORY_NOT_REVIEWED')

    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('PLANNER_DUPLICATE_INVENTORY_KEY')
            result[key] = value
        return result

    document = json.loads(raw, object_pairs_hook=unique)
    if (not isinstance(document, dict) or
            set(document) != {'schema', 'id', 'source_path', 'package_path', 'files'} or
            document['schema'] != SCHEMA or document['id'] != 'planner' or
            document['source_path'] != SOURCE_PATH or document['package_path'] != PACKAGE_PATH or
            not isinstance(document['files'], dict) or len(document['files']) != SOURCE_FILE_COUNT):
        raise ValueError('PLANNER_INVALID_SOURCE_INVENTORY')
    seen = set()
    for name, digest in document['files'].items():
        _name(name)
        if name.casefold() in seen or _runtime(name):
            raise ValueError('PLANNER_INVALID_SOURCE_INVENTORY')
        seen.add(name.casefold())
        if not isinstance(digest, str) or _HEX.fullmatch(digest) is None:
            raise ValueError('PLANNER_INVALID_SOURCE_INVENTORY')
    return raw, document['files']


def source_files(root: Path = ROOT) -> dict[str, bytes]:
    """Return unchanged app bytes, refusing unreviewed files and linked paths."""
    root = Path(root).absolute()
    _, expected = _inventory(root)
    app = root / SOURCE_PATH
    for node in (root, root / 'examples', app):
        if not stat.S_ISDIR(_safe_node(node).st_mode):
            raise ValueError('PLANNER_INVALID_SOURCE_ROOT')
    actual = set()
    for current, directories, files in os.walk(app, followlinks=False):
        parent = Path(current)
        for directory in list(directories):
            child = parent / directory
            name = child.relative_to(app).as_posix()
            if _runtime(name):
                directories.remove(directory)
                continue
            _safe_node(child)
        for filename in files:
            child = parent / filename
            name = child.relative_to(app).as_posix()
            if _runtime(name):
                continue
            _name(name)
            _safe_node(child)
            actual.add(name)
    if actual != set(expected):
        raise ValueError('PLANNER_SOURCE_ROSTER_MISMATCH')
    result = {}
    total = 0
    for name, digest in sorted(expected.items()):
        raw = _read(root, SOURCE_PATH + '/' + name)
        if _sha(raw) != digest:
            raise ValueError('PLANNER_SOURCE_CHANGED:' + name)
        total += len(raw)
        if total > MAX_TOTAL_BYTES:
            raise ValueError('PLANNER_SOURCE_RESOURCE_LIMIT')
        result[name] = raw
    return result


def package_files(root: Path = ROOT) -> dict[str, bytes]:
    """Keep the same app folder and inventory in every Planner download."""
    files = {PACKAGE_PATH + '/' + name: raw for name, raw in source_files(root).items()}
    inventory, _ = _inventory(Path(root))
    files['PLANNER_FILES.json'] = inventory
    return files


def reviewed_planner_assets(root: Path) -> dict[str, str]:
    """Provide exact app hashes to source export without broadening file types."""
    root = Path(root)
    if not (root / INVENTORY_PATH).exists() and not (root / SOURCE_PATH).exists():
        return {}
    return {SOURCE_PATH + '/' + name: _sha(raw) for name, raw in source_files(root).items()}
