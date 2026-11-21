# Muse Hub website

[Open Muse Hub](https://atlas-agents-hub.github.io/muse-hub/) · [Download kits](https://atlas-agents-hub.github.io/muse-hub/downloads.html)

The website brings together Muse feature guides, 15 specialists, 5242 skills, 396 workflows, full-stack Space templates, setup guides, and official Meta documentation. Three guided journeys connect the right tools to everyday planning, engineering, and creative work.

## Pages

- [Explore Muse Hub](index.html)
- [Downloads](downloads.html)
- [Setup guides](public/index.html)

## Preview locally

From the repository root, run `python -m http.server 8000 --directory hub/site` and open `http://localhost:8000`.

The site uses plain HTML, CSS and JavaScript. Search, filtering, setup links, keyboard navigation and download links work without a build service. All packages are hosted in the GitHub release.

## Update

Use `python scripts/render_downloads.py` after changing the collection. Refresh `INTEGRITY.json` and the public manifest after reviewing the rendered pages. The Pages workflow deploys this directory from the reviewed main branch.

The resource directory accepts `?route=cli`, `desktop`, `watch`, `family`, `doors`, or `companion`. Selecting or clearing a route updates the shareable URL; browser Back and Forward restore the selection.
