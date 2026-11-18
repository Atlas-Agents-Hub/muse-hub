---
name: raindrop-connector
description: "Bookmark manager to save, search, and organize content from the web"
---

# Raindrop for Muse

Bookmark manager to save, search, and organize content from the web

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Raindrop**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://raindrop.io/oauth/authorize>
- Token endpoint: <https://raindrop.io/oauth/access_token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/index.ts).

## Actions

### Create Bookmark

Saves a new bookmark to your Raindrop.io account

| Input | What to provide | Required |
| --- | --- | --- |
| `link` | The URL of the page to bookmark | Yes |
| `title` | Custom title for the bookmark. If left empty, Raindrop will extract it from the URL automatically. | Optional |
| `excerpt` | Short description or summary of the page | Optional |
| `note` | Personal note to attach to this bookmark | Optional |
| `collection_id` | Collection_Id | See action definition |
| `tags` | List of tags to organize the bookmark (press Enter to add each tag) | Optional |
| `important` | Mark this bookmark as important / favourite | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/lib/actions/create-raindrop.ts).

### Delete Bookmark

Moves a bookmark to the trash. To permanently delete it, empty the trash in Raindrop.io.

| Input | What to provide | Required |
| --- | --- | --- |
| `raindrop_id` | The numeric ID of the bookmark to delete. You can find it in the URL when viewing the bookmark in Raindrop.io (e.g. raindrop.io/app/raindrop/123456789). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/lib/actions/delete-raindrop.ts).

### Find Bookmarks

Lists bookmarks from a collection, with optional keyword search

| Input | What to provide | Required |
| --- | --- | --- |
| `collection_id` | Collection_Id | See action definition |
| `search` | Filter bookmarks by keyword. Supports operators like #tag or type:article. Leave empty to list all bookmarks. | Optional |
| `limit` | Maximum number of bookmarks to return (max 50) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/lib/actions/find-raindrops.ts).

### Get Bookmark

Retrieves the details of a bookmark by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `raindrop_id` | The numeric ID of the bookmark. You can find it in the URL when viewing the bookmark in Raindrop.io (e.g. raindrop.io/app/raindrop/123456789). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/lib/actions/get-raindrop.ts).

### Update Bookmark

Updates the details of an existing bookmark

| Input | What to provide | Required |
| --- | --- | --- |
| `raindrop_id` | The numeric ID of the bookmark to update. You can find it in the URL when viewing the bookmark in Raindrop.io (e.g. raindrop.io/app/raindrop/123456789). | Yes |
| `title` | Updated title for the bookmark | Optional |
| `excerpt` | Updated short description or summary of the page | Optional |
| `note` | Updated personal note attached to the bookmark | Optional |
| `collection_id` | Collection_Id | See action definition |
| `tags` | New list of tags (replaces existing tags). Leave empty to keep existing tags unchanged. | Optional |
| `important` | Mark or unmark this bookmark as important / favourite | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/raindrop/src/lib/actions/update-raindrop.ts).

## Try it

> Use Raindrop to find bookmarks. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
