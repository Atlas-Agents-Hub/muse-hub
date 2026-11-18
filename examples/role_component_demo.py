"""List specialist components or run their reviewed examples."""
from __future__ import annotations
import argparse,json
from muse_presets.catalog import ROOT
from muse_presets.component_source import list_components,run_component_fixture

RUNNABLE=("claims","evaluation","garden","security","study")

def demonstrate(*,run_fixtures:bool=False)->dict:
    report=list_components(ROOT)
    if not run_fixtures:
        return {"schema":"muse-presets/role-component-demo-v1",
                "status":"COMPONENT_CATALOG",
                "capabilities":report["capabilities"],
                "fixture_executed":False,
                "external_effect_authorized":False}
    outputs={name:run_component_fixture(ROOT,name,allow_reviewed_fixture=True)
             for name in RUNNABLE}
    if any(item["status"]!="FIXTURE_PASSED" for item in outputs.values()):
        raise ValueError("COMPONENT_FIXTURE_NOT_COMPLETE")
    return {"schema":"muse-presets/role-component-demo-v1",
            "status":"COMPONENT_FIXTURES_PASSED",
            "capabilities":report["capabilities"],
            "fixtures":outputs,
            "fixture_executed":True,
            "external_effect_authorized":False}

def main(argv=None)->int:
    parser=argparse.ArgumentParser(description="Inspect specialist components and run their examples")
    parser.add_argument("--run-fixtures",action="store_true",
                        help="Opt into local, reviewed first-party Python fixtures")
    args=parser.parse_args(argv)
    print(json.dumps(demonstrate(run_fixtures=args.run_fixtures),
                     sort_keys=True,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
