# Observation comparison tool

Compare two recorded UI observation sequences with the included Python tool. The report identifies changed outcomes and added or removed controls so you can investigate application behavior. Use Python 3.12+ and observations collected for an authorized task.

## Create and verify a kit

From this repository:

```sh
PYTHONPATH=src python3 -B examples/export_reverse_sourcekit.py --to "$HOME/observation-comparison.zip"
PYTHONPATH=src python3 -B examples/export_reverse_sourcekit.py --verify "$HOME/observation-comparison.zip" --sha256 EXPECTED_SHA256
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python`. Choose a new ZIP filename in an existing directory outside the source tree. Replace `EXPECTED_SHA256` with the digest from the release page or your retained export result.

Verification compares the supplied checksum and exact expected archive bytes before extraction. Extract the verified kit into a new folder, open a terminal there, and run:

```sh
python -I -B run.py --operation demo
python -I -B run.py --operation self-test
```

The example compares a sample form's Save, Cancel, and Export results. It reports a changed Save response and added or removed controls. The self-test runs the ten included engine checks.

## Compare your observations

Create a JSON file outside the extracted kit. Use the following format, replacing the sample records with yours:

```json
{
  "schema": "muse-presets/reverse-offline-fixture-input-v1",
  "analysis_boundary": "OFFLINE_SUPPLIED_OBSERVATIONS_ONLY",
  "authorization_declaration": "OWNER_OR_PERMISSION_DECLARED_UNVERIFIED",
  "before": [{"action": "click", "target": "save", "outcome": "silent"}],
  "after": [{"action": "click", "target": "save", "outcome": "toast"}]
}
```

Then run:

```sh
python -I -B run.py --operation compare --fixture /absolute/path/fixture.json
```

Keep the schema and declaration fields as shown. The input limit is 128 KiB, with at most 256 observations on each side. Supported actions are `view`, `click`, `scroll`, and `hover`; use short symbolic names for targets. Each action-and-target pair must be unique within a sequence.

The result lists changed, added, and removed action-and-target pairs and the input file's SHA-256 digest. Keep the original observations so you can inspect a difference, reproduce it in the application, and investigate its cause. Confirm the target and your permissions before collecting further observations.

## Files, privacy, and updates

The kit includes the comparison engine, ten engine tests, specialist instructions, a license, and a runner. The runner checks file hashes, JSON fields, resource limits, and paths before importing the engine. Store observation files outside the kit and protect any private content they contain.

Run reviewed code with the permissions you intend it to have. Check the publisher through the release page and verify the download checksum. For updates, extract the new kit into a separate folder and retain your observation files and earlier reports.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_reverse_fixture.py -v
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_reverse_sourcekit.py -v
```

[Specialist setup](../../presets/reverse-engineering-researcher/INSTALL.md) · [Terminal](../TERMINAL.md)
