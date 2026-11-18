---
name: lever-connector
description: "Lever is a modern, collaborative recruiting platform that powers a more human approach to hiring."
---

# Lever for Muse

Lever is a modern, collaborative recruiting platform that powers a more human approach to hiring.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Lever**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api Key** (`apiKey`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/index.ts).

## Actions

### Add feedback to opportunity

Provide feedback to a candidate after an interview

| Input | What to provide | Required |
| --- | --- | --- |
| `performAs` | Feedback author | Yes |
| `opportunityId` | Opportunity ID | Yes |
| `panelId` | If you select one, you must select an interview too | Optional |
| `interviewId` | Mandatory is you select an interview panel | Optional |
| `feedbackTemplateId` | Ignored if you select an interview panel and an interview | Optional |
| `feedbackFields` | Fields | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/lib/actions/add-feedback-to-opportunity.ts).

### Get opportunity

Retrieve a single opportunity, i.e. an individual's unique candidacy or journey for a given job position

| Input | What to provide | Required |
| --- | --- | --- |
| `opportunityId` | Opportunity ID | Yes |
| `expand` | Expand | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/lib/actions/get-opportunity.ts).

### List opportunity feedback

Get all feedback for a given opportunity, optionally for a given template

| Input | What to provide | Required |
| --- | --- | --- |
| `opportunityId` | Opportunity ID | Yes |
| `template` | Feedback template | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/lib/actions/list-opportunity-feedback.ts).

### List opportunity forms

Get all forms for a given opportunity, optionally for a given form template

| Input | What to provide | Required |
| --- | --- | --- |
| `opportunityId` | Opportunity ID | Yes |
| `template` | Form template | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/lib/actions/list-opportunity-forms.ts).

### Update opportunity stage

Change an Opportunity's current stage

| Input | What to provide | Required |
| --- | --- | --- |
| `opportunityId` | Opportunity ID | Yes |
| `stage` | Stage | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/lever/src/lib/actions/update-opportunity-stage.ts).

## Try it

> Use Lever to get opportunity. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
