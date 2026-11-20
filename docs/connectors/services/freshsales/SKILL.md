---
name: freshsales-connector
description: "Sales CRM software"
---

# Freshsales for Muse

Sales CRM software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Freshsales**.
2. Configure **Service username and password or token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/index.ts).

## Actions

### Get Account

Get an account by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `sales_account_id` | ID of the account to fetch | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/get-account.ts).

### Get Contact

Get a contact by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `contact_id` | ID of the contact to fetch | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/get-contact.ts).

### Get Deal

Get a deal by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `deal_id` | ID of the deal to fetch | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/get-deal.ts).

### Get Task

Get a task by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `task_id` | ID of the task to fetch | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/get-task.ts).

### List Pipelines and Stages

List deal pipelines with their stages

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/list-pipelines.ts).

### List Records in View

List contacts, accounts or deals from a saved view

| Input | What to provide | Required |
| --- | --- | --- |
| `entity` | Which records to list | Yes |
| `view_id` | View_Id | See action definition |
| `page` | Page number, starting at 1 | Optional |
| `per_page` | Records per page (1-100) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/list-records.ts).

### List Tasks

List tasks by status (open, overdue, completed...)

| Input | What to provide | Required |
| --- | --- | --- |
| `filter` | Which tasks to list | Yes |
| `page` | Page number, starting at 1 | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/list-tasks.ts).

### List Users

List Freshsales users (owners) with their IDs

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/actions/list-users.ts).

## Events and recurring work

- **[New Account](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/triggers/new-account.ts)** — Triggers when a new account is created
- **[New Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/triggers/new-contact.ts)** — Triggers when a new contact is created
- **[New Deal](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshsales/src/lib/triggers/new-deal.ts)** — Triggers when a new deal is created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Freshsales to get account. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
