"""Build complete Muse specialist, skill, workflow and starter downloads."""
from __future__ import annotations
import argparse, hashlib, importlib.util, io, json, re, subprocess, sys, zipfile
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from muse_presets.catalog import load_preset, load_registry
from muse_presets.playbooks import load_playbook, render_playbook
from muse_presets.product_copy import FIRST_TASKS
from muse_presets.standalone_pack import standalone_files
from muse_presets import portable_skill_export
from muse_presets import planner_package

def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

collection = _module("release_collection", ROOT / "tools/muse_collection.py")
legacy = _module("release_source_checks", ROOT / "scripts/build_v1_release.py")
connector_catalog = _module("release_connectors", ROOT / "scripts/connector_catalog.py")
REPOSITORY = "https://github.com/atlas-origins/muse-ai-agent-presets"
DEFAULT_VERSION = json.loads((ROOT / 'presets/catalog.json').read_bytes())['release']
SKILLS_PER_PACK = 40
INDIVIDUAL_SKILL_LIMIT = 600
MAX_RELEASE_ASSETS = 1000
ALIASES = {"data-engineering-architect":"data-engineer",
           "infrastructure-reliability-engineer":"reliability-engineer"}
ROLE_WORKFLOWS = {
    "coordinator": ["calm-day","priority-week","practical-plan","operations-review","conversation-prep"],
    "software-engineer": ["reproduce-to-repair","review-to-release"],
    "model-builder": ["model-evaluation"],
    "research-evaluator": ["evidence-brief","open-question","data-to-decision"],
    "creative-studio": ["brief-to-board","draft-to-delivery"],
    "adversarial-verifier": ["review-to-release"],
    "personal-companion": ["calm-day","priority-week","conversation-prep","practical-plan",
                           "visit-and-handoff","personal-routine"],
    "garden-companion": [],
    "learning-coach": ["exam-cycle","concept-repair","practice-cycle"],
    "claims-adjudicator": [],
    "reverse-engineering-researcher": [],
    "data-engineering-architect": ["pipeline-validation","data-to-decision"],
    "infrastructure-reliability-engineer": ["incident-recovery"],
    "automation-engineer": ["automation-readiness","product-to-implementation","interface-quality"],
    "product-interface-designer": ["interface-quality","product-to-implementation"],
}

VERIFY = r'''"""Verify the files shipped in this extracted package."""
from pathlib import Path, PurePosixPath
import hashlib, json, re, sys
root = Path(__file__).resolve().parent
try:
    manifest = json.loads((root / 'MANIFEST.json').read_bytes())
    members = manifest['files']
    if not isinstance(members,dict) or not 1 <= len(members) <= 60000:
        raise ValueError('INVALID_FILE_ROSTER')
    seen = set()
    for name, expected in members.items():
        if not isinstance(name,str) or name.casefold() in seen:
            raise ValueError('DUPLICATE_PORTABLE_PATH')
        seen.add(name.casefold())
        path = PurePosixPath(name)
        if (not name or path.is_absolute() or any(p in ('','.','..') for p in name.split('/'))
                or '\\' in name or ':' in name or path.as_posix() != name
                or not isinstance(expected,str) or re.fullmatch('[0-9a-f]{64}',expected) is None):
            raise ValueError('UNSAFE_MANIFEST_ENTRY')
        target = root / name
        for current in (target, *target.parents):
            if current == root: break
            if current.is_symlink() or (getattr(current.lstat(),'st_file_attributes',0) & 0x400):
                raise ValueError('LINKED_MEMBER')
        if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            raise ValueError('MEMBER_CHANGED:' + name)
    print(json.dumps({'status':'PASS','files_verified':len(members),'package':manifest['id']}))
except (OSError, ValueError, KeyError, TypeError) as exc:
    print(json.dumps({'status':'FAIL','error':str(exc)}), file=sys.stderr)
    raise SystemExit(2)
'''

def _json(value):
    return (json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+"\n").encode("utf-8")

def _sha(raw): return hashlib.sha256(raw).hexdigest()

def _version(value):
    if not isinstance(value,str) or not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+",value):
        raise ValueError("INVALID_RELEASE_VERSION")
    return value

def asset_url(name,version):
    return REPOSITORY+"/releases/download/"+_version(version)+"/"+name

