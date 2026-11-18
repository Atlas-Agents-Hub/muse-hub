# Keep documents useful and recoverable

Give important documents a stable home and a recoverable version history. Check that you can **save, find, reopen, back up, and restore** the files you depend on.

## First useful result

Start with a sample brief. Ask the assistant to save a new version through its file or document tool in a location you control. Then reopen that exact document and compare its title, three distinctive lines and version. Keep the file path or document link returned by the tool.

Make a second version with one small edit. Keep the first version. Export or back up through the supported provider, then restore the exported copy to a **new** destination and compare the contents. Confirm the restored copy before relying on the backup.

## A small document record

For each important artifact retain a logical ID, title, source version, last verified time, canonical location, content digest when available, attachment references, ownership and retention preference. Keep search/index status separate from the file's existence. A useful short memory entry can point to this record without duplicating the entire document.

User preferences, private source text, host-managed records and immutable shipped templates are different ownership classes. Keep your working documents outside the repository's managed source files. Never place credentials or private conversations in a public update or source ZIP.

## Verify

Compare copied files using a hash calculated from their bytes. For hosted documents, reopen the original and exported copy through the document service and compare their contents. Close and reopen the client to check that the saved version remains available.

For source kits, `python -B tools/collection_compatibility.py` checks that the packaged files match their expected versions. The [source-and-custody method](../../collections/muse-starters-v1/skills/source-and-custody/SKILL.md) gives a reusable evidence procedure. Do not overwrite managed source simply to place a personal note where the source checker expects a file.

## Failure and recovery

If saved content disappears from an answer, first distinguish a missing file from a retrieval failure. Reopen the canonical document directly using an approved tool. If the original is present but not indexed, give the assistant its exact reference; do not rewrite it to force discovery. If it is missing, preserve the error and recover a verified copy into a new location.

During upgrades use a three-way comparison: the previous template, the new template and your current edited bytes. Preserve unknown files and unresolved conflicts. Do not replace a long-lived MEMORY.md, database or notebook with a fresh template. Coordinate simultaneous edits so one writer preserves another's changes.

## Keep working

[Setup and saved data](../INSTALL_AND_PERSISTENCE.md) covers profile customization, updates, and recovery. [Daily Desk](../spaces/DAILY_DESK.md) provides a browser workspace for tasks and notes with backup and restore. For hosted documents, follow your document service's access, retention, and recovery settings.
