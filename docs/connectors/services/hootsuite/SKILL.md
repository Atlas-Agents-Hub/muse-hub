---
name: hootsuite-connector
description: "Social media management \u2014 schedule posts and manage multiple networks from one dashboard."
---

# Hootsuite for Muse

Social media management — schedule posts and manage multiple networks from one dashboard.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Hootsuite**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://platform.hootsuite.com/oauth2/auth>
- Token endpoint: <https://platform.hootsuite.com/oauth2/token>

Provider scopes: `offline`, `post`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/index.ts).

## Actions

### Delete Post

Permanently deletes a post. Only posts in a deletable state (e.g. SCHEDULED) can be removed.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | The unique ID of the post to delete. You can get this from the "Schedule Post" or "Get Post Details" action. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/lib/actions/delete-message.ts).

### Get Post Details

Retrieves the details of a specific scheduled or published post by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | The unique ID of the post. You can get this from a previous "Schedule Post" action output or from the Hootsuite dashboard URL. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/lib/actions/get-message.ts).

### Schedule Post

Schedules or immediately publishes a post to one or more social media profiles.

| Input | What to provide | Required |
| --- | --- | --- |
| `socialProfileIds` | Select the social media profiles to post to. | Yes |
| `text` | The text content of your post. | Yes |
| `scheduledSendTime` | When to publish the post (UTC, must be at least 5 minutes in the future). Leave empty to post immediately. | Optional |
| `emailNotification` | Send an email notification when the post is published. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/lib/actions/create-message.ts).

## Events and recurring work

- **[New Published Post](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/lib/triggers/new-published-post.ts)** — Triggers when a post is published (sent) in Hootsuite.
- **[New Scheduled Post](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/hootsuite/src/lib/triggers/new-scheduled-post.ts)** — Triggers when a new post is scheduled in Hootsuite.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Hootsuite to get post details. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
