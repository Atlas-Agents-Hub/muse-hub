# Implement and Check Access Control

Define identity and authorization rules and prove them at the application boundary.

## Bring these inputs

- User roles and resource ownership model
- Application routes and identity provider

## 1. Auth

Read [the Auth method](../skills/auth-pro/SKILL.md). Define the authentication flow, session lifecycle, and identity claims.

**Carry forward:** An authentication design with failure and recovery paths.

**Check:** The design covers expiration, revocation, and account recovery.

## 2. Role Based Access Designer

Read [the Role Based Access Designer method](../skills/rbac-designer/SKILL.md). Map roles and ownership to resource operations.

**Carry forward:** An authorization matrix and enforcement points.

**Check:** Every sensitive operation has a clear decision rule and default behavior.

## 3. Secure Code Guardian

Read [the Secure Code Guardian method](../skills/secure-code-guardian/SKILL.md). Exercise the implementation against the authorization matrix.

**Carry forward:** Access-control tests and resolved findings.

**Check:** Cross-account access, escalation, and invalid-session cases are denied.

## Check the finished work

- The design covers expiration, revocation, and account recovery.
- Every sensitive operation has a clear decision rule and default behavior.
- Cross-account access, escalation, and invalid-session cases are denied.

## Finish

Access-control tests and resolved findings. Cross-account access, escalation, and invalid-session cases are denied.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
