#!/usr/bin/env python3
"""Choose an inbox search interval from the last completed run or a cadence.

Use --since with the previous successful window_end for recurring work. Cadence
defaults cover an evenly spaced interval plus two hours of overlap. All interval
arithmetic uses UTC; the run label follows the supplied --now offset.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import math
import sys

CADENCE_DEFAULT_HOURS = {
    'once-daily': 26,
    '2x-daily': 14,
    '3x-daily': 10,
    'on-demand': 24,
}
MAX_HOURS = 24 * 30


def utc(value: datetime) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError('timestamps must be datetime values')
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def cadence_to_hours(cadence: str, override_hours: int | None = None) -> int:
    key = cadence.lower().strip()
    if key not in CADENCE_DEFAULT_HOURS:
        raise ValueError('choose a supported cadence')
    if override_hours is not None:
        if type(override_hours) is not int or not 1 <= override_hours <= MAX_HOURS:
            raise ValueError('override-hours must be an integer between 1 and 720')
        return override_hours
    return CADENCE_DEFAULT_HOURS[key]


def run_label(hour_of_day: int) -> str:
    return 'Morning' if hour_of_day < 12 else 'Afternoon' if hour_of_day < 17 else 'Evening'


def compute(cadence: str, now: datetime, override_hours: int | None = None,
            *, since: datetime | None = None, overlap_minutes: int = 5) -> dict:
    fallback_hours = cadence_to_hours(cadence, override_hours)
    if type(overlap_minutes) is not int or not 0 <= overlap_minutes <= 120:
        raise ValueError('overlap-minutes must be between 0 and 120')
    end = utc(now)
    if since is not None:
        if override_hours is not None:
            raise ValueError('choose since or override-hours, not both')
        previous = utc(since)
        if previous > end:
            raise ValueError('since cannot be later than now')
        start = previous - timedelta(minutes=overlap_minutes)
        if end - start > timedelta(hours=MAX_HOURS):
            raise ValueError('interval exceeds 30 days; review the backlog in explicit date ranges')
        basis = 'previous-success'
    else:
        previous = None
        start = end - timedelta(hours=fallback_hours)
        basis = 'explicit-lookback' if override_hours is not None else 'cadence'
    return {
        'cadence': cadence.lower().strip(),
        'override_hours': override_hours,
        'coverage_basis': basis,
        'previous_success': previous.isoformat() if previous else None,
        'overlap_minutes': overlap_minutes if previous else 0,
        'hours_back': (end - start).total_seconds() / 3600,
        'now': now.isoformat(),
        'window_start': start.isoformat(),
        'window_end': end.isoformat(),
        'run_label': run_label(now.hour),
        # Broaden second-resolution provider queries, then filter exact [start,end).
        'search_filter_after_unix': math.floor(start.timestamp()) - 1,
        'search_filter_before_unix': math.ceil(end.timestamp()),
    }


def render_human(result: dict) -> str:
    return '\n'.join([
        f"Cadence:        {result['cadence']}",
        f"Coverage:       {result['coverage_basis']}",
        f"Window start:   {result['window_start']}",
        f"Window end:     {result['window_end']}",
        f"Hours lookback: {result['hours_back']:g}",
        f"Run label:      {result['run_label']}", '',
        'Retrieve messages in [window_start, window_end); deduplicate overlap by message ID.',
        f"Gmail: after:{result['search_filter_after_unix']} before:{result['search_filter_before_unix']}",
        f"Outlook: receivedDateTime ge {result['window_start']} and receivedDateTime lt {result['window_end']}",
        'Filter coarse provider results to the exact interval before triage.',
        'Save window_end only after every requested page and the report are complete.',
    ])


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value[:-1] + '+00:00' if value.endswith('Z') else value)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if callable(getattr(stream, 'reconfigure', None)):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cadence', choices=sorted(CADENCE_DEFAULT_HOURS), default='on-demand')
    selected = parser.add_mutually_exclusive_group()
    selected.add_argument('--since', help='Previous successful window_end, as an ISO timestamp')
    selected.add_argument('--override-hours', type=int, help='Explicit lookback, from 1 to 720 hours')
    parser.add_argument('--overlap-minutes', type=int, default=5)
    parser.add_argument('--now', help='ISO timestamp; defaults to current UTC; naive inputs mean UTC')
    parser.add_argument('--output', choices=['human', 'json'], default='human')
    args = parser.parse_args(argv)
    try:
        now = parse_timestamp(args.now) if args.now else datetime.now(timezone.utc)
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        since = parse_timestamp(args.since) if args.since else None
        result = compute(args.cadence, now, args.override_hours,
                         since=since, overlap_minutes=args.overlap_minutes)
    except (ValueError, TypeError, OverflowError) as exc:
        print('Window error: ' + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.output == 'json' else render_human(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
