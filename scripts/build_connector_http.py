"""Build exact HTTP read contracts from the downloaded service source files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlencode, urlsplit

from import_service_connectors import DIRECTORY, balanced, canonical, literal, members, sha, source_url


def enclosing_object(text, position):
    stack, quote, escaped, comment = [], None, False, None
    i = 0
    while i < position:
        char, pair = text[i], text[i:i+2]
        if comment == 'line':
            if char == '\n': comment = None
        elif comment == 'block':
            if pair == '*/': comment = None; i += 1
        elif quote:
            if escaped: escaped = False
            elif char == '\\': escaped = True
            elif char == quote: quote = None
        elif pair in ('//', '/*'):
            comment = 'line' if pair == '//' else 'block'; i += 1
        elif char in "\"'`": quote = char
        elif char == '{': stack.append(i)
        elif char == '}' and stack: stack.pop()
        i += 1
    return balanced(text, stack[-1]) if stack else ''


def scalar(expression):
    expression = expression.strip()
    if expression in ('true', 'false'): return expression
    if re.fullmatch(r'[0-9]+', expression): return expression
    if len(expression) >= 2 and expression[0] in "\"'`" and expression[-1] == expression[0]:
        value = expression[1:-1]
        if '${' not in value and not re.search(r'(?<!\\)' + re.escape(expression[0]), value):
            return value.replace('\\"','"').replace("\\'", "'")
    return None


def binding_from(headers):
    result = []
    for key, value in members(headers) if headers.startswith('{') else []:
        if key.lower() == 'authorization':
            match = re.fullmatch(r'[\'"`](Bearer |OAuth |Klaviyo-API-Key )\$\{[^}]+\}[\'"`]', value.strip())
            if match:
                result.append({'placement':'header', 'name':key, 'prefix':match.group(1)})
        elif key.lower() in ('x-api-key','api-key','x-umami-api-key','x-auth-token','x-access-token','dd-api-key','x-apikey'):
            if scalar(value) is None:
                result.append({'placement':'header', 'name':key, 'prefix':''})
    return result


def collect(service, source):
    files = sorted((source/'files'/service).rglob('*.ts'))
    texts = {p.relative_to(source/'files').as_posix():p.read_bytes().decode('utf-8') for p in files if not p.name.endswith(('.test.ts','.spec.ts'))}
    constants = {}
    defaults = []
    for path, text in texts.items():
        for match in re.finditer(r'(?:\bconst\s+|\b)([A-Za-z_][A-Za-z0-9_]*)\s*[:=]\s*([\'"`])(https://[^\'"`\s$]+)\2',text):
            if re.search(r'url|base|endpoint',match.group(1),re.I):
                constants.setdefault(match.group(1),set()).add(match.group(3))
        for match in re.finditer(r'\bheaders\s*:\s*\{',text):
            headers=balanced(text,text.find('{',match.start()))
            for binding in binding_from(headers):
                if binding not in [v['binding'] for v in defaults]:
                    defaults.append({'binding':binding,'path':path})
    requests=[]
    seen=set()
    for path,text in texts.items():
        for match in re.finditer(r'\bmethod\s*:\s*(?:HttpMethod\.GET|[\'"]GET[\'"])',text):
            body=enclosing_object(text,match.start())
            fields=dict(members(body)) if body else {}
            expression=fields.get('url','').strip()
            if not expression or expression[0] not in "\"'`" or expression[-1]!=expression[0]:continue
            value=expression[1:-1]
            if re.search(r'(?<!\\)'+re.escape(expression[0]),value):continue
            params=[]
            failed=False
            for variable in re.findall(r'\$\{([^}]+)\}',value):
                candidates=constants.get(variable.split('.')[-1],set())
                if len(candidates)==1:
                    value=value.replace('${'+variable+'}',next(iter(candidates)))
                elif re.fullmatch(r'(?:context\.propsValue\.|propsValue\.)?[A-Za-z_][A-Za-z0-9_]*',variable) and not re.search(r'auth|token|secret|base|url',variable,re.I):
                    name=variable.split('.')[-1]
                    value=value.replace('${'+variable+'}','{'+name+'}')
                    if name not in params:params.append(name)
                else:
                    failed=True;break
            if failed:continue
            parsed=urlsplit(value)
            if parsed.scheme!='https' or not parsed.hostname or '{' in parsed.netloc or parsed.username or parsed.password or parsed.port not in (None,443):continue
            if re.search(r'logout|delete|remove|unsubscribe|revoke|reset|send|publish',parsed.path,re.I):continue
            if re.search(r'/(?:generations|jobs)/1$',parsed.path):continue
            query={}
            query_expression=fields.get('queryParams','')
            if query_expression:
                if not query_expression.startswith('{'):continue
                for key,expression in members(query_expression):
                    value2=scalar(expression)
                    if value2 is None or re.search(r'key|token|secret',key,re.I):failed=True;break
                    query[key]=value2
                if failed or '...' in query_expression:continue
            headers_expression=fields.get('headers','').strip()
            bindings=binding_from(headers_expression)
            credential_source=path
            if len(bindings)==1:
                credential=bindings[0]
            elif not bindings and len(defaults)==1:
                credential=defaults[0]['binding'];credential_source=defaults[0]['path']
            else:continue
            headers={}
            if headers_expression.startswith('{'):
                for key,expression in members(headers_expression):
                    if key==credential['name']:continue
                    value2=scalar(expression)
                    if value2 is None:failed=True;break
                    headers[key]=value2
            elif headers_expression:
                continue
            if failed:continue
            if query:value+=('&' if parsed.query else '?')+urlencode(query)
            signature=(re.sub(r'\{[^}]+\}','{}',value),json.dumps(credential,sort_keys=True),
                       json.dumps({k.lower():v for k,v in headers.items() if k.lower()!='accept'},sort_keys=True))
            if signature in seen:continue
            seen.add(signature)
            name='read-'+re.sub(r'[^a-z0-9]+','-',urlsplit(value).path.strip('/').lower()).strip('-')
            if len(name)>100:name=name[:100].rstrip('-')
            if name in {r['id'] for r in requests}:name+='-'+str(len(requests)+1)
            requests.append({'id':name,'method':'GET','url_template':value,'host':parsed.hostname,
                             'parameters':params,'headers':headers,'credential':credential,
                             'source_url':source_url(path),'source_path':path,'source_sha256':sha(text.encode()),
                             'credential_source_path':credential_source,'credential_source_sha256':sha(texts[credential_source].encode())})
    return requests[:5]


def build(source):
    catalog=json.loads((DIRECTORY/'catalog.json').read_bytes())
    manifest=json.loads((DIRECTORY/'ADAPTER_SOURCES.json').read_bytes())
    records={r['id']:r for r in manifest['connectors']}
    total=0;services=0
    for row in catalog['connectors']:
        if row.get('source_id')!='activepieces-community':continue
        requests=collect(row['id'],source)
        if not requests:continue
        payload={'schema':'muse-hub/connector-http-v1','id':row['id'],'requests':requests}
        relative=f"services/{row['id']}/http.json"
        (DIRECTORY/relative).write_bytes(canonical(payload))
        if 'http.json' not in row['files']:row['files'].append('http.json')
        records[row['id']]['files'][relative]=sha(canonical(payload))
        records[row['id']]['http_reads']=len(requests)
        guide=DIRECTORY/row['guide_path']
        text=guide.read_text(encoding='utf-8')
        marker='## Run a direct request\n\n'
        if marker in text:
            text=text.split(marker,1)[0].rstrip()+'\n'
        text+='\n'+marker+'From the connector directory, inspect available requests with:\n\n```console\npython connector.py inspect '+row['id']+'\n```\n\n'
        text+='Available HTTP reads: '+', '.join('`'+r['id']+'`' for r in requests)+'.\n\n'
        text+='[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).\n'
        guide.write_bytes(text.encode('utf-8'))
        records[row['id']]['files'][row['guide_path']]=sha(guide.read_bytes())
        services+=1;total+=len(requests)
    (DIRECTORY/'ADAPTER_SOURCES.json').write_bytes(canonical(manifest))
    catalog['extensions']['sha256']=sha(canonical(manifest))
    (DIRECTORY/'catalog.json').write_bytes(canonical(catalog))
    return {'direct_http_services':services,'http_reads':total}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--source',type=Path,required=True)
    args=parser.parse_args();print(json.dumps(build(args.source),sort_keys=True))
