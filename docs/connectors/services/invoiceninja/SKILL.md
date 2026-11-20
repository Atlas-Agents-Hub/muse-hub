---
name: invoiceninja-connector
description: "Free open-source invoicing tool"
---

# Invoice Ninja for Muse

Free open-source invoicing tool

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Invoice Ninja**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Base URL** (`base_url`): https://invoicing.co for the hosted service, or your self-hosted address such as https://invoices.example.com
- **Access_Token** (`access_token`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/index.ts).

## Actions

### Check Task Existence

Returns 1 if a task with this number exists, 0 if not.

| Input | What to provide | Required |
| --- | --- | --- |
| `number` | The task or ticket number to check. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/task-exists.ts).

### Create Client

Creates a new client with a primary contact in Invoice Ninja.

| Input | What to provide | Required |
| --- | --- | --- |
| `client_first_name` | First name of the client contact (optional). | Optional |
| `client_last_name` | Last name of the client contact (optional). | Optional |
| `client_phone` | Phone number of the client contact (optional). | Optional |
| `client_email` | E-mail of the client contact. | Yes |
| `client_send_email` | Should Invoice Ninja e-mail invoices to this contact? | Yes |
| `client_business_name` | Name of the business or person. | Yes |
| `client_tax_no` | Leave blank if not a business (optional). | Optional |
| `client_private_notes` | Notes not visible to the client (optional). | Optional |
| `client_address1` | Usually street name and number. | Yes |
| `client_address2` | Additional address details (optional). | Optional |
| `client_city` | City / Town | Yes |
| `client_state` | Optional. | Optional |
| `client_postcode` | Optional. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/create-client.ts).

### Create Invoice

Creates an invoice from existing products (price and tax are taken from each product).

| Input | What to provide | Required |
| --- | --- | --- |
| `client_id` | Client_Id | See action definition |
| `purchase_order_no` | Purchase_Order_No | See action definition |
| `discount` | Discount | See action definition |
| `discount_type` | Discount_Type | See action definition |
| `public_notes` | Public_Notes | See action definition |
| `private_notes` | Private_Notes | See action definition |
| `order_items_json` | Order_Items_Json | See action definition |
| `send_email` | Send the invoice by Invoice Ninja e-mail when it is created. | Yes |
| `mark_sent` | Makes the invoice active; otherwise it stays a draft. | Yes |
| `due_date` | The date part is used, e.g. 2024-01-20. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/create-invoice.ts).

### Create Task

Creates a billable task in Invoice Ninja.

| Input | What to provide | Required |
| --- | --- | --- |
| `number` | A task or ticket number not used before in Invoice Ninja. | Yes |
| `client_id` | Client_Id | See action definition |
| `project_id` | Project_Id | See action definition |
| `description` | What the task is about. | Yes |
| `rate` | Leave empty to use the default rate. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/create-task.ts).

### Get Client Details from e-mail

Gets the client whose contact has this e-mail. Returns false when there is none.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The e-mail address of one of the client's contacts. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/get-client.ts).

### Get Invoices

Gets invoices by payment status, optionally for one client. Returns false when none match.

| Input | What to provide | Required |
| --- | --- | --- |
| `invoiceStatus` | Select the invoice status for filtering. | Yes |
| `clientID` | Client Id | See action definition |
| `numberOfResults` | Maximum number of invoices to return (1-${MAX_RESULTS}). Default ${MAX_RESULTS}. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/get-invoices.ts).

### Get Report

Runs an Invoice Ninja report and returns its columns and rows.

| Input | What to provide | Required |
| --- | --- | --- |
| `reportType` | Report Type | See action definition |
| `dateRange` | Date Range | See action definition |
| `startDate` | Start Date | See action definition |
| `endDate` | End Date | See action definition |
| `clientID` | Client Id | See action definition |
| `numberOfResults` | Return at most this many rows. Empty = all. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/get-report.ts).

### Perform Action on Recurring Invoice

Start, stop, send now, restore, archive or delete a recurring invoice.

| Input | What to provide | Required |
| --- | --- | --- |
| `recurring_id` | The ID of the recurring invoice in Invoice Ninja. | Yes |
| `actionRecurring` | Choose one. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/invoiceninja/src/lib/actions/action-recurring.ts).

## Try it

> Use Invoice Ninja to get client details from e-mail. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
