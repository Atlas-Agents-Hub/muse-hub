# Website maintenance

The published website is in maintenance mode. Preserve the visual contract, responsive layouts, navigation, English resource descriptions, search and discovery, and published package identities. Plugin, MCP, concierge, personal installer and specialist-installation development are independently governed and are not part of website maintenance.

## Change policy

- **Maintenance:** repair demonstrated defects, broken links, inaccurate descriptions, security or accessibility regressions, and add verified resources or documentation for released functionality.
- **Active development:** major redesigns, new product features, navigation or architecture changes, mass editorial changes, infrastructure changes, and package distribution changes require explicit owner authorization.
- **Incident response:** investigate verified production failures, security exposures or provenance discrepancies. Apply the smallest correction through normal branch protection, relevant tests and a reviewed PR. Preserve evidence and establish a rollback path. Do not automatically merge, deploy, rewrite content, delete branches or publish packages.

Keep main as the canonical source and compare production to its actual deployment commit; a newer source commit is not itself evidence of a deployment. The publishing workflow remains a separate, manual operation. Retain release tags, package assets and protected development work. Never discard unique material or another contributor's changes.

## Checks and alert handling

| Cadence (UTC) | Automated checks | Manual checks and limits |
| --- | --- | --- |
| Daily | 13:17: successful Pages deployment and publishing run, exact deployed website bytes, homepage and two critical download destinations | Review failures and actionable security notices; investigate transient network/deployment states before declaring an outage. |
| Weekly | Monday 13:47: daily checks plus release manifest/checksum/asset metadata, package compatibility, generated pages and sitewide structural tests | Sample external resource links and security advisories. Asset metadata is not a fresh download of every archive. |
| Monthly | First day 14:17: daily checks plus desktop/mobile browser journeys against deployed source | Review captures on actual devices when available, accessibility and performance, resource accuracy, SEO/indexing and dependency health. Browser emulation is not native Safari/VoiceOver evidence. |
| Quarterly | None: preservation archives are outside the public repository | Verify private archive recoverability, canonical checkout and branch ownership, recovery readiness, deprecated resources and operational cost. |

The [read-only maintenance workflow](../.github/workflows/website-maintenance.yml) can also be dispatched manually to run all automated checks. It has read-only permissions and no deployment, release or repository mutation steps. Failure is visible in GitHub Actions. Owners should verify their existing Actions failure-notification preferences; no new external notification integration is required. Successful runs do not create issues.

Classify failures as P0 (outage, confirmed critical security or package integrity incident), P1 (critical functionality or actionable high-risk exposure), P2 (noncritical accessibility, SEO, link or content defects), or P3 (optional polish; defer unless justified). Record the affected URL or release identity, evidence, impact, and bounded remediation. Repeated symptoms belong to the same incident.

A project-specific robots.txt is not part of the accepted site; robots directives are origin-scoped. Inspect the origin's behavior manually if indexing changes. Verify sitemap, canonical URLs and llms.txt through the deployed byte check, generated-page checks and periodic editorial review. Security-alert availability is a repository-wide setting; if unavailable, review advisories manually and request owner authorization before changing shared settings. Do not treat an unavailable security feed as a passing scan.

## Release and recovery

Run existing public-source checks, relevant browser tests and package-scope verification for maintenance PRs. Keep maintenance-only changes separate from package code. For a website incident, verify the last known-good source tree and package identity before restoring an authorized deployment. Do not roll back by rewriting main or release tags. Keep private work logs, machine paths, archive contents and credentials out of this repository.
