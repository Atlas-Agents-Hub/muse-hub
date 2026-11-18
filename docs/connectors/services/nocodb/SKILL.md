---
name: nocodb-connector
description: "NocoDB: get a record, get current user, get table schema."
---

# NocoDB for Muse

NocoDB: get a record, get current user, get table schema.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **NocoDB**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **NocoDB Base URL** (`baseUrl`): ShortText
- **Api Token** (`apiToken`): ProviderField
- **API Version** (`version`): Required only for self-hosted instances. Not needed for the cloud version.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/index.ts).

## Actions

### Get a Record

Gets a record by the Record ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `baseId` | Base Id | See action definition |
| `tableId` | Table Id | See action definition |
| `recordId` | Record ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/get-record.ts).

### Get Current User

Returns the profile and roles of the authenticated user.

| Input | What to provide | Required |
| --- | --- | --- |
| `baseId` | Base ID | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/get-current-user.ts).

### Get Table Schema

Returns the columns and metadata of the given table.

| Input | What to provide | Required |
| --- | --- | --- |
| `baseId` | Base ID | Yes |
| `tableId` | Table ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/get-table-schema.ts).

### List Bases

Returns the bases within the given workspace (or the instance, on self-hosted).

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Leave unset on self-hosted instances. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/list-bases.ts).

### List View Columns

Returns the columns configured on the given view, with their view-scoped column IDs.

| Input | What to provide | Required |
| --- | --- | --- |
| `viewId` | View ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/list-view-columns.ts).

### List View Sorts

Returns the sort rules configured on the given view.

| Input | What to provide | Required |
| --- | --- | --- |
| `viewId` | View ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/list-view-sorts.ts).

### List Workspaces

Returns the workspaces visible to the authenticated account.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/list-workspaces.ts).

### Search Records

Returns a list of records matching the where condition.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `baseId` | Base Id | See action definition |
| `tableId` | Table Id | See action definition |
| `columnId` | Column Id | See action definition |
| `whereCondition` | Enables you to define specific conditions for filtering records.See docs [here](https://docs.nocodb.com/0.109.7/developer-resources/rest-apis/#comparison-operators). | Optional |
| `limit` | Enables you to set a limit on the number of records you want to retrieve. | Yes |
| `sort` | Comma separated field names without space.Example: **field1,-field2** will sort the records first by 'field1' in ascending order and then by 'field2' in descending order. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/nocodb/src/lib/actions/search-records.ts).

## Try it

> Use NocoDB to get a record. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
