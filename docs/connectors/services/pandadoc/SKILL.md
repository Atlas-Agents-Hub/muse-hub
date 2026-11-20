---
name: pandadoc-connector
description: "Create, send and track documents, proposals and e-signatures."
---

# PandaDoc for Muse

Create, send and track documents, proposals and e-signatures.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **PandaDoc**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/index.ts).

## Actions

### Find Contacts

Finds contacts by exact email, or lists all contacts.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Exact email to match. Leave empty to list all contacts. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/find-contacts.ts).

### Find Document(s)

Finds documents using filters such as name, status, template, folder, contact and dates.

| Input | What to provide | Required |
| --- | --- | --- |
| `q` | Search documents by name or reference number | Optional |
| `id` | Search for document by its specific ID | Optional |
| `status` | Filter documents by status | Optional |
| `status__ne` | Exclude documents with this status | Optional |
| `template_id` | Template_Id | See action definition |
| `form_id` | Form_Id | See action definition |
| `folder_uuid` | Folder_Uuid | See action definition |
| `contact_id` | Contact_Id | See action definition |
| `membership_id` | Membership_Id | See action definition |
| `tag` | Tag | See action definition |
| `custom_tag` | Custom_Tag | See action definition |
| `created_from` | Include only documents created on or after this date | Optional |
| `created_to` | Include only documents created before this date | Optional |
| `completed_from` | Include only documents completed on or after this date | Optional |
| `completed_to` | Include only documents completed before this date | Optional |
| `modified_from` | Include only documents modified on or after this date | Optional |
| `modified_to` | Include only documents modified before this date | Optional |
| `deleted` | When on, returns only deleted documents instead of active ones. | Optional |
| `count` | Number of documents to return (default: 50, max: 100) | Optional |
| `page` | Page number for pagination (starts with 1) | Optional |
| `order_by` | Sort results by field | Optional |
| `metadata` | Filter by metadata key-value pairs. Use format: {"key": "value"} | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/find-document.ts).

### Get Document

Retrieves comprehensive document data.

| Input | What to provide | Required |
| --- | --- | --- |
| `document_id` | Document_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/get-document-details.ts).

### Get Document Attachment

Retrieves details of a specific attachment from a document.

| Input | What to provide | Required |
| --- | --- | --- |
| `document_id` | Document_Id | See action definition |
| `attachment_id` | Attachment_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/get-document-attachments.ts).

### Get Template Details

Gets a template with its roles, fields and variables.

| Input | What to provide | Required |
| --- | --- | --- |
| `template_id` | Template ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/get-template-details.ts).

### List Document Fields

Lists the fields of a document with their current values.

| Input | What to provide | Required |
| --- | --- | --- |
| `document_id` | Document_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/list-document-fields.ts).

### List Document Folders

Lists document folders, optionally inside a parent folder.

| Input | What to provide | Required |
| --- | --- | --- |
| `parent_folder_id` | Leave empty for top-level folders. | Optional |
| `count` | 1 to 100, default 50. | Optional |
| `page` | Starts at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/list-document-folders.ts).

### List Templates

Lists or searches templates.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Matches template name. | Optional |
| `tag` | Tag | Optional |
| `folder_id` | Folder ID | Optional |
| `count` | 1 to 100, default 50. | Optional |
| `page` | Starts at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/actions/list-templates.ts).

## Events and recurring work

- **[Document Completed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/triggers/document-completed.ts)** — Triggers when a document is completed (all recipients have signed or approved).
- **[Document Creation Failed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/triggers/document-creation-failed.ts)** — Triggers when PandaDoc fails to create a document requested through the API (for example a bad file or missing field values).
- **[Document Deleted](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pandadoc/src/lib/triggers/document-deleted.ts)** — Triggers when a document is deleted.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use PandaDoc to find contacts. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
