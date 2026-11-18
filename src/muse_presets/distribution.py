"""Check Muse Hub product pages, functionality, privacy and package integrity."""
from __future__ import annotations
import hashlib,json,os,re,tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

IGNORED={'.git','__pycache__','.pytest_cache','.mypy_cache','.ruff_cache','.venv','venv'}
PRIVATE_DIRS={'control','.atlas','scratch','evidence','receipts','checkpoints'}
OLD_DOCS={'STATUS.md','GITHUB_ROLE_ACCEPTANCE.md','GITHUB_RELEASE_SCOPE.md',
 'CAPABILITY_FIT_AUDIT.md','RELEASE_CHECKLIST.md','PRIVACY_RELEASE_ASSURANCE.md',
 'COMMUNITY_RESEARCH.md','NEUTRALITY_AND_PROVENANCE.md'}
WORK_ID=re.compile(r'\b(?:R\d{2,}|T\d{2,})(?:\b|_)|\bAsana\b|\bprepush\b|\bsource candidate\b',re.I)
MILESTONE=re.compile(r'^R\d{2,}[_-]',re.I)
LINK=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
MODULE=re.compile(r'^muse_presets\.[a-z][a-z0-9_]*$')
MAX_TEXT=2_000_000
RELEASE_JARGON=re.compile(r'\bsource[- ]only\b|\bnot additional agents\b|\bno authenticated cross-account\b|\bnot a claim that\b',re.I)

# Domain identifiers such as MITRE techniques, grant mechanisms and ResNet models.
# A changed file is scanned again and must receive an explicit content review.
REVIEWED_DOMAIN_TEXT = {'collections/library/skills/ai-security/SKILL.md': 'fba7802c2c1aebf652d6e6521658a4b0c34c2d06f8aa6f50567418f3e93aa2fe',
 'collections/library/skills/ai-security/references/atlas-coverage.md': '3807ef4d5d03137aa0cacba9c3ccfc880b80ab2f6824e2bddaf126367719e24f',
 'collections/library/skills/aims-vs-objectives/SKILL.md': '14b511fa405a63838b758782f98986e007e46142e14fd8dc08d5030481ed6267',
 'collections/library/skills/change-management/references/change-playbook.md': 'e7f6168ddb7ccad13c603f0365a6cc1494bfc3aa6d20aceeb2c93aaa9289c430',
 'collections/library/skills/cloud-security/SKILL.md': 'd6b7d222122a3001a81390273436d301efc365aac77e0318caadd10de4def1bd',
 'collections/library/skills/cloud-security/references/cspm-checks.md': '8f20efed46ce966fd97e17fc0fe046c731a9e5a4122510b151eda335364401e6',
 'collections/library/skills/content-strategy/references/content-strategy-reference.md': '0372d3bfdfbd8b65a2b4e20835b90342b6adf901dc78c7e111c6a6c1c8808243',
 'collections/library/skills/grants/SKILL.md': '8b8cea031d7e7cd8f0138d5abf6597314949cfaa1e5faf4622bdd1de218d4f97',
 'collections/library/skills/grants/references/docx_9_sections.md': '16e6dc23a3c3dae272605fed513aa8faedce7827f72c16091ded3fa7e171a6b8',
 'collections/library/skills/grants/references/nih_mechanism_matching.md': '422092a6fdfcda3585f039f0acf60b7d5f1890498847656deecea07e70e8c147',
 'collections/library/skills/incident-response/SKILL.md': '23358d4af18d9784f4a34db72cc7b6b32b69f41c95371954028f7e8718c2c10d',
 'collections/library/skills/marketing-strategy-pmm/references/launch-checklists.md': '56eb263385be1769378a08150e9be1a003b2a825f3d19edfb84d963aa7bb2bfb',
 'collections/library/skills/mobile-release/references/play_release_rules.md': '3891ec1b8aed2510cb33b9f042f500be716573e7c27e0a1e252484855a6174c3',
 'collections/library/skills/programmatic-seo/SKILL.md': '7283e13673a7c6fc4fcfe228b9529365adab0b27a93b43e56c7e0454f701fa63',
 'collections/library/skills/purple-team/SKILL.md': '6eb884e9ffb123ac2dce3e4c669a8b62f8a1db5f62f39a5c88567a80b0d37613',
 'collections/library/skills/red-team/SKILL.md': 'ae00dcd41517ee7de3777d9b003eac34c365747efbafbc448917f529402b9988',
 'collections/library/skills/red-team/references/attack-path-methodology.md': '2678ec1aab4640c6d4fc4dc2bb52fdcea5333093d0937ec4a96ee18aa5cc541f',
 'collections/library/skills/resubmission-strategy/SKILL.md': 'bdb8302e14ebabea4f272a7f9d1df2a9cccf1b95395fd66f41c716cda46665a6',
 'collections/library/skills/senior-computer-vision/SKILL.md': '7c2b2b9bafd69d5ffa730ffe5698bfd43f9e8ef1deb0dff75ecb396e1800cc76',
 'collections/library/skills/senior-computer-vision/references/computer_vision_architectures.md': 'd566c52284645c18d0491aec6b292f25973772611b6145cc265f7f9bc5944095',
 'collections/library/skills/specific-aims-page/SKILL.md': '625684ce0d93541eaeef1a89aad9d0a86c15befbbb23f8562006b5f7f66f1f01',
 'collections/library/skills/spectroscopy-basics/SKILL.md': '744b0e46e1ccb5f53df2b2b98c27a9d1e5715768572ccf9d13bd27add0e14f5b',
 'collections/library/skills/threat-detection/SKILL.md': '9eb25d17c1b7070a06dd5fb041b4f2f9b8e098c8f97f2fdfe97a5ef75d9142f5',
 'collections/library/skills/threat-detection/references/hunt-playbooks.md': '8286c3abb4a0a60488ceeb58a230fbfad84a48f9e9eb06ff6391ca13a0048773'}


