---
name: matomo-connector
description: "Open source alternative to Google Analytics"
---

# Matomo for Muse

Open source alternative to Google Analytics

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Matomo**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Matomo Domain** (`domain`): The domain of your Matomo account: https://matomo.example.com
- **Token Auth** (`tokenAuth`): ProviderField
- **Site ID** (`siteId`): The site ID that will be associated to this connection. Site IDs can be found on the main Websites page.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/matomo/src/index.ts).

## Actions

### Add Annotation

Add an annotation to a Matomo site

| Input | What to provide | Required |
| --- | --- | --- |
| `note` | The note to add | Yes |
| `date` | The date to add the note to. Format: YYYY-MM-DD | Yes |
| `starred` | Whether or not the note should be starred | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/matomo/src/lib/actions/add-annotation.ts).

## Try it

> Use Matomo to add annotation. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
