# Family Link — offline source handoff kit (H12)

This is a **source-only, independently runnable archive** of Muse Hub's existing `family.py` and `family_envelope.py` policy plus its two-process fictional demonstration. It does not add a transport, scheduler, identity provider, durable replay ledger, agent registration or cross-account messaging controller.

The exporter packages the accepted **15 disabled-by-default assistant role profiles**, local catalog and exact dependency modules, source-level MIT license, and original two-process demo. It does **not** copy secrets, installed accounts, memory, connectors, owner state or private donor files. It leaves the separate original TaskGuard/retention P1 security hold unchanged.

## Build and verify from reviewed source

From a checked-out Muse Hub source tree with Python 3.12+:

macOS/Linux:

```sh
PYTHONPATH=src python -B examples/export_family_link_sourcekit.py --to /path/to/new-family-offline-kit.zip
PYTHONPATH=src python -B examples/export_family_link_sourcekit.py --verify /path/to/new-family-offline-kit.zip --sha256 YOUR_VERIFIED_EXTERNAL_SHA256
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -B examples/export_family_link_sourcekit.py --to C:\Temp\new-family-offline-kit.zip
python -B examples/export_family_link_sourcekit.py --verify C:\Temp\new-family-offline-kit.zip --sha256 YOUR_VERIFIED_EXTERNAL_SHA256
```

The exporter refuses to overwrite any existing destination or write the ZIP into its own source tree. A valid ZIP digest is printed during export. For external verification, obtain the expected digest from a **trusted, independently supplied source**, not from the candidate archive's embedded manifest. A local hash match detects changed bytes; it is not an operator signature or provider authorization.

Extract the ZIP to a **new directory**. From that extracted root run:

```sh
PYTHONPATH=src python -B examples/family_offline_handoff_demo.py
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` first and run the same Python command. The demo uses fictional findings and separate local processes. Its successful output is `LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED` with `separate_process_verified` and `replayed_id_refused` true; all effect, recipient, authentication, and durable-fence flags remain false. No paid API or network service is used.

## Integrity and security boundaries

- The input modules, catalog, and all 15 role profiles are pinned to the accepted Muse Hub `7069f062` source by explicit SHA-256. Future changes require deliberate pin review. Exact role IDs and disabled Family Link settings are verified; no role gets native grants.
- Archive members are fixed, sorted, deterministic and SHA-256 inventoried. The ZIP verifier requires a caller-supplied archive digest, rejects duplicate entries, unsafe paths, symlinks, unreviewed members, modified source pins and oversized content. The manifest is a *record*, never a permission grant.
- The existing `muse_presets.family_envelope` remains the one metadata/replay-shape implementation. Local declared consent and caller-provided history are untrusted. Real sender and recipient identities, durable replay fences, recipient readback, and policy admission remain **NOT VERIFIED**.
- Distribution validation and source tests evaluate a portable archive, **not** actual Family Link delivery or native Muse skills installed into a live account.

## Engineering acceptance

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -p test_family_sourcekit.py -v
PYTHONPATH=src python -B -m unittest discover -s tests -p test_family_envelope.py -v
python -B scripts/check_public.py
```

For authoritative product claims, see [Family Link source contract](../FAMILY_LINK.md), [source and host limits](../handbook/source-and-host-capabilities.md), and the repository's [public release status](../RELEASES.md). This kit's presence in Git does **not** imply it is included in the currently published release.
