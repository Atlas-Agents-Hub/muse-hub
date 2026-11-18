"""Validate and export Muse service connectors with their guides and adapters."""
from __future__ import annotations
import argparse,hashlib,json,re,sys,tempfile,zipfile,os
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/"docs"/"connectors"
REPO="bluman1/muse-connectors"
PIN="73f302c2d8569fdc65e0e57c26b244c547fcd40e"
ID=re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SHA=re.compile("[0-9a-f]{64}\\Z")
GIT_SHA=re.compile("[0-9a-f]{40}\\Z")
SCHEMA="muse-specialist-toolkit/connectors-v2"
EXTENSION_REPO="activepieces/activepieces"
EXTENSION_PIN="5110199059649227b42a805020ab03ef429103aa"
LEGACY_COUNT=151
MANDATORY={"id","name","description","category","auth","allowed_hosts","specialists",
           "source_url","source_sha256","source_git_blob","setup_prompt",
           "permissions","auth_details","operations","upstream_maturity","files","setup_guide"}
FORBIDDEN={"installed","connected","working","officially_endorsed","token","password","secret"}
FILES=("catalog.json","upstream-catalog.json","UPSTREAM_LICENSE.txt",
       "SOURCE_RECORDS.json","PROVENANCE.json","README.md","CATALOG.md",
       "index.html","app.css","app.js")

def _sha(raw:bytes)->str:
    return hashlib.sha256(raw).hexdigest()

def _canonical(obj)->bytes:
    return (json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False)+"\n").encode("utf8")

def _roles()->set[str]:
    doc=json.loads((ROOT/"presets/catalog.json").read_bytes())
    return set(doc["presets"])

