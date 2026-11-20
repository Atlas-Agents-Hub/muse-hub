---
name: bigcommerce-connector
description: "BigCommerce is a leading e-commerce platform that enables businesses to create and manage online stores."
---

# BigCommerce for Muse

BigCommerce is a leading e-commerce platform that enables businesses to create and manage online stores.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **BigCommerce**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Instruction** (`instruction`): MarkDown
- **Store Hash** (`storeHash`): Your BigCommerce store hash (e.g., abcd1234)
- **Access Token** (`accessToken`): Your BigCommerce API access token

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/index.ts).

## Actions

### Find or Create Customer

Finds or creates a customer

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Customer email address | Yes |
| `first_name` | Customer first name | Yes |
| `last_name` | Customer last name | Yes |
| `company` | Customer company name | Optional |
| `phone` | Customer phone number | Optional |
| `notes` | Customer notes | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/find-or-create-customer.ts).

### Find or Create Product

Finds or creates a product

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Product Name | Yes |
| `sku` | SKU | Optional |
| `type` | Product Type | Yes |
| `weight` | Weight | Yes |
| `price` | Price | Yes |
| `description` | Description | Optional |
| `brand_id` | Brand ID | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/find-or-create-product.ts).

### Get Order

Gets details of an order

| Input | What to provide | Required |
| --- | --- | --- |
| `orderId` | The ID of the order to retrieve | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/get-order.ts).

### List Categories

Lists all categories

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Filter by category name | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/list-categories.ts).

### List Orders

Lists all orders

| Input | What to provide | Required |
| --- | --- | --- |
| `customer_id` | Filter by customer ID | Optional |
| `status_id` | Filter by status ID | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/list-orders.ts).

### Search Customer

Searches for a registered customer

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Customer email to search for | Optional |
| `phone` | Phone Number to search for | Optional |
| `name` | Customer name to search for | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/search-customer.ts).

### Search Customer Address

Searches for a customer’s address

| Input | What to provide | Required |
| --- | --- | --- |
| `customer_ids` | Customer_Ids | See action definition |
| `name` | Customer name to search for | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/search-customer-address.ts).

### Search Product

Searches for a product in the catalog

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Product name to search for | Optional |
| `sku` | Product SKU to search for | Optional |
| `type` | Product Type | Optional |
| `brand_id` | Brand ID to search for | Optional |
| `weight` | Weight | Optional |
| `price` | Price | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/actions/search-product.ts).

## Events and recurring work

- **[Abandoned Cart](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/triggers/abandoned-cart.ts)** — Triggers when a cart is abandoned
- **[Cart Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/triggers/cart-created.ts)** — Triggers when a new cart is created
- **[Customer Address Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/bigcommerce/src/lib/triggers/customer-address-created.ts)** — Triggers when a new customer address is created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use BigCommerce to find or create customer. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
