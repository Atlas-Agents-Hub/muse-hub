#!/usr/bin/env python3
"""Render static release labels and downloads from the validated Muse collection."""
from __future__ import annotations

import argparse
import unicodedata
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
sys.path.insert(0, str(ROOT / 'scripts'))
from muse_collection import load_collection
from tool_guides import load_guides
from build_release import ALIASES, ROLE_WORKFLOWS, skill_download_layout, planner_asset

REPO = 'https://github.com/Atlas-Agents-Hub/muse-hub'
# Versioned guide links must match the actual selected downloadable release.
SITE_BASE = 'https://atlas-agents-hub.github.io/muse-hub/'
SOCIAL_IMAGE = SITE_BASE + 'social-card.png'


def social_meta(url: str, title: str, description: str) -> str:
    # Use the same branded image and page-specific description on each landing page.
    content = [
        ('og:type', 'website'),
        ('og:site_name', 'Muse Hub'),
        ('og:url', url),
        ('og:title', title),
        ('og:description', description),
        ('og:image', SOCIAL_IMAGE),
        ('og:image:secure_url', SOCIAL_IMAGE),
        ('og:image:type', 'image/png'),
        ('og:image:width', '1200'),
        ('og:image:height', '630'),
        ('og:image:alt', 'Muse Hub: build more with specialists, skills, Spaces and workflows.'),
    ]
    tags = ['<meta property="' + name + '" content="' + html.escape(value,quote=True) + '">' for name,value in content]
    tags.extend('<meta name="' + name + '" content="' + html.escape(value,quote=True) + '">' for name,value in (
        ('twitter:card', 'summary_large_image'),
        ('twitter:title', title),
        ('twitter:description', description),
        ('twitter:image', SOCIAL_IMAGE),
    ))
    return '\n'.join(tags)

SITE = ROOT / 'hub/site'
DOWNLOAD_PAGE_SIZE = 18
HOME_CAPTIONS = {
    'packages': 'Complete ZIP packages · Version {version}',
    'specialist': 'YOUR SPECIALIST / VERSION {version}',
    'footer': 'MUSE HUB · VERSION {version}',
}
CAPTION = re.compile(
    r'(?P<open><(?P<tag>div|span)\b[^<>]*\bdata-release-caption="(?P<key>[^"]+)"[^<>]*>)'
    r'[^<>]*(?P<close></(?P=tag)>)')


def release_version(root: Path = ROOT) -> str:
    version = json.loads((root / 'presets/catalog.json').read_bytes())['release']
    if not isinstance(version, str) or not re.fullmatch(r'v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)', version):
        raise ValueError('The catalog must select a stable release version.')
    return version

