"""Large libraries remain individually discoverable within bounded release packs."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('release_pack_tests', ROOT / 'scripts/build_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class SkillDownloadPacks(unittest.TestCase):
    def catalog(self, count=5201):
        return {'skills': [
            {'id': 'skill-' + str(index).zfill(5), 'title': 'Skill ' + str(index),
             'category': ('engineering', 'research', 'design')[index % 3],
             **({'format': 'portable-skill'} if index >= 75 else {})}
            for index in range(count)
        ]}

    def test_large_library_has_exact_coverage_and_bounded_pack_size(self):
        data = self.catalog()
        layout = release.skill_download_layout(data, 'v2.0.0')
        self.assertEqual(set(layout), {row['id'] for row in data['skills']})
        packs = {}
        for identity, row in layout.items():
            packs.setdefault(row['asset'], []).append(identity)
            self.assertEqual(row['entry'], 'skills/' + identity + '/SKILL.md')
        self.assertLess(len(packs), 250)
        self.assertTrue(all(len(ids) <= release.SKILLS_PER_PACK for ids in packs.values()))
        self.assertTrue(all(layout[row['id']]['pack_size'] == 1 for row in data['skills'][:75]))
        for ids in packs.values():
            self.assertEqual(layout[ids[0]]['pack_size'], len(ids))
        self.assertEqual(layout, release.skill_download_layout(data, 'v2.0.0'))

    def test_source_order_does_not_change_download_routes(self):
        data = self.catalog()
        reversed_data = copy.deepcopy(data)
        reversed_data['skills'].reverse()
        self.assertEqual(release.skill_download_layout(data, 'v2.0.0'),
                         release.skill_download_layout(reversed_data, 'v2.0.0'))

    def test_small_library_keeps_individual_download_urls(self):
        data = self.catalog(461)
        layout = release.skill_download_layout(data, 'v1.5.0')
        self.assertEqual(len({row['asset'] for row in layout.values()}), 461)
        for identity, row in layout.items():
            self.assertEqual(row['asset'], 'muse-skill-' + identity + '-v1.5.0.zip')
            self.assertEqual(row['pack_size'], 1)

    def test_layout_rejects_unsafe_identifiers_and_collisions(self):
        for kind in ('id', 'category', 'duplicate'):
            data = self.catalog()
            if kind == 'duplicate':
                data['skills'][-1]['id'] = data['skills'][-2]['id']
            else:
                data['skills'][-1][kind] = '../bad'
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                release.skill_download_layout(data, 'v2.0.0')

    def test_batch_snapshot_keeps_validated_metadata_immutable(self):
        data=release.collection.load_collection()
        prepared=release.collection.prepare_collection(data)
        original=prepared['skills'][0]['title']
        data['skills'][0]['title']='Changed after preparation'
        self.assertEqual(prepared['skills'][0]['title'],original)
        with self.assertRaises(TypeError):prepared['skills'].append({})
        with self.assertRaises(TypeError):prepared['skills'][0]['title']='Changed'
        with self.assertRaises(TypeError):prepared.update(schema='changed')
        with self.assertRaises(ValueError):release.collection.prepare_collection({'schema':'broken'})
        self.assertIs(release.collection.prepare_collection(prepared),prepared)


if __name__ == '__main__':
    unittest.main()
