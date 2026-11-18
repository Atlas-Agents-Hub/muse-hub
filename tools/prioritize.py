#!/usr/bin/env python3
"""Rank work with RICE and choose the next batch within resource capacities.

Usage: python -B tools/prioritize.py --input FILE [--format json|csv]
                                    [--output NEW_PATH]

JSON input schema: muse-prioritization/v1. Required fields: schema,
reach_period (nonempty text), effort_unit (person-hours, person-days, or
person-months), capacity (resource slug to number), and items (1..1000).
Each item requires id, name, reach, impact, confidence_pct, effort, resource.
Optional dependencies is an array of item IDs; optional status is todo or done
(default todo). Impact must be exactly 0.25, 0.5, 1, 2, or 3. Reach is >= 0,
confidence_pct is 0..100, effort is > 0. Every resource needs a capacity >= 0.

An input filename ending in .csv selects CSV input. Use the same item columns;
dependencies contains semicolon-separated IDs. The dependencies and status
columns may be omitted; blank cells mean no dependencies and todo. CSV needs
--reach-period TEXT --effort-unit UNIT and repeatable --capacity RESOURCE=NUMBER.
JSON already contains this metadata and rejects these flags. --format selects
the OUTPUT format (default json), independently of the input file extension.

Numbers use JSON decimal syntax, magnitude <= 10^12, at most 12 decimal places,
and exponent magnitude <= 12. Input must be a regular UTF-8 file <= 1 MiB.
Slugs use lowercase letters/digits separated by single hyphens, up to 64 chars.
Unknown fields, duplicate keys/IDs, missing dependencies and cycles are errors.

RICE = reach * impact * (confidence_pct / 100) / effort. Ranking is exact,
descending score then ID; display scores round to six places, half up.
The greedy batch considers each todo item's full unmet prerequisite bundle,
in dependency order (ID order for sibling prerequisites). It selects the whole
bundle only when every resource fits. Completed items cost zero; shared work
is charged once. This is a next-batch heuristic, not an optimal roadmap.

JSON report schema: muse-prioritization-report/v1; ranked_items, selected_order,
deferred, completed_ids, budgets, reach_period, effort_unit. Quantities are exact
decimal strings; score_exact is a numerator/denominator string. Deferred
shortfalls record remaining capacity when that bundle was considered.
CSV includes ranking, execution order, status, reason and per-resource context.
To prevent spreadsheet formulas, CSV prefixes textual cells beginning with
=, +, -, @ (also after whitespace), tab, CR, or LF with an apostrophe. JSON
preserves original text. CSV reports are for reading, not reimport as input.

Without --output, stdout is the complete report. With --output, a NEW file is
created and stdout stays empty. Existing paths, including symlinks, are never
overwritten. Errors go to stderr as 'prioritize: error: ...', with exit code 2.
No dependencies outside the Python 3.10+ standard library are required.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Context, Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction
import heapq
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile


MAX_BYTES = 1024 * 1024
MAX_ITEMS = 1000
MAX_NUMBER = Decimal("1e12")
UNITS = ("person-hours", "person-days", "person-months")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE]([+-]?[0-9]+))?\Z")
ITEM_REQUIRED = {"id", "name", "reach", "impact", "confidence_pct", "effort", "resource"}
ITEM_FIELDS = ITEM_REQUIRED | {"dependencies", "status"}
ROOT_FIELDS = {"schema", "reach_period", "effort_unit", "capacity", "items"}


class PrioritizationError(ValueError):
    """Invalid input or an output that could not be safely created."""


def _number_token(token: str) -> Decimal:
    match = NUMBER.fullmatch(token) if len(token) <= 64 else None
    if not match or (match[1] is not None and abs(int(match[1])) > 12):
        raise PrioritizationError("number must use bounded decimal syntax (exponent -12..12)")
    value = Decimal(token)
    if value.as_tuple().exponent < -12 or value.copy_abs() > MAX_NUMBER:
        raise PrioritizationError("number exceeds 12 decimal places or magnitude 10^12")
    return value


def _number(value, field: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise PrioritizationError(f"{field} must be a number")
    try:
        return Fraction(_number_token(str(value)))
    except (ValueError, OverflowError) as exc:
        raise PrioritizationError(f"{field}: invalid number; {exc}") from exc


def _slug(value, field: str) -> str:
    if not isinstance(value, str) or len(value) > 64 or not SLUG.fullmatch(value):
        raise PrioritizationError(f"{field} must be a lowercase slug, at most 64 characters")
    return value


def _text(value, field: str, limit: int) -> str:
    if (not isinstance(value, str) or not value.strip() or len(value) > limit
            or any((ord(c) < 32 and c not in "\t\r\n") or 0xD800 <= ord(c) <= 0xDFFF
                   for c in value)):
        raise PrioritizationError(f"{field} must be nonempty text, at most {limit} characters")
    return value


def _fields(value, required: set, allowed: set, label: str) -> None:
    if not isinstance(value, dict):
        raise PrioritizationError(f"{label} must be an object")
    if required - value.keys():
        raise PrioritizationError(f"{label} missing fields: {', '.join(sorted(required - value.keys()))}")
    if value.keys() - allowed:
        raise PrioritizationError(f"{label} contains unknown fields")


def _pairs(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise PrioritizationError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _invalid_constant(token: str):
    raise PrioritizationError(f"number must be finite: {token}")


def read_input(path: Path) -> str:
    """Check before and after opening; nonblocking open also closes the FIFO race."""
    if not stat.S_ISREG(path.stat().st_mode):
        raise PrioritizationError("input must be a regular file")
    flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_BINARY", 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise PrioritizationError("input must be a regular file")
        if info.st_size > MAX_BYTES:
            raise PrioritizationError("input must be at most 1 MiB")
        data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise PrioritizationError("input must be at most 1 MiB")
    try:
        return data.decode("utf-8-sig")
    except UnicodeError as exc:
        raise PrioritizationError("input must be UTF-8") from exc


def parse_json(text: str) -> dict:
    try:
        return json.loads(text, parse_int=_number_token, parse_float=_number_token,
                          parse_constant=_invalid_constant, object_pairs_hook=_pairs)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise PrioritizationError("invalid JSON input or excessive nesting") from exc


def parse_csv(text: str, reach_period: str, effort_unit: str, capacities: list[str]) -> dict:
    if reach_period is None or effort_unit is None or not capacities:
        raise PrioritizationError("CSV metadata requires --reach-period, --effort-unit and --capacity")
    capacity = {}
    for declaration in capacities:
        resource, separator, amount = declaration.partition("=")
        _slug(resource, "capacity resource")
        if not separator or resource in capacity:
            raise PrioritizationError("capacity must be unique RESOURCE=NUMBER declarations")
        capacity[resource] = _number_token(amount.strip())
    try:
        reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(reader, [])
        if (len(header) != len(set(header)) or not ITEM_REQUIRED <= set(header)
                or not set(header) <= ITEM_FIELDS):
            raise PrioritizationError("CSV columns must be the required item fields and optional dependencies/status")
        items = []
        for row in reader:
            if len(row) != len(header):
                raise PrioritizationError(f"CSV row ending at line {reader.line_num} has the wrong column count")
            entry = dict(zip(header, row))
            for field in ("reach", "impact", "confidence_pct", "effort"):
                entry[field] = _number_token(entry[field].strip())
            deps = entry.get("dependencies", "")
            entry["dependencies"] = [x.strip() for x in deps.split(";")] if deps.strip() else []
            entry["status"] = entry.get("status", "") or "todo"
            items.append(entry)
            if len(items) > MAX_ITEMS:
                raise PrioritizationError("CSV must contain 1..1000 items")
    except csv.Error as exc:
        raise PrioritizationError(f"invalid CSV: {exc}") from exc
    return {"schema": "muse-prioritization/v1", "reach_period": reach_period,
            "effort_unit": effort_unit, "capacity": capacity, "items": items}


def _validated(data: dict) -> tuple[dict, dict]:
    _fields(data, ROOT_FIELDS, ROOT_FIELDS, "document")
    if data["schema"] != "muse-prioritization/v1":
        raise PrioritizationError("schema must be muse-prioritization/v1")
    _text(data["reach_period"], "reach_period", 200)
    if data["effort_unit"] not in UNITS:
        raise PrioritizationError("effort_unit must be person-hours, person-days or person-months")
    if not isinstance(data["capacity"], dict) or not 1 <= len(data["capacity"]) <= MAX_ITEMS:
        raise PrioritizationError("capacity must map 1..1000 resources to nonnegative numbers")
    budgets = {}
    for resource, value in data["capacity"].items():
        _slug(resource, "capacity resource")
        amount = _number(value, f"capacity.{resource}")
        if amount < 0:
            raise PrioritizationError(f"capacity.{resource} must be nonnegative")
        budgets[resource] = amount
    if not isinstance(data["items"], list) or not 1 <= len(data["items"]) <= MAX_ITEMS:
        raise PrioritizationError("items must contain 1..1000 entries")
    items = {}
    for entry in data["items"]:
        _fields(entry, ITEM_REQUIRED, ITEM_FIELDS, "item")
        ident = _slug(entry["id"], "item id")
        if ident in items:
            raise PrioritizationError(f"duplicate item id: {ident}")
        resource = _slug(entry["resource"], f"{ident}.resource")
        if resource not in budgets:
            raise PrioritizationError(f"{ident}: missing capacity for resource {resource}")
        numbers = {field: _number(entry[field], f"{ident}.{field}")
                   for field in ("reach", "impact", "confidence_pct", "effort")}
        if numbers["reach"] < 0 or numbers["effort"] <= 0:
            raise PrioritizationError(f"{ident}: reach must be >= 0 and effort must be > 0")
        if numbers["impact"] not in (Fraction(1, 4), Fraction(1, 2), 1, 2, 3):
            raise PrioritizationError(f"{ident}: impact must be 0.25, 0.5, 1, 2 or 3")
        if not 0 <= numbers["confidence_pct"] <= 100:
            raise PrioritizationError(f"{ident}: confidence_pct must be 0..100")
        status = entry.get("status", "todo")
        if status not in ("todo", "done"):
            raise PrioritizationError(f"{ident}: status must be todo or done")
        dependencies = entry.get("dependencies", [])
        if not isinstance(dependencies, list) or len(dependencies) > MAX_ITEMS:
            raise PrioritizationError(f"{ident}: dependencies must be an array of item IDs")
        for dependency in dependencies:
            _slug(dependency, f"{ident} dependency")
        if len(dependencies) != len(set(dependencies)):
            raise PrioritizationError(f"{ident}: duplicate dependency")
        items[ident] = {"id": ident, "name": _text(entry["name"], f"{ident}.name", 500),
                        **numbers, "resource": resource, "dependencies": sorted(dependencies), "status": status}
    # Kahn's algorithm avoids recursion limits for a valid 1000-item chain.
    pending = {ident: len(item["dependencies"]) for ident, item in items.items()}
    children = {ident: [] for ident in items}
    for ident, item in items.items():
        for dependency in item["dependencies"]:
            if dependency not in items:
                raise PrioritizationError(f"{ident}: missing dependency {dependency}")
            children[dependency].append(ident)
    ready = [ident for ident, count in pending.items() if count == 0]
    heapq.heapify(ready)
    visited = 0
    while ready:
        ident = heapq.heappop(ready); visited += 1
        for child in children[ident]:
            pending[child] -= 1
            if pending[child] == 0:
                heapq.heappush(ready, child)
    if visited != len(items):
        raise PrioritizationError("dependency cycle detected")
    return items, budgets


def _decimal(value: Fraction, places: int | None = None) -> str:
    with localcontext(Context(prec=80, rounding=ROUND_HALF_UP, Emin=-1000, Emax=1000)):
        number = Decimal(value.numerator) / Decimal(value.denominator)
        text = format(number, "f" if places is None else f".{places}f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _bundle(ident: str, items: dict, satisfied: set) -> list[str]:
    seen = set(satisfied)
    stack = [(ident, False)]
    result = []
    while stack:
        current, expanded = stack.pop()
        if current in seen:
            continue
        if expanded:
            result.append(current); seen.add(current)
        else:
            stack.append((current, True))
            stack.extend((dependency, False) for dependency in reversed(items[current]["dependencies"]))
    return result


def plan(data: dict) -> dict:
    """Return a deterministic report without mutating the input document."""
    items, capacity = _validated(data)
    scores = {ident: x["reach"] * x["impact"] * x["confidence_pct"] / 100 / x["effort"]
              for ident, x in items.items()}
    ranked = sorted(items, key=lambda ident: (-scores[ident], ident))
    completed = {ident for ident, x in items.items() if x["status"] == "done"}
    satisfied = set(completed)
    used = {resource: Fraction(0) for resource in capacity}
    selected, deferred = [], []
    for ident in ranked:
        if ident in satisfied:
            continue
        bundle = _bundle(ident, items, satisfied)
        costs = {}
        for dependency in bundle:
            entry = items[dependency]
            costs[entry["resource"]] = costs.get(entry["resource"], Fraction(0)) + entry["effort"]
        shortfalls = {}
        for resource in sorted(costs):
            remaining = capacity[resource] - used[resource]
            if costs[resource] > remaining:
                shortfalls[resource] = {"required": _decimal(costs[resource]),
                                       "remaining": _decimal(remaining),
                                       "shortfall": _decimal(costs[resource] - remaining)}
        if shortfalls:
            reasons = [f"{r} needs {v['required']}, remaining {v['remaining']}, shortfall {v['shortfall']}"
                       for r, v in shortfalls.items()]
            deferred.append({"id": ident, "bundle": bundle, "shortfalls": shortfalls,
                             "reason": "; ".join(reasons) + f" {data['effort_unit']}"})
        else:
            for resource, cost in costs.items():
                used[resource] += cost
            selected.extend(bundle); satisfied.update(bundle)
    order = {ident: position for position, ident in enumerate(selected, 1)}
    rows = []
    for rank, ident in enumerate(ranked, 1):
        entry = items[ident]
        rows.append({**{key: _decimal(value) if isinstance(value, Fraction) else value
                        for key, value in entry.items()},
                     "rank": rank, "score": _decimal(scores[ident], 6),
                     "score_exact": f"{scores[ident].numerator}/{scores[ident].denominator}",
                     "selection_status": "done" if ident in completed else
                         "selected" if ident in order else "deferred",
                     "selection_order": order.get(ident)})
    return {"schema": "muse-prioritization-report/v1", "reach_period": data["reach_period"],
            "effort_unit": data["effort_unit"], "ranked_items": rows,
            "selected_order": selected, "deferred": deferred, "completed_ids": sorted(completed),
            "budgets": {r: {"capacity": _decimal(capacity[r]), "used": _decimal(used[r]),
                            "remaining": _decimal(capacity[r] - used[r])} for r in sorted(capacity)}}


def _safe_cell(text: str) -> str:
    if text.startswith(("\t", "\r", "\n")) or text.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def render_csv(report: dict) -> str:
    fields = ["rank", "id", "name", "reach", "impact", "confidence_pct", "effort", "resource",
              "dependencies", "status", "score", "score_exact", "selection_order", "selection_status",
              "reason", "reach_period", "effort_unit", "capacity", "used", "remaining"]
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\r\n")
    writer.writeheader()
    reasons = {entry["id"]: entry["reason"] for entry in report["deferred"]}
    for entry in report["ranked_items"]:
        row = {**entry, **report["budgets"][entry["resource"]],
               "dependencies": ";".join(entry["dependencies"]), "reason": reasons.get(entry["id"], ""),
               "reach_period": report["reach_period"], "effort_unit": report["effort_unit"]}
        writer.writerow({key: _safe_cell(str(row[key])) if row[key] is not None else "" for key in fields})
    return stream.getvalue()


def write_new_output(path: Path, content: str) -> None:
    """Create a new report while preserving existing final directory entries.

    Windows CRT exclusive open can follow a dangling symlink. Write an owned
    sibling temporary file there and use Windows rename's no-replace contract.
    POSIX O_EXCL rejects an existing symlink at the creation operation.
    """
    fd, owned, identity = None, None, None
    temporary, finished = os.name == "nt", False
    try:
        if temporary:
            fd, name = tempfile.mkstemp(prefix=".prioritize-", suffix=".tmp", dir=path.parent)
            owned = Path(name)
        else:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            owned = path
        identity = os.fstat(fd)
        with os.fdopen(fd, "wb") as stream:
            fd = None
            stream.write(content.encode("utf-8")); stream.flush(); os.fsync(stream.fileno())
        if temporary:
            os.rename(owned, path)  # Windows refuses any existing destination.
        finished = True
    except FileExistsError as exc:
        raise PrioritizationError("output path already exists; choose a new path") from exc
    finally:
        if fd is not None:
            os.close(fd)
        if owned is not None and identity is not None and (temporary or not finished):
            try:
                current = owned.lstat()
                if (current.st_dev, current.st_ino) == (identity.st_dev, identity.st_ino):
                    owned.unlink()
            except OSError:
                pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="prioritize", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     allow_abbrev=False)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--format", choices=("json", "csv"), default="json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--reach-period")
    parser.add_argument("--effort-unit", choices=UNITS)
    parser.add_argument("--capacity", action="append", default=[])
    args = parser.parse_args(argv)
    try:
        text = read_input(args.input)
        if args.input.suffix.lower() == ".csv":
            data = parse_csv(text, args.reach_period, args.effort_unit, args.capacity)
        else:
            if args.reach_period is not None or args.effort_unit is not None or args.capacity:
                raise PrioritizationError("JSON input contains metadata; CSV metadata flags are not allowed")
            data = parse_json(text)
        report = plan(data)
        content = render_csv(report) if args.format == "csv" else json.dumps(
            report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output is not None:
            write_new_output(args.output, content)
        elif hasattr(sys.stdout, "buffer"):
            # Preserve UTF-8 and CSV CRLF even through a Windows text stream.
            sys.stdout.buffer.write(content.encode("utf-8"))
            sys.stdout.buffer.flush()
        else:
            sys.stdout.write(content)
        return 0
    except (PrioritizationError, OSError, UnicodeError) as exc:
        print(f"prioritize: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