# Short customer descriptions; procedures and acceptance criteria remain in each kit.
DESCRIPTIONS = {
    'daily-briefing': 'Make a realistic plan for today. Includes reusable reminder and calendar worksheets with filled examples.',
    'weekly-reset': 'Review your goals, progress and available time, then choose the next useful action. Includes a goal review worksheet and example.',
    'accessible-ui': 'Review accessible interfaces and check HTML for missing language, empty page titles, duplicate IDs and markup to review. Includes a Python checker and example pages.',
    'project-prioritization': 'Rank your backlog with RICE and choose work that fits your dependencies and resource budgets. Includes a Python calculator and JSON/CSV examples.',
    'inbox-triage': 'Prioritize email threads, prepare replies in your voice and resume from the last completed review. Includes workspace validation, search-window calculation and a draft-operation log checker.',
    'claim-audit': 'Check a factual claim against the evidence that supports it.',
    'release-readiness': 'Review a release package, its checks, and the path to delivery.',
    'purchase-compare': 'Compare products against your requirements, budget and total cost.',
    'hobby-practice': 'Build a manageable practice session with useful feedback.',
    'content-system': 'Plan consistent content from your existing material and ideas.',
    'literature-triage': 'Organize a set of papers into a focused literature map.',
    'question-to-evidence': 'Turn a broad research question into an answerable investigation.',
    'creative-brief': 'Shape a creative idea into a clear production brief.',
    'calm-day': 'Turn your commitments into a realistic plan for the day.',
    'evidence-brief': 'Investigate a focused question and check the resulting findings.',
    'product-to-implementation': 'Turn a product request into interface, data and automation specifications your team can build.',
    'pipeline-validation': 'Review schema changes, reconcile a data batch and inspect query performance.',
    'idea-to-offer': 'Explore customer needs and shape a practical offer.',
    # Verified against the linked source SKILL.md files; retain source terminology.
    'azure-eventhub-dotnet': 'Send and receive events with the Azure Event Hubs .NET SDK. Covers EventProcessorClient checkpointing, Azure Identity and event-streaming configuration.',
    'cc-skill-project-guidelines-example': 'Use an illustrative project-skill template for architecture, code patterns, tests and deployment. Adapt its examples to your own repository; it is not a universal project policy.',
    'claude-scientific-skills': 'Find relevant workflows in the upstream Scientific Agent Skills library and review dependencies, licenses and evidence before importing. This is a discovery guide, not a bundled scientific toolkit.',
    'expo-dev-client': 'Create an Expo development client with EAS Build for native modules and platform extensions beyond Expo Go. Includes development build profiles and device testing.',
    'favicon': 'Generate favicon variants from a supplied image, place them in the correct static assets folder and update HTML links. Includes ImageMagick and framework detection.',
    'geo-citability': 'Review answer clarity and source evidence with a citability rubric, then measure AI citations on a dated query sample. This editorial method does not guarantee ranking gains.',
    'geo-crawlers': 'Review crawler access against search, privacy and training preferences. Distinguish search bots, training crawlers and user-directed requests before changing site rules.',
    'hugging-face-dataset-viewer': 'Explore datasets with the read-only Hugging Face Dataset Viewer API: inspect splits, preview rows, search or filter entries, and retrieve statistics and Parquet links.',
    # Source-grounded descriptions for competitor research tasks.
    'competitor-analysis': 'Compare approved competitors using cited feature and pricing research, optional authorized screenshots, and an HTML or CSV report. Browserbase use requires provider and budget approval.',
    'competitor-backlink-idea-generator': 'Analyze competitor backlink examples to identify relevant outreach prospects and original content opportunities. Mark unverified link metrics as unknown.',
    'competitor-gap-analyzer': 'Compare offerings, audience needs and product capabilities using comparable evidence. Prioritize identified gaps by user value and implementation effort.',
    'competitor-keyword-overlap-checker': 'Compare two labeled keyword sets to identify shared and exclusive keywords, overlap percentages and keyword opportunities. Does not infer rankings.',
    'competitor-summary-report-creator': 'Organize sourced competitor research into a dated report covering positioning, audiences, offerings and acquisition signals. Separate facts from interpretations.',
    'ai-competitor-title-rewriter': 'Create three original page titles based on competing content promises while preserving factual scope and avoiding copied phrasing.',
    # English display summaries of mixed-language source triggers; source packages stay intact.
    'baoyu-comic': 'Create educational, biographical and tutorial comics that explain a subject visually.',
    'baoyu-infographic': 'Design infographics using 21 layout options and 21 visual styles.',
    'crossframe': 'Use the CrossFrame method for structural diagnosis of complex relationships, organizations, institutions, public disputes or long-term change. The source method uses Chinese terminology.',
    'de-ai-writer': 'Review Chinese drafts for 35 patterns associated with AI-generated writing, score those patterns, and revise the prose or adapt it to a supplied writing style.',
    'emergency-card': 'Prepare a concise emergency medical information card from supplied allergies, medications, urgent conditions and implants. Export as JSON, text or a QR code for travel or clinical visits.',
    'fact-check-x-unified': 'Orchestrate comparison of multiple AI answers, distinguish unverified synthesis from authoritative verification, and produce an auditable report. The full pipeline requires separately installed companion skills.',
    'health-trend-analyzer': 'Explore changes in supplied health data over time, including symptoms, medications, vital signs, lab results, weight, mood and sleep. Includes correlation analysis and interactive ECharts reports.',
    'humanize-chinese': 'Review AI-like patterns in Chinese prose and revise it for natural style. Covers scoring, academic writing review and style conversion.',
    'liepin-jobs': "Connect supported coding agents to Liepin's official MCP server to search Chinese job listings and review resumes. Applications require explicit approval; tokens stay in environment variables.",
    'liuguang-banlan-ui': 'Build iridescent white or colorful black UI themes with parameterized OKLCH colors, WebGL or CSS fallback, screenshot checks and measured color-intensity reports.',
    'makepad-animation': "Work with Makepad's animation system, including animators, hover and pressed states, and transitions.",
    'makepad-basics': 'Get started with Makepad app structure, project setup, live_design! and app_main!.',
    'makepad-deployment': 'Package and distribute Makepad applications for desktop, mobile and WebAssembly with cargo-packager, cargo-makepad and CI workflows.',
    'makepad-dsl': "Use Makepad's live design syntax, inheritance, prototypes and component definitions.",
    'makepad-event-action': 'Handle Makepad events and actions using Event, ActionTrait, handle_event, pointer input and post_action.',
    'makepad-font': 'Configure Makepad fonts, typography, glyph rendering, font atlases and text layout.',
    'makepad-layout': 'Build Makepad layouts with Fit, Fill, Size, Walk, flow, spacing, padding and alignment.',
    'makepad-platform': 'Review Makepad platform support across macOS, Windows, Linux, Android, iOS and web, including graphics backend differences.',
    'makepad-shaders': 'Work with Makepad shaders, Sdf2d, draw_bg and draw_quad for GPU-based drawing.',
    'makepad-splash': "Use Makepad's Splash scripting language, script! and cx.eval for scripting and dynamic behavior.",
    'monetize': 'Build a personal side-income plan from existing experience and skills, with opportunity assessment, product ideas, a first action and sourced or explicitly labeled estimates.',
    'pro-launch': 'Plan a product from concept to launch with references, naming, style frames, UI iteration, launch video and go-to-market gates.',
    'pro-motion': 'Plan an audio-first product launch or promotional motion-graphics video, then render timed visuals to match the track.',
    'readme-polish': "Improve an existing README's readability, information hierarchy, badges and diagrams using comparable repositories and a deterministic lint check.",
    'robius-app-architecture': 'Apply Robius architecture patterns for Tokio, asynchronous requests, SignalToUI, worker tasks and app startup.',
    'robius-event-action': 'Handle custom Robius actions and signals, including cx.widget_action, handle_actions and DefaultNone.',
    'robius-matrix-integration': 'Integrate the Matrix SDK into Makepad and Robius apps, including sliding sync, requests, timelines, rooms and session handling.',
    'robius-state-management': 'Manage Robius application state, persistence, theme switching, scoped data and Serde serialization.',
    'robius-widget-patterns': 'Build Robius widget patterns including overlays, modals, collapsible sections, drag and drop, and reusable components.',
    'skill-skill': 'Write, improve or audit a Claude skill with explicit triggers, behavioral requirements and a static quality audit.',
    'travel-health-analyzer': 'Review supplied travel health information and destination risks, summarize vaccination considerations from supported WHO and CDC data, and prepare multilingual emergency information cards.',
    'wechat-official-account-strategist': 'Plan content for WeChat Official Accounts, including article structure, title approaches and Mini-Program integration.',
    'xiaohongshu-content-strategist': 'Plan Xiaohongshu content using platform-specific topics, save-rate optimization, trend formats and search discovery.',
}
TITLES = {
    'release-readiness': 'Prepare a Release for Delivery',
    'prose-revision': 'Revise Prose While Preserving Its Voice',
    'literature-triage': 'Build a Focused Literature Map',
    'inbox-triage': 'Inbox Review and Reply Drafts',
}

# Public subjects group the original catalog vocabulary without losing search terms.
SUBJECTS = {
    'software-engineering': 'Software & automation',
    'automation-engineering': 'Software & automation',
    'engineering': 'Software & automation', 'apps': 'Software & automation',
    'data-and-models': 'Data & AI', 'data-engineering': 'Data & AI',
    'data': 'Data & AI', 'models': 'Data & AI',
    'scientific-research': 'Research & science',
    'research-and-evidence': 'Research & science', 'research': 'Research & science',
    'interface-design': 'Design & visualization',
    'design': 'Design & visualization', 'visualization': 'Design & visualization',
    'creative-production': 'Creative & games',
    'creative': 'Creative & games', 'games': 'Creative & games',
    'business-and-projects': 'Business & projects',
    'career-and-communication': 'Business & projects', 'coordination': 'Business & projects',
    'care-and-personal-life': 'Personal planning', 'everyday-life': 'Personal planning',
    'personal-productivity': 'Personal planning', 'companion': 'Personal planning',
    'home-travel-and-hobbies': 'Home & travel',
    'learning-and-development': 'Learning & study',
    'learning-and-study': 'Learning & study', 'learning': 'Learning & study',
    'security': 'Security',
    'reliability-engineering': 'Infrastructure & reliability',
    'computing': 'Infrastructure & reliability',
    'shared-foundations': 'Using Muse', 'discovery': 'Using Muse',
}
SPECIALIST_SUBJECTS = {
    'coordinator': 'Business & projects',
    'software-engineer': 'Software & automation',
    'automation-engineer': 'Software & automation',
    'data-engineer': 'Data & AI', 'model-builder': 'Data & AI',
    'reliability-engineer': 'Infrastructure & reliability',
    'research-evaluator': 'Research & science', 'claims-adjudicator': 'Research & science',
    'adversarial-verifier': 'Security', 'reverse-engineering-researcher': 'Security',
    'creative-studio': 'Creative & games', 'product-interface-designer': 'Design & visualization',
    'learning-coach': 'Learning & study', 'personal-companion': 'Personal planning',
    'garden-companion': 'Home & travel',
}


