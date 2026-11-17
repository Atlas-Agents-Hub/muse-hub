# Muse Hub — offline Muse CLI route compatibility (H03)

**Scope:** source-code research and deterministic local comparison. This is **not** a Muse API client, a connected account, a verified backend inventory, or a transport authorization.

It is not a Muse API client.

## What was verified

The two public, MIT-licensed `nikships/muse-cli` source revisions were read at their immutable commits, and their **Git blob SHA-1s** checked against the original research pins. The included fixtures are byte-identical to the earlier Muse Hub H03 projections. They preserve every method name but carry full HTTP/path details **only for the eight names with observed differences**.

| Pinned source | Earlier | Newer |
| --- | --- | --- |
| Commit | `dbc7624368fd3aec20258c545f50654dbc92cc5f` | `b62adbabb77abf688d26a74f93d405b6667dbc9f` |
| Blob SHA-1 | `bfdb6b492290c1dd8827087f2f49ab8046f56664` | `6634f1b09d7e98b235bd24bdf3397391689cf981` |
| Method names | **258** | **402** |
| Name-only projections | 250 | 394 |
| Detailed projections | 8 | 8 |

[Earlier original route table](https://github.com/nikships/muse-cli/blob/dbc7624368fd3aec20258c545f50654dbc92cc5f/src/muse_cli/routes.json) · [Newer original route table](https://github.com/nikships/muse-cli/blob/b62adbabb77abf688d26a74f93d405b6667dbc9f/src/muse_cli/routes.json) · [Donor MIT license](route-compat/NIKSHIPS-MIT.txt)

The source-diff yields **146 added method names, two names absent from the newer file, and eight changed definitions**. The absent names are `feed.ingest` and `feed.unit.share`. This is a *historical source delta*, not proof that the live service added or removed any endpoint.

## What changed in the eight detailed rows

| Method(s) | Source-level change | Operational interpretation |
| --- | --- | --- |
| `chat.subscribe` | `requestTimeoutMs` introduced, 30,000 | Source change; behavior requires separately authorized runtime testing |
| `connectors.accounts_link` | Adds `capabilities` query placeholder | URL-template change; do not infer credentials or permissions |
| `custom_connectors.register` | Alias list serialized as JSON string → list | Representation difference |
| `node.list`, `node.register`, `node.heartbeat`, `node.unpair`, `node.disconnect` | Same alias serialization difference | Representation difference, not an independently demonstrated breaking API change |

All **396 other names** in the union lack a full route definition in these projections. The comparator retains each row's observed version(s), whether full details exist, and `live_availability: NOT_TESTED`. It does not execute any method.

## Run it locally

From a source checkout with Python 3.12+:

```sh
python -B tools/compare_muse_routes.py --expect 258,402,146,2,8
python -B tools/compare_muse_routes.py --out /path/to/new-report.json
python -B -m unittest discover -s tests -p test_muse_route_compat_h03.py -v
```

The comparator uses Python's standard library, reads local JSON, produces deterministic JSON and **never makes network requests**. The `--out` destination must not already exist; it does not overwrite prior evidence.

With `--old` and `--new` custom files, the report is explicitly marked `UNVERIFIED_CUSTOM_INPUT_NOT_LIVE_PROVIDER`. Inputs are size-bounded, must be UTF-8 JSON, and reject duplicate methods, unrecognized fields, unsafe aliases, malformed relative paths and encoded traversal. The two default fixtures are pinned to exact SHA-256 digests. Source pins prove file identity, **not** live account availability.

## What this does not establish

No host-specific Muse session, authorized Personal Muse terminal (original H04), account pairing, Gadget/Noise transport, node enrollment, Family Link, five-door execution or cross-account call has been exercised. These require separate owner-scoped admission and independently observed results.

The projected identifiers and eight changed definitions are attributed to `nikships/muse-cli` under its included MIT notice; third-party source code and credentials are not bundled. Keep the original source snapshots and the evidence of their exact revisions when researching later versions.
