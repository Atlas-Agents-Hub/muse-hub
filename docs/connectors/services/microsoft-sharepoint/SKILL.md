---
name: microsoft-sharepoint-connector
description: "Microsoft SharePoint: copy file or folder (across sites), create list, find file."
---

# Microsoft SharePoint for Muse

Microsoft SharePoint: copy file or folder (across sites), create list, find file.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Microsoft SharePoint**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{cloud}/common/oauth2/v2.0/authorize>
- Token endpoint: <https://{cloud}/common/oauth2/v2.0/token>
- **Cloud** (`cloud`): ProviderField

Provider scopes: `Files.ReadWrite.All`, `Sites.Manage.All`, `Sites.Read.All`, `Sites.ReadWrite.All`, `email`, `offline_access`, `openid`, `profile`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/index.ts).

## Actions

### Copy File or Folder (Across Sites)

Copy a file or folder from one site to another within the same tenant, with overwrite option.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `driveId` | Drive Id | See action definition |
| `itemId` | Item Id | See action definition |
| `destination_site_id` | Destination_Site_Id | See action definition |
| `destination_drive_id` | Destination_Drive_Id | See action definition |
| `destination_folder_id` | Destination_Folder_Id | See action definition |
| `new_name` | A new name for the copied item. If not provided, the original name is used. | Optional |
| `conflict_behavior` | Action to take if a file with the same name already exists. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/copy-item.ts).

### Create List

Creates a new list.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `displayName` | List Name | Yes |
| `description` | List Description | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/create-list.ts).

### Find File

Look up a file by its name or path.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `driveId` | Drive Id | See action definition |
| `findMethod` | Choose how to find the file. | Yes |
| `filePath` | The exact path to the file from the drive's root. **Required if finding by path.** Example: `Documents/Reports/Q1-Report.docx` | Optional |
| `searchQuery` | The file name or keyword to search for. **Required if searching by name.** Example: `Q1-Report.docx` | Optional |
| `searchFolderId` | The folder to search within. If not specified, the entire drive will be searched. **Only applies when searching by name.** | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/find-file.ts).

### Find List Item

Finds a item in a list based on name.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `listId` | List Id | See action definition |
| `searchValue` | Item title to search | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/search-list-item.ts).

### Find Site

Search for SharePoint sites by name and return matching results.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchTerm` | The name or keyword to search for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/find-site.ts).

### Get Folder Contents

List all files and subfolders in a specified folder, optionally with detailed metadata.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `driveId` | Drive Id | See action definition |
| `folderId` | The folder whose contents you want to list. Select "Root Folder" for the top-level folder. | Yes |
| `includeCustomFields` | Check this to include SharePoint-specific metadata (custom columns). This may slow down the request. | Optional |
| `top` | The maximum number of items to return. The API default is 200. If more items exist, the output will contain a field `@odata.nextLink` that you can use in a custom API call to get the next page. | Optional |
| `select` | A comma-separated list of properties to return. Example: `id,name,size,webUrl` | Optional |
| `orderby` | Specifies how to sort the returned items. Example: `name asc` or `lastModifiedDateTime desc` | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/get-folder-contents.ts).

### Get Site Information

Fetch metadata of a SharePoint site (site ID, title, URL, description, etc.).

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `select` | A comma-separated list of properties to return. If left blank, all default properties are returned. Example: `id,displayName,webUrl,description` | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/get-site-information.ts).

### Move File

Move a file from one folder to another within the same drive.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteId` | Site Id | See action definition |
| `driveId` | Drive Id | See action definition |
| `fileId` | The file you want to move. | Yes |
| `destinationFolderId` | The folder to move the file into. Select "Root" to move to the top level of the drive. | Yes |
| `newName` | Provide a new name to rename the file during the move. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/actions/move-file.ts).

## Events and recurring work

- **[New File in Folder](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/triggers/new-file-in-folder.ts)** — Fires when a new file is created or added in a specific folder.
- **[New File in Subfolders](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/triggers/new-file-in-subfolders.ts)** — Fires when a new file is added anywhere in the first-level subfolders of a folder. Note: This trigger will not monitor subfolders created after the flow is activated.
- **[New List Item](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-sharepoint/src/lib/triggers/new-list-item.ts)** — Triggers when a new item is created in a SharePoint list.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Microsoft SharePoint to create list. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
