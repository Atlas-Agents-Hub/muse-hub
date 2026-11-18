---
name: buffer-connector
description: "Schedule, publish and analyze social media posts across multiple channels with Buffer."
---

# Buffer for Muse

Schedule, publish and analyze social media posts across multiple channels with Buffer.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Buffer**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/index.ts).

## Actions

### Create Idea

Save a new idea to your Buffer Idea Bank.

| Input | What to provide | Required |
| --- | --- | --- |
| `organizationId` | Organization Id | See action definition |
| `groupId` | Group Id | See action definition |
| `title` | A short title or headline for the idea. | Optional |
| `text` | The main body of the idea. | Optional |
| `imageUrls` | Public URLs of images to attach to the idea. | Optional |
| `aiAssisted` | Mark this idea as created with AI assistance. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/lib/actions/create-idea.ts).

### Create Post

Create a post in Buffer and add it to the queue, share it next, share it now, or schedule it for a custom time. Each run also loads your channel list (one extra Buffer API request, counted against your plan limit; Free: 600 a day).

| Input | What to provide | Required |
| --- | --- | --- |
| `organizationId` | Organization Id | See action definition |
| `channelIds` | Channel Ids | See action definition |
| `text` | The text content of the post. | Yes |
| `mode` | When and how the post should be published. | Yes |
| `dueAt` | When to publish the post. Required when Share Mode is "Schedule for Custom Time". ISO 8601 (UTC). | Optional |
| `schedulingType` | Use "Automatic" for channels Buffer can publish to directly. Use "Notification" for channels that require manual publishing via the Buffer mobile app (e.g. Instagram personal accounts). | Yes |
| `saveToDraft` | Save the post as a draft instead of scheduling it. Drafts are not published until explicitly scheduled. | Optional |
| `imageUrls` | Public URLs of images to attach to the post. | Optional |
| `linkUrl` | A link to share. On Facebook, LinkedIn, Threads, Bluesky and Substack it becomes a link preview card when no images are attached; otherwise it is added to the end of the text. | Optional |
| `youtubeTitle` | The video title. Required when a YouTube channel is selected; ignored for other channels. | Optional |
| `youtubeCategoryId` | The video category. Required when a YouTube channel is selected; ignored for other channels. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/lib/actions/create-post.ts).

## Events and recurring work

- **[New Channel](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/lib/triggers/new-channel.ts)** — Triggers when a new channel is connected to your Buffer organization. Each check uses one Buffer API request, which counts against your plan limit (Free: 600 a day).
- **[New Queue Item](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/lib/triggers/new-queue-item.ts)** — Triggers when a new post is queued in Buffer. Each check usually uses one Buffer API request (one more per 100 matching posts, at most 10 per check; any left over are picked up on the next check), which counts against your plan limit (Free: 600 a day).
- **[New Sent Post](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/buffer/src/lib/triggers/new-sent-item.ts)** — Triggers when a Buffer post is successfully published. Each check usually uses one Buffer API request (one more per 100 posts sent in the last 24 hours, at most 10 per check), which counts against your plan limit (Free: 600 a day). If more than 1,000 posts are sent in one day, only the 1,000 with the latest scheduled times are checked.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Buffer to create idea. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
