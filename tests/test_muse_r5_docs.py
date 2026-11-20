"""Reader-facing product contracts for the additive specialist collection."""
from pathlib import Path
import json,re,unittest
R=Path(__file__).resolve().parents[1]
C=R/'collections/muse-starters-v1'
def current_collection():
    import importlib.util
    spec=importlib.util.spec_from_file_location('current_library_docs', R/'tools/muse_collection.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.load_collection()

class ProductDocumentationTests(unittest.TestCase):
    def test_readme_explains_current_product_and_actual_first_use(self):
        text=(R/'README.md').read_text('utf-8')
        collection=current_collection()
        for term in ('15 independent assistants',"5,200+ skills","nearly 400 workflows","550+ task starters",
                     'tools/muse_collection.py demo data-engineer', 'START_HERE.md',
                     'docs/DOWNLOAD_A_SPECIALIST.md','docs/GETTING_STARTED.md',
                     'docs/TERMINAL.md','docs/GITHUB_QUICKSTART.md'):
            self.assertIn(term,text)
        self.assertLess(len(text.encode()),8000)
    def test_unified_catalog_covers_fifteen_real_packages(self):
        path=R/'docs/collection/SPECIALIST_CATALOG.md';self.assertTrue(path.is_file())
        text=path.read_text('utf-8')
        roles=json.loads((C/'specialists.json').read_text('utf-8'))
        self.assertEqual(len(roles),15)
        for role in roles:self.assertIn(role['id'],text)
        for term in ('DOWNLOAD_A_SPECIALIST.md','START_HERE.md','Main','three subchats',
                     'SPECIALIST_QUICKSTART.md'):
            self.assertIn(term,text)
    def test_new_product_links_resolve(self):
        paths=['docs/collection/SPECIALIST_QUICKSTART.md','docs/collection/SPECIALIST_CATALOG.md',
               'collections/muse-starters-v1/README.md','collections/muse-starters-v1/SKILL_INDEX.md']
        for path in paths:
            page=R/path;self.assertTrue(page.is_file())
            for link in re.findall(r'\]\(([^)#]+)(?:#[^)]+)?\)',page.read_text('utf-8')):
                if '://' not in link:self.assertTrue((page.parent/link).exists(),path+':'+link)
    def test_current_collection_docs_do_not_use_old_inventory_as_current(self):
        page=(C/'README.md').read_text('utf-8')
        intro=page.split('\n## ',1)[0]
        collection=current_collection()
        self.assertRegex(intro,str(len(collection['skills']))+r' (?:reusable |developed )?skills')
        self.assertIn("nearly 400 workflows",intro)
        self.assertNotIn('Current depth: R4',intro)
        self.assertIn('SKILL_INDEX.md',page)
        counts=json.loads((C/'COUNTS.json').read_text('utf-8'))
        self.assertEqual(counts['skills'],len(collection['skills']))
if __name__=='__main__':unittest.main()
