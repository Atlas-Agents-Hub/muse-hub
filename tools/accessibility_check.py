#!/usr/bin/env python3
"""Find five useful accessibility review items in an HTML document's source.

Python 3.10+ standard library; reads one UTF-8 .html/.htm file. No scripts,
stylesheets or network resources are executed. Output is deterministic JSON
(default) or text. Exit codes: 0 checked, 1 findings, 2 input/parse error.

Usage: python -B tools/accessibility_check.py --input page.html [--format text]
"""
from __future__ import annotations

import argparse
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import stat
import sys


MAX_BYTES = 2_000_000
MAX_ELEMENTS = 50_000
MAX_DEPTH = 256
MAX_ATTRIBUTES = 128
MAX_FINDINGS = 1_000
ASCII_SPACE = " \t\r\n\f"
VOID = frozenset(("area", "base", "br", "col", "embed", "hr", "img", "input",
                  "link", "meta", "param", "source", "track", "wbr"))
# HTML's foreign-content parser switches back to HTML for these tokens. The
# source checker refuses the transition instead of approximating a DOM builder.
FOREIGN_BREAKOUT = frozenset(("b", "big", "blockquote", "body", "br", "center", "code",
                             "dd", "div", "dl", "dt", "em", "embed", "h1", "h2", "h3",
                             "h4", "h5", "h6", "head", "hr", "i", "img", "li", "listing",
                             "menu", "meta", "nobr", "ol", "p", "pre", "ruby", "s", "small",
                             "span", "strong", "strike", "sub", "sup", "table", "tt", "u", "ul", "var"))
FOREIGN_TEXT_POINTS = frozenset(("title", "desc", "mi", "mo", "mn", "ms", "mtext"))
RULES = {
    "html-lang": "https://www.w3.org/WAI/standards-guidelines/act/rules/b5c3f8/",
    "page-title": "https://www.w3.org/WAI/standards-guidelines/act/rules/2779a5/",
    "duplicate-id": "https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute",
    "label-target": "https://html.spec.whatwg.org/multipage/forms.html#the-label-element",
    "image-alt": "https://www.w3.org/WAI/standards-guidelines/act/rules/23a2a8/",
}
SCHEMA = "muse-accessibility-source-report/v1"


