---
name: wordpress-connector
description: "Open-source website creation software"
---

# WordPress for Muse

Open-source website creation software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **WordPress**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Username** (`username`): The WordPress user the flow acts as.
- **Password** (`password`): ProviderField
- **Website URL** (`website_url`): Address of your WordPress site.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/index.ts).

## Actions

### Get Media

Gets one media library file by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `media_id` | ID of the media item, from list_media or upload_media. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/get-media.action.ts).

### Get Page

Gets one site page by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `page_id` | ID of the page, from list_pages or search_site_content. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/get-page.action.ts).

### Get Post Details

Fetch one post by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Number after post= in the post's edit URL. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/get-post.action.ts).

### List Media

Lists files in the media library, optionally filtered by keyword, type or attached post.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Only files whose title, caption or file name contain this text. | Optional |
| `media_type` | Only files of this general type. | Optional |
| `mime_type` | Only files with this exact MIME type, e.g. image/png. | Optional |
| `parent` | Only files attached to this post or page ID. Use 0 for unattached files. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/list-media.action.ts).

### List Pages

Lists site pages, optionally filtered by keyword, status or parent page.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Only pages whose title or content contain this text. | Optional |
| `status` | Page statuses to include. Defaults to published only. "Any" includes every status except trash. | Optional |
| `parent` | Only direct children of this page ID. Use 0 for top-level pages. | Optional |
| `orderby` | Sort field. Defaults to date. "Relevance" needs Search. | Optional |
| `order` | Sort direction. Defaults to descending. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/list-pages.action.ts).

### List Posts

Lists blog posts, optionally filtered by keyword, status, category, tag, author or date.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Only posts whose title, content or excerpt contain this text. | Optional |
| `status` | Post statuses to include. Defaults to published only. "Any" includes every status except trash. | Optional |
| `categories` | Only posts in any of these category IDs (from list_categories). | Optional |
| `tags` | Only posts with any of these tag IDs (from list_tags). | Optional |
| `author` | Only posts by this user ID (from list_users). | Optional |
| `after` | Only posts published after this ISO 8601 date, e.g. 2026-01-31T00:00:00. | Optional |
| `before` | Only posts published before this ISO 8601 date. | Optional |
| `orderby` | Sort field. Defaults to date. "Relevance" needs Search. | Optional |
| `order` | Sort direction. Defaults to descending. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/list-posts.action.ts).

### List Tags

Lists post tags, optionally filtered by name or post.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Only tags whose name or slug contain this text. | Optional |
| `slug` | Only the tag with this exact slug. | Optional |
| `post` | Only tags assigned to this post ID (from list_posts). | Optional |
| `hide_empty` | Whether to leave out tags with no published posts. Defaults to No. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/list-tags.action.ts).

### List Users

Lists site users, optionally filtered by name or role.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Only users whose name, slug, email or URL contain this text. | Optional |
| `roles` | Only users with any of these role slugs, e.g. administrator, editor, author, contributor, subscriber. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wordpress/src/lib/actions/list-users.action.ts).

## Try it

> Use WordPress to get media. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