# Presentation-only taxonomy fixes, grounded in the linked SKILL.md topics.
# The upstream collection and install-package membership remain unchanged.
SUBJECT_CORRECTIONS = {
    '2d-games': 'Creative & games',
    '3d-games': 'Creative & games',
    'emergency-card': 'Personal planning',
    'health-trend-analyzer': 'Personal planning',
    'travel-health-analyzer': 'Home & travel',
    'liuguang-banlan-ui': 'Design & visualization',
    'wechat-official-account-strategist': 'Business & projects',
    'competitor-analysis': 'Business & projects',
    'competitor-backlink-idea-generator': 'Business & projects',
    'competitor-gap-analyzer': 'Business & projects',
    'competitor-keyword-overlap-checker': 'Business & projects',
    'competitor-summary-report-creator': 'Business & projects',
}

# Editorial task paths link only to existing source guides. These are not
# rankings, endorsements or an alternative release inventory.
SUBJECT_STARTS = {
    'Business & projects': (
        ('customer-research', 'Learn from customers', 'Plan or synthesize customer research before choosing a direction.'),
        ('project-prioritization', 'Prioritize the backlog', 'Compare impact, dependencies and capacity before selecting work.'),
        ('idea-to-offer', 'Test a proposed offer', 'Move from customer needs to a defensible offer without overpromising.'),
    ),
    'Creative & games': (
        ('creative-brief', 'Define the brief', 'Turn an idea into a clear production brief with constraints and deliverables.'),
        ('storyboard', 'Plan a visual sequence', 'Map scene purpose and progression before producing video or animation.'),
        ('game-design', 'Design a game loop', 'Plan mechanics, player goals and progression before implementation.'),
    ),
    'Data & AI': (
        ('data-quality-auditor', 'Inspect a dataset', 'Check missing values, inconsistencies and quality risks before analysis.'),
        ('senior-data-engineer', 'Design a data pipeline', 'Plan ETL and ELT jobs, scheduling and data quality checks.'),
        ('sql-pro', 'Investigate a slow query', 'Use query plans, schema design and indexes to diagnose SQL performance.'),
    ),
    'Design & visualization': (
        ('ux-flow', 'Map a user journey', 'Lay out navigation and the steps people take to finish a task.'),
        ('ux-audit', 'Find interface friction', 'Review usability issues and prioritize fixes grounded in observed screens.'),
        ('design-token-audit', 'Verify interface colors', 'Check actual foreground and background token pairs for contrast.'),
    ),
    'Infrastructure & reliability': (
        ('incident-commander', 'Coordinate an incident', 'Organize response roles, status and safe next actions during an outage.'),
        ('performance-profiler', 'Find a bottleneck', 'Use profiling and traces to isolate slow endpoints or memory spikes.'),
        ('capacity-planner', 'Plan for demand', 'Translate measured performance into realistic infrastructure capacity.'),
    ),
    'Learning & study': (
        ('lecture-map', 'Preview a lecture', 'Build a concept map from slides or notes before detailed study.'),
        ('source-flashcards', 'Practice from source', 'Turn supplied material into traceable questions and flashcards.'),
        ('teach-back', 'Explain it aloud', 'Use an explanation to reveal missing links in your understanding.'),
    ),
    'Personal planning': (
        ('daily-briefing', 'Plan today', 'Fit commitments into the time available with a practical daily briefing.'),
        ('inbox-triage', 'Triage the inbox', 'Prioritize threads, draft replies and resume from the last review.'),
        ('weekly-reset', 'Review the week', 'Revisit goals and available capacity to choose what matters next.'),
    ),
    'Research & science': (
        ('question-to-evidence', 'Frame a research question', 'Define an answerable question and the evidence needed to check it.'),
        ('literature-triage', 'Map the literature', 'Sort papers into themes and gaps before writing a review.'),
        ('claim-audit', 'Check a claim', 'Trace a factual statement to the evidence that actually supports it.'),
    ),
    'Security': (
        ('ai-agent-security', 'Harden an AI agent', 'Review prompt injection, tool privileges and data-exposure risks.'),
        ('agentic-actions-auditor', 'Audit workflow permissions', 'Check automation integrations for insecure GitHub Action patterns.'),
        ('security-pen-testing', 'Test with authorization', 'Define scope and check vulnerabilities only in permitted systems.'),
    ),
    'Software & automation': (
        ('ai-code-review-triage', 'Review an AI-built change', 'Triage pull requests and focus review on high-impact defects.'),
        ('api-contract-testing', 'Check an API change', 'Test consumer and provider contracts before schema changes break clients.'),
        ('agentic-test-audit', 'Audit a test suite', 'Find flaky tests, surviving mutants and coverage gaps before release.'),
    ),
}



def subject(category: str) -> str:
    if category in SUBJECTS.values():
        return category
    if category not in SUBJECTS:
        raise ValueError('Unmapped public subject: ' + str(category))
    return SUBJECTS[category]


