---
name: content-creator
description: "Use when someone asks for 'content creator' by name. Deprecated alias: hands writing to content-production and planning to content-strategy."
---

# Content Creator

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

> **This skill has been split into two specialist skills.** Use the one that matches your intent:

| You want to... | Use this instead |
|----------------|-----------------|
| **Write** a blog post, article, or guide | [content-production](https://github.com/alirezarezvani/claude-skills/tree/f8593c4941210a621a6629ce1da9e07897976d5f/marketing-skill/skills/content-production) |
| **Plan** what content to create, topic clusters, calendar | [content-strategy](https://github.com/alirezarezvani/claude-skills/tree/f8593c4941210a621a6629ce1da9e07897976d5f/marketing-skill/skills/content-strategy) |
| **Analyze brand voice** | [content-production](https://github.com/alirezarezvani/claude-skills/tree/f8593c4941210a621a6629ce1da9e07897976d5f/marketing-skill/skills/content-production) (includes `brand_voice_analyzer.py`) |
| **Optimize SEO** for existing content | [content-production](https://github.com/alirezarezvani/claude-skills/tree/f8593c4941210a621a6629ce1da9e07897976d5f/marketing-skill/skills/content-production) (includes `seo_optimizer.py`) |
| **Create social media content** | [social-content](https://github.com/alirezarezvani/claude-skills/tree/f8593c4941210a621a6629ce1da9e07897976d5f/marketing-skill/skills/social-content) |

## Why the Change

The original `content-creator` tried to do everything: planning, writing, SEO, social, brand voice. That made it a jack of all trades. The specialist skills do each job better:

- **content-production** — Full pipeline: research → brief → draft → optimize → publish. Includes all Python tools from the original content-creator.
- **content-strategy** — Strategic planning: topic clusters, keyword research, content calendars, prioritization frameworks.

## Proactive Triggers

- **User asks "content creator"** → Route to content-production (most likely intent is writing).
- **User asks "content plan" or "what should I write"** → Route to content-strategy.

## Output Artifacts

| When you ask for... | Routed to... |
|---------------------|-------------|
| "Write a blog post" | content-production |
| "Content calendar" | content-strategy |
| "Brand voice analysis" | content-production (`brand_voice_analyzer.py`) |
| "SEO optimization" | content-production (`seo_optimizer.py`) |

## Communication

This is a redirect skill. Route the user to the correct specialist — don't attempt to handle the request here.

## Related Skills

- **content-production**: Full content execution pipeline (successor).
- **content-strategy**: Content planning and topic selection (successor).
- **content-humanizer**: Post-processing AI content to sound authentic.
- **marketing-context**: Foundation context that both successors read.

## More in this skill

Load these only when the task needs them.

- [references/analytics_guide.md](references/analytics_guide.md) — Content Analytics & Performance Metrics
- [references/brand_guidelines.md](references/brand_guidelines.md) — Brand Voice & Style Guidelines
- [references/content_frameworks.md](references/content_frameworks.md) — Content Creation Frameworks & Templates
- [references/social_media_optimization.md](references/social_media_optimization.md) — Social Media Optimization Guide
