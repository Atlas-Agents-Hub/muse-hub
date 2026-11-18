"""Behavior and false-positive controls for the packaged HTML source checker."""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "accessibility_check.py"
EXAMPLES = ROOT / "collections" / "muse-starters-v1" / "skills" / "accessible-ui" / "examples"


def document(body="", *, lang=' lang="en"', title="Source review"):
    return '<!doctype html>\n<html' + lang + '>\n<head><title>' + title + '</title></head>\n<body>\n' + body + '\n</body>\n</html>\n'


class AccessibilityCheckTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("accessibility_check_under_test", TOOL)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def checked(self, source):
        return self.mod.check_html(source.encode("utf-8"))

    def run_cli(self, args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            result = self.mod.main(args)
        return result, out.getvalue(), err.getvalue()

    def file_cli(self, source, *, suffix=".html", fmt="json"):
        path = self.root / ("page" + suffix)
        path.write_bytes(source.encode("utf-8") if isinstance(source, str) else source)
        return self.run_cli(["--input", str(path), "--format", fmt])

    def rejected(self, source, code):
        with self.assertRaises(self.mod.SourceCheckError) as caught:
            self.checked(source)
        self.assertEqual(caught.exception.code, code)

    def test_independent_five_rule_fixture_and_positions(self):
        source = document('<label for="missing">Email</label>\n<img src="portrait.png">\n<div id="same"></div>\n<span id="same"></span>', lang="", title=" ")
        result = self.checked(source)
        self.assertEqual(result["status"], "findings")
        self.assertEqual(result["finding_count"], 5)
        self.assertEqual([(row["line"], row["column"], row["rule"]) for row in result["findings"]],
                         [(2, 1, "html-lang"), (3, 7, "page-title"), (5, 1, "label-target"),
                          (6, 1, "image-alt"), (8, 1, "duplicate-id")])
        self.assertEqual(result["input"]["sha256"], hashlib.sha256(source.encode()).hexdigest())
        self.assertEqual(result["input"]["bytes"], len(source.encode()))
        for row in result["findings"]:
            self.assertTrue(row["reference"].startswith(("https://www.w3.org/", "https://html.spec.whatwg.org/")))
            self.assertTrue(row["suggestion"])

    def test_empty_alt_and_alternative_naming_hints_are_controls(self):
        body = '''<img src="a.png" alt=""><img src="b.png" alt>
<img src="c.png" aria-label="Route map"><img src="d.png" aria-labelledby="dynamic-label">
<img src="e.png" title="Route map"><img src="f.png" role="presentation">
<img src="g.png" role="none"><img src="h.png" hidden>
<div hidden><img src="i.png"></div><div aria-hidden="true"><img src="j.png"></div>'''
        self.assertEqual(self.checked(document(body))["findings"], [])
        findings = self.checked(document('<img aria-label=" " role="button presentation">'))["findings"]
        self.assertEqual([row["rule"] for row in findings], ["image-alt"])

    def test_label_targets_are_exact_and_implicit_labels_need_no_for(self):
        body = '<label><input name="email"> Email</label><label for="A&amp;B">Name</label><input id="A&amp;B"><label for="a&amp;b">Other</label>'
        findings = self.checked(document(body))["findings"]
        self.assertEqual([row["rule"] for row in findings], ["label-target"])
        self.assertIn('a&b', findings[0]["message"])

    def test_duplicate_ids_decode_entities_and_preserve_case(self):
        findings = self.checked(document('<p id="A"></p><p id="a"></p><p id="A&#38;B"></p><p id="A&amp;B"></p>'))["findings"]
        self.assertEqual([row["rule"] for row in findings], ["duplicate-id"])
        self.assertIn('A&B', findings[0]["message"])

    def test_template_is_a_separate_tree_and_its_own_id_is_live(self):
        body = '<p id="same"></p><template id="holder"><img><p id="same"></p><template><p id="same"></p></template></template><p id="holder"></p>'
        findings = self.checked(document(body))["findings"]
        self.assertEqual([row["rule"] for row in findings], ["duplicate-id"])
        self.assertIn('holder', findings[0]["message"])
        result = self.checked(document('<label for="inside">Name</label><template><input id="inside"></template>'))
        self.assertEqual([row["rule"] for row in result["findings"]], ["label-target"])

    def test_raw_text_comments_and_noscript_do_not_create_findings(self):
        body = '''<script>const sample = '<img><label for="missing"></label>';</script>
<style>/* <img><p id="same"> */</style><textarea><img></textarea>
<noscript><img></noscript><iframe title="Example"><img></iframe>
<!-- <img><label for="missing"> -->&lt;img alt=&quot;&quot;&gt;'''
        self.assertEqual(self.checked(document(body))["findings"], [])

    def test_first_html_title_is_used_even_in_body_and_svg_title_is_not(self):
        source = '<html lang="en"><body><svg><title>Icon</title></svg><title>Page</title><title></title></body></html>'
        self.assertEqual(self.checked(source)["findings"], [])
        source = '<html lang="en"><body><svg><title>Icon</title></svg></body></html>'
        self.assertEqual([row["rule"] for row in self.checked(source)["findings"]], ["page-title"])
        source = '<html lang="en"><title> </title><title>Later title</title></html>'
        self.assertEqual([row["rule"] for row in self.checked(source)["findings"]], ["page-title"])
        self.assertEqual(self.checked(document(title="A &amp; B &lt; C"))["findings"], [])

    def test_optional_html_end_tags_and_foreign_ids_are_accepted(self):
        source = '<html lang="en"><title>Page</title><body><p>One<p>Two'
        self.assertEqual(self.checked(source)["findings"], [])
        body = '<svg><g id="art"><path d="M0 0"/></g></svg><label for="art">Review in browser</label>'
        self.assertEqual(self.checked(document(body))["findings"], [])

    def test_dynamic_aria_and_heading_order_are_outside_five_rules(self):
        body = '<h1>Page</h1><h3>Section</h3><input aria-errormessage="not-added-yet"><button aria-controls="later">Open</button>'
        self.assertEqual(self.checked(document(body))["findings"], [])

    def test_utf8_bom_uppercase_html_and_crlf_are_supported(self):
        source = '\ufeff<!DOCTYPE HTML>\r\n<HTML LANG="en">\r\n<TITLE>Résumé</TITLE>\r\n<BODY><IMG></BODY></HTML>'
        findings = self.checked(source)["findings"]
        self.assertEqual([(row["line"], row["column"], row["rule"]) for row in findings], [(4, 7, "image-alt")])

    def test_blank_ascii_language_and_missing_title_are_findings(self):
        result = self.checked('<html lang="&#32;&#9;\n"><body></body></html>')
        self.assertEqual({row["rule"] for row in result["findings"]}, {"html-lang", "page-title"})

    def test_unsupported_markup_has_explicit_errors(self):
        cases = [
            ('<img alt="example">', "document-required"),
            ('<html lang="en"><html></html>', "multiple-html"),
            (document('<img alt="" ALT="duplicate">'), "duplicate-attribute"),
            (document('<div/>'), "nonvoid-self-close"),
            (document('<plaintext>'), "unsupported-plaintext"),
            (document('<template><span></span>'), "crossed-context"),
            ('<html lang="en"><title>Page</title><template>', "unclosed-context"),
            ('<html lang="en"><title>Page', "unclosed-context"),
            ('<html lang="en"><title>Page</title><img alt="unfinished', "unparsed-markup"),
            ('<html lang="en"><title>Page</title><body><input id="oops></body></html>', "unparsed-markup"),
            (document('<!-- unfinished comment'), "unparsed-markup"),
            (document('<script><!-- <script>nested</script>'), "script-state"),
            ('<?xml version="1.0"?>' + document(), "unsupported-processing-instruction"),
            (document() + '<p>After document</p>', "content-after-html"),
        ]
        for source, code in cases:
            with self.subTest(code=code):
                self.rejected(source, code)

    def test_foreign_html_transitions_are_explicitly_unsupported(self):
        cases = [
            '<svg><foreignObject><div><img><label for="gone">Name</label></div></foreignObject></svg>',
            '<math><annotation-xml encoding="text/html"><img></annotation-xml></math>',
            '<math><annotation-xml encoding="application/xhtml+xml"><img></annotation-xml></math>',
            '<svg><title>Icon <img></title></svg>',
            '<svg><desc><label for="gone">Name</label></desc></svg>',
            '<math><mtext><img></mtext></math>',
            '<svg><img></svg>',
        ]
        for body in cases:
            with self.subTest(body=body):
                self.rejected(document(body), "foreign-html-context")
        self.assertEqual(self.checked(document('<svg><title>Icon</title><desc>A shape</desc></svg><math><mi>x</mi></math>'))["findings"], [])

    def test_invalid_encoding_controls_and_wrong_extension_do_not_succeed(self):
        for raw, suffix, expected in [(b'\xff', '.html', 'encoding'), (b'\x00', '.html', 'control-character'),
                                      (document().encode(), '.txt', 'file-type')]:
            with self.subTest(expected=expected):
                code, out, err = self.file_cli(raw, suffix=suffix)
                self.assertEqual((code, err), (2, ""))
                result = json.loads(out)
                self.assertEqual(result["status"], "error")
                self.assertEqual(result["error"]["code"], expected)
                self.assertNotIn("finding_count", result)
                self.assertNotIn("findings", result)

    def test_missing_directory_link_and_unreadable_input_do_not_succeed(self):
        missing = self.root / "missing.html"
        directory = self.root / "directory.html"
        directory.mkdir()
        paths = [(missing, "read"), (directory, "regular-file")]
        original = self.root / "original.html"
        original.write_text(document(), encoding="utf-8")
        link = self.root / "link.html"
        try:
            link.symlink_to(original)
        except (OSError, NotImplementedError):
            pass  # Creating symlinks may require privileges on Windows.
        else:
            paths.append((link, "regular-file"))
        for path, expected in paths:
            with self.subTest(path=path.name):
                code, out, _ = self.run_cli(["--input", str(path)])
                self.assertEqual(code, 2)
                self.assertEqual(json.loads(out)["error"]["code"], expected)
        with mock.patch.object(self.mod.os, "open", side_effect=PermissionError("denied")):
            code, out, _ = self.run_cli(["--input", str(original)])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(out)["error"]["code"], "read")

    def test_bytes_bound_at_limit_and_over_limit(self):
        base = document()
        padding = " " * (self.mod.MAX_BYTES - len(base.encode()))
        self.assertEqual(self.checked(base + padding)["status"], "checked")
        code, out, _ = self.file_cli(base + padding + " ")
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(out)["error"]["code"], "byte-limit")

    def test_element_depth_attribute_and_finding_limits(self):
        cases = [
            (document('<br>' * self.mod.MAX_ELEMENTS), "element-limit"),
            (document('<div>' * self.mod.MAX_DEPTH), "depth-limit"),
            (document('<div ' + ' '.join('data-a' + str(i) + '="x"' for i in range(self.mod.MAX_ATTRIBUTES + 1)) + '></div>'), "attribute-limit"),
            (document('<img>' * (self.mod.MAX_FINDINGS + 1)), "finding-limit"),
        ]
        for source, code in cases:
            with self.subTest(code=code):
                self.rejected(source, code)

    def test_deterministic_json_text_escaping_and_cli_exit_codes(self):
        source = document('<label for="evil&#27;[2J&#8238;id">Name</label>')
        first = self.file_cli(source)
        second = self.file_cli(source)
        self.assertEqual(first, second)
        self.assertEqual(first[0], 1)
        self.assertEqual(first[2], "")
        code, out, err = self.file_cli(source, fmt="text")
        self.assertEqual((code, err), (1, ""))
        self.assertIn("label-target", out)
        self.assertNotIn("\x1b", out)
        self.assertNotIn("\u202e", out)
        self.assertIn("\\u202e", out)
        self.assertEqual(self.file_cli(document())[0], 0)

    def test_invalid_arguments_are_json_errors(self):
        code, out, err = self.run_cli(["--format", "table"])
        self.assertEqual((code, err), (2, ""))
        self.assertEqual(json.loads(out)["error"]["code"], "arguments")

    def test_documented_examples_execute_from_an_independent_directory(self):
        for filename, expected_code, expected_rules in [
            ("clean.html", 0, set()),
            ("review.html", 1, set(self.mod.RULES)),
        ]:
            with self.subTest(filename=filename):
                source = EXAMPLES / filename
                before = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
                result = subprocess.run([sys.executable, "-B", str(TOOL), "--input", str(source)],
                                        cwd=self.root, capture_output=True, text=True, timeout=10)
                self.assertEqual((result.returncode, result.stderr), (expected_code, ""))
                report = json.loads(result.stdout)
                self.assertEqual({row["rule"] for row in report["findings"]}, expected_rules)
                self.assertEqual({p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}, before)
                self.assertFalse(any(p.is_dir() for p in self.root.iterdir()))

    def test_current_public_html_is_supported(self):
        for relative in ("hub/site/index.html", "hub/site/public/index.html", "hub/site/downloads.html"):
            with self.subTest(relative=relative):
                result = self.mod.check_file(ROOT / relative)
                self.assertIn(result["status"], ("checked", "findings"))
                self.assertEqual(result["finding_count"], len(result["findings"]))


if __name__ == "__main__":
    unittest.main()
