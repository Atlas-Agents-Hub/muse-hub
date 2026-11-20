---
name: grist-connector
description: "open source spreadsheet"
---

# Grist for Muse

open source spreadsheet

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Grist**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api Key** (`apiKey`): ProviderField
- **Domain URL** (`domain`): ShortText

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/index.ts).

## Actions

### Create Record

Creates a new record in specific table.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `document_id` | Document_Id | See action definition |
| `table_id` | Table_Id | See action definition |
| `table_columns` | Table_Columns | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/actions/create-record.action.ts).

### Search Record

Search record by matching criteria.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `document_id` | Document_Id | See action definition |
| `table_id` | Table_Id | See action definition |
| `column` | Column | Yes |
| `value` | Enter the search text. The search operation is case sensitive, exact text match, and supports column-type Text only. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/actions/search-record.action.ts).

### Update Record

Updates an existing record in specific table.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `document_id` | Document_Id | See action definition |
| `table_id` | Table_Id | See action definition |
| `record_id` | Record ID | Yes |
| `table_columns` | Table_Columns | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/actions/update-record.action.ts).

### Upload Attachment to Document

Uploads attachments to specific document.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `document_id` | Document_Id | See action definition |
| `attachment` | Attachment | Yes |
| `attachment_name` | In case you want to change the name of the attachment. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/actions/upload-attachments-to-document.action.ts).

## Events and recurring work

- **[New Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/triggers/new-record.trigger.ts)** — Triggers when a new record is added to the table.
- **[Updated Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/grist/src/lib/triggers/updated-record.trigger.ts)** — Triggers when a record is updated in the table.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Grist to search record. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