def specialist_asset(role,version):
    if role not in ROLE_WORKFLOWS: raise ValueError("UNKNOWN_SPECIALIST")
    return "muse-"+ALIASES.get(role,role)+"-"+_version(version)+".zip"

def planner_asset(version=DEFAULT_VERSION):
    return 'muse-space-planner-' + _version(version) + '.zip'

def _seal(files,kind,identity,version,**details):
    result=dict(files)
    if "MANIFEST.json" in result: raise ValueError("OUTER_MANIFEST_COLLISION")
    result.setdefault("LICENSE",(ROOT/"LICENSE").read_bytes())
    result["VERIFY.py"]=VERIFY.encode("utf-8")
    result["MANIFEST.json"]=_json({"schema":"muse-download-package/v1","kind":kind,
        "id":identity,"version":_version(version),**details,
        "files":{name:_sha(raw) for name,raw in sorted(result.items())}})
    return result

def _use_text(title,entry,*,files):
    text=("# "+title+"\n\n"
        "1. Extract this ZIP into its own folder.\n"
        "2. Open "+entry+". Give Muse this folder or ZIP and your current task.\n"
        '3. Ask: "Use these instructions for my task, keeping my existing preferences and memory."\n\n'
        "Use the Markdown instructions through your existing Muse file or terminal workflow. "
        "No Python is required for that use.\n\n"
        "## Check the downloaded files\n\nWith Python 3.10 or newer, run from the extracted folder:\n\n"
        "    python -B VERIFY.py\n")
    if 'tools/run.py' in files:
        text+=("\n## Try the included local tools\n\nThe examples use Python 3.10 or newer and the standard library:\n\n"
               "    python -B tools/run.py --demo\n\nSee tools/README.md for your own JSON input.\n")
    return text+collection.resource_start_guide(files)

