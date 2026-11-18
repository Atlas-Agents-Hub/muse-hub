"""Compose the opt-in loopback Notebook using the original five-room source UI.

No server or storage authority lives here. Static preview files keep their
network-disabled CSP; only the explicitly served local view receives this panel.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- ROOM_NOTEBOOK_START -->"
END = "<!-- ROOM_NOTEBOOK_END -->"


def _asset(path: Path) -> bytes:
    if (any(p.is_symlink() or (hasattr(p, "is_junction") and p.is_junction())
            for p in (path, *path.parents)) or not path.is_file()
            or path.stat().st_size > 131072):
        raise ValueError("UI_ASSET_INVALID")
    return path.read_bytes()


def companion_pages() -> dict:
    home = ROOT / "examples/companion_home"
    assets = Path(__file__).parent / "companion_assets"
    page = _asset(home / "index.html").decode("utf-8")
    if page.count(START) != 1 or page.count(END) != 1:
        raise ValueError("COMPANION_TEMPLATE_MARKERS")
    before, rest = page.split(START)
    _, after = rest.split(END)
    page = before + _asset(assets / "notebook.html").decode("utf-8") + after
    page = page.replace("connect-src 'none'", "connect-src 'self'")
    page = page.replace("</head>", '<link rel="stylesheet" href="notebook.css">\n<script defer src="notebook.js"></script>\n</head>')
    pages = {"/": ("text/html; charset=utf-8", page.encode("utf-8"))}
    for name, folder, mime in (
        ("home.js", home, "text/javascript"), ("rooms.js", home, "text/javascript"),
        ("style.css", home, "text/css"), ("notebook.js", assets, "text/javascript"),
        ("notebook.css", assets, "text/css"),
    ):
        pages["/" + name] = (mime + "; charset=utf-8", _asset(folder / name))
    pages["/docs/COMPANION_HOME.md"] = ("text/plain; charset=utf-8", _asset(ROOT / "docs/COMPANION_HOME.md"))
    return pages
