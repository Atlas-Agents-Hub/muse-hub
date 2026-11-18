---
name: customer-io-connector
description: "Create personalized journeys across all channels with our customer engagement platform."
---

# customer.io for Muse

Create personalized journeys across all channels with our customer engagement platform.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **customer.io**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Region** (`region`): ProviderField
- **Site ID** (`track_site_id`): ShortText
- **API Key** (`track_api_key`): ShortText
- **Bearer Token** (`api_bearer_token`): ShortText

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/customer-io/src/index.ts).

## Actions

### Create Event

Create an event in Customer.io

| Input | What to provide | Required |
| --- | --- | --- |
| `customer_identifier` | The unique value representing a person. You may identify a person by id, email address, or the cio_id (when updating people), depending on your workspace settings | Yes |
| `event_name` | The name of the event. This is how you'll reference the event in campaigns or segments | Yes |
| `body_type` | Event information to be sent to Customer.io | Optional |
| `body` | Body | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/customer-io/src/lib/actions/create_event.ts).

## Try it

> Use customer.io to create event. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
