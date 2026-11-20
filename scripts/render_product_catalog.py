"""Keep product counts, specialist guides and discovery metadata together."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'tools'),str(ROOT/'scripts')]
import muse_collection
import tool_guides
from collection_compatibility import current_inventory
from build_release import ALIASES, ROLE_WORKFLOWS, specialist_asset, planner_asset
from muse_presets.planner_package import ROLES as PLANNER_ROLES
from render_downloads import subject
from render_specialist_directory import AREAS, COPY

REPO='https://github.com/Atlas-Agents-Hub/muse-hub'
SITE='https://atlas-agents-hub.github.io/muse-hub/'
# These pages describe the current collection. Historical release notes and the
# original compatibility fixtures retain their original counts and versions.
CURRENT_PAGES=(
    'README.md','START_HERE.md','llms.txt','hub/README.md','hub/site/README.md',
    'docs/README.md','docs/GETTING_STARTED.md','docs/CAPABILITIES.md','docs/SKILLS.md',
    'docs/ARCHITECTURE.md','docs/CONNECTORS.md','docs/handbook/README.md',
    'docs/collection/MUSE_CURATED_COLLECTION.md','docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md',
    'docs/discovery/AI_AGENT_GUIDE.md','docs/journeys/BUILD_AND_AUTOMATE.md',
    'collections/muse-starters-v1/README.md',
)

from muse_presets.product_copy import FIRST_TASKS

def encode(value):
    return (json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode('utf-8')

def suggested_starters(data, role_id, selected_workflows):
    """Keep explicit role assignments first, then add supported workflow tasks."""
    direct=[row for row in data['starters']
            if role_id in (row['base_role'],row.get('specialist_role'))]
    if role_id not in muse_collection.EXTENSION_ROLES:
        return direct
    seen={row['id'] for row in direct}
    selected=set(selected_workflows)
    return direct+[row for row in data['starters']
                   if row['id'] not in seen and selected.intersection(row['workflows'])]

def planner_guide(version):
    return f'''# Muse Planner: projects, routines and your next action

Turn a loose idea into a project you can move forward. Muse Planner brings your inbox, projects, daily routines, weekly review, reference notes and calendar into one Muse Space with persistent SQLite storage.

**[Download Muse Planner]({REPO}/releases/download/{version}/{planner_asset(version)})** · [{version} release]({REPO}/releases/tag/{version}) · [Complete setup guide](../../examples/gtd_space/README.md)

The same complete app is included in the [Coordinator](../../presets/coordinator/INSTALL.md) and [Personal Companion](../../presets/personal-companion/INSTALL.md) downloads. In any of those ZIPs, open `spaces/planner/README.md`.

## Make a useful workspace

| View | What you can do |
| --- | --- |
| Today | Choose your next actions, priorities and scheduled work. |
| Inbox | Capture ideas, then clarify and route them into the right project. |
| Projects | Define an outcome and keep its next actions together. |
| Future | Build daily and weekly routines, reminders and scheduled items. |
| Week | View connected calendars and reserve focus blocks. |
| Someday and Reference | Keep future ideas, notes and useful links easy to find. |
| Done | Review completed work and reopen an item when you need it. |

## Create your Space

1. Extract the download into a new folder and give Muse the complete `spaces/planner/` app folder.
2. Ask Muse to create a **TypeScript Space** named **Muse Planner**. Follow the app's README to prepare the Muse host's SDK and install the locked dependencies with Bun.
3. Apply the included SQL migrations in journal order and build through Muse's Space builder.
4. Capture an inbox item, create a project with a next action, and add a daily routine. Reopen the Space to continue from the saved workspace.
5. Choose **Export** to keep a portable JSON backup.

The [app guide](../../examples/gtd_space/README.md) includes the exact commands, local preview, calendar settings, backup and restore. Start with your projects and routines; add the calendars you want when you are ready.

## Plan with your specialist

Ask **Coordinator** to turn a project outcome into next actions, dependencies and a weekly plan. Ask **Personal Companion** to shape routines and reminders around your priorities. Copy an item's reference into the conversation so your assistant can discuss the same work.

> Set up my current projects in Muse Planner. Help me capture loose tasks, define each project's outcome, choose a small next action and create a weekly review routine.

Use **Export** before an update or move. **Import** validates a backup and asks you to confirm replacing the current workspace, then restores it as one transaction.

[All workspaces](../README.md#open-a-workspace) · [Setup and saved data](../INSTALL_AND_PERSISTENCE.md) · [Specialist library](../collection/SPECIALIST_LIBRARY.md)
'''

def outputs(root=ROOT):
    root=Path(root)
    data=muse_collection.load_collection(root/'collections/muse-starters-v1')
    preset_catalog=json.loads((root/'presets/catalog.json').read_bytes())
    version=preset_catalog['release']
    connectors=json.loads((root/'docs/connectors/catalog.json').read_bytes())['connectors']
    guides=tool_guides.load_guides(root)
    counts={'skills':len(data['skills']),'workflows':len(data['workflows']),
            'task starters':len(data['starters']),'connectors':len(connectors),
            'tool guides':len(guides['guides'])}
    result={}
    def add(name,body):result[name]=body.encode('utf-8') if isinstance(body,str) else body
    preset_catalog['downloads']={
        role:REPO+'/releases/download/'+version+'/'+specialist_asset(role,version)
        for role in preset_catalog['presets']
    }
    add('presets/catalog.json',encode(preset_catalog))
    add('docs/spaces/MUSE_PLANNER.md',planner_guide(version))
    feature_status=json.loads((root/'docs/discovery/hub-feature-status.json').read_bytes())
    feature_status.update(release=version,release_url=REPO+'/releases/tag/'+version,
                          release_manifest_url=REPO+'/releases/download/'+version+'/RELEASE_MANIFEST.json')
    add('docs/discovery/hub-feature-status.json',encode(feature_status))
    def current(text):
        text=re.sub(r'v1\.5\.0\b',version,text)
        for term,number in counts.items():
            text=re.sub(r'\b[0-9]+(?= (?:\*\*)?'+re.escape(term)+r'\b)',str(number),text)
        text=re.sub(r'\b[0-9]+(?= (?:reusable |developed )skills\b)',str(counts['skills']),text)
        text=re.sub(r'\b[0-9]+(?= connector guides\b)',str(counts['connectors']),text)
        text=re.sub(r'one of [0-9]+ focused configurations',f"one of {counts['task starters']} focused configurations",text)
        text=re.sub(r'for [0-9]+ services',f"for {counts['connectors']} services",text)
        return text
    for name in CURRENT_PAGES:
        path=root/name
        if path.exists():add(name,current(path.read_text(encoding='utf-8')))
    add('collections/muse-starters-v1/COUNTS.json',encode(current_inventory(data)))
    starters=f"# Choose a task starter\n\n**{counts['task starters']} task starters** help you turn a goal into a useful result. Choose a prompt, bring the requested inputs, and follow its skills and workflows with your Muse assistant. [Choose a specialist](../../docs/DOWNLOAD_A_SPECIALIST.md).\n\n"
    for family in data['specialists']:
        rows=[row for row in data['starters'] if row['base_role']==family['id']]
        if not rows:continue
        starters+='## '+family['title']+'\n\n| Starter | What you will make |\n| --- | --- |\n'
        for row in sorted(rows,key=lambda row:row['title'].casefold()):
            starters+=f"| [{row['title'].replace('|','/')}](starters/{row['id']}/STARTER.md) | {row['purpose'].replace('|','/')} |\n"
        starters+='\n'
    add('collections/muse-starters-v1/CATALOG.md',starters)
    roles={row['id']:row for row in data['specialists']}
    skills={row['id']:row for row in data['skills']}
    flows={row['id']:row for row in data['workflows']}
    summaries={}
    for canonical in ROLE_WORKFLOWS:
        rid=ALIASES.get(canonical,canonical)
        role=roles[rid]
        title,scope,*_=COPY[canonical]
        selected_flows=list(dict.fromkeys(ROLE_WORKFLOWS[canonical]+role.get('library_workflows',[])))
        selected=set(role['skills'])|set(role.get('library_skills',[]))
        for key in selected_flows:selected.update(flows[key]['skills'])
        selected_guides=set(tool_guides.selected_ids(guides,role=rid))
        selected_guides.update(gid for key in selected_flows for gid in flows[key].get('tool_guides',[]))
        selected_connectors=[row for row in connectors if canonical in row['specialists']]
        starters=suggested_starters(data,rid,selected_flows)
        summary=f"**{len(selected)} skills · {len(selected_flows)} workflows · {len(selected_guides)} tool guides**"
        summaries[canonical]={'skills':len(selected),'workflows':len(selected_flows),
                             'tool_guides':len(selected_guides),'connectors':len(selected_connectors),
                             'task_starters':len(starters)}
        url=REPO+'/releases/download/'+version+'/'+specialist_asset(canonical,version)
        browse=SITE+'downloads.html?role='+rid
        first=FIRST_TASKS[canonical]
        inbox_note=('\n\n## Review email with saved preferences\n\nUse the [inbox workspace](../../collections/muse-starters-v1/skills/inbox-triage/INBOX_WORKSPACE.md) to prepare reply preferences, resume from the last completed review and check the action log. The download includes three Python helpers, an example workspace and Inbox Setup for personalizing it.'
                    if 'inbox-triage' in selected else '')
        planner_note=('\n\n## Plan in a Muse Space\n\nYour download includes [Muse Planner](../../docs/spaces/MUSE_PLANNER.md), a complete Space for projects, next actions, daily routines, weekly reviews, notes and calendars. Open `spaces/planner/README.md` in the ZIP to create your Space and save your first project.'
                      if canonical in PLANNER_ROLES else '')
        readme=f'''# {title}

**Muse Hub specialist:** {scope}

**[Download the assistant]({url})** · **[Set up {title}](INSTALL.md)** · [Browse its library](LIBRARY.md)

{summary}. Give this specialist its own Main conversation and **three subchats**. Its package includes the selected methods, supporting files, examples and service guides for your work.

## Put it to work

Bring your current task and source material. Open `PROFILE.md` in the download and choose the relevant skill or workflow. Follow its inputs, steps and result checks, then save the result with your project.

**First task:** {first}

## Explore the toolkit

- [Skills and workflows for {title}]({browse}) — search the full selection by task or subject.
- [Library and suggested task starters](LIBRARY.md) — find the right method and next step.
- [Working methods](../../docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md) and [included tools](../../docs/CAPABILITIES.md).
- [Service connectors](../../docs/connectors/README.md) — {len(selected_connectors)} recommended services for this specialist.

Keep your customized instructions, preferences and memory in your working copy. [Setup and saved data](../../docs/INSTALL_AND_PERSISTENCE.md) explains updates.{inbox_note}{planner_note}

[All specialists](../../docs/DOWNLOAD_A_SPECIALIST.md) · [{version} downloads](../../docs/RELEASES.md) · [Muse Hub]({SITE})
'''
        install=f'''# {title} | Muse Hub

{scope}

**[Download {title}]({url})** · [{version} release]({REPO}/releases/tag/{version}) · [Checksums]({REPO}/releases/download/{version}/SHA256SUMS)

{summary}. [Explore the full selection](LIBRARY.md).

## Set up this assistant

1. Extract the ZIP into its own folder and open `START_HERE.md`. You can also give Muse the ZIP with your current task.
2. Choose a **separate Muse assistant** for {title} and add the supplied Main instructions.
3. Set up its **three subchats** using their included instructions, context, tools and memory documents.
4. Personalize the assistant's working preferences. Open `PROFILE.md` to choose the methods for your task.
5. Try the first task below, check the result against the method's expected outputs, and save your work.

**First task to try:** {first}

No Python is needed for the assistant instructions. Optional local tools include their commands and requirements in `START_HERE.md`. Use `CONNECTORS.md` for the included service guides and select the account and permissions for each connection you add.

## Use a skill or workflow

Start with [this specialist's library](LIBRARY.md). A skill describes a focused method and includes its reference files. A workflow connects several methods with named inputs, expected results and checks. Load the method that fits the current task; the complete selection remains available in the download.

[Find and build your own pack](../../docs/collection/FIND_AND_BUILD.md) to search this specialist's methods, preview the included files and create a ZIP for your task. Add `--role {canonical}` to the toolkit's search command to focus on this specialist.

Explore the [working methods and included engines](../../docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md). For terminal tools, follow the [terminal guide](../../docs/TERMINAL.md). Keep the original download and your personalized working copy separately when updating.{inbox_note}{planner_note}

Role ID: `{canonical}`. Package: `{specialist_asset(canonical,version)}`.

[All specialists](../../docs/DOWNLOAD_A_SPECIALIST.md) · [Setup and saved data](../../docs/INSTALL_AND_PERSISTENCE.md) · [Get started](../../docs/GETTING_STARTED.md)
'''
        groups=Counter(subject(skills[key]['category']) for key in selected)
        library=f'# {title}: skills, workflows and connections\n\n{scope}\n\n{summary} · **{len(starters)} task starters** · **{len(selected_connectors)} recommended connectors**\n\n[Download the specialist]({url}) · [Search its methods]({browse}) · [Setup](INSTALL.md)\n\n## Browse by subject\n\n| Subject | Skills | Browse |\n| --- | ---: | --- |\n'
        for label,number in sorted(groups.items()):
            library+=f'| {label} | {number} | [Explore]({browse}&subject={quote(label)}) |\n'
        library+='\n## Start a useful task\n\n'
        for row in starters[:12]:
            library+=f"- [{row['title']}](../../collections/muse-starters-v1/starters/{row['id']}/STARTER.md) — {row['purpose']}\n"
        library+=f'\n[All task starters](../../collections/muse-starters-v1/CATALOG.md) · [All {len(selected_flows)} workflows for this specialist]({browse}&type=workflow)\n\n## Connect your services\n\n'
        for row in selected_connectors[:18]:
            target='../../docs/connectors/'+row['guide_path'] if row.get('guide_path') else row['source_url']
            library+=f"- [{row['name']}]({target}) — {row['description'].splitlines()[0][:180]}\n"
        library+='\n[Complete connector directory](../../docs/connectors/README.md) · [Tools and examples](../../docs/CAPABILITIES.md)\n'
        if inbox_note:
            library=library.rstrip()+inbox_note+'\n'
        if planner_note:
            library=library.rstrip()+planner_note+'\n'
        add(f'presets/{canonical}/README.md',readme)
        add(f'presets/{canonical}/INSTALL.md',install)
        add(f'presets/{canonical}/LIBRARY.md',library)
        preset=json.loads((root/'presets'/canonical/'preset.json').read_bytes())
        preset['description']=scope
        add(f'presets/{canonical}/preset.json',encode(preset))
    boundaries=json.loads((root/'kits/family-handoff/role-boundaries.json').read_bytes())
    for canonical in ROLE_WORKFLOWS:
        profile_path=f'presets/{canonical}/preset.json'
        boundaries['roles'][canonical]['profile_sha256']=hashlib.sha256(result[profile_path]).hexdigest()
    add('kits/family-handoff/role-boundaries.json',encode(boundaries))
    chooser=f'# Choose your Muse assistant\n\nDownload one specialist for the work you want to do. Each package includes Main instructions, three subchat guides, selected skills, workflows, examples and service guides for **one Muse assistant**.\n\n**Current release: [{version}]({REPO}/releases/tag/{version})** · [Checksums]({REPO}/releases/download/{version}/SHA256SUMS) · [Latest release]({REPO}/releases/latest)\n\n'
    for area,identities in AREAS:
        chooser+='## '+area+'\n\n| Specialist | What you can work on | Skills | Download |\n| --- | --- | ---: | --- |\n'
        for rid in identities:
            title,scope,*_=COPY[rid]
            chooser+=f"| [{title}](../presets/{rid}/INSTALL.md) | {scope} | {summaries[rid]['skills']} | [Download ZIP]({REPO}/releases/download/{version}/{specialist_asset(rid,version)}) |\n"
        chooser+='\n'
    chooser+='## Open your package\n\n1. Download the ZIP and extract it into a new folder.\n2. Open `START_HERE.md`, or give Muse the ZIP and your current task.\n3. Follow the included guide for Main and the three subchats, then try the specialist\'s first task.\n\nNo Python is needed for assistant instructions. Optional local tools include their requirements and commands.\n\n[Get started](GETTING_STARTED.md) · [Setup and updates](INSTALL_AND_PERSISTENCE.md) · [Browse tasks](handbook/specialists-by-task.md) · [Release notes](RELEASES.md)\n'
    add('docs/DOWNLOAD_A_SPECIALIST.md',chooser)
    doc=json.loads((root/'docs/discovery/agent-capabilities.json').read_bytes())
    doc=json.loads(current(json.dumps(doc)))
    doc['release']=version
    doc['curated_task_collection'].update(skills=counts['skills'],workflow_recipes=counts['workflows'],starter_configurations=counts['task starters'])
    doc['configuration_count']=counts['task starters']+15
    doc['configuration_breakdown']['task_starters']=counts['task starters']
    doc['skill_collection'].update(developed_task_skills=counts['skills'],workflows=counts['workflows'])
    doc['custom_connector_count']=counts['connectors']
    workbenches=doc.setdefault('local_workbenches',[])
    board={
        'name':'Muse Task Board','specialist':'personal-companion',
        'demo':'examples/task_board/run.py','guide':'docs/spaces/TASK_BOARD.md',
        'storage':'SQLite',
        'features':['task_cards','drag_and_keyboard_moves','saved_revisions',
                    'json_export_and_import','assistant_request_and_result'],
    }
    workbenches[:]=[row for row in workbenches if row.get('name')!=board['name']]+[board]
    spaces=doc.setdefault('spaces',[])
    planner={'id':'planner','name':'Muse Planner','specialists':list(PLANNER_ROLES),
        'source':'examples/gtd_space','guide':'docs/spaces/MUSE_PLANNER.md',
        'download_url':REPO+'/releases/download/'+version+'/'+planner_asset(version),
        'storage':'SQLite','features':['inbox','projects','next_actions','daily_and_weekly_routines',
            'reference_notes','calendar_focus_blocks','portable_backup_and_restore']}
    spaces[:]=[row for row in spaces if row.get('id')!='planner']+[planner]
    doc['specialist_libraries']=summaries
    doc['skill_downloads']={'format':'subject-packs','skills_per_pack_maximum':40,
                            'entrypoint':'skills/<skill-id>/SKILL.md','directory':SITE+'downloads.html#skills'}
    add('docs/discovery/agent-capabilities.json',encode(doc))
    role_directory=json.loads(current((root/'hub/site/roles.json').read_text(encoding='utf-8')))
    for row in role_directory['roles']:
        row['description']=COPY[row['id']][1]
        row['library']=summaries[row['id']]
    add('hub/site/roles.json',encode(role_directory))
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name,raw in outputs().items():
        path=ROOT/name
        if args.check:
            if not path.is_file() or path.read_bytes()!=raw:stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(raw)
    if stale:
        print(json.dumps({'status':'FAIL','stale':stale}));return 2
    print('Product catalog is current.' if args.check else 'Product catalog updated.')
    return 0

if __name__=='__main__':raise SystemExit(main())
