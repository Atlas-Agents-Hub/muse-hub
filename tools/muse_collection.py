#!/usr/bin/env python3
"""Find Muse skills and compose complete specialist, skill and workflow packages."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import unicodedata
import zipfile
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_library
import workflow_library

PROJECT_LICENSE = 'MIT License\n\nCopyright (c) 2026 Muse AI Agent Presets contributors\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'

MAX_JSON_BYTES = 8_000_000
SCHEMA = 'muse-curated-collection/v1'
CORE_ROLES = ('coordinator','software-engineer','model-builder','research-evaluator',
              'creative-studio','adversarial-verifier','personal-companion',
              'garden-companion','learning-coach','claims-adjudicator',
              'reverse-engineering-researcher')
EXTENSION_ROLES = ('data-engineer','reliability-engineer','automation-engineer','product-interface-designer')
EXTENSION_ROLE_SKILLS = {
    'data-engineer': ('schema-evolution','incremental-pipeline','query-plan-review'),
    'reliability-engineer': ('service-objectives','capacity-planning','incident-triage'),
    'automation-engineer': ('automation-contract','selector-resilience','effect-reconciliation'),
    'product-interface-designer': ('design-token-audit','interaction-state-coverage'),
}
EXTENSION_SKILLS = frozenset(('schema-evolution','incremental-pipeline','query-plan-review',
    'service-objectives','capacity-planning','incident-triage','automation-contract',
    'selector-resilience','effect-reconciliation','design-token-audit','interaction-state-coverage'))
ID = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SHA = re.compile(r'^[0-9a-f]{40}$')
DEFAULT_ROOT = Path(__file__).resolve().parents[1]/'collections'/'muse-starters-v1'
# Explicit attachments follow the same dependency closure as their skill. Keep
# these independent of the legacy executable-extension role contracts.
SKILL_ASSETS = {
    'project-prioritization': ('PRIORITIZE.md','PROVENANCE.md','backlog.json','backlog.csv'),
    'daily-briefing': ('REMINDERS.md','CALENDAR_REVIEW.md'),
    'weekly-reset': ('GOAL_REVIEW.md',),
    'accessible-ui': ('SOURCE_CHECK.md','examples/clean.html','examples/review.html'),
    'inbox-triage': (
        'INBOX_WORKSPACE.md', 'SOURCE.json', 'LICENSE.txt', 'NOTICE.txt',
        'scripts/kb_reader.py', 'scripts/search_window_calculator.py',
        'scripts/draft_safety_validator.py', 'references/kb_file_contract.md',
        'references/draft_action_log.md', 'examples/Email/email-taxonomy.md',
        'examples/Email/email-patterns.md', 'examples/Email/blocklist.md',
        'examples/Email/tracker.md', 'examples/Email/triage-log/example-run.md',
    ),
}
SKILL_TOOLS = {
    'project-prioritization': 'tools/prioritize.py',
    'accessible-ui': 'tools/accessibility_check.py',
}
SKILL_RESOURCE_SECTIONS = {
    'project-prioritization': '## Score your backlog\nUse the included [prioritization calculator](PRIORITIZE.md) to compare RICE scores and choose a batch that fits each resource budget, including prerequisite work. The guide includes JSON and CSV examples.\n\n',
    'daily-briefing': '## Plan the details\nUse the [reminder worksheet](REMINDERS.md) to set up and follow through on a task. Use the [calendar review](CALENDAR_REVIEW.md) to make room for preparation, travel and focused work. Each includes a blank template and a worked example.\n\n',
    'weekly-reset': '## Review a goal\nUse the [goal review worksheet](GOAL_REVIEW.md) to connect a measurable outcome with this week\'s actions, available time and evidence of progress. Start with the blank template or follow the worked example.\n\n',
    'accessible-ui': '## Check an HTML page\nRun the included [HTML source checker](SOURCE_CHECK.md) to find missing document language, empty page titles, duplicate IDs and markup that needs a closer look. The guide includes two example pages and next steps for browser testing.\n\n',
    'inbox-triage': '## Keep inbox reviews in sync\nUse the included [inbox workspace](INBOX_WORKSPACE.md) to load your preferences, calculate the next search interval and check the action log. Three local Python helpers and a complete example workspace support first-time setup and resumed reviews.\n\n',
}

class CollectionError(ValueError):
    """Invalid content or unsafe export destination."""

def _pairs(items: list[tuple[str,Any]]) -> dict[str,Any]:
    out: dict[str,Any] = {}
    for key,value in items:
        if key in out: raise CollectionError(f'duplicate JSON key: {key}')
        out[key]=value
    return out

def _safe_path(path: Path) -> Path:
    if '..' in path.parts: raise CollectionError('parent traversal is not permitted')
    p=path.absolute()
    for part in list(reversed(p.parents))+[p]:
        try: info=part.lstat()
        except FileNotFoundError: continue
        if stat.S_ISLNK(info.st_mode):
            # Standard macOS root aliases are OS-owned, not user-controlled paths.
            trusted=(sys.platform=='darwin' and str(part) in ('/var','/tmp','/etc')
                     and info.st_uid==0 and str(part.resolve())=='/private'+str(part))
            if not trusted: raise CollectionError(f'symlink path refused: {part}')
        if getattr(info,'st_file_attributes',0) & 0x400 and not stat.S_ISLNK(info.st_mode):
            raise CollectionError(f'reparse point refused: {part}')
    return p

def read_json(path: Path) -> Any:
    try:
        p=_safe_path(Path(path))
        if not stat.S_ISREG(p.lstat().st_mode):
            raise CollectionError('JSON source is not a regular file')
        flags=os.O_RDONLY | getattr(os,'O_NONBLOCK',0) | getattr(os,'O_NOFOLLOW',0)
        with os.fdopen(os.open(p,flags),'rb') as f:
            if not stat.S_ISREG(os.fstat(f.fileno()).st_mode):
                raise CollectionError('JSON source is not a regular file')
            data=f.read(MAX_JSON_BYTES+1)
        if len(data)>MAX_JSON_BYTES: raise CollectionError('JSON source exceeds size limit')
        value=json.loads(data.decode('utf-8'),object_pairs_hook=_pairs,
                         parse_constant=lambda x: (_ for _ in ()).throw(CollectionError(f'invalid constant: {x}')))
        stack=[(value,0)]
        while stack:
            node,depth=stack.pop()
            if depth>64:raise CollectionError('JSON nesting exceeds depth limit')
            if isinstance(node,dict):stack.extend((v,depth+1) for v in node.values())
            elif isinstance(node,list):stack.extend((v,depth+1) for v in node)
        return value
    except (OSError,UnicodeError,json.JSONDecodeError,RecursionError) as e:
        raise CollectionError(f'cannot read {path}: {e}') from e

def _text(v: Any, where: str, minimum: int=1) -> str:
    if not isinstance(v,str) or len(v.strip())<minimum or len(v)>30_000:
        raise CollectionError(f'invalid text: {where}')
    if any(c in v for c in ('\x00','\u202e','\u202d','\u2066','\u2067','\u2068','\u2069')):
        raise CollectionError(f'control characters in {where}')
    return v

def _texts(v: Any, where: str, minimum: int=1) -> list[str]:
    if not isinstance(v,list) or len(v)<minimum or len(v)>100:
        raise CollectionError(f'invalid list: {where}')
    for s in v:_text(s,where)
    if len(set(v))!=len(v):raise CollectionError(f'duplicate values: {where}')
    return v

def _index(items: Any, kind: str) -> dict[str,dict[str,Any]]:
    if not isinstance(items,list) or not items or len(items)>10_000:
        raise CollectionError(f'invalid {kind} collection')
    out={}
    for x in items:
        if not isinstance(x,dict):raise CollectionError(f'{kind} record must be an object')
        key=x.get('id')
        if not isinstance(key,str) or len(key)>100 or not ID.fullmatch(key):
            raise CollectionError(f'invalid {kind} id: {key!r}')
        if key in out:raise CollectionError(f'duplicate {kind}: {key}')
        out[key]=x
    return out

def validate(data: dict[str,Any]) -> None:
    if isinstance(data,_PreparedCollection):
        return
    if not isinstance(data,dict) or data.get('schema')!=SCHEMA:
        raise CollectionError('unsupported collection schema')
    ss=_index(data.get('sources'),'source')
    sk=_index(data.get('skills'),'skill')
    st=_index(data.get('starters'),'starter')
    wf=_index(data.get('workflows'),'workflow')
    for key,s in ss.items():
        if not isinstance(s.get('revision'),str) or not SHA.fullmatch(s['revision']):
            raise CollectionError(f'unpinned source: {key}')
        repo=_text(s.get('repository'),key)
        _text(s.get('license'),f'{key}.license')
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo):
            raise CollectionError(f'invalid repository: {key}')
        if s.get('reuse') not in ('reference-only','original-synthesis','copy','adaptation'):
            raise CollectionError(f'unknown reuse policy: {key}')
        if s['reuse'] in ('copy','adaptation'):
            if s.get('license') not in ('MIT','Apache-2.0','BSD-2-Clause','BSD-3-Clause','CC0-1.0'):
                raise CollectionError(f'uncleared reuse: {key}')
            _text(s.get('notice_text'),f'{key}.notice_text',20)
        if s.get('license') in ('UNKNOWN','NOASSERTION') and s['reuse']!='reference-only':
            raise CollectionError(f'unknown-license source must be reference-only: {key}')
    bodies=set()
    for key,s in sk.items():
        if s.get('format') == 'portable-skill':
            skill_library.validate_entry(s)
            continue
        for f in ('title','category','trigger','not_for','recovery','example'):_text(s.get(f),f'{key}.{f}',12)
        first_party=(key in EXTENSION_SKILLS and s.get('origin')=='ORIGINAL_FIRST_PARTY'
                     and s.get('depth',{}).get('revision')=='R5')
        for f,n in (('inputs',2),('steps',5),('outputs',2),('checks',3),('source_ids',0 if first_party else 1)):
            _texts(s.get(f),f'{key}.{f}',n)
        if s.get('depth',{}).get('revision')=='R5' and not first_party:
            raise CollectionError('R5 skill requires explicit original first-party provenance')
        if set(s['source_ids'])-ss.keys():raise CollectionError(f'unknown source in {key}')
        if 'evaluation' in s:raise CollectionError(f'evaluation results belong in a completed run record: {key}')
        body=tuple(re.sub(r'\s+',' ',x.strip().lower()) for x in s['steps'])
        if body in bodies:raise CollectionError('duplicate skill procedure')
        bodies.add(body)
    known_guides=set()
    if any('tool_guides' in w for w in wf.values()):
        import tool_guides
        known_guides={row['id'] for row in tool_guides.load_guides()['guides']}
    for key,w in wf.items():
        if 'resources' in w:
            try:workflow_library.validate_resources(w)
            except ValueError as exc:raise CollectionError(str(exc)) from exc
        for f in ('title','goal','finish'):_text(w.get(f),f'{key}.{f}',10)
        _texts(w.get('skills'),key,2)
        if set(w['skills'])-sk.keys():raise CollectionError(f'unknown skill in workflow {key}')
        if 'steps' in w:
            if not isinstance(w['steps'],list) or len(w['steps'])<2:raise CollectionError('workflow needs connected stages')
            for stage in w['steps']:
                if not isinstance(stage,dict) or stage.get('skill_id') not in w['skills']:
                    raise CollectionError('workflow stage skill unresolved')
                _text(stage.get('title'),'workflow stage title',3)
                for field in ('action','output','check'):_text(stage.get(field),'workflow stage '+field,10)
            if set(stage['skill_id'] for stage in w['steps'])!=set(w['skills']):raise CollectionError('workflow skill missing a stage')
            _texts(w.get('inputs'),'workflow inputs',1)
            _texts(w.get('checks'),'workflow checks',2)
            _texts(w.get('roles'),'workflow roles',1)
            if set(w['roles'])-skill_library.ROLES:raise CollectionError('workflow role unresolved')
            if 'tool_guides' in w:
                _texts(w['tool_guides'],'workflow tool guides',1)
                if set(w['tool_guides'])-known_guides:raise CollectionError('workflow tool guide unresolved')
    specialist_ids=set()
    if 'specialists' in data:
        catalog=_index(data['specialists'],'specialist')
        if set(catalog)!=set(CORE_ROLES)|set(EXTENSION_ROLES):
            raise CollectionError('combined specialist inventory mismatch')
        specialist_ids=set(catalog)
        for sid,role in catalog.items():
            extension=sid in EXTENSION_ROLES
            if role.get('kind')!=('executable-extension' if extension else 'existing-specialist'):
                raise CollectionError('specialist kind mismatch')
            expected=f"presets/{sid}/"+('specialist.json' if extension else 'preset.json')
            if role.get('contract')!=expected:raise CollectionError('specialist contract path mismatch')
            _text(role.get('title'),'specialist title',5)
            _text(role.get('purpose'),'specialist purpose',20)
            _texts(role.get('skills'),'specialist skills',2)
            if set(role['skills'])-sk.keys():raise CollectionError('specialist skill unresolved')
            if extension and tuple(role['skills'])!=EXTENSION_ROLE_SKILLS[sid]:
                raise CollectionError('specialist executable-tool contract mismatch')
    if any(k in EXTENSION_SKILLS for k in sk) and not specialist_ids:
        raise CollectionError('R5 requires the combined specialist registry')
    missions=set()
    for key,p in st.items():
        for f in ('title','category','purpose','first_task','output','tone'):_text(p.get(f),f'{key}.{f}',5)
        for f,n in (('skills',2),('workflows',1),('onboarding',2),('acceptance',3)):_texts(p.get(f),f'{key}.{f}',n)
        if p.get('base_role') not in CORE_ROLES:raise CollectionError(f'unknown core role: {key}')
        if 'specialist_role' in p and (p['specialist_role'] not in EXTENSION_ROLES
                                      or p['specialist_role'] not in specialist_ids):
            raise CollectionError('unknown specialist extension: '+key)
        if p.get('automatic_external_actions') is not False:raise CollectionError(f'automatic actions not permitted: {key}')
        if set(p['skills'])-sk.keys() or set(p['workflows'])-wf.keys():raise CollectionError(f'unresolved starter reference: {key}')
        if p['first_task'] in missions:raise CollectionError('duplicate first task')
        missions.add(p['first_task'])
    cases=data.get('evaluation_cases')
    authored_skills={key for key,row in sk.items() if row.get('format')!='portable-skill'}
    if not isinstance(cases,list) or len(cases)!=len(authored_skills):raise CollectionError('one practice case per authored skill is required')
    if not all(isinstance(x,dict) for x in cases):raise CollectionError('evaluation case must be an object')
    if len({x.get('skill_id') for x in cases})!=len(cases):raise CollectionError('duplicate evaluation case')
    for c in cases:
        if c.get('skill_id') not in sk:raise CollectionError('unknown evaluation skill')
        for f in ('task','negative_case'):_text(c.get(f),f'case.{f}',10)
        _texts(c.get('rubric'),'case.rubric',3)
        if 'results' in c:raise CollectionError('practice definitions cannot contain run results')
    _validate_depth(data,ss,sk)

def _validate_depth(data: dict[str,Any], sources: dict[str,Any], skills: dict[str,Any]) -> None:
    deep={k:v for k,v in skills.items() if v.get('depth') is not None}
    raw=data.get('depth_cases',[])
    if not deep:
        if raw: raise CollectionError('depth cases without depth skills')
        return
    cases=_index(raw,'depth case')
    seen=set()
    for key,s in deep.items():
        d=s['depth']
        if not isinstance(d,dict) or d.get('schema')!='muse-skill-depth/v1':
            raise CollectionError('invalid depth schema: '+key)
        for name,fields in [('decisions',('when','do','avoid')),
                            ('failure_modes',('symptom','cause','repair','recheck'))]:
            rows=d.get(name)
            if not isinstance(rows,list) or not 3<=len(rows)<=20:
                raise CollectionError('missing depth '+name+': '+key)
            for row in rows:
                if not isinstance(row,dict): raise CollectionError('invalid depth row')
                for f in fields:_text(row.get(f),key+'.'+name+'.'+f,10)
        if d.get('revision') in ('R3','R4','R5'):
            for f in ('domain_method','output_contract'):_text(d.get(f),key+'.'+f,50)
            if 'comparison_result' in d:raise CollectionError('method definitions cannot contain comparison results')
            extra=d.get('additional_examples')
            if not isinstance(extra,list) or not 1<=len(extra)<=5:raise CollectionError('missing R3 edge example')
            for item in extra:
                if not isinstance(item,dict):raise CollectionError('invalid R3 example')
                for f in ('input','method','result'):_text(item.get(f),key+'.edge.'+f,20)
            if len(d['decisions'])<5:raise CollectionError('R3 requires five meaningful decisions')
        example=d.get('worked_example')
        if not isinstance(example,dict):raise CollectionError('missing worked example')
        for f in ('input','method','result'):_text(example.get(f),key+'.example.'+f,20)
        for f in ('handoff','practice_scope'):_text(d.get(f),key+'.'+f,20)
        _texts(d.get('case_ids'),key+'.case_ids',3)
        refs=d.get('upstream_items')
        own=(d.get('revision')=='R5' and key in EXTENSION_SKILLS and s.get('origin')=='ORIGINAL_FIRST_PARTY')
        if not isinstance(refs,list) or (not refs and not own):raise CollectionError('missing item references')
        if own and (refs or s['source_ids']):raise CollectionError('original R5 provenance cannot imply unreviewed upstream attribution')
        for ref in refs:
            if not isinstance(ref,dict) or ref.get('source_id') not in sources:
                raise CollectionError('unknown depth source')
            if ref.get('revision')!=sources[ref['source_id']]['revision']:
                raise CollectionError('depth source revision mismatch')
            path=_text(ref.get('path'),'reference path')
            if path.startswith(('/', '\\')) or '..' in path.split('/'):
                raise CollectionError('invalid depth reference path')
            if ref.get('disposition')!='REFERENCE_ONLY_NO_COPY':
                raise CollectionError('unreviewed upstream copying refused')
        for cid in d['case_ids']:
            if cid in seen or cid not in cases or cases[cid].get('skill_id')!=key:
                raise CollectionError('depth case reference mismatch: '+cid)
            seen.add(cid)
    if seen!=cases.keys():raise CollectionError('orphan depth case')
    for cid,c in cases.items():
        _text(c.get('request'),cid+'.request',50)
        _texts(c.get('review_rubric'),cid+'.review_rubric',3)
        for f in ('inputs','reference_output','wrong_output'):
            if not isinstance(c.get(f),dict) or not c[f]:raise CollectionError('missing concrete '+f)
        if c.get('status')!='PUBLIC_REGRESSION_CASE_NOT_MODEL_RESULT' or c.get('model_results') is not None:
            raise CollectionError('fixture falsely promoted to model result')
        if c['reference_output']==c['wrong_output']:raise CollectionError('negative exercise is not discriminating')

def load_collection(root: Path=DEFAULT_ROOT) -> dict[str,Any]:
    d={'schema':SCHEMA}
    for key in ('sources','skills','starters','workflows','evaluation_cases'):
        d[key]=read_json(Path(root)/f'{key}.json')
    if (Path(root)/'depth_cases.json').exists():
        d['depth_cases']=read_json(Path(root)/'depth_cases.json')
    if (Path(root)/'specialists.json').exists():d['specialists']=read_json(Path(root)/'specialists.json')
    library_root=Path(root).parent/'library'
    if (library_root/'catalog.json').exists():
        try:
            additions=skill_library.collection_entries(library_root)
        except ValueError as exc:
            raise CollectionError(str(exc)) from exc
        d['skills'].extend(additions)
        d['_library_root']=str(library_root)
        extra_workflows=library_root/'workflows.json'
        if extra_workflows.exists():
            extra=read_json(extra_workflows)
            if (not isinstance(extra,dict) or set(extra)!={'schema','workflows'}
                or extra['schema']!='muse-skill-workflows/v1'
                or not isinstance(extra['workflows'],list)):
                raise CollectionError('unsupported skill workflow catalog')
            d['workflows'].extend(extra['workflows'])
        for role in d.get('specialists',[]):
            role['library_skills']=[s['id'] for s in additions if role['id'] in s['roles']]
            role['library_workflows']=[w['id'] for w in d['workflows'] if role['id'] in w.get('roles',[])]
    validate(d)
    return d

def _list(lines: list[str]) -> str:return '\n'.join('- '+s for s in lines)

OPERATING_RULES = '''## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.
'''

def render_skill(s: dict[str,Any], sources: dict[str,dict[str,Any]], *, include_local_tools: bool=True) -> str:
    if s.get('format')=='portable-skill':
        return skill_library.package_files(s)[s['path']+'/SKILL.md'].decode('utf-8')
    refs='\n'.join(f"- {sources[k]['repository']} @ `{sources[k]['revision']}` ({sources[k]['license']}; {sources[k]['reuse']})" for k in s['source_ids'])
    if not refs and s.get('origin')=='ORIGINAL_FIRST_PARTY':
        refs='Original procedure and Python tool; see the included examples and practice cases.'
    steps='\n'.join(f'{i}. {x}' for i,x in enumerate(s['steps'],1))
    deeper=('## Go deeper\nRead [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.\n\n' if s.get('depth') else '')
    local_tool=SKILL_RESOURCE_SECTIONS.get(s['id'],'') if include_local_tools else ''
    return (f"---\nname: {s['id']}\ndescription: {json.dumps(s['trigger'],ensure_ascii=False)}\n---\n\n# {s['title']}\n\n"
            f"## Use when\n{s['trigger']}\n\n## Not for\n{s['not_for']}\n\n## Inputs\n{_list(s['inputs'])}\n\n"
            f"## Procedure\n{steps}\n\n## Deliver\n{_list(s['outputs'])}\n\n## Check the result\n{_list(s['checks'])}\n\n"
            f"## Recover or narrow\n{s['recovery']}\n\n## Example request\n{s['example']}\n\n"
            f"{OPERATING_RULES}\n{local_tool}{deeper}")

def render_depth(s: dict[str,Any], *, include_example: bool=True) -> str:
    d=s['depth'];lines=[f"# {s['title']} — examples and decisions",'',
        'Choose the branch that fits the current task, then use its result checks.','',
        '## Choose the right action','']
    if d.get('domain_method'):
        # Insert expertise before conditional procedures without changing R2 output.
        lines[-2:-2]=['## Domain method','',d['domain_method'],'','## Output contract','',d['output_contract'],'']
    for row in d['decisions']:
        lines += ['### '+row['when'],row['do'],'', '**Avoid:** '+row['avoid'],'']
    ex=d['worked_example']
    if include_example:
        lines += ['## Worked example','','**Input:** '+ex['input'],'',
                  '**Method:** '+ex['method'],'','**Result:** '+ex['result'],'']
    if include_example:
        for index,item in enumerate(d.get('additional_examples',[]),1):
            lines += [f'## Edge or recovery example {index} (example)','',
                      '**Input:** '+item['input'],'','**Method:** '+item['method'],'',
                      '**Result:** '+item['result'],'']
    lines += ['## Failure diagnosis','']
    for row in d['failure_modes']:
        lines += ['### '+row['symptom'],'**Likely cause:** '+row['cause'],'',
                  '**Repair:** '+row['repair'],'','**Recheck:** '+row['recheck'],'']
    lines += ['## Preserve for the next turn','',d['handoff'],'']
    if include_example:
        lines += ['## Practice and mechanical checks','',d['practice_scope'],'',
                  'Practice case IDs: '+', '.join('`'+x+'`' for x in d['case_ids'])+'.',
                  'Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.','']
    return '\n'.join(lines)

RUN_PROTOCOL = """# Matched task protocol
Use separate fresh contexts for plain Muse, the pinned upstream skill package, and this candidate. Keep the same observed model setting, supplied inputs, connected tools, observed memory mode and budget. Hash only the supplied context pack as supplied_context_sha256; do not claim to hash hidden provider memory or instructions. Unavoidable hidden context differences remain a limitation. Record a specific model/version only when actually exposed. If Muse does not disclose the underlying model, use model_visibility=managed-opaque, model=null and the observed visible_model_setting; report a host-matched comparison, not proof of identical underlying model weights. A hidden sampling setting is recorded with temperature_visibility=managed-opaque and temperature=null, never a made-up number. Time and output budgets are requested test limits unless actual enforcement is observed. No independent assistant installation or internal provider-event access is required. Retain raw outputs and failures; do not silently drop cases. Record randomized order before running. Load all dependencies the upstream package actually requires; missing references make that arm unqualified, not a competitor failure.

