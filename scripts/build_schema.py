#!/usr/bin/env python3
"""
Extract FAQ Q&A from faq.html and emit FAQSchema JSON-LD block.
Also emit the Organization + WebSite schema block for injection.
"""
import re
import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAQ = ROOT / "faq.html"

content = FAQ.read_text(encoding="utf-8")

# Match each FAQ item
pattern = re.compile(
    r'<div class="faq-q">([^<]+?)<span class="chevron">'
    r'.*?<div class="faq-a"><p>(.*?)</p></div>',
    re.DOTALL
)
matches = pattern.findall(content)

def clean(s):
    # Strip HTML tags from answer, unescape entities
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

faq_items = []
for q, a in matches:
    faq_items.append({
        "@type": "Question",
        "name": clean(q),
        "acceptedAnswer": {
            "@type": "Answer",
            "text": clean(a),
        }
    })

faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faq_items,
}

print(f"Extracted {len(faq_items)} FAQ items")

# Write out
(ROOT / "scripts" / "faq_schema.json").write_text(
    json.dumps(faq_schema, indent=2), encoding="utf-8"
)

# Organization + WebSite schema (sitewide)
org_schema = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "LeadEvolution",
    "url": "https://leadevolution.com.au",
    "logo": "https://leadevolution.com.au/images/logo.png",
    "email": "info@leadevolution.com.au",
    "description": "Australia's specialist pay per lead agency. Exclusive, consent-based leads across mortgage broking, financial planning, solar, insurance, energy, and commercial finance.",
    "legalName": "Artificial Innovations Pty Ltd",
    "taxID": "53 677 049 946",
    "areaServed": {
        "@type": "Country",
        "name": "Australia",
    },
    "sameAs": [],
}

website_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "LeadEvolution",
    "url": "https://leadevolution.com.au",
    "potentialAction": {
        "@type": "SearchAction",
        "target": "https://leadevolution.com.au/contact.html",
        "query-input": "required name=search_term_string",
    },
}

(ROOT / "scripts" / "org_schema.json").write_text(
    json.dumps(org_schema, indent=2), encoding="utf-8"
)
(ROOT / "scripts" / "website_schema.json").write_text(
    json.dumps(website_schema, indent=2), encoding="utf-8"
)

print("Wrote faq_schema.json, org_schema.json, website_schema.json")
