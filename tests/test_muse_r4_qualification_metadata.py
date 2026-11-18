"""C100 R4 qualification metadata, not a live Muse benchmark."""
from pathlib import Path
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
C=ROOT/"collections/muse-starters-v1"
R4_LANDED_SHA="82abced781e2603a022e1c378a486b5a2e49cf7e"

class R4QualificationMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.counts=json.loads((C/"COUNTS.json").read_text(encoding="utf-8"))
        cls.wave=json.loads((C/"R4_WAVE.json").read_text(encoding="utf-8"))

    def test_depth_and_catalog_ids_still_match_source(self):
        skills=json.loads((C/"skills.json").read_text(encoding="utf-8"))
        starters=json.loads((C/"starters.json").read_text(encoding="utf-8"))
        workflows=json.loads((C/"workflows.json").read_text(encoding="utf-8"))
        self.assertEqual((len(starters),len(skills),len(workflows)),(100,75,25))
        self.assertEqual(sum(bool(x.get("depth")) for x in skills),75)
        self.assertEqual(len({x["id"] for x in skills}),75)
        self.assertEqual(len(self.wave["selected_skill_ids"]),28)
        self.assertEqual(self.counts["foundation_skills_awaiting_depth"],0)

    def test_r4_source_qualification_is_no_longer_marked_candidate(self):
        self.assertEqual(self.counts["r4_acceptance"],"PRIVATE_MAIN_SOURCE_QUALIFIED")
        self.assertEqual(self.wave["state"],"PRIVATE_MAIN_SOURCE_QUALIFIED")
        self.assertEqual(self.counts["r4_acceptance_commit"],R4_LANDED_SHA)
        self.assertEqual(self.wave["r4_acceptance_commit"],R4_LANDED_SHA)
        self.assertEqual(self.counts["r4_ci_run_id"],43262169201)

    def test_historical_qualification_counts_are_truthful_and_scoped(self):
        self.assertEqual(self.counts["r4_focused_test_cases_at_qualification"],397)
        self.assertEqual(self.counts["r4_parent_test_cases_at_qualification"],2041)
        self.assertIn("A_B_C",self.counts["source_test_count_status"])
        self.assertIn("SOURCE_TESTED",self.wave["source_qualification"])
        self.assertEqual(self.counts["paired_muse_comparisons_executed"],0)
        self.assertEqual(self.wave["actual_muse_comparisons"],0)
        self.assertEqual(self.counts["independent_upstream_reviews"],0)

    def test_product_guides_and_historical_qualification_records_stay_distinct(self):
        for path in (C/"README.md",C/"ROADMAP.md",ROOT/"docs/collection/MUSE_CURATED_COLLECTION.md"):
            with self.subTest(path=path):
                text=path.read_text(encoding="utf-8")
                self.assertNotIn("This is a candidate state until",text)
                self.assertNotIn("LOCAL_CANDIDATE_NOT_INTEGRATED",text)
        product=(ROOT/"docs/collection/MUSE_CURATED_COLLECTION.md").read_text(encoding="utf-8")
        for term in ("15 specialist packages", "75 skills", "25 workflows", "100 task starters",
                     "DOWNLOAD_A_SPECIALIST.md", "SPECIALIST_QUICKSTART.md", "PUBLIC_COMPATIBILITY.json"):
            self.assertIn(term,product)
        self.assertNotIn("## R4 source qualification",product)
        self.assertEqual(self.counts["paired_muse_comparisons_executed"],0)
        self.assertEqual(self.wave["actual_muse_comparisons"],0)
        self.assertNotIn("LOCAL_CANDIDATE_NOT_INTEGRATED",(C/"R4_WAVE.json").read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
