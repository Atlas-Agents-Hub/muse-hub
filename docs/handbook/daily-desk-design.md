# Daily Desk design

Daily Desk combines task and note editing, saved revisions, reopening, and backup restoration in a local browser workspace. [Open Daily Desk](../spaces/DAILY_DESK.md) for the launch and usage guide. This page describes the implementation decisions to preserve when extending it.

## Storage and service

Daily Desk reuses `PersonalCompanion` storage helpers and the existing `SpaceCompanion` HTTP adapter. Tasks and notes live in the selected SQLite database. Browser sessions use the adapter's loopback, Host/Origin, token, JSON, body-size, and content-security-policy checks.

The application supplies the owner and Space scope through its trusted service boundary. Browser-provided owner fields must never establish authority. Keep the existing Space request and callback controls separate from task and note editing.

## Revision-checked writes

Each record has a stable ID and revision. Each mutation carries an operation ID bound to its exact request. An identical retry returns the original result; conflicting reuse is refused. A stale expected revision must leave the newer saved record intact and keep the user's draft available for comparison.

The UI shows empty, loading, saved, error, and recovery states. Keyboard controls, readable labels, narrow layouts, and explicit conflict actions are part of the normal workflow. Conversation can help organize a task, while the database remains the source of saved state.

## Backup and restore

Export a consistent snapshot and restore it into a new empty store. Task and note IDs, revisions, content, and receipt history must match the exported snapshot. A restored store receives a new database-instance identity so a pending browser write cannot accidentally target a replacement store.

Never restore over an existing database. Verify the archive and migration compatibility, show the result, and let the user choose the restored store. Keep the original database and archive until that review is complete.

## Recovery

If an update's result is uncertain, read its original operation before issuing a new ID. Preserve conflicting versions and let the user reconcile them. Inspect the original restore destination after an interrupted publication; keep partial output available for diagnosis.

## Verification

A useful end-to-end check creates three tasks and two notes, edits one of each, reopens the workspace, exports it, and restores into a new database. Compare IDs, fields, revisions, and hashes.

Regression coverage includes malformed input, wrong owner or Space, duplicate requests, conflicting operation IDs, stale revisions, lost responses, interruption, consistent export, corrupt archives, occupied destinations, traversal, symlinks, and reopening in a separate process. Browser checks cover keyboard use, labels, narrow screens, preserved drafts, and refusal of a write to the wrong store.

[Daily Desk](../spaces/DAILY_DESK.md) · [Architecture](../ARCHITECTURE.md) · [Development](../DEVELOPMENT.md)
