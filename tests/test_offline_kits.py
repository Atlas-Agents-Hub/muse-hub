"""H12 exact Family Link source-contract boundary and two-party negative tests."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from muse_presets.catalog import load_preset, load_registry
from muse_presets.family import FamilyLinkRefusal, propose_handoff
from muse_presets.family_envelope import (
    FIELDS, FALSE_FLAGS, SCHEMA, STATE, envelope_sha256,
    prepare_offline_envelope, review_local_envelope,
)
from muse_presets.public_export import PublicExportError, select_public_files

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kits" / "family-handoff"
NOW = datetime(2026, 11, 9, 18, 0, 0, tzinfo=timezone.utc)
H12_FILES = {
    "kits/family-handoff/README.md",
    "kits/family-handoff/envelope-contract.json",
    "kits/family-handoff/role-boundaries.json",
}


def load_json(path: Path) -> dict:
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("DUPLICATE_JSON_FIELD")
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


def fictional_finding():
    observation = "Fictional source-only observation: green sprouts appear.\n"
    return {
        "source_uri": "fictional-example.txt",
        "source_sha256": hashlib.sha256(observation.encode("utf-8")).hexdigest(),
        "observation": observation,
        "result": "FOUND",
    }


class OfflineFamilyH12Tests(unittest.TestCase):
    def test_contract_is_an_exact_projection_of_the_existing_envelope(self):
        envelope = load_json(KIT / "envelope-contract.json")
        self.assertEqual(envelope["schema"], "muse-hub/h12-family-envelope-contract/v1")
        self.assertEqual(envelope["existing_module"], "src/muse_presets/family_envelope.py")
        self.assertEqual(envelope["existing_envelope_schema"], SCHEMA)
        self.assertEqual(envelope["existing_state"], STATE)
        self.assertEqual(envelope["required_fields"], sorted(FIELDS))
        self.assertEqual(envelope["required_false_flags"], sorted(FALSE_FLAGS))
        self.assertEqual(envelope["max_validity_seconds"], 3600)
        self.assertEqual(
            envelope["module_sha256"],
            hashlib.sha256((ROOT / "src/muse_presets/family_envelope.py").read_bytes()).hexdigest(),
        )
        for field in ("native_recipient_authenticated", "sender_authenticated",
                      "effect_authorized", "native_transport_verified",
                      "durable_replay_fence_verified", "delivered"):
            self.assertIs(envelope[field], False, field)

    def test_all_role_boundaries_match_original_disabled_profiles(self):
        data = load_json(KIT / "role-boundaries.json")
        self.assertEqual(data["schema"], "muse-hub/h12-family-role-boundaries/v1")
        self.assertEqual(data["scope"], "OFFLINE_PROJECTION_NOT_NATIVE_IDENTITY")
        expected = load_registry()["presets"]
        self.assertEqual(data["role_ids"], expected)
        self.assertEqual(set(data["roles"]), set(expected))
        for role in expected:
            with self.subTest(role=role):
                item = data["roles"][role]
                original = load_preset(role)
                source = ROOT / "presets" / role / "preset.json"
                self.assertEqual(item["profile_path"], f"presets/{role}/preset.json")
                self.assertEqual(item["profile_sha256"], hashlib.sha256(source.read_bytes()).hexdigest())
                self.assertEqual(item["suggested_receivers"], original["family_link"]["suggested_receivers"])
                self.assertIs(item["enabled"], False)
                self.assertEqual(item["transport"], "unbound")
                self.assertIs(item["recipient_authenticated"], False)
                self.assertIs(item["effect_authorized"], False)

    def test_receiver_self_forgery_mismatched_role_and_replay_refused(self):
        with self.assertRaises(FamilyLinkRefusal):
            propose_handoff("model-builder", "model-builder", request_id="h12-fixture", capability="finding-review")
        with self.assertRaises(FamilyLinkRefusal):
            propose_handoff("model-builder", "invented-agent", request_id="h12-fixture", capability="finding-review")
        envelope = prepare_offline_envelope(
            "model-builder", "research-evaluator", "h12-fixture", "finding-review",
            fictional_finding(), True, "2026-11-09T17:59:00Z",
            "2026-11-09T18:30:00Z", NOW,
        )
        digest = envelope_sha256(envelope)
        with self.assertRaisesRegex(ValueError, "ROLE_MISMATCH"):
            review_local_envelope(envelope, fictional_finding(), digest, [], [], NOW, "claims-adjudicator")
        with self.assertRaisesRegex(ValueError, "REPLAY"):
            review_local_envelope(envelope, fictional_finding(), digest, ["h12-fixture"], [], NOW, "research-evaluator")
        forged = dict(envelope, recipient_authenticated=True)
        with self.assertRaisesRegex(ValueError, "AUTHORITY"):
            review_local_envelope(forged, fictional_finding(), envelope_sha256(forged), [], [], NOW, "research-evaluator")
        checked = review_local_envelope(
            envelope, fictional_finding(), digest, [], [], NOW, "research-evaluator",
        )
        self.assertEqual(checked["status"], "LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED")
        for flag in ("effect_authorized", "sender_authenticated", "recipient_authenticated",
                     "recipient_acknowledged", "durable_replay_fence_verified",
                     "native_transport_invoked"):
            self.assertFalse(checked[flag])

    def test_only_named_h12_contracts_are_admitted_into_public_source(self):
        exported = select_public_files(ROOT, verify_manifest=False)
        self.assertTrue(H12_FILES.issubset(exported))
        with tempfile.TemporaryDirectory(prefix="muse-h12-public-") as d:
            root = Path(d)
            allowed = root / "kits" / "family-handoff"
            allowed.mkdir(parents=True)
            for name in H12_FILES:
                (root / name).write_text("Reviewed source-only contract\n", encoding="utf-8")
            self.assertEqual(set(select_public_files(root, verify_manifest=False)), H12_FILES)
            secret = allowed / "secrets.json"
            secret.write_text('{"token":"unreviewed"}', encoding="utf-8")
            with self.assertRaises(PublicExportError):
                select_public_files(root, verify_manifest=False)
            secret.unlink()
            unknown = root / "kits" / "engineering-doors"
            unknown.mkdir()
            (unknown / "new.json").write_text('{"not":"reviewed"}', encoding="utf-8")
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root, verify_manifest=False)

    def test_readme_keeps_original_authority_and_no_delivery_claim(self):
        text = (KIT / "README.md").read_text(encoding="utf-8")
        self.assertIn("family_envelope.py", text)
        self.assertIn("NOT", text)
        self.assertIn("review_local_envelope", text)
        self.assertIn("../kits/family-handoff/README.md", (ROOT / "docs/README.md").read_text(encoding="utf-8"))
        self.assertIn("NOT_DELIVERED", text)
        self.assertNotIn("native Family Link installed", text)


if __name__ == "__main__":
    unittest.main()
