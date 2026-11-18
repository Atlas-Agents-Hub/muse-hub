#!/usr/bin/env python3
"""Verify the complete published release before deploying its download directory."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'https://github.com/atlas-origins/muse-ai-agent-presets'
METADATA = frozenset({'SHA256SUMS', 'SPECIALIST_DOWNLOADS.json', 'SKILL_DOWNLOADS.json',
                      'WORKFLOW_DOWNLOADS.json', 'RELEASE_MANIFEST.json', 'DOWNLOADS.md'})
VERSION = re.compile(r'v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\Z')
SHA = re.compile(r'[0-9a-f]{40}\Z')
DIGEST = re.compile(r'sha256:[0-9a-f]{64}\Z')
CHECKSUM = re.compile(r'([0-9a-f]{64})  ([A-Za-z0-9][A-Za-z0-9._-]*)\Z')


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def check(release: dict, directory: dict) -> dict:
    """Check roster, publication state, canonical URLs and provider digests."""
    version = directory['version']
    if not isinstance(version, str) or not VERSION.fullmatch(version):
        raise ValueError('Invalid stable release version.')
    if release.get('draft') is not False or release.get('prerelease') is not False:
        raise ValueError('The website requires a published stable release.')
    if release.get('tag_name') != version:
        raise ValueError('Release version does not match the downloads directory.')
    base = REPOSITORY + '/releases/download/' + version + '/'
    advertised = directory['items'] + directory['bundles']
    expected = {row['asset'] for row in advertised}
    if len(expected) != len(advertised):
        raise ValueError('Duplicate download directory asset names.')
    expected |= METADATA | {'muse-role-procedures-50-' + version + '.zip'}
    rows = release.get('assets', [])
    assets = {row['name']: row for row in rows}
    if len(assets) != len(rows):
        raise ValueError('Duplicate release asset names.')
    if set(assets) != expected:
        raise ValueError('Release roster mismatch: missing=' + ','.join(sorted(expected - set(assets)))
                         + '; unexpected=' + ','.join(sorted(set(assets) - expected)))
    for name, asset in assets.items():
        if asset.get('state') != 'uploaded' or type(asset.get('size')) is not int or asset['size'] <= 0:
            raise ValueError('Missing or incomplete download: ' + name)
        if asset.get('browser_download_url') != base + name:
            raise ValueError('Download URL mismatch: ' + name)
        if not isinstance(asset.get('digest'), str) or not DIGEST.fullmatch(asset['digest']):
            raise ValueError('Missing SHA-256 provider digest: ' + name)
    for row in advertised:
        if row['url'] != base + row['asset']:
            raise ValueError('Download directory URL mismatch: ' + row['asset'])
    return assets


def check_proof(release: dict, directory: dict, manifest_raw: bytes, checksums_raw: bytes,
                expected_head: str, tag_head: str) -> None:
    """Bind every uploaded file and package index to the deployed Git commit."""
    assets = check(release, directory)
    if not SHA.fullmatch(expected_head) or tag_head != expected_head:
        raise ValueError('Release tag does not identify the website commit.')
    checksums = {}
    for line in checksums_raw.decode('utf-8').splitlines():
        match = CHECKSUM.fullmatch(line)
        if not match or match[2] in checksums:
            raise ValueError('Invalid or duplicate checksum entry.')
        checksums[match[2]] = match[1]
    if set(checksums) != set(assets) - {'SHA256SUMS'}:
        raise ValueError('Checksum roster does not match the full release.')
    for name, digest in checksums.items():
        if assets[name]['digest'] != 'sha256:' + digest:
            raise ValueError('Provider/checksum digest mismatch: ' + name)
    for name, raw in (('SHA256SUMS', checksums_raw), ('RELEASE_MANIFEST.json', manifest_raw)):
        if assets[name]['size'] != len(raw) or assets[name]['digest'] != 'sha256:' + hashlib.sha256(raw).hexdigest():
            raise ValueError('Downloaded metadata differs from the uploaded asset: ' + name)
    manifest = json.loads(manifest_raw, object_pairs_hook=_unique)
    if manifest.get('schema') != 'muse-release/v2' or manifest.get('version') != directory['version']:
        raise ValueError('Manifest version or schema mismatch.')
    if manifest.get('source', {}).get('head') != expected_head:
        raise ValueError('Packages were built from a different commit.')
    packages = manifest['assets']
    if set(packages) != set(assets) - METADATA:
        raise ValueError('Package manifest roster mismatch.')
    for name, row in packages.items():
        if row.get('sha256') != checksums[name] or row.get('bytes') != assets[name]['size']:
            raise ValueError('Package manifest hash or size mismatch: ' + name)
    records = manifest['downloads']
    all_records = []
    for kind, key in (('specialist', 'specialists'), ('skill', 'skills'), ('workflow', 'workflows')):
        rows = records[key]
        expected = {row['id']: row['asset'] for row in directory['items'] if row['kind'] == kind}
        actual = {row['id']: row['asset'] for row in rows}
        if len(actual) != len(rows) or actual != expected:
            raise ValueError('Package index differs from the website: ' + kind)
        all_records.extend(rows)
    all_records.extend(records['bundles'])
    if len(all_records) != len(packages) or {row['asset'] for row in all_records} != set(packages):
        raise ValueError('Package index roster mismatch.')
    for row in all_records:
        name = row['asset']
        if (row['sha256'] != checksums[name] or row['bytes'] != assets[name]['size']
                or row['url'] != assets[name]['browser_download_url']):
            raise ValueError('Package index hash, size or URL mismatch: ' + name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('release', type=Path)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--checksums', type=Path, required=True)
    parser.add_argument('--expected-head', required=True)
    parser.add_argument('--tag-head', required=True)
    args = parser.parse_args()
    try:
        release = json.loads(args.release.read_bytes(), object_pairs_hook=_unique)
        directory = json.loads((ROOT / 'hub/site/downloads.json').read_bytes(), object_pairs_hook=_unique)
        check_proof(release, directory, args.manifest.read_bytes(), args.checksums.read_bytes(),
                    args.expected_head, args.tag_head)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"Verified all {len(release['assets'])} release files for {directory['version']} at {args.expected_head}.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
