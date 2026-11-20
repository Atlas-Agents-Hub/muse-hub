---
name: confluence-connector
description: "Confluence: find page by title, find user, get page by url."
---

# Confluence for Muse

Confluence: find page by title, find user, get page by url.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Confluence**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Account Email** (`username`): Account email for basic auth
- **Password** (`password`): ProviderField
- **Confluence Domain** (`confluenceDomain`): Example value - https://your-domain.atlassian.net (without trailing slash)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/index.ts).

## Actions

### Find Page by Title

Finds a page by exact title, optionally scoped to a space.

| Input | What to provide | Required |
| --- | --- | --- |
| `spaceId` | Space Id | See action definition |
| `title` | Exact title to match. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/find-page-by-title.ts).

### Find User

Looks up Confluence users by name, email, or keyword.

| Input | What to provide | Required |
| --- | --- | --- |
| `keyword` | Username, email, or display name to search for. | Yes |
| `limit` | Limit | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/find-user.ts).

### Get Page by URL

Fetches a page by its Confluence web URL (extracts the page ID automatically).

| Input | What to provide | Required |
| --- | --- | --- |
| `url` | Paste any Confluence page URL, e.g. https://your-domain.atlassian.net/wiki/spaces/DOCS/pages/12345/My+Page | Yes |
| `bodyFormat` | Body Format | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/get-page-by-url.ts).

### Get Page Content

Get page content and optionally all its descendants

| Input | What to provide | Required |
| --- | --- | --- |
| `pageId` | Get this from the page URL of your Confluence Cloud | Yes |
| `includeDescendants` | If checked, will fetch all child pages recursively. | Optional |
| `dynamic` | Dynamic Properties | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/get-page-content.ts).

### List Attachments

Lists all attachments on a page.

| Input | What to provide | Required |
| --- | --- | --- |
| `spaceId` | Space Id | See action definition |
| `pageId` | Page Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/list-attachments.ts).

### List Comments

Lists footer and/or inline comments on a page.

| Input | What to provide | Required |
| --- | --- | --- |
| `spaceId` | Space Id | See action definition |
| `pageId` | Page Id | See action definition |
| `commentType` | Comment Type | Yes |
| `bodyFormat` | Body Format | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/list-comments.ts).

### List Spaces

Lists all spaces the authenticated user can access.

| Input | What to provide | Required |
| --- | --- | --- |
| `type` | Type | Optional |
| `status` | Status | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/list-spaces.ts).

### Search Content (CQL)

Search Confluence content with CQL (Confluence Query Language). Example: `type = "page" AND space = "DOCS" AND title ~ "release"`.

| Input | What to provide | Required |
| --- | --- | --- |
| `cql` | Confluence Query Language expression. See https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/ | Yes |
| `maxResults` | Max Results | Yes |
| `expand` | Comma-separated list of properties to expand (e.g. `body.storage,version,space,history`). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/actions/search-pages.ts).

## Events and recurring work

- **[New Attachment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/triggers/new-attachment.ts)** — Triggers when a new attachment is uploaded to the selected page.
- **[New Blog Post](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/triggers/new-blog-post.ts)** — Triggers when a new blog post is published in the selected space.
- **[New Comment on Page](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/confluence/src/lib/triggers/new-comment.ts)** — Triggers when a new footer comment is added to the selected page.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Confluence to find page by title. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
