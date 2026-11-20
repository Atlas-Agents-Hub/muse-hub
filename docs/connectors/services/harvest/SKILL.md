---
name: harvest-connector
description: "Time Tracking Software with Invoicing"
---

# Harvest for Muse

Time Tracking Software with Invoicing

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Harvest**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://id.getharvest.com/oauth2/authorize>
- Token endpoint: <https://id.getharvest.com/api/v2/oauth2/token>

Provider scopes: `harvest:all`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/index.ts).

## Actions

### Get Clients

Fetches Clients

| Input | What to provide | Required |
| --- | --- | --- |
| `is_active` | Pass `true` to only return active clients and `false` to return inactive clients. | Optional |
| `updated_since` | Only return clients that have been updated since the given date and time. | Optional |
| `page` | DEPRECATED: The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-clients.ts).

### Get Estimates

Fetches Estimates

| Input | What to provide | Required |
| --- | --- | --- |
| `from` | Only return estimates with an issue_date on or after the given date. (YYYY-MM-DD) | Optional |
| `to` | Only return estimates with an issue_date on or before the given date. (YYYY-MM-DD) | Optional |
| `state` | Only return estimates with a state matching the value provided. Options: draft, open, accepted, or declined. | Optional |
| `updated_since` | Only return estimates that have been updated since the given date and time. | Optional |
| `client_id` | Only return estimates belonging to the client with the given ID. | Optional |
| `page` | The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-estimates.ts).

### Get Expenses

Fetches expenses

| Input | What to provide | Required |
| --- | --- | --- |
| `from` | Only return expenses with an spent_date on or after the given date. (YYYY-MM-DD) | Optional |
| `to` | Only return expenses with an spent_date on or before the given date. (YYYY-MM-DD) | Optional |
| `user_id` | Only return expenses belonging to the user with the given ID. | Optional |
| `client_id` | Only return expenses belonging to the client with the given ID. | Optional |
| `project_id` | Only return expenses belonging to the project with the given ID. | Optional |
| `is_billed` | Pass `true` to only return expenses that have been invoiced and `false` to return expenses that have not been invoiced. | Optional |
| `updated_since` | Only return expenses that have been updated since the given date and time. | Optional |
| `page` | The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-expenses.ts).

### Get Invoices

Fetches invoices

| Input | What to provide | Required |
| --- | --- | --- |
| `from` | Only return invoices with an issue_date on or after the given date. (YYYY-MM-DD) | Optional |
| `to` | Only return invoices with an issue_date on or before the given date. (YYYY-MM-DD) | Optional |
| `state` | Only return invoices with a state matching the value provided. Options: draft, open, paid, or closed. | Optional |
| `updated_since` | Only return invoices that have been updated since the given date and time. | Optional |
| `client_id` | Only return invoices belonging to the client with the given ID. | Optional |
| `project_id` | Only return invoices belonging to the project with the given ID. | Optional |
| `page` | The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-invoices.ts).

### Get Projects

Fetches projects

| Input | What to provide | Required |
| --- | --- | --- |
| `is_active` | Pass `true` to only return active projects and `false` to return inactive projects. | Optional |
| `updated_since` | Only return projects that have been updated since the given date and time. | Optional |
| `client_id` | Only return invoices belonging to the client with the given ID. | Optional |
| `page` | DEPRECATED: The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-projects.ts).

### Get Roles

Fetches Roles

| Input | What to provide | Required |
| --- | --- | --- |
| `page` | DEPRECATED: The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-roles.ts).

### Get Tasks

Fetches Tasks

| Input | What to provide | Required |
| --- | --- | --- |
| `is_active` | Pass `true` to only return active tasks and `false` to return inactive tasks. | Optional |
| `updated_since` | Only return tasks that have been updated since the given date and time. | Optional |
| `page` | DEPRECATED: The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-tasks.ts).

### Get Users

Fetches Users

| Input | What to provide | Required |
| --- | --- | --- |
| `is_active` | Pass `true` to only return active users and `false` to return inactive users. | Optional |
| `updated_since` | Only return users that have been updated since the given date and time. | Optional |
| `page` | DEPRECATED: The page number to use in pagination. | Optional |
| `per_page` | The number of records to return per page. (1-2000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/harvest/src/lib/actions/get-users.ts).

## Try it

> Use Harvest to get clients. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
