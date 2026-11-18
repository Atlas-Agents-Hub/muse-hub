#!/usr/bin/env python3
"""Build a GitHub release request that retains its intended tag and source commit."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def payload(version: str, head: str, phase: str, body: str | None = None) -> dict:
    if not re.fullmatch(r'v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)',version):
        raise ValueError('A stable release tag is required.')
    if not re.fullmatch(r'[0-9a-f]{40}',head):
        raise ValueError('The full accepted commit SHA is required.')
    # GitHub draft edits can otherwise replace the tag with an untagged placeholder.
    result={'tag_name':version,'target_commitish':head,'prerelease':False}
    if phase=='draft':
        if not isinstance(body,str) or not body.strip():
            raise ValueError('Draft release notes are required.')
        result.update(name='Muse Hub '+version,body=body,draft=True)
    elif phase=='publish':
        if body is not None:
            raise ValueError('Publish the already-reviewed draft notes unchanged.')
        result.update(draft=False,make_latest='true')
    else:
        raise ValueError('Choose draft or publish.')
    return result


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version',required=True)
    parser.add_argument('--expected-head',required=True)
    parser.add_argument('--phase',choices=('draft','publish'),required=True)
    parser.add_argument('--body-file',type=Path)
    args=parser.parse_args()
    try:
        body=args.body_file.read_text(encoding='utf-8') if args.body_file else None
        result=payload(args.version,args.expected_head,args.phase,body)
    except (ValueError,OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
