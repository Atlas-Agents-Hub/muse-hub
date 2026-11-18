"""Create and verify specialist packages from the documented quickstart."""
from __future__ import annotations
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

from muse_presets.catalog import load_registry
from muse_presets.standalone_pack import inspect_standalone_pack

ROOT=Path(__file__).resolve().parents[1]
ENTRY=ROOT/"examples"/"github_quickstart.py"

def load():
    spec=importlib.util.spec_from_file_location("github_quickstart",ENTRY)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class GitHubQuickstartTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name)

    def call(self,argv):
        out=io.StringIO()
        with redirect_stdout(out):
            result=load().main(argv)
        return result,json.loads(out.getvalue())

    def test_all_fifteen_roles_in_temporary_directories(self):
        result,data=self.call(["--all"])
        self.assertEqual(result,0)
        self.assertEqual(data["schema"],"r45/github-quickstart-v1")
        self.assertEqual(data["mode"],"PACKAGE_CHECK")
        self.assertEqual(data["role_count"],15)
        self.assertEqual(set(data["roles"]),set(load_registry()["presets"]))
        self.assertEqual(data["total_subchat_scopes"],45)
        self.assertEqual(data["total_disabled_skills"],120)
        for role,item in data["roles"].items():
            self.assertEqual(item["source_inspection"],"LOCAL_STANDALONE_MATCH",role)
            self.assertEqual(item["example_result"],"CONNECTOR_FIXTURE_PASSED")
            self.assertRegex(item["profile_source_sha256"],r"^[0-9a-f]{64}$")
            self.assertEqual(item["subchats"],3)
            self.assertEqual(item["disabled_skills"],8)
        self.assertEqual(list(self.folder.iterdir()),[])

    def test_create_one_role_in_an_absent_directory(self):
        target=self.folder/"fresh-coordinator"
        rc,output=self.call(["--role","coordinator","--to",str(target)])
        self.assertEqual(rc,0)
        self.assertEqual(output["mode"],"PACKAGE_CREATED")
        self.assertEqual(output["role_count"],1)
        self.assertEqual(inspect_standalone_pack(target)["status"],"LOCAL_STANDALONE_MATCH")

    def test_no_target_creates_no_cwd_files(self):
        rc,output=self.call(["--role","garden-companion"])
        self.assertEqual(rc,0)
        self.assertEqual(output["mode"],"PACKAGE_CHECK")
        self.assertEqual(list(self.folder.iterdir()),[])

    def test_preexisting_target_never_overwritten(self):
        path=self.folder/"occupied"
        path.mkdir()
        owner=path/"MEMORY.md"
        owner.write_text("original owner state",encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.call(["--role","coordinator","--to",str(path)])
        self.assertEqual(owner.read_text(),"original owner state")

    def test_empty_parent_never_created(self):
        dest=self.folder/"missing"/"new"
        with self.assertRaises(FileNotFoundError):
            self.call(["--role","coordinator","--to",str(dest)])
        self.assertFalse(dest.parent.exists())

    def test_invalid_role_never_creates_target(self):
        with self.assertRaises(SystemExit):
            self.call(["--role","not-real","--to",str(self.folder/"bad")])
        self.assertEqual(list(self.folder.iterdir()),[])

    def test_all_cannot_write_external_target(self):
        with self.assertRaises(SystemExit):
            self.call(["--all","--to",str(self.folder/"unexpected")])
        self.assertEqual(list(self.folder.iterdir()),[])

    def test_every_role_has_source_accurate_install_guide(self):
        for role in load_registry()["presets"]:
            path=ROOT/"presets"/role/"INSTALL.md"
            doc=path.read_text(encoding="utf-8")
            self.assertIn(role,doc)
            self.assertIn("START_HERE.md",doc)
            self.assertIn("TERMINAL.md",doc)
            self.assertIn("three subchats",doc)
        self.assertEqual(len(load_registry()["presets"]),15)

    def test_release_guide_has_os_commands_and_first_use(self):
        guide=(ROOT/"docs/GITHUB_QUICKSTART.md").read_text(encoding="utf-8")
        for text in ("PowerShell","Windows","macOS","Linux","--all","--role",
                     "PYTHONPATH","INSTALL.md","TERMINAL.md"):
            self.assertIn(text,guide)
        self.assertIn("quickstart.py",guide)
        self.assertIn("tools/muse_collection.py demo data-engineer",guide)
        self.assertIn("new absolute output path",guide)

    def test_extension_guide_references_real_modules_and_stop_rules(self):
        guide=(ROOT/"docs/EXTENDING_GENERIC_AGENTS.md").read_text(encoding="utf-8")
        for text in ("presets/catalog.json","presets/ROLE/playbook.json",
                     "src/muse_presets/role_skills.py","src/muse_presets/portable_connectors.py",
                     "test", "permissions", "owner", "recovery"):
            self.assertIn(text,guide)

    def test_new_docs_exclude_private_identifiers_and_live_grants(self):
        docs=[ROOT/"docs/GITHUB_QUICKSTART.md",ROOT/"docs/EXTENDING_GENERIC_AGENTS.md"]
        docs.extend(ROOT/"presets"/role/"INSTALL.md" for role in load_registry()["presets"])
        for file in docs:
            raw=file.read_text(encoding="utf-8").lower()
            for fragment in ("example-private-network", "legacy-role-zeta", "legacy-role-delta", "legacy-role-gamma",
                             "example-private-host", "legacy-role-eta"):
                self.assertNotIn(fragment,raw,str(file))
            import re
            self.assertNotRegex(raw,r"(?:[a-z]:)?[\\/](?:users|home)[\\/][a-z0-9._-]+[\\/]")

    def test_quickstart_smoke_requires_no_secrets_or_provider(self):
        _,result=self.call(["--role","personal-companion"])
        self.assertEqual(result["roles"]["personal-companion"]["example_result"],
                         "CONNECTOR_FIXTURE_PASSED")
        self.assertFalse(result["external_effect_authorized"])

    def test_quickstart_local_links_resolve_to_real_files(self):
        import re
        guides=[ROOT/"docs/GITHUB_QUICKSTART.md",
                ROOT/"docs/EXTENDING_GENERIC_AGENTS.md",
                ROOT/"README.md"]
        guides.extend(ROOT/"presets"/role/"INSTALL.md" for role in load_registry()["presets"])
        for guide in guides:
            for raw in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",guide.read_text(encoding="utf-8")):
                if "://" in raw or raw.startswith(("mailto:","#")):
                    continue
                linked=(guide.parent/raw).resolve()
                self.assertTrue(linked.is_file() or linked.is_dir(),
                                f"{guide.relative_to(ROOT)} has broken link {raw}")

    def test_documented_local_example_paths_are_real(self):
        import re
        guides=[ROOT/"docs/GITHUB_QUICKSTART.md",
                ROOT/"docs/EXTENDING_GENERIC_AGENTS.md"]
        guides.extend(ROOT/"presets"/role/"INSTALL.md" for role in load_registry()["presets"])
        paths=set()
        for guide in guides:
            paths.update(re.findall(r"examples/[a-z0-9_]+\.py",guide.read_text(encoding="utf-8")))
        self.assertIn("examples/daily_desk.py",paths)
        self.assertIn("quickstart.py --all",(ROOT/"docs/GITHUB_QUICKSTART.md").read_text(encoding="utf-8"))
        self.assertTrue((ROOT/"quickstart.py").is_file())
        for path in sorted(paths):
            self.assertTrue((ROOT/path).is_file(),path)



if __name__=="__main__":
    unittest.main()