def validate_catalog(doc:object)->dict:
    if type(doc) is not dict or set(doc)!={"schema","source","extensions","connectors"} or doc["schema"]!=SCHEMA:
        raise ValueError("INVALID_CATALOG_SCHEMA")
    src=doc["source"]
    if type(src) is not dict or src.get("repository")!=REPO or src.get("commit")!=PIN:
        raise ValueError("SOURCE_PIN_MISMATCH")
    if src.get("license")!="MIT" or not isinstance(src.get("catalog_sha256"),str) or not SHA.fullmatch(src["catalog_sha256"]):
        raise ValueError("INVALID_SOURCE_LICENSE_OR_DIGEST")
    extension=doc['extensions']
    if (type(extension) is not dict or set(extension)!={'manifest','sha256','repository','commit','count'} or
        extension['repository']!=EXTENSION_REPO or extension['commit']!=EXTENSION_PIN or
        extension['manifest']!='ADAPTER_SOURCES.json' or type(extension['count']) is not int or
        not 1<=extension['count']<=2000 or type(extension['sha256']) is not str or not SHA.fullmatch(extension['sha256'])):
        raise ValueError('INVALID_EXTENSION_SOURCE')
    rows=doc["connectors"]
    if type(rows) is not list or len(rows)!=LEGACY_COUNT+extension['count']:
        raise ValueError("CONNECTOR_COUNT_INVALID")
    roles=_roles();seen=set()
    for row in rows:
        if type(row) is not dict or not MANDATORY<=set(row) or FORBIDDEN&set(row):
            raise ValueError("INVALID_CONNECTOR_FIELDS")
        name=row["id"]
        if type(name) is not str or not ID.fullmatch(name) or name in seen:
            raise ValueError("INVALID_OR_DUPLICATE_CONNECTOR_ID")
        seen.add(name)
        for key in ("name","description","category","auth","setup_prompt","permissions","auth_details",
                    "operations","upstream_maturity","setup_guide"):
            if type(row[key]) is not str or not row[key].strip() or len(row[key])>20000:
                raise ValueError("INVALID_CONNECTOR_TEXT")
        for key in ("source_sha256","source_git_blob"):
            pattern=SHA if key=="source_sha256" else GIT_SHA
            if type(row[key]) is not str or not pattern.fullmatch(row[key]):
                raise ValueError("INVALID_CONNECTOR_DIGEST")
        source_id=row.get('source_id','muse-connectors')
        if source_id not in ('muse-connectors','activepieces-community'):
            raise ValueError('UNKNOWN_CONNECTOR_SOURCE')
        expected=(f"https://github.com/{REPO}/blob/{PIN}/connectors/{name}/SKILL.md" if source_id=='muse-connectors' else
                  f"https://github.com/{EXTENSION_REPO}/blob/{EXTENSION_PIN}/packages/pieces/community/{name}/src/index.ts")
        if row["source_url"]!=expected or row["source_url"] not in row["setup_prompt"]:
            raise ValueError("CONNECTOR_SOURCE_MISMATCH")
        for key in ("specialists","files","allowed_hosts"):
            value=row[key]
            if type(value) is not list or not value or len(value)!=len(set(map(str,value))):
                raise ValueError("INVALID_CONNECTOR_LIST")
            if not all(type(v) is str and v and len(v)<180 for v in value):
                raise ValueError("INVALID_CONNECTOR_LIST_VALUE")
        if not set(row["specialists"])<=roles:
            raise ValueError("UNKNOWN_SPECIALIST")
        if "SKILL.md" not in row["files"]:
            raise ValueError("MISSING_SKILL_FILE")
        for f in row["files"]:
            if not all(part and part not in (".","..") for part in f.split("/")) or "\\" in f or ":" in f or f.startswith("/"):
                raise ValueError("UNSAFE_MANIFEST_PATH")
        for host in row["allowed_hosts"]:
            if "://" in host or re.match(r"^[a-z]+:",host,re.I) or any(ord(ch)<32 or ord(ch)==127 for ch in host):
                raise ValueError("INVALID_ALLOWED_HOST")
        expected_guide=f"https://github.com/{REPO}/blob/{PIN}/INSTALL.md" if source_id=='muse-connectors' else f'services/{name}/SKILL.md'
        if row["setup_guide"]!=expected_guide:
            raise ValueError("INSTALL_PIN_MISMATCH")
        if source_id=='activepieces-community' and (row.get('guide_path')!=expected_guide or row.get('adapter_path')!=f'services/{name}/adapter.json'):
            raise ValueError('ADAPTER_PATH_MISMATCH')
        if "credentials" not in row["setup_prompt"].lower() or "approval" not in row["setup_prompt"].lower():
            raise ValueError("UNSAFE_SETUP_PROMPT")
    if rows!=sorted(rows,key=lambda r:r["id"]):
        raise ValueError("CONNECTOR_ORDER_UNSTABLE")
    if sum(row.get('source_id','muse-connectors')=='muse-connectors' for row in rows)!=LEGACY_COUNT:
        raise ValueError('LEGACY_SOURCE_COUNT_INVALID')
    return doc

def load_catalog()->dict:
    doc=json.loads((DIRECTORY/"catalog.json").read_bytes(),parse_constant=lambda _ :(_ for _ in ()).throw(ValueError("NONFINITE")))
    return validate_catalog(doc)

