"""Public explorer fail-closed acceptance against the actual shipped JavaScript.

Runs unsafe catalog objects through an isolated Node VM with no network,
browser, credentials, or filesystem mutations. Valid catalogue behavior is
covered by the independent local browser QA.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "hub/site/public/catalog.json"
SCRIPT = ROOT / "hub/site/public/app.js"

JS = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const data = JSON.parse(fs.readFileSync(0, 'utf8'));
const raw = { textContent: JSON.stringify(data) };
const status = { textContent: 'Loading resources.' };
const document = {
  getElementById: id => id === 'catalog-data' ? raw : id === 'count' ? status : null,
};
try {
  vm.runInNewContext(fs.readFileSync('hub/site/public/app.js', 'utf8'),
    { document, URL }, { timeout: 750 });
} catch (error) {
  process.stderr.write('UNHANDLED_' + error.name + ': ' + error.message);
  process.exit(2);
}
if (status.textContent !== 'Catalog verification failed. No sources are shown.') {
  process.stderr.write('NOT_REJECTED: ' + status.textContent);
  process.exit(3);
}
process.stdout.write('CATALOG_REJECTED_NO_EXCEPTION');
"""


@unittest.skipUnless(shutil.which("node"), "Node unavailable for JS runtime negatives")
class ExplorerFailClosed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid = json.loads(CATALOG.read_text(encoding="utf-8"))

    def assert_rejected_without_runtime_exception(self, doc):
        result = subprocess.run(
            ["node", "-e", JS],
            cwd=ROOT,
            input=json.dumps(doc, separators=(",", ":")),
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "CATALOG_REJECTED_NO_EXCEPTION")

    def test_missing_route_membership_array(self):
        doc = copy.deepcopy(self.valid)
        del doc["routes"][0]["source_ids"]
        self.assert_rejected_without_runtime_exception(doc)

    def test_route_object_can_never_be_null(self):
        doc = copy.deepcopy(self.valid)
        doc["routes"][0] = None
        self.assert_rejected_without_runtime_exception(doc)

    def test_route_membership_not_array(self):
        doc = copy.deepcopy(self.valid)
        doc["routes"][0]["source_ids"] = "MH-001"
        self.assert_rejected_without_runtime_exception(doc)

    def test_duplicate_route_id(self):
        doc = copy.deepcopy(self.valid)
        doc["routes"][1]["id"] = doc["routes"][0]["id"]
        self.assert_rejected_without_runtime_exception(doc)

    def test_unknown_route_id(self):
        doc = copy.deepcopy(self.valid)
        doc["routes"][1]["id"] = "hidden-new-route"
        self.assert_rejected_without_runtime_exception(doc)

    def test_unknown_route_item(self):
        doc = copy.deepcopy(self.valid)
        doc["routes"][0]["source_ids"][0] = "MH-999"
        self.assert_rejected_without_runtime_exception(doc)

    def test_null_item(self):
        doc = copy.deepcopy(self.valid)
        doc["items"][0] = None
        self.assert_rejected_without_runtime_exception(doc)

    def test_missing_item_rights(self):
        doc = copy.deepcopy(self.valid)
        del doc["items"][0]["license_class"]
        self.assert_rejected_without_runtime_exception(doc)

    def test_insecure_item_url(self):
        doc = copy.deepcopy(self.valid)
        doc["items"][0]["url"] = "javascript:alert(1)"
        self.assert_rejected_without_runtime_exception(doc)

    def test_external_and_mislabelled_resource_urls(self):
        for url in ("https://github.com/example/muse-cli", "https://muse.ai.example.org/"):
            doc = copy.deepcopy(self.valid)
            doc["items"][0]["url"] = url
            self.assert_rejected_without_runtime_exception(doc)
        doc = copy.deepcopy(self.valid)
        doc["items"][0]["category"] = "Official Meta"
        self.assert_rejected_without_runtime_exception(doc)

    def test_duplicate_item_id(self):
        doc = copy.deepcopy(self.valid)
        doc["items"][1]["id"] = doc["items"][0]["id"]
        self.assert_rejected_without_runtime_exception(doc)

    def test_item_bad_route_tags(self):
        doc = copy.deepcopy(self.valid)
        doc["items"][0]["route_tags"] = ["not-a-public-route"]
        self.assert_rejected_without_runtime_exception(doc)

    def test_item_title_object(self):
        doc = copy.deepcopy(self.valid)
        doc["items"][0]["name"] = {"__proto__": "misleading"}
        self.assert_rejected_without_runtime_exception(doc)


class ExplorerCatalogSourceContract(unittest.TestCase):
    def test_mobile_details_focus_waits_until_panel_is_visible(self):
        script = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("requestAnimationFrame(() => {", script)
        self.assertIn("returnFocus !== trigger", script)
        self.assertIn("window.setTimeout(focusOpenDetail, 120)", script)
        self.assertIn("detail.focus({ preventScroll: true })", script)

    def test_embedded_and_shipped_catalog_are_equal(self):
        import re
        page = (ROOT / "hub/site/public/index.html").read_text(encoding="utf-8")
        match = re.search(
            r'<script\s+id="catalog-data"\s+type="application/json">(.+?)</script>',
            page, re.S,
        )
        self.assertIsNotNone(match, "Expected reviewed inline catalog")
        self.assertEqual(json.loads(match.group(1)),
                         json.loads(CATALOG.read_text(encoding="utf-8")))

    def test_no_dynamic_network_or_markup_sinks(self):
        js = SCRIPT.read_text(encoding="utf-8")
        for forbidden in ("fetch(", "XMLHttpRequest(", "document.write(",
                          ".innerHTML", "eval(", "localStorage", "new Function("):
            self.assertNotIn(forbidden, js)
        self.assertIn("connect-src 'none'",
                      (ROOT / "hub/site/public/index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
