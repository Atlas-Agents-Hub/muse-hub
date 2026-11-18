---
name: metabase-connector
description: "The simplest way to ask questions and learn from data"
---

# Metabase for Muse

The simplest way to ask questions and learn from data

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Metabase**.
2. Configure **API key or access token; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/index.ts).

## Actions

### Embed question

Enable embedding for a Metabase question and configure parameters

| Input | What to provide | Required |
| --- | --- | --- |
| `questionId` | Metabase question ID | Yes |
| `enableEmbedding` | Whether to enable embedding for this question | Yes |
| `parameterSettings` | Parameter Settings | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/lib/actions/embed-question.ts).

### Get Dashboard Questions

Execute all questions across all tabs in a Metabase dashboard and return their consolidated results in a single response

| Input | What to provide | Required |
| --- | --- | --- |
| `dashboardId` | Metabase Dashboard ID | Yes |
| `parameters` | Dashboard parameters to apply to all questions | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/lib/actions/get-dashboard.ts).

### Get question

Fetch the results of a Metabase question

| Input | What to provide | Required |
| --- | --- | --- |
| `questionId` | Metabase question ID | Yes |
| `parameters` | Parameters (slug name -> value) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/lib/actions/get-question.ts).

### Get Question PNG Preview

Get PNG preview rendering (low resolution) of a Metabase card/question.

| Input | What to provide | Required |
| --- | --- | --- |
| `questionId` | Metabase question ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/lib/actions/get-png-rendering.ts).

### Get the graph of the question

Get the graph of a Metabase question and save it as a png

| Input | What to provide | Required |
| --- | --- | --- |
| `questionId` | Metabase question ID | Yes |
| `parameters` | Parameters (slug name -> value) | Optional |
| `graphName` | The name of the graph (without the extension) | Optional |
| `waitTime` | How long to wait for the graph to render completely in seconds | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/metabase/src/lib/actions/get-graph-question.ts).

## Try it

> Use Metabase to get dashboard questions. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
