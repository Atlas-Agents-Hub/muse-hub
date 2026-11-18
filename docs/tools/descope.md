# Descope

**Review sign-in and application access rules**

Trace a login flow and its roles, permissions, tenant boundaries, and audit evidence before changing access behavior.

**Works well with:** Software Engineer, Adversarial Verifier, Infrastructure Reliability Engineer.

## What to bring

- Application routes
- Role and tenant matrix
- Expected access decisions

## Setup

1. Connect the intended Descope project and prepare test users for the allowed and denied cases.

**Access:** Descope project plan.

## Supported functions

| Function | Use it to |
| --- | --- |
| `session` | Confirm the account and selected project |
| `list_operations` | Discover the current management operations |
| `flows_read` | Read authentication flow definitions |
| `access_control_read` | Read roles, permissions, and relationship rules |

## Workflow

1. Confirm the project and discover the relevant management operations.
2. Read the flow and access-control definitions needed for the task.
3. Compare the configured rules with an allow-and-deny test matrix.
4. Apply the requested change through the supported project workflow and repeat both positive and negative cases.

## What you get

- Access-control matrix
- Flow or policy update
- Authentication regression results

## Check the result

- Authorized users reach the intended routes.
- Wrong-role and wrong-tenant cases are rejected without exposing protected data.

## Try it

> Use Descope to review sign-in and application access rules. Start from the inputs I provide, follow the setup and workflow, and return access-control matrix, flow or policy update, authentication regression results. Verify: Authorized users reach the intended routes. Wrong-role and wrong-tenant cases are rejected without exposing protected data.

## Combine it with

- **Review access, dependencies, and agent boundaries:** Endor Labs Agent Kit, Prompt Injection Security, Authorised OSINT Toolkit, reverse engineering anything.

## Learn more

- [docs.descope.com](https://docs.descope.com/api/management)
