---
name: formbricks-connector
description: "Open source Survey Platform"
---

# Formbricks for Muse

Open source Survey Platform

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Formbricks**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **App URL** (`appUrl`): ShortText
- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/index.ts).

## Actions

### Find Contact

Finds a contact by email or user ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `email` | Fill in the email or the user ID. | Optional |
| `userId` | User ID | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/find-contact.ts).

### Get Personal Survey Link

Generates a survey link tied to one contact, so the response is linked to them.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `surveyId` | Survey Id | See action definition |
| `contactId` | Use Find Contact to get the ID from an email. | Yes |
| `expirationDays` | 1 to 365. Leave empty for a link that never expires. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/get-contact-survey-link.ts).

### Get Response

Gets a single survey response by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `responseId` | From a Formbricks trigger or List Responses. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/get-response.ts).

### Get Survey

Gets a survey with its questions and their IDs.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `surveyId` | Survey Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/get-survey.ts).

### List Actions

Lists the user actions (action classes) that can trigger in-app surveys.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Only actions of this workspace. Leave empty for all. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/list-action-classes.ts).

### List Contact Attribute Keys

Lists the contact attributes (email, user ID and custom ones) defined in Formbricks.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Only keys of this workspace. Leave empty for all. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/list-contact-attribute-keys.ts).

### List Responses

Lists survey responses, newest first, with optional survey and date filters.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `surveyId` | Survey Id | See action definition |
| `startDate` | Only responses created on or after this date. | Optional |
| `endDate` | Only responses created on or before this date. | Optional |
| `limit` | Responses per page (1 to 250). | Optional |
| `skip` | Number of responses to skip, for paging. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/list-responses.ts).

### List Surveys

Lists the surveys in a workspace, optionally only those with a given status. Scans up to 1,000 surveys; "More Available" is true when the list may be incomplete.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `status` | Only list surveys with this status. | Optional |
| `limit` | Maximum number of surveys to return (1 to 500). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/formbricks/src/lib/actions/list-surveys.ts).

## Try it

> Use Formbricks to find contact. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
