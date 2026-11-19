"""Render the GitHub-native, use-case-oriented connector directory.

This is a deterministic presentation of the already reviewed source-pinned
metadata. It does not fetch code, install connectors or contact any provider.
"""
from __future__ import annotations

import argparse
import json
import re
import html
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "docs" / "connectors"
CATALOG = DIRECTORY / "catalog.json"

# These are editorial navigation groups, not additional connector identities.
GROUPS = (
    ("Work and productivity", "Plans, messages, scheduling, documents and everyday teamwork.", (
        "Productivity", "Project management", "Scheduling", "Notes & docs",
        "Email", "Communication", "Support")),
    ("AI, research and data", "Model services, information retrieval and structured knowledge.", (
        "AI & ML", "Search & Data", "Translation", "Memory")),
    ("Development and infrastructure", "Code hosting, cloud services, deployment and observability.", (
        "Developer & Infra", "Cloud & hosting", "Monitoring")),
    ("Design and creative", "Design, images, sound, video and creative production.", (
        "Media generation", "Design", "Voice AI", "Media management", "Video", "Stock media")),
    ("Business and commerce", "Commerce, financial tools, contacts and business operations.", (
        "Finance & Commerce", "Sales & CRM", "E-commerce", "Jobs",
        "Logistics", "Marketing")),
    ("Home and devices", "Connected homes, hardware, vehicles and energy.", (
        "Smart home", "3D printing", "Vehicles", "Energy", "Agritech", "Weather")),
    ("Publishing and social", "Share, publish, stream and build an audience.", (
        "Newsletters", "Social", "Podcasting", "Blogging", "Creator", "Livestreaming")),
    ("Everyday and more", "Travel, personal information, reading and additional services.", (
        "Travel", "Health", "Reading", "Other")),
)

def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")

def visible(text: str) -> str:
    return text

