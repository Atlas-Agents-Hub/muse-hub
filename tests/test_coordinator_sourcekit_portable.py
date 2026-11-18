"""R59: exact cross-platform sourcekit canonical profile/receipt serialization."""
from __future__ import annotations
import hashlib,json,subprocess,sys,tempfile,unittest,zipfile
from pathlib import Path
from muse_presets.coordinator_dropin import stage_coordinator_dropin
from muse_presets.coordinator_sourcekit import (
    export_coordinator_sourcekit,verify_coordinator_sourcekit
)


class PortableCoordinatorSourceKitTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix="r59-t19-portable-")
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)

    def export(self):
        folder=self.root/"source"
        archive=self.root/"coordinator.zip"
        result=stage_coordinator_dropin(folder)
        self.assertEqual(result["status"],"COORDINATOR_FILES_CREATED")
        exported=export_coordinator_sourcekit(folder,archive)
        self.assertEqual(exported["status"],"LOCAL_COORDINATOR_SOURCEKIT_EXPORTED")
        with zipfile.ZipFile(archive) as z:
            files={name:z.read(name) for name in z.namelist()}
        return archive,files

    def test_profile_systemfiles_and_digest_receipts_match_portable_lf_bytes(self):
        archive,contents=self.export()
        for name,data in contents.items():
            if (name.startswith("coordinator/profile/") or
                name.startswith("coordinator/system-files/") or
                name=="coordinator/receipts/COORDINATOR_RECEIPT.json"):
                self.assertNotIn(b"\r\n",data,name)
        # Reviewed v1.1.0 neutral profile bytes, after portable LF normalization.
        # 's historical macOS pin remains in git history; this release has new copy.
        release_profile_sha="21d620f75c721d0865f9e008ba7a2624774805b3ef95c283449c2b3319210aaa"
        profile=contents["coordinator/profile/AGENTS.md"]
        self.assertEqual(hashlib.sha256(profile).hexdigest(),release_profile_sha)
        self.assertEqual(profile,contents["coordinator/system-files/AGENTS.md"])
        receipt=json.loads(contents["coordinator/profile/RECEIPT.json"])
        for name,pin in receipt["rendered_sha256"].items():
            self.assertEqual(
                pin,hashlib.sha256(contents["coordinator/profile/"+name]).hexdigest(),name)
        coordinator=json.loads(contents["coordinator/receipts/COORDINATOR_RECEIPT.json"])
        for relative,pin in coordinator["files_sha256"].items():
            self.assertEqual(
                pin,hashlib.sha256(contents["coordinator/"+relative]).hexdigest(),relative)

    def test_fresh_portable_archive_self_hash_doctor_passes_with_newline_normalization(self):
        archive,contents=self.export()
        self.assertEqual(verify_coordinator_sourcekit(
            archive,hashlib.sha256(archive.read_bytes()).hexdigest())["status"],
            "LOCAL_COORDINATOR_SOURCEKIT_VERIFIED")
        extracted=self.root/"fresh"
        extracted.mkdir()
        with zipfile.ZipFile(archive) as z:z.extractall(extracted)
        doctor=extracted/"coordinator/scripts/doctor.py"
        p=subprocess.run([sys.executable,"-I","-B",str(doctor)],
                         capture_output=True,text=True,timeout=25)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        d=json.loads(p.stdout)
        self.assertEqual(d["status"],"LOCAL_SELF_HASH_MATCH")
        self.assertFalse(d["native_authenticated"])
        self.assertFalse(d["external_effect_authorized"])


if __name__=="__main__":
    unittest.main()
