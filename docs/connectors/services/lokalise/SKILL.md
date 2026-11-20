---
name: lokalise-connector
description: "Lokalise is a collaborative translation platform."
---

# Lokalise for Muse

Lokalise is a collaborative translation platform.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Lokalise**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/index.ts).

## Actions

### Create Key

Create one or more keys in your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `keyName` | The name/identifier for the key (e.g., "index.welcome") | Yes |
| `description` | Optional description for the key | Optional |
| `platforms` | Select the platforms this key applies to | Yes |
| `tags` | Comma-separated tags for the key (e.g., "urgent,ui") | Optional |
| `useAutomations` | Whether to run automations on the new key translations | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/create-key.ts).

### Create Task

Create a new task in your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `taskTitle` | Title of the task | Yes |
| `description` | Brief task description. Used as instructions for AI in automatic_translation and lqa_by_ai task types | Optional |
| `taskType` | Type of the task | Optional |
| `keys` | Comma-separated list of key IDs to include in the task (required unless parent_task_id is specified) | Optional |
| `languages` | Comma-separated language ISO codes for the task (e.g., "fr,de,es") | Yes |
| `sourceLanguageIso` | Source language code for the task | Optional |
| `dueDate` | Due date in format: Y-m-d H:i:s (e.g., "2024-12-31 23:59:59") | Optional |
| `autoCloseLanguages` | Whether languages should be closed automatically upon completion. Default is true | Optional |
| `autoCloseTask` | Whether the task should be automatically closed upon all language completion. Default is true | Optional |
| `closingTags` | Comma-separated tags to be added to keys when task is closed | Optional |
| `doLockTranslations` | If set to true, will lock translations for non-assigned project members | Optional |
| `markVerified` | Mark translations as verified. Only for automatic_translation tasks. Default is true | Optional |
| `saveAiTranslationToTm` | Save AI translations to Translation Memory. Only for automatic_translation tasks | Optional |
| `applyAiTm100Matches` | Apply 100% translation memory matches. Only for automatic_translation tasks | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/create-task.ts).

### Delete Key

Delete a key from your Lokalise project (software and marketing projects only)

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `keyId` | Key Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/delete-key.ts).

### Retrieve a comment

Retrieve a specific comment on a key in your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `keyId` | Key Id | See action definition |
| `commentId` | Unique identifier of the comment | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/retrieve-a-comment.ts).

### Retrieve a key

Retrieve detailed information about a specific key in your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `keyId` | Key Id | See action definition |
| `disableReferences` | Disable key references in the response | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/retrieve-a-key.ts).

### Retrieve a project

Retrieve detailed information about a Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/retrieve-a-project.ts).

### Retrieve Translation

Retrieve a specific translation from your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `translationId` | Unique translation identifier | Yes |
| `disableReferences` | Disable key references in the translation | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/retrieve-translation.ts).

### Update Key

Update properties of a key in your Lokalise project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `keyId` | Key Id | See action definition |
| `keyName` | Key identifier (or JSON with ios, android, web, other for per-platform names) | Optional |
| `description` | Description of the key | Optional |
| `platforms` | List of platforms enabled for this key | Optional |
| `tags` | Comma-separated tags for the key | Optional |
| `mergeTags` | Enable to merge specified tags with current tags | Optional |
| `isPlural` | Whether this key is plural | Optional |
| `pluralName` | Optional custom plural name | Optional |
| `isHidden` | Whether this key is hidden from non-admins | Optional |
| `isArchived` | Whether this key is archived | Optional |
| `context` | Optional context of the key (used with some file formats) | Optional |
| `charLimit` | Maximum allowed number of characters in translations | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/actions/update-key.ts).

## Events and recurring work

- **[Key Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/triggers/key-added.ts)** — Trigger when a new key is added to your Lokalise project
- **[Key Updated](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/triggers/key-updated.ts)** — Trigger when a key is updated in your Lokalise project
- **[Translation Updated](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lokalise/src/lib/triggers/translation-updated.ts)** — Trigger when a translation is updated in your Lokalise project

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Lokalise to retrieve a comment. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
