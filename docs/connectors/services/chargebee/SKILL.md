---
name: chargebee-connector
description: "Subscription billing and revenue operations platform for managing customers and subscriptions."
---

# Chargebee for Muse

Subscription billing and revenue operations platform for managing customers and subscriptions.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Chargebee**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Site** (`site`): Your Chargebee site subdomain. For acme.chargebee.com, enter acme.
- **Api_Key** (`api_key`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/index.ts).

## Actions

### Cancel Subscription

Cancel a Chargebee subscription immediately, at end of term, or on a specific date.

| Input | What to provide | Required |
| --- | --- | --- |
| `subscription_id` | Subscription ID | Yes |
| `cancel_option` | When to cancel the subscription. Not applicable when the subscription has a contract term — use Contract Term Cancel Option instead. | Optional |
| `cancel_at` | UTC timestamp in seconds for when to cancel. Required when Cancel Option is "Specific Date". | Optional |
| `cancel_reason_code` | Reason code from Settings > Configure Chargebee > Reason Codes > Subscriptions > Subscription Cancellation. Case-sensitive. | Optional |
| `credit_option_for_current_term_charges` | How to handle credits for current term charges when canceling immediately. | Optional |
| `unbilled_charges_option` | How to handle unbilled charges when canceling immediately. | Optional |
| `contract_term_cancel_option` | Required when the subscription has a contract term. Determines when to cancel the subscription and contract term. | Optional |
| `account_receivables_handling` | How to handle past due invoices when canceling immediately. | Optional |
| `refundable_credits_handling` | How to handle refundable credits when canceling immediately. | Optional |
| `invoice_date` | Document date displayed on the invoice PDF. Defaults to the current date. Provide to backdate the invoice. | Optional |
| `decommissioned` | When true, all subscription operations will be disabled except deletion. This is irreversible. | Optional |
| `termination_fee_item_price_id` | The unique ID of the charge item price representing the termination fee. Used only when the subscription has a contract term. | Optional |
| `termination_fee_quantity` | Quantity for the termination fee. Applicable only for quantity-based item prices. | Optional |
| `termination_fee_unit_price` | The termination fee in cents. For quantity-based items, this is the fee per unit. | Optional |
| `termination_fee_service_period_days` | Service period of the termination fee in days, starting from the current date. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/actions/cancel-subscription.ts).

### Create Customer

Create a customer in Chargebee.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Optional custom customer identifier. | Optional |
| `first_name` | First Name | Optional |
| `last_name` | Last Name | Optional |
| `email` | Email | Optional |
| `company` | Company | Optional |
| `phone` | Phone | Optional |
| `locale` | For example: en-US, fr-CA. | Optional |
| `preferred_currency_code` | ISO 4217 currency code (e.g. USD, EUR). Requires Multi-currency pricing to be enabled. | Optional |
| `auto_collection` | Whether invoices should be automatically charged when possible. | Optional |
| `net_term_days` | Number of days within which the customer must pay their invoices. | Optional |
| `allow_direct_debit` | Whether the customer can pay via Direct Debit. | Optional |
| `vat_number` | The VAT/tax registration number for the customer. | Optional |
| `taxability` | Specifies if the customer is liable for tax. | Optional |
| `invoice_notes` | A customer-facing note added to all invoices for this customer. | Optional |
| `meta_data` | Key-value pairs to store extra information on the customer. | Optional |
| `billing_address_first_name` | Billing Address: First Name | Optional |
| `billing_address_last_name` | Billing Address: Last Name | Optional |
| `billing_address_line1` | Billing Address: Line 1 | Optional |
| `billing_address_line2` | Billing Address: Line 2 | Optional |
| `billing_address_city` | Billing Address: City | Optional |
| `billing_address_state` | Billing Address: State | Optional |
| `billing_address_zip` | Billing Address: ZIP / Postal Code | Optional |
| `billing_address_country` | Two-letter ISO 3166-1 alpha-2 country code (e.g. US, GB). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/actions/create-customer.ts).

### Create Subscription

Create a subscription for an existing customer using a Chargebee item price.

| Input | What to provide | Required |
| --- | --- | --- |
| `customer_id` | Customer ID | Yes |
| `item_price_id` | The Chargebee item price ID to subscribe the customer to. | Yes |
| `quantity` | Quantity | Optional |
| `auto_collection` | Whether to automatically charge the customer. Defaults to the customer setting. | Optional |
| `billing_cycles` | Number of billing cycles before the subscription ends. Defaults to the item price setting. | Optional |
| `trial_end` | UTC timestamp in seconds when the trial period ends. Set to 0 for no trial. | Optional |
| `start_date` | UTC timestamp in seconds when the subscription starts. Defaults to now. Provide a past value to backdate. | Optional |
| `coupon_ids` | A coupon ID or code to apply to this subscription. | Optional |
| `po_number` | Purchase order number to associate with this subscription. | Optional |
| `invoice_notes` | Customer-facing note added to all invoices for this subscription. | Optional |
| `payment_source_id` | ID of the payment source to attach to this subscription. | Optional |
| `invoice_immediately` | Invoice any charges raised at creation time immediately rather than adding them to unbilled charges. | Optional |
| `net_term_days` | Number of days within which invoices for this subscription must be paid (Net D). Must match a value configured in Chargebee. | Optional |
| `meta_data` | Key-value pairs to store extra information on the subscription. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/actions/create-subscription.ts).

### Get Customer

Retrieve a customer from Chargebee by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `customer_id` | Customer ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/actions/get-customer.ts).

## Events and recurring work

- **[Customer Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/triggers/customer-created.ts)** — Triggers when a new customer is created in Chargebee.
- **[Invoice Generated](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/triggers/invoice-generated.ts)** — Triggers when a new invoice is generated for a subscription.
- **[Payment Failed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chargebee/src/lib/triggers/payment-failed.ts)** — Triggers when a payment attempt fails. Useful for dunning and retry workflows.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Chargebee to get customer. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
