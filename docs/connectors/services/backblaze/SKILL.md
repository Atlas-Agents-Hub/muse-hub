---
name: backblaze-connector
description: "Scalable storage in the cloud"
---

# Backblaze for Muse

Scalable storage in the cloud

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Backblaze**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Access Key ID** (`accessKeyId`): ShortText
- **Secret Access Key** (`secretAccessKey`): ProviderField
- **Bucket** (`bucket`): ShortText
- **Endpoint** (`endpoint`): ShortText
- **Region** (`region`): StaticDropdown

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/backblaze/src/index.ts).

## Actions

### Read File

Read a file from Backblaze bucket to use it in other steps.

| Input | What to provide | Required |
| --- | --- | --- |
| `key` | The key of the file to read. include extension if file has any extension. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/backblaze/src/lib/actions/read-file.ts).

### Upload File

Upload an File to bucket.

| Input | What to provide | Required |
| --- | --- | --- |
| `file` | File | Yes |
| `fileName` | my-file-name (no extension). write full path if you want to store in the directories or sub-directories. | Optional |
| `acl` | ACL | Optional |
| `type` | Type | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/backblaze/src/lib/actions/upload-file.ts).

## Events and recurring work

- **[New File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/backblaze/src/lib/triggers/new-file.ts)** — Trigger when a new file is uploaded.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Backblaze to read file. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
