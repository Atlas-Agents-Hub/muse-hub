#!/usr/bin/env python3
"""Find Muse Hub resources and build a focused toolkit for your next task."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'tools'), str(ROOT / 'scripts')]
import muse_collection as collection
import tool_guides

KINDS = ('skill', 'workflow', 'starter', 'specialist', 'connector', 'tool-guide')
PUBLIC_ROLES = {
    'data-engineer': 'data-engineering-architect',
    'reliability-engineer': 'infrastructure-reliability-engineer',
}
ROLE_ALIASES = {value: key for key, value in PUBLIC_ROLES.items()}
STOP_WORDS = frozenset('a an and for the to with my me help how do i in of on or using'.split())
MAX_SELECTED_SKILLS = 64
MAX_PACKAGE_BYTES = 160_000_000


def _json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def _words(value):
    return re.findall(r'[^\W_]+', unicodedata.normalize('NFKC', value).casefold())


def _normalized(value):
    return ' '.join(_words(value))


def _role(value):
    return ROLE_ALIASES.get(value, value)


def _guide(role):
    return 'presets/' + PUBLIC_ROLES.get(role, role) + '/INSTALL.md'


def _plain(value):
    return ' '.join(value.split())


def _checked_text(value, label, limit=256):
    if (not isinstance(value, str) or len(value) > limit or len(value.encode('utf-8')) > limit * 4
            or any(unicodedata.category(c) in ('Cc', 'Cf', 'Cs') for c in value)):
        raise collection.CollectionError(f'{label} must be ordinary text of at most {limit} characters')
    return value


def catalog_records(data, *, guides=(), connectors=()):
    """Create a common searchable view from already validated source catalogs."""
    collection.validate(data)
    role_rows = {row['id']: row for row in data.get('specialists', [])}
    skill_roles = {row['id']: set(row.get('roles', [])) for row in data['skills']}
    workflow_roles = {row['id']: set(row.get('roles', [])) for row in data['workflows']}
    for role in role_rows.values():
        for key in (*role['skills'], *role.get('library_skills', [])):
            skill_roles[key].add(role['id'])
    for starter in data['starters']:
        assigned = {starter.get('specialist_role', starter['base_role'])}
        for key in starter['skills']:
            skill_roles[key].update(assigned)
        for key in starter['workflows']:
            workflow_roles[key].update(assigned)
    records = []

    def add(kind, row, *, title, summary, category, roles, guide, example='', requirements=()):
        roles = sorted({_role(value) for value in roles})
        records.append({
            'kind': kind, 'id': row['id'], 'title': _plain(title),
            'summary': _plain(summary), 'category': category,
            'specialists': [{'id': PUBLIC_ROLES.get(value, value),
                             'title': role_rows[value]['title'], 'guide': _guide(value)}
                            for value in roles if value in role_rows],
            'guide': guide, 'example': example, 'requirements': list(requirements),
        })

    for row in data['skills']:
        root = 'collections/library' if row.get('format') == 'portable-skill' else 'collections/muse-starters-v1'
        add('skill', row, title=row['title'], summary=row['trigger'], category=row['category'],
            roles=skill_roles[row['id']], guide=f"{root}/skills/{row['id']}/SKILL.md",
            example=row['example'], requirements=row.get('requirements', []))
    for row in data['workflows']:
        roles = workflow_roles[row['id']] or set().union(*(skill_roles[key] for key in row['skills']))
        root = 'collections/library' if row.get('steps') else 'collections/muse-starters-v1'
        add('workflow', row, title=row['title'], summary=row['goal'], category=row.get('category', 'workflows'),
            roles=roles, guide=f"{root}/workflows/{row['id']}.md", example=row['finish'],
            requirements=row.get('inputs', []))
    for row in data['starters']:
        add('starter', row, title=row['title'], summary=row['purpose'], category=row['category'],
            roles=[row.get('specialist_role', row['base_role'])],
            guide=f"collections/muse-starters-v1/starters/{row['id']}/STARTER.md", example=row['first_task'])
    for row in role_rows.values():
        add('specialist', row, title=row['title'], summary=row['purpose'], category='specialists',
            roles=[row['id']], guide=_guide(row['id']))
    for row in guides:
        add('tool-guide', row, title=row['name'], summary=row['summary'], category=row['category'],
            roles=row['specialist_ids'], guide=row['doc_path'], example=row['starter_prompt'],
            requirements=row['setup'])
    for row in connectors:
        guide = 'docs/connectors/' + row['guide_path'] if row.get('guide_path') else 'docs/connectors/CATALOG.md'
        add('connector', row, title=row['name'], summary=row['description'], category=row['category'],
            roles=row['specialists'], guide=guide, example=row['operations'], requirements=[row['auth_details']])
    return sorted(records, key=lambda row: (row['kind'], row['id']))


def load_records(data):
    import connector_catalog
    return catalog_records(data, guides=tool_guides.load_guides()['guides'],
                           connectors=connector_catalog.load_catalog()['connectors'])


def search(records, query='', *, kinds=(), role=None, category=None, match='any', limit=20, offset=0):
    """Rank literal words, explain matches and paginate the complete filtered set."""
    _checked_text(query, 'query')
    if not isinstance(kinds, (list, tuple)) or any(kind not in KINDS for kind in kinds):
        raise collection.CollectionError('choose a supported resource kind')
    if match not in ('any', 'all'):
        raise collection.CollectionError('match must be any or all')
    if type(limit) is not int or not 1 <= limit <= 100:
        raise collection.CollectionError('limit must be between 1 and 100')
    if type(offset) is not int or not 0 <= offset <= 100_000:
        raise collection.CollectionError('offset must be between 0 and 100000')
    if role is not None:
        role = PUBLIC_ROLES.get(_role(role), _role(role))
        known_roles = {item['id'] for row in records for item in row['specialists']}
        if role not in known_roles:
            raise collection.CollectionError('unknown specialist: ' + role)
    if category is not None:
        _checked_text(category, 'category', 100)
        if not _normalized(category):
            raise collection.CollectionError('category must contain a word')
    raw_tokens = list(dict.fromkeys(_words(query)))
    tokens = [word for word in raw_tokens if word not in STOP_WORDS] or raw_tokens
    phrase = _normalized(query)
    if query.strip() and not tokens:
        raise collection.CollectionError('query must contain a word')
    matches = []
    for row in records:
        if kinds and row['kind'] not in kinds:
            continue
        if role is not None and role not in {item['id'] for item in row['specialists']}:
            continue
        if category is not None and _normalized(category) != _normalized(row['category']):
            continue
        fields = [(set(_words(row[key])), weight) for key, weight in
                  (('id', 14), ('title', 12), ('summary', 3), ('category', 2))]
        matched = [word for word in tokens if any(word in words for words, _ in fields)]
        if tokens and (not matched or match == 'all' and len(matched) != len(tokens)):
            continue
        score = sum(max((weight for words, weight in fields if word in words), default=0) for word in matched)
        title, identifier = _normalized(row['title']), _normalized(row['id'])
        reason = 'category and specialist filters' if not tokens else 'matching words'
        if phrase and phrase in (title, identifier):
            score += 1000
            reason = 'exact title or identifier'
        elif phrase and phrase in title:
            score += 80
            reason = 'title phrase'
        if phrase and identifier.startswith(phrase):
            score += 40
        matches.append({**row, 'score': score, 'matched_terms': matched, 'match_reason': reason})
    matches.sort(key=lambda row: (-row['score'], row['title'].casefold(), row['kind'], row['id']))
    page = matches[offset:offset + limit]
    return {'schema': 'muse-hub/discovery-v1', 'query': query, 'query_terms': tokens,
            'filters': {'kinds': sorted(set(kinds)), 'specialist': role, 'category': category, 'match': match},
            'total': len(matches), 'offset': offset, 'limit': limit,
            'next_offset': offset + len(page) if offset + len(page) < len(matches) else None,
            'kind_counts': dict(sorted(Counter(row['kind'] for row in matches).items())), 'results': page}


def _select(values, known, kind):
    if not isinstance(values, (list, tuple)) or len(values) > 64:
        raise collection.CollectionError(f'choose at most 64 {kind} identifiers')
    if any(not isinstance(value, str) or value not in known for value in values):
        raise collection.CollectionError('unknown ' + kind + ' selection')
    return sorted(set(values))


def compose_files(data, *, skills=(), workflows=(), starters=()):
    """Compose selected resources through the existing dependency-aware exporter."""
    collection.validate(data)
    skill_rows = {row['id']: row for row in data['skills']}
    workflow_rows = {row['id']: row for row in data['workflows']}
    starter_rows = {row['id']: row for row in data['starters']}
    requested = {'skills': _select(skills, skill_rows, 'skill'),
                 'workflows': _select(workflows, workflow_rows, 'workflow'),
                 'starters': _select(starters, starter_rows, 'starter')}
    if not any(requested.values()):
        raise collection.CollectionError('select a skill, workflow or starter for your toolkit')
    selected_skills = set(requested['skills'])
    selected_workflows = set(requested['workflows'])
    for identifier in requested['starters']:
        selected_skills.update(starter_rows[identifier]['skills'])
        selected_workflows.update(starter_rows[identifier]['workflows'])
    for identifier in selected_workflows:
        selected_skills.update(workflow_rows[identifier]['skills'])
    if len(selected_skills) > MAX_SELECTED_SKILLS:
        raise collection.CollectionError('choose a smaller toolkit: selections resolve to more than 64 skills')
    # Check library sizes before loading supporting files into memory.
    library_root = Path(data.get('_library_root', collection.skill_library.DEFAULT_ROOT))
    predicted = sum((library_root / skill_rows[key]['path'] / name).stat().st_size
                    for key in selected_skills if skill_rows[key].get('format') == 'portable-skill'
                    for name in skill_rows[key]['files'])
    if predicted > MAX_PACKAGE_BYTES:
        raise collection.CollectionError('choose a smaller toolkit: supporting files exceed 160 MB')
    files = collection.instruction_files(data, sorted(selected_skills), sorted(selected_workflows))
    for identifier in requested['starters']:
        files[f'starters/{identifier}/STARTER.md'] = collection.render_profile(starter_rows[identifier]).encode('utf-8')
    lines = ['# Your Muse toolkit', '',
             'Give this ZIP or its extracted folder to Muse with your task and relevant files. '
             'Ask Muse to read the selected methods, choose the useful steps and return the requested result.', '',
             '## Start a task', '',
             '> Read START_HERE.md. Use the included methods that fit my task, carry each workflow result '
             'into the next step, and save the finished work with its checks.', '']
    for heading, selected, rows, pattern in (
        ('Task starters', requested['starters'], starter_rows, 'starters/{}/STARTER.md'),
        ('Workflows', sorted(selected_workflows), workflow_rows, 'workflows/{}.md'),
        ('Skills', sorted(selected_skills), skill_rows, 'skills/{}/SKILL.md'),
    ):
        if selected:
            lines += ['## ' + heading, '']
            lines += [f"- [{rows[key]['title']}]({pattern.format(key)})" for key in selected]
            lines += ['']
    requirements = sorted({item for key in selected_skills for item in skill_rows[key].get('requirements', [])})
    if requirements:
        lines += ['## Prepare your tools', ''] + ['- ' + value for value in requirements] + ['']
    lines += ['## Use supporting files', '',
              'Keep each skill folder together. Open its guide for examples, scripts and references. '
              'Run the documented local commands from the folder named in that guide.', '']
    files['START_HERE.md'] = ('\n'.join(lines) + collection.resource_start_guide(files)).encode('utf-8')
    files['LICENSE'] = collection.PROJECT_LICENSE.encode('utf-8')
    if sum(map(len, files.values())) > MAX_PACKAGE_BYTES:
        raise collection.CollectionError('choose a smaller toolkit: supporting files exceed 160 MB')
    manifest = {'schema': 'muse-hub/custom-toolkit-v1', 'selection': requested,
                'skills': sorted(selected_skills), 'workflows': sorted(selected_workflows),
                'requirements': requirements,
                'files': {name: hashlib.sha256(raw).hexdigest() for name, raw in sorted(files.items())}}
    files['MANIFEST.json'] = _json(manifest)
    return files


def plan(files):
    manifest = json.loads(files['MANIFEST.json'])
    return {'schema': 'muse-hub/toolkit-plan-v1', 'selection': manifest['selection'],
            'skills': manifest['skills'], 'workflows': manifest['workflows'],
            'added_skills': sorted(set(manifest['skills']) - set(manifest['selection']['skills'])),
            'requirements': manifest['requirements'], 'file_count': len(files),
            'uncompressed_bytes': sum(map(len, files.values())),
            'manifest_sha256': hashlib.sha256(files['MANIFEST.json']).hexdigest(),
            'files': [{'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
                      for name, raw in sorted(files.items())]}


def _print_search(result):
    print(f"{result['total']} matching resources; showing {len(result['results'])} from offset {result['offset']}.")
    for row in result['results']:
        print(f"\n{row['kind']}  {row['id']}\n  {row['title']}\n  {row['summary']}\n  Guide: {row['guide']}")
        if row['specialists']:
            print('  Specialists: ' + ', '.join(item['title'] for item in row['specialists']))
    if result['next_offset'] is not None:
        print('\nContinue with --offset ' + str(result['next_offset']))


def main(argv=None):
    # Keep redirected output portable on Windows and in legacy locales.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if callable(reconfigure):
            reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    find = commands.add_parser('search', help='Find skills, workflows, starters, services and specialists')
    find.add_argument('query', nargs='?', default='')
    find.add_argument('--kind', choices=KINDS, action='append', default=[])
    find.add_argument('--role', help='Specialist identifier; public and toolkit aliases are accepted')
    find.add_argument('--category')
    find.add_argument('--match', choices=('any', 'all'), default='any')
    find.add_argument('--limit', type=int, default=20)
    find.add_argument('--offset', type=int, default=0)
    find.add_argument('--json', action='store_true')
    show = commands.add_parser('show', help='Show a resource, its guide and specialist routes')
    show.add_argument('kind', choices=KINDS)
    show.add_argument('identifier')
    for name in ('plan', 'build'):
        command = commands.add_parser(name, help='Preview a custom toolkit' if name == 'plan' else 'Export a custom toolkit ZIP')
        for kind in ('skill', 'workflow', 'starter'):
            command.add_argument('--' + kind, action='append', default=[])
        if name == 'build':
            command.add_argument('--to', type=Path, required=True, help='A new .zip file in an existing folder')
        else:
            command.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    try:
        data = collection.prepare_collection(collection.load_collection())
        if args.command in ('search', 'show'):
            records = load_records(data)
            if args.command == 'show':
                identifier = _role(args.identifier) if args.kind == 'specialist' else args.identifier
                row = next((row for row in records if row['kind'] == args.kind and row['id'] == identifier), None)
                if row is None:
                    raise collection.CollectionError('resource not found; search for its identifier first')
                print(_json(row).decode(), end='')
            else:
                result = search(records, args.query, kinds=args.kind, role=args.role, category=args.category,
                                match=args.match, limit=args.limit, offset=args.offset)
                if args.json:
                    print(_json(result).decode(), end='')
                else:
                    _print_search(result)
        else:
            files = compose_files(data, skills=args.skill, workflows=args.workflow, starters=args.starter)
            result = plan(files)
            if args.command == 'build':
                if args.to.suffix.lower() != '.zip':
                    raise collection.CollectionError('choose a new filename ending in .zip')
                payload = collection.build_file_map_bytes(files)
                collection.write_new_pack(args.to, payload)
                print(_json({'status': 'PACKAGE_CREATED', 'path': str(args.to.absolute()),
                             'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest(),
                             'skills': len(result['skills']), 'workflows': len(result['workflows']),
                             'files': result['file_count']}).decode(), end='')
            elif args.json:
                print(_json(result).decode(), end='')
            else:
                print(f"Your toolkit: {len(result['skills'])} skills, {len(result['workflows'])} workflows, "
                      f"{result['file_count']} files ({result['uncompressed_bytes']:,} bytes).")
                print('\nSkills: ' + ', '.join(result['skills']))
                if result['workflows']:
                    print('Workflows: ' + ', '.join(result['workflows']))
                if result['added_skills']:
                    print('Included through selected starters and workflows: ' + ', '.join(result['added_skills']))
                print('\nUse build with the same selection and --to NEW.zip to save this toolkit.')
        return 0
    except (collection.CollectionError, ValueError, OSError, KeyError, TypeError) as exc:
        print('Discovery error: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
