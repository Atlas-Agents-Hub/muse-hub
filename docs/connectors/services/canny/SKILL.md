---
name: canny-connector
description: "Product feedback management platform. Collect, organize, and prioritize feature requests from your users."
---

# Canny for Muse

Product feedback management platform. Collect, organize, and prioritize feature requests from your users.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Canny**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/index.ts).

## Actions

### Create Post

Creates a new post on a Canny board.

| Input | What to provide | Required |
| --- | --- | --- |
| `boardID` | Board Id | See action definition |
| `authorID` | The unique identifier of the post author (Canny user ID). | Yes |
| `title` | A brief title describing the post. | Yes |
| `details` | The longer description of the post. | Yes |
| `byID` | The unique identifier of the admin creating the post on behalf of the author. | Optional |
| `categoryID` | The unique identifier of the category to assign. | Optional |
| `ownerID` | The unique identifier of the user responsible for completing the work. | Optional |
| `eta` | The estimated delivery date in MM/YYYY format (e.g. "06/2026"). | Optional |
| `etaPublic` | Whether the ETA should be visible to all users. | Optional |
| `customFields` | Custom fields as key-value pairs (keys max 30 chars, values max 200 chars). | Optional |
| `createdAt` | Original creation date in ISO 8601 format, for migrating posts from another source. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/lib/actions/create-post.ts).

### Create Vote

Casts a vote on a post on behalf of a user.

| Input | What to provide | Required |
| --- | --- | --- |
| `postID` | The unique identifier of the post to vote on. | Yes |
| `voterID` | The unique identifier of the voter (Canny user ID). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/lib/actions/create-vote.ts).

### Delete Vote

Removes a vote from a post for a given user.

| Input | What to provide | Required |
| --- | --- | --- |
| `postID` | The unique identifier of the post to remove the vote from. | Yes |
| `voterID` | The unique identifier of the voter (Canny user ID). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/lib/actions/delete-vote.ts).

### List Posts

Returns a list of posts for a board, with optional filtering and sorting.

| Input | What to provide | Required |
| --- | --- | --- |
| `boardID` | The board to list posts for (optional — omit to list across all boards). | Optional |
| `search` | A search query to filter posts. | Optional |
| `sort` | The order of returned posts. | Optional |
| `status` | Comma-separated list of statuses to filter by (e.g. "open,planned"). | Optional |
| `limit` | Number of posts to fetch (default 10). | Optional |
| `skip` | Number of posts to skip (for pagination). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/lib/actions/list-posts.ts).

### Retrieve Post

Retrieves the details of an existing post by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | The unique identifier of the post. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/canny/src/lib/actions/retrieve-post.ts).

## Try it

> Use Canny to list posts. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