def specialist_files(data,role,version=DEFAULT_VERSION):
    if role not in load_registry()["presets"]: raise ValueError("UNKNOWN_SPECIALIST")
    alias=ALIASES.get(role,role)
    entry=next((s for s in data["specialists"] if s["id"]==alias),None)
    if entry is None: raise ValueError("SPECIALIST_COLLECTION_MAPPING_MISSING")
    preset,book=load_preset(role),load_playbook(role)
    workflows=list(dict.fromkeys(ROLE_WORKFLOWS[role]+entry.get('library_workflows',[])))
    files=collection.instruction_files(data,entry["skills"]+entry.get('library_skills',[]),workflows)
    import tool_guides
    guides=tool_guides.load_guides()
    flow_index={w['id']:w for w in data['workflows']}
    guide_ids=sorted(set(tool_guides.selected_ids(guides,role=alias))|
        {gid for key in workflows for gid in flow_index[key].get('tool_guides',[])})
    files.update(tool_guides.package_files(guides,ids=guide_ids))
    files.update({"assistant/"+name:raw for name,raw in standalone_files(role).items()})
    files.update(connector_catalog.specialist_package_files(role))
    spaces = ['planner'] if role in planner_package.ROLES else []
    if spaces:
        files.update(planner_package.package_files(ROOT))
    connectors=json.loads(files['connectors/catalog.json'])['connectors']
    selected=sorted(name.split("/")[1] for name in files
                    if name.startswith("skills/") and name.endswith("/SKILL.md"))
    title=preset["title"]
    skills={s["id"]:s for s in data["skills"]};flows={w["id"]:w for w in data["workflows"]}
    files["AGENTS.md"]=("# "+title+"\n\n"+preset["description"]+"\n\n"
        "Read PROFILE.md and ROLE_PLAYBOOK.md. Select the skills and workflows relevant "
        "to the user's current task. Keep the existing assistant identity, preferences, memory "
        "and tool permissions. Use observed results to decide what has completed; reconcile "
        "an uncertain external action before retrying it.\n").encode()
    profile="# "+title+"\n\n"+preset["description"]+"\n\n## Skills\n\n"
    profile+="\n".join("- ["+skills[k]["title"]+"](skills/"+k+"/SKILL.md)" for k in selected)+"\n"
    if workflows:
        profile+="\n## Workflows\n\n"+"\n".join("- ["+flows[k]["title"]+"](workflows/"+k+".md)" for k in workflows)+"\n"
    profile+="\n## First task\n\nRead [FIRST_TASK.md](FIRST_TASK.md), or start with your current request.\n"
    if guide_ids:
        profile+="\n## Recommended tools\n\nRead [the tool guides](TOOL_GUIDES.md) for setup, practical recipes and result checks.\n"
    profile+="\n## Connect your services\n\nUse [the connector directory](CONNECTORS.md) for the "+str(len(connectors))+" services selected for this specialist.\n"
    planner_note=("\n## Plan in your Muse Space\n\n"
        "Open [Muse Planner](spaces/planner/README.md) to set up a saved workspace for "
        "projects, next actions, routines, reference notes and your weekly review. "
        "The complete app is in `spaces/planner/`; its guide covers Muse Space setup, "
        "Bun, the host SDK, calendar settings and portable backups.\n") if spaces else ''
    profile+=planner_note
    if spaces:
        files['AGENTS.md']+=planner_note.encode('utf-8')
    files["PROFILE.md"]=profile.encode()
    files["ROLE_PLAYBOOK.md"]=render_playbook(book,display_name=title,role_title=title).encode()
    files["FIRST_TASK.md"]=("# Try "+title+"\n\n"+FIRST_TASKS[role]+
        "\n\n## Choose a method\n\nOpen [PROFILE.md](PROFILE.md) and select the skill or workflow that fits your task. "
        "Bring its requested inputs, follow the method, and check the result against its expected outputs.\n\n"
        "## Keep the result\n\nSave the finished work with your project, including useful source links, "
        "calculations or checks. Record the next action so you can resume easily.\n\n"
        "[Working methods and examples](ROLE_PLAYBOOK.md) · [Service connectors](CONNECTORS.md)\n").encode()
    if spaces:
        files['FIRST_TASK.md']+=planner_note.encode('utf-8')
    start=_use_text("Start with "+title,"PROFILE.md",files=files)
    start+="\n## Connect your tools\n\nOpen [CONNECTORS.md](CONNECTORS.md) for service guides, action inputs and the included request helper.\n"
    start+=("\n## Use the host-format components\n\n"
        "- Profile documents: assistant/system-profile/profile/.\n"
        "- Scoped task contexts: assistant/subchat-scopes/subchats/.\n"
        "- Role and shared skills: assistant/role-skills/custom-skills/.\n\n"
        "Use your current host's supported import controls for those components. "
        "Keep the extracted package separate from the live assistant home. Review changes "
        "before importing; preserve existing identity, memory and preference files. "
        "For the current task, Muse can read AGENTS.md, PROFILE.md and the selected skills directly.\n")
    files["START_HERE.md"]=(start+planner_note).encode()
    files["SPECIALIST.json"]=_json({"id":role,"collection_id":alias,"title":title,"skills":selected,
        "workflows":workflows,"methods":[m["id"] for m in book["methods"]],"tool_guides":guide_ids,
        "connectors":[row['id'] for row in connectors],"spaces":spaces})
    return _seal(files,"specialist",role,version,skills=selected,workflows=workflows,spaces=spaces)

def planner_files(version=DEFAULT_VERSION):
    files = planner_package.package_files(ROOT)
    files['START_HERE.md'] = ("# Muse Planner\n\n"
        "Turn ideas into projects, choose the next action, and keep your routines and notes "
        "together in a persistent Muse Space.\n\n"
        "1. Extract this ZIP into its own folder.\n"
        "2. Open [the Planner setup guide](spaces/planner/README.md) and give Muse the "
        "complete `spaces/planner/` folder.\n"
        "3. Create a TypeScript Space, prepare its host SDK, install the locked dependencies "
        "with Bun, and build it using the guide.\n"
        "4. Capture an inbox item, create a project and next action, then reopen the Space "
        "and export your first backup.\n\n"
        "The same app is included with Coordinator and Personal Companion. "
        "Use it with your existing Muse assistant to plan a project or review the week.\n\n"
        "## Check the downloaded files\n\n"
        "With Python 3.10 or newer, run from the extracted folder:\n\n"
        "    python -B VERIFY.py\n").encode('utf-8')
    return _seal(files, 'space', 'planner', version,
        entry=planner_package.PACKAGE_PATH+'/README.md',
        source_files=planner_package.SOURCE_FILE_COUNT,
        specialists=list(planner_package.ROLES))

