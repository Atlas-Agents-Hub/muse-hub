---
name: workable-connector
description: "Workable: get candidate, get job, get members."
---

# Workable for Muse

Workable: get candidate, get job, get members.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Workable**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/index.ts).

## Actions

### Get Candidate

Gets a candidate's full profile.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `id` | Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/get-candidate.ts).

### Get Job

Gets the details of a job.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `shortcode` | Shortcode of the job, for example "GROOV005". Find it with List Jobs. | Yes |
| `include_description` | Also return the description, requirements and benefits. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/get-job.ts).

### Get Members

Lists members of the hiring team, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `role` | Role | Optional |
| `shortcode` | Only members of this job. | Optional |
| `email` | Only the member with this email. | Optional |
| `name` | Only members with this exact name. | Optional |
| `limit` | Members per page, 1 to 100. Default 50. | Optional |
| `cursor` | nextCursor from a previous run, to get the next page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/get-members.ts).

### Get Stages

Lists the pipeline stages of a job, or of the account when no job is given.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `shortcode` | Shortcode of the job. Empty lists the account-wide stages. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/get-stages.ts).

### List Accounts

Lists the Workable accounts this token can use, with their subdomains.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/list-accounts.ts).

### List Candidates

Finds candidates by email, job, stage or date, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `email` | Only candidates with this email. | Optional |
| `shortcode` | Only candidates of this job. | Optional |
| `stage` | Only candidates in this stage. Needs Job Shortcode. | Optional |
| `created_after` | Created After | Optional |
| `updated_after` | Updated After | Optional |
| `limit` | Candidates per page, 1 to 100. Default 50. | Optional |
| `cursor` | nextCursor from a previous run, to get the next page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/list-candidates.ts).

### List Jobs

Lists jobs, optionally by state or date, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `state` | State | Optional |
| `created_after` | Created After | Optional |
| `updated_after` | Updated After | Optional |
| `limit` | Jobs per page, 1 to 100. Default 50. | Optional |
| `cursor` | nextCursor from a previous run, to get the next page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/list-jobs.ts).

### List Recruiters

Lists external recruiters of the account or of one job.

| Input | What to provide | Required |
| --- | --- | --- |
| `account_subdomain` | Account_Subdomain | See action definition |
| `shortcode` | Only recruiters of this job. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/actions/list-recruiters.ts).

## Events and recurring work

- **[Candidate Stage Changed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/triggers/candidate-stage-changed.ts)** — Triggers when a candidate is moved to another stage. Can be filtered by job and target stage.
- **[New Candidate](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/workable/src/lib/triggers/new-candidate.ts)** — Triggers when a new candidate is added. Can be filtered by job and pipeline stage.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Workable to get candidate. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect workable
```

Available HTTP reads: `read-spi-v3-accounts`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
