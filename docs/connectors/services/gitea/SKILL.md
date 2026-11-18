---
name: gitea-connector
description: "Self-hosted Git service"
---

# Gitea for Muse

Self-hosted Git service

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Gitea**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Base URL** (`baseUrl`): Enter your Gitea instance URL (e.g., https://gitea.com)

Provider scopes: `read:issue`, `read:repository`, `read:user`, `write:issue`, `write:repository`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/index.ts).

## Actions

### Add Comment to Issue/PR

Adds a comment to an issue or pull request.

| Input | What to provide | Required |
| --- | --- | --- |
| `repository` | Repository | See action definition |
| `index` | The index of the issue or pull request. | Yes |
| `body` | Comment Body | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/actions/create-comment.ts).

### Create Issue

Creates a new issue in a repository.

| Input | What to provide | Required |
| --- | --- | --- |
| `repository` | Repository | See action definition |
| `title` | Title | Yes |
| `body` | Body | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/actions/create-issue.ts).

### Update Repository

Update repository settings.

| Input | What to provide | Required |
| --- | --- | --- |
| `repository` | Repository | See action definition |
| `name` | The name of the repository. | Optional |
| `description` | Description | Optional |
| `private` | Private | Optional |
| `website` | Website | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/actions/update-repo.ts).

## Events and recurring work

- **[New Commit](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/triggers/new-commit.ts)** — Triggers when a new commit is pushed to a repository.
- **[New Issue](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/triggers/new-issue.ts)** — Triggers when a new issue is created.
- **[New Pull Request](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gitea/src/lib/triggers/new-pull-request.ts)** — Triggers when a new pull request is created.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Gitea to add comment to issue/pr. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
