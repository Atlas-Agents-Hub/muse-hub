---
name: algolia-connector
description: "Manage your Algolia search indices \u2014 add, browse, and delete records."
---

# Algolia for Muse

Manage your Algolia search indices — add, browse, and delete records.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Algolia**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Application ID** (`applicationId`): Your Algolia application ID.
- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/algolia/src/index.ts).

## Actions

### Browse Records

Retrieves records from an Algolia index.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | Index Name | See action definition |
| `limit` | Maximum number of records to retrieve. Defaults to 10,000. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/algolia/src/lib/actions/browse-records.ts).

### Delete Records

Deletes records from an Algolia index by objectID.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | Index Name | See action definition |
| `recordIds` | Provide the Algolia objectIDs to delete from the selected index. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/algolia/src/lib/actions/delete-records.ts).

### Save Records

Adds or updates records in an Algolia index.

| Input | What to provide | Required |
| --- | --- | --- |
| `indexName` | Enter an existing index name or a new one — Algolia creates it automatically. | Yes |
| `records` | Provide an array of JSON objects to save. Include `objectID` to update an existing record, or omit it to let Algolia create one. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/algolia/src/lib/actions/save-records.ts).

## Try it

> Use Algolia to browse records. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
