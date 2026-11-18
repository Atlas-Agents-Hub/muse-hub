# Family Link handoff kit

Prepare and review handoff records with the Family Link kit. It contains the role policies, envelope checks, and a worked two-process example using `family.py` and `family_envelope.py`.

The archive includes 15 role policies, their required modules, the MIT license, and the example. Keep your personal account configuration and working data in your private workspace.

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
- Use the generated handoff proposal as input to the communication route you choose. Check delivery and the returned result in that service.

## Engineering acceptance

```sh
PYTHONPATH=src python -B -m unittest discover -s tests -p test_family_sourcekit.py -v
PYTHONPATH=src python -B -m unittest discover -s tests -p test_family_envelope.py -v
python -B scripts/check_public.py
```

[Family Link](../FAMILY_LINK.md) · [Tools and connections](../handbook/source-and-host-capabilities.md) · [Downloads](../RELEASES.md)
