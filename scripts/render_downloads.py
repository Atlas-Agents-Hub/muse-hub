#!/usr/bin/env python3
"""Render static release labels and downloads from the validated Muse collection."""
from __future__ import annotations

import argparse
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

REPO = 'https://github.com/atlas-origins/muse-ai-agent-presets'
SITE = ROOT / 'hub/site'
DOWNLOAD_PAGE_SIZE = 60
HOME_CAPTIONS = {
    'packages': 'Complete ZIP packages · Version {version}',
    'specialist': 'YOUR SPECIALIST / VERSION {version}',
    'footer': 'VERSION {version} · BUILT FOR MUSE',
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


def subject(category: str) -> str:
    if category in SUBJECTS.values():
        return category
    if category not in SUBJECTS:
        raise ValueError('Unmapped public subject: ' + str(category))
    return SUBJECTS[category]


def subject_slug(label: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')


def subject_pages(data: dict) -> dict[str,bytes]:
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
    for label in data['categories']:
        rows=[row for row in data['items'] if row['category']==label]
        pages=[rows[i:i+200] for i in range(0,len(rows),200)]
        slug=subject_slug(label)
        for number,items in enumerate(pages,1):
            route=f'library/{slug}-{number:03d}.html'
            title=f'{label} skills and workflows for Muse'
            navigation=' '.join(f'<a href="{slug}-{i:03d}.html"'+(' aria-current="page"' if i==number else '')+f'>{i}</a>' for i in range(1,len(pages)+1))
            cards=[]
            for row in items:
                text=row['description']
                if len(text)>400:text=text[:397].rsplit(' ',1)[0]+'…'
                read=f'<a href="{esc(row["guide_url"])}">Read the method</a> · ' if row.get('guide_url') else ''
                packed=row.get('pack_kind')=='skill-pack'
                download='Download skill pack' if packed else 'Download ZIP'
                entry=f'<p class="download-entry"><code>{esc(row["entry"])}</code></p>' if packed else ''
                cards.append(f'<article class="download-card"><span class="download-kind">{esc(row["kind"].replace("-"," "))}</span><h2>{esc(row["title"])}</h2><p>{esc(text)}</p><p>{read}<a href="{esc(row["url"])}">{download}</a></p>{entry}</article>')
            url='https://atlas-origins.github.io/muse-ai-agent-presets/'+route
            schema={'@context':'https://schema.org','@type':'CollectionPage','name':title,
                    'url':url,'description':intros[label],
                    'isPartOf':{'@type':'WebSite','name':'Muse Hub','url':'https://atlas-origins.github.io/muse-ai-agent-presets/'}}
            body=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | Muse Hub · {number}</title><meta name="description" content="{esc(intros[label])}">
<link rel="canonical" href="{url}"><link rel="stylesheet" href="../site.css">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body class="section-paper"><a class="skip-link" href="#main">Skip to resources</a>
<main id="main" class="shell" style="padding-block:2rem"><nav aria-label="Breadcrumb"><a href="../index.html">Muse Hub</a> / <a href="../downloads.html">Downloads</a> / {esc(label)}</nav>
<h1>{esc(title)}</h1><p>{esc(intros[label])}</p>
<p>{len(rows)} resources · Page {number} of {len(pages)} · <a href="../downloads.html?subject={quote(label)}">Search this subject</a></p>
<nav class="download-pagination" aria-label="Subject pages">{navigation}</nav>
<div class="download-grid">{''.join(cards)}</div><nav class="download-pagination" aria-label="More subject pages">{navigation}</nav>
<p><a href="../downloads.html">Explore all Muse skills, workflows and specialist kits</a></p></main></body></html>
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
                         roles=[ALIASES.get(role['id'],role['id'])]))
    for key, kind, description in (('skills', 'skill', 'trigger'), ('workflows', 'workflow', 'goal')):
        for item in sorted(collection[key], key=lambda row: (TITLES.get(row['id'],row['title']).casefold(), row['id'])):
            asset = f"muse-{kind}-{item['id']}-{version}.zip"
            pack = skill_routes[item['id']] if kind == 'skill' else {}
            if pack:
                asset = pack['asset']
                pack = {key:value for key,value in pack.items() if key!='asset'}
            original_category = (item['category'] if kind == 'skill'
                                 else skill_by_id[item['skills'][0]]['category'])
            rows.append(dict(id=item['id'], kind=kind, title=TITLES.get(item['id'],item['title']),
                             description=DESCRIPTIONS.get(item['id'],item[description]), asset=asset, url=base+asset,
                             category=subject(original_category),
                             keywords=original_category+' '+original_category.replace('-', ' '),
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
        guide_url=REPO+'/blob/main/docs/spaces/MUSE_PLANNER.md'))
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
        return match['open']+str(values[key])+match['close']
    home=re.sub(r'(?P<open><(?:strong|span) data-library-count="(?P<key>[a-z-]+)">)\d+(?P<close></(?:strong|span)>)',library_count,home)
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
    bundle_html = '\n'.join(
        f'<a class="bundle-card" href="{esc(row["url"])}"><span>{esc(row["title"])}</span><p>{esc(row["description"])}</p><strong>Download ZIP ↓</strong></a>'
        for row in data['bundles'])
    initial_items = data['items'][:DOWNLOAD_PAGE_SIZE]
    subject_links = []
    for label in data['categories']:
        count = sum(row['category'] == label for row in data['items'])
        pages = (count + 199) // 200
        for page in range(1, pages + 1):
            title = label + (f' · Page {page}' if pages > 1 else '')
            subject_links.append(f'<a href="library/{subject_slug(label)}-{page:03d}.html">{esc(title)}</a>')
    sections=[]
    for kind, heading, anchor in (('specialist','Specialists','specialists'),('skill','Skills','skills'),('workflow','Workflows','workflows'),('tool-guide','Tool guides','tool-guides')):
        cards=[]
        for row in initial_items:
            if row['kind']!=kind:continue
            description=row['description']
            if len(description)>320:
                description=description[:317].rsplit(' ',1)[0]+'…'
            search=esc(' '.join((row['title'],description,row['id'],row['category'],row.get('keywords',''))))
            read_link=f'<a class="guide-link" href="{esc(row["guide_url"])}">Read guide →</a>' if row.get('guide_url') else ''
            packed=row.get('pack_kind')=='skill-pack'
            label=f"Download skill pack · {row['pack_size']} skills" if packed else 'Download ZIP'
            hint=f'<p class="download-entry">Open <code>{esc(row["entry"])}</code> in this pack.</p>' if packed else ''
            cards.append(f'''<article class="download-card" data-id="{esc(row['id'])}" data-kind="{kind}" data-category="{esc(row['category'])}" data-roles="{esc(' '.join(row['roles']))}" data-search="{search}">
  <span class="download-kind">{esc(row['category'])}</span><h3>{esc(row['title'])}</h3><p>{esc(description)}</p>{read_link}{hint}
  <a href="{esc(row['url'])}" aria-label="Download {esc(row['title'])}{' skill pack' if packed else ' ZIP'}">{esc(label)} <span aria-hidden="true">↓</span></a>
</article>''')
        sections.append(f'<section class="download-section" data-kind="{kind}" id="{anchor}" aria-labelledby="{anchor}-heading"'+(' hidden' if not cards else '')+f'><h2 id="{anchor}-heading">{heading} <span>{data["counts"][kind]}</span></h2><div class="download-grid">'+ '\n'.join(cards)+'</div></section>')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="dark light">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'">
  <meta name="description" content="Download {data['counts']['skill']} Muse AI skills, {data['counts']['workflow']} workflows, 15 specialists and practical tool guides. Search by subject or specialist and choose a ready-to-use ZIP.">
  <link rel="canonical" href="https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Muse Hub">
  <meta property="og:url" content="https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html">
  <meta property="og:title" content="Muse AI Skills, Workflows and Specialist Downloads">
  <meta property="og:description" content="Find the skills, workflows and tools for your next task.">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Muse Hub Downloads">
  <meta name="twitter:description" content="Muse AI skills, workflows, specialists and tool guides.">
  <script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':'Muse Hub Downloads','url':'https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html','description':'Muse AI skills, workflows, specialists and tool guides.','isPartOf':{'@type':'WebSite','name':'Muse Hub','url':'https://atlas-origins.github.io/muse-ai-agent-presets/'}})}</script>
  <title>Muse AI Skills &amp; Workflow Downloads | Muse Hub</title>
{favicon}
  <link rel="stylesheet" href="site.css">
  <script defer src="downloads.js"></script>
