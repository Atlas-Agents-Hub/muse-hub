---
name: gorgias-connector
description: "Helpdesk platform for ecommerce teams to manage tickets, customers, and support conversations."
---

# Gorgias for Muse

Helpdesk platform for ecommerce teams to manage tickets, customers, and support conversations.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Gorgias**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Helpdesk Domain** (`domain`): Your Gorgias subdomain only, for example `acme` from https://acme.gorgias.com.
- **Email Address** (`email`): The email address associated with your Gorgias API key.
- **Api_Key** (`api_key`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/index.ts).

## Actions

### Create Message

Create a reply or message on an existing Gorgias ticket.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticketId` | Ticket ID | Yes |
| `fromAgent` | True when the sender is an agent/user; false when the sender is a customer. | Yes |
| `senderId` | User ID when From Agent is true, otherwise Customer ID. | Yes |
| `receiverId` | Customer ID when From Agent is true, otherwise User ID. | Yes |
| `fromAddress` | Email or channel address of the sender. | Yes |
| `toAddress` | Email or channel address of the receiver. | Yes |
| `message` | Message body. HTML is accepted by the API. | Yes |
| `subject` | Subject | Optional |
| `channel` | Channel | Yes |
| `via` | Via | Yes |
| `sentDatetime` | Optional ISO-8601 timestamp for when the message was sent. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/create-message.ts).

### Create Ticket

Create a new Gorgias ticket with an initial message.

| Input | What to provide | Required |
| --- | --- | --- |
| `fromAddress` | The sender address for the initial message, typically the customer email. | Yes |
| `toAddress` | The recipient address for the initial message. | Yes |
| `subject` | Subject | Yes |
| `message` | Initial ticket message. HTML is accepted by the API. | Yes |
| `channel` | Channel | Yes |
| `via` | How the message reached Gorgias. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/create-ticket.ts).

### Get Customer

Retrieve a Gorgias customer by ID or find one by email.

| Input | What to provide | Required |
| --- | --- | --- |
| `customerId` | Use this when you already know the customer ID. | Optional |
| `email` | If Customer ID is not provided, search customers by email using Gorgias server-side filtering. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/get-customer.ts).

### Get Ticket

Retrieve a Gorgias ticket by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticketId` | Ticket ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/get-ticket.ts).

### List Tickets

List Gorgias tickets with cursor-based pagination support.

| Input | What to provide | Required |
| --- | --- | --- |
| `customerId` | Optional customer ID to filter tickets for one customer. | Optional |
| `cursor` | Optional cursor returned by a previous list response. | Optional |
| `limit` | Maximum number of tickets to return in this page. Defaults to 25. | Optional |
| `orderBy` | Optional ordering, for example `created_datetime:desc`. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/list-tickets.ts).

### Update Ticket

Update a Gorgias ticket.

| Input | What to provide | Required |
| --- | --- | --- |
| `ticketId` | Ticket ID | Yes |
| `subject` | Subject | Optional |
| `status` | Status | Optional |
| `channel` | Channel | Optional |
| `customerId` | Optional customer ID to attach to the ticket. | Optional |
| `customerEmail` | Optional customer email to attach alongside the customer ID. | Optional |
| `fromAgent` | Whether the first message of the ticket was sent by your company. | Optional |
| `isUnread` | Is Unread | Optional |
| `spam` | Spam | Optional |
| `externalId` | External ID | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gorgias/src/lib/actions/update-ticket.ts).

## Try it

> Use Gorgias to get customer. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
