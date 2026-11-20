---
name: pushover-connector
description: "Simple push notification service"
---

# Pushover for Muse

Simple push notification service

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Pushover**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api_Token** (`api_token`): ProviderField
- **User_Key** (`user_key`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/index.ts).

## Actions

### Assign License

Spend a prepaid credit to license a Pushover user

| Input | What to provide | Required |
| --- | --- | --- |
| `user` | The 30-character user key to license. Supply either this or Email, not both. | Optional |
| `email` | Pushover account email of the person to license, used when their user key is unknown. Supply either this or User Key, not both. | Optional |
| `os` | Restrict the license to one platform. Any platform may be used when omitted. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/assign-license.ts).

### Get Delivery Group

Read the name and members of one Pushover delivery group

| Input | What to provide | Required |
| --- | --- | --- |
| `group_key` | The 30-character delivery group key. Resolve it with List Delivery Groups; this is not the user key stored on the connection. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/get-delivery-group.ts).

### Get Emergency Receipt Status

Read the acknowledgement status of an emergency notification receipt

| Input | What to provide | Required |
| --- | --- | --- |
| `receipt` | Receipt id returned by Send Push Message at emergency priority, for example rXXXXXXXXXXXXXXXXXXXXXXXXXXXXX. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/get-receipt-status.ts).

### Get License Credits

Read how many prepaid Pushover license credits remain

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/get-license-credits.ts).

### Get Monthly Message Limits

Read the monthly message allowance and remaining quota of the application

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/get-app-limits.ts).

### List Delivery Groups

List the delivery groups owned by the Pushover account

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/list-delivery-groups.ts).

### List Notification Sounds

List the notification sound identifiers Pushover accepts

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/list-notification-sounds.ts).

### Update Glance Widget

Update the Pushover glance widget fields on the user devices

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Short description of the data, maximum 100 characters. Omit to leave unchanged. Values cannot be cleared once set. | Optional |
| `text` | Main line of text, maximum 100 characters. Omit to leave unchanged. Values cannot be cleared once set. | Optional |
| `subtext` | Second line of text, maximum 100 characters. Omit to leave unchanged. Values cannot be cleared once set. | Optional |
| `count` | Integer shown on the widget, may be negative. Omit to leave unchanged. | Optional |
| `percent` | Integer from 0 to 100 rendered as a progress bar. Omit to leave unchanged. | Optional |
| `device` | Update only this device name. All devices are updated when omitted. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushover/src/lib/actions/update-glance.ts).

## Try it

> Use Pushover to get delivery group. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