def check()->dict:
    doc=load_catalog()
    proof=json.loads((DIRECTORY/"PROVENANCE.json").read_bytes())
    if proof.get("connector_count")!=len(doc['connectors']) or proof.get("source_commit")!=PIN or proof.get("source_repository")!=REPO:
        raise ValueError("PROVENANCE_CONFLICT")
    if proof.get("upstream_code_executed") is not False:
        raise ValueError("AUTHORITY_MISREPRESENTED")
    files=proof.get("distributed_files")
    if type(files) is not dict or len(files)<4:
        raise ValueError("INCOMPLETE_FILE_INTEGRITY")
    for key,digest in files.items():
        if type(key) is not str or not key.startswith("docs/connectors/") or ".." in key or type(digest) is not str or not SHA.fullmatch(digest):
            raise ValueError("INVALID_PROVENANCE_PATH")
        if not (ROOT/key).is_file() or (ROOT/key).is_symlink() or _sha((ROOT/key).read_bytes())!=digest:
            raise ValueError("DISTRIBUTED_HASH_MISMATCH")
    upstream=(DIRECTORY/"upstream-catalog.json").read_bytes()
    if _sha(upstream)!=doc["source"]["catalog_sha256"]:
        raise ValueError("UPSTREAM_HASH_MISMATCH")
    rows=json.loads(upstream)
    legacy=[r for r in doc['connectors'] if r.get('source_id','muse-connectors')=='muse-connectors']
    if len(rows)!=LEGACY_COUNT or {r["id"] for r in rows}!={r["id"] for r in legacy}:
        raise ValueError("UPSTREAM_CATALOG_MISMATCH")
    manifest=json.loads((DIRECTORY/"SOURCE_RECORDS.json").read_bytes())
    source_by_id={v["path"].split("/")[1]:v for v in manifest["documents"]}
    if len(source_by_id)!=LEGACY_COUNT:
        raise ValueError("SOURCE_RECORD_COUNT")
    for r in legacy:
        rec=source_by_id[r["id"]]
        if rec["sha256"]!=r["source_sha256"] or rec["git_blob"]!=r["source_git_blob"]:
            raise ValueError("SOURCE_RECORD_CONFLICT")
        if sorted(x["path"].rsplit("/",2)[-1] if "/" not in x["path"].replace("connectors/"+r["id"]+"/","") else x["path"].replace("connectors/"+r["id"]+"/","") for x in rec["files"])!=sorted(r["files"]):
            raise ValueError("SOURCE_FILE_MANIFEST_CONFLICT")
    if "muse-connectors contributors" not in (DIRECTORY/"UPSTREAM_LICENSE.txt").read_text(encoding="utf8"):
        raise ValueError("MISSING_UPSTREAM_ATTRIBUTION")
    if any(not (DIRECTORY/name).is_file() for name in FILES):
        raise ValueError("INCOMPLETE_DIRECTORY")
    extension_raw=(DIRECTORY/'ADAPTER_SOURCES.json').read_bytes()
    if _sha(extension_raw)!=doc['extensions']['sha256']:
        raise ValueError('ADAPTER_MANIFEST_HASH_MISMATCH')
    manifest=json.loads(extension_raw)
    if (manifest.get('schema')!='muse-hub/service-sources-v1' or manifest.get('repository')!=EXTENSION_REPO or
        manifest.get('commit')!=EXTENSION_PIN or manifest.get('community_tree')!='eea26d0134dd6a2e17077e9196d55a9904ab204d'):
        raise ValueError('ADAPTER_SOURCE_CONFLICT')
    extensions=[r for r in doc['connectors'] if r.get('source_id')=='activepieces-community']
    records=manifest.get('connectors',[])
    if (len(records)!=len(extensions) or len({r['id'] for r in records})!=len(records) or
        {r['id'] for r in records}!={r['id'] for r in extensions}):
        raise ValueError('ADAPTER_INVENTORY_CONFLICT')
    record_by_id={r['id']:r for r in records}
    operation_count=0
    for row in extensions:
        record=record_by_id[row['id']]
        source={r['path']:r for r in record['source_files']}
        index=source.get(row['id']+'/src/index.ts',{})
        if index.get('sha256')!=row['source_sha256'] or index.get('git_blob')!=row['source_git_blob']:
            raise ValueError('ADAPTER_INDEX_SOURCE_CONFLICT')
        expected_files={f"services/{row['id']}/"+name for name in row['files']}
        if set(record['files'])!=expected_files:
            raise ValueError('ADAPTER_FILE_INVENTORY_CONFLICT')
        for path,digest in record['files'].items():
            if not SHA.fullmatch(digest) or files.get('docs/connectors/'+path)!=digest or _sha((DIRECTORY/path).read_bytes())!=digest:
                raise ValueError('ADAPTER_FILE_HASH_MISMATCH')
        adapter=json.loads((DIRECTORY/row['adapter_path']).read_bytes())
        if (adapter.get('schema')!='muse-hub/service-adapter-v1' or adapter.get('id')!=row['id'] or
            adapter.get('source',{}).get('commit')!=EXTENSION_PIN or adapter.get('specialists')!=row['specialists'] or
            adapter.get('allowed_hosts')!=row['allowed_hosts']):
            raise ValueError('ADAPTER_CONTRACT_CONFLICT')
        ops=adapter.get('operations',[])
        if not ops or len(ops)!=record['operation_count'] or len({(o['kind'],o['id']) for o in ops})!=len(ops):
            raise ValueError('ADAPTER_OPERATIONS_CONFLICT')
        for op in ops:
            origin=source.get(op['source_path'],{})
            expected=f"https://github.com/{EXTENSION_REPO}/blob/{EXTENSION_PIN}/packages/pieces/community/"+op['source_path']
            if origin.get('sha256')!=op['source_sha256'] or op['source_url']!=expected:
                raise ValueError('ADAPTER_OPERATION_SOURCE_CONFLICT')
        if 'http.json' in row['files']:
            http=json.loads((DIRECTORY/f"services/{row['id']}/http.json").read_bytes())
            if http.get('schema')!='muse-hub/connector-http-v1' or http.get('id')!=row['id']:
                raise ValueError('HTTP_CONTRACT_CONFLICT')
            reads=http.get('requests',[])
            if not reads or len(reads)!=record.get('http_reads') or len({r['id'] for r in reads})!=len(reads):
                raise ValueError('HTTP_READ_INVENTORY_CONFLICT')
            for request in reads:
                parsed=urlparse(request['url_template'])
                if (request['method']!='GET' or parsed.scheme!='https' or parsed.hostname!=request['host'] or
                    parsed.username or parsed.password or parsed.port not in (None,443) or
                    request['host'] not in row['allowed_hosts'] or
                    set(re.findall(r'\{([A-Za-z_][A-Za-z0-9_]*)\}',request['url_template']))!=set(request['parameters'])):
                    raise ValueError('INVALID_HTTP_READ_CONTRACT')
                for path_key,digest_key in [('source_path','source_sha256'),('credential_source_path','credential_source_sha256')]:
                    if source.get(request[path_key],{}).get('sha256')!=request[digest_key]:
                        raise ValueError('HTTP_SOURCE_CONFLICT')
                binding=request['credential']
                if (binding.get('placement')!='header' or not re.fullmatch(r'[A-Za-z0-9-]+',binding.get('name','')) or
                    binding.get('prefix') not in ('','Bearer ','OAuth ','Klaviyo-API-Key ')):
                    raise ValueError('INVALID_CREDENTIAL_BINDING')
        operation_count+=len(ops)
    if 'Activepieces Inc.' not in (DIRECTORY/'ACTIVEPIECES_LICENSE.txt').read_text(encoding='utf-8'):
        raise ValueError('MISSING_EXTENSION_LICENSE')
    return {"status":"CONNECTOR_CATALOG_VERIFIED","connectors":len(doc['connectors']),
            "categories":len({r["category"] for r in doc["connectors"]}),
            "specialist_roles":len(_roles()),"source_commit":PIN,
            "service_adapters":len(extensions),"service_operations":operation_count,
            "connector_code_executed":False,"external_effects":False}

