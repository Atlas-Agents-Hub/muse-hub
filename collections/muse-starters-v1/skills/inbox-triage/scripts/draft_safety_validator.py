#!/usr/bin/env python3
"""Check an inbox action log for send-operation names.

Scan the recorded tool calls before saving drafts and after the run. The result
lists matching log lines for review. Keep message bodies out of the action log.
This helper reads a local file and does not call any email service.
"""

import argparse
import json
import os
import stat
import re
import sys
from pathlib import Path
from typing import Any, Dict, List


MAX_LOG_BYTES = 1_000_000

SEND_PATTERNS = [re.compile(pattern, re.IGNORECASE) for pattern in (
    r'\b(?:gmail\.)?users\.(?:messages|drafts)\.send\b',
    r'(?<![A-Za-z0-9])(?:messages|drafts)[._]+send(?![A-Za-z0-9])',
    r'\b(?:gmail|outlook|email|smtp)\.send(?:mail)?\b',
    r'\b(?:me|users/[^/\s]+)/sendMail\b',
    r'\b(?:me|users/[^/\s]+)/messages/[^/\s]+/send\b',
    r'\busers/[^/\s]+/(?:messages|drafts)/send\b',
    r'\bgraph\.sendMail\b',
    r'(?<![A-Za-z0-9])(?:sendMail|sendMessage|sendDraft)(?![A-Za-z0-9])',
    r'(?<![A-Za-z0-9])(?:send_email|send_mail|send_message|dispatch_email|transmit_email|schedule_send)(?![A-Za-z0-9])',
)]

# Patterns that explicitly look like drafts/reads (used for context — NOT flagged)
DRAFT_INDICATORS = [
    re.compile(r"\bdrafts\.create\b", re.IGNORECASE),
    re.compile(r"\bSaveAsDraft\b"),
    re.compile(r"\bdrafts\.update\b", re.IGNORECASE),
    re.compile(r"\busers\.drafts\b", re.IGNORECASE),
]


SAMPLE_PASS_LOG = """# Triage Log — 2026-05-15 (Morning)

## Emails Processed (12)

- alice@example.com: classified Active Conversations
- bob@example.com: classified New Opportunities, recommendation TAKE IT
- newsletter@example.org: skipped (low priority)

## Drafts Created (3)

- gmail.users.drafts.create -> draft_id=abc123 (alice@example.com thread)
- gmail.users.drafts.create -> draft_id=def456 (bob@example.com thread)
- gmail.users.drafts.create -> draft_id=ghi789 (carol@example.com thread)

## KB Updates

- blocklist.md: appended 1 new pattern
- tracker.md: marked 2 items resolved, added 1 new follow-up

## Notable Observations

- bob@example.com is on the priority list; a reply draft is ready for review.
"""

SAMPLE_FAIL_LOG = """# Triage Log — 2026-05-15 (Morning)

## Emails Processed (12)

- alice@example.com: classified Active Conversations, response sent
- bob@example.com: classified New Opportunities

## Drafts Created (2)

- gmail.users.drafts.create -> draft_id=abc123
- gmail.users.drafts.create -> draft_id=def456

## Auto-replies sent

- gmail.users.messages.send -> message_id=xyz789 (alice@example.com auto-reply)

## KB Updates
- blocklist.md: appended 1 new pattern
"""


def scan_log(text: str) -> Dict[str, Any]:
    if not isinstance(text, str) or len(text.encode('utf-8')) > MAX_LOG_BYTES:
        raise ValueError('action log must be UTF-8 text of at most 1 MB')
    findings: List[Dict[str, Any]] = []
    draft_count = 0
    for line_no, line in enumerate(text.splitlines(), start=1):
        matches = [pattern.pattern for pattern in SEND_PATTERNS if pattern.search(line)]
        if matches:
            findings.append({'line': line_no, 'patterns': matches, 'text': line.strip()[:200]})
        if any(pattern.search(line) for pattern in DRAFT_INDICATORS):
            draft_count += 1
    verdict = 'EMPTY' if not text.strip() else 'FAIL' if findings else 'PASS'
    return {'verdict': verdict, 'send_violations': findings,
            'send_violation_count': len(findings), 'draft_indicator_count': draft_count}


def read_log(path: Path) -> str:
    info = path.lstat()
    if (path.is_symlink() or not stat.S_ISREG(info.st_mode)
            or getattr(info, 'st_file_attributes', 0) & 0x400
            or info.st_size > MAX_LOG_BYTES):
        raise ValueError('action log must be a regular file of at most 1 MB')
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0)
    with os.fdopen(os.open(path, flags), 'rb') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_LOG_BYTES:
            raise ValueError('action log must be a regular file of at most 1 MB')
        raw = stream.read(MAX_LOG_BYTES + 1)
    if len(raw) > MAX_LOG_BYTES or b'\0' in raw:
        raise ValueError('invalid action log')
    return raw.decode('utf-8-sig')

def render_human(result: Dict[str, Any]) -> str:
    lines = [f"Action-log check: {result['verdict']}",
             f"Send-operation matches: {result['send_violation_count']}",
             f"Draft-operation lines: {result['draft_indicator_count']}"]
    if result['verdict'] == 'EMPTY':
        lines.append('Record the tool calls for this run, then check the log again.')
    elif result['verdict'] == 'PASS':
        lines.append('No matching send-operation names in the supplied log.')
    else:
        for finding in result['send_violations']:
            lines.append(f"Line {finding['line']}: {finding['text']}")
        lines.append('Review these operations and reconcile their provider results before continuing.')
    return '\n'.join(lines)


def main(argv: List[str]) -> int:
    for stream in (sys.stdout, sys.stderr):
        if callable(getattr(stream, 'reconfigure', None)):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--action-log', type=Path)
    source.add_argument('--sample-pass', action='store_true')
    source.add_argument('--sample-fail', action='store_true')
    parser.add_argument('--output', choices=['human', 'json'], default='human')
    args = parser.parse_args(argv)
    try:
        text = SAMPLE_PASS_LOG if args.sample_pass else SAMPLE_FAIL_LOG if args.sample_fail else read_log(args.action_log)
        result = scan_log(text)
    except (ValueError, OSError, UnicodeError) as exc:
        print('Action-log error: ' + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.output == 'json' else render_human(result))
    return {'PASS': 0, 'FAIL': 1, 'EMPTY': 2}[result['verdict']]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
