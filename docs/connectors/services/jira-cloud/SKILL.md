---
name: jira-cloud-connector
description: "Issue tracking and project management"
---

# Jira Cloud for Muse

Issue tracking and project management

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Jira Cloud**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Instance URL** (`instanceUrl`): The link of your Jira instance (e.g https://example.atlassian.net)
- **Email** (`email`): The email you use to login to Jira
- **Api Token** (`apiToken`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/index.ts).

## Actions

### Assign Issue

Assigns an issue to a user.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `issueId` | Issue Id | See action definition |
| `assignee` | Assignee | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/assign-issue.ts).

### Create Issue

Creates a new issue in a project.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `issueTypeId` | Issue Type Id | See action definition |
| `issueFields` | Fields | Yes |
| `adfFields` | Fields whose value is Atlassian Document Format JSON, not plain text. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/create-issue.ts).

### Find User

Finds an existing user.

| Input | What to provide | Required |
| --- | --- | --- |
| `keyword` | Matches part of a name or email address. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/find-user.ts).

### Get Issue

Gets an issue's fields and details.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `issueId` | Issue Id | See action definition |
| `expand` | More sections to include in the output. | Optional |
| `mapNames` | Key fields by their name instead of their ID. | Optional |
| `mapTransitions` | Adds the issue's transitions, keyed by name. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/get-issue.ts).

### Get Issue Attachment

Gets an attachment's details and downloads its file.

| Input | What to provide | Required |
| --- | --- | --- |
| `attachmentId` | Found in a Get Issue step's output, under fields → attachment. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/get-issue-attachment.ts).

### Link Issues

Creates a link between two issues.

| Input | What to provide | Required |
| --- | --- | --- |
| `linkInfo` | Link Info | Optional |
| `firstIssueId` | First Issue Id | See action definition |
| `issueLinkTypeId` | Issue Link Type Id | See action definition |
| `secondIssueId` | Second Issue Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/link-issues.ts).

### List Issue Comments

Lists an issue's comments, newest or oldest first.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `issueId` | Issue Id | See action definition |
| `orderBy` | Order By | Yes |
| `limit` | Most comments to return. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/list-issue-comments.ts).

### Search Issues

Finds issues that match a JQL query.

| Input | What to provide | Required |
| --- | --- | --- |
| `memoryWarning` | Memory Warning | Optional |
| `jql` | Put text and dates in single quotes. | Yes |
| `fields` | Field IDs, e.g. summary. Use *all for every field. | Optional |
| `mapNames` | Key fields by their name instead of their ID. | Optional |
| `maxResults` | Most issues to return, up to 5,000. | Yes |
| `sanitizeJql` | Jira swaps names you can't view for IDs before the search runs. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/actions/search-issues.ts).

## Events and recurring work

- **[Issue Assigned](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/triggers/issue-assigned.ts)** — Triggers when an issue is assigned to someone.
- **[New Attachment on Issue](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/triggers/new-attachment.ts)** — Triggers when a file is attached to an issue.
- **[New Comment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/jira-cloud/src/lib/triggers/new-comment.ts)** — Triggers when a comment is added to an issue.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Jira Cloud to find user. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
