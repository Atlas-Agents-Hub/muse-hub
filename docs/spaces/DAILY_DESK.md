# Daily Desk: tasks, notes, and saved progress

Keep tasks and notes together in Daily Desk. Edit records in your browser, reopen them later, resolve conflicting edits, and back up your work. Daily Desk stores your records in a SQLite database on your computer.

## Try the worked example

From a checkout with Python 3.12+:

```sh
python -B examples/daily_desk.py
```

Use `python3` on macOS or Linux where appropriate. The command uses Python's standard library. It creates three sample tasks and two notes, edits and reopens them, checks conflicting and repeated updates, then backs up and restores the records in temporary storage. Read the result for each check.

## Open your desk

```sh
python -B examples/daily_desk.py --serve --database "$HOME/daily-desk.sqlite"
```

The same command works in PowerShell. Choose a path in an existing private directory. Use a new filename for a fresh desk or the same path to reopen an existing one. The launcher creates a sibling `daily-desk-restores` directory for restored databases; use `--restore-directory` with an absolute path to choose another location.

Open the **127.0.0.1 URL printed in your terminal** on the same computer and enter the session token. Keep the terminal running while using the desk. Press Ctrl+C to stop it.

The page keeps the token in memory for the current session. Enter it again after reloading. Restarting the launcher creates a new token. Keep this development server on your computer; use a production server and authentication when building a shared application.

## Work with tasks and notes

Create a task with a clear title and, optionally, a due time. Due times appear in your local time zone. Mark a task done when you finish it. For scheduled notifications, use [Muse reminders](https://www.meta.com/help/superintelligence/1484325780075655/). Notes store plain text, including emoji.

Select a saved record to edit it. Each record has a revision; if another tab saves a newer version, Daily Desk keeps your draft and asks you to resolve the conflict. Choose **Load saved version** when you want to compare the latest saved text before applying an edit.

**Refresh saved work** reloads the list while preserving your open draft. **Lock session** hides the workspace and clears the page's token. Your saved tasks and notes remain in the database.

## Recover an interrupted save

Each save has an operation ID tied to its content and expected revision. Repeating the same save returns its recorded result. Daily Desk refuses to reuse that ID for different content.

If a response disappears, choose **Check saved receipt** first. The page reopens a saved result when it exists. Otherwise, choose **Retry the exact write** to repeat the original operation. Keep the same database open while resolving the save.

Until confirmation, the page retains the pending content and operation ID in the tab's session storage. Your browser may restore that text when reopening a session. Use its privacy controls to clear the tab when needed.

## Back up and restore

Choose **Download backup** to save a JSON archive of tasks, notes, deleted-note records, and write receipts. Its checksum lets Daily Desk detect changed archive content. Keep the backup in protected storage because receipts can include earlier note text.

Choose the file and a new store name in the restore panel. Daily Desk validates the archive, checks a staging database, and creates a new database while preserving existing files. **Check restore result** reopens the chosen destination if the reply was interrupted. Check that result before trying another restore.

To open the restored desk, stop the launcher and restart with the restored database path:

```sh
python -B examples/daily_desk.py --serve --database "$HOME/daily-desk-restores/desk-restored.sqlite"
```

You can also restore from the terminal:

```sh
python -B examples/daily_desk.py --restore "$HOME/daily-desk-backup.json" --database "$HOME/restored-desk.sqlite"
```

Choose a new destination. Restoration preserves record IDs, content, revisions, and operation receipts. It assigns the restored database a new instance ID so a pending save from another desk cannot be applied to it accidentally.

## Storage and limits

| Item | Limit |
| --- | --- |
| Tasks | 256 records |
| Notes | 256 records |
| Task and note operation receipts | 1,024 records |
| Backup archive | 16 MiB |
| Task title | 160 characters |
| Note text | 8,000 characters |

Daily Desk preserves existing history when a limit is reached and reports the operation it could not complete. Keep exports and records within these limits; use a separate new database when you need a fresh workspace.

SQLite databases and backup archives contain readable text. Protect their directories and backups using your operating system's access controls. Write receipts may retain older note text after an edit or deletion, so include them in your retention decisions. Follow your storage system's procedures when permanent erasure is required.

The backup contains the desk's tasks, notes, and write receipts. Keep your separate service settings, preferences, and credentials in their own protected storage.

## Developer reference

`DailyDesk` extends `PersonalCompanion` using its account and workspace scope, path checks, SQLite connection, and transactions. Notes use `companion_notes`; tasks, operation receipts, and the database-instance ID use additional tables. Enable desk mode through the existing server factory.

The host resolves user access. The HTTP layer checks loopback requests, origins, session tokens, JSON fields, and body size. Restore operations validate paths and create a new destination without replacing existing data. After a process or power interruption, inspect the original restore destination before retrying.

```sh
PYTHONPATH=src python3 -B -m unittest discover -s tests -p 'test_daily_desk*.py' -v
```

On PowerShell, set `$env:PYTHONPATH = "src"` and use `python`. The tests cover atomic saves, rollback, concurrent edits, duplicate and conflicting operations, user separation, database migration, reopen, archive validation, restore races, and HTTP requests. Open the desk to check editing, recovery, and restore in your browser.

[Companion Home](../COMPANION_HOME.md) · [Space workspace](OPTIONAL_SPACE_STARTER.md) · [Document recovery](../handbook/durable-documents.md) · [Data design](../handbook/daily-desk-design.md)

Implementation references: [SQLite transactions](https://www.sqlite.org/lang_transaction.html) and [SQLite isolation](https://www.sqlite.org/isolation.html).
