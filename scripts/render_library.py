"""Render the Muse skill and workflow indexes from their current catalogs."""
from __future__ import annotations
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import muse_collection as collection
import tool_guides
sys.path.insert(0,str(ROOT/'scripts'))
from render_downloads import subject, subject_slug


def outputs(root=ROOT):
    root=Path(root)
    base=root/'collections/muse-starters-v1'
    data=collection.load_collection(base)
    sources={row['id']:row for row in data['sources']}
    skills={row['id']:row for row in data['skills']}
    version=json.loads((root/'presets/catalog.json').read_bytes())['release']
    release='https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/'+version+'/'
    import build_release
    skill_routes=build_release.skill_download_layout(data,version)
    result={}
    def add(path,body):result[path]=(body if body.endswith('\n') else body+'\n').encode('utf-8')
    grouped=defaultdict(list)
    for row in data['skills']:
        grouped[subject(row['category'])].append(row)
        if row.get('format')!='portable-skill':
            add('collections/muse-starters-v1/skills/'+row['id']+'/SKILL.md',collection.render_skill(row,sources))
            if row.get('depth'):
                add('collections/muse-starters-v1/skills/'+row['id']+'/DEPTH.md',collection.render_depth(row))
    for row in data['starters']:
        add('collections/muse-starters-v1/starters/'+row['id']+'/STARTER.md',collection.render_profile(row))
    for row in data['workflows']:
        folder='collections/library/workflows/' if row.get('steps') else 'collections/muse-starters-v1/workflows/'
        # Repository references point to each skill's canonical folder; the ZIP renderer
        # retains ../skills paths because those packages contain a complete closure.
        body=collection.render_workflow(row,skills)
        if row.get('steps'):
            for sid in row['skills']:
                target='../skills/'+sid+'/SKILL.md' if skills[sid].get('format')=='portable-skill' else '../../muse-starters-v1/skills/'+sid+'/SKILL.md'
                body=body.replace('](../skills/'+sid+'/SKILL.md)',']('+target+')')
            body=body.replace('](../TOOL_GUIDES.md)','](../../../docs/tools/README.md)')
            if row.get('resources'):
                body=body.replace(']('+row['id']+'/','](../workflow-assets/'+row['id']+'/')
                body=body.replace('`'+row['id']+'/', '`../workflow-assets/'+row['id']+'/')
                body=body.replace('tools/workflow_graph.py workflows/'+row['id']+'/',
                                  '../../../tools/workflow_library.py ../workflow-assets/'+row['id']+'/')
        add(folder+row['id']+'.md',body)
    index=f"# Muse skills\n\nChoose from **{len(skills)} skills**. Each download includes its method and supporting files. [Search by subject or specialist](https://atlas-agents-hub.github.io/muse-hub/downloads.html#skills).\n\n"
    large=len(skills)>600
    if large:
        index+='## Browse the library\n\nDownload a subject pack, open `SKILLS.md`, and choose the method for your task. Each search result names the exact `skills/<skill-id>/SKILL.md` entry inside its pack.\n\n| Subject | Skills | Read the guides |\n| --- | ---: | --- |\n'
    for category,rows in sorted(grouped.items(),key=lambda pair:pair[0].casefold()):
        rows=sorted(rows,key=lambda row:row['title'].casefold())
        if large:
            slug=subject_slug(category)
            index+=f'| {category} | {len(rows)} | [Browse](../library/subjects/{slug}-001.md) |\n'
            chunks=[rows[i:i+150] for i in range(0,len(rows),150)]
        else:
            index+='## '+category+'\n\n| Skill | Use it when | Download |\n| --- | --- | --- |\n'
            chunks=[rows]
        for number,chunk in enumerate(chunks,1):
            page=f'# {category}: Muse skills\n\n{len(rows)} skills · Page {number} of {len(chunks)}\n\n[All subjects](../../muse-starters-v1/SKILL_INDEX.md) · [Search and download](https://atlas-agents-hub.github.io/muse-hub/downloads.html#skills)\n\n'
            if large:
                page+=' · '.join(f'[Page {i}]({slug}-{i:03d}.md)' for i in range(1,len(chunks)+1))+'\n\n'
            page+='| Skill | Use it when | Download |\n| --- | --- | --- |\n'
            for row in chunk:
                if large:
                    path=('../'+row['path'] if row.get('format')=='portable-skill' else '../../muse-starters-v1/skills/'+row['id'])+'/SKILL.md'
                else:
                    path=('../library/'+row['path'] if row.get('format')=='portable-skill' else 'skills/'+row['id'])+'/SKILL.md'
                route=skill_routes[row['id']]
                label='Skill pack' if route['pack_kind']=='skill-pack' else 'ZIP'
                trigger=' '.join(row['trigger'].replace('|','/').split())
                if len(trigger)>300:trigger=trigger[:297].rsplit(' ',1)[0]+'…'
                line=f"| [{row['title'].replace('|','/')}]({path}) | {trigger} | [{label}]({release+route['asset']}) |\n"
                if large:page+=line
                else:index+=line
            if large:add(f'collections/library/subjects/{slug}-{number:03d}.md',page)
        if not large:index+='\n'
    add('collections/muse-starters-v1/SKILL_INDEX.md',index)
    workflow_index=f"# Muse workflows\n\n**{len(data['workflows'])} workflows** connect skills into useful results. Each ZIP includes every skill needed by its steps.\n\n"
    workflow_index+='| Workflow | Result | Download |\n| --- | --- | --- |\n'
    for row in sorted(data['workflows'],key=lambda row:row['title'].casefold()):
        path=('workflows/' if row.get('steps') else '../muse-starters-v1/workflows/')+row['id']+'.md'
        workflow_index+=f"| [{row['title']}]({path}) | {row['goal'].replace('|','/')} | [ZIP]({release+'muse-workflow-'+row['id']+'-'+version+'.zip'}) |\n"
    add('collections/library/WORKFLOWS.md',workflow_index)
    guides=tool_guides.load_guides(root)
    roles='# Skills and tools by specialist\n\nEach specialist download includes the skills, workflows and tool guides relevant to its work. Open `PROFILE.md` after extracting the ZIP and select the methods you need for the current task.\n\n'
    roles+='| Specialist | Skills | Workflows | Tool guides | Browse |\n| --- | ---: | ---: | ---: | --- |\n'
    # Keep release composition as the single source of workflow membership.
    sys.path.insert(0,str(ROOT/'scripts'))
    import build_release
    reverse={v:k for k,v in build_release.ALIASES.items()}
    for row in data['specialists']:
        rid=row['id'];canonical=reverse.get(rid,rid)
        workflows=list(dict.fromkeys(build_release.ROLE_WORKFLOWS[canonical]+row.get('library_workflows',[])))
        chosen=set(row['skills'])|set(row.get('library_skills',[]))
        by_workflow={w['id']:w for w in data['workflows']}
        for key in workflows:chosen.update(by_workflow[key]['skills'])
        count=len(set(tool_guides.selected_ids(guides,role=rid))|
                  {gid for key in workflows for gid in by_workflow[key].get('tool_guides',[])})
        roles+=f"| [{row['title']}](../../presets/{canonical}/README.md) | {len(chosen)} | {len(workflows)} | {count} | [Browse](https://atlas-agents-hub.github.io/muse-hub/downloads.html?role={rid}) |\n"
    roles+='\n[Tool guides](../tools/README.md) · [Combined tool workflows](../tools/workflows.md) · [All skills](../../collections/muse-starters-v1/SKILL_INDEX.md) · [All workflows](../../collections/library/WORKFLOWS.md)\n'
    add('docs/collection/SPECIALIST_LIBRARY.md',roles)
    add('collections/library/README.md',f"# Muse skill library\n\nExplore **{len(skills)} skills**, **{len(data['workflows'])} workflows** and **{len(guides['guides'])} tool guides** for engineering, research, data, design, creative work and everyday projects.\n\n- [Browse every skill](../muse-starters-v1/SKILL_INDEX.md).\n- [Choose a workflow](WORKFLOWS.md).\n- [Find skills and tools for your specialist](../../docs/collection/SPECIALIST_LIBRARY.md).\n- [Search and download ZIPs](https://atlas-agents-hub.github.io/muse-hub/downloads.html).\n\nExtract a ZIP and open `START_HERE.md`. Give Muse the selected method and your task. Each skill includes the reference files, examples and tools used by its instructions; the method states any additional software or account setup needed for its commands.\n")
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name,raw in outputs().items():
        p=ROOT/name
        if args.check:
            if not p.is_file() or p.read_bytes()!=raw:stale.append(name)
        else:
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(raw)
    if stale:
        print(json.dumps({'status':'FAIL','stale':stale}));return 2
    print('Library indexes verified.' if args.check else 'Library indexes updated.')
    return 0


if __name__=='__main__':raise SystemExit(main())
