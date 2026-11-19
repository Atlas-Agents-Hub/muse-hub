---
name: context-agent
description: "Save session summaries, decisions, open tasks, and searchable project memory; restore a practical briefing when work resumes."
---

# Context Agent

Keep a project moving across sessions with structured summaries, a SQLite search index, and a concise restart briefing. Run the included Python helpers from this skill folder.

## Prepare the Session Records

The importer reads one JSON object per line. Place a conversation export in `data/imports/session.jsonl`, or set `CONTEXT_SESSION_DIR` to the folder containing your exports. Each conversation message uses this shape:

```json
{"type":"user","sessionId":"project-planning","timestamp":"2026-01-12T09:00:00Z","message":{"role":"user","content":"Let's use SQLite for the local prototype. Next: add the import screen."}}
{"type":"assistant","sessionId":"project-planning","timestamp":"2026-01-12T09:01:00Z","message":{"role":"assistant","content":"Decision: use SQLite. Pending: implement and test the import screen."}}
```

Use the actual conversation and task records. Existing Claude session exports also use this message format and can be imported directly. The helpers select the most recent JSONL file in the configured import folder.

## Initialize and Save

Python 3 and its standard SQLite module are sufficient. Initialize the local data folders, then save the current session:

```bash
python scripts/context_manager.py init
python scripts/context_manager.py save
```

The save command extracts topics, decisions, open tasks, changed files, and useful discoveries. It writes a session summary, updates `data/ACTIVE_CONTEXT.md`, and indexes the content for full-text search. Review extracted decisions against the actual conversation before using them as project instructions.

## Resume and Search

```bash
python scripts/context_manager.py load
python scripts/context_manager.py status
python scripts/context_manager.py search "rate limit"
```

Read the briefing into the current Muse conversation. Confirm the next action and check that referenced files still exist. Search returns matching summaries when a decision or earlier result needs more detail.

## Keep the Memory Useful

```bash
python scripts/context_manager.py maintain
```

Maintenance archives older sessions, compresses the active context, and rebuilds the search index. Keep a copy of the data folder before applying a new retention policy.

The helper writes a compact `MEMORY.md` to `data/memory/`. Set `CONTEXT_MEMORY_DIR` when a project needs a different output folder. Import files and generated memory stay in these configured locations; the package resolves its scripts and data relative to its own folder.

## Verify the Result

1. Confirm that a summary appears in `data/sessions/` and includes the correct session identifier.
2. Compare the decisions and pending work with the supplied conversation.
3. Run `status` and search for a distinctive phrase from the session.
4. Run `load` and check that the briefing identifies a concrete next action.

See [the context format](references/context-format.md) for the stored records and [compression rules](references/compression-rules.md) for retention details.
