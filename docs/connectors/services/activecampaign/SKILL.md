---
name: activecampaign-connector
description: "Email marketing, marketing automation, and CRM tools you need to create incredible customer experiences."
---

# ActiveCampaign for Muse

Email marketing, marketing automation, and CRM tools you need to create incredible customer experiences.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **ActiveCampaign**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **API URL** (`apiUrl`): For example https://youraccount.api-us1.com
- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/index.ts).

## Actions

### Add Note

Adds a note to a contact, deal or account.

| Input | What to provide | Required |
| --- | --- | --- |
| `recordType` | Record Type | See action definition |
| `recordId` | The ID of the contact, deal or account. Map it from the trigger or an earlier step, for example the contact ID from Find Contact. | Yes |
| `note` | Note | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/notes/create-note.ts).

### Create Account

Creates a new account.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Account Name | Yes |
| `accountUrl` | Account URL | Optional |
| `accountCustomFields` | Account Custom Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/accounts/create-account.ts).

### Create Contact

Creates a new contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |
| `firstName` | First Name | Optional |
| `lastName` | Last Name | Optional |
| `phone` | Phone | Optional |
| `contactCustomFields` | Contact Custom Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/contacts/create-contact.ts).

### Create Deal

Creates a deal in a pipeline stage, linked to a contact, an account or both.

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Title | Yes |
| `value` | The amount as a decimal, such as 1500 or 1234.50. | Yes |
| `currency` | 3-letter currency code, such as usd or eur. | Yes |
| `pipelineId` | Pipeline Id | See action definition |
| `stageId` | Stage Id | See action definition |
| `ownerId` | Owner Id | See action definition |
| `contactId` | Contact Id | See action definition |
| `accountId` | Account Id | See action definition |
| `description` | Description | Optional |
| `status` | Status | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/deals/create-deal.ts).

### Create Task

Creates a task on a contact or deal.

| Input | What to provide | Required |
| --- | --- | --- |
| `ownerType` | Owner Type | See action definition |
| `recordId` | Map it from the trigger or an earlier step. | Yes |
| `taskTypeId` | Task Type Id | See action definition |
| `title` | Title | Optional |
| `note` | Note | Optional |
| `dueDate` | An ISO 8601 date or date-time, such as 2026-03-01 or 2026-03-01T09:00:00Z. Times are UTC unless you add an offset (2026-03-01T09:00:00-06:00). A date without a time is sent as 12:00 UTC, which keeps the task on that day for accounts between UTC-11 and UTC+11; for other time zones, give a time with an offset. | Yes |
| `endDate` | Optional, in the same format as Due Date and not before it. A date without a time means 12:00 UTC. Defaults to 15 minutes after the due date. | Optional |
| `assigneeId` | Assignee Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/tasks/create-task.ts).

### Find Contact

Finds a contact by email address.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/contacts/find-contact.ts).

### Update Account

Updates an account.

| Input | What to provide | Required |
| --- | --- | --- |
| `accountId` | Account Id | See action definition |
| `name` | Account Name | Optional |
| `accountUrl` | Account URL | Optional |
| `accountCustomFields` | Account Custom Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/accounts/update-account.ts).

### Update Deal

Updates a deal. Fields left empty keep their current value.

| Input | What to provide | Required |
| --- | --- | --- |
| `dealId` | Deal Id | See action definition |
| `title` | Title | Optional |
| `value` | The amount as a decimal, such as 1500 or 1234.50. | Optional |
| `currency` | 3-letter currency code, such as usd or eur. | Optional |
| `pipelineId` | Pipeline Id | See action definition |
| `stageId` | Stage Id | See action definition |
| `ownerId` | Owner Id | See action definition |
| `contactId` | Contact Id | See action definition |
| `accountId` | Account Id | See action definition |
| `description` | Description | Optional |
| `status` | Status | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/actions/deals/update-deal.ts).

## Events and recurring work

- **[Contact Unsubscribed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/triggers/contact-unsubscribed.ts)** — Triggers when a contact unsubscribes from a list. Also fires for changes made through the API, including this piece's own actions, so a flow that changes the same record can trigger itself again.
- **[Deal Task Completed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/triggers/deal-task-completed.ts)** — Triggers when a deal task has been completed. Also fires for changes made through the API, including this piece's own actions, so a flow that changes the same record can trigger itself again.
- **[New Campaign Link Click](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/activecampaign/src/lib/triggers/campaign-link-clicked.ts)** — Triggers when a contact clicks a link in a campaign message (will only run once for each unique link).

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use ActiveCampaign to find contact. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
