---
name: rabbitmq-connector
description: "RabbitMQ: send message to exchange, send message to queue, message received."
---

# RabbitMQ for Muse

RabbitMQ: send message to exchange, send message to queue, message received.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **RabbitMQ**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Host** (`host`): Broker host name or IP, without scheme or port (for example rabbitmq.example.com).
- **Username** (`username`): Username
- **Password** (`password`): ProviderField
- **Port** (`port`): AMQP port. Usually 5672, or 5671 with TLS.
- **Virtual Host** (`vhost`): Virtual host name. Leave empty for the default "/".
- **Use TLS (amqps)** (`useTls`): Connect with TLS. Most hosted brokers require this.
- **Management API URL** (`managementUrl`): Optional. Base URL of the RabbitMQ Management plugin (for example http://localhost:15672). Uses the same username and password.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/rabbitmq/src/index.ts).

## Actions

### Send Message to Exchange

Send a message on a RabbitMQ exchange

| Input | What to provide | Required |
| --- | --- | --- |
| `exchange` | The name of the exchange to send the message to | Yes |
| `routingKey` | The routing key to use when sending the message | Optional |
| `data` | The data to send | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/rabbitmq/src/lib/actions/send-message-to-exchange.ts).

### Send Message to Queue

Send a message on a RabbitMQ queue

| Input | What to provide | Required |
| --- | --- | --- |
| `queue` | The name of the queue to send the message to. It must already exist. | Yes |
| `data` | The data to send | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/rabbitmq/src/lib/actions/send-message-to-queue.ts).

## Events and recurring work

- **[Message Received](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/rabbitmq/src/lib/triggers/message-received.ts)** — Triggers when a message is received on a RabbitMQ queue

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use RabbitMQ to send message to exchange. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
