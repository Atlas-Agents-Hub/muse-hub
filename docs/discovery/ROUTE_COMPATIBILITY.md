# Muse CLI route reference

Compare two saved revisions of the Muse CLI route table. For personal Muse chat, side chats, history, and setup, use the [terminal guide](../TERMINAL.md).

## Included route snapshots

The comparison uses two MIT-licensed `nikships/muse-cli` revisions, identified by immutable commits and Git blob hashes. The fixtures preserve every method name and the HTTP/path details for the eight names whose definitions changed.

| Source | Earlier revision | Later revision |
| --- | --- | --- |
| Commit | `dbc7624368fd3aec20258c545f50654dbc92cc5f` | `b62adbabb77abf688d26a74f93d405b6667dbc9f` |
| Git blob SHA-1 | `bfdb6b492290c1dd8827087f2f49ab8046f56664` | `6634f1b09d7e98b235bd24bdf3397391689cf981` |
| Method names | **258** | **402** |
| Name-only entries | 250 | 394 |
| Entries with full details | 8 | 8 |

[Earlier route table](https://github.com/nikships/muse-cli/blob/dbc7624368fd3aec20258c545f50654dbc92cc5f/src/muse_cli/routes.json) · [Later route table](https://github.com/nikships/muse-cli/blob/b62adbabb77abf688d26a74f93d405b6667dbc9f/src/muse_cli/routes.json) · [MIT license](route-compat/NIKSHIPS-MIT.txt)

The later file adds **146 method names**, omits `feed.ingest` and `feed.unit.share`, and changes eight definitions. Use this reference when comparing client versions; check the client and connected account for current service behavior.

## Changed definitions

| Method(s) | Change in the route table |
| --- | --- |
| `chat.subscribe` | Adds `requestTimeoutMs` with a value of 30,000. |
| `connectors.accounts_link` | Adds a `capabilities` query placeholder. |
| `custom_connectors.register` | Changes aliases from a serialized JSON string to a list. |
| `node.list`, `node.register`, `node.heartbeat`, `node.unpair`, `node.disconnect` | Uses the same list representation for aliases. |

The other 396 distinct method names are stored as name-only entries. The report identifies the revision in which each name appears and whether full route details are available.

## Compare revisions

From a checkout with Python 3.12+:

```sh
python -B tools/compare_muse_routes.py --expect 258,402,146,2,8
python -B tools/compare_muse_routes.py --out /path/to/new-report.json
```

The comparator reads the saved JSON files with Python's standard library and produces a repeatable JSON report. Choose a new `--out` destination to preserve previous reports.

Use `--old` and `--new` to compare your own route files. Inputs must be UTF-8 JSON within the documented size limit. The parser checks duplicate methods, unknown fields, aliases, relative paths, and traversal attempts. The included snapshots are checked against their SHA-256 digests before comparison.

## License and setup

The projected identifiers and eight definitions are provided under the included `nikships/muse-cli` MIT notice. Retain the source revisions and notice when reusing this reference.

[Set up Muse in your terminal](../TERMINAL.md) · [Computer and device resources](https://atlas-origins.github.io/muse-ai-agent-presets/public/index.html?route=desktop)
