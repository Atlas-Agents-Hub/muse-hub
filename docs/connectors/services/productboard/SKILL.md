---
name: productboard-connector
description: "Productboard is a product management tool that helps you manage your product roadmap and features."
---

# Productboard for Muse

Productboard is a product management tool that helps you manage your product roadmap and features.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Productboard**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/index.ts).

## Actions

### Create Feature

Create a new feature in Productboard

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Name of the feature | Yes |
| `description` | Description of the feature | Yes |
| `type` | Type of the feature | Yes |
| `status` | Status | See action definition |
| `parent_type` | Parent Type | Yes |
| `parent_id` | Parent | Yes |
| `archived` | A flag denoting if the feature is archived. If null, it will default to `false`. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/actions/create-feature.ts).

### Create Note

Creates a new note in Productboard

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Title of the feedback note | Yes |
| `content` | HTML-encoded rich text content of the feedback note | Yes |
| `user_email` | Email address of a user to be attached to the note. This field can't be combined with `Company Domain`. | Optional |
| `company_domain` | Domain of a company the note should be linked to. This field can't be combined with `User Email`. | Optional |
| `display_url` | URL where the external entity can be accessed. | Optional |
| `source_origin` | A unique string identifying the external system from which the data came. | Optional |
| `source_record_id` | The unique id of the record in the origin system. | Optional |
| `tags` | A set of tags for categorizing the note. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/actions/create-note.ts).

### Get Feature

Get an existing feature in Productboard

| Input | What to provide | Required |
| --- | --- | --- |
| `feature_id` | Feature_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/actions/get-feature.ts).

### Update Feature

Updates an existing feature in Productboard.

| Input | What to provide | Required |
| --- | --- | --- |
| `feature_id` | Feature_Id | See action definition |
| `name` | New name for the feature. | Optional |
| `description` | New description for the feature. | Optional |
| `status` | Status | See action definition |
| `archived` | Whether the feature is archived. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/actions/update-feature.ts).

## Events and recurring work

- **[New Feature](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/triggers/new-feature.ts)** — Triggers when a new feature is created in Productboard
- **[New Note](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/triggers/new-note.ts)** — Triggers when a new note is created in Productboard
- **[Updated Feature](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/productboard/src/lib/triggers/updated-feature.ts)** — Triggers when an existing feature is updated in Productboard

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Productboard to get feature. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
