# Family Link handoff kit

Prepare and review a task handoff with the receiving role, useful context, and an expected result. The kit includes 15 role policies, envelope checks, a worked example that runs in two processes, and the MIT license.

## Build and verify

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/export_family_link_sourcekit.py --to "$HOME/family-link-kit.zip"
PYTHONPATH=src python3 -B examples/export_family_link_sourcekit.py --verify "$HOME/family-link-kit.zip" --sha256 EXPECTED_ZIP_SHA256
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python` instead of `python3`. Choose a new destination outside the toolkit in an existing directory. Replace `EXPECTED_ZIP_SHA256` with the expected digest from your trusted release record or retained export result.

The exporter preserves existing files. The verifier checks the exact archive digest, member list, paths, and source hashes before you extract the package.

## Try a handoff

Extract into a new directory and open a terminal there:

```sh
PYTHONPATH=src python3 -B examples/family_offline_handoff_demo.py
```

Use the PowerShell import-path setting above on Windows. The example prepares a fictional task and reviews it in a separate process. Its report includes `LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED`, `separate_process_verified`, and `replayed_id_refused` so you can inspect exactly what happened.

For your work, choose the receiving specialist, provide the task and relevant sources, and review the proposed handoff. Send it through the account or communication route you selected, then check delivery and the returned result in that service. Keep the operation ID so an interrupted action can be reconciled before another send.

## Integrate with your tools

`family.py` supplies role policies and `family_envelope.py` checks envelope fields and replay declarations. Use your host's verified account and permission checks for sender and recipient identity. Caller-provided consent fields or history are input records; the receiving service establishes access and delivery.

Package verification checks all 15 role profiles and their current configuration. Source updates require reviewed hash changes. Keep credentials, personal memory, and task data in your private workspace.

## Developer checks

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_family_sourcekit.py -v
PYTHONPATH=src python3 -B -m unittest discover -s tests -p test_family_envelope.py -v
```

[Family Link guide](../FAMILY_LINK.md) · [Tools and connections](../handbook/source-and-host-capabilities.md) · [Downloads](../RELEASES.md)
