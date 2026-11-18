"""Build complete Muse specialist, skill, workflow and starter downloads."""
from __future__ import annotations
import argparse, hashlib, importlib.util, io, json, re, subprocess, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from muse_presets.catalog import load_preset, load_registry
from muse_presets.playbooks import load_playbook, render_playbook
from muse_presets.standalone_pack import standalone_files
from muse_presets import portable_skill_export

def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

collection = _module("release_collection", ROOT / "tools/muse_collection.py")
legacy = _module("release_source_checks", ROOT / "scripts/build_v1_release.py")
REPOSITORY = "https://github.com/atlas-origins/muse-ai-agent-presets"
DEFAULT_VERSION = "v1.1.1"
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
    if not isinstance(members,dict) or not 1 <= len(members) <= 1000:
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

def _seal(files,kind,identity,version,**details):
    result=dict(files)
    if "MANIFEST.json" in result: raise ValueError("OUTER_MANIFEST_COLLISION")
    result.setdefault("LICENSE",(ROOT/"LICENSE").read_bytes())
    result["VERIFY.py"]=VERIFY.encode("utf-8")
    result["MANIFEST.json"]=_json({"schema":"muse-download-package/v1","kind":kind,
        "id":identity,"version":_version(version),**details,
        "files":{name:_sha(raw) for name,raw in sorted(result.items())}})
    return result

def _use_text(title,entry,*,optional_tools=False):
    text=("# "+title+"\n\n"
        "1. Extract this ZIP into its own folder.\n"
        "2. Open "+entry+". Give Muse this folder or ZIP and your current task.\n"
        '3. Ask: "Use these instructions for my task, keeping my existing preferences and memory."\n\n'
        "Use the Markdown instructions through your existing Muse file or terminal workflow. "
        "No Python is required for that use.\n\n"
        "## Check the downloaded files\n\nWith Python 3.10 or newer, run from the extracted folder:\n\n"
        "    python -B VERIFY.py\n")
    if optional_tools:
        text+=("\n## Try the included local tools\n\nThe examples use Python 3.10 or newer and the standard library:\n\n"
               "    python -B tools/run.py --demo\n\nSee tools/README.md for your own JSON input.\n")
    return text

def specialist_files(data,role,version=DEFAULT_VERSION):
    if role not in load_registry()["presets"]: raise ValueError("UNKNOWN_SPECIALIST")
    alias=ALIASES.get(role,role)
    entry=next((s for s in data["specialists"] if s["id"]==alias),None)
    if entry is None: raise ValueError("SPECIALIST_COLLECTION_MAPPING_MISSING")
    preset,book=load_preset(role),load_playbook(role)
    workflows=ROLE_WORKFLOWS[role]
    files=collection.instruction_files(data,entry["skills"],workflows)
    files.update({"assistant/"+name:raw for name,raw in standalone_files(role).items()})
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
    files["PROFILE.md"]=profile.encode()
    files["ROLE_PLAYBOOK.md"]=render_playbook(book,display_name=title,role_title=title).encode()
    first=book["first_canary"]
    files["FIRST_TASK.md"]=("# Try "+title+"\n\n"+first["task"]+"\n\n## Expected result\n\n"+
        first["observable_result"]+"\n\n## Check an edge case\n\n"+first["negative_test"]+"\n").encode()
    start=_use_text("Start with "+title,"PROFILE.md",optional_tools="tools/run.py" in files)
    start+=("\n## Use the host-format components\n\n"
        "- Profile documents: assistant/system-profile/profile/.\n"
        "- Scoped task contexts: assistant/subchat-scopes/subchats/.\n"
        "- Role and shared skills: assistant/role-skills/custom-skills/.\n\n"
        "Use your current host's supported import controls for those components. "
        "Keep the extracted package separate from the live assistant home. Review changes "
        "before importing; preserve existing identity, memory and preference files. "
        "For the current task, Muse can read AGENTS.md, PROFILE.md and the selected skills directly.\n")
    files["START_HERE.md"]=start.encode()
    files["SPECIALIST.json"]=_json({"id":role,"collection_id":alias,"title":title,"skills":selected,
        "workflows":workflows,"methods":[m["id"] for m in book["methods"]],
        "native_installed":False,"external_effect_authorized":False})
    return _seal(files,"specialist",role,version,skills=selected,workflows=workflows)

