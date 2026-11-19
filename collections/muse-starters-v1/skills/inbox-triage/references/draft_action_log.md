# Record and check inbox operations

Keep a separate action log with one operation per line. Record tool names, thread IDs, draft IDs and results. Keep quoted message text in the source thread so operation names mentioned by a correspondent do not enter this check.

Example draft run:

```text
gmail.users.messages.list -> message_ids=example-1,example-2
gmail.users.messages.get -> message_id=example-1
gmail.users.drafts.create -> draft_id=example-draft-1,thread_id=example-thread-1
```

Check it from the extracted package folder:

```sh
python -B skills/inbox-triage/scripts/draft_safety_validator.py --action-log YOUR_ACTION_LOG.md --output json
```

The checker identifies common Gmail, Microsoft Graph and generic send-operation names, including `users.drafts.send`, `users.messages.send`, `me/sendMail`, `me/messages/ID/send`, `send_email` and `schedule_send`. It also recognizes namespaced forms such as `mcp__gmail__send_email` and reports each matching line once.

| Exit code | Result | Next action |
| --- | --- | --- |
| 0 | `PASS`: no matching send name in this log. | Complete the draft readback and save the report. |
| 1 | `FAIL`: a matching operation appears. | Inspect the line and reconcile the service result before retrying. |
| 2 | Empty, invalid or unreadable input. | Supply the complete action log and check again. |

Use the same check on proposed operation names before calling a service and on the recorded operation log afterward. Record any separately authorized sending task in its own action log.

[Workspace walkthrough](../INBOX_WORKSPACE.md)
