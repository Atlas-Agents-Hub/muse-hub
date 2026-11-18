---
name: close-connector
description: "Sales automation and CRM integration for Close"
---

# Close for Muse

Sales automation and CRM integration for Close

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Close**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/index.ts).

## Actions

### Create Contact

Creates a new contact.

| Input | What to provide | Required |
| --- | --- | --- |
| `lead_id` | Lead_Id | See action definition |
| `name` | Name | Yes |
| `title` | Title | Optional |
| `officePhone` | Office Phone | Optional |
| `mobilePhone` | Mobile Phone | Optional |
| `homePhone` | Home Phone | Optional |
| `directPhone` | Direct Phone | Optional |
| `faxPhone` | Fax Phone | Optional |
| `otherPhone` | Other Phone | Optional |
| `officeEmail` | Office Email | Optional |
| `homeEmail` | Home Email | Optional |
| `directEmail` | Direct Email | Optional |
| `otherEmail` | Other Email | Optional |
| `url` | URL | Optional |
| `customFields` | Custom Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/actions/create-contact.ts).

### Create Lead

Creates a new lead.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | The name of the lead/company. | Yes |
| `url` | URL | Optional |
| `description` | Description | Optional |
| `contacts` | Array of contact details for this lead | Yes |
| `statusId` | Status Id | See action definition |
| `customFields` | Custom Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/actions/create-lead.ts).

### Create Opportunity

Create a new opportunity.

| Input | What to provide | Required |
| --- | --- | --- |
| `lead_id` | Lead_Id | See action definition |
| `status_id` | Status_Id | See action definition |
| `name` | A descriptive name for the opportunity. | Optional |
| `note` | Additional details about the opportunity. | Optional |
| `confidence` | The probability of winning this opportunity (0-100). | Optional |
| `value` | Monetary value in cents of your organization currency, e.g. 340000 for $3,400.00. | Optional |
| `value_period` | The period for the opportunity value. | Optional |
| `contact_id` | The ID of the contact associated with this opportunity. | Optional |
| `user_id` | User_Id | See action definition |
| `custom_fields` | Custom_Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/actions/create-opportunity.ts).

### Find Contact

Search for contacts by name, email, or other criteria with advanced filtering

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Search Type | Yes |
| `search_query` | Search Query | Yes |
| `match_type` | Match Type | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/actions/find-contact.ts).

### Find Lead

Search for leads with advanced filtering options

| Input | What to provide | Required |
| --- | --- | --- |
| `search_type` | Search Type | Yes |
| `search_query` | Search Query | Yes |
| `match_type` | Match Type | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/actions/find-lead.ts).

## Events and recurring work

- **[New Contact Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/triggers/new-contact-added.ts)** — Triggers when a new contact is created.
- **[New Lead Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/close/src/lib/triggers/new-lead-added.ts)** — Triggers when a new lead is created.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Close to find contact. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
