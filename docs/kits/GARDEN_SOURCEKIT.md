# Garden records tool

Build an application that keeps garden events and reviewed date changes in SQLite. This portable kit includes the Garden engine, a disposable worked example, regression checks, a role guide, and license information. Use Python 3.12+ after extraction. For assistant-guided planning, start with [Garden Companion](../../presets/garden-companion/INSTALL.md).

## Build and verify

From this repository, with a new output filename outside the source directory:

    PYTHONPATH=src python3 -B examples/export_garden_sourcekit.py --to "$HOME/garden-sourcekit.zip"
    PYTHONPATH=src python3 -B examples/export_garden_sourcekit.py --verify "$HOME/garden-sourcekit.zip" --sha256 EXPECTED_SHA256

Replace `EXPECTED_SHA256` with the digest from your trusted release record or retained export result. On Windows PowerShell, set `$env:PYTHONPATH='src'` and use `python` instead of `python3`. Output is create-only. Verification requires both an external archive digest and exact equality with a regenerated canonical artifact. It does not parse or decompress the supplied archive. Recompressed equivalents, appended bytes, modified manifests and any noncanonical ZIP are refused rather than interpreted.

## Use the extracted kit

Verify the archive digest from a separately trusted release record before extraction. Extract into a new directory, then run:

    python -I -B run.py --operation demo
    python -I -B run.py --operation self-test

The demo creates a temporary SQLite database, proposes and approves a date shift with fictional users, reopens the saved state, and recovers the operation receipt. It removes the sample database when finished. Follow the [calendar integration guide](../GARDEN_LOCAL_CALENDAR.md) to store your own records in an application. The original bundled tests cover local owner/specialist separation, cross-owner isolation, wrong decisions, stale events, transaction rollback and interrupted/repeated operations. The source-pinned runner refuses modified source, rehashed altered manifests, extra import-shadow files and linked kit paths before importing package code.

Use the bundled `muse_presets.garden_calendar` API in your application. Resolve accounts and permissions through a trusted host callback, and keep that callback separate from model or browser input. Keep user databases outside the kit, protect the database directory, and run reviewed code with the permissions you intend it to have. SQLite stores readable data.

## Connect services and update

The kit records and reviews local garden plans. To connect an external calendar or weather service, follow its [connector setup](../connectors/README.md) and choose the account and permissions needed for that task.

Use the release page to check the publisher and the package checksum to verify your download. For an update, extract the new kit into a separate folder and keep your existing database. Back it up and check storage compatibility before moving your records.

Run packaging and original engine regressions:

    PYTHONPATH=src python3 -B -m unittest discover -s tests -p "test_garden*.py" -v
