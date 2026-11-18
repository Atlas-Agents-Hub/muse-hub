---
name: google-drive-connector
description: "Cloud storage and file backup"
---

# Google Drive for Muse

Cloud storage and file backup

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Drive**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-drive/src/index.ts).

## Actions

## Events and recurring work

- **[New File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-drive/src/lib/triggers/new-file.ts)** — Triggers when a file is created in Drive or the chosen folder. Uploads and copies count. A file moved in from another folder fires only if it is newer than the last file this trigger sent.
- **[New Folder](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-drive/src/lib/triggers/new-folder.ts)** — Triggers when a new folder is created in Drive or the chosen folder.
- **[New or Updated File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-drive/src/lib/triggers/new-or-updated-file.ts)** — Triggers when a file is created or edited. A rename counts; trashing or moving does not.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Drive to new file. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