</head>
<body id="top">
  <a class="skip-link" href="#main">Skip to downloads</a>
{header}  <main id="main">
    <section class="downloads-hero section-dark"><div class="shell">
      <span class="eyebrow signal">MUSE HUB / VERSION {esc(version.removeprefix('v'))}</span>
      <h1>Make it yours.</h1>
      <p>15 specialists. {data['counts']['skill']} skills. {data['counts']['workflow']} workflows. {data['counts']['tool-guide']} tool guides. Choose what you need, or get the collection.</p>
      <p class="downloads-start">Unzip your download and open <strong>START_HERE.md</strong>. Add the kit to your Muse conversation with the task you want to work on.</p>
      <a class="action-primary" href="#download-search">Find a skill or workflow <span aria-hidden="true">↓</span></a>
      <div class="bundle-grid">{bundle_html}</div>
      <div class="downloads-help"><a href="{REPO}/blob/main/docs/GETTING_STARTED.md">Getting started →</a><a href="{REPO}/blob/main/docs/collection/FIND_AND_BUILD.md">Build a custom pack →</a><a href="{REPO}/blob/main/docs/TERMINAL.md">Terminal guide →</a><a href="{REPO}/releases/tag/{esc(version)}">Release notes and checksums →</a></div>
    </div></section>
    <div class="downloads-catalog section-paper"><div class="shell">
      <div class="role-toolbar">
        <div class="field-wrap"><label for="download-search">Find a download</label><input id="download-search" type="search" placeholder="Try debugging, design, research…" autocomplete="off" aria-controls="download-results"></div>
        <div class="field-wrap category-wrap"><label for="download-kind">Type</label><select id="download-kind" aria-controls="download-results"><option value="all">Everything</option><option value="specialist">Specialists</option><option value="skill">Skills</option><option value="workflow">Workflows</option><option value="tool-guide">Tool guides</option></select></div>
        <div class="field-wrap category-wrap"><label for="download-role">Specialist</label><select id="download-role" aria-controls="download-results"><option value="all">All specialists</option>{''.join('<option value="'+esc(key)+'">'+esc(title)+'</option>' for key,title in data['roles'].items())}</select></div>
        <div class="field-wrap category-wrap"><label for="download-category">Subject</label><select id="download-category" aria-controls="download-results"><option value="all">All subjects</option>{''.join('<option value="'+esc(title)+'">'+esc(title)+'</option>' for title in data['categories'])}</select></div>
        <button id="download-reset" class="reset-btn" type="button">Clear</button>
      </div>
      <p id="download-count" role="status" aria-live="polite">Showing 1–{len(initial_items)} of {len(data['items'])} downloads</p>
      <nav class="download-jumps" aria-label="Download groups"><a href="#specialists">15 specialists</a><a href="#skills">{data['counts']['skill']} skills</a><a href="#workflows">{data['counts']['workflow']} workflows</a><a href="#tool-guides">{data['counts']['tool-guide']} tool guides</a></nav>
      <details class="catalog-subjects"><summary>Browse every download by subject</summary><nav class="download-jumps" aria-label="Subject library">{''.join(subject_links)}</nav></details>
      <div id="download-results" data-total="{len(data['items'])}" data-version="{esc(version)}">{''.join(sections)}</div>
      <nav id="download-pages" class="download-pagination" aria-label="Download result pages" hidden><button id="download-previous" class="reset-btn" type="button">Previous</button><span id="download-page-label"></span><button id="download-next" class="reset-btn" type="button">Next</button></nav>
      <div id="download-empty" class="role-empty" hidden><h2>No matching downloads.</h2><p>Try a shorter search or clear the filters.</p><button id="download-clear-empty" type="button">Show all downloads</button></div>
    </div></div>
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
    result.update(subject_pages(data))
    urls=['','downloads.html','public/index.html',*sorted(name for name in result if name.startswith('library/'))]
    result['sitemap.xml']=('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+
        ''.join('<url><loc>https://atlas-origins.github.io/muse-ai-agent-presets/'+name+'</loc></url>\n' for name in urls)+'</urlset>\n').encode('utf-8')
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