def skill_files(data,identity,version=DEFAULT_VERSION):
    entry=next((s for s in data["skills"] if s["id"]==identity),None)
    if entry is None: raise ValueError("UNKNOWN_SKILL")
    files=collection.instruction_files(data,[identity],[])
    files["START_HERE.md"]=_use_text(entry["title"],"skills/"+identity+"/SKILL.md",
        optional_tools="tools/run.py" in files).encode()
    files["AGENTS.md"]=("# "+entry["title"]+"\n\nRead [SKILL.md](skills/"+identity+
        "/SKILL.md) for this task and [DEPTH.md](skills/"+identity+
        "/DEPTH.md) when you need examples or recovery steps. "
        "Keep the existing assistant preferences, memory and tool permissions.\n").encode()
    return _seal(files,"developed-skill",identity,version,skills=[identity])

def workflow_files(data,identity,version=DEFAULT_VERSION):
    entry=next((w for w in data["workflows"] if w["id"]==identity),None)
    if entry is None: raise ValueError("UNKNOWN_WORKFLOW")
    files=collection.instruction_files(data,[],[identity])
    files["START_HERE.md"]=_use_text(entry["title"],"workflows/"+identity+".md",
        optional_tools="tools/run.py" in files).encode()
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
    raw=collection.build_file_map_bytes(files);verify_archive(raw);return raw

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
    if tuple(len(data[k]) for k in ("specialists","skills","workflows","starters"))!=(15,75,25,100):
        raise ValueError("REVIEW_CHANGED_COLLECTION_INVENTORY")
    archives={};records={"specialists":[],"skills":[],"workflows":[],"bundles":[]}
    groups={"specialists":{},"skills":{},"workflows":{},"starters":{}}
    for role in load_registry()["presets"]:
        name=specialist_asset(role,version);raw=_zip(specialist_files(data,role,version))
        archives[name]=groups["specialists"][name]=raw;manifest=verify_archive(raw)
        records["specialists"].append({"id":role,"role":role,"download_id":ALIASES.get(role,role),
            "title":load_preset(role)["title"],"asset":name,"url":asset_url(name,version),
            "bytes":len(raw),"sha256":_sha(raw),"skills":len(manifest["skills"]),
            "workflows":len(manifest["workflows"])})
    for category,rows,build in (("skills",data["skills"],skill_files),("workflows",data["workflows"],workflow_files)):
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
    for category in groups:
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
    _version(version);target=collection._safe_path(Path(destination))
    if not target.is_absolute() or target.exists() or not target.parent.is_dir():
        raise ValueError("NEW_ABSOLUTE_OUTPUT_DIRECTORY_REQUIRED")
    if target.is_relative_to(ROOT): raise ValueError("RELEASE_OUTPUT_MUST_BE_OUTSIDE_SOURCE")
    state=legacy.verify_checkout(ROOT,expected_head)
    legacy._run(ROOT,[sys.executable,"-B","scripts/check_public.py"])
    archives,records=compose_downloads(collection.load_collection(),version)
    toolkit="muse-specialist-toolkit-"+version+".zip"
    archives[toolkit]=_source_archive(version,json.loads((ROOT/"PUBLIC_SOURCE_MANIFEST.json").read_bytes()))
    records["bundles"].append({"id":"toolkit","asset":toolkit,"url":asset_url(toolkit,version),
        "bytes":len(archives[toolkit]),"sha256":_sha(archives[toolkit])})
    if legacy.verify_checkout(ROOT,expected_head)!=state: raise ValueError("SOURCE_CHANGED_DURING_BUILD")
    metadata={
        "SPECIALIST_DOWNLOADS.json":_json({"schema":"muse-specialist-downloads/v2","version":version,
            "source_head":expected_head,"role_count":15,"specialists":records["specialists"]}),
        "SKILL_DOWNLOADS.json":_json({"schema":"muse-skill-downloads/v1","version":version,
            "source_head":expected_head,"skill_count":75,"skills":records["skills"]}),
        "WORKFLOW_DOWNLOADS.json":_json({"schema":"muse-workflow-downloads/v1","version":version,
            "source_head":expected_head,"workflow_count":25,"workflows":records["workflows"]}),
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
        "specialists":15,"developed_skills":75,"workflows":25,"starters_in_bundle":100,
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
