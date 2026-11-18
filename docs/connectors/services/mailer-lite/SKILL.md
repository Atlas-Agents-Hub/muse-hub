---
name: mailer-lite-connector
description: "Email marketing software"
---

# MailerLite for Muse

Email marketing software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **MailerLite**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/index.ts).

## Actions

### Get Campaign

Get a campaign by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `campaign_id` | The campaign ID, from list_campaigns. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/get-campaign.ts).

### Get Form

Get a form by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `form_id` | The form ID, from list_forms. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/get-form.ts).

### Get Webhook

Get a webhook by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `webhook_id` | The webhook ID, from list_webhooks. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/get-webhook.ts).

### List Fields

List the subscriber fields in the account.

| Input | What to provide | Required |
| --- | --- | --- |
| `keyword` | Only return fields whose name contains this text. | Optional |
| `type` | Only return fields of this type. | Optional |
| `limit` | Items to return (1-100, default 100). | Optional |
| `page` | Page number to return, starting at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/list-fields.ts).

### List Forms

List signup forms of one type.

| Input | What to provide | Required |
| --- | --- | --- |
| `type` | The type of forms to list. | Yes |
| `name` | Only return forms whose name contains this text. | Optional |
| `limit` | Items to return (1-100, default 25). | Optional |
| `page` | Page number to return, starting at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/list-forms.ts).

### List Groups

List groups in the account, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `limit` | How many groups to return per page, up to 1000. | Optional |
| `page` | Page number, starting at 1; meta.last_page in the response is last. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/list-groups.ts).

### List Segments

List the segments in the account.

| Input | What to provide | Required |
| --- | --- | --- |
| `limit` | Items to return (1-250, default 50). | Optional |
| `page` | Page number to return, starting at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/list-segments.ts).

### List Webhooks

List the webhooks in the account.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailer-lite/src/lib/actions/list-webhooks.ts).

## Try it

> Use MailerLite to get campaign. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
