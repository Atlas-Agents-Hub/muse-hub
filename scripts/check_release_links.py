#!/usr/bin/env python3
"""Require every advertised website package in the published GitHub release."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]


def check(release: dict, directory: dict) -> None:
    if release.get('draft') is not False or release.get('prerelease') is not False:
        raise ValueError('The website requires a published stable release.')
    if release.get('tag_name')!=directory['version']:
        raise ValueError('Release version does not match the downloads directory.')
    rows=release.get('assets',[])
    assets={row['name']:row for row in rows}
    if len(assets)!=len(rows):raise ValueError('Duplicate release asset names.')
    for row in directory['items']+directory['bundles']:
        asset=assets.get(row['asset'])
        if not asset or asset.get('state')!='uploaded' or asset.get('size',0)<=0:
            raise ValueError('Missing or incomplete download: '+row['asset'])
        if asset.get('browser_download_url')!=row['url']:
            raise ValueError('Download URL mismatch: '+row['asset'])
    for name in ('SHA256SUMS','SPECIALIST_DOWNLOADS.json'):
        if name not in assets or assets[name].get('state')!='uploaded':
            raise ValueError('Missing release metadata: '+name)


def main() -> int:
    if len(sys.argv)!=2:
        print('Usage: python scripts/check_release_links.py release.json',file=sys.stderr)
        return 2
    release=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    directory=json.loads((ROOT/'hub/site/downloads.json').read_text(encoding='utf-8'))
    try:check(release,directory)
    except (ValueError,KeyError,TypeError) as exc:
        print(str(exc),file=sys.stderr)
        return 1
    print('Every website download is available in '+directory['version']+'.')
    return 0


if __name__=='__main__':raise SystemExit(main())
