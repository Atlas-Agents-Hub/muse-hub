# Build an API Service

Deliver an API with explicit schemas, access checks, and behavioral tests.

## Bring these inputs

- API use cases and data model
- Authentication and operational requirements

## 1. FastAPI

Read [the FastAPI method](../skills/fastapi-expert/SKILL.md). Implement routes, schemas, validation, and error responses for the use cases.

**Carry forward:** A runnable API and its documented request/response contract.

**Check:** Valid and invalid requests produce the documented behavior.

## 2. Secure Code Guardian

Read [the Secure Code Guardian method](../skills/secure-code-guardian/SKILL.md). Review trust boundaries, authentication, authorization, and sensitive data handling.

**Carry forward:** Security corrections tied to concrete failure cases.

**Check:** Unauthorized access and unsafe input cases are rejected.

## 3. API Test Suite Builder

Read [the API Test Suite Builder method](../skills/api-test-suite-builder/SKILL.md). Exercise the contract and corrected failure cases through integration tests.

**Carry forward:** A repeatable API test suite and results.

**Check:** Tests cover success, invalid input, access control, and dependency failure.

## Check the finished work

- Valid and invalid requests produce the documented behavior.
- Unauthorized access and unsafe input cases are rejected.
- Tests cover success, invalid input, access control, and dependency failure.

## Finish

A repeatable API test suite and results. Tests cover success, invalid input, access control, and dependency failure.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
