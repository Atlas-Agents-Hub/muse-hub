#!/usr/bin/env python3
"""Validate, inspect and package Muse workflow graphs and their input templates."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import stat
import sys

ROOT = Path(__file__).resolve().parents[1] / 'collections/library'
ID = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
HASH = re.compile(r'[a-f0-9]{64}\Z')
MAX_RESOURCE_BYTES = 2_000_000
MAX_GRAPH_NODES = 200


def _identifier(value, label):
    if not isinstance(value, str) or not ID.fullmatch(value) or len(value) > 100:
        raise ValueError('invalid ' + label)


def _text(value, label, limit=30_000):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError('invalid ' + label)
    if any(ord(c) < 32 and c not in '\n\r\t' for c in value):
        raise ValueError('control character in ' + label)


def validate_graph(graph):
    if not isinstance(graph, dict) or graph.get('schema') != 'muse-workflow-graph/v1':
        raise ValueError('unsupported workflow graph')
    _identifier(graph.get('id'), 'workflow identifier')
    _text(graph.get('title'), 'workflow title')
    nodes = graph.get('nodes')
    if not isinstance(nodes, list) or not 2 <= len(nodes) <= MAX_GRAPH_NODES:
        raise ValueError('workflow requires 2..200 nodes')
    ids = set()
    for node in nodes:
        if not isinstance(node, dict):
            raise ValueError('invalid workflow node')
        _identifier(node.get('id'), 'node identifier')
        if node['id'] in ids:
            raise ValueError('duplicate workflow node')
        ids.add(node['id'])
        for key in ('label', 'operation', 'adapter'):
            _text(node.get(key), 'node ' + key)
        if not isinstance(node.get('parameters'), dict):
            raise ValueError('node parameters must be an object')
    config = graph.get('configuration')
    if not isinstance(config, list) or len(config) > 2000:
        raise ValueError('invalid workflow configuration')
    inputs = set()
    for item in config:
        if not isinstance(item, dict):
            raise ValueError('invalid configuration item')
        _identifier(item.get('id'), 'configuration identifier')
        _text(item.get('purpose'), 'configuration purpose')
        if item['id'] in inputs:
            raise ValueError('duplicate configuration input')
        inputs.add(item['id'])
    stack = [(node['parameters'], 0) for node in nodes]
    while stack:
        obj, depth = stack.pop()
        if depth > 50:
            raise ValueError('parameter nesting exceeds limit')
        if isinstance(obj, dict):
            if set(obj) == {'configuration_input'}:
                if not isinstance(obj['configuration_input'],str) or obj['configuration_input'] not in inputs:
                    raise ValueError('unresolved configuration input')
            if not all(isinstance(k, str) for k in obj):
                raise ValueError('parameter keys must be text')
            stack.extend((x, depth + 1) for x in obj.values())
        elif isinstance(obj, list):
            stack.extend((x, depth + 1) for x in obj)
        elif isinstance(obj, float) and not math.isfinite(obj):
            raise ValueError('parameters must be finite')
        elif not isinstance(obj, (str, int, float, bool, type(None))):
            raise ValueError('invalid parameter value')
    edges = graph.get('edges')
    if not isinstance(edges, list) or not edges or len(edges) > 2000:
        raise ValueError('workflow requires connected operations')
    seen = set()
    for edge in edges:
        if (not isinstance(edge, dict) or not {'from','to','channel','branch'} <= set(edge)
                or set(edge)-{'from','to','channel','branch','input'}):
            raise ValueError('invalid graph edge')
        if edge['from'] not in ids or edge['to'] not in ids:
            raise ValueError('unresolved graph edge')
        _text(edge['channel'], 'edge channel', 80)
        if type(edge['branch']) is not int or not 0 <= edge['branch'] <= 100:
            raise ValueError('invalid branch index')
        if type(edge.get('input',0)) is not int or not 0 <= edge.get('input',0) <= 100:
            raise ValueError('invalid input port')
        key = (edge['from'], edge['to'], edge['channel'], edge['branch'], edge.get('input',0))
        if key in seen:
            raise ValueError('duplicate graph edge')
        seen.add(key)
    terminal = graph.get('terminal_branches',[])
    if not isinstance(terminal,list):raise ValueError('invalid terminal branches')
    terminal_keys=set()
    for branch in terminal:
        if not isinstance(branch,dict) or set(branch)!={'from','channel','branch'} or branch['from'] not in ids:
            raise ValueError('unresolved terminal branch')
        _text(branch['channel'],'terminal channel',80)
        if type(branch['branch']) is not int or not 0<=branch['branch']<=100:raise ValueError('invalid terminal branch index')
        key=(branch['from'],branch['channel'],branch['branch'])
        if key in terminal_keys or any((e['from'],e['channel'],e['branch'])==key for e in edges):
            raise ValueError('conflicting terminal branch')
        terminal_keys.add(key)
    entries = graph.get('entrypoints')
    if not isinstance(entries, list) or not entries or len(entries) != len(set(entries)) or set(entries) - ids:
        raise ValueError('unresolved workflow entrypoint')
    return graph


def plan(graph):
    """Return dependency waves and loop members without running any adapter."""
    validate_graph(graph)
    ids = {node['id'] for node in graph['nodes']}
    dependencies = {key: set() for key in ids}
    outgoing = {key: set() for key in ids}
    for edge in graph['edges']:
        dependencies[edge['to']].add(edge['from'])
        outgoing[edge['from']].add(edge['to'])
    remaining = set(ids); waves = []
    while remaining:
        ready = sorted(key for key in remaining if not dependencies[key] & remaining)
        if not ready:
            break
        waves.append(ready); remaining.difference_update(ready)
    # Distinguish actual loop members from nodes waiting on a loop's output.
    def reaches(start, current, visited):
        for target in outgoing[current]:
            if target == start:
                return True
            if target not in visited:
                visited.add(target)
                if reaches(start, target, visited):
                    return True
        return False
    iterative = sorted(key for key in remaining if reaches(key, key, {key}))
    return {'schema': 'muse-workflow-plan/v1', 'workflow': graph['id'],
            'waves': waves, 'iterative_nodes': iterative,
            'waiting_on_iteration': sorted(remaining - set(iterative)),
            'edges': graph['edges'], 'entrypoints': graph['entrypoints'],
            'adapters': sorted({node['adapter'] for node in graph['nodes']}),
            'configuration': graph['configuration'],
            'terminal_branches':graph.get('terminal_branches',[])}


def validate_resources(workflow):
    resources = workflow.get('resources')
    if not isinstance(resources, dict) or set(resources) != {'path', 'files'}:
        raise ValueError('invalid workflow resources')
    _identifier(workflow.get('id'), 'workflow identifier')
    if resources['path'] != 'workflow-assets/' + workflow['id']:
        raise ValueError('invalid workflow resource path')
    files = resources['files']
    if not isinstance(files, dict) or not 1 <= len(files) <= 10 or 'WORKFLOW.json' not in files:
        raise ValueError('workflow graph resource is required')
    for name, digest in files.items():
        if (not isinstance(name, str) or not name.isascii() or '\\' in name or ':' in name
                or len(PurePosixPath(name).parts) != 1 or name.startswith('.')
                or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', name)):
            raise ValueError('invalid workflow member path')
        if not isinstance(digest, str) or not HASH.fullmatch(digest):
            raise ValueError('invalid workflow member digest')
    return resources


def package_files(workflow, root=ROOT):
    resources = validate_resources(workflow)
    root = Path(root).absolute()
    result = {}
    for name, digest in resources['files'].items():
        path = root / resources['path'] / name
        for part in list(reversed(path.parents)) + [path]:
            if part.is_symlink():
                info=part.lstat()
                trusted=(sys.platform=='darwin' and str(part) in ('/var','/tmp','/etc')
                         and info.st_uid==0 and str(part.resolve())=='/private'+str(part))
                if not trusted:raise ValueError('workflow resource symlink refused')
            if part.exists() and getattr(part.lstat(), 'st_file_attributes', 0) & 0x400:
                raise ValueError('workflow resource reparse point refused')
        info = path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_RESOURCE_BYTES:
            raise ValueError('workflow resource exceeds file budget')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError('workflow resource digest mismatch: ' + name)
        if name == 'WORKFLOW.json':
            graph = json.loads(raw)
            validate_graph(graph)
            if graph['id'] != workflow['id']:
                raise ValueError('workflow resource identity mismatch')
        result['workflows/' + workflow['id'] + '/' + name] = raw
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph', type=Path)
    args = parser.parse_args(argv)
    path = args.graph
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_RESOURCE_BYTES:
        parser.error('select a regular workflow JSON file within the size limit')
    print(json.dumps(plan(json.loads(path.read_bytes())), ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
