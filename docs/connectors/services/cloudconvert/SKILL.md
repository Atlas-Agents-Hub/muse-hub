---
name: cloudconvert-connector
description: "File conversion and processing platform supporting 200+ formats"
---

# CloudConvert for Muse

File conversion and processing platform supporting 200+ formats

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **CloudConvert**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://cloudconvert.com/oauth/authorize>
- Token endpoint: <https://cloudconvert.com/oauth/token>
- **Region** (`region`): CloudConvert processing region

Provider scopes: `task.read`, `task.write`, `user.read`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/index.ts).

## Actions

### Archive File

Creates a ZIP, RAR, 7Z, TAR, TAR.GZ or TAR.BZ2 archive

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/archive-file.ts).

### Capture Website

Capture webpage as PDF, screenshot PNG, or JPG from a URL

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/capture-website.ts).

### Convert File

Create a basic file conversion task for a single file with desired output format

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/convert-file.ts).

### Download a File

Downloads output from a completed task

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/download-file.ts).

### Merge Files to PDF

Combine multiple documents/images into a single PDF

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/merge-pdf.ts).

### Optimize File

Creates a task to optimize and compress a file

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/actions/optimize-file.ts).

## Events and recurring work

- **[Job Failed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/triggers/job-failed.ts)** — Triggers when a CloudConvert job has failed
- **[Job Finished](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/triggers/job-finished.ts)** — Triggers when a CloudConvert job has been completed
- **[New Job Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cloudconvert/src/lib/triggers/new-job.ts)** — Triggers when a new job has been created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use CloudConvert to archive file. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect cloudconvert
```

Available HTTP reads: `read-v2-users-me`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