def compare_catalogs(old:dict,new:dict)->dict:
    older={r["id"]:r for r in old["connectors"]}
    newer={r["id"]:r for r in new["connectors"]}
    return {"added":sorted(newer.keys()-older.keys()),"removed":sorted(older.keys()-newer.keys()),
            "changed":sorted(k for k in old_keys_and(newer,older) if older[k]!=newer[k]),"applied":False}


def specialist_package_files(role:str)->dict[str,bytes]:
    """Return a complete connector folder scoped to one specialist's services."""
    if role not in _roles():
        raise ValueError('UNKNOWN_SPECIALIST')
    doc=load_catalog()
    rows=[row for row in doc['connectors'] if role in row['specialists']]
    if not rows:
        raise ValueError('SPECIALIST_CONNECTORS_EMPTY')
    selected={row['id'] for row in rows if row.get('source_id')=='activepieces-community'}
    source=json.loads((DIRECTORY/'ADAPTER_SOURCES.json').read_bytes())
    source['connectors']=[record for record in source['connectors'] if record['id'] in selected]
    files={'connectors/connector.py':(DIRECTORY/'connector.py').read_bytes(),
           'connectors/ADAPTER_SOURCES.json':_canonical(source),
           'connectors/UPSTREAM_LICENSE.txt':(DIRECTORY/'UPSTREAM_LICENSE.txt').read_bytes(),
           'connectors/ACTIVEPIECES_LICENSE.txt':(DIRECTORY/'ACTIVEPIECES_LICENSE.txt').read_bytes()}
    for record in source['connectors']:
        for path,digest in record['files'].items():
            raw=(DIRECTORY/path).read_bytes()
            if _sha(raw)!=digest:
                raise ValueError('ADAPTER_FILE_CHANGED:'+path)
            files['connectors/'+path]=raw
    files['connectors/catalog.json']=_canonical({'schema':'muse-hub/specialist-connectors-v1',
        'specialist':role,'count':len(rows),'service_adapters':len(selected),'connectors':rows})
    lines=['# Connect your services','','Choose a service for this specialist and open its setup guide.','',
           f'**{len(rows)} recommended connectors**, including **{len(selected)} local service guides** with action inputs and examples.','',
           '| Service | Use it for |','| --- | --- |']
    for row in sorted(rows,key=lambda r:r['name'].casefold()):
        target=row.get('guide_path',row['source_url'])
        description=' '.join(row['description'].split()).replace('|','/')
        lines.append(f"| [{row['name']}]({target}) | {description} |")
    lines+=['','[Use the request helper](RUN_CONNECTORS.md) · [Specialist profile](../PROFILE.md)','']
    files['connectors/CATALOG.md']='\n'.join(lines).encode('utf-8')
    files['connectors/README.md']=(f'# Service connectors\n\nThis specialist includes {len(rows)} recommended connectors. '
        'Open [the service directory](CATALOG.md), choose a task and follow the selected guide.\n\n'
        '[Request helper](RUN_CONNECTORS.md) · [Specialist profile](../PROFILE.md)\n').encode('utf-8')
    files['CONNECTORS.md']=(f'# Connect your tools\n\n**{len(rows)} recommended service connectors** support this specialist. '
        'Browse [the included directory](connectors/CATALOG.md) for account setup, actions, inputs and examples.\n\n'
        'The local service guides live in `connectors/services/`. Open the guide for your chosen service, '
        'then give Muse the task and relevant workspace or record IDs.\n\n'
        '[Use the request helper](connectors/RUN_CONNECTORS.md) · [Specialist profile](PROFILE.md)\n').encode('utf-8')
    helper=['# Use the included connectors','','Run these commands from the `connectors` folder with Python 3.10 or later.','']
    adapters=[json.loads(files[f'connectors/services/{ident}/adapter.json']) for ident in sorted(selected)]
    example=next((a for a in adapters if any(op['kind']=='action' for op in a['operations'])),None)
    if example:
        action=next(op for op in example['operations'] if op['kind']=='action')
        helper+=['## Inspect actions and inputs','','```console',f"python connector.py inspect {example['id']}",'```','',
                 'Choose an action from the result, then save its named inputs as a JSON object.','',
                 '```console',f"python connector.py plan {example['id']} {action['id']} --inputs /absolute/path/inputs.json",'```','',
                 'The helper identifies missing required values and provider fields to resolve. Follow the linked request definition through your service connection.','']
    available=[]
    for ident in sorted(selected):
        key=f'connectors/services/{ident}/http.json'
        if key in files:
            available.extend((ident,request) for request in json.loads(files[key])['requests'])
    if available:
        ident,request=next(((ident,request) for ident,request in available if not request['parameters']),available[0])
        suffix=' --inputs /absolute/path/inputs.json' if request['parameters'] else ''
        helper+=['## Run a direct HTTP read','',
                 'Prepare the request first:','','```console',f"python connector.py read {ident} {request['id']}"+suffix,'```','',
                 'Supply an access token through your connection manager or local secret store, then pass its environment variable name and a new output path:','',
                 '```console',f"python connector.py read {ident} {request['id']}"+suffix+' --execute --token-env MUSE_SERVICE_TOKEN --output /absolute/path/result.json','```','',
                 'The result file includes the HTTP status and provider response. Keep record IDs and page cursors for subsequent workflow steps.','']
    helper+=['[Service directory](CATALOG.md) · [Specialist profile](../PROFILE.md)','']
    files['connectors/RUN_CONNECTORS.md']='\n'.join(helper).encode('utf-8')
    return files

