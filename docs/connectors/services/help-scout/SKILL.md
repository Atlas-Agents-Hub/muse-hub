---
name: help-scout-connector
description: "Help Scout: add note, create conversation, create customer."
---

# Help Scout for Muse

Help Scout: add note, create conversation, create customer.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Help Scout**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://secure.helpscout.net/authentication/authorizeClientApplication>
- Token endpoint: <https://api.helpscout.net/v2/oauth2/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/index.ts).

## Actions

### Add Note

Adds a note to a conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `conversationId` | Conversation Id | See action definition |
| `text` | Note Text | Yes |
| `userId` | User Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/add-note.ts).

### Create Conversation

Start a new conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `mailboxId` | Mailbox Id | See action definition |
| `subject` | Subject | Yes |
| `customerEmail` | Customer Email | Yes |
| `conversationType` | Defaults to Chat, which is what earlier versions of this step always created. | Optional |
| `fromUser` | From User | See action definition |
| `threadType` | Thread Type | Yes |
| `status` | Conversation Status | Yes |
| `body` | Body | Yes |
| `assignTo` | Assign To | See action definition |
| `tags` | Tags | Optional |
| `cc` | CC | Optional |
| `bcc` | BCC | Optional |
| `imported` | Imported | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/create-conversation.ts).

### Create Customer

Adds a new customer to Help Scout.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |
| `firstName` | First Name | Optional |
| `lastName` | Last Name | Optional |
| `phone` | Phone | Optional |
| `photoUrl` | Photo URL | Optional |
| `jobTitle` | Job Title | Optional |
| `location` | Location | Optional |
| `background` | Background | Optional |
| `age` | Customer’s age (string, e.g. "30-35") | Optional |
| `gender` | Gender | Optional |
| `organization` | Organization | Optional |
| `socialProfiles` | URLs for social profiles (type will be set to "other") | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/create-customer.ts).

### Find Conversation

Finds an existing conversation using provided filter.

| Input | What to provide | Required |
| --- | --- | --- |
| `subject` | Subject | Optional |
| `mailboxId` | Mailbox Id | See action definition |
| `status` | Leave empty to search every status. | Optional |
| `assignTo` | Assign To | See action definition |
| `email` | Email | Optional |
| `tags` | Tags | Optional |
| `query` | Custom Query | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/find-conversation.ts).

### Find Customer

Finds a customer by email.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The customer email address, for example jane@example.com. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/find-customer.ts).

### Find User

Finds a user by email.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The teammate email address, for example agent@yourcompany.com. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/find-user.ts).

### Send Reply

Sends a reply in an existing conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `conversationId` | Conversation Id | See action definition |
| `text` | Reply Text | Yes |
| `customerEmail` | Customer Email | Yes |
| `draft` | Draft | Optional |
| `status` | Conversation Status | Optional |
| `userId` | User Id | See action definition |
| `cc` | CC (emails) | Optional |
| `bcc` | BCC (emails) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/send-reply.ts).

### Update Customer Properties

Updates customer's properties.

| Input | What to provide | Required |
| --- | --- | --- |
| `customerId` | Customer Id | See action definition |
| `fields` | Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/actions/update-customer-properties.ts).

## Events and recurring work

- **[Conversation Assigned](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/triggers/conversation-assigned.ts)** — Triggers when a conversation is assigned to a user.
- **[Conversation Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/triggers/conversation-created.ts)** — Triggers when a new conversation is started in a mailbox.
- **[New Customer](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/help-scout/src/lib/triggers/new-customer.ts)** — Triggers when a new customer is added.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Help Scout to find conversation. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
