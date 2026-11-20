---
name: microsoft-outlook-connector
description: "Microsoft Outlook: add label to email, create draft email, find email."
---

# Microsoft Outlook for Muse

Microsoft Outlook: add label to email, create draft email, find email.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Microsoft Outlook**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{cloud}/{tenant}/oauth2/v2.0/authorize>
- Token endpoint: <https://{cloud}/{tenant}/oauth2/v2.0/token>
- **Cloud** (`cloud`): ProviderField
- **Access Mode** (`accessMode`): ProviderField
- **Tenant ID** (`tenant`): Use "common" for the default delegated multi-tenant flow. For app-only (Client Credentials), set this to your Directory (tenant) ID.
- **Mailbox (App-only)** (`mailbox`): Email/UPN or user object ID of the mailbox to act on. Required for app-only (Client Credentials). Leave blank for delegated access (acts as the signed-in user).

Provider scopes: `{accessMode}`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/index.ts).

## Actions

### Add Label to Email

Tag an email with one or more Outlook categories.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | Message Id | See action definition |
| `categories` | Category names to add, one per row. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/add-label-to-email.ts).

### Create Draft Email

Save a new email to your Drafts folder without sending it.

| Input | What to provide | Required |
| --- | --- | --- |
| `recipients` | To | Yes |
| `ccRecipients` | Cc | Optional |
| `bccRecipients` | Bcc | Optional |
| `subject` | Subject | Yes |
| `bodyFormat` | How the text in Body is interpreted. | Yes |
| `body` | Body | Yes |
| `attachments` | Attachments | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/create-draft-email.ts).

### Find Email

Search your mailbox by keywords, sender or subject.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchQuery` | Words to find. Narrow with from:, subject: or hasAttachments:true. | Yes |
| `folderId` | Folder Id | See action definition |
| `top` | How many emails to return, up to 1000. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/find-email.ts).

### Forward Email

Forward an email to new recipients with an optional note.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | Message Id | See action definition |
| `recipients` | One address per row. | Yes |
| `comment` | Added above the forwarded email. HTML tags are rendered. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/forward-email.ts).

### Reply to Email

Reply to an Outlook email, or save the reply as a draft.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | Message Id | See action definition |
| `bodyFormat` | How the text in Body is interpreted. | Yes |
| `replyBody` | Body | Yes |
| `ccRecipients` | Cc | Optional |
| `bccRecipients` | Bcc | Optional |
| `attachments` | Attachments | Yes |
| `draft` | Save the reply to Drafts instead of sending it. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/reply-email.ts).

### Send Draft

Sends an existing draft message.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | ID of the draft to send. Obtain it from Create Draft or one of the Create ... Draft actions. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/outlook-send-draft.ts).

### Send Draft Email

Send an email that is waiting in your Drafts folder.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | Message Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/send-draft-email.ts).

### Send Email

Send an email from your Outlook mailbox.

| Input | What to provide | Required |
| --- | --- | --- |
| `recipients` | To | Yes |
| `ccRecipients` | Cc | Optional |
| `bccRecipients` | Bcc | Optional |
| `subject` | Subject | Yes |
| `bodyFormat` | How the text in Body is interpreted. | Yes |
| `body` | Body | Yes |
| `attachments` | Attachments | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/actions/send-email.ts).

## Events and recurring work

- **[New Attachment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/triggers/new-attachment.ts)** — Triggers once for each attachment on a new email.
- **[New Email in Folder](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-outlook/src/lib/triggers/new-email-in-folder.ts)** — Triggers when a new email lands in the folder you pick.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Microsoft Outlook to find email. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
