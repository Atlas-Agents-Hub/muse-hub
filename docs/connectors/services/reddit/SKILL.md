---
name: reddit-connector
description: "Interact with Reddit - fetch and submit posts."
---

# Reddit for Muse

Interact with Reddit - fetch and submit posts.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Reddit**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://www.reddit.com/api/v1/authorize>
- Token endpoint: <https://www.reddit.com/api/v1/access_token>

Provider scopes: `edit`, `flair`, `history`, `identity`, `mysubreddits`, `privatemessages`, `read`, `report`, `save`, `submit`, `subscribe`, `wikiread`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/index.ts).

## Actions

### Create Comment

Comment on a Reddit post or reply to a comment.

| Input | What to provide | Required |
| --- | --- | --- |
| `parent_id` | ID of the post (t3_*) or comment (t1_*) to reply to. | Yes |
| `content` | Text of the comment. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/create-reddit-comment.ts).

### Create Post

Submit a new self (text) post to a subreddit.

| Input | What to provide | Required |
| --- | --- | --- |
| `subreddit` | The subreddit to post in (without r/). | Yes |
| `title` | Title of the Reddit post. | Yes |
| `content` | Text content of the post. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/create-reddit-post.ts).

### Delete Post

Delete a specific Reddit post by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `post_id` | ID of the Reddit post to delete (e.g., "abc123" or "t3_abc123"). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/delete-reddit-post.ts).

### Edit Comment

Edits the content of an existing Reddit comment.

| Input | What to provide | Required |
| --- | --- | --- |
| `comment_id` | ID of the Reddit comment to edit (e.g., "def456" or "t1_def456"). | Yes |
| `content` | Updated text content for the comment. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/edit-reddit-comment.ts).

### Edit Post

Edits the content of an existing Reddit post.

| Input | What to provide | Required |
| --- | --- | --- |
| `post_id` | ID of the Reddit post to edit (e.g., "abc123" or "t3_abc123"). | Yes |
| `content` | Updated text content for the post. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/edit-reddit-post.ts).

### Fetch Post Comments

Fetch comments from a specific Reddit post.

| Input | What to provide | Required |
| --- | --- | --- |
| `post_id` | The ID of the Reddit post (e.g. "abc123" or "t3_abc123"). | Yes |
| `sort` | Sorting method for comments | Optional |
| `limit` | Maximum number of top-level comments to fetch | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/fetch-post-comments.ts).

### Get Post Details

Fetch detailed information about a specific Reddit post using its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `post_id` | The ID of the Reddit post (e.g. "t3_abc123" or "abc123") | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/get-reddit-post-details.ts).

### Retrieve Post

Fetch top posts in a subreddit with optional size limit.

| Input | What to provide | Required |
| --- | --- | --- |
| `post_category` | Select the category of posts to retrieve | Yes |
| `subreddit` | The subreddit to fetch posts from | Yes |
| `size` | Number of posts to fetch (max 100) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/reddit/src/lib/actions/retrieve-reddit-post.ts).

## Try it

> Use Reddit to get post details. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
