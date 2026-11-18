---
name: quickbooks-connector
description: "Quickbooks Online: create bill, create vendor, find account."
---

# Quickbooks Online for Muse

Quickbooks Online: create bill, create vendor, find account.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Quickbooks Online**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://appcenter.intuit.com/connect/oauth2>
- Token endpoint: <https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer>
- **Company ID** (`companyId`): ShortText

Provider scopes: `com.intuit.quickbooks.accounting`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/index.ts).

## Actions

### Create Bill

Creates a bill (accounts payable) in QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `vendorRef` | Vendor | Yes |
| `lineItems` | Details of the bill (expense categories). At least one line is required. | Yes |
| `txnDate` | The date of the bill. Defaults to today if empty. | Optional |
| `dueDate` | The date the payment is due. If empty, the vendor/company term is used. | Optional |
| `docNumber` | Reference number for the bill. | Optional |
| `privateNote` | Internal note about the bill. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/create-bill.ts).

### Create Vendor

Creates a vendor in QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `displayName` | The name QuickBooks will show for this vendor. Must be unique across all vendors, customers, and employees. | Yes |
| `companyName` | Company Name | Optional |
| `email` | Email Address | Optional |
| `phone` | Phone Number | Optional |
| `billAddrLine1` | Billing Address Line 1 | Optional |
| `billAddrCity` | Billing Address City | Optional |
| `billAddrState` | State or province code, e.g. CA. | Optional |
| `billAddrPostalCode` | Billing Address Postal Code | Optional |
| `vendor1099` | Whether this vendor should be tracked for 1099 reporting. | Optional |
| `taxIdentifier` | Tax ID (SSN or EIN) | Optional |
| `acctNum` | Your own reference/account number for this vendor (external ID). Shown on checks. | Optional |
| `termRef` | Optional. The default payment term for bills from this vendor. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/create-vendor.ts).

### Find Account

List or search the chart of accounts to get an account Id (e.g. an expense account for a bill).

| Input | What to provide | Required |
| --- | --- | --- |
| `search_term` | Optional. Filter accounts whose name contains this text. | Optional |
| `accountType` | Optional. Filter by account type. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/find-account.ts).

### Find Customer

Search for a customer by display name in QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_term` | The display name of the customer to search for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/find-customer.ts).

### Find Invoice

Search for an invoice by its number in QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `invoice_number` | The document number (DocNumber) of the invoice to search for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/find-invoice.ts).

### Find Payment

Finds an existing payment in QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `customerId` | The ID of the customer to find payments for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/find-payment.ts).

### Find Vendor

Search for a vendor in QuickBooks by display name, email address, or account number.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchBy` | Search By | Optional |
| `search_term` | The exact vendor display name, email address, or account number to search for, depending on Search By. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/find-vendor.ts).

### Read AR/AP Aging

Reads an accounts receivable or accounts payable aging report from QuickBooks.

| Input | What to provide | Required |
| --- | --- | --- |
| `reportType` | Report | Yes |
| `reportDate` | The date to age balances against. Defaults to today if empty. | Optional |
| `agingPeriod` | Number of days in each aging bucket (e.g. 30). | Optional |
| `numPeriods` | How many aging buckets to include. | Optional |
| `agingMethod` | Whether buckets are calculated from the report date or from each transaction's due date. | Optional |
| `pastDue` | Only include transactions overdue by at least this many days. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/actions/read-aging-report.ts).

## Events and recurring work

- **[New Bill](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/triggers/new-bill.ts)** — Triggers when a new bill (accounts payable) is created in QuickBooks.
- **[New Customer](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/triggers/new-customer.ts)** — Triggers when a new customer is created.
- **[New Deposit](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/quickbooks/src/triggers/new-deposit.ts)** — Triggers when a Deposit is created.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Quickbooks Online to find account. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
