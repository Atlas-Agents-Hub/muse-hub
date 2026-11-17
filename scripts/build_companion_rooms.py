"""Build/check the neutral Companion Home room configuration for static previews.

No external requests, native agents, private user data or auto publishing.
The generated rooms.js file must be reproducible from reviewed rooms.json.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/"examples/companion_home"
SOURCE=DIRECTORY/"rooms.json"
OUTPUT=DIRECTORY/"rooms.js"
IDS=("focus","notebook","garden","arcade","studio")
THEMES=("signal","ivory","mint","coral","lavender")
ID=re.compile(r"[a-z][a-z0-9-]{0,39}\Z")


def render() -> bytes:
    def no_duplicates(pairs):
        doc={}
        for key,value in pairs:
            if key in doc:raise ValueError("DUPLICATE_CONFIG_KEY")
            doc[key]=value
        return doc
    raw=SOURCE.read_bytes()
    if len(raw)>16_384:
        raise ValueError("ROOM_SOURCE_TOO_LARGE")
    data=json.loads(raw.decode("utf-8"),object_pairs_hook=no_duplicates)
    if type(data) is not dict or set(data)!={
        "schema","native_muse_installed","room_local_chat",
        "global_assistant_external","rooms"
    }:
        raise ValueError("ROOM_CONFIG_SHAPE")
    if data["schema"]!="muse-hub/neutral-companion-home/v1":
        raise ValueError("ROOM_CONFIG_SCHEMA")
    if data["native_muse_installed"] is not False or data["room_local_chat"] is not False or data["global_assistant_external"] is not True:
        raise ValueError("FALSE_ROOM_AUTHORITY")
    rows=data["rooms"]
    if type(rows) is not list or len(rows)!=5 or tuple(x.get("id") for x in rows)!=IDS:
        raise ValueError("FIVE_ROOMS_REQUIRED")
    for room,theme in zip(rows,THEMES):
        if type(room) is not dict or set(room)!={"id","label","theme","feature_ids","description","kicker","prompt"}:
            raise ValueError("ROOM_FIELDS")
        if room["theme"]!=theme or not ID.fullmatch(room["id"]):
            raise ValueError("ROOM_ID_THEME")
        for key in ("label","description","kicker","prompt"):
            value=room[key]
            if type(value) is not str or not value.strip() or len(value)>180 or any(ord(x)<32 for x in value):
                raise ValueError("ROOM_TEXT")
        features=room["feature_ids"]
        if type(features) is not list or len(features)!=2 or len(set(features))!=2 or not all(
            type(x) is str and ID.fullmatch(x) for x in features
        ):
            raise ValueError("ROOM_FEATURE_IDS")
    return ("window.MUSE_HOME_CONFIG = Object.freeze("+
            json.dumps(data,sort_keys=True,ensure_ascii=False,separators=(",",":"),allow_nan=False)+
            ");\n").encode("utf-8")


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check",action="store_true")
    mode.add_argument("--write",action="store_true")
    args=parser.parse_args()
    try:
        generated=render()
        if args.check:
            if not OUTPUT.is_file() or OUTPUT.read_bytes()!=generated:
                raise ValueError("ROOMS_JS_STALE_OR_MISSING")
            print("COMPANION_ROOM_CONFIG_REPRODUCIBLE")
        else:
            if OUTPUT.is_symlink():
                raise ValueError("ROOMS_JS_SYMLINK_REFUSED")
            OUTPUT.write_bytes(generated)
            print("ROOMS_JS_WRITTEN_FROM_REVIEWED_JSON",len(generated))
    except (ValueError,OSError,UnicodeError,KeyError,TypeError) as exc:
        print("ROOM_CONFIG_REFUSED:"+str(exc),file=sys.stderr)
        return 2
    return 0

if __name__=="__main__":
    raise SystemExit(main())
