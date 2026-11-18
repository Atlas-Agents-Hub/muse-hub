---
name: intercom-connector
description: "Customer messaging platform for sales, marketing, and support"
---

# Intercom for Muse

Customer messaging platform for sales, marketing, and support

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Intercom**.
2. Configure **OAuth 2.0 account connection; Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://app.{region}.com/oauth>
- Token endpoint: <https://api.{region}.io/auth/eagle/token>
- **Region** (`region`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/index.ts).

## Actions

### Find Company

Finds an existing company.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchField` | Search Field | Yes |
| `searchValue` | Search Value | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/find-company.ts).

### Find Lead

Finds an existing lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchField` | Search Field | Yes |
| `searchValue` | Search Value | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/find-lead.ts).

### Find User

Finds an existing user.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchField` | Search Field | Yes |
| `searchValue` | Search Value | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/find-user.ts).

### Get Company

Gets one company by its Intercom ID or by your own Company ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `lookupBy` | Look Up By | Yes |
| `value` | Value | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/get-company.ts).

### Get Contact

Gets one contact (user or lead) by ID, email or external ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `lookupBy` | Look Up By | Yes |
| `value` | The contact ID, email or external ID. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/get-contact.ts).

### Get Ticket

Gets one ticket by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticketId` | The ticket "id" from Intercom, not the inbox ticket number. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/get-ticket.ts).

### List Admins

Lists the admins (teammates) in the workspace.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/list-admins.ts).

### List Teams

Lists the teams in the workspace.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/actions/list-teams.ts).

## Events and recurring work

- **[Contact Replied](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/triggers/contact-replied.ts)** — Triggers when a contact replies to a Conversation in Intercom.
- **[Conversation assigned to any Intercom admin](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/triggers/conversation-assigned.ts)** — Triggers when a conversation is assigned to an admin
- **[Updated Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/intercom/src/lib/triggers/contact-updated.ts)** — Triggers when a contact is updated.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Intercom to find company. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
