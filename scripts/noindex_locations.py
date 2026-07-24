#!/usr/bin/env python3
"""
Add <meta name="robots" content="noindex, follow"> to every /locations/ page.
Also regenerate sitemap.xml to exclude the 120 location pages.
"""
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leadevolution.com.au"

# ---------- Add noindex to location pages ----------
loc_dir = ROOT / "locations"
noindex_tag = '<meta name="robots" content="noindex, follow">'
touched = 0
for path in loc_dir.glob("*.html"):
    content = path.read_text(encoding="utf-8")
    if noindex_tag in content:
        continue
    # Insert after <meta charset ...>
    new = re.sub(
        r'(<meta charset="UTF-8">)',
        r'\1' + noindex_tag,
        content,
        count=1,
    )
    if new != content:
        path.write_text(new, encoding="utf-8")
        touched += 1

print(f"[✓] added noindex to {touched} location pages")

# ---------- Rebuild sitemap.xml without location pages ----------
today = datetime.utcnow().strftime("%Y-%m-%d")

base_pages = [
    "/", "/faq.html", "/team.html", "/contact.html",
    "/privacy.html", "/terms.html",
    "/verticals/mortgage-broker-leads.html",
    "/verticals/financial-planning-leads.html",
    "/verticals/solar-leads.html",
    "/verticals/insurance-leads.html",
    "/verticals/energy-leads.html",
    "/verticals/commercial-finance-leads.html",
]

# Discover any comparison / guide pages that exist already
extras = []
for sub in ("compare", "guides"):
    sub_dir = ROOT / sub
    if sub_dir.exists():
        for p in sorted(sub_dir.glob("*.html")):
            extras.append(f"/{sub}/{p.name}")

all_urls = base_pages + extras

urlset = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in all_urls:
    if url == "/":
        pri = "1.0"
    elif "/verticals/" in url:
        pri = "0.9"
    elif "/compare/" in url or "/guides/" in url:
        pri = "0.8"
    else:
        pri = "0.6"
    urlset.append(f"  <url>")
    urlset.append(f"    <loc>{SITE}{url}</loc>")
    urlset.append(f"    <lastmod>{today}</lastmod>")
    urlset.append(f"    <changefreq>weekly</changefreq>")
    urlset.append(f"    <priority>{pri}</priority>")
    urlset.append(f"  </url>")
urlset.append("</urlset>")

(ROOT / "sitemap.xml").write_text("\n".join(urlset), encoding="utf-8")
print(f"[✓] sitemap.xml rebuilt with {len(all_urls)} URLs (location pages excluded)")
