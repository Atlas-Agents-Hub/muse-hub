"""Browser-script fail-closed guard for malformed offline Hub discovery records."""
from __future__ import annotations

import copy
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "hub/site/public/index.html"
APP = ROOT / "hub/site/public/app.js"


def catalog() -> dict:
    page = PAGE.read_text(encoding="utf-8")
    match = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>', page, re.S)
    if match is None:
        raise AssertionError("Missing embedded catalog-data source")
    return json.loads(match.group(1))


def execute_under_minimal_document(data: dict) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if not node:
        raise unittest.SkipTest("Node.js not installed; browser JS validation check unavailable")
    program = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(process.argv[1], 'utf8');
const data = JSON.parse(process.argv[2]);
const status = {textContent:'Loading resources…'};
const document = {
  getElementById(id) {
    if (id === 'catalog-data') return {textContent:JSON.stringify(data)};
    if (id === 'count') return status;
    return null;
  }
};
try {
  vm.runInNewContext(source, {document, URL, console}, {timeout: 1000});
} catch (error) {
  console.error('UNCAUGHT_CATALOG_ERROR:', error.name, error.message);
  process.exit(2);
}
if (status.textContent !== 'Catalog source restriction failed. No sources are shown.') {
  console.error('FAIL_OPEN:', status.textContent);
  process.exit(3);
}
console.log('CATALOG_FAIL_CLOSED');
"""
    return subprocess.run([node, "-e", program, str(APP), json.dumps(data)],
                          capture_output=True, text=True, timeout=12)


class InvalidCatalogMustNotCrash(unittest.TestCase):
    def test_invalid_catalog_item_and_route_shapes_fail_closed(self):
        source = catalog()
        variants = {
            "null item": lambda d: d["items"].__setitem__(0, None),
            "item rights absent": lambda d: d["items"][0].pop("license_class"),
            "null route": lambda d: d["routes"].__setitem__(0, None),
            "missing source ids": lambda d: d["routes"][0].pop("source_ids"),
            "nonarray source ids": lambda d: d["routes"][0].__setitem__("source_ids", None),
            "nonnumeric source identifier": lambda d: d["routes"][0].__setitem__("source_ids", [42]),
            "duplicate route identifiers": lambda d: d["routes"][1].__setitem__("id", d["routes"][0]["id"]),
        }
        for description, corrupt in variants.items():
            record = copy.deepcopy(source)
            corrupt(record)
            with self.subTest(description=description):
                result = execute_under_minimal_document(record)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("CATALOG_FAIL_CLOSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
