---
name: bannerbear-connector
description: "Automate image generation"
---

# Bannerbear for Muse

Automate image generation

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Bannerbear**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/index.ts).

## Actions

### Create Image

Create image from Bannerbear template

| Input | What to provide | Required |
| --- | --- | --- |
| `template` | Template | See action definition |
| `template_version` | Render a specific template version. Leave empty for latest. | Optional |
| `modifications` | Values for each template layer. Empty fields are skipped. | Yes |
| `transparent` | Render a PNG with a transparent background. | Optional |
| `render_pdf` | Also render a PDF (uses extra credits). | Optional |
| `metadata` | Any text to store with the image, e.g. a record ID. | Optional |
| `wait_for_completion` | Wait_For_Completion | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/create-image.ts).

### Get Account

Get plan and credit usage for this API key.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/get-account.ts).

### Get Image

Get an image and its status by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `image_uid` | The image UID returned by Create Image. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/get-image.ts).

### Get Template

Get a template and its layer names.

| Input | What to provide | Required |
| --- | --- | --- |
| `template_uid` | The template UID, from List Templates. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/get-template.ts).

### List Images

List images, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `page` | Page number, starting at 1. | Optional |
| `limit` | Images per page, 1 to 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/list-images.ts).

### List Templates

List image templates, optionally filtered by name or tag.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Only templates whose name contains this text. | Optional |
| `tag` | Only templates with this tag. | Optional |
| `page` | Page number, starting at 1. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/list-templates.ts).

### Update Template

Rename a template or change its tags.

| Input | What to provide | Required |
| --- | --- | --- |
| `template_uid` | The template UID, from List Templates. | Yes |
| `name` | New template name. | Optional |
| `tags` | Replaces all tags. Leave empty to keep current tags. | Optional |
| `metadata` | Text stored with the template. | Optional |
| `description` | Template description. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/actions/update-template.ts).

## Events and recurring work

- **[New Image Completed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bannerbear/src/lib/triggers/new-image-completed.ts)** — Triggers when an image finishes rendering.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Bannerbear to get account. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
