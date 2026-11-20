"""Source catalog content must be public-safe without losing real service names."""
from pathlib import Path
import json,sys,tempfile,unittest
from muse_presets.distribution import product_findings
from muse_presets.neutrality import audit_public_tree
ROOT=Path(__file__).resolve().parents[1]

class ProductSanitizationTests(unittest.TestCase):
 def test_service_label_is_preserved_without_confusing_it_with_internal_notes(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"docs"/"connectors";p.mkdir(parents=True)
   (p/"CATALOG.md").write_text("# Connector directory\nAsana manages team tasks.\n",encoding="utf8")
   self.assertNotIn("INTERNAL_WORK_LANGUAGE",
                 [v["reason"] for v in product_findings(Path(d))])
 def test_domain_identifiers_are_not_misidentified_as_work_packets(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'docs';p.mkdir()
   (p/'science.md').write_text('# Research methods\nNIH R01 and R21 grants; MITRE T1059 technique; Asana workflow automation.\n',encoding='utf8')
   self.assertEqual(product_findings(Path(d)),[])
 def test_nonservice_internal_markers_remain_blocked(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"docs"/"connectors";p.mkdir(parents=True)
   (p/"CATALOG.md").write_text("# Directory\nAsana prepush notes R123.\n",encoding="utf8")
   self.assertIn("INTERNAL_WORK_LANGUAGE",[x["reason"] for x in product_findings(Path(d))])
 def test_normalized_connector_metadata_has_no_private_paths_or_emails(self):
  doc=ROOT/"docs/connectors/catalog.json"
  self.assertNotIn("PERSONAL_EMAIL_REVIEW_REQUIRED",[x["reason"] for x in audit_public_tree(doc.parent.parent.parent) if x["path"]=="docs/connectors/catalog.json"])
  self.assertNotIn("PRIVATE_HOST_PATH",[x["reason"] for x in audit_public_tree(doc.parent.parent.parent) if x["path"]=="docs/connectors/catalog.json"])
if __name__=="__main__":unittest.main()