def old_keys_and(a,b):
    return a.keys()&b.keys()

def compare_upstream(candidate:Path)->dict:
    path=Path(candidate)
    if not path.is_file() or path.stat().st_size>2_000_000 or path.is_symlink():
        raise ValueError("UNSAFE_CANDIDATE")
    rows=json.loads(path.read_bytes())
    if type(rows) is not list or len(rows)>500 or not all(type(v) is dict and type(v.get("id")) is str and ID.fullmatch(v["id"]) for v in rows):
        raise ValueError("INVALID_UPSTREAM_CANDIDATE")
    if len(set(r["id"] for r in rows))!=len(rows):
        raise ValueError("DUPLICATE_SOURCE_IDS")
    current=json.loads((DIRECTORY/"upstream-catalog.json").read_bytes())
    a={r["id"]:r for r in current};b={r["id"]:r for r in rows}
    return {"added":sorted(b.keys()-a.keys()),"removed":sorted(a.keys()-b.keys()),
            "changed":sorted(k for k in a.keys()&b.keys() if a[k]!=b[k]),
            "applied":False,"source_code_executed":False}

def export_catalog(destination:Path)->dict:
    result=check()
    p=Path(destination)
    if not p.is_absolute() or not p.parent.is_dir() or p.is_symlink() or ".." in p.parts:
        raise ValueError("UNSAFE_OUTPUT_PATH")
    proof=json.loads((DIRECTORY/'PROVENANCE.json').read_bytes())
    names=set(FILES)|{'PROVENANCE.json'}|{p.removeprefix('docs/connectors/') for p in proof['distributed_files']}
    contents={name:(DIRECTORY/name).read_bytes() for name in sorted(names)}
    hashes={"connectors/"+name:_sha(raw) for name,raw in sorted(contents.items())}
    manifest={"schema":"muse-specialist-toolkit/connector-export-v1","source_commit":PIN,
              "connector_count":result['connectors'],"files":hashes}
    with tempfile.TemporaryDirectory(dir=str(p.parent)) as td:
        stage=Path(td)/"catalog.zip"
        with zipfile.ZipFile(stage,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
            for name,raw in sorted(contents.items()):
                info=zipfile.ZipInfo("connectors/"+name,date_time=(2026,1,1,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED
                info.create_system=3
                info.external_attr=0o644<<16
                z.writestr(info,raw)
            info=zipfile.ZipInfo("MANIFEST.json",date_time=(2026,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.create_system=3
            info.external_attr=0o644<<16
            z.writestr(info,_canonical(manifest))
        with zipfile.ZipFile(stage) as z:
            if z.testzip() is not None or set(z.namelist())!=set(hashes)|{"MANIFEST.json"}:
                raise ValueError("PACKAGE_VERIFICATION_FAILED")
            for name,expected in hashes.items():
                if _sha(z.read(name))!=expected:raise ValueError("PACKAGE_HASH_MISMATCH")
        # Exclusive hard-link admission refuses a preexisting destination, no overwrite.
        os.link(stage,p)
    return dict(result,status="CONNECTOR_PACKAGE_EXPORTED",path=str(p),sha256=_sha(p.read_bytes()))

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="action",required=True)
    sub.add_parser("check")
    ex=sub.add_parser("export");ex.add_argument("--to",required=True,type=Path)
    cp=sub.add_parser("compare");cp.add_argument("--candidate",required=True,type=Path)
    args=parser.parse_args(argv)
    try:
        data=check() if args.action=="check" else export_catalog(args.to) if args.action=="export" else compare_upstream(args.candidate)
        print(json.dumps(data,sort_keys=True,ensure_ascii=False));return 0
    except (ValueError,OSError,TypeError,KeyError,json.JSONDecodeError) as error:
        print(json.dumps({"status":"REFUSED","reason":type(error).__name__+":"+str(error)[:150]}));return 2

if __name__=="__main__":raise SystemExit(main())
