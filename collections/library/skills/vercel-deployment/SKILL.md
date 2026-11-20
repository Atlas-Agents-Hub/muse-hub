---
name: vercel-deployment
description: "Expert knowledge for deploying to Vercel with Next.js"
---

# Vercel Deployment

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

Expert knowledge for deploying to Vercel with Next.js

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## Prerequisites

- Verify the project's Next.js version and available local skills; historical upstream names such as `nextjs-app-router` may not be installed.

## When to Use
- User mentions or implies: vercel
- User mentions or implies: deploy
- User mentions or implies: deployment
- User mentions or implies: hosting
- User mentions or implies: production
- User mentions or implies: environment variables
- User mentions or implies: edge function
- User mentions or implies: serverless function

## Example

```text
Prepare a preview deployment for the approved Vercel project/team using staging data. Verify build/runtime settings, environment scopes and rollback; production promotion and DNS changes require explicit destination authorization. Report the actual deployment ID and smoke-check result.
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