class _VisibleHTML(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.skip+=1
  if tag=='meta':
   values=dict(attrs)
   if values.get('name')=='description':self.parts.append(values.get('content',''))
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,value):
  if not self.skip:self.parts.append(value)

def _prose(text:str)->str:
 text=re.sub(r'\A---\r?\n.*?\r?\n---(?:\r?\n|$)','',text,flags=re.S)
 text=re.sub(r'```.*?```|~~~.*?~~~','',text,flags=re.S)
 text=re.sub(r'`[^`]*`','',text)
 return re.sub(r'\]\([^)]+\)',']()',text)

def product_findings(root:Path)->list[dict[str,str]]:
 """Check all product pages recursively; never follow symlinks."""
 root=Path(root)
 if root.is_symlink() or not root.is_dir():
  return [{'path':'.','reason':'UNSAFE_PRODUCT_ROOT'}]
 root=root.resolve();found=[]
 def add(path,reason):found.append({'path':path,'reason':reason})
 for current,dirs,files in os.walk(root,followlinks=False):
  base=Path(current)
  for name in list(dirs):
   p=base/name;rel=p.relative_to(root).as_posix()
   if name in IGNORED:dirs.remove(name);continue
   if p.is_symlink() or (hasattr(p,'is_junction') and p.is_junction()):
    add(rel,'SYMLINK_REFUSED');dirs.remove(name)
   elif name.lower() in PRIVATE_DIRS:
    add(rel,'INTERNAL_ARTIFACT');dirs.remove(name)
  for name in files:
   p=base/name;rel=p.relative_to(root).as_posix()
   if p.is_symlink():add(rel,'SYMLINK_REFUSED');continue
   doc=rel.startswith(('docs/','presets/','services/','skills/','templates/',
                       'collections/')) or '/' not in rel
   ui=rel.startswith(('hub/site/','examples/companion_home/','src/muse_presets/')) and p.suffix.lower()=='.html'
   if rel.startswith('docs/') and (MILESTONE.match(name) or name.upper() in OLD_DOCS or re.search(r'(?:FINAL|CURRENT|RESTART)[_-]CHECKPOINT',name,re.I)):
    add(rel,'INTERNAL_ARTIFACT')
   if rel.startswith('docs/history/'):
    add(rel,'INTERNAL_ARTIFACT');continue
   if not ((doc and p.suffix.lower()=='.md') or ui):continue
   try:
    if p.stat().st_size>MAX_TEXT:raise ValueError('too large')
    body=p.read_text(encoding='utf-8')
   except (OSError,UnicodeError,ValueError):add(rel,'UNREADABLE_PRODUCT_PAGE');continue
   if '\ufffd' in body or '\u00e2\u20ac' in body:add(rel,'CORRUPTED_PRODUCT_TEXT')
   if ui:
    parser=_VisibleHTML();parser.feed(body);prose=' '.join(parser.parts)
   else:prose=_prose(body)
   if WORK_ID.search(prose) and REVIEWED_DOMAIN_TEXT.get(rel)!=hashlib.sha256(body.encode('utf-8')).hexdigest():add(rel,'INTERNAL_WORK_LANGUAGE')
   if RELEASE_JARGON.search(prose):add(rel,'INTERNAL_RELEASE_LANGUAGE')
   if ui:continue
   for match in LINK.finditer(body):
    target=match.group(1).strip().split('#',1)[0].split('?',1)[0]
    if not target or re.match(r'^[a-z][a-z0-9+.-]*:',target,re.I) or target.startswith('//'):continue
    try:
     path=(p.parent/unquote(target)).resolve()
     if not path.is_relative_to(root) or not path.exists():add(rel,'BROKEN_LOCAL_LINK')
    except (OSError,ValueError,RuntimeError):add(rel,'BROKEN_LOCAL_LINK')
 return sorted(found,key=lambda x:(x['path'],x['reason']))

