---
name: chatwoot-connector
description: "Receive and reply to customer messages with Chatwoot"
---

# Chatwoot for Muse

Receive and reply to customer messages with Chatwoot

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Chatwoot**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Chatwoot URL** (`baseUrl`): Your Chatwoot instance URL (e.g. https://app.chatwoot.com)
- **Api Access Token** (`apiAccessToken`): ProviderField
- **Account ID** (`accountId`): Your numeric account ID (visible in the dashboard URL)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chatwoot/src/index.ts).

## Actions

### Send Message

Send a message reply to a Chatwoot conversation

| Input | What to provide | Required |
| --- | --- | --- |
| `conversationId` | The numeric conversation display ID. Available from the trigger output. | Yes |
| `message` | The text message to send | Yes |
| `isPrivate` | If checked, sends as a private note visible only to agents (not the contact) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chatwoot/src/lib/actions/send-message.ts).

## Events and recurring work

- **[New Incoming Message](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/chatwoot/src/lib/triggers/new-message.ts)** — Triggers when a contact sends a new message in a Chatwoot conversation

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Chatwoot to send message. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