def skill_files(data,identity,version=DEFAULT_VERSION):
    entry=next((s for s in data["skills"] if s["id"]==identity),None)
    if entry is None: raise ValueError("UNKNOWN_SKILL")
    files=collection.instruction_files(data,[identity],[])
    files["START_HERE.md"]=_use_text(entry["title"],"skills/"+identity+"/SKILL.md",files=files).encode()
    detail=(" and [DEPTH.md](skills/"+identity+"/DEPTH.md) when you need examples or recovery steps" if entry.get('depth') else '')
    files["AGENTS.md"]=("# "+entry["title"]+"\n\nRead [SKILL.md](skills/"+identity+
        "/SKILL.md) for this task"+detail+". "
        "Keep the existing assistant preferences, memory and tool permissions.\n").encode()
    return _seal(files,"developed-skill",identity,version,skills=[identity])


def skill_download_layout(data, version=DEFAULT_VERSION):
    """Give each skill a stable entry point while keeping large releases bounded.

    Small catalogs retain their individual ZIPs. Larger catalogs retain the
    original authored-skill ZIPs and group portable skills by subject and ID.
    Both the website and the release builder consume this exact mapping.
    """
    _version(version)
    rows = data['skills']
    if not isinstance(rows, list) or not rows:
        raise ValueError('SKILL_INVENTORY_REQUIRED')
    by_id = {}
    subjects = defaultdict(list)
    layout = {}
    grouped = len(rows) > INDIVIDUAL_SKILL_LIMIT
    for row in rows:
        identity, category = row['id'], row['category']
        if (not isinstance(identity, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identity)
                or not isinstance(category, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', category)
                or identity in by_id):
            raise ValueError('INVALID_SKILL_DOWNLOAD_IDENTITY')
        by_id[identity] = row
        if grouped and row.get('format') == 'portable-skill':
            subjects[category].append(identity)
        else:
            layout[identity] = {'asset': f'muse-skill-{identity}-{version}.zip',
                'entry': f'skills/{identity}/SKILL.md', 'pack_id': identity,
                'pack_title': row['title'], 'pack_size': 1, 'pack_kind': 'skill'}
    for category, identities in sorted(subjects.items()):
        identities.sort()
        for start in range(0, len(identities), SKILLS_PER_PACK):
            selected = identities[start:start + SKILLS_PER_PACK]
            number = start // SKILLS_PER_PACK + 1
            pack_id = f'{category}-{number:03d}'
            title = category.replace('-', ' ').capitalize() + f' · Pack {number}'
            for identity in selected:
                layout[identity] = {'asset': f'muse-skills-{pack_id}-{version}.zip',
                    'entry': f'skills/{identity}/SKILL.md', 'pack_id': pack_id,
                    'pack_title': title, 'pack_size': len(selected), 'pack_kind': 'skill-pack'}
    return dict(sorted(layout.items()))


def skill_pack_files(data, identities, pack, version=DEFAULT_VERSION):
    """Compose a subject pack with each skill's complete supporting files."""
    by_id = {row['id']: row for row in data['skills']}
    selected = sorted(identities)
    if not selected or len(selected) > SKILLS_PER_PACK or len(set(selected)) != len(selected):
        raise ValueError('INVALID_SKILL_PACK_SELECTION')
    files = collection.instruction_files(data, selected, [])
    links = '\n'.join('- [' + by_id[key]['title'] + '](skills/' + key + '/SKILL.md) — '
                      + by_id[key]['trigger'] for key in selected)
    index = '# ' + pack['pack_title'] + '\n\nChoose the method that fits your task.\n\n' + links + '\n'
    files['SKILLS.md'] = index.encode('utf-8')
    files['AGENTS.md'] = (index + '\nLoad only the selected skill and its supporting files for the current task. '
                         'Keep the assistant\'s existing preferences and memory.\n').encode('utf-8')
    files['START_HERE.md'] = _use_text(pack['pack_title'], 'SKILLS.md', files=files).encode('utf-8')
    return _seal(files, 'skill-pack', pack['pack_id'], version, skills=selected)

def workflow_files(data,identity,version=DEFAULT_VERSION):
    entry=next((w for w in data["workflows"] if w["id"]==identity),None)
    if entry is None: raise ValueError("UNKNOWN_WORKFLOW")
    files=collection.instruction_files(data,[],[identity])
    files["START_HERE.md"]=_use_text(entry["title"],"workflows/"+identity+".md",files=files).encode()
    files["AGENTS.md"]=("# "+entry["title"]+"\n\n"+entry["goal"]+"\n\nFollow workflows/"+
        identity+".md, loading each included skill when needed. Preserve real outputs between "
        "steps and follow the user's current authorization for external actions.\n").encode()
    return _seal(files,"workflow",identity,version,skills=entry["skills"],workflows=[identity])

def verify_archive(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        if archive.testzip() is not None: raise ValueError("ZIP_CRC_FAILED")
        names=archive.namelist();manifest=json.loads(archive.read("MANIFEST.json"))
        if len(names)!=len(set(names)) or set(names)!=set(manifest["files"])|{"MANIFEST.json"}:
            raise ValueError("ZIP_ROSTER_MISMATCH")
        for name,expected in manifest["files"].items():
            if _sha(archive.read(name))!=expected: raise ValueError("ZIP_MEMBER_CHANGED")
        return manifest

def _zip(files):
    raw=collection.build_file_map_bytes(files,max_files=60000,
        max_member_bytes=512_000_000,max_total_bytes=1_000_000_000)
    verify_archive(raw)
    return raw

def _bundle(title,identity,members,version):
    files={"packages/"+name:raw for name,raw in members.items()}
    files["START_HERE.md"]=("# "+title+"\n\nChoose one ZIP from packages/, extract it into "
        "its own folder, and open START_HERE.md. Each package includes its required instructions "
        "and examples.\n\nWith Python 3.10 or newer, run python -B VERIFY.py to check this bundle.\n").encode()
    files["PACKAGES.json"]=_json({"packages":[{"asset":n,"bytes":len(b),"sha256":_sha(b)}
                                             for n,b in sorted(members.items())]})
    return _zip(_seal(files,"bundle",identity,version))

def compose_downloads(data,version=DEFAULT_VERSION):
    _version(version)
    data=collection.prepare_collection(data)
    if len(data['specialists'])!=15 or len(data['starters'])<100:
        raise ValueError("COLLECTION_INVENTORY_MISMATCH")
    archives={};records={"specialists":[],"skills":[],"workflows":[],"tool-guides":[],"bundles":[]}
    groups={"specialists":{},"skills":{},"workflows":{},"starters":{},"tool-guides":{}}
    for role in load_registry()["presets"]:
        name=specialist_asset(role,version);raw=_zip(specialist_files(data,role,version))
        archives[name]=groups["specialists"][name]=raw;manifest=verify_archive(raw)
        records["specialists"].append({"id":role,"role":role,"download_id":ALIASES.get(role,role),
            "title":load_preset(role)["title"],"asset":name,"url":asset_url(name,version),
            "bytes":len(raw),"sha256":_sha(raw),"skills":len(manifest["skills"]),
            "workflows":len(manifest["workflows"])})
    layout = skill_download_layout(data, version)
    skill_by_id = {row['id']: row for row in data['skills']}
    pack_members = defaultdict(list)
    for identity, entry in layout.items():
        pack_members[entry['asset']].append(identity)
    for name, identities in sorted(pack_members.items()):
        entry = layout[identities[0]]
        files = (skill_files(data, identities[0], version) if entry['pack_kind'] == 'skill'
                 else skill_pack_files(data, identities, entry, version))
        raw = _zip(files)
        archives[name] = groups['skills'][name] = raw
        for identity in identities:
            row = skill_by_id[identity]
            records['skills'].append({'id': identity, 'title': row['title'], 'summary': row['trigger'],
                **layout[identity], 'url': asset_url(name, version), 'bytes': len(raw), 'sha256': _sha(raw)})
    records['skills'].sort(key=lambda row: row['id'])
    for category,rows,build in (("workflows",data["workflows"],workflow_files),):
        kind="skill" if category=="skills" else "workflow"
        for row in rows:
            name="muse-"+kind+"-"+row["id"]+"-"+version+".zip";raw=_zip(build(data,row["id"],version))
            archives[name]=groups[category][name]=raw
            records[category].append({"id":row["id"],"title":row["title"],
                "summary":row.get("trigger",row.get("goal","")),"asset":name,"url":asset_url(name,version),
                "bytes":len(raw),"sha256":_sha(raw)})
    for row in data["starters"]:
        files=collection.package_files(data,row["id"]);files.pop("MANIFEST.json")
        groups["starters"]["muse-starter-"+row["id"]+"-"+version+".zip"]=_zip(
            _seal(files,"starter",row["id"],version))
    import tool_guides
    guides=tool_guides.load_guides()
    for row in guides['guides']:
        name='muse-tool-'+row['id']+'-'+version+'.zip'
        files=tool_guides.package_files(guides,ids=[row['id']])
        files['START_HERE.md']=_use_text(row['name']+' guide','TOOL_GUIDES.md',files=files).encode()
        raw=_zip(_seal(files,'tool-guide',row['id'],version))
        archives[name]=groups['tool-guides'][name]=raw
        records['tool-guides'].append({'id':row['id'],'title':row['name'],'summary':row['summary'],
            'asset':name,'url':asset_url(name,version),'bytes':len(raw),'sha256':_sha(raw)})
    for category in groups:
        if not groups[category]:continue
        name="muse-"+category+"-"+version+".zip";raw=_bundle("Muse "+category,category,groups[category],version)
        archives[name]=raw
        records["bundles"].append({"id":category,"asset":name,"url":asset_url(name,version),
            "packages":len(groups[category]),"bytes":len(raw),"sha256":_sha(raw)})
    files,receipt=portable_skill_export._build()
    files[portable_skill_export.MANIFEST]=portable_skill_export._json(receipt)
    name="muse-role-procedures-50-"+version+".zip"
    raw=_zip(_seal(files,"role-procedure-library","role-procedures-50",version,procedures=receipt["unique_skills"]))
    archives[name]=raw
    records["bundles"].append({"id":"role-procedures-50","asset":name,"url":asset_url(name,version),
        "procedures":50,"bytes":len(raw),"sha256":_sha(raw)})
    name=planner_asset(version);raw=_zip(planner_files(version))
    archives[name]=raw
    records['bundles'].append({'id':'space-planner','title':'Muse Planner',
        'asset':name,'url':asset_url(name,version),'bytes':len(raw),'sha256':_sha(raw),
        'entry':planner_package.PACKAGE_PATH+'/README.md',
        'source_files':planner_package.SOURCE_FILE_COUNT,'specialists':list(planner_package.ROLES)})
    # The source ZIP and six index/checksum files are added by build_release.
    if len(archives) + 7 > MAX_RELEASE_ASSETS:
        raise ValueError('RELEASE_ASSET_LIMIT_EXCEEDED')
    return archives,records

def _source_archive(version,manifest):
    prefix="muse-specialist-toolkit-"+version+"/"
    proc=subprocess.run(["git","-C",str(ROOT),"archive","--format=zip","--prefix="+prefix,"HEAD"],
                        capture_output=True,timeout=60)
    if proc.returncode: raise ValueError("SOURCE_ARCHIVE_FAILED")
    with zipfile.ZipFile(io.BytesIO(proc.stdout)) as archive:
        expected=set(manifest["files"])|{"PUBLIC_SOURCE_MANIFEST.json"}
        names={n[len(prefix):] for n in archive.namelist() if not n.endswith("/")}
        if archive.testzip() is not None or names!=expected: raise ValueError("SOURCE_ARCHIVE_ROSTER_MISMATCH")
        for name,digest in manifest["files"].items():
            if _sha(archive.read(prefix+name))!=digest: raise ValueError("SOURCE_ARCHIVE_DIGEST_MISMATCH")
    return proc.stdout

def build_release(destination,expected_head,version=DEFAULT_VERSION):
    _version(version)
    if version != DEFAULT_VERSION:
        raise ValueError("RELEASE_VERSION_MISMATCH")
    target = collection._safe_path(Path(destination))
    if not target.is_absolute() or target.exists() or not target.parent.is_dir():
        raise ValueError("NEW_ABSOLUTE_OUTPUT_DIRECTORY_REQUIRED")
    if target.is_relative_to(ROOT): raise ValueError("RELEASE_OUTPUT_MUST_BE_OUTSIDE_SOURCE")
    state=legacy.verify_checkout(ROOT,expected_head)
    legacy._run(ROOT,[sys.executable,"-B","scripts/check_public.py"])
    data=collection.load_collection()
    archives,records=compose_downloads(data,version)
    toolkit="muse-specialist-toolkit-"+version+".zip"
    archives[toolkit]=_source_archive(version,json.loads((ROOT/"PUBLIC_SOURCE_MANIFEST.json").read_bytes()))
    records["bundles"].append({"id":"toolkit","asset":toolkit,"url":asset_url(toolkit,version),
        "bytes":len(archives[toolkit]),"sha256":_sha(archives[toolkit])})
    if legacy.verify_checkout(ROOT,expected_head)!=state: raise ValueError("SOURCE_CHANGED_DURING_BUILD")
    metadata={
        "SPECIALIST_DOWNLOADS.json":_json({"schema":"muse-specialist-downloads/v2","version":version,
            "source_head":expected_head,"role_count":15,"specialists":records["specialists"]}),
        "SKILL_DOWNLOADS.json":_json({"schema":"muse-skill-downloads/v1","version":version,
            "source_head":expected_head,"skill_count":len(records['skills']),"skills":records["skills"]}),
        "WORKFLOW_DOWNLOADS.json":_json({"schema":"muse-workflow-downloads/v1","version":version,
            "source_head":expected_head,"workflow_count":len(records['workflows']),"workflows":records["workflows"]}),
        "RELEASE_MANIFEST.json":_json({"schema":"muse-release/v2","version":version,"source":state,
            "downloads":records,"assets":{n:{"bytes":len(b),"sha256":_sha(b)} for n,b in sorted(archives.items())}}),
    }
    guide="# Muse downloads "+version+"\n\nChoose a specialist, skill, or workflow, extract its ZIP, and open START_HERE.md. Use the instructions with your existing Muse assistant.\n\n"
    for category,rows in records.items():
        guide+="## "+category.title()+"\n\n"
        guide+="".join("- ["+row.get("title",row["id"])+"]("+row["url"]+")\n" for row in rows)+"\n"
    guide+="SHA256SUMS lists the exact SHA-256 digest of every downloadable ZIP and index.\n"
    metadata["DOWNLOADS.md"]=guide.encode()
    all_files={**archives,**metadata}
    sums="".join(_sha(raw)+"  "+name+"\n" for name,raw in sorted(all_files.items()))
    target.mkdir();marker=target/"BUILD_INCOMPLETE";marker.write_bytes(b"BUILD_INCOMPLETE\n")
    for name,raw in all_files.items():
        with (target/name).open("xb") as stream: stream.write(raw)
        if (target/name).read_bytes()!=raw: raise ValueError("ARTIFACT_READBACK_FAILED")
    (target/"SHA256SUMS").write_text(sums,encoding="ascii",newline="\n")
    result={"status":"COMPLETE","version":version,"source":state,"zip_count":len(archives),
        "specialists":15,"developed_skills":len(records['skills']),"workflows":len(records['workflows']),
        "tool_guides":len(records['tool-guides']),"starters_in_bundle":len(data['starters']),
        "separate_role_procedures":50,"published":False,
        "artifacts":{n:{"bytes":len(b),"sha256":_sha(b)} for n,b in sorted(all_files.items())}}
    (target/"BUILD_RECEIPT.json").write_bytes(_json(result));marker.unlink()
    return result

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--to",required=True,type=Path)
    parser.add_argument("--expected-head",required=True)
    parser.add_argument("--version",default=DEFAULT_VERSION)
    args=parser.parse_args(argv)
    try:
        print(json.dumps(build_release(args.to,args.expected_head,args.version),sort_keys=True));return 0
    except (ValueError,OSError,KeyError,TypeError,zipfile.BadZipFile) as exc:
        print(json.dumps({"status":"REFUSED","error":str(exc)}),file=sys.stderr);return 2

if __name__=="__main__": raise SystemExit(main())
