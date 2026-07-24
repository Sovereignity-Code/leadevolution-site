#!/usr/bin/env python3
"""
Update contact.html links on vertical + location pages to include
?industry=<value> query param, so the industry dropdown on the form
pre-populates when a user arrives from a vertical/location page.

Only touches btn-primary + btn-outline + info-box + final-cta links.
Leaves nav + footer contact links clean.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# vertical slug → industry option value (must match <option value="X">)
INDUSTRY_MAP = {
    "mortgage-broker-leads": "Mortgage Broking",
    "financial-planning-leads": "Financial Planning",
    "solar-leads": "Solar Installation",
    "insurance-leads": "Insurance Broking",
    "energy-leads": "Energy Broking",
    "commercial-finance-leads": "Commercial Finance",
}


def encode_industry(v):
    return v.replace(" ", "+")


def update_file(path, industry_value):
    """Replace contact.html links inside CTA blocks with param version."""
    content = path.read_text(encoding="utf-8")
    param = encode_industry(industry_value)

    # Pattern: any link to contact.html that carries btn-primary or btn-outline class
    # or is inside an info-box (identified by "Get ... Leads" or "Get Leads in" text pattern)
    # Simplest robust approach: replace href="contact.html" or href="../contact.html"
    # ONLY when the anchor has class="btn ..." — nav and footer use "nav-link" / "mobile-link" / "vert-cta" / plain <a>

    # We want: any href="contact.html" or "../contact.html" where the <a> tag has btn-primary or btn-outline
    def repl(match):
        full_tag = match.group(0)
        href = match.group(1)
        # Skip if already has query string
        if "?" in href:
            return full_tag
        new_href = href.replace('contact.html', f'contact.html?industry={param}')
        return full_tag.replace(f'href="{href}"', f'href="{new_href}"')

    # Match <a ... class="btn btn-primary ..." ... href="...contact.html"> or href-first version
    # Two directions: class before href, or href before class
    patterns = [
        r'<a[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*href="((?:\.\./)?contact\.html)"[^>]*>',
        r'<a[^>]*href="((?:\.\./)?contact\.html)"[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*>',
    ]
    changed = False
    for pat in patterns:
        new_content = re.sub(pat, repl, content)
        if new_content != content:
            changed = True
            content = new_content

    if changed:
        path.write_text(content, encoding="utf-8")
    return changed


# ---------- 1. Vertical pages ----------
for slug, industry in INDUSTRY_MAP.items():
    path = ROOT / "verticals" / f"{slug}.html"
    if path.exists():
        did = update_file(path, industry)
        print(f"{'[✓]' if did else '[·]'} {path.relative_to(ROOT)}")

# ---------- 2. Location pages ----------
loc_dir = ROOT / "locations"
count = 0
for path in sorted(loc_dir.glob("*.html")):
    # Slug format: <vertical-slug>-<suburb>-<state>.html
    for slug, industry in INDUSTRY_MAP.items():
        if path.name.startswith(slug + "-"):
            did = update_file(path, industry)
            if did:
                count += 1
            break
print(f"[✓] updated {count} location pages")
