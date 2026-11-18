---
name: cohere-connector
description: "Generate text using Cohere AI language models"
---

# Cohere for Muse

Generate text using Cohere AI language models

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Cohere**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cohere/src/index.ts).

## Actions

### Generate Text

Generate a text response using Cohere AI Chat API

| Input | What to provide | Required |
| --- | --- | --- |
| `prompt` | The user message to send to the model | Yes |
| `model` | The Cohere model to use for generation | Yes |
| `temperature` | Controls randomness (0.0 = deterministic, 1.0 = maximum randomness). Default: 0.3 | Optional |
| `maxTokens` | Maximum number of tokens to generate. Leave empty for model default. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/cohere/src/lib/actions/generate-text.ts).

## Try it

> Use Cohere to generate text. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect cohere
```

Available HTTP reads: `read-v2-models`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
