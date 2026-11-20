---
name: ghostcms-connector
description: "Publishing platform for professional bloggers"
---

# GhostCMS for Muse

Publishing platform for professional bloggers

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **GhostCMS**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **API URL** (`baseUrl`): The API URL of your application (https://test-publication.ghost.io)
- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/index.ts).

## Actions

### Create Member

Create a new member

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |
| `name` | Full Name | Optional |
| `note` | Note | Optional |
| `newsletters` | Newsletters | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/actions/create-member.ts).

### Create Post

Create a new post

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Title | Yes |
| `slug` | Slug | Optional |
| `status` | Status | Yes |
| `publishedAt` | Published At | Optional |
| `html` | Content (HTML) | Yes |
| `customExcerpt` | Custom Excerpt | Optional |
| `author` | Author | See action definition |
| `featured` | Featured | Optional |
| `tags` | Tags | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/actions/create-post.ts).

### Find Member

Find a member by email

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/actions/find-member.ts).

### Find User

Find a staff user by email

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/actions/find-user.ts).

### Update Member

Update a member

| Input | What to provide | Required |
| --- | --- | --- |
| `member` | Member | See action definition |
| `email` | Email | Optional |
| `name` | Full Name | Optional |
| `note` | Note | Optional |
| `newsletters` | Newsletters | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/actions/update-member.ts).

## Events and recurring work

- **[Member Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/triggers/member-added.ts)** — Triggers when a new member is added
- **[Member Deleted](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/triggers/member-deleted.ts)** — Triggers when a member is deleted
- **[Member Edited](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/ghostcms/src/lib/triggers/member-edited.ts)** — Triggers when a member is edited

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use GhostCMS to find member. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