TASK.json is identical in every arm. Do not give the participant authored expected answers, negative examples, evaluator oracles, or another arm's outputs. The skill's worked example is development material, not a hidden holdout. These task cases are PUBLIC regression cases. Use separately authored unseen cases and independent review before claiming broad superiority.

The returned artifact and the requested structured output are both required. Mechanical checks cover closed facts and declared scope; a human reviews usefulness, fidelity, reasoning and presentation. The metadata checker cannot attest a provider or prove that a run occurred. No automatic model, scheduler, send, purchase, installation or paid API is started by this packet.
"""

def challenge_files(data: dict[str,Any], case_id: str, arm: str) -> dict[str,bytes]:
    validate(data)
    if arm not in ('plain','upstream','candidate'):raise CollectionError('unknown comparison arm')
    case=next((x for x in data.get('depth_cases',[]) if x['id']==case_id),None)
    if case is None:raise CollectionError('unknown concrete case: '+case_id)
    skill=next(s for s in data['skills'] if s['id']==case['skill_id'])
    if arm=='upstream' and not skill['depth']['upstream_items']:
        raise CollectionError('original first-party skill has no admitted upstream comparator; use plain and candidate arms')
    # Positive allowlist: internal answer fields cannot leak by adding new metadata.
    task={k:case[k] for k in ('id','skill_id','request','inputs')}
    files={'TASK.json':(json.dumps(task,indent=2,ensure_ascii=False)+'\n').encode(),
           'RUN_PROTOCOL.md':RUN_PROTOCOL.encode()}
    if arm=='candidate':
        files[f"skills/{skill['id']}/SKILL.md"]=render_skill(skill,{s['id']:s for s in data['sources']},include_local_tools=False).encode()
        files[f"skills/{skill['id']}/DEPTH.md"]=render_depth(skill,include_example=False).encode()
    if arm=='upstream':
        files['UPSTREAM_REFERENCE.json']=(json.dumps(skill['depth']['upstream_items'],indent=2)+'\n').encode()
    return files

def render_profile(p: dict[str,Any]) -> str:
    return (f"# {p['title']}\n\n{p['purpose']}\n\nSpecialist family: **{p['base_role']}**. Voice: {p['tone']}\n\n" +
            (f"Specialist extension: **{p['specialist_role']}**.\n\n" if p.get('specialist_role') else '') +
            f"## Set up only what is missing\n{_list(p['onboarding'])}\n\n## First task\n{p['first_task']}\n\n"

            f"## Expected result\n{p['output']}\n\n## Acceptance\n{_list(p['acceptance'])}\n\n"
            f"## Selected skills\n{_list(p['skills'])}\n\n## Optional workflow recipes\n{_list(p['workflows'])}\n\nUse a recipe only when it fits the current request. Do not force unrelated steps into a one-off task; start with the selected skills above.\n\n{OPERATING_RULES}")

def render_workflow(w: dict[str,Any], skills: dict[str,dict[str,Any]]) -> str:
    steps='\n'.join(f"{i}. **{skills[k]['title']}** — load `skills/{k}/SKILL.md`, then carry the previous step's output forward." for i,k in enumerate(w['skills'],1))
    body=f"# {w['title']}\n\n{w['goal']}\n\n{steps}\n\n## Finish\n{w['finish']}\n"
    if w.get('steps'):
        body=f"# {w['title']}\n\n{w['goal']}\n"
        if w.get('inputs'):body+='\n## Bring these inputs\n\n'+_list(w['inputs'])+'\n'
        for index,stage in enumerate(w['steps'],1):
            key=stage['skill_id']
            body+=f"\n## {index}. {stage['title']}\n\nRead [the {skills[key]['title']} method](../skills/{key}/SKILL.md). {stage['action']}\n\n"
            body+='**Carry forward:** '+stage['output']+'\n\n**Check:** '+stage['check']+'\n'
        if w.get('checks'):body+='\n## Check the finished work\n\n'+_list(w['checks'])+'\n'
        body+='\n## Finish\n\n'+w['finish']+'\n'
    if w.get('tool_guides'):
        body+='\n## Tools for this workflow\n\nRead [the included tool guides](../TOOL_GUIDES.md) when a stage calls for those tools.\n'
    if w.get('resources'):
        key=w['id']
        body+='\n## Workflow files\n\n'
        body+=f'Open [WORKFLOW.json]({key}/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. '
        body+=f'Fill [INPUTS.json]({key}/INPUTS.json) with your selected sources, destinations, connections, and model capability. '
        body+='Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.\n'
        body+='\nModel and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. '
        body+='An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. '
        body+='Check a representative input before continuing through a batch or a loop.\n'
        body+='\nInspect the dependency order and required connections from the extracted package folder:\n\n'
        body+=f'```sh\npython -B tools/workflow_graph.py workflows/{key}/WORKFLOW.json\n```\n'
    if w.get('tool_bindings'):
        body+='\n## Included local tools\n\nRun the included examples from the extracted package folder:\n\n```sh\npython -B tools/run.py --demo\n```\n\n'
        body+='For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.\n\n'
        body+='\n'.join('- `'+b['skill_id']+'`: carry its returned JSON into the next relevant step.' for b in w['tool_bindings'])
        body+='\n\n## Input artifacts\n'+_list(w['input_contract'])+'\n\n## Output artifacts\n'+_list(w['output_contract'])+'\n'
    return body


class _FrozenDict(dict):
    def _readonly(self,*args,**kwargs):raise TypeError('prepared collection is immutable')
    __setitem__=__delitem__=clear=pop=popitem=setdefault=update=__ior__=_readonly


class _FrozenList(list):
    def _readonly(self,*args,**kwargs):raise TypeError('prepared collection is immutable')
    __setitem__=__delitem__=append=clear=extend=insert=pop=remove=reverse=sort=__iadd__=__imul__=_readonly


def _freeze(value):
    if isinstance(value,dict):return _FrozenDict({key:_freeze(item) for key,item in value.items()})
    if isinstance(value,list):return _FrozenList(_freeze(item) for item in value)
    return value


class _PreparedCollection(_FrozenDict):
    def __init__(self,data):
        validate(data)
        dict.__init__(self,{key:_freeze(item) for key,item in data.items()})


def prepare_collection(data: dict[str,Any]) -> dict[str,Any]:
    """Validate and freeze metadata once for a batch of package builds.

    Source files are still read and checked against their declared hashes for
    every package. The snapshot owns its nested lists and mappings, so editing
    the original catalog cannot change an in-progress release.
    """
    return data if isinstance(data,_PreparedCollection) else _PreparedCollection(data)


def instruction_files(data: dict[str,Any], skill_ids: list[str], workflow_ids: list[str]) -> dict[str,bytes]:
    """Compose instruction dependencies once for starters, roles and individual downloads."""
    validate(data)
    skills={s['id']:s for s in data['skills']}
    workflows={w['id']:w for w in data['workflows']}
    sources={s['id']:s for s in data['sources']}
    if any(k not in skills for k in skill_ids) or any(k not in workflows for k in workflow_ids):
        raise CollectionError('unknown instruction dependency')
    chosen=set(skill_ids)
    for key in workflow_ids:chosen.update(workflows[key]['skills'])
    if not chosen:raise CollectionError('instruction package requires at least one skill')
    files={};depth_ids=set()
    for key in sorted(chosen):
        if skills[key].get('format')=='portable-skill':
            files.update(skill_library.package_files(skills[key],data.get('_library_root',skill_library.DEFAULT_ROOT)))
            continue
        files[f'skills/{key}/SKILL.md']=render_skill(skills[key],sources).encode()
        if skills[key].get('depth'):
            files[f'skills/{key}/DEPTH.md']=render_depth(skills[key]).encode()
            depth_ids.update(skills[key]['depth']['case_ids'])
    if depth_ids:
        files['practice/check_outputs.py']=_bounded_source(DEFAULT_ROOT/'depth'/'check_outputs.py',200000)
        if any(skills[k].get('depth',{}).get('revision')=='R4' for k in chosen):
            files['practice/r4_checks.py']=_bounded_source(DEFAULT_ROOT/'r4'/'r4_checks.py')
        if any(skills[k].get('depth',{}).get('revision')=='R5' for k in chosen):
            files['practice/r5_checks.py']=_bounded_source(DEFAULT_ROOT/'r5'/'r5_checks.py')
            for name,raw in _extension_sources().items():files['practice/'+name]=raw
        cases=[c for c in data['depth_cases'] if c['id'] in depth_ids]
        if {c['id'] for c in cases}!=depth_ids:raise CollectionError('missing practice dependency')
        for case in cases:
            files['practice/'+case['id']+'.json']=(json.dumps(case,indent=2,ensure_ascii=False)+'\n').encode()
            files['practice/answers/'+case['id']+'.json']=(json.dumps(case['reference_output'],indent=2,ensure_ascii=False)+'\n').encode()
        first=sorted(depth_ids)[0]
        files['practice/README.md']=(f'# Practice examples\n\nTry a supplied case, then check its structured result. From the package folder, run:\n\n```sh\npython -B practice/check_outputs.py check --case practice/{first}.json --output practice/answers/{first}.json\n```\n\nUse your own response file with `--output` when practicing. Review reasoning and visual quality alongside the mechanical checks.\n').encode()
    for key in workflow_ids:
        files[f'workflows/{key}.md']=render_workflow(workflows[key],skills).encode()
        if workflows[key].get('resources'):
            try:files.update(workflow_library.package_files(workflows[key],data.get('_library_root',workflow_library.ROOT)))
            except (ValueError,OSError) as exc:raise CollectionError(str(exc)) from exc
            files.setdefault('tools/workflow_graph.py',_bounded_source(Path(__file__).with_name('workflow_library.py')))
    selected_guides={guide for key in workflow_ids for guide in workflows[key].get('tool_guides',[])}
    if selected_guides:
        import tool_guides
        files.update(tool_guides.package_files(tool_guides.load_guides(),ids=selected_guides))
    files['PRACTICE.json']=(json.dumps([{k:v for k,v in c.items() if k!='results'} for c in data['evaluation_cases'] if c['skill_id'] in chosen],indent=2,ensure_ascii=False)+'\n').encode()
    if chosen & EXTENSION_SKILLS:files.update(_local_tool_files(data,chosen & EXTENSION_SKILLS))
    for key in sorted(chosen):
        if key in SKILL_TOOLS:
            name=SKILL_TOOLS[key]
            files[name]=_bounded_source(DEFAULT_ROOT.parents[1]/name)
        for name in SKILL_ASSETS.get(key,()):
            files['skills/'+key+'/'+name]=_bounded_source(DEFAULT_ROOT/'skills'/key/name)
    return files


def resource_start_guide(files: dict[str,bytes]) -> str:
    """Expose only resources actually present in this extracted package."""
    parts=[]
    worksheets=(('skills/daily-briefing/REMINDERS.md','Set up and manage a reminder'),
        ('skills/daily-briefing/CALENDAR_REVIEW.md','Review your calendar'),
        ('skills/weekly-reset/GOAL_REVIEW.md','Review a goal and choose the next action'))
    available=[(path,title) for path,title in worksheets if path in files]
    if available:
        parts.append('\n## Plan your week\n\nCopy a blank worksheet, or use its filled example to get started:\n\n'+
            '\n'.join('- ['+title+']('+path+')' for path,title in available)+'\n')
    if 'tools/prioritize.py' in files:
        parts.append('\n## Choose a batch of work\n\nCompare RICE scores and fit prerequisite work into your resource budgets. With Python 3.10 or newer, run:\n\n'
            '    python -B tools/prioritize.py --input skills/project-prioritization/backlog.json\n\n'
            'See [the calculator guide](skills/project-prioritization/PRIORITIZE.md) for your own JSON or CSV backlog.\n')
    if 'tools/accessibility_check.py' in files:
        parts.append('\n## Check an HTML page\n\nWith Python 3.10 or newer, try the included example:\n\n'
            '    python -B tools/accessibility_check.py --input skills/accessible-ui/examples/clean.html\n\n'
            'Read [the HTML source checker guide](skills/accessible-ui/SOURCE_CHECK.md) for your own pages and browser checks.\n')
    if 'skills/inbox-triage/scripts/kb_reader.py' in files:
        parts.append('\n## Review your inbox\n\nUse the [inbox workspace guide](skills/inbox-triage/INBOX_WORKSPACE.md) to prepare preferences, resume from the last completed interval and check draft operations. Try the included workspace with Python 3.10 or newer:\n\n'
            '    python -B skills/inbox-triage/scripts/kb_reader.py --workspace skills/inbox-triage/examples --output json\n')
    return ''.join(parts)


def package_files(data: dict[str,Any], starter_id: str) -> dict[str,bytes]:
    validate(data)
    starters={p['id']:p for p in data['starters']}
    if starter_id not in starters:raise CollectionError(f'unknown starter: {starter_id}')
    p=starters[starter_id]
    files=instruction_files(data,p['skills'],p['workflows'])
    files.update({'LICENSE':PROJECT_LICENSE.encode(),'PROFILE.md':render_profile(p).encode(),
        'START_HERE.md':(f"# Use {p['title']} with Muse\n\nGive this ZIP or its extracted folder to your current Muse assistant. Say: ‘Read PROFILE.md and use the relevant skills for my current task, keeping my existing preferences and memory.’\n\nStart with your own request or the example in PROFILE.md. Load a workflow when it fits the task. You can use all Markdown instructions without Python. Optional local commands state their requirements alongside the command.\n").encode()})
    files['START_HERE.md']+=resource_start_guide(files).encode()
    chosen=sorted(name.split('/')[1] for name in files if name.startswith('skills/') and name.endswith('/SKILL.md'))
    manifest={'schema':'muse-starter-pack/v1','starter':starter_id,'base_role':p['base_role'],'skills':chosen,
              'files':{k:hashlib.sha256(v).hexdigest() for k,v in sorted(files.items())}}
    files['MANIFEST.json']=(json.dumps(manifest,sort_keys=True,indent=2)+'\n').encode()
    return files


def build_bytes(data: dict[str,Any], starter_id: str) -> bytes:
    return build_file_map_bytes(package_files(data,starter_id))

def build_file_map_bytes(files: dict[str,bytes], *, max_files: int = 12000,
                         max_member_bytes: int = 8_000_000,
                         max_total_bytes: int = 160_000_000) -> bytes:
    # Package data may be supplied by library callers, not only our CLI builder.
    # Refuse names that extract differently across POSIX and Windows.
    if (type(max_files) is not int or not 1 <= max_files <= 60000
            or type(max_member_bytes) is not int or not 1 <= max_member_bytes <= 512_000_000
            or type(max_total_bytes) is not int or not 1 <= max_total_bytes <= 1_000_000_000):
        raise CollectionError('invalid archive resource budget')
    if not isinstance(files,dict) or not 1<=len(files)<=max_files:
        raise CollectionError('archive requires a bounded roster of regular file entries')
    normalized=set();total=0
    reserved={'con','prn','aux','nul',*(f'com{i}' for i in range(1,10)),*(f'lpt{i}' for i in range(1,10))}
    for name,content in files.items():
        if not isinstance(name,str) or not name or len(name)>400 or not name.isascii():
            raise CollectionError('invalid portable archive name')
        if any(ord(c)<32 or ord(c)==127 or c in '\\:*?"<>|' for c in name):
            raise CollectionError('unsafe archive name')
        parts=name.split('/')
        if any(not x or x in ('.','..') or x.endswith((' ','.')) or
               x.split('.')[0].lower() in reserved for x in parts):
            raise CollectionError('unsafe archive path component')
        key=unicodedata.normalize('NFC',name).casefold()
        if key in normalized:raise CollectionError('cross-platform archive name collision')
        normalized.add(key)
        if not isinstance(content,bytes) or len(content)>max_member_bytes:
            raise CollectionError('archive content must be bounded bytes')
        total+=len(content)
        if total>max_total_bytes:raise CollectionError('archive uncompressed size budget exceeded')
    for name in normalized:
        parts=name.split('/')
        if any('/'.join(parts[:i]) in normalized for i in range(1,len(parts))):
            raise CollectionError('archive file/directory collision')
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,content in sorted(files.items()):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,content)
    return out.getvalue()

def write_new_pack(path: Path, content: bytes) -> None:
    try:
        p=_safe_path(Path(path))
        if not p.parent.is_dir():raise CollectionError('output parent must already exist')
        with p.open('xb') as f:
            f.write(content);f.flush();os.fsync(f.fileno())
    except OSError as e:raise CollectionError(f'cannot create new output: {e}') from e


def _bounded_source(path: Path, limit: int=250000) -> bytes:
    p=_safe_path(path)
    flags=os.O_RDONLY|getattr(os,'O_NOFOLLOW',0)|getattr(os,'O_NONBLOCK',0)
    with os.fdopen(os.open(p,flags),'rb') as stream:
        info=os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size>limit:raise CollectionError('unsafe source member')
        raw=stream.read(limit+1)
    if len(raw)>limit:raise CollectionError('source member too large')
    return raw


def _extension_sources() -> dict[str,bytes]:
    root=Path(__file__).resolve().parents[1]/'src'/'muse_presets'/'specialist_extensions'
    names=('__init__.py','common.py','data.py','reliability.py','automation.py','interface.py')
    return {'specialist_extensions/'+name:_bounded_source(root/name) for name in names}


def _extension_contract(data: dict[str,Any], role_id: str) -> tuple[dict,dict]:
    validate(data)
    if role_id not in EXTENSION_ROLES:raise CollectionError('unknown executable specialist extension')
    role=next((r for r in data.get('specialists',[]) if r['id']==role_id),None)
    if role is None:raise CollectionError('specialist registry entry absent')
    root=Path(__file__).resolve().parents[1]
    contract=read_json(root/'presets'/role_id/'specialist.json')
    if (contract.get('schema')!='muse-specialist-extension/v1' or contract.get('id')!=role_id
        or contract.get('skills')!=role['skills']):
        raise CollectionError('specialist contract mismatch')
    example=read_json(root/'presets'/role_id/'example.json')
    if (example.get('specialist')!=role_id or not isinstance(example.get('jobs'),list)
        or not 2<=len(example['jobs'])<=12):raise CollectionError('specialist example invalid')
    if set(j.get('skill_id') for j in example['jobs'])!=set(role['skills']):
        raise CollectionError('specialist example tool coverage mismatch')
    return contract,example


def specialist_demo(data: dict[str,Any], role_id: str) -> dict:
    contract,example=_extension_contract(data,role_id)
    source=Path(__file__).resolve().parents[1]/'src'
    if str(source) not in sys.path:sys.path.insert(0,str(source))
    from muse_presets.specialist_extensions import evaluate
    from muse_presets.specialist_extensions.common import canonical
    results=[]
    for job in example['jobs']:
        result=evaluate(job['skill_id'],job['inputs'])
        results.append({'skill_id':job['skill_id'],
            'input_sha256':hashlib.sha256(canonical(job['inputs']).encode()).hexdigest(),'output':result})
    return {'specialist':role_id,'results':results,'status':'EXAMPLES_COMPLETED'}


def workflow_demo(data: dict[str,Any], workflow_id: str) -> dict:
    validate(data)
    workflow=next((w for w in data['workflows'] if w['id']==workflow_id),None)
    if workflow is None or not workflow.get('tool_bindings'):
        raise CollectionError('workflow has no registered local-stage demonstration')
    source=Path(__file__).resolve().parents[1]/'src'
    if str(source) not in sys.path:sys.path.insert(0,str(source))
    from muse_presets.specialist_extensions import evaluate
    from muse_presets.specialist_extensions.common import canonical
    results=[]
    for binding in workflow['tool_bindings']:
        sid=binding['skill_id']
        if (sid not in workflow['skills'] or sid not in EXTENSION_SKILLS
            or binding.get('module')!='muse_presets.specialist_extensions' or binding.get('function')!='evaluate'):
            raise CollectionError('workflow tool binding mismatch')
        case=next(c for c in data['depth_cases'] if c['id']==sid+'-r5-standard')
        # The tool boundary accepts plain JSON, while a prepared catalog owns
        # immutable metadata. Copy only this trusted example for evaluation.
        inputs=(json.loads(json.dumps(case['inputs'],allow_nan=False))
                if isinstance(data,_PreparedCollection) else case['inputs'])
        results.append({'skill_id':sid,'case_id':case['id'],
            'input_sha256':hashlib.sha256(canonical(inputs).encode()).hexdigest(),
            'output':evaluate(sid,inputs)})
    executed={r['skill_id'] for r in results}
    return {'workflow':workflow_id,'results':results,
        'unexecuted_skills':[s for s in workflow['skills'] if s not in executed],
        'status':'EXAMPLES_COMPLETED'}



LOCAL_TOOL_RUNNER = "\"\"\"Run the local calculations included with this package.\"\"\"\nfrom __future__ import annotations\nimport argparse, hashlib, json, os, re, stat, sys\nfrom pathlib import Path, PurePosixPath\nsys.dont_write_bytecode = True\nMAX_BYTES = 2_000_000\n\ndef read_json(path):\n    if path.is_symlink() or (getattr(path.lstat(), 'st_file_attributes', 0) & 0x400):\n        raise ValueError('LINKED_INPUT_REFUSED')\n    with path.open('rb') as stream:\n        info = os.fstat(stream.fileno())\n        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:\n            raise ValueError('BOUNDED_REGULAR_INPUT_REQUIRED')\n        raw = stream.read(MAX_BYTES + 1)\n    def pairs(rows):\n        result = {}\n        for key, value in rows:\n            if key in result: raise ValueError('DUPLICATE_JSON_KEY')\n            result[key] = value\n        return result\n    def reject(value): raise ValueError('NONFINITE_JSON_NUMBER')\n    return json.loads(raw.decode('utf-8'), object_pairs_hook=pairs, parse_constant=reject)\n\ndef main():\n    parser = argparse.ArgumentParser(description='Use an included local tool with JSON input.')\n    modes = parser.add_mutually_exclusive_group(required=True)\n    modes.add_argument('--demo', action='store_true')\n    modes.add_argument('--tool')\n    parser.add_argument('--input', type=Path)\n    args = parser.parse_args()\n    root = Path(__file__).resolve().parent.parent\n    try:\n        manifest = read_json(root / 'MANIFEST.json')\n        members = manifest['files']\n        critical = ['tools/run.py', 'tools/EXAMPLES.json'] + [\n            'tools/specialist_extensions/' + n for n in\n            ('__init__.py','common.py','data.py','reliability.py','automation.py','interface.py')]\n        for name in critical:\n            path = root / name\n            if any(p.is_symlink() or (getattr(p.lstat(), 'st_file_attributes', 0) & 0x400)\n                   for p in (path, path.parent, path.parent.parent) if p != root):\n                raise ValueError('LINKED_PACKAGE_MEMBER')\n            if hashlib.sha256(path.read_bytes()).hexdigest() != members.get(name):\n                raise ValueError('PACKAGE_MEMBER_CHANGED:' + name)\n        example = read_json(root / 'tools/EXAMPLES.json')\n        allowed = set(example['tools'])\n        from specialist_extensions import evaluate\n        from specialist_extensions.common import bounded_json\n        if args.demo:\n            if args.input is not None: raise ValueError('DEMO_INPUT_NOT_NEEDED')\n            jobs = example['jobs']\n        else:\n            if args.tool not in allowed or args.input is None:\n                raise ValueError('CHOOSE_INCLUDED_TOOL_AND_INPUT')\n            jobs = [{'skill_id':args.tool,'inputs':read_json(args.input)}]\n        if not isinstance(jobs,list) or not 1 <= len(jobs) <= 11:\n            raise ValueError('INVALID_JOB_COUNT')\n        results = []\n        for job in jobs:\n            bounded_json(job)\n            if set(job) != {'skill_id','inputs'} or job['skill_id'] not in allowed:\n                raise ValueError('TOOL_OUTSIDE_PACKAGE')\n            results.append({'skill_id':job['skill_id'],'output':evaluate(job['skill_id'],job['inputs'])})\n        print(json.dumps({'status':'COMPLETED','results':results},\n                         indent=2,sort_keys=True,allow_nan=False))\n        return 0\n    except (ValueError,TypeError,KeyError,OSError,UnicodeError,RecursionError) as exc:\n        print(json.dumps({'error':str(exc)}),file=sys.stderr)\n        return 2\n\nif __name__ == '__main__': raise SystemExit(main())\n"


def _local_tool_files(data: dict[str,Any], selected: set[str]) -> dict[str,bytes]:
    """Bundle only advertised local stages with their executable dependency closure."""
    if not selected or not selected <= EXTENSION_SKILLS:
        raise CollectionError('invalid local tool selection')
    examples={}
    for role,ids in EXTENSION_ROLE_SKILLS.items():
        if selected.intersection(ids):
            _,example=_extension_contract(data,role)
            for job in example['jobs']:
                if job['skill_id'] in selected:
                    examples.setdefault(job['skill_id'],job)
    if set(examples)!=selected:raise CollectionError('local tool example missing')
    files={'tools/'+name:raw for name,raw in _extension_sources().items()}
    files['tools/run.py']=LOCAL_TOOL_RUNNER.encode('utf-8')
    files['tools/EXAMPLES.json']=(json.dumps({'tools':sorted(selected),'jobs':[examples[k] for k in sorted(selected)]},indent=2,ensure_ascii=False)+'\n').encode()
    first=sorted(selected)[0]
    files['tools/README.md']=('# Local tools\n\nPython 3.10 or newer is required. From the extracted package folder, run:\n\n'
        '```sh\npython -B tools/run.py --demo\n```\n\n'
        '## Use your own input\n\nOpen [EXAMPLES.json](EXAMPLES.json) and find the job whose `skill_id` matches your tool. '
        'Copy that job\'s `inputs` object into `input.json` in the extracted package folder, then replace its sample values with your records. '
        'The input file contains that one object, without the `jobs` or `inputs` wrapper.\n\n'
        'For `'+first+'`, run:\n\n```sh\npython -B tools/run.py --tool '+first+' --input input.json\n```\n\n'
        'Available tools: '+', '.join(sorted(selected))+'. Choose another listed tool with `--tool` and use its matching input shape.\n').encode()
    return files

def specialist_kit_files(data: dict[str,Any], role_id: str) -> dict[str,bytes]:
    contract,example=_extension_contract(data,role_id)
    root=Path(__file__).resolve().parents[1]
    # This format keeps its original root-level runner. Reuse the complete
    # instruction and practice closure, replacing only the alternate tools/ entrypoint.
    files={name:raw for name,raw in instruction_files(data,contract['skills'],[]).items()
           if not name.startswith('tools/')}
    files.update(_extension_sources())
    files['run.py']=_bounded_source(root/'examples'/'specialist_kit_runner.py')
    files['SPECIALIST.json']=(json.dumps(contract,indent=2,ensure_ascii=False)+'\n').encode()
    files['EXAMPLE.json']=(json.dumps(example,indent=2,ensure_ascii=False)+'\n').encode()
    files['README.md']=_bounded_source(root/'presets'/role_id/'COLLECTION_README.md')
    files['PLAYBOOK.md']=_bounded_source(root/'presets'/role_id/'PLAYBOOK.md')
    files['LICENSE']=PROJECT_LICENSE.encode()
    title=next(role['title'] for role in data['specialists'] if role['id']==role_id)
    files['START_HERE.md']=('# Start with '+title+'\n\n'
        'Give Muse this extracted folder and your current task. Read [README.md](README.md) for the available tools '
        'and [PLAYBOOK.md](PLAYBOOK.md) for the working method. Keep your existing preferences and memory.\n\n'
        '## Run an example\n\nWith Python 3.10 or newer, run from the extracted folder:\n\n'
        '```sh\npython -B run.py --demo\n```\n\n'
        'For your own records, copy the chosen job\'s `inputs` object from [EXAMPLE.json](EXAMPLE.json) into `input.json` '
        'and follow the command in README.md. [Practice examples](practice/README.md) include their own check command.\n').encode()
    manifest={'schema':'muse-specialist-kit/v1','specialist':role_id,
              'files':{name:hashlib.sha256(raw).hexdigest() for name,raw in sorted(files.items())}}
    files['MANIFEST.json']=(json.dumps(manifest,sort_keys=True,indent=2)+'\n').encode()
    return files

def main(argv: list[str]|None=None) -> int:
    # Preserve catalog text when output is redirected on Windows or in legacy locales.
    for stream in (sys.stdout, sys.stderr):
        reconfigure=getattr(stream,'reconfigure',None)
        if callable(reconfigure):
            reconfigure(encoding='utf-8')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--collection',type=Path,default=DEFAULT_ROOT)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('check');ls=sub.add_parser('list');ls.add_argument('--category')
    show=sub.add_parser('show');show.add_argument('starter')
    build=sub.add_parser('build');build.add_argument('starter');build.add_argument('--to',type=Path,required=True)
    challenge=sub.add_parser('challenge');challenge.add_argument('case');challenge.add_argument('--arm',choices=('plain','upstream','candidate'),required=True);challenge.add_argument('--to',type=Path,required=True)
    sub.add_parser('specialists')
    kit=sub.add_parser('kit');kit.add_argument('specialist');kit.add_argument('--to',type=Path,required=True)
    demo=sub.add_parser('demo');demo.add_argument('specialist');demo.add_argument('--to',type=Path)
    workflow=sub.add_parser('workflow-demo');workflow.add_argument('workflow');workflow.add_argument('--to',type=Path)
    args=ap.parse_args(argv)
    try:
        d=load_collection(args.collection)
        if args.command=='check':
            print(json.dumps({'schema':SCHEMA,'starters':len(d['starters']),'skills':len(d['skills']),'workflows':len(d['workflows']),
                              'specialists':len(d.get('specialists',[])),'status':'VALID'},sort_keys=True))
        elif args.command=='specialists':
            for role in d.get('specialists',[]):print(f"{role['id']}\t{role['title']}\t{role['kind']}")
        elif args.command=='kit':
            payload=build_file_map_bytes(specialist_kit_files(d,args.specialist));write_new_pack(args.to,payload)
            print(json.dumps({'specialist':args.specialist,'path':str(args.to),'bytes':len(payload),
                              'sha256':hashlib.sha256(payload).hexdigest(),'status':'PACKAGE_CREATED'},sort_keys=True))
        elif args.command=='workflow-demo':
            result=workflow_demo(d,args.workflow)
            raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode()
            if args.to:write_new_pack(args.to,raw)
            print(raw.decode(),end='')
        elif args.command=='demo':
            result=specialist_demo(d,args.specialist)
            raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode()
            if args.to:write_new_pack(args.to,raw)
            print(raw.decode(),end='')
        elif args.command=='list':
            for p in d['starters']:
                if args.category is None or args.category==p['category']:print(f"{p['id']}\t{p['title']}\t{p['category']}")
        elif args.command=='show':
            p=next((p for p in d['starters'] if p['id']==args.starter),None)
            if p is None:raise CollectionError(f'unknown starter: {args.starter}')
            print(render_profile(p))
        elif args.command=='challenge':
            b=build_file_map_bytes(challenge_files(d,args.case,args.arm));write_new_pack(args.to,b)
            print(json.dumps({'path':str(args.to),'arm':args.arm,'sha256':hashlib.sha256(b).hexdigest(),'status':'PRACTICE_CREATED'},sort_keys=True))
        else:
            b=build_bytes(d,args.starter);write_new_pack(args.to,b)
            print(json.dumps({'path':str(args.to),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)},sort_keys=True))
        return 0
    except CollectionError as e:
        print(f'collection error: {e}',file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
