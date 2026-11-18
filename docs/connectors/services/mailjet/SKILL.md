---
name: mailjet-connector
description: "Email delivery service for sending transactional and marketing emails"
---

# Mailjet for Muse

Email delivery service for sending transactional and marketing emails

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Mailjet**.
2. Configure **Service username and password or token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **API Key** (`username`): The API Key from Mailjet API Key Management.
- **Secret Key** (`password`): The Secret Key that belongs to the API Key.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailjet/src/index.ts).

## Actions

### Send Email

Send a text, HTML or template email through Mailjet

| Input | What to provide | Required |
| --- | --- | --- |
| `fromEmail` | Sender email, must be verified in Mailjet | Yes |
| `fromName` | From (Name) | Optional |
| `toEmails` | Emails of recipients | Yes |
| `subject` | Subject | Yes |
| `textPart` | Text part | Optional |
| `htmlPart` | HTML part | Optional |
| `templateId` | Template Id (number) defined in Mailjet | Optional |
| `templateVariables` | Template variables | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailjet/src/lib/actions/send-email.ts).

## Try it

> Use Mailjet to send email. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
