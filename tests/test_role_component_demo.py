"""Component examples require explicit execution and preserve deterministic results."""
from __future__ import annotations
import unittest
from examples.role_component_demo import demonstrate

class ComponentExampleTests(unittest.TestCase):
    def test_default_is_read_only_catalog_without_work(self):
        r=demonstrate()
        self.assertEqual(r["status"],"COMPONENT_CATALOG")
        self.assertEqual(len(r["capabilities"]),6)
        self.assertFalse(r["fixture_executed"])
        self.assertFalse(r["external_effect_authorized"])

    def test_explicit_opt_in_uses_five_real_local_fixtures(self):
        r=demonstrate(run_fixtures=True)
        self.assertEqual(r["status"],"COMPONENT_FIXTURES_PASSED")
        self.assertEqual(len(r["fixtures"]),5)
        self.assertTrue(all(x["status"]=="FIXTURE_PASSED"
                            for x in r["fixtures"].values()))
        self.assertFalse(r["external_effect_authorized"])

    def test_animation_never_misrepresented_as_runnable(self):
        r=demonstrate()
        self.assertFalse(r["capabilities"]["animation"]["executable"])
        self.assertEqual(r["capabilities"]["animation"]["status"],
                         "REFERENCE_GUIDE")
        self.assertNotIn("animation",demonstrate(run_fixtures=True)["fixtures"])

if __name__=="__main__":
    unittest.main()