def safe_short(text: str, limit: int = 156) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) > limit:
        cut = text.rfind(" ", 0, limit - 1)
        text = text[:cut if cut > limit // 2 else limit - 1].rstrip(" ,;:") + "…"
    text = text.replace("]", "\\]").replace("[", "\\[")
    return visible(text)

def read_catalog() -> dict:
    data = json.loads(CATALOG.read_bytes())
    if data.get("schema") != "muse-specialist-toolkit/connectors-v2":
        raise ValueError("UNRECOGNIZED_CONNECTOR_DATA")
    rows = data.get("connectors")
    if not isinstance(rows, list) or len(rows) != 151 + data.get('extensions',{}).get('count',0):
        raise ValueError("CONNECTOR_INVENTORY_CHANGED")
    if len({x["id"] for x in rows}) != len(rows):
        raise ValueError("DUPLICATE_CONNECTORS")
    all_categories = {cat for _, _, cats in GROUPS for cat in cats}
    if len(all_categories) != sum(len(cats) for _, _, cats in GROUPS):
        raise ValueError("OVERLAPPING_EDITORIAL_CATEGORIES")
    if {x["category"] for x in rows} != all_categories:
        raise ValueError("UNMAPPED_CONNECTOR_CATEGORY")
    if len({slug(title) for title, _, _ in GROUPS}) != len(GROUPS):
        raise ValueError("DUPLICATE_CATEGORY_LINKS")
    pin = data["source"]["commit"]
    for row in rows:
        expected = ("https://github.com/bluman1/muse-connectors/blob/" + pin + "/connectors/" + row["id"] + "/SKILL.md" if row.get('source_id','muse-connectors')=='muse-connectors' else
                    'https://github.com/activepieces/activepieces/blob/'+data['extensions']['commit']+'/packages/pieces/community/'+row['id']+'/src/index.ts')
        if row["source_url"] != expected:
            raise ValueError("UNPINNED_CONNECTOR_LINK")
    return data


def render_html(rows: list[dict]) -> bytes:
    esc = lambda value: html.escape(str(value), quote=True)
    categories = sorted({row['category'] for row in rows})
    roles = sorted({role for row in rows for role in row['specialists']})
    parts = ['<!doctype html>', '<html lang="en"><head>',
             '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
             '<meta name="color-scheme" content="light">',
             '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; script-src \'self\'; style-src \'self\'; connect-src \'none\'; img-src \'none\'; base-uri \'none\'; form-action \'none\'">',
             '<title>Muse Hub | Custom connectors for your apps and services</title>',
             f'<meta name="description" content="Explore {len(rows)} Muse custom connectors for work, research and creative projects. Find app setup guides, useful actions and ready-to-use task prompts.">',
             '<link rel="stylesheet" href="app.css"><script defer src="app.js"></script></head><body>',
             '<a class="skip" href="#catalog">Skip to connector directory</a>',
             '<header class="mast"><a class="brand" href="../../README.md" aria-label="Muse Hub home"><span class="monogram" aria-hidden="true">M/</span><span>Muse Hub</span></a><nav aria-label="Page navigation"><a href="../v1/START_HERE.md">Start here</a><a href="README.md">Connector setup</a><a href="CATALOG.md">All categories</a></nav></header>',
             '<main><section class="hero" aria-labelledby="title"><p class="eyebrow">MUSE HUB / CONNECTORS</p><h1 id="title">Bring your tools into the conversation.</h1>',
             '<p class="intro">Find your service, choose an action and give Muse a useful task. Connect documents, calendars, customers, databases, creative tools and the rest of your day.</p>',
             f'<div class="metrics"><div><strong>{len(rows)}</strong><span>Custom connectors</span></div><div><strong>{len(categories)}</strong><span>Categories</span></div><div><strong>{len(roles)}</strong><span>Specialist assistants</span></div></div></section>',
             '<section id="catalog" class="directory" aria-labelledby="catalog-title"><div class="section-header"><div><p class="eyebrow">FIND YOUR TOOLS</p><h2 id="catalog-title">Choose a connector</h2></div><p>Setup instructions, service actions and task prompts in one place.</p></div>',
             '<div class="filters"><div><label for="connector-search">Search services and capabilities</label><input id="connector-search" type="search" placeholder="Try Google Drive, support tickets, design or SQL" autocomplete="off"></div>',
             '<div><label for="category-filter">Category</label><select id="category-filter"><option value="">All categories</option>',
             *[f'<option value="{esc(cat)}">{esc(cat)}</option>' for cat in categories],
             '</select></div><div><label for="specialist-filter">Specialist</label><select id="specialist-filter"><option value="">All specialists</option>',
             *[f'<option value="{esc(role)}">{esc(role.replace("-", " ").title())}</option>' for role in roles],
             '</select></div></div>',
             f'<div class="directory-tools"><p id="results" role="status" aria-live="polite">Showing all {len(rows)} connectors.</p><button id="reset" class="secondary" type="button">Clear filters</button></div><div id="cards" class="cards">']
    for row in rows:
        identifier = esc(row['id'])
        keywords = ' '.join([row['id'], row['name'], row['description'], row['category'], row['operations']]).lower()
        guide_url = row.get('guide_path', row['source_url'])
        parts += [f'<details class="connector-card" id="{identifier}" data-name="{esc(row["name"].lower())}" data-keywords="{esc(keywords)}" data-category="{esc(row["category"])}" data-specialists="{esc(" ".join(row["specialists"]))}">',
                  f'<summary><span class="service"><strong>{esc(row["name"])}</strong><small>{esc(row["category"])}</small></span><span class="chevron" aria-hidden="true">+</span></summary>',
                  f'<div class="card-body"><p class="description">{esc(row["description"])}</p>',
                  f'<dl><dt>Account setup</dt><dd>{esc(row["auth"])}</dd><dt>Useful with</dt><dd>{esc(", ".join(role.replace("-", " ").title() for role in row["specialists"]))}</dd></dl>',
                  f'<div class="actions"><button type="button" class="copy-prompt" data-id="{identifier}" aria-label="Copy {esc(row["name"])} setup message">Copy setup for Muse</button><a href="{esc(guide_url)}">Open connector guide</a></div>',
                  f'<label class="prompt-label" for="prompt-{identifier}">Task and setup prompt</label><textarea readonly class="prompt" id="prompt-{identifier}" rows="5">{esc(row["setup_prompt"])}</textarea>',
                  '</div></details>']
    parts += ['</div><p id="no-results" class="empty" hidden>No matching connectors. Try a different service or clear the filters.</p></section></main>',
              '<footer><p><a href="README.md">Connector setup</a> · <a href="RUN_CONNECTORS.md">Request helper</a> · <a href="../../README.md">Muse Hub</a></p></footer>', '</body></html>', '']
    return '\n'.join(parts).encode('utf-8')

def render() -> dict[str, bytes]:
    doc = read_catalog()
    rows = doc["connectors"]
    count_by_cat = Counter(x["category"] for x in rows)
    catalog = [
        f"# Browse {len(rows)} Custom Connectors",
        "",
        "Find the services you want to use with Muse. Choose a use case, then open a connector's setup guide.",
        "",
        "## Browse by use case",
        "",
    ]
    homepage = [
        "# Muse Hub connector directory",
        "",
        "Find the services you want to use with Muse. Open a setup guide, choose your account and permissions, and try the connection with a small task.",
        "",
        "## Connect a service",
        "",
        f"**{len(rows)} connectors across {len(count_by_cat)} categories.**",
        "",
        "Find setup instructions for calendars, code hosting, design platforms, home devices and business services.",
        "",
        "## Browse by category",
        "",
    ]
    for title, intro, categories in GROUPS:
        count = sum(count_by_cat[c] for c in categories)
        url = "CATALOG.md#" + slug(title)
        entry = f"- **[{title}]({url})** — {intro} ({count})"
        homepage.append(entry)
        catalog.append(entry)
    homepage.extend([
        "",
        "## Common services",
        "",
    ])
    highlights = (
        "google-drive", "gmail", "trello", "github", "notion", "slack", "salesforce",
        "zendesk", "postgres", "canva", "home-assistant", "shopify",
    )
    by_id = {x["id"]: x for x in rows}
    for ident in highlights:
        row = by_id[ident]
        homepage.append(f"- **[{visible(row['name'])}]({row.get('guide_path',row['source_url'])})** — {safe_short(row['description'], 90)}")
    homepage.extend([
        "",
        "## Set up a connector",
        "",
        "1. Open the connector you want from the categories above.",
        "2. Review its service capabilities and access requirements in the linked guide.",
        "3. Follow the custom-connector setup steps in Muse, and choose the operations you want to use.",
        "",
        "For an interactive search experience, download the connector directory package and open its",
        "`index.html` file with the included CSS and JavaScript. The GitHub categories work without downloads.",
        "",
        "## Use connector actions in a workflow",
        "",
        "Each new service guide includes action inputs, account setup, event options and a practical starting prompt. Select an action, resolve the required IDs, and pass the result to your specialist or next workflow.",
        "",
        "[Prepare a request with the connector helper](RUN_CONNECTORS.md) · [Browse all services](CATALOG.md)",
        "",
        "[Back to Muse Hub](../../README.md) · [All connector categories](CATALOG.md)",
        "",
    ])
    catalog.extend(["", "---", ""])
    shown = []
    for title, intro, categories in GROUPS:
        catalog.extend([f"## {title}", "", intro, ""])
        for category in categories:
            matching = sorted((x for x in rows if x["category"] == category), key=lambda x: x["name"].casefold())
            catalog.extend([f"### {category} ({len(matching)})", ""])
            for row in matching:
                catalog.append(
                    f"- **[{visible(row['name'])}]({row.get('guide_path',row['source_url'])})** — "
                    f"{safe_short(row['description'])}"
                )
                shown.append(row["id"])
            catalog.append("")
        catalog.extend(["[Back to all categories](#browse-by-use-case)", "", "---", ""])
    if sorted(shown) != sorted(x["id"] for x in rows) or len(shown) != len(rows):
        raise ValueError("CONNECTOR_NAVIGATION_COVERAGE_FAILED")
    catalog.extend([
        "The [downloadable searchable directory](README.md) provides filters and copy-ready setup prompts.",
        "",
    ])
    return {
        "README.md": ("\n".join(homepage)).encode("utf8"),
        "CATALOG.md": ("\n".join(catalog)).encode("utf8"),
        "index.html": render_html(rows),
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    option = parser.add_mutually_exclusive_group(required=True)
    option.add_argument("--check", action="store_true")
    option.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    try:
        output = render()
        for filename, content in output.items():
            path = DIRECTORY / filename
            if args.check:
                if not path.is_file() or path.read_bytes() != content:
                    raise ValueError("GITHUB_DIRECTORY_OUT_OF_DATE:" + filename)
            else:
                path.write_bytes(content)
        print(json.dumps({"status": "GITHUB_CONNECTOR_DIRECTORY_VERIFIED" if args.check else "GITHUB_CONNECTOR_DIRECTORY_RENDERED",
                          "connectors": len(read_catalog()['connectors']), "groups": len(GROUPS), "files": sorted(output)}))
        return 0
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "REFUSED", "reason": str(error)[:160]}))
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
