---
name: xero-connector
description: "Beautiful accounting software"
---

# Xero for Muse

Beautiful accounting software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Xero**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://login.xero.com/identity/connect/authorize>
- Token endpoint: <https://identity.xero.com/connect/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/index.ts).

## Actions

### Find Contact

Finds a contact by name or account number (or SearchTerm).

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `search_by` | Search By | Yes |
| `value` | Name, Account Number, or Search Term depending on Search By. | Yes |
| `include_archived` | Include Archived | Optional |
| `summary_only` | Recommended for broad searches (Search Term). Excludes heavy fields. | Optional |
| `page` | Pagination page (optional). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/find-contact.ts).

### Find Invoice

Finds an invoice by number or reference.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `search_by` | Search By | Yes |
| `value` | Invoice Number, Reference, or Search Term. | Yes |
| `type_filter` | Type Filter | Optional |
| `summary_only` | Summary Only (faster, lighter) | Optional |
| `page` | Page | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/find-invoice.ts).

### Find Item

Finds an item by name or code.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `search_by` | Search By | Yes |
| `value` | Item Code or Name (exact match). | Yes |
| `order` | e.g. Name or Name DESC | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/find-item.ts).

### Get Contact

Gets one contact by ID, with addresses and phone numbers.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `contact_id` | The Xero ContactID (a GUID). Use Find Contact to get it. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/get-contact.ts).

### Get Invoice

Gets one invoice or bill by its ID or invoice number, including line items.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `invoice_id` | The Xero InvoiceID (a GUID) or the invoice number, for example INV-0042. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/get-invoice.ts).

### List Accounts

Lists the chart of accounts, optionally filtered by type, class or status.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `type` | Type | Optional |
| `account_class` | Class | Optional |
| `status` | Status | Optional |
| `payments_enabled_only` | Keep only bank accounts and accounts with "Enable payments to this account" on. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/list-accounts.ts).

### List Tax Rates

Lists the tax rates of the organisation and the TaxType codes to use on line items.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `tax_type` | Only the rate with this TaxType code, e.g. OUTPUT. | Optional |
| `active_only` | Active Only | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/list-tax-rates.ts).

### Search Invoices

Searches sales invoices and bills by type, status, contact, date range or text, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `tenant_id` | Tenant_Id | See action definition |
| `type` | Leave empty to include both sales invoices and bills. | Optional |
| `statuses` | Statuses | Optional |
| `contact_id` | Only invoices for this Xero ContactID. Use Find Contact to get it. | Optional |
| `date_from` | Invoice Date From (YYYY-MM-DD) | Optional |
| `date_to` | Invoice Date To (YYYY-MM-DD) | Optional |
| `search_term` | Matches invoice number and reference (case-insensitive, partial). | Optional |
| `summary_only` | Leave on for faster results without line items; use Get Invoice for the full invoice. | Optional |
| `page` | Page number, starting at 1. | Optional |
| `page_size` | Invoices per page, 1 to 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/actions/search-invoices.ts).

## Events and recurring work

- **[New Bank Transaction](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/triggers/new-bank-transaction.ts)** — Fires the first time a bank transaction is created or changed after the trigger is turned on.
- **[New Bill](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/triggers/new-bill.ts)** — Fires the first time a bill (Accounts Payable) is created or changed after the trigger is turned on.
- **[New Contact](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/xero/src/lib/triggers/new-contact.ts)** — Fires when a new contact is added to Xero (via Xero webhooks). Configure the webhook in Xero Developer portal to point to this URL.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Xero to find contact. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
