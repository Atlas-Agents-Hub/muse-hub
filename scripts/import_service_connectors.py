"""Convert pinned service definitions into Muse connector guides and contracts.

The input directory contains selection.json, tree.json and files/<service>/src.
Source code is parsed as text and is never imported or executed.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'docs' / 'connectors'
REPOSITORY = 'activepieces/activepieces'
COMMIT = '5110199059649227b42a805020ab03ef429103aa'
PREFIX = 'packages/pieces/community/'


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def balanced(text, start):
    """Read a brace/bracket expression without interpreting JavaScript."""
    opening = text[start]
    closing = {'{': '}', '[': ']', '(': ')'}[opening]
    level, quote, escaped, line_comment, block_comment, regex, charclass = 0, None, False, False, False, False, False
    i = start
    while i < len(text):
        c = text[i]
        pair = text[i:i + 2]
        if line_comment:
            if c == '\n':
                line_comment = False
        elif block_comment:
            if pair == '*/':
                block_comment = False
                i += 1
        elif regex:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '[':
                charclass = True
            elif c == ']':
                charclass = False
            elif c == '/' and not charclass:
                regex = False
        elif quote:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == quote:
                quote = None
        elif pair == '//':
            line_comment = True
            i += 1
        elif pair == '/*':
            block_comment = True
            i += 1
        elif c == '/' and (text[start:i].rstrip()[-1:] in ('(', '=', ',', ':', '[', '!', '?', '{', ';') or
                           re.search(r'\b(?:return|throw|case|yield)\s*$',text[start:i])):
            regex = True
        elif c in "\"'`":
            quote = c
        elif c == opening:
            level += 1
        elif c == closing:
            level -= 1
            if level == 0:
                return text[start:i + 1]
        i += 1
    raise ValueError('UNBALANCED_SOURCE_EXPRESSION')


def literal(text, key):
    if text.lstrip().startswith('{'):
        expression=dict(members(text.strip())).get(key,'').strip()
        match=re.fullmatch(r'([\'"`])((?:\\.|(?!\1)[\s\S])*?)\1',expression)
        if not match:
            return ''
        return match.group(2).replace('\\n','\n').replace("\\'", "'").replace('\\"','"').strip()
    match = re.search(r'\b' + re.escape(key) + r'\s*:\s*([\'"`])((?:\\.|(?!\1)[\s\S])*?)\1', text)
    if not match:
        return ''
    value = match.group(2)
    return value.replace('\\n', '\n').replace("\\'", "'").replace('\\"', '"').strip()


def object_after(text, pattern):
    match = re.search(pattern, text)
    if not match:
        return ''
    start = text.find('{', match.end())
    return balanced(text, start) if start >= 0 else ''


def paragraphs(value):
    return re.sub(r'\s+', ' ', value).strip()


def members(expression):
    """Yield direct object fields, including provider-defined field references."""
    body = expression[1:-1]
    start, quote, escaped, stack, regex, charclass = 0, None, False, [], False, False
    comment = None
    parts = []
    i = 0
    while i < len(body):
        char, pair = body[i], body[i:i + 2]
        if comment == 'line':
            if char == '\n':
                comment = None
        elif comment == 'block':
            if pair == '*/':
                comment = None
                i += 1
        elif regex:
            if escaped: escaped=False
            elif char=='\\': escaped=True
            elif char=='[': charclass=True
            elif char==']': charclass=False
            elif char=='/' and not charclass: regex=False
        elif quote:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == quote:
                quote = None
        elif pair in ('//', '/*'):
            comment = 'line' if pair == '//' else 'block'
            i += 1
        elif char=='/' and (body[:i].rstrip()[-1:] in ('(', '=', ',', ':', '[', '!', '?', '{', ';') or
                            re.search(r'\b(?:return|throw|case|yield)\s*$',body[:i])):
            regex=True
        elif char in "\"'`":
            quote = char
        elif char in '{[(':
            stack.append(char)
        elif char in '}])':
            if stack:
                stack.pop()
        elif char == ',' and not stack:
            parts.append(body[start:i])
            start = i + 1
        i += 1
    parts.append(body[start:])
    result = []
    for part in parts:
        part = re.sub(r'^\s*(?://[^\n]*\n\s*)*', '', part).strip()
        match = re.match(r'[\'"`]?([A-Za-z][A-Za-z0-9_-]*)[\'"`]?\s*:\s*([\s\S]+)', part)
        if match:
            result.append((match.group(1), match.group(2).strip()))
    return result


def clean(value):
    value = value.replace('Activepieces', 'Muse').replace('activepieces connection', 'service connection')
    value = re.sub(r'\s*\(H\d{2}\)', '', value)
    return value


def source_url(path):
    return f'https://github.com/{REPOSITORY}/blob/{COMMIT}/{PREFIX}{path}'


def roles(category):
    return {
        'Project management': ['coordinator', 'automation-engineer', 'software-engineer'],
        'Productivity': ['personal-companion', 'coordinator', 'automation-engineer'],
        'Scheduling': ['personal-companion', 'coordinator', 'automation-engineer'],
        'Communication': ['coordinator', 'personal-companion', 'automation-engineer'],
        'Email': ['personal-companion', 'coordinator', 'automation-engineer'],
        'Notes & docs': ['personal-companion', 'coordinator', 'research-evaluator', 'learning-coach'],
        'Sales & CRM': ['coordinator', 'automation-engineer'],
        'Jobs': ['personal-companion', 'coordinator'],
        'Support': ['coordinator', 'automation-engineer', 'software-engineer'],
        'Marketing': ['creative-studio', 'product-interface-designer', 'coordinator'],
        'Social': ['creative-studio', 'personal-companion', 'coordinator'],
        'E-commerce': ['coordinator', 'automation-engineer', 'product-interface-designer'],
        'Finance & Commerce': ['coordinator', 'personal-companion', 'claims-adjudicator'],
        'Search & Data': ['data-engineering-architect', 'research-evaluator', 'model-builder'],
        'Developer & Infra': ['software-engineer', 'infrastructure-reliability-engineer', 'automation-engineer'],
        'Monitoring': ['infrastructure-reliability-engineer', 'software-engineer', 'adversarial-verifier'],
        'Blogging': ['creative-studio', 'product-interface-designer', 'coordinator'],
        'Media management': ['creative-studio', 'automation-engineer'],
        'Video': ['creative-studio', 'learning-coach'],
        'Design': ['creative-studio', 'product-interface-designer'],
        'Translation': ['creative-studio', 'learning-coach'],
        'AI & ML': ['model-builder', 'research-evaluator', 'software-engineer'],
        'Reading': ['personal-companion', 'research-evaluator', 'learning-coach'],
    }[category]


def input_fields(text):
    props = dict(members(text)).get('props','')
    if not props.startswith('{'):
        return []
    result = []
    # Keep the source's input names and field types. Dynamic choices are resolved
    # through the referenced provider definition, never fabricated here.
    for name, expression in members(props):
        match = re.match(r'Property\.([A-Za-z0-9_]+)\s*\(', expression)
        field = object_after(expression, r'^') if match else ''
        required = bool(re.search(r'\brequired\s*:\s*true\b', field)) if match else None
        item = {'name': name, 'type': match.group(1) if match else 'ProviderField',
                'label': clean(literal(field, 'displayName') or re.sub(r'([a-z])([A-Z])', r'\1 \2', name).title()),
                'description': clean(literal(field, 'description')),
                'required': required}
        if not match:
            item['source_expression'] = paragraphs(expression)[:1000]
        if item['name'] not in {x['name'] for x in result}:
            result.append(item)
    return result


def parse_operation(raw, path):
    text = raw.decode('utf-8')
    kind = 'trigger' if re.search(r'/triggers?/', path) else 'action'
    marker = r'\bcreateTrigger\s*\(' if kind == 'trigger' else r'\bcreateAction\s*\('
    body = object_after(text, marker)
    if not body:
        return None
    name = literal(body, 'name') or Path(path).stem
    display_name = literal(body, 'displayName')
    if not display_name:
        return None
    return {'id': name, 'name': clean(display_name), 'kind': kind,
            'description': clean(literal(body, 'description')),
            'inputs': input_fields(body), 'source_url': source_url(path),
            'source_path': path, 'source_sha256': sha(raw)}


def get_auth(texts):
    joined = '\n'.join(texts)
    types = list(dict.fromkeys(re.findall(r'PieceAuth\.([A-Za-z0-9]+)\s*\(', joined)))
    labels = {'OAuth2': 'OAuth 2.0 account connection', 'SecretText': 'API key or access token',
              'BasicAuth': 'Service username and password or token', 'CustomAuth': 'Provider connection fields',
              'None': 'No account token for the listed public requests'}
    actual = [t for t in types if t in labels]
    authorization = list(dict.fromkeys(re.findall(r'\bauthUrl\s*:\s*[\'"`](https://[^\'"`\s]+)', joined)))
    token = list(dict.fromkeys(re.findall(r'\btokenUrl\s*:\s*[\'"`](https://[^\'"`\s]+)', joined)))
    scopes = []
    for match in re.finditer(r'\bscopes?\s*:\s*\[', joined):
        array = balanced(joined, joined.find('[', match.start()))
        scopes.extend(re.findall(r'[\'"`]([^\'"`\n]+)[\'"`]', array))
    auth_props = []
    for text in texts:
        body = object_after(text, r'PieceAuth\.(?:CustomAuth|BasicAuth|SecretText|OAuth2)\s*\(')
        if body:
            auth_props.extend(input_fields(body))
            direct=dict(members(body))
            for key in ('username','password'):
                field=direct.get(key,'')
                if field.startswith('{'):
                    auth_props.append({'name':key,'type':'AccountField','label':clean(literal(field,'displayName') or key),
                                       'description':clean(literal(field,'description')),'required':True})
    unique = {v['name']: v for v in auth_props}
    return {'method': '; '.join(labels[t] for t in actual) or 'Provider account connection',
            'authorization_urls': authorization, 'token_urls': token,
            'scopes': sorted(set(scopes)), 'fields': list(unique.values())}


def hosts(texts):
    found = set()
    for text in texts:
        for url in re.findall(r'https://[A-Za-z0-9_.-]+(?=[/:\s\'"`])', text):
            host = urlsplit(url).hostname
            if host and '.' in host and not host.startswith('cdn.') and host not in {
                'github.com', 'raw.githubusercontent.com', 'activepieces.com', 'docs.activepieces.com',
                'example.com', 'example.org', 'localhost', 'developer.mozilla.org', 'community.activepieces.com'}:
                found.add(host)
    return sorted(found)


def guide(row, contract):
    name = row['name']
    lines = ['---', 'name: ' + row['id'] + '-connector', 'description: ' + json.dumps(row['description']),
             '---', '', '# ' + name + ' for Muse', '', row['description'], '', '## Start a task', '',
             'Tell Muse the result you want, the account or workspace to use, and the records or files involved.',
             'Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.',
             '', '## Connect your account', '', '1. Open the service connection in your Muse setup and choose **' + name + '**.',
             '2. Configure **' + contract['auth']['method'] + '** using the provider fields below.',
             '3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.',
             '4. Start with a lookup or list operation. Keep the returned record IDs for the next step.', '']
    auth = contract['auth']
    for label, key in [('Authorize account', 'authorization_urls'), ('Token endpoint', 'token_urls')]:
        for value in auth[key]:
            lines.append(f'- {label}: <{value}>')
    for field in auth['fields']:
        lines.append(f"- **{field['label']}** (`{field['name']}`): {paragraphs(field['description']) or field['type']}")
    if auth['scopes']:
        lines += ['', 'Provider scopes: ' + ', '.join('`' + scope + '`' for scope in auth['scopes']) + '.']
    lines += ['', '[Provider connection definition](' + row['source_url'] + ').', '', '## Actions', '']
    for op in contract['operations']:
        if op['kind'] != 'action':
            continue
        lines += ['### ' + op['name'], '', op['description'] or 'Use the provider operation with the inputs below.', '']
        if op['inputs']:
            lines += ['| Input | What to provide | Required |', '| --- | --- | --- |']
            for item in op['inputs']:
                desc = paragraphs(item['description'] or item['label']).replace('|', '/')
                required = 'See action definition' if item['required'] is None else 'Yes' if item['required'] else 'Optional'
                lines.append(f"| `{item['name']}` | {desc} | {required} |")
            lines.append('')
        lines += ['[Request and response definition](' + op['source_url'] + ').', '']
    triggers = [op for op in contract['operations'] if op['kind'] == 'trigger']
    if triggers:
        lines += ['## Events and recurring work', '']
        for op in triggers:
            lines.append(f"- **[{op['name']}]({op['source_url']})** — {paragraphs(op['description'])}")
        lines += ['', 'Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.', '']
    reads = [x for x in contract['operations'] if x['kind'] == 'action' and re.search(r'\b(get|find|list|search|retrieve|read|query|browse|lookup)\b', x['name'], re.I)]
    example = (reads or [x for x in contract['operations'] if x['kind'] == 'action'] or contract['operations'])[0]
    lines += ['## Try it', '', f'> Use {name} to {example["name"].lower()}. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.', '',
              '## Complete the task', '',
              '- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.',
              '- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.',
              '- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.',
              '- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.',
              '- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.', '',
              '[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)', '']
    return '\n'.join(lines).encode('utf-8')


def build(source: Path):
    selected = json.loads((source / 'selection.json').read_bytes())
    tree = json.loads((source / 'tree.json').read_bytes())
    if tree.get('truncated') or tree['sha'] != 'eea26d0134dd6a2e17077e9196d55a9904ab204d':
        raise ValueError('INVALID_SOURCE_TREE')
    blob_by_path = {row['path']: row for row in tree['tree'] if row['type'] == 'blob'}
    current = json.loads((DIRECTORY / 'catalog.json').read_bytes())
    legacy = [row for row in current['connectors'] if row.get('source_id', 'muse-connectors') == 'muse-connectors']
    if len(legacy) != 151:
        raise ValueError('BASE_CONNECTOR_INVENTORY_CHANGED')
    rows, records, failures = [], [], []
    for ident, category in sorted(selected.items()):
        if ident in {x['id'] for x in legacy}:
            raise ValueError('DUPLICATE_EXISTING_CONNECTOR:' + ident)
        folder = source / 'files' / ident
        files = sorted(p for p in folder.rglob('*.ts') if not p.name.endswith(('.test.ts', '.spec.ts')))
        raw_by_path, sources = {}, []
        for file in files:
            relative = file.relative_to(source / 'files').as_posix()
            raw = file.read_bytes()
            blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
            if blob_by_path[relative]['sha'] != blob:
                raise ValueError('SOURCE_BLOB_MISMATCH:' + relative)
            raw_by_path[relative] = raw
            sources.append({'path': relative, 'git_blob': blob, 'sha256': sha(raw), 'bytes': len(raw)})
        index_path = ident + '/src/index.ts'
        index_raw = raw_by_path[index_path]
        index_text = index_raw.decode('utf-8')
        piece = object_after(index_text, r'\bcreatePiece\s*\(')
        name = literal(piece, 'displayName')
        description = clean(paragraphs(literal(piece, 'description')))
        if not name:
            raise ValueError('MISSING_SERVICE_NAME:' + ident)
        operations = []
        for path, raw in raw_by_path.items():
            if re.search(r'/(?:actions?|triggers?)/', path):
                op = parse_operation(raw, path)
                if op and (op['kind'], op['id']) not in {(o['kind'], o['id']) for o in operations}:
                    operations.append(op)
        operations.sort(key=lambda x: (x['kind'], x['name'].casefold(), x['id']))
        if not operations:
            raise ValueError('NO_SERVICE_OPERATIONS:' + ident)
        if not description:
            description = name + ': ' + ', '.join(o['name'].lower() for o in operations[:3]) + '.'
        texts = [index_text] + [raw.decode('utf-8') for path, raw in raw_by_path.items() if not re.search(r'/(?:actions?|triggers?)/', path)]
        auth = get_auth(texts)
        allowed_hosts = hosts([raw.decode('utf-8') for raw in raw_by_path.values()])
        if not allowed_hosts:
            allowed_hosts = ['account-configured-service-host']
        source_record = next(r for r in sources if r['path'] == index_path)
        row = {'id': ident, 'name': clean(name), 'description': description, 'category': category,
               'auth': auth['method'], 'auth_details': '\n'.join(auth['authorization_urls'] + auth['token_urls']) or auth['method'],
               'allowed_hosts': allowed_hosts, 'specialists': roles(category),
               'source_id': 'activepieces-community', 'source_url': source_url(index_path),
               'source_sha256': source_record['sha256'], 'source_git_blob': source_record['git_blob'],
               'setup_guide': 'services/' + ident + '/SKILL.md', 'guide_path': 'services/' + ident + '/SKILL.md',
               'adapter_path': 'services/' + ident + '/adapter.json',
               'files': ['SKILL.md', 'adapter.json'],
               'operations': '\n'.join(o['name'] + ': ' + o['description'] for o in operations),
               'permissions': 'Choose the account and permissions required by the task; review proposed changes before applying them.',
               'upstream_maturity': 'Version-pinned service definitions',
               'specialist_mapping': 'Recommended assistants for this service',
               'setup_prompt': f'Help me use the {clean(name)} connector with Muse. Open docs/connectors/services/{ident}/SKILL.md, choose the action for my task, resolve its required inputs, and use the service account credentials from my connection manager. Show proposed changes for approval, then save the result with its record IDs. Provider definition: {source_url(index_path)}.'}
        if ident in {'google-calendar','google-docs','google-drive','google-sheets','google-forms','grist'}:
            row['specialists'].append('garden-companion')
        if ident in {'okta','gitea','azure-devops','datadog','pagerduty','logrocket'}:
            row['specialists'].append('reverse-engineering-researcher')
        contract = {'schema': 'muse-hub/service-adapter-v1', 'id': ident, 'name': clean(name),
                    'category': category, 'auth': auth, 'allowed_hosts': allowed_hosts,
                    'specialists': row['specialists'], 'operations': operations,
                    'source': {'repository': REPOSITORY, 'commit': COMMIT, 'index_path': index_path,
                               'index_git_blob': source_record['git_blob'], 'index_sha256': source_record['sha256']}}
        target = DIRECTORY / 'services' / ident
        target.mkdir(parents=True, exist_ok=True)
        (target / 'adapter.json').write_bytes(canonical(contract))
        (target / 'SKILL.md').write_bytes(guide(row, contract))
        records.append({'id': ident, 'source_files': sources,
                        'files': {f'services/{ident}/{f}': sha((target / f).read_bytes()) for f in row['files']},
                        'operation_count': len(operations)})
        rows.append(row)
    manifest = {'schema': 'muse-hub/service-sources-v1', 'repository': REPOSITORY, 'commit': COMMIT,
                'community_tree': tree['sha'], 'connectors': records}
    (DIRECTORY / 'ADAPTER_SOURCES.json').write_bytes(canonical(manifest))
    current['schema'] = 'muse-specialist-toolkit/connectors-v2'
    current['extensions'] = {'manifest': 'ADAPTER_SOURCES.json', 'sha256': sha(canonical(manifest)),
                             'repository': REPOSITORY, 'commit': COMMIT, 'count': len(rows)}
    current['connectors'] = sorted(legacy + rows, key=lambda row: row['id'])
    (DIRECTORY / 'catalog.json').write_bytes(canonical(current))
    return {'connectors': len(current['connectors']), 'added': len(rows),
            'operations': sum(r['operation_count'] for r in records),
            'source_files': sum(len(r['source_files']) for r in records)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.source), sort_keys=True))


if __name__ == '__main__':
    main()
