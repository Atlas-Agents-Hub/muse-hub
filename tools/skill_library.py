"""Load and package the Muse Hub skill library with complete file dependencies."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = ROOT / 'collections/library'
SCHEMA = 'muse-skill-library/v1'
ROLES = frozenset(('coordinator', 'software-engineer', 'model-builder',
    'research-evaluator', 'creative-studio', 'adversarial-verifier',
    'personal-companion', 'garden-companion', 'learning-coach',
    'claims-adjudicator', 'reverse-engineering-researcher', 'data-engineer',
    'reliability-engineer', 'automation-engineer', 'product-interface-designer'))
ID = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
DIGEST = re.compile(r'[0-9a-f]{64}\Z')
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
MAX_FILE_BYTES = 2_000_000
MAX_PACKAGE_BYTES = 12_000_000
MAX_LIBRARY_BYTES = 160_000_000
MAX_PACKAGE_FILES = 1000


def _require(condition, reason):
    if not condition:
        raise ValueError('SKILL_LIBRARY_' + reason)


def _path(name):
    _require(isinstance(name, str) and bool(name) and name.isascii()
             and len(name) <= 300 and not any(c in name for c in '\\:*?"<>|'), 'PATH')
    parts = name.split('/')
    reserved = {'con', 'prn', 'aux', 'nul', *(f'com{i}' for i in range(1, 10)),
                *(f'lpt{i}' for i in range(1, 10))}
    _require(all(p not in ('', '.', '..') and not p.endswith((' ', '.'))
                 and p.split('.')[0].casefold() not in reserved
                 and not any(ord(c) < 32 or ord(c) == 127 for c in p) for p in parts), 'PATH')
    return PurePosixPath(name)


def _text(value, minimum=1, maximum=3000):
    _require(isinstance(value, str) and minimum <= len(value.strip()) <= maximum
             and not any(c in value for c in ('\x00', '\u202e', '\u202d')), 'TEXT')


def _strings(values, minimum=1, maximum=100):
    _require(isinstance(values, list) and minimum <= len(values) <= maximum, 'LIST')
    for value in values:
        _text(value)
    _require(len(set(values)) == len(values), 'DUPLICATE_VALUE')


def validate_entry(row):
    _require(isinstance(row, dict), 'ENTRY')
    _require(isinstance(row.get('id'), str) and len(row['id']) <= 64
             and ID.fullmatch(row['id']) is not None, 'ID')
    for key in ('title', 'category', 'trigger', 'example'):
        _text(row.get(key), 4 if key in ('title', 'category') else 20)
    _strings(row.get('checks'), 3)
    _strings(row.get('roles'))
    _require(set(row['roles']) <= ROLES, 'ROLE')
    _require(row.get('path') == 'skills/' + row['id'], 'PATH')
    files = row.get('files')
    _require(isinstance(files, dict) and 2 <= len(files) <= MAX_PACKAGE_FILES, 'FILES')
    seen = set()
    for name, digest in files.items():
        _path(name)
        _require(name.casefold() not in seen, 'PATH_COLLISION')
        seen.add(name.casefold())
        _require(isinstance(digest, str) and DIGEST.fullmatch(digest) is not None, 'DIGEST')
    _require('SKILL.md' in files, 'ENTRYPOINT')
    for name in seen:
        parts = name.split('/')
        _require(not any('/'.join(parts[:i]) in seen for i in range(1, len(parts))), 'PATH_COLLISION')
    _strings(row.get('license_files'))
    _require(set(row['license_files']) <= files.keys(), 'LICENSE')
    for name in row['license_files']:
        _require('license' in name.lower() or 'notice' in name.lower(), 'LICENSE')
    for key in ('requirements', 'related_skills'):
        if key in row:
            _strings(row[key], 0)


def _read(path, root, limit=MAX_FILE_BYTES):
    _require(path.is_relative_to(root), 'PATH')
    for current in (path, *path.parents):
        if current == root.parent:
            break
        info = current.lstat()
        _require(not stat.S_ISLNK(info.st_mode)
                 and not getattr(info, 'st_file_attributes', 0) & 0x400, 'LINK')
    info = path.stat()
    _require(stat.S_ISREG(info.st_mode) and info.st_size <= limit, 'FILE_SIZE')
    with path.open('rb') as stream:
        raw = stream.read(limit + 1)
    _require(len(raw) <= limit and b'\x00' not in raw, 'FILE_SIZE')
    raw.decode('utf-8')
    return raw


def _check_references(files):
    for name, raw in files.items():
        if not name.endswith('.md'):
            continue
        text = re.sub(r'```.*?```|~~~.*?~~~', '', raw.decode('utf-8'), flags=re.S)
        for match in LINK.finditer(text):
            target = match[1].strip().split('#', 1)[0].split('?', 1)[0]
            if not target or re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('//'):
                continue
            # Resolve dot components against the package, without touching the filesystem.
            pieces = list(PurePosixPath(name).parent.parts)
            for part in unquote(target).split('/'):
                if part in ('', '.'):
                    continue
                if part == '..':
                    _require(bool(pieces), 'REFERENCE_ESCAPE:' + name)
                    pieces.pop()
                else:
                    pieces.append(part)
            joined = '/'.join(pieces)
            _require(joined in files or any(n.startswith(joined.rstrip('/') + '/') for n in files),
                     'REFERENCE_MISSING:' + name + ':' + target)


def package_files(row, root=DEFAULT_ROOT):
    validate_entry(row)
    root = Path(root).absolute()
    folder = root / row['path']
    contents = {}
    total = 0
    for name, digest in row['files'].items():
        raw = _read(folder / name, root)
        _require(hashlib.sha256(raw).hexdigest() == digest, 'DIGEST_CHANGED:' + row['id'] + ':' + name)
        contents[name] = raw
        total += len(raw)
    _require(total <= MAX_PACKAGE_BYTES, 'PACKAGE_SIZE')
    _check_references(contents)
    return {row['path'] + '/' + name: raw for name, raw in contents.items()}


def load_library(root=DEFAULT_ROOT):
    root = Path(root).absolute()
    raw = _read(root / 'catalog.json', root, 8_000_000)
    def pairs(items):
        result = {}
        for key, value in items:
            _require(key not in result, 'DUPLICATE_JSON_KEY')
            result[key] = value
        return result
    catalog = json.loads(raw, object_pairs_hook=pairs)
    _require(isinstance(catalog, dict) and catalog.get('schema') == SCHEMA, 'SCHEMA')
    rows = catalog.get('skills')
    _require(isinstance(rows, list) and 1 <= len(rows) <= 1500, 'INVENTORY')
    seen = set(); bodies = set(); total = 0
    for row in rows:
        validate_entry(row)
        _require(row['id'] not in seen, 'DUPLICATE_ID')
        seen.add(row['id'])
        _require(row['files']['SKILL.md'] not in bodies, 'DUPLICATE_BODY')
        bodies.add(row['files']['SKILL.md'])
        folder = root / row['path']
        actual = set()
        for p in folder.rglob('*'):
            _require(not p.is_symlink()
                     and not getattr(p.lstat(), 'st_file_attributes', 0) & 0x400, 'LINK')
            if p.is_file(): actual.add(p.relative_to(folder).as_posix())
        _require(actual == set(row['files']), 'ROSTER:' + row['id'])
        for name in row['files']:
            total += (folder / name).stat().st_size
        entry = _read(folder / 'SKILL.md', root).decode('utf-8')
        _require(entry.startswith('---\n') and re.search(r'^name:\s*' + re.escape(row['id']) + r'\s*$', entry, re.M), 'FRONTMATTER')
    _require(total <= MAX_LIBRARY_BYTES, 'LIBRARY_SIZE')
    for row in rows:
        _require(set(row.get('related_skills', [])) <= seen, 'RELATED_SKILL')
    return rows


def collection_entries(root=DEFAULT_ROOT):
    return [{**row, 'format': 'portable-skill', 'source_ids': []} for row in load_library(root)]
