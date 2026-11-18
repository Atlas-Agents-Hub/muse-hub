"""Prepare Muse connector tasks and run documented HTTP reads.

Python 3.10 or later; no third-party packages are required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
IDENTIFIER = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
VARIABLE = re.compile(r'[A-Za-z_][A-Za-z0-9_]*\Z')
MAX_RESPONSE_BYTES = 4 * 1024 * 1024


class ConnectorError(ValueError):
    pass


def _read_json(path):
    return json.loads(path.read_bytes(), parse_constant=lambda x: (_ for _ in ()).throw(ConnectorError('NONFINITE_JSON')))


def contract(service, filename='adapter.json', root=ROOT):
    if not isinstance(service, str) or not IDENTIFIER.fullmatch(service):
        raise ConnectorError('INVALID_SERVICE_ID')
    if filename not in ('adapter.json', 'http.json'):
        raise ConnectorError('INVALID_CONTRACT_FILE')
    root = Path(root)
    path = root / 'services' / service / filename
    if path.is_symlink() or not path.is_file():
        raise ConnectorError('SERVICE_CONTRACT_UNAVAILABLE')
    manifest = _read_json(root / 'ADAPTER_SOURCES.json')
    records = [r for r in manifest['connectors'] if r['id'] == service]
    if len(records) != 1:
        raise ConnectorError('SERVICE_MANIFEST_CONFLICT')
    expected = records[0]['files'].get('services/' + service + '/' + filename)
    if expected != hashlib.sha256(path.read_bytes()).hexdigest():
        raise ConnectorError('SERVICE_CONTRACT_CHANGED')
    result = _read_json(path)
    if result.get('id') != service:
        raise ConnectorError('SERVICE_ID_MISMATCH')
    return result


def inspect(service, root=ROOT):
    adapter = contract(service, root=root)
    result = {'service': service, 'name': adapter['name'], 'account_setup': adapter['auth'],
              'operations': adapter['operations']}
    http_path = Path(root) / 'services' / service / 'http.json'
    result['http_reads'] = contract(service, 'http.json', root)['requests'] if http_path.exists() else []
    return result


def plan(service, operation, inputs=None, root=ROOT):
    inputs = {} if inputs is None else inputs
    if type(inputs) is not dict:
        raise ConnectorError('INPUTS_MUST_BE_AN_OBJECT')
    adapter = contract(service, root=root)
    matches = [op for op in adapter['operations'] if op['id'] == operation and op['kind'] == 'action']
    if len(matches) != 1:
        raise ConnectorError('UNKNOWN_ACTION')
    selected = matches[0]
    fields = {field['name']: field for field in selected['inputs']}
    unknown = set(inputs) - fields.keys()
    if unknown:
        raise ConnectorError('UNKNOWN_INPUTS:' + ','.join(sorted(unknown)))
    missing = sorted(name for name, field in fields.items() if field['required'] is True and (name not in inputs or inputs[name] is None or inputs[name] == ''))
    # ProviderField values are resolved from the specific linked action definition.
    resolve = sorted(name for name, field in fields.items() if field['required'] is None and name not in inputs)
    return {'service': service, 'action': selected['id'], 'name': selected['name'],
            'inputs': inputs, 'missing_required_inputs': missing, 'provider_fields_to_resolve': resolve,
            'request_definition': selected['source_url'], 'source_sha256': selected['source_sha256'],
            'ready': not missing and not resolve}


def prepare_read(service, request_id, inputs=None, root=ROOT):
    doc = contract(service, 'http.json', root)
    requests = [r for r in doc['requests'] if r['id'] == request_id]
    if len(requests) != 1:
        raise ConnectorError('UNKNOWN_HTTP_READ')
    selected = requests[0]
    if selected.get('method') != 'GET':
        raise ConnectorError('HTTP_METHOD_UNSUPPORTED')
    values = {} if inputs is None else inputs
    if type(values) is not dict or set(values) != set(selected['parameters']):
        raise ConnectorError('HTTP_INPUTS_MISMATCH')
    url = selected['url_template']
    for name in selected['parameters']:
        value = values[name]
        if type(value) not in (str, int) or not str(value) or len(str(value)) > 2000 or any(ord(c) < 32 for c in str(value)):
            raise ConnectorError('INVALID_HTTP_INPUT')
        url = url.replace('{' + name + '}', urllib.parse.quote(str(value), safe=''))
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != 'https' or parsed.hostname != selected['host'] or parsed.username or parsed.password or
        parsed.port not in (None, 443) or parsed.fragment or '{' in url or '}' in url):
        raise ConnectorError('HTTP_HOST_MISMATCH')
    return {'service': service, 'request_id': request_id, 'method': 'GET', 'url': url,
            'headers': selected.get('headers', {}), 'credential': selected['credential'],
            'source_url': selected['source_url']}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ConnectorError('REDIRECT_REFUSED')


def execute_read(prepared, token_env, output, *, environment=None, opener=None):
    if not VARIABLE.fullmatch(token_env):
        raise ConnectorError('INVALID_TOKEN_ENVIRONMENT_NAME')
    environment = os.environ if environment is None else environment
    token = environment.get(token_env, '')
    if not token or '\r' in token or '\n' in token:
        raise ConnectorError('TOKEN_ENVIRONMENT_VARIABLE_UNAVAILABLE')
    output = Path(output)
    if not output.is_absolute() or not output.parent.is_dir() or output.exists() or output.is_symlink():
        raise ConnectorError('OUTPUT_MUST_BE_A_NEW_ABSOLUTE_PATH')
    binding = prepared['credential']
    if binding.get('placement') != 'header' or not re.fullmatch(r'[A-Za-z0-9-]+', binding.get('name','')):
        raise ConnectorError('UNSUPPORTED_CREDENTIAL_BINDING')
    headers = dict(prepared['headers'])
    headers[binding['name']] = binding.get('prefix', '') + token
    headers['Accept'] = 'application/json'
    headers['User-Agent'] = 'Muse-Hub-Connector/1.0'
    request = urllib.request.Request(prepared['url'], headers=headers, method='GET')
    opener = urllib.request.build_opener(_NoRedirect()) if opener is None else opener
    try:
        with opener.open(request, timeout=30) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
            status = response.status
    except urllib.error.HTTPError as error:
        raise ConnectorError('PROVIDER_HTTP_ERROR:' + str(error.code)) from None
    except urllib.error.URLError:
        raise ConnectorError('PROVIDER_CONNECTION_FAILED') from None
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ConnectorError('PROVIDER_RESPONSE_TOO_LARGE')
    try:
        body = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError('NONFINITE_JSON')))
    except (ValueError, UnicodeDecodeError):
        raise ConnectorError('PROVIDER_RESPONSE_IS_NOT_JSON') from None
    receipt = {'service': prepared['service'], 'request_id': prepared['request_id'],
               'http_status': status, 'response': body}
    # Exclusive creation leaves existing results intact, including after a race.
    with output.open('x', encoding='utf-8') as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')
    return {'status': 'SAVED', 'service': prepared['service'], 'request_id': prepared['request_id'],
            'http_status': status, 'path': str(output), 'response_bytes': len(raw)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    inspect_parser = sub.add_parser('inspect'); inspect_parser.add_argument('service')
    planner = sub.add_parser('plan'); planner.add_argument('service'); planner.add_argument('action')
    planner.add_argument('--inputs', type=Path)
    read = sub.add_parser('read'); read.add_argument('service'); read.add_argument('request_id')
    read.add_argument('--inputs', type=Path); read.add_argument('--execute', action='store_true')
    read.add_argument('--token-env'); read.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'inspect':
            result = inspect(args.service)
        else:
            inputs = _read_json(args.inputs) if args.inputs else {}
            if args.command == 'plan':
                result = plan(args.service, args.action, inputs)
            else:
                prepared = prepare_read(args.service, args.request_id, inputs)
                if args.execute:
                    if not args.token_env or not args.output:
                        raise ConnectorError('EXECUTION_REQUIRES_TOKEN_ENV_AND_OUTPUT')
                    result = execute_read(prepared, args.token_env, args.output)
                else:
                    result = {**prepared, 'credential': {'placement': prepared['credential']['placement'],
                              'name': prepared['credential']['name']}}
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
        return 0
    except (ConnectorError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        # Error output intentionally contains no account response or credential.
        print(json.dumps({'status': 'ERROR', 'reason': str(error)[:200]}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
