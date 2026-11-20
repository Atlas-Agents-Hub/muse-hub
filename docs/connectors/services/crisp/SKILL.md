---
name: crisp-connector
description: "Crisp: add note to conversation, change conversation state, create conversation."
---

# Crisp for Muse

Crisp: add note to conversation, change conversation state, create conversation.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Crisp**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Identifier** (`identifier`): ProviderField
- **Token** (`token`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/index.ts).

## Actions

### Add Note to Conversation

Adds an internal note to a conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `sessionId` | Session Id | See action definition |
| `content` | Note Content | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/add-note-to-conversation.ts).

### Change Conversation State

Updates the state of a conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `sessionId` | Session Id | See action definition |
| `state` | State | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/update-conversation-state.ts).

### Create Conversation

Creates a new conversation.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `email` | Customer Email | Yes |
| `username` | Customer Username | Yes |
| `messageFrom` | Message From | Yes |
| `message` | Message | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/create-conversation.ts).

### Create/Update Contact

Creates a new contact or updates an existing contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `email` | Email | Yes |
| `name` | Name | Yes |
| `phone` | Phone Number | Optional |
| `address` | Address | Optional |
| `company` | Company | Optional |
| `website` | Contact Website | Optional |
| `notepad` | Notepad | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/create-or-update-contact.ts).

### Find Conversation

Searches for conversations matching the specified criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `searchQuery` | Search Query | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/find-conversation.ts).

### Find User Profile

Finds a user profile by email address.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `email` | The email address of the user to find. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/actions/find-user-profile.ts).

## Events and recurring work

- **[New Contact Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/triggers/new-contact.ts)** — Triggers when a new contact is added.
- **[New Conversation Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/crisp/src/lib/triggers/new-conversation.ts)** — Triggers when a new conversation is started.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Crisp to find conversation. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