class SourceCheckError(ValueError):
    """Input cannot be checked within the tool's stated scope."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


def _quoted(value: str) -> str:
    """Bound and escape user text, including terminal controls and bidi marks."""
    return json.dumps(value[:160] + ("..." if len(value) > 160 else ""), ensure_ascii=True)


class SourceParser(HTMLParser):
    # Python 3.10 normally treats only script/style as raw text. These contexts
    # also need shielding from apparent tags. Title/textarea character references
    # are decoded explicitly where title text is needed. Noscript is left to the
    # rendered-browser review; its two scripting modes have different DOMs.
    CDATA_CONTENT_ELEMENTS = ("script", "style", "title", "textarea", "xmp",
                              "iframe", "noembed", "noframes", "noscript")

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.frames = []
        self.root = None
        self.root_closed = False
        self.title = None
        self.title_active = False
        self.ids = {}
        self.labels = []
        self.findings = []
        self.elements = 0

    def _position(self):
        line, column = self.getpos()
        return {"line": line, "column": column + 1}

    def _context(self, name):
        return any(frame[name] for frame in self.frames)

    def _finding(self, rule, element, position, message, suggestion):
        if len(self.findings) >= MAX_FINDINGS:
            raise SourceCheckError("finding-limit", "More than 1000 findings; check a smaller document.")
        self.findings.append({"rule": rule, "element": element, **position,
                              "message": message, "suggestion": suggestion,
                              "reference": RULES[rule]})

    def handle_starttag(self, tag, attributes):
        self._start(tag, attributes, False)

    def handle_startendtag(self, tag, attributes):
        self._start(tag, attributes, True)

    def _start(self, tag, attributes, self_closing):
        self.elements += 1
        if self.elements > MAX_ELEMENTS:
            raise SourceCheckError("element-limit", "More than 50000 start tags; check a smaller document.")
        if len(attributes) > MAX_ATTRIBUTES:
            raise SourceCheckError("attribute-limit", "A start tag has more than 128 attributes.")
        attrs = {}
        for key, value in attributes:
            if key in attrs:
                raise SourceCheckError("duplicate-attribute", "A start tag repeats an attribute; remove the duplicate before checking.")
            attrs[key] = value if value is not None else ""
        position = self._position()
        inert = self._context("inert")
        foreign = self._context("foreign")
        hidden = self._context("hidden") or "hidden" in attrs or attrs.get("aria-hidden", "").lower() == "true"
        if foreign and not inert:
            integration = (tag == "foreignobject" or
                           (tag == "annotation-xml" and attrs.get("encoding", "").lower() in
                            {"text/html", "application/xhtml+xml"}) or
                           self.frames[-1]["tag"] in FOREIGN_TEXT_POINTS or
                           tag in FOREIGN_BREAKOUT or
                           (tag == "font" and any(key in attrs for key in ("color", "face", "size"))))
            if integration:
                raise SourceCheckError("foreign-html-context", "HTML inside SVG or MathML needs a rendered-browser review; check its generated HTML separately.")
        if self.root is None:
            if tag != "html":
                raise SourceCheckError("document-required", "Choose a complete HTML document with an explicit <html> element.")
            self.root = {"attrs": attrs, **position}
        elif tag == "html" and not inert and not foreign:
            raise SourceCheckError("multiple-html", "More than one <html> start tag needs a rendered-browser review.")
        elif self.root_closed:
            raise SourceCheckError("content-after-html", "Content after </html> needs a rendered-browser review.")
        if tag == "plaintext":
            raise SourceCheckError("unsupported-plaintext", "The legacy <plaintext> context needs a rendered-browser review.")
        # In text/html, a slash does not close ordinary HTML elements. Refusing
        # this ambiguous spelling avoids accidentally hiding subsequent content.
        if self_closing and tag not in VOID and not foreign and tag not in {"svg", "math"}:
            raise SourceCheckError("nonvoid-self-close", "A non-void HTML element uses />; provide its closing tag before checking.")
        if not inert:
            ident = attrs.get("id", "")
            if ident:
                if ident in self.ids:
                    first = self.ids[ident]
                    self._finding("duplicate-id", tag, position,
                                  "ID " + _quoted(ident) + " also appears at line " + str(first["line"]) + ".",
                                  "Give each element a unique ID and update references to it.")
                else:
                    self.ids[ident] = position
            if not foreign:
                if tag == "title" and self.title is None:
                    self.title = {"parts": [], **position}
                    self.title_active = True
                if tag == "label" and "for" in attrs:
                    self.labels.append({"target": attrs["for"], **position})
                if tag == "img" and not hidden and "alt" not in attrs:
                    naming = any(attrs.get(key, "").strip(ASCII_SPACE)
                                 for key in ("aria-label", "aria-labelledby", "title"))
                    roles = attrs.get("role", "").lower().split()
                    decorative = bool(roles and roles[0] in {"none", "presentation"})
                    if not naming and not decorative:
                        self._finding("image-alt", tag, position,
                                      "This image has no alt attribute or explicit naming hint.",
                                      'Review its purpose: add descriptive alt text, or alt="" for a decorative image.')
        if tag not in VOID and not self_closing:
            self.frames.append({"tag": tag, "inert": inert or (tag == "template" and not foreign),
                                "foreign": foreign or tag in {"svg", "math"}, "hidden": hidden})
            if len(self.frames) > MAX_DEPTH:
                raise SourceCheckError("depth-limit", "Source nesting exceeds 256 open elements; check a smaller document.")

    def handle_endtag(self, tag):
        matches = [index for index, frame in enumerate(self.frames) if frame["tag"] == tag]
        if not matches:
            return  # HTML permits omitted tags; this tool is not an HTML validator.
        index = matches[-1]
        if any(frame["tag"] in {"template", "svg", "math"} for frame in self.frames[index + 1:]):
            raise SourceCheckError("crossed-context", "An unclosed template or foreign-content context needs a rendered-browser review.")
        if tag == "title":
            self.title_active = False
        if tag == "html":
            self.root_closed = True
        del self.frames[index:]

    def handle_data(self, data):
        if self.title_active:
            self.title["parts"].append(unescape(data))
        if self.frames and self.frames[-1]["tag"] in self.CDATA_CONTENT_ELEMENTS:
            if (self.frames[-1]["tag"] == "title" and self._context("foreign")
                    and re.search(r"<(?:[A-Za-z/]|[!?])", data)):
                raise SourceCheckError("foreign-html-context", "Markup inside an SVG title needs a rendered-browser review.")
            # HTML has an additional script double-escaped state which
            # HTMLParser does not implement. Do not guess its closing boundary.
            if self.frames[-1]["tag"] == "script" and "<!--" in data and re.search(r"<script(?:[\s/>])", data, re.I):
                raise SourceCheckError("script-state", "An escaped legacy script context needs a rendered-browser review.")
            return
        if re.search(r"<(?:[A-Za-z/]|[!?])", data):
            raise SourceCheckError("unparsed-markup", "Incomplete or unsupported markup needs repair before checking.")
        if data.strip(ASCII_SPACE) and (self.root is None or self.root_closed):
            raise SourceCheckError("document-required", "Choose a complete HTML document with content inside <html>.")

    def handle_entityref(self, name):
        if self.title_active:
            self.title["parts"].append(unescape("&" + name + ";"))

    def handle_charref(self, name):
        if self.title_active:
            self.title["parts"].append(unescape("&#" + name + ";"))

    def handle_decl(self, decl):
        if not re.match(r"doctype\s+html(?:\s|$)", decl, re.I):
            raise SourceCheckError("unsupported-declaration", "Choose an HTML document; this declaration is unsupported.")

    def unknown_decl(self, data):
        raise SourceCheckError("unsupported-declaration", "This declaration needs a rendered-browser review.")

    def handle_pi(self, data):
        raise SourceCheckError("unsupported-processing-instruction", "XML and server-template processing instructions must be rendered to HTML first.")

    def finish(self):
        if self.root is None:
            raise SourceCheckError("document-required", "Choose a complete HTML document with an explicit <html> element.")
        if self.cdata_elem or any(frame["tag"] in {"template", "svg", "math"} for frame in self.frames):
            raise SourceCheckError("unclosed-context", "An unclosed text, template or foreign-content context needs repair before checking.")
        if not self.root["attrs"].get("lang", "").strip(ASCII_SPACE):
            self._finding("html-lang", "html", {key: self.root[key] for key in ("line", "column")},
                          "The document has no nonempty lang attribute.",
                          'Set the document language, for example <html lang="en">.')
        if self.title is None or not "".join(self.title["parts"]).strip():
            target = self.title or self.root
            self._finding("page-title", "title" if self.title else "html",
                          {key: target[key] for key in ("line", "column")},
                          "The first HTML title is missing or blank.",
                          "Give the page a concise title that identifies its purpose.")
        for label in self.labels:
            if label["target"] not in self.ids:
                self._finding("label-target", "label", {key: label[key] for key in ("line", "column")},
                              "Label target " + _quoted(label["target"]) + " does not appear in this document source.",
                              "Match for to the control ID; if the control is added later, inspect that rendered state.")
        return sorted(self.findings, key=lambda row: (row["line"], row["column"], row["rule"]))


def check_html(raw: bytes, name: str = "page.html") -> dict:
    """Check bytes already read from a bounded regular file; useful to embedders."""
    if len(raw) > MAX_BYTES:
        raise SourceCheckError("byte-limit", "Input exceeds 2000000 bytes; check a smaller document.")
    try:
        source = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise SourceCheckError("encoding", "Input must be UTF-8 HTML.") from exc
    if re.search(r"[\x00-\x08\x0b\x0e-\x1f\x7f]", source):
        raise SourceCheckError("control-character", "Input contains unsupported control characters.")
    parser = SourceParser()
    try:
        parser.feed(source.replace("\r\n", "\n").replace("\r", "\n"))
        # close() can split an unfinished start tag/comment into data chunks,
        # obscuring that the original source had never completed the token.
        if not parser.cdata_elem and re.search(r"<(?:[A-Za-z/]|[!?])", parser.rawdata):
            raise SourceCheckError("unparsed-markup", "Incomplete markup needs repair before checking.")
        parser.close()
        findings = parser.finish()
    except (AssertionError, RecursionError) as exc:
        raise SourceCheckError("parse", "The document could not be parsed within the supported source checks.") from exc
    return {"schema": SCHEMA, "status": "findings" if findings else "checked",
            "input": {"name": name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()},
            "rules": list(RULES), "finding_count": len(findings), "findings": findings}


def check_file(path: Path) -> dict:
    if path.suffix.lower() not in {".html", ".htm"}:
        raise SourceCheckError("file-type", "Choose a UTF-8 .html or .htm document.")
    try:
        before = path.lstat()
        if not stat.S_ISREG(before.st_mode) or getattr(before, "st_file_attributes", 0) & 0x400:
            raise SourceCheckError("regular-file", "The selected input must be a regular file, not a link or directory.")
        flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
        with os.fdopen(os.open(path, flags), "rb") as stream:
            current = os.fstat(stream.fileno())
            if (not stat.S_ISREG(current.st_mode) or (before.st_dev, before.st_ino) != (current.st_dev, current.st_ino)):
                raise SourceCheckError("input-changed", "Input changed while being opened; choose a stable regular file.")
            if current.st_size > MAX_BYTES:
                raise SourceCheckError("byte-limit", "Input exceeds 2000000 bytes; check a smaller document.")
            raw = stream.read(MAX_BYTES + 1)
    except OSError as exc:
        raise SourceCheckError("read", "Input could not be read; check its path and read permissions.") from exc
    return check_html(raw, path.name)


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise SourceCheckError("arguments", message)


def _emit(report: dict, output_format: str):
    if output_format == "json":
        print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True))
    elif report["status"] == "error":
        print("Source check error [" + report["error"]["code"] + "]: " + report["error"]["message"])
    else:
        print("HTML source: " + _quoted(report["input"]["name"]) + " — " + str(report["finding_count"]) + " review item(s) across five checks.")
        for row in report["findings"]:
            print(str(row["line"]) + ":" + str(row["column"]) + " [" + row["rule"] + "] " + row["message"])
            print("  " + row["suggestion"])


def main(argv=None) -> int:
    parser = ArgumentParser(description="Review five accessibility checks in one HTML document's source.")
    parser.add_argument("--input", type=Path, required=True, help="UTF-8 .html/.htm document (up to 2 MB)")
    parser.add_argument("--format", choices=("json", "text"), default="json", help="report format (default: json)")
    output_format = "json"
    try:
        args = parser.parse_args(argv)
        output_format = args.format
        report = check_file(args.input)
        _emit(report, output_format)
        return 1 if report["findings"] else 0
    except SourceCheckError as exc:
        _emit({"schema": SCHEMA, "status": "error", "error": {"code": exc.code, "message": str(exc)}}, output_format)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
