---
name: google-search-console-connector
description: "Monitor your site's Google Search traffic, sitemaps and index status."
---

# Google Search Console for Muse

Monitor your site's Google Search traffic, sitemaps and index status.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Search Console**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

Provider scopes: `email`, `https://www.googleapis.com/auth/webmasters`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/index.ts).

## Actions

### Add a Site

Adds a site to the set of the user's sites in Search Console.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | A URL-prefix property such as "https://www.example.com/" (a missing trailing slash is added) or a domain property such as "sc-domain:example.com". | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/add-a-site.ts).

### Delete a Site

Removes a site from the set of the user's Search Console sites.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/delete-a-site.ts).

### Delete a Sitemap

Removes a sitemap from the Sitemaps report of a site.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |
| `feedpath` | Feedpath | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/delete-a-sitemap.ts).

### List Sitemaps

List all your sitemaps for a given site

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |
| `sitemapIndex` | Optional. The full URL of a sitemap index to list only the sitemaps inside it. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/list-sitemaps.ts).

### List Sites

Lists the user's Search Console sites.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/list-sites.ts).

### Search Analytics

Query traffic data for your site using the Google Search Console API.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |
| `startDate` | First day of the range (YYYY-MM-DD), in Pacific Time. Search Console data lags 2-3 days and is kept for about 16 months. | Yes |
| `endDate` | Last day of the range (YYYY-MM-DD, inclusive), in Pacific Time. A range that covers only today or yesterday usually has no data yet. | Yes |
| `dimensions` | The dimensions to group results by, in order. Valid values: "query", "page", "country", "device", "searchAppearance", "date", "hour". Each row of the output gets one column per dimension. | Optional |
| `searchType` | Search Type | See action definition |
| `filters` | Filters | See action definition |
| `aggregationType` | Aggregation Type | See action definition |
| `dataState` | Data State | See action definition |
| `rowLimit` | The maximum number of rows to return, from 1 to 25,000. Defaults to 1,000. | Optional |
| `startRow` | Zero-based index of the first row to return. Use with Row Limit to page through results. Defaults to 0. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/search-analytics.ts).

### Submit a Sitemap

Submits a sitemap for a site.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |
| `feedpath` | The full URL of the sitemap, e.g. "https://www.example.com/sitemap.xml". | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/submit-a-sitemap.ts).

### URL Inspection

Use the URL Inspection action to check the status and presence of a specific page within Google's index.

| Input | What to provide | Required |
| --- | --- | --- |
| `siteUrl` | Site Url | See action definition |
| `url` | The full URL of the page. It must belong to the selected property. | Yes |
| `languageCode` | Optional language for the issue messages, as a BCP-47 code such as "en-US" or "de". Defaults to English. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-search-console/src/lib/actions/url-inspection.ts).

## Try it

> Use Google Search Console to list sitemaps. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
