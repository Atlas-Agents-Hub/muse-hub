---
name: rbac-designer
description: "Design role-based access control — role engineering, permission modeling, hierarchies, and governance."
---

# Role Based Access Designer

## Working setup

Use the files, project settings, and connected tools available for this task. Read the relevant reference before changing an unfamiliar API or format. Run included commands from this skill folder, using the project's actual inputs.

## When to use

- Designing authorization for a new application or platform.
- Cleaning up accumulated direct grants and ad-hoc permissions.
- Reducing role explosion in an existing RBAC deployment.
- Preparing for audits that require demonstrable least privilege.

## Core concepts

- **The model:** users → roles → permissions → resources. Sessions activate subsets of roles. Keep the chain clean: no user→permission shortcuts in a mature model.
- **Role engineering approaches:** top-down (from job functions/org structure — fast but often wrong) vs bottom-up/role mining (from actual access patterns — accurate but messy). Best practice blends both: mine usage, then rationalize against job functions.
- **Least privilege per role:** each role holds the minimum permissions its members need. "Standard employee" roles should not include admin rights "just in case."
- **Hierarchies with care:** senior roles inheriting junior permissions reduces duplication — but deep hierarchies become incomprehensible. Two to three levels is usually the sweet spot.
- **Constraints:** static separation of duties (conflicting roles never assigned together) and dynamic (not activated in the same session). Enforce in the system, not in policy documents.
- **Role lifecycle:** roles are born (with justification), reviewed (still needed? still correct?), and retired. Roles without lifecycle become permanent privilege.

- **Attribute-based extensions.** When roles alone cannot express policy (project membership, data classification, location), ABAC attributes complement RBAC — but add ABAC only where RBAC demonstrably cannot cope, as complexity compounds.
- **Temporal constraints.** Time-bound role activations (contractor access, incident response) with automatic expiry prevent the most common privilege-accumulation vector.
- **Role mining cadence.** Re-mine usage patterns annually — organizations reorganize, and roles that matched last year's structure drift into irrelevance.

## Practical workflow

1. **Inventory current state:** dump all direct grants and existing roles; identify the worst offenders (over-broad roles, single-user roles, direct grants to sensitive resources).
2. **Mine candidate roles:** cluster users by actual permission usage; propose roles that cover 80%+ of members' needs with minimal excess. Validate against job functions with managers.
3. **Design the role catalog:** named, documented roles with clear purpose, membership criteria, and permission lists. Keep the catalog small enough to review — dozens, not thousands.
4. **Build hierarchies and constraints:** inheritance where it genuinely reduces duplication; SoD constraints for conflicting duties (finance, procurement, admin).
5. **Migrate:** map users to new roles, remove direct grants in phases, and verify no one loses needed access (pilot with one department first).
6. **Govern:** quarterly role reviews (membership still correct? permissions still minimal?), role-owner accountability, and a request workflow for new roles that requires justification — the gate that prevents re-explosion.

### Role definition template

- **Role name:** (clear, e.g., "Finance Analyst — EMEA")
- **Purpose:** what job function this serves
- **Membership criteria:** who qualifies (department, job code)
- **Permissions:** explicit list, with resources
- **Owner:** accountable person for reviews
- **Review date:** next scheduled review
- **SoD conflicts:** roles that cannot be combined with this one

### Sustaining the practice

- Review the role catalog annually for consolidation opportunities
- Track direct-grant percentage as the headline hygiene metric
- Audit role membership changes for anomalies (bulk grants, off-hours changes)
- Keep role documentation where requesters actually look — in the access request flow

### Metrics that prove it works

- Role count trend (should stabilize, not grow unboundedly)
- % of access granted via roles vs direct grants
- Role-review completion rate and permissions removed per review
- SoD violation count (target: zero unremediated)

## Common pitfalls

- **Role explosion.** Creating a role per user or per tiny permission set. If roles ≈ users, you have direct assignment with overhead.
- **Top-down-only design.** Org-chart roles rarely match actual access needs; validate with usage data or the model will be bypassed.
- **Permissions creep in roles.** Roles only grow unless reviews actively shrink them. Review with last-used data.
- **Skipping SoD.** Discovering toxic combinations after the fact. Build constraints into the model from day one.
- **No role owners.** Roles without accountable owners never get reviewed. Name an owner for every role.
- **Migrating without a pilot.** Big-bang RBAC migrations break access and get rolled back. Phase it, verify each wave.
- **Nesting roles into spaghetti.** Deep role-in-role hierarchies become unauditable. Keep nesting shallow and document the inheritance chain.
- **Emergency access via permanent role assignment.** Break-glass needs time-boxed elevation with automatic expiry, not a permanent role grant "for now."
- **Creating roles for organizational politics.** 'Executive super-user' roles that bypass the model teach everyone the model is optional. No exceptions to least privilege by title.
- **Forgetting the deprovisioning side.** Roles make granting easy; ensure removal is equally automated when people change roles or leave.
