# Muse Hub website

[Open Muse Hub](https://atlas-origins.github.io/muse-ai-agent-presets/) · [Download kits](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html)

The website brings together 15 specialists, 75 skills, 25 workflows, and a directory of 63 tools and projects.

## Pages

- [Home and specialists](index.html)
- [Downloads](downloads.html)
- [Tools and projects](public/index.html)

## Preview locally

From the repository root, run `python -m http.server 8000 --directory hub/site` and open `http://localhost:8000`.

The site uses plain HTML, CSS and JavaScript. Search, filtering, setup links, keyboard navigation and download links work without a build service. All packages are hosted in the GitHub release.

## Update

Use `python scripts/render_downloads.py` after changing the collection. Refresh `INTEGRITY.json` and the public manifest after reviewing the rendered pages. The Pages workflow deploys this directory from the reviewed main branch.
