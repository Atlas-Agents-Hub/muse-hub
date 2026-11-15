"""Render a human-first directory from the canonical 15-role engine registry.

This is documentation, never a role installer or a grant of host authority.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/"docs/discovery/specialist-engine-index.json"
OUTPUT=ROOT/"docs/handbook/specialists-by-task.md"

AREAS=[
 ("Build and automate",("software-engineer","data-engineering-architect","automation-engineer","infrastructure-reliability-engineer")),
 ("Research and evaluate",("research-evaluator","claims-adjudicator","adversarial-verifier","reverse-engineering-researcher")),
 ("Create and learn",("creative-studio","product-interface-designer","model-builder","learning-coach")),
 ("Life and planning",("personal-companion","garden-companion","coordinator"))
]
# Each description covers the actual role, not merely its smallest local demo.
COPY={
"software-engineer":("Software Engineer",
 "Build, debug, refactor and release software. Work from reproduction and architecture decisions through implementation, regression tests, source integrity and reviewed delivery.",
 "The engineering sourcekit runs bounded repair and test workflows. Claim Gate checks admission and recovery; Iron Ledger and Provenance Vault remain evidence-only candidates under separate qualification.",
 "Engineering sourcekit","Claim Gate"),
"data-engineering-architect":("Data Engineering & Database Architect",
 "Design and maintain reliable data systems, from schemas and ingestion quality to record identity, event reconciliation, query performance and safe migrations.",
 "The data extension reviews schema contracts, versioned events and supplied query plans; the role engine checks key identity, duplicates and nulls.",
 "Data extension","Role engine"),
"automation-engineer":("Automation Engineer",
 "Build repeatable workflows across tools and services, with dependency graphs, triggers, approval points, idempotency, retry policy and uncertain-effect recovery.",
 "The automation extension validates approvals, locator evidence and effect records; the role engine checks graph validity and ordering. Live actions use host-authorized connectors.",
 "Automation extension","Dependency engine"),
"infrastructure-reliability-engineer":("Infrastructure & Reliability Engineer",
 "Improve service reliability using SLOs, error budgets, capacity forecasts, incident investigation, recovery plans and evidence from real measurements.",
 "The reliability extension calculates capacity and incident timing; the role engine computes error-budget consumption from supplied metrics.",
 "Reliability extension","Reliability engine"),
"research-evaluator":("Research Evaluator",
 "Investigate scientific and technical questions, compare explanations, audit primary evidence and design controlled, held-out evaluations.",
 "The research engine validates quotations and source separation; numerical evaluation scores supplied predictions and checks group leakage.",
 "Research engine","Numerical evaluation"),
"claims-adjudicator":("Claims Adjudicator",
 "Resolve competing factual and technical claims by tracing original evidence, testing counterexamples, qualifying uncertainty and recording defensible conclusions.",
 "The claims engine and portable sourcekit produce source-bound findings with reproducible evidence and limitations.",
 "Claims engine","Claims sourcekit"),
"adversarial-verifier":("Adversarial Verifier",
 "Challenge authorized software, agent systems and releases with threat models, failure injection, negative controls and independent remediation reviews.",
 "The public V1 includes a defensive testing playbook and editable review methods. No standalone security-testing engine is bundled with this role.",
 None,None),
"reverse-engineering-researcher":("Reverse Engineering & Security Researcher",
 "Understand software and protocol behavior with authorized observations, defensive trace analysis, scoped experiments and clean-room reconstructions.",
 "The reverse-analysis engine and sourcekit compare supplied observations. No live probing or new security-assistance executable is bundled in public V1.",
 "Reverse-analysis engine","Reverse sourcekit"),
"creative-studio":("Creative Studio",
 "Develop original visual media, animation, video and interactive scenes—from creative direction, characters, environments and asset development to motion, render inspection, continuity and delivery.",
 "The bundled creative-production engine is a production planner, not an image or video renderer. It compiles briefs, dependencies, shots, timelines, continuity checks and textual storyboards; actual media uses authorized render tools.",
 "Creative-production engine","Creative sourcekit"),
"product-interface-designer":("Product & Interface Designer",
 "Design and evaluate complete product experiences: user research, information architecture, responsive layouts, interaction flows, accessibility and build-ready handoffs.",
 "The interface extension tests color contrast and declared interaction states; the role engine reviews labels in supplied screen definitions.",
 "Interface extension","Role engine"),
"model-builder":("Model Builder",
 "Design datasets, models and adapters, conduct training experiments, compare candidates on held-out data and preserve model, tokenizer and artifact provenance.",
 "The model sourcekit performs bounded local model training, mathematical checks and evaluations; larger GPU training requires a separate host.",
 "Model-building sourcekit","Toy-model training engine"),
"learning-coach":("Learning Coach",
 "Build lessons, flashcards, practice sessions, scored quizzes and adaptive review from trusted study material, keeping learner progress and weak areas visible.",
 "The learning engine, session store and portable sourcekit provide local scoring, study history and repeatable practice.",
 "Learning engine","Session store"),
"personal-companion":("Personal Companion",
 "Support daily life with personal planning, routines, accessible interactions and privacy-aware assistance shaped to the owner's preferences.",
 "Daily Desk is a working local SQLite workbench for task and note editing, revision conflicts, persistence, export and restore. Connected calendars and reminders use host-authorized services.",
 "Daily Desk workbench","Companion storage"),
"garden-companion":("Garden Companion",
 "Organize plants, growing seasons and gardening projects through observations, evidence-aware care guidance, planting plans and owner-managed schedules.",
 "The garden engine, local calendar and sourcekit retain versioned observations and care schedules without silently changing external calendars.",
 "Garden records engine","Garden calendar"),
"coordinator":("Coordinator",
 "Turn complex goals into scoped work across specialists: sequence dependencies, manage owner approvals and resources, recover interrupted work and verify handoffs.",
 "The coordinator sourcekit, review tools and drop-in implementation provide local plan and evidence checks; there is no built-in live worker dispatch.",
 "Coordinator sourcekit","Review engine")
}


ENGINE_PATHS={
 "software-engineer":("src/muse_presets/engineer_sourcekit.py","presets/software-engineer/runtime/claim-gate/ENGINE.json"),
 "data-engineering-architect":("src/muse_presets/specialist_extensions/data.py","src/muse_presets/specialist_engines.py"),
 "automation-engineer":("src/muse_presets/specialist_extensions/automation.py","src/muse_presets/specialist_engines.py"),
 "infrastructure-reliability-engineer":("src/muse_presets/specialist_extensions/reliability.py","src/muse_presets/specialist_engines.py"),
 "research-evaluator":("src/muse_presets/research_evaluator.py","src/muse_presets/numeric_evaluation.py"),
 "claims-adjudicator":("src/muse_presets/claims.py","src/muse_presets/claims_sourcekit.py"),
 "reverse-engineering-researcher":("src/muse_presets/reverse.py","src/muse_presets/reverse_sourcekit.py"),
 "creative-studio":("src/muse_presets/creative_production.py","src/muse_presets/creative_sourcekit.py"),
 "product-interface-designer":("src/muse_presets/specialist_extensions/interface.py","src/muse_presets/specialist_engines.py"),
 "model-builder":("src/muse_presets/model_builder_sourcekit.py","src/muse_presets/model_toy_bundle.py"),
 "learning-coach":("src/muse_presets/learning.py","src/muse_presets/learning_session.py"),
 "personal-companion":("src/muse_presets/daily_desk.py","src/muse_presets/personal_companion.py"),
 "garden-companion":("src/muse_presets/garden.py","src/muse_presets/garden_calendar.py"),
 "coordinator":("src/muse_presets/coordinator_sourcekit.py","src/muse_presets/coordinator_review.py"),
}

def render()->str:
 data=json.loads(INDEX.read_bytes())
 rows={v["id"]:v for v in data["roles"]}
 wanted={k for _,ids in AREAS for k in ids}
 if set(rows)!=set(COPY) or set(rows)!=wanted or len(rows)!=15:
  raise ValueError("ROLE_INDEX_OR_COPY_DRIFT")
 lines=[
 "# Specialists by task",
 "",
 "Pick the specialist closest to your task. Each entry explains its scope, the tools included with the toolkit and a concrete starting point.",
 "",
 "[Start here](../v1/START_HERE.md) · [All engines and evidence](../collection/SPECIALIST_SCOPE_AND_ENGINES.md) · [Machine-readable engine index](../discovery/specialist-engine-index.json) · [100 task configurations](../../collections/muse-starters-v1/CATALOG.md)",
 ""
 ]
 for area,ids in AREAS:
  lines.extend(["### "+area,""])
  for rid in ids:
   row=rows[rid]
   title,scope,technical,engine_label,second_label=COPY[rid]
   if rid=="adversarial-verifier":
    assert row["delivery"]=="source-methods" and row["source_engines"]==[]
   else:
    assert row["source_engines"] and engine_label
   profile=f"../../presets/{rid}/README.md"
   link= lambda p:"../../"+p
   need=[profile,row["playbook"],*row["source_engines"],*row["examples"]]
   for item in need:
    full=ROOT/(item.replace("../../","") if item.startswith("../../") else item)
    if not full.is_file():raise ValueError("MISSING_ROLE_SOURCE:"+rid+":"+item)
   lines.append(f"- **[{title}]({profile})** (`{rid}`) — {scope} [Role contract]({link(row['playbook'])}).")
   sources=row["source_engines"]
   if sources:
    chosen=ENGINE_PATHS.get(rid)
    if not chosen or not set(chosen)<=set(sources):
     raise ValueError("ENGINE_LINK_DRIFT:"+rid)
    engine1=f"[{engine_label}]({link(chosen[0])})"
    engine2=f" and [{second_label}]({link(chosen[1])})" if len(chosen)>1 and second_label else ""
    lines.append(f"  **Included tools:** {engine1}{engine2}. {technical}")
   else:
    lines.append(f"  **Included methods:** {technical}")
   if row["examples"]:
    lines.append(f"  [Example or exporter]({link(row['examples'][0])}) · [Full engine scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)")
   else:
    lines.append(f"  [Set up the workroom](../../presets/{rid}/INSTALL.md) · [Full scope](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)")
   lines.append("")
 lines.extend([
 "## Source, engine and connection boundaries",
 "",
 "An editable role profile and a built-in executable engine are different things. The source programs above run specific operations on provided inputs; additional tools, browsers, media renderers and service connectors work only when available and authorized in the receiving Muse environment.",
 "",
 "The old 11-role compatibility catalog is preserved in [the original source list](../collection/SPECIALIST_CATALOG.md). The current registry has 15 unique roles; aliases such as `data-engineer` and `reliability-engineer` are not extra agents.",
 "",
 "The public Adversarial Verifier currently supplies methods and configuration, not a standalone security-testing engine. Reverse Engineering includes supplied-observation analysis. Neither profile is an automatically installed native security agent.",
 "",
 "For exact package contents, see the [V1 release](../RELEASES.md) and [capability matrix](../CAPABILITIES.md).",
 ""
 ])
 return "\n".join(lines)

def main(argv=None):
 parser=argparse.ArgumentParser()
 mode=parser.add_mutually_exclusive_group(required=True)
 mode.add_argument("--check",action="store_true")
 mode.add_argument("--write",action="store_true")
 args=parser.parse_args(argv)
 data=render().encode("utf8")
 if args.check:
  if not OUTPUT.is_file() or OUTPUT.read_bytes()!=data:
   print("DIRECTORY_OUT_OF_DATE");return 2
  print("DIRECTORY_CURRENT_15_ROLES");return 0
 OUTPUT.write_bytes(data)
 print("DIRECTORY_GENERATED_15_ROLES");return 0

if __name__=="__main__":raise SystemExit(main())
