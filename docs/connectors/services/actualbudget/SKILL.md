---
name: actualbudget-connector
description: "Open-source personal finance app with envelope budgeting (self-hosted)"
---

# Actual Budget for Muse

Open-source personal finance app with envelope budgeting (self-hosted)

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Actual Budget**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Server URL** (`server_url`): The URL of your Actual server, e.g. https://actual.example.com
- **Password** (`password`): ProviderField
- **Sync_Id** (`sync_id`): ProviderField
- **Encryption_Password** (`encryption_password`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/index.ts).

## Actions

### Delete Transaction

Deletes a transaction (and its splits). This cannot be undone from the flow.

| Input | What to provide | Required |
| --- | --- | --- |
| `transaction_id` | Transaction ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/delete-transaction.ts).

### Find Payees

Finds payees whose name contains the search text (all payees when empty).

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Part of the payee name, e.g. "kroger". Leave empty to list all payees. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/find-payees.ts).

### Find Transactions

Finds transactions in a date range, optionally filtered by account, payee, category, amount or text.

| Input | What to provide | Required |
| --- | --- | --- |
| `start_date` | YYYY-MM-DD (inclusive) | Yes |
| `end_date` | YYYY-MM-DD (inclusive). Leave empty for no end. | Optional |
| `account_id` | Only this account. Leave empty for all accounts. | Optional |
| `payee_id` | Only this payee (ID from Find Payees) | Optional |
| `category_id` | Only this category | Optional |
| `min_amount` | e.g. -100 (currency units; expenses are negative) | Optional |
| `max_amount` | e.g. 0 to get only expenses | Optional |
| `search` | Matched against notes, payee name and imported payee | Optional |
| `limit` | Max transactions to return (1-${MAX_LIMIT}, default 100) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/find-transactions.ts).

### Get Accounts

Gets every account in the budget (open and closed).

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/get-accounts.ts).

### Get Budget

Gets the budget for one month: totals plus budgeted, spent and balance per category (amounts in cents).

| Input | What to provide | Required |
| --- | --- | --- |
| `month` | The month of the budget you want to get | Yes |
| `year` | Year | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/get-budget.ts).

### Get Categories

Gets every budget category as a flat list.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/get-categories.ts).

### Run Bank Sync

Pulls new transactions from the bank for one linked account, or for all linked accounts.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_id` | Linked account to sync. Leave empty to sync all linked accounts. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/run-bank-sync.ts).

### Set Budget Amount

Sets how much is budgeted for a category in a month (replaces the current amount).

| Input | What to provide | Required |
| --- | --- | --- |
| `month` | YYYY-MM, e.g. 2026-10 | Yes |
| `category_id` | Category ID | Yes |
| `amount` | Budgeted amount in currency units, e.g. 250 | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/actions/set-budget-amount.ts).

## Events and recurring work

- **[New Transaction](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/actualbudget/src/lib/triggers/new-transaction.ts)** — Triggers when a transaction dated within the last ${LOOKBACK_DAYS} days (or later) is added to an account. Split transactions trigger once, with their splits.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Actual Budget to find payees. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
