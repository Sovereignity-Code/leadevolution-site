#!/usr/bin/env python3
"""
Add 'Resources' nav link to all existing pages (nav + mobile nav + footer Company col).
Also update sitemap.xml to include resources.html.
"""
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leadevolution.com.au"

pages = list(ROOT.glob("*.html")) + list((ROOT / "verticals").glob("*.html"))
# Include /compare and /guides too so their footers link back
for sub in ("compare", "guides"):
    d = ROOT / sub
    if d.exists():
        pages.extend(d.glob("*.html"))


def add_link_to_nav(content, res_href, level="root"):
    """Inject Resources link into desktop nav between FAQ and Why Us."""
    marker = '<a href="' + ('' if level == 'root' else '../') + 'faq.html" class="nav-link">FAQ</a>'
    if marker not in content:
        # Try alt: no "root" versioning
        pass
    if 'class="nav-link">Resources' in content:
        return content, False
    resources_link = f'<a href="{res_href}" class="nav-link">Resources</a>\n      '
    # Insert BEFORE the FAQ nav link (Resources appears before FAQ)
    new = content.replace(marker, resources_link + marker, 1)
    if new == content:
        return content, False
    return new, True


def add_link_to_mobile(content, res_href, level="root"):
    """Inject Resources link into mobile nav between FAQ and Why Us."""
    marker = '<a href="' + ('' if level == 'root' else '../') + 'faq.html" class="mobile-link">FAQ</a>'
    if 'class="mobile-link">Resources' in content:
        return content, False
    resources_link = f'<a href="{res_href}" class="mobile-link">Resources</a>\n  '
    new = content.replace(marker, resources_link + marker, 1)
    if new == content:
        return content, False
    return new, True


def add_link_to_footer(content, res_href):
    """Insert Resources link at start of Company footer column."""
    if '"footer-col"><h4>Company</h4><a href="' + res_href + '"' in content:
        return content, False
    # Find the Company column and inject before first <a>
    def sub(m):
        return m.group(0).replace('<h4>Company</h4>', f'<h4>Company</h4><a href="{res_href}">Resources</a>')
    new = re.sub(r'<div class="footer-col"><h4>Company</h4><a', lambda m: m.group(0).replace('<h4>Company</h4><a', f'<h4>Company</h4><a href="{res_href}">Resources</a><a', 1), content, count=1)
    if new == content:
        return content, False
    return new, True


touched = 0
for path in pages:
    if path.name == "resources.html":
        continue
    # Determine level for relative paths
    rel = path.relative_to(ROOT)
    if len(rel.parts) == 1:
        res_href = "resources.html"
        level = "root"
    else:
        res_href = "../resources.html"
        level = "sub"

    content = path.read_text(encoding="utf-8")
    original = content
    content, ch1 = add_link_to_nav(content, res_href, level=level)
    content, ch2 = add_link_to_mobile(content, res_href, level=level)
    content, ch3 = add_link_to_footer(content, res_href)
    if content != original:
        path.write_text(content, encoding="utf-8")
        touched += 1

print(f"[✓] added Resources nav link to {touched} pages")

# Rebuild sitemap including resources.html
today = datetime.utcnow().strftime("%Y-%m-%d")
base_pages = [
    "/", "/faq.html", "/team.html", "/contact.html", "/resources.html", "/how-we-qualify.html",
    "/privacy.html", "/terms.html",
    "/verticals/mortgage-broker-leads.html",
    "/verticals/financial-planning-leads.html",
    "/verticals/solar-leads.html",
    "/verticals/insurance-leads.html",
    "/verticals/energy-leads.html",
    "/verticals/commercial-finance-leads.html",
]
extras = []
for sub in ("compare", "guides"):
    d = ROOT / sub
    if d.exists():
        for p in sorted(d.glob("*.html")):
            extras.append(f"/{sub}/{p.name}")

all_urls = base_pages + extras

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in all_urls:
    if url == "/":
        pri = "1.0"
    elif "/verticals/" in url:
        pri = "0.9"
    elif "/compare/" in url or "/guides/" in url:
        pri = "0.8"
    elif url == "/resources.html":
        pri = "0.8"
    else:
        pri = "0.6"
    lines.append(f"  <url>")
    lines.append(f"    <loc>{SITE}{url}</loc>")
    lines.append(f"    <lastmod>{today}</lastmod>")
    lines.append(f"    <changefreq>weekly</changefreq>")
    lines.append(f"    <priority>{pri}</priority>")
    lines.append(f"  </url>")
lines.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")
print(f"[✓] sitemap rebuilt with {len(all_urls)} URLs")
