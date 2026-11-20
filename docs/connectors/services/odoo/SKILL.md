---
name: odoo-connector
description: "Open source all-in-one management software"
---

# Odoo for Muse

Open source all-in-one management software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Odoo**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Odoo URL** (`base_url`): The address of your Odoo without a port, for example https://mycompany.odoo.com. Put a port in the Port field.
- **Odoo Database** (`database`): The database name, for example mycompany
- **Odoo Username** (`username`): The login of the Odoo user, usually an email address
- **Api_Key** (`api_key`): ProviderField
- **Port (optional)** (`port`): Leave empty to use port 443 (the default, right for Odoo Online and most HTTPS setups). Set it only when Odoo listens on another port, for example 8069 for a self-hosted Odoo reached directly.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/index.ts).

## Actions

### Custom Search and read records

Records can be listed and filtered

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model name. e.g.: res.partner | Yes |
| `domain` | A domain is a list of criteria, each criterion being a triple of (field_name, operator, value). See https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html#reference-orm-domains for details. | Optional |
| `fields` | Returns the requested fields of the records. When undefined, returns all fields. | Optional |
| `offset` | Offset | Optional |
| `limit` | Limit | Optional |
| `order` | Optional. Field names with asc or desc, separated by commas, for example "create_date desc, id desc". Leave empty for Odoo's default order. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/get-records.ts).

### Find Invoices

List invoices, bills and credit notes, filtered by type, status, customer and dates.

| Input | What to provide | Required |
| --- | --- | --- |
| `move_types` | Leave empty for all four types. | Optional |
| `state` | Status | Optional |
| `payment_states` | Payment Status | Optional |
| `partner_id` | Partner_Id | See action definition |
| `number` | Number or Reference Contains | Optional |
| `invoice_date_from` | Invoice Date From | Optional |
| `invoice_date_to` | Invoice Date To | Optional |
| `due_date_from` | Due Date From | Optional |
| `due_date_to` | Due Date To | Optional |
| `limit` | Default 50, maximum 500. | Optional |
| `offset` | Skip this many invoices (for paging). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/find-invoices.ts).

### Find Leads

Search Odoo CRM leads and opportunities.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Query | See action definition |
| `type` | Omit for both. | Optional |
| `stage_id` | Stage_Id | See action definition |
| `user_id` | User_Id | See action definition |
| `team_id` | Team_Id | See action definition |
| `partner_id` | Partner_Id | See action definition |
| `created_after` | Created_After | See action definition |
| `include_lost` | Also return lost (archived) leads. | Optional |
| `limit` | Limit | See action definition |
| `offset` | Offset | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/atomics/find-leads.ts).

### Find Tasks

Search Odoo project tasks.

| Input | What to provide | Required |
| --- | --- | --- |
| `project_id` | Project_Id | See action definition |
| `user_id` | User_Id | See action definition |
| `stage_id` | Stage_Id | See action definition |
| `partner_id` | Partner_Id | See action definition |
| `query` | Query | See action definition |
| `limit` | Limit | See action definition |
| `offset` | Offset | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/atomics/find-tasks.ts).

### Get contacts

Get contacts on Odoo

| Input | What to provide | Required |
| --- | --- | --- |
| `type` | Select which contact type to get | Yes |
| `name` | Would you like to search any specific name? | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/get-contacts.ts).

### Get Record

Get one record of any Odoo model by picking it from a list.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `record_id` | Record_Id | See action definition |
| `fields` | Optional. Field names to return, for example name, email. Leave empty for all fields except files and images. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/get-record.ts).

### Get Records by ID

Read one or more records of any Odoo model by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `ids` | Ids | See action definition |
| `fields` | Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/atomics/get-records.ts).

### List Users

List internal Odoo users (salespeople, assignees).

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Query | See action definition |
| `limit` | Limit | See action definition |
| `offset` | Offset | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/actions/atomics/list-users.ts).

## Events and recurring work

- **[New Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/triggers/new-contact.ts)** — Triggers when a new contact (person or company) is created in Odoo.
- **[New Lead or Opportunity](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/triggers/new-lead.ts)** — Triggers when a new lead or opportunity is created in Odoo CRM.
- **[New or Updated Record](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/odoo/src/lib/triggers/new-or-updated-record.ts)** — Triggers when a record is created or changed in any Odoo model. Odoo also counts automatic updates (computed fields, scheduled actions) as changes.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Odoo to custom search and read records. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
