# Deliver a Service Environment

Create a repeatable environment with deployment and operational checks.

## Bring these inputs

- Service build and environment requirements
- Cloud account scope and operating targets

## 1. Docker Development

Read [the Docker Development method](../skills/docker-development/SKILL.md). Package the service with reproducible build inputs and runtime settings.

**Carry forward:** A service image and container run configuration.

**Check:** The image starts correctly and contains only the required runtime material.

## 2. Terraform Patterns

Read [the Terraform Patterns method](../skills/terraform-patterns/SKILL.md). Describe the required infrastructure and review the proposed changes.

**Carry forward:** An infrastructure plan with state and rollback considerations.

**Check:** Resource permissions, network exposure, and destructive changes are reviewed.

## 3. Observability Designer

Read [the Observability Designer method](../skills/observability-designer/SKILL.md). Add service indicators, dashboards, and actionable alerts.

**Carry forward:** An observable environment with documented incident entry points.

**Check:** A controlled failure is visible and routes to a clear recovery action.

## Check the finished work

- The image starts correctly and contains only the required runtime material.
- Resource permissions, network exposure, and destructive changes are reviewed.
- A controlled failure is visible and routes to a clear recovery action.

## Finish

An observable environment with documented incident entry points. A controlled failure is visible and routes to a clear recovery action.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
