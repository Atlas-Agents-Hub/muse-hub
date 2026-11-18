# Check HTML before your interface review

Find missing page metadata, repeated IDs, disconnected labels and images that
need a text-alternative review. Each result gives a source location and a next
action. Use this short check before the keyboard, zoom and screen-reader work
in this skill.

## Run the examples

Use Python 3.10 or newer from the extracted package folder:

```sh
python -B tools/accessibility_check.py --input skills/accessible-ui/examples/clean.html
python -B tools/accessibility_check.py --input skills/accessible-ui/examples/review.html --format text
```

The first example returns exit code `0` and no source findings. The second
returns exit code `1` with five review items: language, title, image text, label
target and a repeated ID. Its errors are intentional so you can see the report.

Check your generated HTML with:

```sh
python -B tools/accessibility_check.py --input page.html --format json
```

JSON is the default. The tool reads your document and prints the complete
report to the terminal. It does not modify the document or load linked assets.

## What the five checks cover

| Check | Reported source condition | Review action |
|---|---|---|
| `html-lang` | The explicit `<html>` element has no `lang`, or its value is empty or ASCII whitespace. | Set the page's language, then verify it matches the content. |
| `page-title` | The first HTML `<title>` is absent or contains only whitespace. An SVG title does not substitute for it. | Give the page a descriptive title. |
| `duplicate-id` | A later element repeats a nonempty ID in the checked document source. IDs are case-sensitive; character references are decoded. Template contents are excluded. | Assign unique IDs and update references. |
| `label-target` | A `<label for="…">` has no matching ID in this source. | Match it to its control. If code adds the control later, inspect the rendered state. |
| `image-alt` | An HTML `<img>` lacks `alt` and has no nonempty `aria-label`, `aria-labelledby` or `title`, or explicit decorative role. Explicitly hidden images are excluded. | Decide whether it needs descriptive text or `alt=""`. |

The image check accepts empty `alt`, and the label check accepts wrapping labels
without `for`. Alternative naming attributes are useful hints here; their
presence does not establish an image's computed accessible name. A label target
being present does not establish that the target is an appropriate control.

## Read and use the result

Reports use the schema `muse-accessibility-source-report/v1`. JSON includes the
five rule IDs, input filename, byte count and SHA-256, plus the findings in
line, column and rule order. Lines and columns start at `1`; columns count
characters. Newline conventions are normalized for locations. The input hash
identifies the original bytes, including a UTF-8 byte-order mark if present.

| Exit code | JSON status | Meaning |
|---|---|---|
| `0` | `checked` | The five source checks produced no review items. |
| `1` | `findings` | Review the listed locations and suggested repairs. |
| `2` | `error` | The input could not be checked; fix the reported input or parsing issue. |

Error reports have an error code and message, without a zero-findings result.
Repeated checks of the same filename and bytes produce the same report.
JSON escapes control characters; text reports also escape input identifiers.

After a repair, rerun the source check and the affected user journey. Keep
keyboard order, focus return, zoom/reflow, computed names and actual colors in
the rendered-interface review. For an optional color-pair calculation,
[download Design Token Audit](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.4.0/muse-skill-design-token-audit-v1.4.0.zip)
and follow its included examples. These five source checks produce review
items, not a WCAG conformance verdict.

## Inputs and boundaries

Choose one regular UTF-8 `.html` or `.htm` file with an explicit `<html>` element.
A UTF-8 byte-order mark and Windows line endings are accepted. Build JSX,
server templates or other source formats into HTML first.

The limits are 2,000,000 bytes, 50,000 start tags, 256 open elements, 128
attributes per start tag and 1,000 findings. Exceeding a limit returns an error.
Missing or unreadable files, directories, selected-file symlinks, invalid UTF-8
and unsupported control characters also return errors.

The parser reads source tokens. It does not implement browser DOM repair,
computed CSS or JavaScript execution. Comments, script/style/text containers,
`noscript` content and inert template contents do not become page findings.
HTML-specific image, label and title checks skip SVG and MathML descendants;
their IDs remain available to the document ID checks. This keeps icon titles
and template examples from being mistaken for page content.

HTML integration inside SVG or MathML returns an explicit error: for example,
`foreignObject`, an HTML-encoded `annotation-xml`, nested markup in an SVG
title/description or MathML text container, and HTML tags that make a browser
leave foreign-content parsing. Inspect those rendered states in a browser.

Duplicate attributes, non-void HTML elements spelled with `/>`, unclosed
text/template/foreign-content contexts, legacy `<plaintext>`, processing
instructions and ambiguous legacy escaped scripts require repair or a browser
review. Other HTML validation is a separate task. Optional end tags are
accepted, but deeply repeated omitted tags can reach the open-element limit.

## Reference basis

- [W3C: HTML page has a lang attribute](https://www.w3.org/WAI/standards-guidelines/act/rules/b5c3f8/)
- [W3C: HTML page has a nonempty title](https://www.w3.org/WAI/standards-guidelines/act/rules/2779a5/)
- [WHATWG: ID attribute](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute)
- [WHATWG: Label element](https://html.spec.whatwg.org/multipage/forms.html#the-label-element)
- [W3C: Image has a nonempty accessible name](https://www.w3.org/WAI/standards-guidelines/act/rules/23a2a8/)
- [W3C: ARIA value rules and dynamic ID-reference exceptions](https://www.w3.org/WAI/standards-guidelines/act/rules/6a7281/)
- [W3C: Parsing criterion removed in WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/parsing.html)
- [Python: HTMLParser behavior](https://docs.python.org/3/library/html.parser.html)
- [WHATWG: Foreign-content parsing](https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inforeign)

The rules are informed by these sources and deliberately narrower than a full
ACT implementation. Missing dynamic ARIA targets and heading-level jumps are
not automatic findings. Repeated IDs are reported as a source repair item,
without treating the removed WCAG parsing criterion as a current requirement.
The checker and examples are original Muse Hub code and content.
