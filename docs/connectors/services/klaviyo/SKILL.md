---
name: klaviyo-connector
description: "Klaviyo: add profile to list, create list, create profile."
---

# Klaviyo for Muse

Klaviyo: add profile to list, create list, create profile.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Klaviyo**.
2. Configure **API key or access token; OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://www.klaviyo.com/oauth/authorize>
- Token endpoint: <https://a.klaviyo.com/oauth/token>

Provider scopes: `accounts:read`, `events:read`, `events:write`, `lists:read`, `lists:write`, `profiles:read`, `profiles:write`, `segments:read`, `subscriptions:read`, `subscriptions:write`, `tags:read`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/index.ts).

## Actions

### Add Profile to List

Add profiles to a specific list without changing subscription status.

| Input | What to provide | Required |
| --- | --- | --- |
| `list_id` | List_Id | See action definition |
| `profile_id` | Profile_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/add-profile-to-list.ts).

### Create List

Create a new subscriber list.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | Name for the new list | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/create-list.ts).

### Create Profile

Add new user profile with email/SMS subscription options

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | Email address (recommended identifier) | Optional |
| `phone_number` | Phone number in E.164 format (e.g., +15005550006) | Optional |
| `external_id` | Unique identifier from external system | Optional |
| `first_name` | First Name | Optional |
| `last_name` | Last Name | Optional |
| `organization` | Company name | Optional |
| `locale` | Language tag (e.g., en-US) | Optional |
| `title` | Job Title | Optional |
| `image` | Profile image URL | Optional |
| `address1` | Street address line 1 | Optional |
| `address2` | Street address line 2 | Optional |
| `city` | City | Optional |
| `country` | Country | Optional |
| `region` | Region/State | Optional |
| `zip` | Zip Code | Optional |
| `timezone` | IANA timezone (e.g., America/New_York) | Optional |
| `ip` | IP Address | Optional |
| `latitude` | Latitude coordinate (4 decimal places recommended) | Optional |
| `longitude` | Longitude coordinate (4 decimal places recommended) | Optional |
| `custom_properties` | Key-value pairs for segmentation and personalization | Optional |
| `include_subscriptions` | Return subscription data in response | Optional |
| `include_predictive_analytics` | Return predictive analytics in response | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/create-profile.ts).

### Find List by Name

Find lists by name with optional additional data

| Input | What to provide | Required |
| --- | --- | --- |
| `search_query` | Enter list name | Yes |
| `include_additional_data` | Include related flow and tag information | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/find-list-by-name.ts).

### Find Profile by Email/Phone

Find a profile using email or phone number.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_query` | Enter an email address or phone number (E.164 format recommended) | Yes |
| `include_additional_data` | Include subscriptions and predictive analytics data | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/find-profile-by-email-phone.ts).

### Find Tag by Name

Find tags whose name contains the search query.

| Input | What to provide | Required |
| --- | --- | --- |
| `search_query` | Search for tags whose name contains this value. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/find-tag-by-name.ts).

### Subscribe Profile

Subscribe profiles to email or SMS marketing on a list.

| Input | What to provide | Required |
| --- | --- | --- |
| `list_id` | List_Id | See action definition |
| `profile_ids` | Profile_Ids | See action definition |
| `subscribe_email` | Subscribe selected profiles to email marketing. | Optional |
| `subscribe_sms` | Subscribe selected profiles to SMS marketing. | Optional |
| `historical_import` | Bypass double opt-in and mark as a historical import. | Optional |
| `consented_at` | ISO 8601 datetime when consent was given (required for historical import, e.g. 2024-01-15T10:00:00Z). | Optional |
| `custom_source` | Label for the subscription source (e.g. "Website Form"). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/subscribe-profile.ts).

### Update Profile

Update existing profile data and preferences.

| Input | What to provide | Required |
| --- | --- | --- |
| `profile_id` | Profile_Id | See action definition |
| `email` | Individual's email address | Optional |
| `phone_number` | Phone number in E.164 format (e.g., +15005550006) | Optional |
| `external_id` | Unique identifier from external system (e.g., POS system) | Optional |
| `anonymous_id` | Anonymous identifier for the profile | Optional |
| `first_name` | Individual's first name | Optional |
| `last_name` | Individual's last name | Optional |
| `organization` | Company or organization name | Optional |
| `locale` | Locale in IETF BCP 47 format (e.g., en-US) | Optional |
| `title` | Individual's job title | Optional |
| `image` | URL pointing to profile image location | Optional |
| `address1` | First line of street address | Optional |
| `address2` | Second line of street address | Optional |
| `city` | City name | Optional |
| `country` | Country | See action definition |
| `region` | Region within country (state/province) | Optional |
| `zip` | Postal/zip code | Optional |
| `timezone` | IANA timezone (e.g., America/New_York) | Optional |
| `ip` | IP address of the profile | Optional |
| `latitude` | Latitude coordinate (4 decimal places recommended) | Optional |
| `longitude` | Longitude coordinate (4 decimal places recommended) | Optional |
| `custom_properties` | Key/value pairs for custom profile properties | Optional |
| `include_subscriptions` | Include subscription data in response | Optional |
| `include_predictive_analytics` | Include predictive analytics data in response | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/actions/update-profile.ts).

## Events and recurring work

- **[New Profile](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/triggers/new-profile.ts)** — Triggers when a new profile is created in Klaviyo.
- **[Profile Added to List/Segment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/klaviyo/src/lib/triggers/profile-added-to-list-segment.ts)** — Triggers when a profile is added to a specific list or segment.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Klaviyo to add profile to list. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect klaviyo
```

Available HTTP reads: `read-api-accounts`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
