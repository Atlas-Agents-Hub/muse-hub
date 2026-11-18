---
name: google-docs-connector
description: "Create and edit documents online"
---

# Google Docs for Muse

Create and edit documents online

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Docs**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/index.ts).

## Actions

### Append Text

Add text to the end of a document.

| Input | What to provide | Required |
| --- | --- | --- |
| `documentId` | Document Id | See action definition |
| `text` | Added to the end of the document. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/append-text.ts).

### Create Document

Create a document on Google Docs.

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Title | See action definition |
| `body` | Body | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/create-document.ts).

### Find Document

Find a document by name, optionally creating it.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Matches any document whose name contains this text. | Yes |
| `folderId` | Folder Id | See action definition |
| `createIfNotFound` | Create If Not Found | Optional |
| `newDocumentProps` | New Document Properties | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/find-document.ts).

### Get Document

Get the full content and structure of a Google Docs document

| Input | What to provide | Required |
| --- | --- | --- |
| `documentId` | The ID of the document to read (from the document URL or Search Documents). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/get-document.action.ts).

### Get Document End Index

Get the end index of a Google Docs document body

| Input | What to provide | Required |
| --- | --- | --- |
| `documentId` | The ID of the document to inspect (from the document URL or Search Documents). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/get-document-end-index.action.ts).

### Get Document Plain Text

Get the plain text content of a Google Docs document.

| Input | What to provide | Required |
| --- | --- | --- |
| `documentId` | The ID of the document to read, found in its URL: 'https://docs.google.com/document/d/<documentId>/edit'. Obtain it from Search Documents or Find Document if you only have a name. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/get-document-plaintext.action.ts).

### Read Document

Read a document from Google Docs.

| Input | What to provide | Required |
| --- | --- | --- |
| `documentId` | Document Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/read-document.action.ts).

### Search Documents

Search Google Drive for Google Docs documents by name or full-text content.

| Input | What to provide | Required |
| --- | --- | --- |
| `name_contains` | Return documents whose name contains this text. Provide this and/or Content Contains. | Optional |
| `full_text_contains` | Return documents whose full text content contains this text. Provide this and/or Name Contains. | Optional |
| `max_results` | Maximum number of documents to return (1-100). | Optional |
| `order_by` | How to sort the results. | Optional |
| `page_token` | Token for the next page of results, taken from the nextPageToken of a previous call. Leave empty for the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/actions/search-documents.action.ts).

## Events and recurring work

- **[New Document](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-docs/src/lib/triggers/new-document.ts)** — Triggers when a new document is created in Drive or a chosen folder.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Docs to find document. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
