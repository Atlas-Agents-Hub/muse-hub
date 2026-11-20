---
name: dropbox-connector
description: "Cloud storage and file synchronization"
---

# Dropbox for Muse

Cloud storage and file synchronization

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Dropbox**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://www.dropbox.com/oauth2/authorize>
- Token endpoint: <https://api.dropboxapi.com/oauth2/token>

Provider scopes: `files.content.read`, `files.content.write`, `files.metadata.read`, `files.metadata.write`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/index.ts).

## Actions

### Get File Lock

Check whether a file is locked

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | The file to check. Accepts a path (/folder/file.txt) or an id (id:abc123), but not a rev: value. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/get-file-lock.ts).

### Get File Metadata

Get metadata for a file or folder

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | The file or folder to inspect. Accepts a path (/folder/file.txt), an id (id:abc123) or a revision (rev:a1c10ce0dd78). | Yes |
| `include_deleted` | Return metadata for a deleted entry instead of failing when the path no longer exists. | Optional |
| `include_media_info` | Include photo and video metadata when available. | Optional |
| `include_has_explicit_shared_members` | Include whether the entry has explicit shared members assigned. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/get-file-metadata.ts).

### Get File Preview

Get a PDF or HTML preview of a document

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | The document to preview. Accepts a path (/folder/report.docx), an id (id:abc123) or a revision (rev:a1c10ce0dd78). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/get-file-preview.ts).

### Get File Thumbnail

Get a thumbnail image for a file

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | The image file to thumbnail. Accepts a path (/folder/photo.jpg), an id (id:abc123) or a revision (rev:a1c10ce0dd78). | Yes |
| `format` | Format | Optional |
| `size` | Size | Optional |
| `mode` | Strict keeps the requested dimensions exactly; the bestfit modes preserve the aspect ratio. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/get-file-thumbnail.ts).

### Get Temporary File Link

Get a download link that expires after 4 hours

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | File to link to. The link expires after 4 hours. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/get-file-link.ts).

### List Folder

List the files and subfolders in a folder

| Input | What to provide | Required |
| --- | --- | --- |
| `path` | Folder to list, starting with /. Use / for the root. | Yes |
| `recursive` | Also list everything inside subfolders. | Optional |
| `limit` | About how many entries to return. Empty: 2,000. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/list-a-folder.ts).

### Search

Search for files and folders

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Words to find in file and folder names or contents. | Yes |
| `path` | Folder to search in. Empty: the whole Dropbox. | Optional |
| `max_results` | Maximum matches to return, up to 1,000. Empty: 100. | Optional |
| `order_by` | How to sort the matches. Empty: by relevance. | Optional |
| `file_status` | Current or deleted files. Empty: current files. | Optional |
| `filename_only` | Match names only, not file contents. | Optional |
| `file_extensions` | Comma-separated, without the dot. | Optional |
| `file_categories` | Comma-separated: image, document, pdf, spreadsheet, presentation, audio, video, folder, paper, others. | Optional |
| `account_id` | Team accounts: only this member's files. Starts with dbid:. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/actions/search.ts).

## Events and recurring work

- **[New Folder](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/dropbox/src/lib/triggers/new-folder.ts)** — Triggers when a new folder is created inside a watched Dropbox folder.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Dropbox to get file lock. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
