---
name: inbox-triage
description: "Review complete email threads, prioritize action, draft replies in your voice, and resume recurring inbox reviews from a saved checkpoint."
---

# Inbox Review and Reply Drafts

## Use when
Review complete email threads, prioritize action, draft replies in your voice, and resume recurring inbox reviews from a saved checkpoint.

## Not for
Sending messages, changing calendars or starting recurring work without the user-authorized route.

## Inputs
- The authorized messages or supplied thread exports
- Response priorities, tone and actions the user has permitted
- For recurring reviews, an Email/ preferences workspace and the last successfully completed search interval

## Procedure
1. For recurring work, validate the saved Email/ workspace and calculate the next search interval from the last completed run. Retrieve every requested page and deduplicate overlapping results by message ID.
2. Read the complete relevant thread in chronological order, including later corrections and owner replies.
3. Identify who currently owes the next response; a draft is not evidence of delivery and a copied request may already be resolved.
4. Classify using explicit due dates and the owner's stated rules. Separate suspicious financial or credential requests from ordinary priority work.
5. Minimize sensitive content in the summary. Keep original source IDs so a reviewer can reopen the decisive message.
6. Prepare only drafts supported by the thread, preserving recipient, attachments and commitments as distinct fields.
7. Before any authorized send or mailbox mutation, re-read the latest thread and confirm the exact target and whether the original operation already succeeded.
8. Save the action queue, draft IDs, follow-ups and operation log. Advance the completed-interval checkpoint only after retrieval and the report finish; preserve the earlier checkpoint after an interruption.

## Deliver
- A prioritized message-action list
- Draft replies with proposed external actions separated
- Return a queue with thread ID, decisive message ID, sender, explicit deadline, category, concise reason and proposed next action. Drafts include unresolved placeholders rather than fabricated promises. Mark archive/send/label states as proposed unless observed through the original service.

## Check the result
- Already resolved threads are not reopened.
- Drafts do not invent availability, promises or attachments.
- No message is sent or moved merely because a draft was produced.
- Queue facts and draft commitments agree with the complete thread history.
- The completed interval has no omitted pages; overlapping messages do not create duplicate drafts.

## Recover or narrow
Preserve thread and message IDs, the previous successful interval, pending drafts and original mutation IDs. Resume interrupted retrieval from that interval and reconcile existing drafts before creating replacements.

## Example request
Summarize these six threads and draft replies to the two that need decisions; do not send anything.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Keep inbox reviews in sync
Use the included [inbox workspace](INBOX_WORKSPACE.md) to load your preferences, calculate the next search interval and check the action log. Three local Python helpers and a complete example workspace support first-time setup and resumed reviews.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

