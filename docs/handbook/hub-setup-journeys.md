# Setup and recovery

Use this checklist to get a specialist working, keep its results, and reopen the workspace later.

## Start an assistant

1. [Choose a specialist](../DOWNLOAD_A_SPECIALIST.md) and download its ZIP.
2. Extract it into a new folder and open `START_HERE.md`.
3. Configure its Main instructions and three subchats through your assistant's supported setup.
4. Try the included first task with your own files and context.

[Get started](../GETTING_STARTED.md) explains the steps. [Terminal](../TERMINAL.md) covers personal Muse chat and local commands.

## Check a local tool

From a toolkit checkout with Python 3.12+:

```sh
python -B quickstart.py --all
python -B tools/muse_collection.py demo data-engineer
python -B examples/daily_desk.py
```

Read the printed result and open any generated report. Use a new destination for exports so existing work is preserved.

## Open and reopen your notebook

Follow [Companion Home](../COMPANION_HOME.md#open-companion-home) or [Daily Desk](../spaces/DAILY_DESK.md). Keep the database in a private directory outside the application folder. The server prints a local URL and temporary session token. Use the URL on the same computer, and stop the server with Ctrl+C when finished.

Restart with the same database path to reopen saved work. Use the newly printed token. If a save was interrupted, refresh saved records and reconcile the original result before another write.

## Update or remove a setup

Compare the new package with your original and customized copies. Preserve memory, preferences, credentials, and task outputs. Back up local databases before moving or removing them. Manage connected accounts and scheduled jobs through the original service.

## Developer diagnostics

The repository includes a read-only setup index that checks its feature register, source paths, and role guides:

```sh
python -B tools/hub_journeys.py --verify
python -B tools/hub_journeys.py --all --format markdown
```

For a named regression command printed by that index, use the portable runner from the repository root:

```sh
python -B scripts/run_source_test.py test_companion_home_h14_h17.py
```

The runner sets up the package import path and returns the selected suite's exit status. The setup index displays commands for you to choose; it reads the checkout without running them.

[Setup and saved data](../INSTALL_AND_PERSISTENCE.md) · [Host setup](../HOST_COMPATIBILITY.md) · [Development](../DEVELOPMENT.md)
