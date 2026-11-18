"""Select practical tool guides for Muse specialists and packaged workflows."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ROLES = frozenset(('coordinator','software-engineer','model-builder','research-evaluator',
    'creative-studio','adversarial-verifier','personal-companion','garden-companion',
    'learning-coach','claims-adjudicator','reverse-engineering-researcher','data-engineer',
    'reliability-engineer','automation-engineer','product-interface-designer'))


def load_guides(root=ROOT):
    root = Path(root)
    path = root/'collections/tool-guides.json'
    if not path.exists():
        return {'schema':'muse-tool-guides/v1','schema_version':1,'guides':[],'workflows':[]}
    if path.is_symlink() or path.stat().st_size > 2_000_000:
        raise ValueError('TOOL_GUIDE_CATALOG_UNSAFE')
    data = json.loads(path.read_bytes())
    if data.get('schema') != 'muse-tool-guides/v1' or data.get('schema_version') != 1:
        raise ValueError('TOOL_GUIDE_SCHEMA')
    rows = data.get('guides')
    if not isinstance(rows,list) or not 1 <= len(rows) <= 150:
        raise ValueError('TOOL_GUIDE_INVENTORY')
    ids = set()
    for row in rows:
        identifier = row.get('id')
        if not isinstance(identifier,str) or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',identifier) or identifier in ids:
            raise ValueError('TOOL_GUIDE_ID')
        ids.add(identifier)
        if row.get('doc_path') != f'docs/tools/{identifier}.md':
            raise ValueError('TOOL_GUIDE_PATH')
        target = root/row['doc_path']
        if target.is_symlink() or not target.is_file() or target.stat().st_size > 200_000:
            raise ValueError('TOOL_GUIDE_FILE')
        for key in ('name','title','category','summary','cost','starter_prompt'):
            if not isinstance(row.get(key),str) or not row[key].strip():
                raise ValueError('TOOL_GUIDE_TEXT:'+key)
        for key in ('setup','inputs','steps','outputs','checks','specialist_ids'):
            values = row.get(key)
            if not isinstance(values,list) or not values or not all(isinstance(x,str) and x.strip() for x in values):
                raise ValueError('TOOL_GUIDE_LIST:'+key)
        aliases={'data-engineering-architect':'data-engineer','infrastructure-reliability-engineer':'reliability-engineer'}
        row['specialist_ids']=[aliases.get(role,role) for role in row['specialist_ids']]
        if not set(row['specialist_ids']) <= ROLES:
            raise ValueError('TOOL_GUIDE_SPECIALIST')
        if not isinstance(row.get('sources'),list) or not all(isinstance(s,str) and s.startswith('https://') for s in row['sources']):
            raise ValueError('TOOL_GUIDE_SOURCE')
    for row in rows:
        if not set(row.get('related_guide_ids',[])) <= ids:
            raise ValueError('TOOL_GUIDE_REFERENCE')
    return data


def selected_ids(data, *, role=None, ids=()):
    chosen = set(ids)
    chosen.update(row['id'] for row in data['guides'] if role in row['specialist_ids'])
    by_id = {row['id']:row for row in data['guides']}
    if not chosen <= by_id.keys():
        raise ValueError('UNKNOWN_TOOL_GUIDE')
    return sorted(chosen)


def package_files(data, *, role=None, ids=(), root=ROOT):
    chosen = selected_ids(data,role=role,ids=ids)
    if not chosen:
        return {}
    by_id = {row['id']:row for row in data['guides']}
    rows = [by_id[key] for key in chosen]
    files = {row['doc_path']:(Path(root)/row['doc_path']).read_bytes() for row in rows}
    guide = '# Tools for your work\n\nChoose a tool when it fits your task. Each guide explains setup, inputs, the working method and how to check the result.\n\n'
    guide += '| Tool | Use it for |\n| --- | --- |\n'
    for row in rows:
        guide += f"| [{row['name']}]({row['doc_path']}) | {row['summary'].replace('|','/')} |\n"
    flows = [flow for flow in data.get('workflows',[]) if set(flow['guide_ids']) <= set(chosen)]
    if flows:
        guide += '\n## Combine tools in a workflow\n\n'
        for flow in flows:
            guide += '### '+flow['title']+'\n\n'
            guide += '\n'.join(f'{i}. {step}' for i,step in enumerate(flow['steps'],1))+'\n\n'
            guide += '**Check the result:** '+' '.join(flow['checks'])+'\n\n'
    files['TOOL_GUIDES.md'] = guide.encode('utf-8')
    return files
