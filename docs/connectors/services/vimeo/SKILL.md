---
name: vimeo-connector
description: "Vimeo: add video to folder, add video to showcase, delete video."
---

# Vimeo for Muse

Vimeo: add video to folder, add video to showcase, delete video.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Vimeo**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://api.vimeo.com/oauth/authorize>
- Token endpoint: <https://api.vimeo.com/oauth/access_token>

Provider scopes: `delete`, `edit`, `interact`, `private`, `public`, `upload`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/index.ts).

## Actions

### Add Video to Folder

Adds an existing video to a user's folder

| Input | What to provide | Required |
| --- | --- | --- |
| `videoId` | Video Id | See action definition |
| `folderId` | Folder Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/actions/add-video-to-folder.ts).

### Add Video to Showcase

Adds an existing video to a user's showcase

| Input | What to provide | Required |
| --- | --- | --- |
| `videoId` | Video Id | See action definition |
| `showcaseId` | ID of the showcase to add the video to | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/actions/add-video-to-showcase.ts).

### Delete Video

Delete a video from Vimeo

| Input | What to provide | Required |
| --- | --- | --- |
| `videoId` | Video Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/actions/delete-video.ts).

### Upload Video

Upload a video to your Vimeo account

| Input | What to provide | Required |
| --- | --- | --- |
| `videoUrl` | URL of the video file to upload | Yes |
| `name` | Name for the video | Yes |
| `description` | Description for the video | Optional |
| `privacy` | Privacy setting for the video | Optional |
| `password` | Privacy | Yes |
| `allowEmbed` | Allow others to embed this video | Optional |
| `allowDownload` | Allow others to download this video (not available for free Vimeo users) | Optional |
| `contentRating` | Content rating for the video | Optional |
| `folderId` | Folder Id | See action definition |
| `language` | Language code for the video | Optional |
| `license` | License for the video | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/actions/upload-video.ts).

## Events and recurring work

- **[New Video by Search](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/triggers/new-video-by-search.ts)** — Triggers when a new video is added that matches a search query
- **[New Video by User](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/triggers/new-video-by-user.ts)** — Triggers when another specified user adds a video
- **[New Video I've Liked](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/vimeo/src/lib/triggers/new-video-liked.ts)** — Triggers when you like a new video on Vimeo

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Vimeo to add video to folder. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
