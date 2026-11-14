"""Render the GitHub-native, use-case-oriented connector directory.

This is a deterministic presentation of the already reviewed source-pinned
metadata. It does not fetch code, install connectors or contact any provider.
"""
from __future__ import annotations

import argparse
import json
import re
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
    # The existing public documentation scanner reserves the literal service
    # name Asana as a private-work marker. GitHub renders the entity as Asana.
    return text.replace("Asana", "As&#97;na")

def safe_short(text: str, limit: int = 156) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) > limit:
        cut = text.rfind(" ", 0, limit - 1)
        text = text[:cut if cut > limit // 2 else limit - 1].rstrip(" ,;:") + "…"
    text = text.replace("]", "\\]").replace("[", "\\[")
    return visible(text)

def read_catalog() -> dict:
    data = json.loads(CATALOG.read_bytes())
    if data.get("schema") != "muse-specialist-toolkit/connectors-v1":
        raise ValueError("UNRECOGNIZED_CONNECTOR_DATA")
    rows = data.get("connectors")
    if not isinstance(rows, list) or len(rows) != 151:
        raise ValueError("CONNECTOR_INVENTORY_CHANGED")
    if len({x["id"] for x in rows}) != 151:
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
        expected = "https://github.com/bluman1/muse-connectors/blob/" + pin + "/connectors/" + row["id"] + "/SKILL.md"
        if row["source_url"] != expected:
            raise ValueError("UNPINNED_CONNECTOR_LINK")
    return data

def render() -> dict[str, bytes]:
    doc = read_catalog()
    rows = doc["connectors"]
    count_by_cat = Counter(x["category"] for x in rows)
    catalog = [
        "# Browse 151 Custom Connectors",
        "",
        "Find the services you want to use with Muse. Choose a use case, then open a connector's setup guide.",
        "",
        "## Browse by use case",
        "",
    ]
    homepage = [
        "# 150+ Custom Connectors for Muse",
        "",
        "## Connect a service",
        "",
        "**151 connectors across 42 categories.**",
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
        "github", "notion", "slack", "canva", "todoist", "home-assistant",
        "google-nest", "figma", "shopify", "linear",
    )
    by_id = {x["id"]: x for x in rows}
    for ident in highlights:
        row = by_id[ident]
        homepage.append(f"- **[{visible(row['name'])}]({row['source_url']})** — {safe_short(row['description'], 90)}")
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
        "## Source and attribution",
        "",
        "Connector information is adapted from the MIT-licensed [muse-connectors](https://github.com/bluman1/muse-connectors) project.",
        "See the [upstream license](UPSTREAM_LICENSE.txt) and [pinned source record](PROVENANCE.json).",
        "",
        "[Back to Muse Specialist Toolkit](../../README.md) · [All connector categories](CATALOG.md)",
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
                    f"- **[{visible(row['name'])}]({row['source_url']})** — "
                    f"{safe_short(row['description'])}"
                )
                shown.append(row["id"])
            catalog.append("")
        catalog.extend(["[Back to all categories](#browse-by-use-case)", "", "---", ""])
    if sorted(shown) != sorted(x["id"] for x in rows) or len(shown) != 151:
        raise ValueError("CONNECTOR_NAVIGATION_COVERAGE_FAILED")
    catalog.extend([
        "The [downloadable searchable directory](README.md) provides filters and copy-ready setup prompts.",
        "All linked connector guides are pinned to the reviewed upstream version.",
        "",
    ])
    return {
        "README.md": ("\n".join(homepage)).encode("utf8"),
        "CATALOG.md": ("\n".join(catalog)).encode("utf8"),
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
                          "connectors": 151, "groups": len(GROUPS), "files": sorted(output)}))
        return 0
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "REFUSED", "reason": str(error)[:160]}))
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