def capability_findings(root:Path,catalog:object)->list[dict[str,str]]:
 """Validate advertised local functionality against actual shipped files."""
 root=Path(root);out=[]
 def add(p,r):out.append({'path':p,'reason':r})
 if type(catalog) is not dict or catalog.get('schema')!='specialist-capabilities/v1':
  return [{'path':'presets/capabilities.json','reason':'INVALID_CAPABILITY_CATALOG'}]
 if catalog.get('external_effects_enabled') is not False:add('catalog','NATIVE_AUTHORITY_NOT_ALLOWED')
 roles=catalog.get('roles');features=catalog.get('features')
 if type(roles) is not list or len(roles)!=15 or not all(type(x) is str for x in roles) or len(set(roles))!=15:
  add('roles','INVALID_ROLES')
 if type(features) is not list:return out+[{'path':'features','reason':'INVALID_FEATURES'}]
 ids=set()
 for feature in features:
  if type(feature) is not dict:add('features','INVALID_FEATURE');continue
  identifier=feature.get('id');module=feature.get('module');example=feature.get('example');role=feature.get('role')
  if type(identifier) is not str or identifier in ids:add('features','DUPLICATE_OR_INVALID_ID')
  else:ids.add(identifier)
  if type(module) is not str or MODULE.fullmatch(module) is None or not (root/'src'/Path(*module.split('.')).with_suffix('.py')).is_file():add(str(identifier),'MISSING_MODULE')
  if type(example) is not str or not example.startswith('examples/') or '..' in Path(example).parts or not (root/example).is_file():add(str(identifier),'MISSING_EXAMPLE')
  if not isinstance(roles,list) or role not in roles:add(str(identifier),'INVALID_ROLE')
  if feature.get('grade') not in ('local-executable','local-review-only','synthetic-training'):add(str(identifier),'INVALID_CAPABILITY_GRADE')
 return sorted(out,key=lambda x:(x['path'],x['reason']))

def refresh_manifest(root:Path)->dict:
 """Validate the public inventory and atomically refresh its exact hashes."""
 from .public_export import SCHEMA,select_public_files
 from .neutrality import audit_public_tree
 root=Path(root)
 bad=product_findings(root)
 if bad:raise ValueError('PUBLIC_PRODUCT_POLICY_FAILED:'+json.dumps(bad[:12],sort_keys=True))
 cap=root/'presets/capabilities.json'
 if cap.exists():
  bad=capability_findings(root,json.loads(cap.read_text(encoding='utf-8')))
  if bad:raise ValueError('PUBLIC_CAPABILITY_POLICY_FAILED:'+json.dumps(bad))
 files=select_public_files(root,verify_manifest=False)
 bad=audit_public_tree(root)
 if bad:raise ValueError('PUBLIC_PRIVACY_POLICY_FAILED:'+json.dumps(bad[:8],sort_keys=True))
 manifest={'schema':SCHEMA,'release_kind':'SOURCE_PACKAGE',
  'source_file_count':len(files),'files':{n:hashlib.sha256(b).hexdigest() for n,b in files.items()}}
 for name,data in files.items():
  if (root/name).read_bytes()!=data:raise ValueError('SOURCE_CHANGED_DURING_MANIFEST_REFRESH')
 raw=(json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+'\n').encode('utf-8')
 destination=root/'PUBLIC_SOURCE_MANIFEST.json'
 if destination.exists() and destination.read_bytes()==raw:return manifest
 fd,temp=tempfile.mkstemp(prefix='.manifest-',suffix='.tmp',dir=root)
 try:
  with os.fdopen(fd,'wb') as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
  os.replace(temp,destination)
 finally:
  if os.path.exists(temp):os.unlink(temp)
 return manifest

def check_distribution(root:Path)->dict:
 from .public_export import select_public_files
 from .neutrality import audit_public_tree
 root=Path(root);findings=product_findings(root)
 try:
  catalog=json.loads((root/'presets/capabilities.json').read_text(encoding='utf-8'))
  findings+=capability_findings(root,catalog)
 except (OSError,ValueError):findings.append({'path':'presets/capabilities.json','reason':'MISSING_OR_INVALID_CAPABILITY_CATALOG'})
 try:
  files=select_public_files(root)
 except ValueError as exc:
  files={};findings.append({'path':'PUBLIC_SOURCE_MANIFEST.json','reason':str(exc)})
 findings+=audit_public_tree(root)
 return {'status':'FAIL' if findings else 'PASS','files':len(files),'findings':findings}
