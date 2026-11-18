---
name: microsoft-onedrive-connector
description: "Cloud storage by Microsoft"
---

# Microsoft OneDrive for Muse

Cloud storage by Microsoft

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Microsoft OneDrive**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{cloud}/common/oauth2/v2.0/authorize>
- Token endpoint: <https://{cloud}/common/oauth2/v2.0/token>
- **Cloud** (`cloud`): ProviderField

Provider scopes: `Files.ReadWrite`, `email`, `offline_access`, `openid`, `profile`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/index.ts).

## Actions

### Copy File

Create a copy of a file in your OneDrive, optionally in a different folder or with a new name.

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `sourceFolderId` | Source Folder Id | See action definition |
| `fileId` | The file to copy. If the file is not listed (up to 1000 files are fetched), toggle the dynamic input (F) and enter the file ID directly. | Yes |
| `destinationFolderId` | Destination Folder Id | See action definition |
| `newName` | A new name for the copied file (e.g. report-copy.xlsx). If left empty, the original name is used. | Optional |
| `conflictBehavior` | What to do if a file with the same name already exists in the destination folder. Note: personal OneDrive (consumer) accounts do not support this option and may fail on name conflicts regardless of the selection. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/copy-file.ts).

### Copy File or Folder

Start copying a OneDrive file or folder. The copy runs in the background; check it with Get Copy Status.

| Input | What to provide | Required |
| --- | --- | --- |
| `itemId` | ID of the item to copy, from Search or List Folder Contents. | Optional |
| `path` | Path from the drive root. Use this or Item ID. | Optional |
| `destinationFolderId` | Folder to copy into. Leave empty for the drive root. | Optional |
| `newName` | Optional name for the copy. Leave empty to keep the original name. | Optional |
| `conflictBehavior` | What to do on a name clash. Not supported on personal OneDrive. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/onedrive-copy-item.ts).

### Get Drive

Get the connected OneDrive drive, including its type and storage quota.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/onedrive-get-drive.ts).

### Get File

Get and download a file using a File ID or filename.

| Input | What to provide | Required |
| --- | --- | --- |
| `lookupBy` | Look Up By | Yes |
| `fileIdentifier` | Enter the File ID or the exact filename depending on the "Look Up By" selection | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/download-file.ts).

### Get File or Folder

Get the metadata of a file or folder by its ID or path.

| Input | What to provide | Required |
| --- | --- | --- |
| `itemId` | Item ID from Search or List Folder Contents, or "root". Or use Path. | Optional |
| `path` | Path from the drive root. Used when Item ID is empty. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/onedrive-get-item.ts).

### List Files

List files in a OneDrive folder

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `parentFolder` | Parent Folder | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/list-files.ts).

### List Folders

List folders in a OneDrive folder

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `parentFolder` | Parent Folder | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/list-folders.ts).

### Upload file

Upload a file to your Microsoft OneDrive with chunked upload if the file is larger than 4MiB

| Input | What to provide | Required |
| --- | --- | --- |
| `fileName` | The name the file should be saved as (e.g. file.txt) | Yes |
| `file` | The file URL or base64 to upload | Yes |
| `markdown` | Markdown | See action definition |
| `parentId` | Parent Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/actions/upload-file.ts).

## Events and recurring work

- **[New File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-onedrive/src/lib/triggers/new-file.ts)** — Trigger when a new file is uploaded.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Microsoft OneDrive to get drive. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
