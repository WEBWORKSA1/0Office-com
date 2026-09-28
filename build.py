#!/usr/bin/env python3
"""Build 0Office.com static site. Usage: python3 build.py
Outputs HTML into the repo root (GitHub Pages serves the root of the main branch).
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import layout
from layout import SITE_URL
import pages, tools_pages, guides

ROOT = os.path.dirname(os.path.abspath(__file__))
# Path prefix the site is served under (for the 404 page). "/" when on a custom domain.
BASE_PATH = "/" if SITE_URL.count("/") == 2 else "/" + SITE_URL.split("/", 3)[3].strip("/") + "/"


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def main():
    out = {}
    out["index.html"] = pages.home()
    out["get-started.html"] = pages.get_started()
    out["tools/index.html"] = tools_pages.tools_index()
    for t in tools_pages.TOOLS:
        out[f'tools/{t["slug"]}.html'] = tools_pages.tool_page(t)
    out["guides/index.html"] = guides.guides_index()
    for g in guides.GUIDES:
        out[f'guides/{g["slug"]}.html'] = guides.guide_page(g)
    for name in ["checklist", "stack", "videos", "hire", "contests", "support", "advertise", "careers", "about", "contact", "privacy", "terms", "disclaimer"]:
        out[f"{name}.html"] = getattr(pages, name)()
    out["404.html"] = pages.notfound(BASE_PATH)
    for p, html in out.items():
        write(p, html)

    write("assets/js/search-index.js", "window.O0_INDEX=" + json.dumps(layout.INDEX, ensure_ascii=False) + ";\n")
    urls = [p for p in out if p != "404.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        loc = f"{SITE_URL}/" + ("" if p == "index.html" else p.replace("/index.html", "/"))
        pri = "1.0" if p == "index.html" else "0.8" if p.startswith("tools/") or p == "get-started.html" else "0.6"
        sm.append(f"  <url><loc>{loc}</loc><lastmod>2026-09-28</lastmod><priority>{pri}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("manifest.webmanifest", json.dumps({
        "name": "0Office.com — Zero Office Tools", "short_name": "0Office", "start_url": "./index.html", "display": "standalone",
        "background_color": "#0b1b33", "theme_color": "#0d9488",
        "icons": [{"src": "assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))
    print(f"Built {len(out)} pages → {ROOT}")


if __name__ == "__main__":
    main()
