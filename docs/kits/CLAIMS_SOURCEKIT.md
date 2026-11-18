# Claims review tool

Review supplied claims against their evidence records and retain the reasoning behind a finding. This portable Python kit includes the claim checker, a role guide, a worked input, a runner, and integrity information.

## Build, verify and run

Requirements: Python 3.12+ and a trusted copy of this repository. No paid API, network or pip packages. From the repository root:

    PYTHONPATH=src python3 -B examples/export_claims_sourcekit.py --to /absolute/NEW/claims-adjudicator.zip
    PYTHONPATH=src python3 -B examples/export_claims_sourcekit.py --verify /absolute/NEW/claims-adjudicator.zip --sha256 EXTERNALLY_VERIFIED_SHA256

On Windows PowerShell, set $env:PYTHONPATH = "src" and use python.

The exporter refuses an occupied ZIP destination and mismatched original first-party source bytes. It creates a repeatable archive with a deterministic file list and ZIP metadata. An embedded SHA-256 receipt does **not** certify its publisher or independent reviewer.

After confirming the ZIP digest through a separately trusted release/source record, extract it into a new directory. Run:

    python -I -B claims-adjudicator/run.py --operation demo

The example returns `LOCAL_CLAIMS_DEMO_PASSED` with disposition `OVERCLAIM`. To assess an explicitly reviewed fictional or user-supplied JSON claim, pipe EXAMPLE_CLAIM.json into:

    python -I -B claims-adjudicator/run.py --operation assess --allow-reviewed-local

Missing opt-in, malformed/duplicate-key JSON, nonfinite values, invalid grades and altered source bytes are refused. The runner accepts at most 16 KiB of stdin and does not use an external provider. The imported code runs under the local account. Python isolation switches are **not an OS sandbox**.

## Operational boundary

The report compares the claim with the supplied evidence criteria. Read it alongside the original sources and record any remaining uncertainty before sharing your conclusion.

The verifier admits the complete member list, regular-file paths, exact expected sizes, compression method, header flags and total unpacked budget before opening any member body. Stored and DEFLATE members are supported; encryption and unsupported ZIP features are refused. Corrupt ZIP containers or compressed data produce a bounded `REFUSED` response and exit code 2, not a successful verification. The external archive digest and canonical source-byte comparisons remain required.

Run both the source-kit and archive-boundary regressions:

    PYTHONPATH=src python3 -B -m unittest discover -s tests -p "test_claims*.py" -v

Keep the original kit and a separate working copy when updating. [Claims Adjudicator setup](../../presets/claims-adjudicator/INSTALL.md) includes the assistant package and first task.
