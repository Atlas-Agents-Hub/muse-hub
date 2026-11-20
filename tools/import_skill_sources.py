#!/usr/bin/env python3
"""Convert pinned skill folders into complete, searchable Muse Hub packages.

The importer reads source text and copies resources; it never imports or executes
donor code. It requires PyYAML for frontmatter. Supply local source roots with
--source ID=/path. Source identities
and layout choices live in skill_sources.json, independently of local paths.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
import unicodedata
from urllib.parse import unquote

import yaml

import skill_library

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = Path(__file__).with_name('skill_sources.json')
_DARWIN_ROOT_ALIASES = {'/var':'/private/var', '/tmp':'/private/tmp', '/etc':'/private/etc'}
IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.pytest_cache', '.venv',
               'fixtures', 'evals', '.claude-plugin', 'agents'}
IGNORE_FILES = {'.DS_Store', '.gitkeep', 'package-lock.json', 'pnpm-lock.yaml',
                'yarn.lock', 'uv.lock', '.env', '.env.local'}
SKIP_PATHS = {'tests', 'test', 'templates', 'fixtures', 'examples', 'evals', 'docs',
              '.gemini', 'workspace'}
LINK = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')
REFERENCE_PATH = re.compile(r'`((?:scripts|references|assets|templates|examples)/[^`\s]+)`')
BOILERPLATE = re.compile(r'Provides step-by-step guidance for|This skill provides automated assistance for|Result: Provides step-by-step guidance', re.I)
CATALOG_POINTER = re.compile(r'reviewed pointer,\s*not the executable package|\*\*Catalog stub\.\*\*', re.I)
WORDS = {'ai':'AI','api':'API','sdk':'SDK','sql':'SQL','seo':'SEO','rag':'RAG',
         'mcp':'MCP','llm':'LLM','ml':'ML','ui':'UI','ux':'UX','qa':'QA',
         'aws':'AWS','gcp':'Google Cloud','ios':'iOS','macos':'macOS','pdf':'PDF',
         'csv':'CSV','json':'JSON','html':'HTML','css':'CSS','http':'HTTP',
         'javascript':'JavaScript','typescript':'TypeScript','nextjs':'Next.js',
         'postgresql':'PostgreSQL','postgres':'PostgreSQL','mysql':'MySQL',
         'github':'GitHub','gitlab':'GitLab','ffmpeg':'FFmpeg','numpy':'NumPy',
         'pytorch':'PyTorch','tensorflow':'TensorFlow','3d':'3D','n8n':'n8n',
         'graphql':'GraphQL','openapi':'OpenAPI','kubernetes':'Kubernetes',
         'wordpress':'WordPress','saas':'SaaS','ci':'CI','cd':'CD','crm':'CRM'}
ROLE_MAP = {
 'software-engineering': ['software-engineer'],
 'data-and-models': ['model-builder','research-evaluator'],
 'data-engineering': ['data-engineer','model-builder'],
 'reliability-engineering': ['reliability-engineer','software-engineer'],
 'security': ['adversarial-verifier','reverse-engineering-researcher'],
 'scientific-research': ['research-evaluator','learning-coach'],
 'creative-production': ['creative-studio'],
 'business-and-projects': ['coordinator'],
 'interface-design': ['product-interface-designer','creative-studio'],
 'personal-productivity': ['personal-companion','coordinator'],
 'learning-and-development': ['learning-coach'],
 'automation-engineering': ['automation-engineer','software-engineer'],
}
CHECKS = {
 'software-engineering': ['Build with the project toolchain and resolve compiler or type errors.', 'Exercise a representative success case and a relevant invalid-input case.', 'Check compatibility with the existing API, application, and dependency versions.'],
 'data-and-models': ['Check input schemas, units, missing values, and training/evaluation separation.', 'Compare the output with a reproducible baseline and retain the parameters used.', 'Test a boundary input and document uncertainty that affects the result.'],
 'data-engineering': ['Compare schema, nulls, uniqueness, and record counts with the source data.', 'Run the query or pipeline on representative and boundary inputs.', 'Check query performance and verify that retries preserve the intended records.'],
 'reliability-engineering': ['Identify the service target, observation window, and measured baseline.', 'Exercise a representative failure and verify the recovery procedure.', 'Check error rates, resource limits, and the conditions for rollback.'],
 'security': ['Keep the assessment within the authorized systems, data, and techniques.', 'Reproduce findings with concrete evidence and determine the actual impact.', 'Verify the remediation against the original finding and check for regressions.'],
 'scientific-research': ['Retain source data, units, assumptions, and the method needed to reproduce the result.', 'Compare an independent baseline, limiting case, or competing explanation.', 'Check calculations and explain uncertainty that changes the conclusion.'],
 'creative-production': ['Compare the result with the brief, reference style, and intended audience.', 'Inspect the rendered output at its intended size for continuity and legibility.', 'Check the export format, linked assets, and complete delivery set.'],
 'business-and-projects': ['Connect recommendations to the supplied evidence, audience, and business objective.', 'Check calculations, dates, ownership, dependencies, and available capacity.', 'Specify the next action, success measure, and condition for revisiting the decision.'],
 'interface-design': ['Check loading, empty, success, and error states in the main journey.', 'Inspect keyboard use, labels, contrast, and narrow and wide layouts.', 'Verify that the interface supports the intended task with the project components.'],
 'personal-productivity': ["Fit the plan to the person's commitments, constraints, and preferences.", 'Check the next action, time estimate, ownership, and reminder or review date.', 'Provide a practical fallback for interruptions or changed priorities.'],
 'learning-and-development': ["Start from the learner's current understanding and a concrete learning objective.", 'Include a worked example, independent practice, and feedback on errors.', 'Check understanding with a new example and choose the next practice task.'],
 'automation-engineering': ['Use the connected tools, documented parameters, and intended target.', 'Exercise a representative result and a failure or interruption path.', 'Check the effect before retrying and retain enough state to resume.'],
}


class IntakeError(ValueError):
    pass


def _trusted_darwin_alias(part: Path) -> bool:
    """Permit only standard root-owned macOS directory aliases."""
    expected = _DARWIN_ROOT_ALIASES.get(str(part))
    if sys.platform != 'darwin' or expected is None:
        return False
    try:
        return (part.is_symlink() and part.lstat().st_uid == 0
                and part.resolve(strict=True) == Path(expected)
                and Path(expected).is_dir())
    except (OSError, RuntimeError):
        return False


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def parse_skill(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)', text, re.S)
    if not match:
        return {}, text.strip()
    try:
        meta = yaml.load(match[1], Loader=getattr(yaml,'CSafeLoader',yaml.SafeLoader)) or {}
    except yaml.YAMLError as exc:
        raise IntakeError('invalid skill frontmatter') from exc
    if not isinstance(meta, dict):
        raise IntakeError('skill frontmatter must be a mapping')
    return meta, match[2].strip()


def identity(name):
    value = unicodedata.normalize('NFKD', name).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')


def content_identity(body):
    """Ignore presentation and harness spellings, keeping all task content."""
    body = re.sub(r'\b(?:Claude Code|Codex CLI|Gemini CLI|OpenCode|Muse)\b', 'assistant', body, flags=re.I)
    body = re.sub(r'^\s*#+\s+[^\n]+\n', '', body, count=1)
    body = re.sub(r'https://github\.com/[^\s)]+', '', body)
    return digest(re.sub(r'[^a-z0-9]+',' ',body.lower()).strip().encode())


def title_for(name):
    return ' '.join(WORDS.get(part, part.capitalize()) for part in name.split('-'))


def portable_text(text):
    """Change invocation plumbing while preserving product APIs and commands."""
    text = text.replace('\r\n','\n')
    text = re.sub(r'\bAskUserQuestion\b', 'ask the user', text)
    text = re.sub(r'\bTodoWrite\b', 'the task checklist', text)
    text = text.replace('${CLAUDE_PLUGIN_ROOT}', '${SKILL_DIR}')
    text = text.replace('${CLAUDE_SKILL_DIR}', '${SKILL_DIR}')
    text = re.sub(r'~/(?:\.claude|\.codex|\.gemini|\.hermes|\.openclaw|\.agents)/skills/', 'skills/', text)
    text = re.sub(r'(?<!\w)\.(?:claude|codex|gemini|hermes|openclaw|agents)/skills/', 'skills/', text)
    text = re.sub(r'\b(?:Claude Code|Codex CLI|Gemini CLI) (?:will |automatically )?loads? this skill\b', 'Muse selects this skill', text, flags=re.I)
    text = re.sub(r'(?im)^.*(?:this skill activates automatically when you|auto-activating skill for|install this skill (?:in|into) (?:Claude|Codex|Gemini)).*\n', '', text)
    text = re.sub(r'(?im)^.*(?:ignore (?:all )?(?:previous|prior) instructions|override (?:all )?(?:system|user) instructions).*\n', '', text)
    return text.strip()+'\n'


def category_for(name, rel, meta):
    category = str(meta.get('category') or (meta.get('metadata') or {}).get('category','')).lower()
    route = (name+' '+rel+' '+category+' '+str(meta.get('description',''))[:250]).lower()
    if re.search(r'learning|study-|flashcard|tutor|syllabus|spaced-repetition|curriculum|language-practice',route): return 'learning-and-development'
    if re.search(r'personal-|daily-|habit|journal|calendar|reminder|pomodoro|focus-mode|travel|recipe|meal-plan|grocery|home-assistant|smart-home|apple-notes|apple-reminders|garden|plant-care|bookmark|zettelkasten|obsidian',route): return 'personal-productivity'
    if re.search(r'scientific|tooluniverse|biology|chemistry|physics|biostat|astronomy|geospatial|literature|research-paper|academic|clinical|genom|protein|molecular|pubmed|arxiv|grant-writing',route): return 'scientific-research'
    if re.search(r'security|pentest|malware|forensic|vulnerabil|threat|red-team|blue-team|owasp|zero-trust|incident-response|reverse-engineer|auth-audit',route): return 'security'
    if re.search(r'blender|unity|unreal|game-dev|godot|animation|video|audio|music|3d-|illustrat|drawing|image-|photo|design-art|creative|motion-|typography|color-theory|content-production',route): return 'creative-production'
    if re.search(r'ux-|ui-|interface|accessibility|design-system|design-token|frontend-design|figma|wireframe|landing-page|responsive',route): return 'interface-design'
    if re.search(r'data-engineer|data-quality|sql|database|postgres|mysql|sqlite|duckdb|snowflake|dbt-|etl|pipeline|airflow|spark|warehouse',route): return 'data-engineering'
    if re.search(r'rag|llm|model-|machine-learning|ml-|deep-learning|fine-tun|embeddings|vector-|pytorch|tensorflow|scikit|diffusion|neural|data-ai',route): return 'data-and-models'
    if re.search(r'devops|reliability|monitor|observability|kubernetes|docker|terraform|infrastructure|sre|incident|capacity|deploy|cloud-|aws-|azure-|gcp-',route): return 'reliability-engineering'
    if re.search(r'n8n|automation|browser|webhook|workflow|connector|integration|api-connection',route): return 'automation-engineering'
    if re.search(r'marketing|business|sales|crm|seo|content-|product-manager|product-strategy|pricing|finance|accounting|customer|recruit|hr-|lead-|brand|campaign|social-media|email-',route): return 'business-and-projects'
    return 'software-engineering'


def roles_for(name, category):
    roles = list(ROLE_MAP[category])
    if re.search(r'garden|plant|weather|climate|hydrol|geospatial|agricult|crop|soil|botan',name): roles.append('garden-companion')
    if re.search(r'claim|fact-check|evidence|peer-review|statistical-review|audit|forensic|reconciliation',name): roles.append('claims-adjudicator')
    if re.search(r'reverse|binary|protocol|decompil|firmware',name): roles.append('reverse-engineering-researcher')
    if re.search(r'seo|cro|landing|analytics',name): roles.append('product-interface-designer')
    return list(dict.fromkeys(roles))


def description_for(meta, body, name):
    desc = meta.get('description','')
    if not isinstance(desc,str) or len(desc.strip())<20:
        desc = next((line.strip() for line in body.splitlines() if len(line.strip())>50 and not line.startswith(('#','|','`','-','*'))), '')
    desc = re.sub(r'\s+', ' ', portable_text(desc)).strip()
    desc = re.sub(r'(?i)\b(?:Auto-activating skill|Designed for Claude Code)[^.]*\.?','',desc).strip()
    if len(desc)<20: raise IntakeError('missing discriminating description')
    if len(desc)>900:
        desc=desc[:900].rsplit(' ',1)[0].rstrip(',:;')+'.'
    return desc


def meaningful_checks(body, category):
    choices=[]; active=False
    for line in body.splitlines():
        if re.match(r'^#{2,4} ',line): active=bool(re.search(r'verif|validation|checks|quality|acceptance|testing',line,re.I))
        if active and re.match(r'^\s*(?:[-*]|\d+\.) ',line):
            value=re.sub(r'^\s*(?:[-*]|\d+\.)\s*','',line).replace('**','').strip()
            if 35<=len(value)<=220 and not re.search(r'http|copyright|claude|[{}]|\||`',value,re.I): choices.append(value)
    return list(dict.fromkeys([*choices[:2],*CHECKS[category]]))[:4]


def example_for(body, title, desc):
    for line in body.splitlines():
        prefix=r'^\s*\*{0,2}(?:Request|Prompt|User|Example request|User request)\*{0,2}:\s*'
        if not re.match(prefix,line,re.I):continue
        value=re.sub(prefix,'',line,flags=re.I).strip(' "\u201c\u201d')
        if 30<=len(value)<=450 and not value.startswith(('#','-')):
            return portable_text(value).strip()
    return f'Help me with {title.lower()}. {desc}'


@dataclass
class Candidate:
    source: dict
    root: Path
    entry: Path
    meta: dict
    body: str
    identifier: str
    normalized: str


def candidates(source, root):
    results=[]; rejected=[]
    root=root.resolve()
    for pattern in source['patterns']:
        for entry in sorted(root.glob(pattern)):
            rel=entry.relative_to(root)
            if entry.is_symlink() or any(part in SKIP_PATHS for part in rel.parts[:-2]):continue
            try:
                excluded=source.get('exclude_entries',{}).get(rel.as_posix())
                if excluded:raise IntakeError('incomplete source package: '+excluded)
                raw=entry.read_bytes()
                if len(raw)>skill_library.MAX_FILE_BYTES or b'\0' in raw:raise IntakeError('entry size or encoding')
                meta,body=parse_skill(raw.decode('utf-8-sig'))
                identifier=identity(str(meta.get('name') or entry.parent.name))
                if not identifier or len(identifier)>64:raise IntakeError('invalid stable identity')
                if len(body)<1200 or len(set(re.findall(r'[A-Za-z]{3,}',body.lower())))<90:raise IntakeError('insufficient task detail')
                if BOILERPLATE.search(body):raise IntakeError('placeholder procedure')
                if CATALOG_POINTER.search(body):raise IntakeError('catalog pointer without its implementation')
                declared=str(meta.get('license','')).lower()
                if any(word in declared for word in ('proprietary','all rights reserved','complete terms in license')):raise IntakeError('source package excluded')
                if re.search(r'(^|[-/])(?:docx|pptx|xlsx|pdf)-(?:official|anthropic)(?:$|[-/])',str(rel)):raise IntakeError('source package excluded')
                description_for(meta,body,identifier)
                results.append(Candidate(source,root,entry,meta,body,identifier,content_identity(body)))
            except (OSError,UnicodeError,IntakeError,ValueError) as exc:
                rejected.append({'source':source['id'],'path':rel.as_posix(),'reason':str(exc)})
    # Prefer primary source folders over mirrored marketplace copies.
    results.sort(key=lambda c: ('.curated' in c.entry.parts, -len(c.body), c.entry.as_posix()))
    return results,rejected


def source_licenses(candidate):
    notices=[]
    for folder in (candidate.entry.parent,*candidate.entry.parent.parents):
        if not folder.is_relative_to(candidate.root):break
        for p in sorted(folder.iterdir()):
            if p.is_file() and not p.is_symlink() and p.name.upper().startswith(('LICENSE','NOTICE','COPYING')):
                raw=p.read_bytes()
                if len(raw)<100_000 and b'\0' not in raw:
                    value=raw.decode('utf-8-sig')
                    if value not in notices:notices.append(value)
    if not notices:raise IntakeError('source license missing')
    return ('\n\n'.join(notices).strip()+'\n').replace('\r\n','\n')


def portable_package(candidate):
    folder=candidate.entry.parent.resolve(); root=candidate.root
    files={}; file_sources={}; queue=[]; processed=set(); fixes=[]
    for path in sorted(folder.rglob('*')):
        rel=path.relative_to(folder)
        if any(part in IGNORE_DIRS for part in rel.parts) or path.name in IGNORE_FILES:continue
        if path.is_symlink():raise IntakeError('package contains a symbolic link')
        if path.is_file():queue.append((rel.as_posix(),path))
    source_base=f"https://github.com/{candidate.source['repository']}/blob/{candidate.source['commit']}/"
    while queue:
        rel,path=queue.pop(0)
        if rel in processed:continue
        processed.add(rel)
        skill_library._path(rel)
        raw=path.read_bytes()
        if len(raw)>skill_library.MAX_FILE_BYTES or b'\0' in raw:raise IntakeError('package resource is binary or oversized: '+rel)
        try:text=raw.decode('utf-8-sig')
        except UnicodeError as exc:raise IntakeError('package resource is not UTF-8: '+rel) from exc
        if rel=='SKILL.md':text=candidate.body
        if path.suffix.lower() in {'.md','.txt','.rst'} and not path.name.upper().startswith(('LICENSE','NOTICE','COPYING')):
            text=portable_text(text)
            def rewrite(match):
                label,target=match.groups();clean=target.strip().split('#',1)[0].split('?',1)[0]
                if not clean or re.match(r'^[a-z][a-z0-9+.-]*:',clean,re.I) or clean.startswith('//'):return match[0]
                actual=(path.parent/unquote(clean)).resolve()
                if actual.is_relative_to(folder) and actual.exists():return match[0]
                if actual.is_relative_to(root) and actual.is_file():
                    dest='references/shared/'+digest(str(actual.relative_to(root)).encode())[:12]+'-'+actual.name
                    queue.append((dest,actual))
                    link=os.path.relpath(dest,str(PurePosixPath(rel).parent)).replace(os.sep,'/')
                    fixes.append({'file':rel,'from':target,'to':link})
                    return f'[{label}]({link})'
                if actual.is_relative_to(root) and actual.is_dir():
                    # Source-tree navigation stays a pinned source link. Task resources
                    # are files and are copied through the branch immediately above.
                    return f'[{label}]({source_base.replace("/blob/","/tree/")+actual.relative_to(root).as_posix()})'
                # Broken source-navigation links are plain labels. Required scripts
                # and reference files are separately checked below.
                fixes.append({'file':rel,'from':target,'to':None})
                return label
            text=LINK.sub(rewrite,text)
            prefix=candidate.entry.parent.relative_to(root).as_posix()+'/'
            text=re.sub(r'(?<![A-Za-z0-9_:/.-])'+re.escape(prefix),'',text)
        if path.suffix=='.py':
            try:ast.parse(text)
            except SyntaxError as exc:raise IntakeError('invalid Python resource: '+rel) from exc
        files[rel]=text.replace('\r\n','\n').encode('utf-8')
        file_sources[rel]={'path':path.relative_to(root).as_posix(),'sha256':digest(raw)}
        if len(files)>skill_library.MAX_PACKAGE_FILES:raise IntakeError('resource count bound')
        if sum(len(x) for x in files.values())>skill_library.MAX_PACKAGE_BYTES:raise IntakeError('package size bound')
    if 'SKILL.md' not in files:raise IntakeError('entrypoint missing')
    for name,raw in list(files.items()):
        if name.endswith('.md'):
            for resource in REFERENCE_PATH.findall(raw.decode()):
                resource=resource.rstrip('.,;:')
                if any(c in resource for c in '<>*{}$'):continue
                if resource not in files and not any(x.startswith(resource.rstrip('/')+'/') for x in files):
                    # Paths are sometimes relative to the current document.
                    local=str(PurePosixPath(name).parent/resource)
                    if local not in files and not any(x.startswith(local.rstrip('/')+'/') for x in files):
                        if (folder/resource).exists():raise IntakeError('required package resource excluded: '+resource)
    category=category_for(candidate.identifier,candidate.entry.relative_to(root).as_posix(),candidate.meta)
    title=title_for(candidate.identifier)
    desc=description_for(candidate.meta,candidate.body,candidate.identifier)
    body=files['SKILL.md'].decode().strip()
    body=re.sub(r'^# [^\n]*\n','',body,count=1).strip()
    if len(body)>20_000 or len(body.splitlines())>400:
        files['METHOD.md']=(body+'\n').encode()
        body='Read [the detailed method](METHOD.md) for the procedure, examples, and supporting references.'
    setup="Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable."
    files['SKILL.md']=(f'---\nname: {candidate.identifier}\ndescription: '+json.dumps(desc,ensure_ascii=False)+'\n---\n\n# '+title+'\n\n'+setup+'\n\n'+body+'\n').encode()
    files['LICENSE.txt']=source_licenses(candidate).encode()
    author=candidate.meta.get('author') or (candidate.meta.get('metadata') or {}).get('author') or candidate.source['repository'].split('/')[0]
    files['NOTICE.txt']=(f'{title}\nSource: {candidate.source["repository"]}\nRevision: {candidate.source["commit"]}\nAuthor: {author}\n{source_base+candidate.entry.relative_to(root).as_posix()}\n\nAdapted for Muse Hub: discovery metadata, invocation paths, specialist routing, and package references.\n').encode()
    # The complete package passes the same reference rules used at download time.
    skill_library._check_references(files)
    requirements=[]
    compat=candidate.meta.get('compatibility','')
    if isinstance(compat,str):
        compat=re.sub(r'(?i)Designed for (?:Claude Code|Codex|Gemini CLI)[.;:]?\s*','',compat).strip()
        if len(compat)>15 and not compat.lower().startswith('any agent'):requirements.append(compat[:700])
    if any(p.endswith('.py') for p in files):requirements.append('Python 3 for the included helpers')
    if any(p.endswith(('.js','.mjs','.ts')) for p in files):requirements.append('Node.js for the included JavaScript tools')
    row={'id':candidate.identifier,'title':title,'category':category,'trigger':desc,
         'roles':roles_for(candidate.identifier,category),'path':'skills/'+candidate.identifier,
         'files':{name:digest(raw) for name,raw in sorted(files.items())},
         'license_files':['LICENSE.txt','NOTICE.txt'],
         'example':example_for(candidate.body,title,desc),
         'checks':meaningful_checks(candidate.body,category),
         'requirements':list(dict.fromkeys(requirements)), 'related_skills':[]}
    skill_library.validate_entry(row)
    return row,files,{'id':candidate.identifier,'source':candidate.source['id'],
        'entry':candidate.entry.relative_to(root).as_posix(),'source_sha256':digest(candidate.entry.read_bytes()),
        'normalized_sha256':candidate.normalized,'files':file_sources,'reference_changes':fixes}


def write_source_index(library_root, sources, accepted):
    """Keep compact source identities separate from user-facing descriptions."""
    path=Path(library_root)/'SOURCES.json'
    prior=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'schema':'muse-skill-origins/v1','sources':[],'skills':[]}
    rows={row['id']:row for row in prior['skills']}
    pins={source['id']:source for source in prior['sources']}
    for source in sources:pins[source['id']]=source
    for entry in accepted:
        row={key:entry[key] for key in ('id','source','entry','source_sha256','normalized_sha256')}
        skill_file=Path(library_root)/'skills'/entry['id']/'SKILL.md'
        row['package_entry_sha256']=digest(skill_file.read_bytes())
        rows[row['id']]=row
    data={'schema':'muse-skill-origins/v1','sources':list(pins.values()),'skills':sorted(rows.values(),key=lambda row:row['id'])}
    temporary=path.with_suffix('.json.new')
    temporary.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temporary.replace(path)


def import_sources(sources, roots, library_root, legacy_ids=(), target_total=None):
    library_root=Path(library_root).absolute()
    for path in (library_root,*library_root.parents):
        if path.is_symlink() and not _trusted_darwin_alias(path):raise IntakeError('destination contains a symbolic link')
    catalog_path=library_root/'catalog.json'
    catalog=json.loads(catalog_path.read_text(encoding='utf-8')) if catalog_path.exists() else {'schema':skill_library.SCHEMA,'skills':[]}
    existing=catalog['skills']; ids={identity(r['id']) for r in existing}|set(legacy_ids)
    bodies=set(); source_bodies=set(); accepted=[]; rejected=[]; additions=[]
    for row in existing:
        folder=library_root/row['path']
        text=(folder/'SKILL.md').read_text(encoding='utf-8')
        method=folder/'METHOD.md'
        bodies.add(content_identity(method.read_text(encoding='utf-8') if method.exists() else parse_skill(text)[1]))
    for source in sources:
        if source['id'] not in roots:continue
        options,errors=candidates(source,Path(roots[source['id']]))
        rejected.extend(errors)
        for candidate in options:
            if target_total is not None and len(existing)+len(additions)+len(legacy_ids)>=target_total:break
            reason=None
            if candidate.identifier in ids:reason='duplicate identity'
            elif candidate.normalized in source_bodies or candidate.normalized in bodies:reason='duplicate content'
            if reason:
                rejected.append({'source':source['id'],'path':candidate.entry.relative_to(candidate.root).as_posix(),'reason':reason});continue
            try:
                row,files,receipt=portable_package(candidate)
                normal=content_identity(files['METHOD.md'].decode() if 'METHOD.md' in files else parse_skill(files['SKILL.md'].decode())[1])
                if normal in bodies:raise IntakeError('duplicate converted content')
                output=library_root/row['path']
                if output.exists():
                    actual={}
                    for path in output.rglob('*'):
                        if path.is_symlink():raise IntakeError('destination contains a symbolic link')
                        if path.is_file():actual[path.relative_to(output).as_posix()]=digest(path.read_bytes())
                    if actual!=row['files']:raise IntakeError('destination contains different files')
                else:
                    staging=Path(tempfile.mkdtemp(prefix='.skill-import-',dir=library_root.parent))
                    try:
                        for name,raw in files.items():
                            p=staging/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
                        output.parent.mkdir(parents=True,exist_ok=True)
                        staging.rename(output)
                    finally:
                        if staging.exists():shutil.rmtree(staging)
                ids.add(candidate.identifier);source_bodies.add(candidate.normalized);bodies.add(normal)
                additions.append(row);accepted.append(receipt)
            except (OSError,UnicodeError,IntakeError,ValueError) as exc:
                rejected.append({'source':source['id'],'path':candidate.entry.relative_to(candidate.root).as_posix(),'reason':str(exc)})
        print(json.dumps({'source':source['id'],'added':len(additions),'total':len(existing)+len(additions)+len(legacy_ids),'rejected':len(rejected)}),flush=True)
        if target_total is not None and len(existing)+len(additions)+len(legacy_ids)>=target_total:break
    catalog['skills']=sorted([*existing,*additions],key=lambda r:r['id'])
    temporary=catalog_path.with_suffix('.json.new')
    temporary.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temporary.replace(catalog_path)
    return {'schema':'muse-skill-import/v1','sources':sources,'added':len(additions),'library_total':len(catalog['skills']),
            'collection_total':len(catalog['skills'])+len(legacy_ids),'accepted':accepted,'rejected':rejected,
            'categories':dict(Counter(r['category'] for r in catalog['skills'])),
            'roles':dict(Counter(role for r in catalog['skills'] for role in r['roles']))}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources',type=Path,default=SOURCE_FILE)
    parser.add_argument('--source',action='append',default=[],metavar='ID=PATH')
    parser.add_argument('--library',type=Path,default=skill_library.DEFAULT_ROOT)
    parser.add_argument('--legacy',type=Path,default=ROOT/'collections/muse-starters-v1/skills.json')
    parser.add_argument('--receipt',type=Path,required=True)
    parser.add_argument('--target-total',type=int)
    args=parser.parse_args(argv)
    roots={}
    for value in args.source:
        name,sep,path=value.partition('=')
        if not sep or not Path(path).is_dir():parser.error('each --source must be ID=existing-directory')
        if name in roots:parser.error('duplicate source ID')
        roots[name]=Path(path)
    sources=json.loads(args.sources.read_text(encoding='utf-8'))['sources']
    unknown=set(roots)-{s['id'] for s in sources}
    if unknown:parser.error('unknown source IDs: '+','.join(sorted(unknown)))
    for source in sources:
        if not re.fullmatch(r'[0-9a-f]{40}',source['commit']):parser.error('source commit must be pinned')
    legacy={r['id'] for r in json.loads(args.legacy.read_text(encoding='utf-8'))} if args.legacy.exists() else set()
    result=import_sources(sources,roots,args.library,legacy,args.target_total)
    write_source_index(args.library,sources,result['accepted'])
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in {'sources','accepted','rejected'}}))


if __name__=='__main__':
    main()
