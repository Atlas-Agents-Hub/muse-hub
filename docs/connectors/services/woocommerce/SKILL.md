---
name: woocommerce-connector
description: "E-commerce platform built on WordPress"
---

# WooCommerce for Muse

E-commerce platform built on WordPress

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **WooCommerce**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Base URL** (`baseUrl`): Your store's address. It must start with https://.
- **Consumer Key** (`consumerKey`): Starts with ck_. Created under Settings > Advanced > REST API.
- **Consumer Secret** (`consumerSecret`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/index.ts).

## Actions

### Create Order

Create an order with one or more line items

| Input | What to provide | Required |
| --- | --- | --- |
| `line_items` | Products to include in the order | Yes |
| `customer_id` | Leave empty for a guest order | Optional |
| `status` | Status the order starts with. | Optional |
| `billing_email` | Where WooCommerce sends the order emails. | Optional |
| `payment_method` | Gateway ID, e.g. bacs, cheque or cod. | Optional |
| `payment_method_title` | Name the customer sees, e.g. Direct bank transfer. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/create-order.ts).

### Find Coupon

Get a coupon by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Find it in WooCommerce under Marketing > Coupons. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/find-coupon.ts).

### Find Customer

Find a customer by their email address

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The exact email address the customer signed up with. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/find-customer.ts).

### Find Orders

Search orders by status, customer or creation date

| Input | What to provide | Required |
| --- | --- | --- |
| `status` | Only return orders with this status | Optional |
| `customer` | Only orders from this customer. | Optional |
| `after` | Only return orders created after this date | Optional |
| `per_page` | How many orders to return, from 1 to 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/find-orders.ts).

### Find Product

Get a product by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Find it in WooCommerce under Products, next to each product. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/find-product.ts).

### Get Customer

Retrieve a single customer by their ID

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Find it in WooCommerce under Customers, or from Find Customer. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/get-customer.ts).

### Get Order

Retrieve a single order by its ID

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | The number after # in WooCommerce > Orders. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/get-order.ts).

### Update Order

Update an order, most commonly its status

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | The number after # in WooCommerce > Orders. | Yes |
| `changes_info` | Changes_Info | Optional |
| `status` | New status for the order. | Optional |
| `customer_note` | The note the customer left at checkout. | Optional |
| `transaction_id` | Payment reference from your payment gateway. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/woocommerce/src/lib/actions/update-order.ts).

## Try it

> Use WooCommerce to find coupon. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
