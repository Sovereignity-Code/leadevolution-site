#!/usr/bin/env python3
"""
Inject Organization + WebSite schema + OG tags + canonical URLs
into every existing HTML page (excluding /locations/ which already have them).

Also injects FAQSchema into faq.html.
Also injects Service/LocalBusiness schema into each vertical page.
Also adds meta descriptions to privacy.html and terms.html.
"""
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leadevolution.com.au"

# ---------- Pages ----------
BASE_PAGES = {
    "index.html": "/",
    "faq.html": "/faq.html",
    "team.html": "/team.html",
    "contact.html": "/contact.html",
    "privacy.html": "/privacy.html",
    "terms.html": "/terms.html",
}

VERTICAL_PAGES = {
    "verticals/mortgage-broker-leads.html": "/verticals/mortgage-broker-leads.html",
    "verticals/financial-planning-leads.html": "/verticals/financial-planning-leads.html",
    "verticals/solar-leads.html": "/verticals/solar-leads.html",
    "verticals/insurance-leads.html": "/verticals/insurance-leads.html",
    "verticals/energy-leads.html": "/verticals/energy-leads.html",
    "verticals/commercial-finance-leads.html": "/verticals/commercial-finance-leads.html",
}

# ---------- Load schemas ----------
org_schema = json.loads((ROOT / "scripts" / "org_schema.json").read_text())
website_schema = json.loads((ROOT / "scripts" / "website_schema.json").read_text())
faq_schema = json.loads((ROOT / "scripts" / "faq_schema.json").read_text())

# ---------- Vertical service schemas ----------
VERTICAL_META = {
    "verticals/mortgage-broker-leads.html": {
        "label": "Mortgage Broker Leads",
        "professional": "mortgage broker",
        "desc": "Exclusive, consent-based mortgage broker leads across Australia. 24-hour delivery. DNCR compliant.",
    },
    "verticals/financial-planning-leads.html": {
        "label": "Financial Planning Leads",
        "professional": "financial adviser",
        "desc": "Exclusive financial planning and SMSF leads for Australian advisers. Consent-based, DNCR compliant.",
    },
    "verticals/solar-leads.html": {
        "label": "Solar Leads",
        "professional": "solar installer",
        "desc": "Exclusive homeowner solar and battery storage leads across Australia. 48-hour delivery.",
    },
    "verticals/insurance-leads.html": {
        "label": "Insurance Broker Leads",
        "professional": "insurance broker",
        "desc": "Exclusive life insurance and income protection leads for Australian brokers.",
    },
    "verticals/energy-leads.html": {
        "label": "Energy Broker Leads",
        "professional": "energy broker",
        "desc": "Exclusive electricity and gas switching leads for Australian brokers. Residential and SME.",
    },
    "verticals/commercial-finance-leads.html": {
        "label": "Commercial Finance Leads",
        "professional": "commercial finance broker",
        "desc": "Exclusive business loan and asset finance leads for Australian brokers.",
    },
}


# ---------- Helpers ----------
def get_title(html):
    m = re.search(r"<title>([^<]+)</title>", html)
    return m.group(1).strip() if m else "LeadEvolution"


def get_desc(html):
    m = re.search(r'<meta name="description" content="([^"]+)"', html)
    return m.group(1).strip() if m else ""


def has_tag(html, tag_marker):
    return tag_marker in html


def build_head_injection(url_path, title, desc, extra_schema=None):
    canonical = f"{SITE}{url_path}"
    schemas = [org_schema, website_schema]
    if extra_schema:
        schemas.append(extra_schema)
    schema_blocks = "\n".join([
        f'<script type="application/ld+json">{json.dumps(s, indent=2)}</script>'
        for s in schemas
    ])
    og_block = f'''<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="LeadEvolution">
<meta property="og:locale" content="en_AU">
<meta property="og:image" content="{SITE}/images/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
{schema_blocks}
'''
    return og_block


def inject_before_close_head(html_content, block):
    """Insert block before </head>. Idempotent — skip if already present."""
    if "og:site_name" in html_content:
        return html_content, False
    return html_content.replace("</head>", block + "</head>"), True


# ---------- 1. Ensure privacy.html and terms.html have meta descriptions ----------
def ensure_meta_desc(rel_path, fallback_desc):
    path = ROOT / rel_path
    content = path.read_text(encoding="utf-8")
    if 'meta name="description"' in content:
        return content, False
    # Insert after <title>
    new = re.sub(
        r"(</title>)",
        r'\1\n<meta name="description" content="' + fallback_desc + '">',
        content,
        count=1,
    )
    path.write_text(new, encoding="utf-8")
    return new, True


ensure_meta_desc(
    "privacy.html",
    "LeadEvolution Privacy Policy — how we collect, store and share Australian consumer and business lead data under the Privacy Act 1988 and ACMA Do Not Call Register rules.",
)
ensure_meta_desc(
    "terms.html",
    "LeadEvolution Terms and Conditions — service agreement covering pay per lead delivery, replacement guarantee, data handling and Australian consumer law compliance.",
)


# ---------- 2. Inject into all base pages ----------
for rel_path, url_path in BASE_PAGES.items():
    path = ROOT / rel_path
    html = path.read_text(encoding="utf-8")
    title = get_title(html)
    desc = get_desc(html) or "LeadEvolution — Australia's specialist pay per lead agency."

    extra = None
    if rel_path == "faq.html":
        extra = faq_schema

    block = build_head_injection(url_path, title, desc, extra_schema=extra)
    new, changed = inject_before_close_head(html, block)
    if changed:
        path.write_text(new, encoding="utf-8")
        print(f"[✓] injected: {rel_path}")
    else:
        print(f"[skip] already has OG tags: {rel_path}")

# ---------- 3. Inject into vertical pages with Service schema ----------
for rel_path, url_path in VERTICAL_PAGES.items():
    path = ROOT / rel_path
    html = path.read_text(encoding="utf-8")
    title = get_title(html)
    desc = get_desc(html) or "LeadEvolution — Australia's specialist pay per lead agency."
    vmeta = VERTICAL_META[rel_path]
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": vmeta["label"],
        "name": vmeta["label"] + " Australia",
        "description": vmeta["desc"],
        "provider": {
            "@type": "Organization",
            "name": "LeadEvolution",
            "url": SITE,
            "email": "info@leadevolution.com.au",
        },
        "areaServed": {
            "@type": "Country",
            "name": "Australia",
        },
        "url": f"{SITE}{url_path}",
    }
    block = build_head_injection(url_path, title, desc, extra_schema=service_schema)
    new, changed = inject_before_close_head(html, block)
    if changed:
        path.write_text(new, encoding="utf-8")
        print(f"[✓] injected: {rel_path}")
    else:
        print(f"[skip] already has OG tags: {rel_path}")

print("\nDone injecting SEO tags across base + vertical pages.")
