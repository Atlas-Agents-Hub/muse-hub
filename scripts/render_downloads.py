#!/usr/bin/env python3
"""Render static release labels and downloads from the validated Muse collection."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
sys.path.insert(0, str(ROOT / 'scripts'))
from muse_collection import load_collection
from tool_guides import load_guides
from build_release import ALIASES, ROLE_WORKFLOWS

REPO = 'https://github.com/atlas-origins/muse-ai-agent-presets'
SITE = ROOT / 'hub/site'
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
    'inbox-triage': 'Triage Messages and Prepare Replies',
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
            original_category = (item['category'] if kind == 'skill'
                                 else skill_by_id[item['skills'][0]]['category'])
            rows.append(dict(id=item['id'], kind=kind, title=TITLES.get(item['id'],item['title']),
                             description=DESCRIPTIONS.get(item['id'],item[description]), asset=asset, url=base+asset,
                             category=subject(original_category),
                             keywords=original_category+' '+original_category.replace('-', ' '),
                             roles=memberships[key][item['id']]))
    for row in guide_catalog['guides']:
        asset=f"muse-tool-{row['id']}-{version}.zip"
        rows.append(dict(id=row['id'],kind='tool-guide',title=row['name'],description=row['summary'],
            asset=asset,url=base+asset,category=subject(row['category']),
            keywords=row['category'],roles=sorted(guide_memberships[row['id']]),
            guide_url=REPO+'/blob/main/'+row['doc_path']))
    counts = {kind: sum(row['kind'] == kind for row in rows) for kind in ('specialist','skill','workflow','tool-guide')}
    if counts['specialist']!=15 or counts['skill']<75 or counts['workflow']<25:
        raise ValueError(f'Incomplete release inventory: {counts}')
    if len({row['asset'] for row in rows}) != len(rows):
        raise ValueError('Duplicate release asset')
    bundles = []
    for slug, title, description in (
        ('specialists', 'All 15 specialists', 'Every specialist kit in one download.'),
        ('skills', f"All {counts['skill']} skills", 'The full skill library, with supporting files and practical methods.'),
        ('workflows', f"All {counts['workflow']} workflows", 'Complete workflows and the skills they use.'),
        ('starters', '100 task starters', 'Project starting points for your next task.'),
        ('specialist-toolkit', 'Python toolkit', 'Run Muse Hub tools, examples and your local notebook.'),
    ):
        asset=f'muse-{slug}-{version}.zip'
        bundles.append(dict(id=slug,title=title,description=description,asset=asset,url=base+asset))
    if counts['tool-guide']:
        asset=f'muse-tool-guides-{version}.zip'
        bundles.append(dict(id='tool-guides',title=f"{counts['tool-guide']} tool guides",description='Setup, recipes and checks for the tools that fit your work.',asset=asset,url=base+asset))
    return {'schema':'muse-hub/downloads/v1','version':version,'counts':counts,
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
        if key not in data['counts']:raise ValueError('Unknown homepage inventory count.')
        return match['open']+str(data['counts'][key])+match['close']
    home=re.sub(r'(?P<open><(?:strong|span) data-library-count="(?P<key>[a-z-]+)">)\d+(?P<close></(?:strong|span)>)',library_count,home)
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
    sections=[]
    for kind, heading, anchor in (('specialist','Specialists','specialists'),('skill','Skills','skills'),('workflow','Workflows','workflows'),('tool-guide','Tool guides','tool-guides')):
        cards=[]
        for row in data['items']:
            if row['kind']!=kind:continue
            search=esc(' '.join((row['title'],row['description'],row['id'],row['category'],row.get('keywords',''))))
            read_link=f'<a class="guide-link" href="{esc(row["guide_url"])}">Read guide →</a>' if row.get('guide_url') else ''
            cards.append(f'''<article class="download-card" data-kind="{kind}" data-category="{esc(row['category'])}" data-roles="{esc(' '.join(row['roles']))}" data-search="{search}">
  <span class="download-kind">{esc(row['category'])}</span><h3>{esc(row['title'])}</h3><p>{esc(row['description'])}</p>{read_link}
  <a href="{esc(row['url'])}" aria-label="Download {esc(row['title'])} ZIP">Download ZIP <span aria-hidden="true">↓</span></a>
</article>''')
        sections.append(f'<section class="download-section" id="{anchor}" aria-labelledby="{anchor}-heading"><h2 id="{anchor}-heading">{heading} <span>{len(cards)}</span></h2><div class="download-grid">'+ '\n'.join(cards)+'</div></section>')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="dark light">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
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
      <a class="action-primary" href="#download-search">Browse individual downloads <span aria-hidden="true">↓</span></a>
      <div class="bundle-grid">{bundle_html}</div>
      <div class="downloads-help"><a href="{REPO}/blob/main/docs/GETTING_STARTED.md">Getting started →</a><a href="{REPO}/blob/main/docs/TERMINAL.md">Terminal guide →</a><a href="{REPO}/releases/tag/{esc(version)}">Release notes and checksums →</a></div>
    </div></section>
    <div class="downloads-catalog section-paper"><div class="shell">
      <div class="role-toolbar">
        <div class="field-wrap"><label for="download-search">Find a download</label><input id="download-search" type="search" placeholder="Try debugging, design, research…" autocomplete="off" aria-controls="download-results"></div>
        <div class="field-wrap category-wrap"><label for="download-kind">Type</label><select id="download-kind" aria-controls="download-results"><option value="all">Everything</option><option value="specialist">Specialists</option><option value="skill">Skills</option><option value="workflow">Workflows</option><option value="tool-guide">Tool guides</option></select></div>
        <div class="field-wrap category-wrap"><label for="download-role">Specialist</label><select id="download-role" aria-controls="download-results"><option value="all">All specialists</option>{''.join('<option value="'+esc(key)+'">'+esc(title)+'</option>' for key,title in data['roles'].items())}</select></div>
        <div class="field-wrap category-wrap"><label for="download-category">Subject</label><select id="download-category" aria-controls="download-results"><option value="all">All subjects</option>{''.join('<option value="'+esc(title)+'">'+esc(title)+'</option>' for title in data['categories'])}</select></div>
        <button id="download-reset" class="reset-btn" type="button">Clear</button>
      </div>
      <p id="download-count" role="status" aria-live="polite">Showing {len(data['items'])} of {len(data['items'])} downloads</p>
      <nav class="download-jumps" aria-label="Download groups"><a href="#specialists">15 specialists</a><a href="#skills">{data['counts']['skill']} skills</a><a href="#workflows">{data['counts']['workflow']} workflows</a><a href="#tool-guides">{data['counts']['tool-guide']} tool guides</a></nav>
      <div id="download-results">{''.join(sections)}</div>
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
    return {'index.html':home.encode('utf-8'),
            'downloads.json':(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8'),
            'downloads.html':render(data,root,home=home).encode('utf-8')}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name,content in outputs().items():
        path=SITE/name
        if args.check:
            if not path.is_file() or path.read_bytes()!=content:stale.append(name)
        else:path.write_bytes(content)
    if stale:
        print('Downloads need regeneration: '+', '.join(stale),file=sys.stderr)
        return 1
    print('Downloads verified.' if args.check else 'Downloads updated.')
    return 0


if __name__=='__main__':raise SystemExit(main())
