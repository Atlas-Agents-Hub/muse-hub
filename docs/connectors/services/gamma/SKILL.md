---
name: gamma-connector
description: "An AI-powered design partner that helps users generate presentations, documents, social media posts, cards, etc., via natural language."
---

# Gamma for Muse

An AI-powered design partner that helps users generate presentations, documents, social media posts, cards, etc., via natural language.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Gamma**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gamma/src/index.ts).

## Actions

### Generate Gamma

Create a new Gamma generation job.

| Input | What to provide | Required |
| --- | --- | --- |
| `folderId` | The folder to save the generated gamma into. | Optional |
| `inputText` | Text used to generate your gamma (1-400,000 characters). | Yes |
| `textMode` | How you want your inputText to be modified. | Optional |
| `format` | The type of artifact you want to create. | Optional |
| `themeName` | The theme from Gamma to be used. Defaults to workspace default. | Optional |
| `numCards` | How many cards to create (default 10). Pro: 1-50, Ultra: 1-75. | Optional |
| `cardSplit` | How your content will be divided into cards. Use '---' in text for breaks. | Optional |
| `additionalInstructions` | Extra specifications about the desired content and layouts (1-500 characters). | Optional |
| `exportAs` | Additional file types for saving your gamma. | Optional |
| `textOptions` | JSON object for text attributes (e.g., amount, tone, audience, language). | Optional |
| `imageOptions` | JSON object for image attributes (e.g., source, model, style). | Optional |
| `cardOptions` | JSON object for card attributes (e.g., dimensions). | Optional |
| `sharingOptions` | JSON object for sharing attributes (e.g., workspaceAccess, externalAccess). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gamma/src/lib/actions/generate-gamma.ts).

### Get Generation

Given a Generation ID, fetch the status, outputs, metadata, etc.

| Input | What to provide | Required |
| --- | --- | --- |
| `generationId` | The ID of the generation job (from the "Generate Gamma" action). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/gamma/src/lib/actions/get-generation.ts).

## Try it

> Use Gamma to get generation. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect gamma
```

Available HTTP reads: `read-v1-0-folders`, `read-v1-0-generations-generationid`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
