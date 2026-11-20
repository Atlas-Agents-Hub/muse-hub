---
name: apify-connector
description: "Access Apify tools for web scraping, data extraction, and automation."
---

# Apify for Muse

Access Apify tools for web scraping, data extraction, and automation.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Apify**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Apikey** (`apikey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/index.ts).

## Actions

### Find Actor

Searches the public Apify Store for Actors by name or keyword.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Name or keyword to search the Apify Store for (e.g. "instagram scraper"). Leave empty to list popular store actors. | Optional |
| `limit` | Maximum number of actors to return. Default 50. | Optional |
| `offset` | Number of actors to skip at the start. Default 0. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/find-actor.ts).

### Get Account

Retrieves the authenticated Apify account profile.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/get-account.ts).

### Get Actor

Retrieves metadata for a single Apify Actor by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `actorId` | The ID (or "username~actor-name") of the Actor. Obtain it from Find Actor or List Actors. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/get-actor.ts).

### Get Build

Retrieves the status and metadata of an Actor build by build ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `buildId` | The ID of the build to read. Obtain it from an actor's build list or a run's buildId. | Yes |
| `waitForFinish` | Optional. Block server-side up to this many seconds (max 60) waiting for the build to finish before returning. Leave empty for an immediate status read. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/get-build.ts).

### Get Dataset

Retrieves metadata for an Apify dataset by dataset ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `datasetId` | The ID of the dataset. Obtain it from List Datasets or a run's defaultDatasetId (Get Actor Run). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/get-dataset.ts).

### Get Task

Retrieves metadata for a saved Actor task by task ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | The ID of the saved task. Obtain it from List Tasks. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/get-task.ts).

### List Runs

Lists Actor runs across the whole account.

| Input | What to provide | Required |
| --- | --- | --- |
| `status` | Optionally filter runs by status. | Optional |
| `limit` | Maximum number of runs to return. Default 50. | Optional |
| `offset` | Number of runs to skip at the start. Default 0. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/list-runs.ts).

### List Tasks

Lists the saved Actor tasks in the authenticated account.

| Input | What to provide | Required |
| --- | --- | --- |
| `limit` | Maximum number of tasks to return. Default 50. | Optional |
| `offset` | Number of tasks to skip at the start. Default 0. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/actions/list-tasks.ts).

## Events and recurring work

- **[Watch Actor Runs](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/triggers/watch-actor-runs.ts)** — Fires when a run of the Actor ends with a chosen status.
- **[Watch Task Runs](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/apify/src/lib/triggers/watch-task-runs.ts)** — Fires when a run of the task ends with a chosen status.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Apify to find actor. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
