---
name: gmail-connector
description: "Email service by Google"
---

# Gmail for Muse

Email service by Google

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Gmail**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/index.ts).

## Actions

### Get Draft

Get a single draft email by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `draft_id` | The ID of the draft to read (obtain from List Drafts). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/get-draft-action.ts).

### Get Email

Read one email by its message ID, including attachments.

| Input | What to provide | Required |
| --- | --- | --- |
| `message_id` | Message_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/get-mail-action.ts).

### Get Label

Get a single label by its ID, including message and thread counts.

| Input | What to provide | Required |
| --- | --- | --- |
| `label_id` | The ID of the label to read (obtain from List Labels). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/get-label-action.ts).

### Get Profile

Get the connected mailbox profile.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/get-profile-action.ts).

### Get Thread

Get a thread from your Gmail account via Id

| Input | What to provide | Required |
| --- | --- | --- |
| `thread_id` | The thread Id of the mail to read | Yes |
| `format` | Format | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/get-thread-action.ts).

### List Drafts

List draft emails in the mailbox.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Optional Gmail search query to filter drafts (e.g. "subject:invoice"). | Optional |
| `max_results` | Maximum number of drafts to return (1-500). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/list-drafts-action.ts).

### List History

List mailbox changes since a given history ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `start_history_id` | Return changes after this history ID (obtain from Get Profile or a previous history result). | Yes |
| `history_types` | Limit results to these change types (leave empty for all). | Optional |
| `max_results` | Maximum number of history records to return (1-500). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/list-history-action.ts).

### List Labels

List all labels in the mailbox.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/actions/list-labels-action.ts).

## Events and recurring work

- **[New Attachment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/triggers/new-attachment.ts)** — Triggers for each attachment on a new email.
- **[New Conversation](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/triggers/new-conversation.ts)** — Triggers when a new email conversation (thread) begins
- **[New Email](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gmail/src/lib/triggers/new-email.ts)** — Triggers when a new email matching the filters arrives.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Gmail to get draft. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect gmail
```

Available HTTP reads: `read-gmail-v1-users-me-profile`, `read-gmail-v1-users-me-messages-message-id`, `read-gmail-v1-users-me-threads-thread-id`, `read-gmail-v1-users-me-labels`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
