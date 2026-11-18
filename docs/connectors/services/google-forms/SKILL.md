---
name: google-forms-connector
description: "Receive form responses from Google Forms"
---

# Google Forms for Muse

Receive form responses from Google Forms

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Forms**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-forms/src/index.ts).

## Actions

### Get Form

Fetch a form's full structure: title, settings, items with their indices and itemIds, question IDs, and current revisionId.

| Input | What to provide | Required |
| --- | --- | --- |
| `form_id` | The ID of the form to fetch. Obtain it from forms_create_form, forms_list_responses, or the New Response trigger. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-forms/src/lib/actions/forms-get-form.ts).

### Get Form Response

Fetch one submission by its responseId, including all answers keyed by questionId and submission timestamps.

| Input | What to provide | Required |
| --- | --- | --- |
| `form_id` | The ID of the form the response belongs to. Obtain it from forms_list_responses or the New Response trigger. | Yes |
| `response_id` | The ID of the response to fetch. Obtain it from forms_list_responses or the New Response trigger. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-forms/src/lib/actions/forms-get-response.ts).

### List Form Responses

List submitted responses for a form, with each response's responseId, timestamps, and answers keyed by questionId.

| Input | What to provide | Required |
| --- | --- | --- |
| `form_id` | The ID of the form whose responses to list. Obtain it from forms_create_form, forms_get_form, or the New Response trigger. | Yes |
| `filter` | Optional filter on submission time, e.g. "timestamp > 2026-01-01T00:00:00Z" or "timestamp < 2026-06-01T00:00:00Z". Only the timestamp field is supported. | Optional |
| `page_size` | Maximum number of responses to return per page (default 5000). | Optional |
| `page_token` | Token from a previous call's nextPageToken to fetch the next page of responses. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-forms/src/lib/actions/forms-list-responses.ts).

## Events and recurring work

- **[New Response](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-forms/src/lib/triggers/new-form-response.ts)** — Triggers when someone submits a response to the form. Can also trigger when a respondent edits their response.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Forms to get form. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect google-forms
```

Available HTTP reads: `read-v1-forms-form-id`, `read-v1-forms-form-id-responses-response-id`, `read-v1-forms-form-id-responses`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
