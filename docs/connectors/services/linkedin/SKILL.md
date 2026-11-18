---
name: linkedin-connector
description: "Post to LinkedIn profiles and Company Pages"
---

# LinkedIn for Muse

Post to LinkedIn profiles and Company Pages

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **LinkedIn**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://www.linkedin.com/oauth/v2/authorization>
- Token endpoint: <https://www.linkedin.com/oauth/v2/accessToken>

Provider scopes: `email`, `openid`, `profile`, `rw_organization_admin`, `w_member_social`, `w_organization_social`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/index.ts).

## Actions

### Create Company Update

Post on a LinkedIn Company Page you manage

| Input | What to provide | Required |
| --- | --- | --- |
| `company` | Company | See action definition |
| `company_visibility_info` | Company_Visibility_Info | See action definition |
| `text` | Text | See action definition |
| `imageUrl` | Image Url | See action definition |
| `link_preview_info` | Link_Preview_Info | See action definition |
| `link` | Link | See action definition |
| `linkTitle` | Link Title | See action definition |
| `linkDescription` | Link Description | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/create-company-update.ts).

### Create Image Upload URL

Reserve a LinkedIn image URN and a URL to upload the bytes to

| Input | What to provide | Required |
| --- | --- | --- |
| `owner_urn` | Who will own the image. Defaults to the connected member. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/create-image-upload-url.ts).

### Create Member Post

Publish a post on the connected LinkedIn member's personal profile

| Input | What to provide | Required |
| --- | --- | --- |
| `text` | Body of the post. | Yes |
| `visibility` | Who can see the post. | Yes |
| `link` | Optional URL to attach as an article preview. | Optional |
| `link_title` | Link Title | Optional |
| `link_description` | Link Description | Optional |
| `image` | Image | See action definition |
| `image_urn` | URN of an image already uploaded to LinkedIn, for example urn:li:image:D4E10AQ.... Obtain it from Create Image Upload URL and PUT the bytes to that upload URL before posting. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/create-member-post.ts).

### Create Share Update

Post on your personal LinkedIn profile

| Input | What to provide | Required |
| --- | --- | --- |
| `text` | Text | See action definition |
| `visibility` | Visibility | See action definition |
| `imageUrl` | Image Url | See action definition |
| `link_preview_info` | Link_Preview_Info | See action definition |
| `link` | Link | See action definition |
| `linkTitle` | Link Title | See action definition |
| `linkDescription` | Link Description | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/create-share-update.ts).

### Delete Post

Permanently delete a LinkedIn post by its URN

| Input | What to provide | Required |
| --- | --- | --- |
| `post_urn` | URN of the post to delete, for example urn:li:share:7212345678901234567. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/delete-post.ts).

### Get Current Member Profile

Get the profile of the LinkedIn member who owns the connection

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/get-current-member-profile.ts).

### List Managed Organizations

List the LinkedIn organization pages the connected member administers

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/list-managed-organizations.ts).

### Update Post Commentary

Edit the commentary, call-to-action label or landing page of an existing LinkedIn post

| Input | What to provide | Required |
| --- | --- | --- |
| `post_urn` | URN of the post to edit, for example urn:li:share:7212345678901234567. | Yes |
| `commentary` | New body text. Leave empty to keep the current text. | Optional |
| `content_call_to_action_label` | New call-to-action button label. Leave empty to keep the current one. | Optional |
| `content_landing_page` | New destination for the call-to-action button. Leave empty to keep the current one. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/linkedin/src/lib/actions/update-post-commentary.ts).

## Try it

> Use LinkedIn to get current member profile. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect linkedin
```

Available HTTP reads: `read-v2-userinfo`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