def subject_slug(label: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')


def subject_pages(data: dict, home: str) -> dict[str,bytes]:
    """Publish readable subject indexes that work with ordinary links."""
    result={}
    intros={
        'Software & automation':'Build apps, review code, reproduce bugs and automate repeatable work. Find framework guides, browser workflows and specialist methods for your next software project.',
        'Data & AI':'Work with SQL, data pipelines, retrieval, model evaluation and AI applications. Choose methods for the data and tools you already use.',
        'Research & science':'Turn questions into research plans, work with scientific data and produce clear findings. Explore methods for statistics, literature reviews and reproducible analysis.',
        'Design & visualization':'Plan products, build accessible interfaces and communicate ideas visually. Find practical methods for research, layouts, interaction design and charts.',
        'Creative & games':'Develop visual concepts, characters, animation, video and games. Bring a brief and use the methods that fit your creative tools.',
        'Business & projects':'Organize projects, improve operations, plan campaigns and support customer work. Each resource gives you a practical way to move from a goal to a result.',
        'Personal planning':'Organize your day, capture notes, manage routines and make room for the work that matters. Adapt each method to your commitments and preferences.',
        'Home & travel':'Plan trips, organize home projects, track plants and develop your hobbies. Start with the details of your situation and choose the next useful action.',
        'Learning & study':'Build lessons, flashcards and focused practice from your material. Use worked examples and review prompts to keep learning active.',
        'Security':'Review application security, investigate software behavior and test defenses in your authorized environment. Find methods for specific systems and concrete findings.',
        'Infrastructure & reliability':'Deploy services, investigate incidents, manage infrastructure and understand performance. Connect changes to observable service behavior.',
        'Using Muse':'Set up your assistant, organize its work and choose the right resources for a task. Start here when building a personal Muse toolkit.',
    }
    esc=html.escape
    # Single source of truth for global navigation; all subject pages share the
    # authored homepage header/footer and resolve relative links from /library/.
    def from_library(fragment: str) -> str:
        return re.sub(r'(?P<attr>(?:href|src)=")(?P<path>index\.html|downloads\.html|public/index\.html|muse-mark\.png)',
                      lambda match: match['attr']+'../'+match['path'], fragment)
    shared_header = from_library(home[home.index('  <header'):home.index('  <main')])
    shared_footer = from_library(home[home.index('  <footer'):home.index('\n</body>')])
    for label in data['categories']:
        rows=[row for row in data['items'] if row['category']==label]
        pages=[rows[i:i+200] for i in range(0,len(rows),200)]
        slug=subject_slug(label)
        for number,items in enumerate(pages,1):
            route=f'library/{slug}-{number:03d}.html'
            title=f'{label} skills and workflows for Muse'
            # Show no dead-end pager for a single page; trim long page lists
            # but preserve access to every page via Prev/Next and edge links.
            total_pages=len(pages)
            navigation=''
            if total_pages>1:
                visible={1,total_pages,number-1,number,number+1}
                if number<=2:visible.add(3)
                if number>=total_pages-1:visible.add(total_pages-2)
                visible=sorted(i for i in visible if 1<=i<=total_pages)
                links=[]
                if number>1:links.append(f'<a rel="prev" href="{slug}-{number-1:03d}.html" aria-label="Previous subject page">← Prev</a>')
                last=0
                for i in visible:
                    if i-last>1:links.append('<span class="subject-ellipsis" aria-hidden="true">…</span>')
                    current=' aria-current="page"' if i==number else ''
                    links.append(f'<a href="{slug}-{i:03d}.html"{current}>{i}</a>')
                    last=i
                if number<total_pages:links.append(f'<a rel="next" href="{slug}-{number+1:03d}.html" aria-label="Next subject page">Next →</a>')
                navigation=' '.join(links)
            start_panel=''
            if number==1 and label in SUBJECT_STARTS:
                by_id={row['id']:row for row in rows}
                paths=[]
                for item_id, action, summary in SUBJECT_STARTS[label]:
                    selected=by_id.get(item_id)
                    if not selected or selected['kind'] not in ('skill','workflow') or not selected.get('guide_url'):
                        raise ValueError(f'Invalid curated starting point: {label} / {item_id}')
                    paths.append(
                        f'<a class="subject-start-link" data-resource-id="{esc(item_id)}" '
                        f'href="{esc(selected["guide_url"])}">'
                        f'<strong>{esc(action)}</strong><span>{esc(summary)}</span>'
                        f'<em>Read method →</em></a>')
                start_panel=(
                    '<section class="subject-start" aria-labelledby="subject-start-title">'
                    '<div class="subject-start-heading">'
                    '<h2 id="subject-start-title">Start with a task</h2></div>'
                    f'<nav class="subject-start-grid" aria-label="Task paths in {esc(label)}">'
                    f'{"".join(paths)}</nav></section>\n')
            page_summary=f'Page {number} of {total_pages}' if total_pages>1 else 'All resources'
            pager_top=f'<nav class="download-pagination subject-pagination" aria-label="Subject pages">{navigation}</nav>' if navigation else ''
            pager_bottom=f'<nav class="download-pagination subject-pagination" aria-label="More subject pages">{navigation}</nav>' if navigation else ''
            cards=[]
            for row in items:
                text=row['description']
                if len(text)>220:text=text[:217].rsplit(' ',1)[0]+'…'
                read=f'<a class="subject-guide-link" href="{esc("../" + row["guide_url"] if row["kind"] == "specialist" else row["guide_url"])}">{"Setup guide" if row["kind"] == "specialist" else "Read method"} →</a>' if row.get('guide_url') else ''
                packed=row.get('pack_kind')=='skill-pack'
                download='Download skill pack' if packed else 'Download ZIP'
                entry=f'<details class="subject-source"><summary>Included pack path</summary><code>{esc(row["entry"])}</code></details>' if packed else ''
                cards.append(f'<article class="download-card subject-card" data-kind="{esc(row["kind"])}"><span class="download-kind">{esc(row["kind"].replace("-"," "))}</span><h2>{esc(row["title"])}</h2><p>{esc(text)}</p>{entry}<div class="subject-card-actions">{read}<a href="{esc(row["url"])}">{download} ↓</a></div></article>')
            # The published URL retains at most 200 indexed cards, but only the
            # first 18 should consume layout space by default. Native details
            # keep the remainder reachable with JavaScript completely disabled.
            first_cards=''.join(cards[:DOWNLOAD_PAGE_SIZE])
            slices=[]
            for offset in range(DOWNLOAD_PAGE_SIZE,len(cards),DOWNLOAD_PAGE_SIZE):
                end=min(offset+DOWNLOAD_PAGE_SIZE,len(cards))
                slices.append(
                    f'<details class="subject-slice" data-start="{offset+1}" data-end="{end}">'
                    f'<summary>Show resources {offset+1}&ndash;{end} of {len(cards)} on this page</summary>'
                    f'<div class="download-grid subject-grid">{"".join(cards[offset:end])}</div></details>')
            preview=(f'<p class="subject-preview-note">Showing the first {DOWNLOAD_PAGE_SIZE} of {len(cards)} '
                     f'resources on this page. <a href="#subject-more">Jump to more ranges</a></p>' if slices else '')
            more=(f'<section class="subject-more" aria-label="More resources on this page">'
                  f'<h2 id="subject-more" tabindex="-1">More resources on this page</h2>{"".join(slices)}</section>' if slices else '')
            url='https://atlas-agents-hub.github.io/muse-hub/'+route
            page_description=(intros[label] if len(pages)==1 else
                f'{intros[label]} Browse {label.lower()} resources on page {number} of {len(pages)}.')
            schema={'@context':'https://schema.org','@type':'CollectionPage','name':title,
                    'url':url,'description':page_description,'image':SOCIAL_IMAGE,
                    'isPartOf':{'@type':'WebSite','name':'Muse Hub','url':SITE_BASE},
                    'breadcrumb':{'@type':'BreadcrumbList','itemListElement':[
                        {'@type':'ListItem','position':1,'name':'Muse Hub','item':SITE_BASE},
                        {'@type':'ListItem','position':2,'name':'Library','item':SITE_BASE+'downloads.html'},
                        {'@type':'ListItem','position':3,'name':label,'item':url},
                    ]}}
            body=f'''<!doctype html>
<html lang="en" class="subject-directory-page"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark"><meta name="theme-color" content="#151515">
<title>{esc(title)} | Muse Hub · {number}</title><meta name="description" content="{esc(page_description)}">
{social_meta(url, f'{title} | Page {number} | Muse Hub', page_description)}
<link rel="canonical" href="{url}"><link rel="stylesheet" href="../site.css"><link rel="stylesheet" href="../experience.css"><link rel="icon" type="image/png" href="../muse-mark.png">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body id="top" class="muse-premium subject-index"><a class="skip-link" href="#main">Skip to resources</a>
{shared_header}
<main id="main" class="shell subject-main">
  <nav class="subject-breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Muse Hub</a><span aria-hidden="true">/</span><a href="../downloads.html">Library</a><span aria-hidden="true">/</span><span>{esc(label)}</span></nav>
  <header class="subject-heading"><span class="subject-kicker">SKILLS, WORKFLOWS &amp; SPECIALISTS</span><h1>{esc(label)}</h1><p>{esc(intros[label])}</p>
  <div class="subject-summary"><span><strong>{len(rows):,}</strong> resources</span><span>{page_summary}</span><a href="../downloads.html?subject={quote(label)}">Search this subject →</a></div></header>
{start_panel}{pager_top}
{preview}
  <div class="download-grid subject-grid">{first_cards}</div>
{more}
{pager_bottom}
  <p class="subject-return"><a href="../downloads.html">← Explore all Muse skills, workflows and specialist kits</a></p>
</main>
{shared_footer}
</body></html>
'''
            result[route]=body.encode('utf-8')
    return result


def specialist_memberships(collection: dict) -> dict:
    """Use the same selected skills and workflow closure as specialist ZIPs."""
    memberships = {kind: {row['id']: [] for row in collection[kind]}
                   for kind in ('skills', 'workflows')}
    workflow_by_id = {row['id']: row for row in collection['workflows']}
    canonical_ids = {alias: canonical for canonical, alias in ALIASES.items()}
    for role in collection['specialists']:
        role_id = role['id']
        canonical = canonical_ids.get(role_id, role_id)
        workflows = set(ROLE_WORKFLOWS[canonical]) | set(role.get('library_workflows', []))
        skills = set(role['skills']) | set(role.get('library_skills', []))
        for workflow_id in workflows:
            memberships['workflows'][workflow_id].append(role_id)
            skills.update(workflow_by_id[workflow_id]['skills'])
        for skill_id in skills:
            memberships['skills'][skill_id].append(role_id)
    return memberships


def catalog(root: Path = ROOT) -> dict:
    version = release_version(root)
    base = REPO + '/releases/download/' + version + '/'
    collection = load_collection(root / 'collections/muse-starters-v1')
    identifiers={item['id'] for key in ('skills','workflows') for item in collection[key]}
    if (set(DESCRIPTIONS)|set(TITLES))-identifiers:
        raise ValueError('Public copy refers to an unknown collection item.')
    roles = json.loads((root / 'hub/site/roles.json').read_text(encoding='utf-8'))['roles']
    rows = []
    role_titles={ALIASES.get(role['id'],role['id']):role['name'] for role in roles}
    memberships = specialist_memberships(collection)
    skill_by_id = {row['id']: row for row in collection['skills']}
    skill_routes = skill_download_layout(collection, version)
    guide_catalog=load_guides(root)
    guide_memberships = {row['id']: set(row['specialist_ids']) for row in guide_catalog['guides']}
    for workflow in collection['workflows']:
        for guide_id in workflow.get('tool_guides', []):
            if guide_id in guide_memberships:
                guide_memberships[guide_id].update(memberships['workflows'][workflow['id']])
    for role in roles:
        asset = 'muse-' + role['asset_id'] + '-' + version + '.zip'
        rows.append(dict(id=role['id'], kind='specialist', title=role['name'],
                         description=role['description'], asset=asset, url=base+asset,
                         category=SPECIALIST_SUBJECTS[ALIASES.get(role['id'],role['id'])],
                         keywords='specialists '+role['category']+' '+role['category_label'],
                         roles=[ALIASES.get(role['id'],role['id'])],
                         guide_url=f'index.html?role={role["id"]}#setup'))
    for key, kind, description in (('skills', 'skill', 'trigger'), ('workflows', 'workflow', 'goal')):
        for item in sorted(collection[key], key=lambda row: (TITLES.get(row['id'],row['title']).casefold(), row['id'])):
            asset = f"muse-{kind}-{item['id']}-{version}.zip"
            pack = skill_routes[item['id']] if kind == 'skill' else {}
            if pack:
                asset = pack['asset']
                pack = {key:value for key,value in pack.items() if key!='asset'}
            original_category = (item['category'] if kind == 'skill'
                                 else skill_by_id[item['skills'][0]]['category'])
            public_category=SUBJECT_CORRECTIONS.get(item['id'], original_category) if kind == 'skill' else original_category
            rows.append(dict(id=item['id'], kind=kind, title=TITLES.get(item['id'],item['title']),
                             description=DESCRIPTIONS.get(item['id'],item[description]), asset=asset, url=base+asset,
                             category=subject(public_category),
                             keywords=(original_category+' '+original_category.replace('-', ' ')+
                                      (' '+public_category+' '+public_category.replace('-', ' ')
                                       if public_category!=original_category else '')),
                             roles=memberships[key][item['id']], **pack,
                             guide_url=REPO+'/blob/main/'+(
                                 ('collections/library/'+item['path'] if item.get('format')=='portable-skill'
                                  else 'collections/muse-starters-v1/skills/'+item['id'])+'/SKILL.md'
                                 if kind=='skill' else
                                 ('collections/library/workflows/' if item.get('steps')
                                  else 'collections/muse-starters-v1/workflows/')+item['id']+'.md')))
    for row in guide_catalog['guides']:
        asset=f"muse-tool-{row['id']}-{version}.zip"
        rows.append(dict(id=row['id'],kind='tool-guide',title=row['name'],description=row['summary'],
            asset=asset,url=base+asset,category=subject(row['category']),
            keywords=row['category'],roles=sorted(guide_memberships[row['id']]),
            guide_url=REPO+'/blob/main/'+row['doc_path']))
    # Reject untranslated prose from scripts used by imported multilingual resources.
    # Greek statistical symbols and Latin diacritics are valid English technical text.
    for row in rows:
        if any(c.isalpha() and not any(script in unicodedata.name(c, '')
                                      for script in ('LATIN', 'GREEK'))
               for c in row['description']):
            raise ValueError(f"Public description requires English editorial review: {row['id']}")
    counts = {kind: sum(row['kind'] == kind for row in rows) for kind in ('specialist','skill','workflow','tool-guide')}
    if counts['specialist']!=15 or counts['skill']<75 or counts['workflow']<25:
        raise ValueError(f'Incomplete release inventory: {counts}')
    if len({(row['kind'],row['id']) for row in rows}) != len(rows):
        raise ValueError('Duplicate catalog identity')
    bundles = []
    for slug, title, description in (
        ('specialists', 'All 15 specialists', 'Every specialist kit in one download.'),
        ('skills', f"All {counts['skill']} skills", 'The full skill library, with supporting files and practical methods.'),
        ('workflows', f"All {counts['workflow']} workflows", 'Complete workflows and the skills they use.'),
        ('starters', f"{len(collection['starters'])} task starters", 'Practical task prompts with the inputs and results to aim for.'),
        ('specialist-toolkit', 'Python toolkit', 'Run Muse Hub tools, examples and your local notebook.'),
    ):
        asset=f'muse-{slug}-{version}.zip'
        bundles.append(dict(id=slug,title=title,description=description,asset=asset,url=base+asset))
    if counts['tool-guide']:
        asset=f'muse-tool-guides-{version}.zip'
        bundles.append(dict(id='tool-guides',title=f"{counts['tool-guide']} tool guides",description='Setup, recipes and checks for the tools that fit your work.',asset=asset,url=base+asset))
    asset=planner_asset(version)
    bundles.append(dict(id='space-planner',title='Muse Planner',
        description='A full-stack Muse Space for projects, next actions, daily routines, weekly reviews, notes and calendars.',
        asset=asset,url=base+asset,roles=['coordinator','personal-companion'],
        guide_url=REPO+'/blob/'+version+'/docs/spaces/MUSE_PLANNER.md'))
    connectors_path=root/'docs/connectors/catalog.json'
    connector_count=len(json.loads(connectors_path.read_bytes())['connectors']) if connectors_path.exists() else 151
    return {'schema':'muse-hub/downloads/v1','version':version,'counts':counts,
            'starter_count':len(collection['starters']), 'connector_count':connector_count,
            'skill_pack_count':len({row['asset'] for row in skill_routes.values()}),
            'bundles':bundles,'items':rows,'roles':role_titles,
            'categories':sorted({row['category'] for row in rows},key=str.casefold)}


def render_homepage(data: dict, root: Path = ROOT) -> str:
    """Keep authored page markup while deriving every current release field."""
    home = (root / 'hub/site/index.html').read_text(encoding='utf-8')
    # Keep authored links readable on main, but publish Space guides at the release tag.
    home = home.replace(REPO+'/blob/main/docs/spaces/', REPO+'/blob/'+data['version']+'/docs/spaces/')
    seen = []

    def caption(match: re.Match) -> str:
        key = match['key']
        if key not in HOME_CAPTIONS or key in seen:
            raise ValueError('Homepage release captions must have unique known keys.')
        seen.append(key)
        label = HOME_CAPTIONS[key].format(version=data['version'].removeprefix('v'))
        return match['open'] + html.escape(label) + match['close']

    home = CAPTION.sub(caption, home)
    def library_count(match):
        key=match['key']
        values={**data['counts'],'starter':data['starter_count'],'connector':data['connector_count']}
        if key not in values:raise ValueError('Unknown homepage inventory count.')
        return match['open']+f'{values[key]:,}'+match['close']
    home=re.sub(r'(?P<open><(?P<tag>strong|span|dd) data-library-count="(?P<key>[a-z-]+)">)[\d,]+(?P<close></(?P=tag)>)',library_count,home)
    for row in (item for item in data['items'] if item['kind']=='specialist'):
        identity=re.escape(row['id'])
        pattern=r'(<article class="role-card" data-role="'+identity+r'"[^>]*>)(.*?)(</article>)'
        def role_card(match):
            opening=re.sub(r'data-search="[^"]*"',lambda _: 'data-search="'+html.escape((row['title']+' '+row['description']+' '+row['keywords']).lower())+'"',match[1])
            body=re.sub(r'(</h3><p>).*?(</p>)',lambda part:part[1]+html.escape(row['description'])+part[2],match[2],count=1,flags=re.S)
            return opening+body+match[3]
        home=re.sub(pattern,role_card,home,flags=re.S)
        home=re.sub(r'(<option value="'+identity+r'" data-description=")[^"]*(">)',
                    lambda match:match[1]+html.escape(row['description'])+match[2],home)
    if set(seen) != set(HOME_CAPTIONS) or home.count('data-release-caption') != len(seen):
        raise ValueError('Homepage must mark all three release captions.')
    if re.search(r'\bversion\s+v?[0-9]+\.[0-9]+\.[0-9]+\b', CAPTION.sub('', home), re.IGNORECASE):
        raise ValueError('Homepage has an unmarked release caption.')

    assets = {row['asset']: row['url'] for row in data['items'] + data['bundles']}
    release_link = re.compile(r'href="' + re.escape(REPO + '/releases/') + r'(?P<route>[^"]+)"')

    def link(match: re.Match) -> str:
        route = match['route']
        if re.fullmatch(r'tag/v[0-9]+\.[0-9]+\.[0-9]+', route):
            return f'href="{REPO}/releases/tag/{data["version"]}"'
        download = re.fullmatch(r'download/v[0-9]+\.[0-9]+\.[0-9]+/([^/]+)', route)
        if download:
            asset = re.sub(r'-v[0-9]+\.[0-9]+\.[0-9]+(?=\.zip$)', '-' + data['version'], download[1])
            if asset in assets:
                return f'href="{html.escape(assets[asset])}"'
        raise ValueError('Homepage release link does not name a catalog download.')

    return release_link.sub(link, home)


def display_count(kind: str, count: int) -> str:
    """Show verified catalog totals, not lower rounded marketing estimates."""
    return f'{count:,}'


def render(data: dict, root: Path = ROOT, *, home: str | None = None) -> str:
    version = data['version']
    if home is None:
        home = render_homepage(data, root)
    favicon = home[home.index('  <link rel="icon"'):home.index('\n',home.index('  <link rel="icon"'))]
    header = home[home.index('  <header'):home.index('  <main')]
    # Shared navigation belongs to Home, even when a new section is added.
    # Only rewrite these inherited regions; download group jumps stay local.
    def home_links(region: str) -> str:
        return re.sub(r'href="#([a-zA-Z][a-zA-Z0-9_-]*)"',
                      lambda match: 'href="index.html' +
                      ('' if match[1] == 'top' else '#' + match[1]) + '"', region)
    header = home_links(header)
    footer = home[home.index('  <footer'):home.index('\n</body>')]
    footer = home_links(footer)
    esc = html.escape
    bundle_kinds = {'skills': ('skill', 'skills'), 'workflows': ('workflow', 'workflows'),
                    'starters': ('starter', 'task starters'), 'tool-guides': ('tool-guide', 'tool guides')}
    counts = {**data['counts'], 'starter': data['starter_count']}
    def bundle_title(row):
        if row['id'] in bundle_kinds:
            kind, label = bundle_kinds[row['id']]
            return f'{display_count(kind, counts[kind]).capitalize()} {label}'
        return row['title']

    bundle_html = '\n'.join(
        f'<a class="bundle-card" href="{esc(row["url"])}"><span>{esc(bundle_title(row))}</span><p>{esc(row["description"])}</p><strong>Download ZIP ↓</strong></a>'
        for row in data['bundles'])
    initial_items = data['items'][:DOWNLOAD_PAGE_SIZE]
    # Curated editorial entry points share the authoritative subject pages.
    goal_paths = (
        ('Build', 'Software & automation', 'Apps, debugging and workflows'),
        ('Research', 'Research & science', 'Questions, evidence and analysis'),
        ('Design', 'Design & visualization', 'Interfaces, graphics and charts'),
        ('Learn', 'Learning & study', 'Lessons, flashcards and review'),
    )
    if any(category not in data['categories'] for _, category, _ in goal_paths):
        raise ValueError('A discovery link lacks a subject page')
    goal_links = ''.join(
        f'<a href="library/{subject_slug(category)}-001.html">'
        f'<strong>{esc(title)}</strong><span>{esc(detail)}</span></a>'
        for title, category, detail in goal_paths
    )
    subject_links = []
    for label in data['categories']:
        count = sum(row['category'] == label for row in data['items'])
        if count:
            subject_links.append(f'<a href="library/{subject_slug(label)}-001.html">{esc(label)}</a>')
    sections=[]
    for kind, heading, anchor in (('specialist','Specialists','specialists'),('skill','Skills','skills'),('workflow','Workflows','workflows'),('tool-guide','Tool guides','tool-guides')):
        cards=[]
        for row in initial_items:
            if row['kind']!=kind:continue
            description=row['description']
            if len(description)>320:
                description=description[:317].rsplit(' ',1)[0]+'…'
            search=esc(' '.join((row['title'],description,row['id'],row['category'],row.get('keywords',''))))
            read_link=f'<a class="guide-link" href="{esc(row["guide_url"])}">{"Setup guide" if kind == "specialist" else "Read guide"} →</a>' if row.get('guide_url') else ''
            packed=row.get('pack_kind')=='skill-pack'
            label=f"Download skill pack · {row['pack_size']} skills" if packed else 'Download ZIP'
            hint=f'<p class="download-entry">Open <code>{esc(row["entry"])}</code> in this pack.</p>' if packed else ''
            cards.append(f'''<article class="download-card" data-id="{esc(row['id'])}" data-kind="{kind}" data-category="{esc(row['category'])}" data-roles="{esc(' '.join(row['roles']))}" data-search="{search}">
  <span class="download-kind">{esc(row['category'])}</span><h3>{esc(row['title'])}</h3><p>{esc(description)}</p>{hint}
  <div class="download-card-actions">{read_link}<a href="{esc(row['url'])}" aria-label="Download {esc(row['title'])}{' skill pack' if packed else ' ZIP'}">{esc(label)} <span aria-hidden="true">↓</span></a></div>
</article>''')
        count_label = display_count(kind, data['counts'][kind])
        sections.append(f'<section class="download-section" data-kind="{kind}" id="{anchor}" aria-labelledby="{anchor}-heading"'+(' hidden' if not cards else '')+f'><h2 id="{anchor}-heading">{heading} <span>{count_label}</span></h2><div class="download-grid">'+ '\n'.join(cards)+'</div></section>')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="dark">
  <meta name="theme-color" content="#151515">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'">
  <meta name="description" content="Search {display_count('skill', counts['skill'])} Muse AI skills, {display_count('workflow', counts['workflow'])} workflows, specialist kits and tool guides. Filter by subject or specialist and sort by title.">
  <link rel="canonical" href="https://atlas-agents-hub.github.io/muse-hub/downloads.html">
{social_meta(SITE_BASE + 'downloads.html', 'Muse AI Skills, Workflows and Specialist Downloads', 'Find the skills, workflows and tools for your next task.')}
  <script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':'Muse Hub Downloads','url':'https://atlas-agents-hub.github.io/muse-hub/downloads.html','image':SOCIAL_IMAGE,'description':'Muse AI skills, workflows, specialists and tool guides.','isPartOf':{'@type':'WebSite','name':'Muse Hub','url':'https://atlas-agents-hub.github.io/muse-hub/'}})}</script>
  <title>Muse AI Skills &amp; Workflow Downloads | Muse Hub</title>
{favicon}
  <link rel="stylesheet" href="site.css">\n  <link rel="stylesheet" href="experience.css">\n  <script defer src="downloads.js"></script>
</head>
<body id="top" class="muse-premium downloads-page">
  <a class="skip-link" href="#main">Skip to downloads</a>
{header}  <main id="main">
    <section class="downloads-catalog section-dark" id="catalog"><div class="shell">
      <div class="catalog-heading">
        <h1>Muse Hub Library</h1>
        <p>Find {display_count('skill', counts['skill'])} Muse skills, {display_count('workflow', counts['workflow'])} workflows, {display_count('specialist', counts['specialist'])} specialist kits and {display_count('tool-guide', counts['tool-guide'])} tool guides. Search by task or start with a subject.</p>
      </div>
      <nav class="download-jumps" aria-label="Library types">
        <a href="downloads.html#catalog" data-download-type="all">All</a>
        <a href="downloads.html?type=skill#catalog" data-download-type="skill">Skills</a>
        <a href="downloads.html?type=workflow#catalog" data-download-type="workflow">Workflows</a>
        <a href="downloads.html?type=specialist#catalog" data-download-type="specialist">Specialists</a>
        <a href="downloads.html?type=tool-guide#catalog" data-download-type="tool-guide">Tool guides</a>
      </nav>
      <div class="role-toolbar download-toolbar">
        <div class="field-wrap"><label for="download-search">Search the library</label><input id="download-search" type="search" placeholder="Try debugging, design, research…" autocomplete="off" aria-controls="download-results"></div>
        <details class="download-advanced"><summary>Refine results</summary><div class="download-filter-grid"><div class="field-wrap category-wrap"><label for="download-kind">Type</label><select id="download-kind" aria-controls="download-results"><option value="all">Everything</option><option value="specialist">Specialists</option><option value="skill">Skills</option><option value="workflow">Workflows</option><option value="tool-guide">Tool guides</option></select></div>
        <div class="field-wrap category-wrap"><label for="download-role">Specialist</label><select id="download-role" aria-controls="download-results"><option value="all">All specialists</option>{''.join('<option value="'+esc(key)+'">'+esc(title)+'</option>' for key,title in data['roles'].items())}</select></div>
        <div class="field-wrap category-wrap"><label for="download-category">Subject</label><select id="download-category" aria-controls="download-results"><option value="all">All subjects</option>{''.join('<option value="'+esc(title)+'">'+esc(title)+'</option>' for title in data['categories'])}</select></div>
        <div class="field-wrap category-wrap"><label for="download-sort">Sort by title</label><select id="download-sort" aria-controls="download-results"><option value="catalog">Catalog order</option><option value="az">A to Z</option><option value="za">Z to A</option></select></div>
        </div></details>\n        <button id="download-reset" class="reset-btn" type="button">Clear</button>
      </div>
      <p id="download-count" role="status" aria-live="polite">Showing 1–{len(initial_items)} of {len(data['items']):,} downloads</p>
      <section class="catalog-goals" aria-labelledby="catalog-goals-title">
        <h2 id="catalog-goals-title">Explore by goal</h2>
        <nav class="catalog-goal-links" aria-label="Find a subject for your next task">{goal_links}</nav>
      </section>
      <details class="catalog-subjects"><summary>Browse every download by subject</summary><nav class="download-jumps" aria-label="Subject library">{''.join(subject_links)}</nav></details>
      <div id="download-results" data-total="{len(data['items'])}" data-page-size="{DOWNLOAD_PAGE_SIZE}" data-version="{esc(version)}">{''.join(sections)}</div>
      <nav id="download-pages" class="download-pagination" aria-label="Download result pages" hidden><button id="download-previous" class="reset-btn" type="button">Previous</button><span id="download-page-label"></span><button id="download-next" class="reset-btn" type="button">Next</button></nav>
      <div id="download-empty" class="role-empty" hidden><h2>No matching downloads.</h2><p>Try a shorter search or clear the filters.</p><button id="download-clear-empty" type="button">Show all downloads</button></div>
    </div></section>
    <section class="downloads-hero section-dark" aria-labelledby="bundle-title"><div class="shell">
      <span class="eyebrow signal">Version {esc(version.removeprefix('v'))}</span>
      <h2 id="bundle-title">Download complete collections</h2>
      <p>Unzip a collection and open <strong>START_HERE.md</strong> to use it with Muse.</p>
      <div class="bundle-grid">{bundle_html}</div>
      <div class="downloads-help"><a href="{REPO}/blob/main/docs/GETTING_STARTED.md">Getting started →</a><a href="{REPO}/blob/main/docs/collection/FIND_AND_BUILD.md">Build a custom pack →</a><a href="{REPO}/blob/main/docs/TERMINAL.md">Terminal guide →</a><a href="{REPO}/releases/tag/{esc(version)}">Release notes and checksums →</a></div>
    </div></section>
  </main>
{footer}
</body>
</html>
'''


def outputs(root: Path = ROOT) -> dict[str,bytes]:
    data=catalog(root)
    home=render_homepage(data,root)
    result={'index.html':home.encode('utf-8'),
            'downloads.json':(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8'),
            'downloads.html':render(data,root,home=home).encode('utf-8')}
    result.update(subject_pages(data,home))
    # Publish a project-specific answer-engine index from the same inventory as the website.
    base='https://atlas-agents-hub.github.io/muse-hub/'
    counts=data['counts']
    result['llms.txt']=(
        '# Muse Hub\n\n'
        "> Muse Hub is an open-source toolkit for Meta's Muse AI. "
        'Published by Atlas Agents Hub. '
        f"The library includes {counts['skill']:,} skills, {counts['workflow']:,} workflows, "
        f"{counts['specialist']} specialist kits and {counts['tool-guide']} tool guides.\n\n"
        '## Start here\n\n'
        f'- [Muse Hub]({base}): choose a task, specialist or Space template.\n'
        f'- [Resource library]({base}downloads.html): search skills, workflows and specialist kits.\n'
        f'- [Setup guides]({base}public/index.html): browse setup and integration routes.\n'
        f'- [Getting started]({REPO}/blob/main/docs/GETTING_STARTED.md): download and configure a kit in Muse.\n'
        f'- [Release packages]({REPO}/releases/tag/{data["version"]}): current downloadable assets.\n'
        f'- [Repository]({REPO}): source code and documentation.\n'
        f'- [Sitemap]({base}sitemap.xml): canonical website pages.\n'
        f'- [Expanded resource index]({REPO}/blob/main/llms.txt): additional guides and resources.\n'
    ).encode('utf-8')
    urls=['','downloads.html','public/index.html',*sorted(name for name in result if name.startswith('library/'))]
    result['sitemap.xml']=('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+
        ''.join('<url><loc>https://atlas-agents-hub.github.io/muse-hub/'+name+'</loc></url>\n' for name in urls)+'</urlset>\n').encode('utf-8')
    return result


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name,content in outputs().items():
        path=SITE/name
        if args.check:
            if not path.is_file() or path.read_bytes()!=content:stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(content)
    if stale:
        print('Downloads need regeneration: '+', '.join(stale),file=sys.stderr)
        return 1
    print('Downloads verified.' if args.check else 'Downloads updated.')
    return 0


if __name__=='__main__':raise SystemExit(main())
