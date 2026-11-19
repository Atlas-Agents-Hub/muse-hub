"""Build task starter packages, executable toolkits and worked examples."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('collection_bundle_exporter', ROOT/'tools/muse_collection.py')
if SPEC is None or SPEC.loader is None:
    raise RuntimeError('collection exporter unavailable')
collection = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(collection)


def json_bytes(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False)+'\n').encode()


def verify_package(raw: bytes) -> int:
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        if archive.testzip() is not None:
            raise ValueError('PACKAGE_CRC_FAILURE')
        manifest = json.loads(archive.read('MANIFEST.json'))
        if set(archive.namelist()) != set(manifest['files']) | {'MANIFEST.json'}:
            raise ValueError('PACKAGE_MEMBER_ROSTER_MISMATCH')
        for name, expected in manifest['files'].items():
            if hashlib.sha256(archive.read(name)).hexdigest() != expected:
                raise ValueError('PACKAGE_MEMBER_HASH_MISMATCH')
        return len(manifest['files'])


def build_bundle() -> bytes:
    data = collection.prepare_collection(collection.load_collection(collection.DEFAULT_ROOT))
    counts = (len(data['specialists']), len(data['skills']), len(data['workflows']), len(data['starters']))
    if counts[0] != 15 or counts[1] < 75 or counts[2] < 25 or counts[3] < 100:
        raise ValueError('COLLECTION_INVENTORY_CHANGED_REVIEW_BUNDLE_CONTRACT')
    files = {}
    verified_entries = 0
    for starter in data['starters']:
        payload = collection.build_bytes(data, starter['id'])
        verified_entries += verify_package(payload)
        files['starters/'+starter['id']+'.zip'] = payload
    for role in collection.EXTENSION_ROLES:
        payload = collection.build_file_map_bytes(collection.specialist_kit_files(data, role))
        verified_entries += verify_package(payload)
        files['kits/'+role+'.zip'] = payload
        files['reports/'+role+'.json'] = json_bytes(collection.specialist_demo(data, role))
    for workflow in data['workflows']:
        if workflow.get('tool_bindings'):
            files['reports/'+workflow['id']+'.json'] = json_bytes(collection.workflow_demo(data, workflow['id']))
    files['SPECIALISTS.json'] = json_bytes(data['specialists'])
    files['COUNTS.json'] = json_bytes({'specialists_catalogued':counts[0], 'skills':counts[1],
        'workflows':counts[2], 'starters_packaged':counts[3],
        'standalone_extensions_packaged':len(collection.EXTENSION_ROLES)})
    files['LICENSE'] = collection.PROJECT_LICENSE.encode()
    files['START_HERE.md'] = """# Task starters and Python toolkits

Choose a task starter for your next project or run one of the four included Python toolkits.

## Start a task

Extract one ZIP from `starters/`, open `START_HERE.md`, and give Muse your task and source material. Keep your assistant's established preferences and memory.

## Run a toolkit

Extract one ZIP from `kits/` and run with Python 3.10 or newer:

```sh
python -B run.py --demo
```

Choose `data-engineer`, `reliability-engineer`, `automation-engineer` or `product-interface-designer`. Each toolkit includes its input examples and a working guide. For your own input object, use `python -B run.py --tool SKILL_ID --input input.json`.

## Compare examples

`reports/` contains the calculated results of the included examples. Use their inputs and output shapes to prepare your own records. `SPECIALISTS.json` lists the full specialist catalog; get complete specialist downloads from [Muse Hub](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html).

`BUNDLE_MANIFEST.json` records each file's checksum. Every nested ZIP includes its own manifest.
""".encode()
    manifest = {'schema':'muse-collection-distribution/v1', 'specialists_catalogued':counts[0],
        'skills':counts[1], 'workflows':counts[2], 'starters_packaged':counts[3],
        'standalone_extensions_packaged':len(collection.EXTENSION_ROLES),
        'nested_file_entries_verified':verified_entries,
        'local_example_reports':sum(name.startswith('reports/') for name in files),
        'files':{name:hashlib.sha256(raw).hexdigest() for name,raw in sorted(files.items())}}
    files['BUNDLE_MANIFEST.json'] = json_bytes(manifest)
    return collection.build_file_map_bytes(files)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--to', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.to.exists() or args.to.is_symlink():
            raise ValueError('EXISTING_OUTPUT_PRESERVED')
        payload = build_bundle()
        collection.write_new_pack(args.to, payload)
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            inventory = json.loads(archive.read('COUNTS.json'))
        print(json.dumps({'status':'COLLECTION_BUNDLE_BUILT_AND_REOPENED',
            'path':str(args.to), 'bytes':len(payload), 'sha256':hashlib.sha256(payload).hexdigest(),
            'starters':inventory['starters_packaged'],
            'standalone_extension_kits':inventory['standalone_extensions_packaged']},sort_keys=True))
        return 0
    except (ValueError, OSError, UnicodeError, KeyError, zipfile.BadZipFile) as exc:
        print(json.dumps({'error':str(exc)}),file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
