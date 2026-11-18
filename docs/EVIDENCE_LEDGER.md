# Evidence Finder: local durable evidence custody

Save exact text findings and linked receipts in a local SQLite evidence ledger.

EvidenceLedger combines exact-text search with local SQLite storage and SHA-256-linked receipts. Use it to keep the source, search result, and operation history together.

## Quick start

From the toolkit root with Python 3.12+:

    PYTHONPATH=src python3 -B examples/evidence_ledger_demo.py

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python -B`. The regression command is `PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_evidence_ledger.py -v`; on Windows use the same PowerShell import-path setting.

The example uses only fictional data and an ephemeral temporary directory. It records a complete exact-text finding and an explicit NOT_FOUND, deletes the source, and reopens the recorded evidence in a separate SQLite connection.

A different specialist role uses the same source API:

    from muse_presets.evidence_ledger import EvidenceLedger, EvidenceScope

    # Example scope; an application resolves its real users in the host callback.
    scope = EvidenceScope('demo-owner', 'demo-workspace',
                          'research-evaluator', 'demo-operator')
    with EvidenceLedger('/absolute/path/to/local.sqlite3',
                        authority=lambda: scope) as evidence:
        saved = evidence.capture('/path/to/owned/source-root', 'note.txt',
                                 'literal phrase', operation_id='unique-op-id')
        restored = evidence.read('unique-op-id')
        proof = evidence.verify()

When integrating the ledger, provide an authenticated authority callback and source permissions on every call. `EvidenceScope` carries the resolved scope; the host establishes the identity.

## Exact behavior

The existing bounded Finder searches one explicitly supplied UTF-8 file under an allowed root, refusing traversal and symlinks. The ledger stores its exact source digest, query and whole original text for FOUND records. A NOT_FOUND receipt stores the source digest and scope but no full absent-match source text. It preserves the original observed negative result without independently proving the absence after source deletion.

Records are partitioned by owner/workspace/role/actor labels, checked through the host-supplied callback. On each read, verify or capture the complete local chain is validated before returning a result. An identical operation ID and input preserves its first receipt, even if the source later disappears; a changed request under the same operation ID refuses. A changed source under a new operation ID creates a distinct record.

The SQLite chain keeps a separate local head. Truncated history, ordinary row deletion and byte modifications are detected. A local chain is NOT a cryptographic signature, immutable ledger or externally anchored anti-rollback system: someone who can rewrite both rows and head can forge another valid-looking history.

## Keep evidence private

Supply the exact source file and allowed root for the task. Confirm access through the host before capture, and review what the record supports before using it in a conclusion. Delivery, approvals, and other external actions belong to the service handling that task.

SQLite retains actual matched document text. Integrators must keep it in the owning user's protected workspace, apply retention and deletion rules and avoid committing real databases to public repositories.

Use Evidence Finder across [specialist tasks](CAPABILITIES.md). An integrated host must verify the user, permitted sources, and current scope before each operation.
