# Review your inbox and keep the next run in sync

Turn a set of email threads into a short action queue, useful reply drafts and a saved handoff. The included Python helpers read your preferences, calculate the next search interval and check recorded email operations.

Use Python 3.10 or newer. The commands below run from the extracted package folder and use only the Python standard library.

## Try the included workspace

```sh
python -B skills/inbox-triage/scripts/kb_reader.py --workspace skills/inbox-triage/examples --output json
python -B skills/inbox-triage/scripts/search_window_calculator.py --cadence 2x-daily --now 2026-11-18T18:00:00Z --output json
python -B skills/inbox-triage/scripts/draft_safety_validator.py --action-log skills/inbox-triage/examples/Email/triage-log/example-run.md --output json
```

The example returns a ready workspace, a search interval beginning at 04:00 UTC, and a passing action-log check. The sample messages and operation IDs illustrate the format.

## Prepare your preferences

Copy `skills/inbox-triage/examples/Email/` into your project folder and customize the four Markdown files. You can also use Muse's **Inbox Setup** skill to build these preferences from your existing email habits.

| File | Put here |
| --- | --- |
| `Email/email-taxonomy.md` | Message categories, classification rules and report preferences. |
| `Email/email-patterns.md` | Your voice, hard rules and sign-off preferences. |
| `Email/blocklist.md` | Senders and patterns to skip; use `None` for an empty list. |
| `Email/tracker.md` | Current follow-ups, deadlines and resolved items. |
| `Email/triage-log/` | One report and action log per run. |

Optional `evaluation-framework.md` and `rate-card.md` hold opportunity criteria and pricing preferences. The [workspace contract](references/kb_file_contract.md) describes the required headings.

Check your working copy before reading mail:

```sh
python -B skills/inbox-triage/scripts/kb_reader.py --workspace YOUR_PROJECT --output json
```

Correct any missing files or malformed sections reported by the reader. It reads files up to 1 MB each and leaves them unchanged.

## Run the review

1. **Choose the account and interval.** Use the user's selected mailbox, folders and thread limit. For the first run, choose a cadence or an explicit `--override-hours`. For later runs, pass the last completed run's `window_end` through `--since`.
2. **Retrieve the complete interval.** Fetch every requested page, filter to `window_start <= message time < window_end`, and deduplicate overlapping results by message ID. Reopen complete threads so later replies and cancellations control the next action.
3. **Prepare the queue.** Classify each thread using the saved preferences. Include source IDs, explicit deadlines, the current response owner and a concise reason for its priority.
4. **Save replies as drafts.** Use the connected service's draft operation, retain draft IDs, and check each draft against the thread and the user's voice. Re-read a thread before changing an existing draft.
5. **Check the operation log.** Record the actual tool names and returned IDs, then run the log checker. A match returns exit code 1 and the matching line numbers; an empty or unreadable log returns exit code 2. Review a flagged operation against the provider's result before continuing.
6. **Save the handoff.** Record the queue, draft IDs, follow-ups, retrieval failures and the completed interval. Advance the checkpoint only after all requested pages and the report are complete. Keep the earlier checkpoint after an interrupted run.

```sh
python -B skills/inbox-triage/scripts/search_window_calculator.py --cadence 2x-daily --since 2026-11-18T18:00:00Z --now 2026-11-19T09:00:00Z --output json
```

This resumed review starts at 17:55 UTC on the previous day. The five-minute overlap covers the previous boundary; message IDs prevent duplicate drafts. UTC interval arithmetic handles different time-zone offsets. Cadence defaults are 26, 14 and 10 hours for one, two and three evenly spaced daily runs; an explicit checkpoint also covers longer interruptions. Review backlogs longer than 30 days in separate date ranges.

## Save a concise result

Use a new log filename for each run, such as `Email/triage-log/2026-11-19-morning.md`. Record:

- Account, folders, exact interval and whether retrieval completed.
- Thread and decisive message IDs, category, deadline and next action.
- Draft IDs and their current state.
- Tool-operation names and returned IDs, without message bodies or credentials.
- Follow-up changes and the checkpoint to use next time.

The [action-log format](references/draft_action_log.md) includes draft and send examples for the checker. For an empty inbox, still review overdue follow-ups and save the completed interval. For a partial retrieval, preserve the failure and resume from the previous checkpoint.

[Inbox method](SKILL.md) · [Examples and decisions](DEPTH.md)
