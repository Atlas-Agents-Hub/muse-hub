---
name: inbox-triage
description: "The user wants an inbox summary, response priorities or drafts for selected messages."
---

# Triage Messages Without Sending

## Use when
The user wants an inbox summary, response priorities or drafts for selected messages.

## Not for
Sending messages, changing calendars or starting recurring work without the user-authorized route.

## Inputs
- The authorized messages or supplied thread exports
- Response priorities, tone and actions the user has permitted

## Procedure
1. Read the complete relevant thread in chronological order, including later corrections and owner replies.
2. Identify who currently owes the next response; a draft is not evidence of delivery and a copied request may already be resolved.
3. Classify using explicit due dates and the owner's stated rules. Separate suspicious financial or credential requests from ordinary priority work.
4. Minimize sensitive content in the summary. Keep original source IDs so a reviewer can reopen the decisive message.
5. Prepare only drafts supported by the thread, preserving recipient, attachments and commitments as distinct fields.
6. Before any authorized send or mailbox mutation, re-read the latest thread and confirm the exact target and whether the original operation already succeeded.

## Deliver
- A prioritized message-action list
- Draft replies with proposed external actions separated
- Return a queue with thread ID, decisive message ID, sender, explicit deadline, category, concise reason and proposed next action. Drafts include unresolved placeholders rather than fabricated promises. Mark archive/send/label states as proposed unless observed through the original service.

## Check the result
- Already resolved threads are not reopened.
- Drafts do not invent availability, promises or attachments.
- No message is sent or moved merely because a draft was produced.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve thread and message IDs, last read timestamp, pending drafts and original mutation IDs. Never preserve passwords or unnecessary message bodies in a generic skill package.

## Example request
Summarize these six threads and draft replies to the two that need decisions; do not send anything.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

