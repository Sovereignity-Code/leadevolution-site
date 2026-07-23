#!/usr/bin/env python3
"""
Build script for LeadEvolution SEO expansion.
- Generates 120 postcode x vertical pages under /locations/
- Writes sitemap.xml with all URLs
- Emits Organization + FAQSchema + LocalBusiness JSON-LD snippets
"""
import os
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leadevolution.com.au"

# ---------- SUBURB / VERTICAL DATA ----------

SUBURBS = [
    # Sydney (NSW)
    {"suburb": "Parramatta", "state": "NSW", "state_full": "New South Wales", "postcode": "2150", "metro": "Sydney", "lat": -33.8151, "lng": 151.0011},
    {"suburb": "Chatswood", "state": "NSW", "state_full": "New South Wales", "postcode": "2067", "metro": "Sydney", "lat": -33.7969, "lng": 151.1836},
    {"suburb": "Bondi Junction", "state": "NSW", "state_full": "New South Wales", "postcode": "2022", "metro": "Sydney", "lat": -33.8918, "lng": 151.2469},
    {"suburb": "North Sydney", "state": "NSW", "state_full": "New South Wales", "postcode": "2060", "metro": "Sydney", "lat": -33.8397, "lng": 151.2072},
    {"suburb": "Liverpool", "state": "NSW", "state_full": "New South Wales", "postcode": "2170", "metro": "Sydney", "lat": -33.9250, "lng": 150.9236},
    # Melbourne (VIC)
    {"suburb": "Southbank", "state": "VIC", "state_full": "Victoria", "postcode": "3006", "metro": "Melbourne", "lat": -37.8226, "lng": 144.9648},
    {"suburb": "Richmond", "state": "VIC", "state_full": "Victoria", "postcode": "3121", "metro": "Melbourne", "lat": -37.8232, "lng": 144.9986},
    {"suburb": "Box Hill", "state": "VIC", "state_full": "Victoria", "postcode": "3128", "metro": "Melbourne", "lat": -37.8194, "lng": 145.1236},
    {"suburb": "Docklands", "state": "VIC", "state_full": "Victoria", "postcode": "3008", "metro": "Melbourne", "lat": -37.8156, "lng": 144.9464},
    {"suburb": "Cheltenham", "state": "VIC", "state_full": "Victoria", "postcode": "3192", "metro": "Melbourne", "lat": -37.9689, "lng": 145.0553},
    # Brisbane (QLD)
    {"suburb": "South Brisbane", "state": "QLD", "state_full": "Queensland", "postcode": "4101", "metro": "Brisbane", "lat": -27.4808, "lng": 153.0181},
    {"suburb": "Fortitude Valley", "state": "QLD", "state_full": "Queensland", "postcode": "4006", "metro": "Brisbane", "lat": -27.4569, "lng": 153.0344},
    {"suburb": "Chermside", "state": "QLD", "state_full": "Queensland", "postcode": "4032", "metro": "Brisbane", "lat": -27.3861, "lng": 153.0331},
    # Gold Coast (QLD)
    {"suburb": "Southport", "state": "QLD", "state_full": "Queensland", "postcode": "4215", "metro": "Gold Coast", "lat": -27.9714, "lng": 153.4136},
    {"suburb": "Surfers Paradise", "state": "QLD", "state_full": "Queensland", "postcode": "4217", "metro": "Gold Coast", "lat": -28.0028, "lng": 153.4306},
    # Perth (WA)
    {"suburb": "Perth CBD", "state": "WA", "state_full": "Western Australia", "postcode": "6000", "metro": "Perth", "lat": -31.9506, "lng": 115.8608},
    {"suburb": "Subiaco", "state": "WA", "state_full": "Western Australia", "postcode": "6008", "metro": "Perth", "lat": -31.9483, "lng": 115.8264},
    # Adelaide (SA)
    {"suburb": "Adelaide CBD", "state": "SA", "state_full": "South Australia", "postcode": "5000", "metro": "Adelaide", "lat": -34.9285, "lng": 138.6007},
    {"suburb": "Norwood", "state": "SA", "state_full": "South Australia", "postcode": "5067", "metro": "Adelaide", "lat": -34.9192, "lng": 138.6317},
    # Canberra (ACT)
    {"suburb": "Canberra CBD", "state": "ACT", "state_full": "Australian Capital Territory", "postcode": "2601", "metro": "Canberra", "lat": -35.2809, "lng": 149.1300},
]

VERTICALS = [
    {
        "slug": "mortgage-broker-leads",
        "label": "Mortgage Broker Leads",
        "short": "Mortgage Leads",
        "professional": "mortgage broker",
        "emoji": "🏠",
        "hero": "Exclusive, consent-based mortgage broker leads. Prospects actively looking to purchase, refinance, or invest.",
        "market_line": "The Australian mortgage market processes over 160,000 new home loans annually. Mortgage brokers now write over 70% of all new residential loans — competition for quality leads has never been higher.",
        "targets": ["First Home Buyers", "Refinancers", "Property Investors", "Upgraders", "Self-Employed Borrowers", "Construction Loans", "SMSF Property", "Downsizers"],
        "commission_note": "A broker closing 20% of quality leads at an average commission of $2,400 per loan generates $9,600 from a single batch — before ongoing trail commissions.",
        "delivery_hours": "24 hours",
        "avg_value": "$2,400+ commission per settlement",
    },
    {
        "slug": "financial-planning-leads",
        "label": "Financial Planning Leads",
        "short": "Financial Planning Leads",
        "professional": "financial adviser",
        "emoji": "📊",
        "hero": "Exclusive financial planning leads for Australian advisers. Superannuation, SMSF, wealth management, retirement planning.",
        "market_line": "With over $3.9 trillion in the Australian superannuation system and advice numbers at historic lows, qualified advisers face record demand — but leads with real intent are scarce.",
        "targets": ["Superannuation Consolidation", "SMSF Setup", "Retirement Planning", "Wealth Accumulation", "Redundancy & Rollover", "Investment Strategy", "Insurance Structuring", "Estate Planning"],
        "commission_note": "Advisers routinely convert quality leads into ongoing fee relationships worth $3,000–$8,000/year — a single closed lead can pay back the entire month's lead cost.",
        "delivery_hours": "48 hours",
        "avg_value": "$3,000–$8,000 ongoing fee per client",
    },
    {
        "slug": "solar-leads",
        "label": "Solar Leads",
        "short": "Solar Leads",
        "professional": "solar installer",
        "emoji": "☀️",
        "hero": "Exclusive homeowner solar leads. Prospects actively researching rooftop solar and battery storage, ready for a quote.",
        "market_line": "Over 3.6 million Australian rooftops now carry solar — but the market is still expanding as battery storage costs fall and grid feed-in tariffs shrink. Homeowners are actively researching installers.",
        "targets": ["Residential Rooftop Solar", "Battery Storage Add-Ons", "Solar + Battery Bundle Enquiries", "EV Charger Integration", "System Upgrades", "Off-Grid Enquiries"],
        "commission_note": "A single solar installation averages $8,000–$15,000. Installer margins on qualified, exclusive leads make cost-per-lead a near-negligible acquisition cost against the deal size.",
        "delivery_hours": "48 hours",
        "avg_value": "$8,000–$15,000 job size",
    },
    {
        "slug": "insurance-leads",
        "label": "Insurance Broker Leads",
        "short": "Insurance Leads",
        "professional": "insurance broker",
        "emoji": "🛡️",
        "hero": "Exclusive life insurance and income protection leads. Prospects who've confirmed they want to review their cover.",
        "market_line": "Australia's life insurance under-insurance gap is over $1 trillion. Prospects want cover — but most brokers waste hours cold-calling old data lists rather than working real intent.",
        "targets": ["Life Insurance", "Income Protection", "Trauma Cover", "TPD Cover", "Business Expense Insurance", "Key Person Cover"],
        "commission_note": "Life insurance upfront commissions range from $800–$3,500 per policy plus ongoing trail — one quality lead can pay for a month of pipeline supply.",
        "delivery_hours": "48 hours",
        "avg_value": "$800–$3,500 upfront + trail",
    },
    {
        "slug": "energy-leads",
        "label": "Energy Broker Leads",
        "short": "Energy Leads",
        "professional": "energy broker",
        "emoji": "⚡",
        "hero": "Exclusive electricity and gas switching leads. Residential and SME prospects actively looking to reduce their bills.",
        "market_line": "Australian energy prices continue to rise across the NEM. Residential and SME customers are actively looking to switch retailers — but only if a broker or comparison specialist makes it simple.",
        "targets": ["Residential Electricity Switch", "Residential Gas Switch", "SME Bill Reduction", "Bundled Energy Plans", "Green Energy Plans", "Multi-Site Business Switch"],
        "commission_note": "Broker commissions on retail energy switches vary but stack quickly across a book of clients — the model rewards consistent volume and low CAC.",
        "delivery_hours": "48 hours",
        "avg_value": "Stackable retail commission per switch",
    },
    {
        "slug": "commercial-finance-leads",
        "label": "Commercial Finance Leads",
        "short": "Commercial Finance Leads",
        "professional": "commercial finance broker",
        "emoji": "🏢",
        "hero": "Exclusive business loan and asset finance leads. Business owners with a real capital need and a project in front of them.",
        "market_line": "Australian SMEs represent 97% of all businesses and account for over $500 billion in outstanding business credit. Commercial brokers with a steady flow of qualified enquiries own the market.",
        "targets": ["Equipment Finance", "Working Capital Loans", "Commercial Property", "Trade Finance", "Invoice Financing", "Business Overdrafts", "Franchise Finance", "Vehicle Fleet Finance"],
        "commission_note": "Commercial deals routinely settle in the $250k–$2M range. A single settled lead can generate $2,500–$20,000+ in upfront commission plus trail.",
        "delivery_hours": "72 hours",
        "avg_value": "$2,500–$20,000+ upfront per settlement",
    },
]

# ---------- HELPERS ----------

def slugify_suburb(s):
    return s.lower().replace(" ", "-")


def state_compliance_note(state):
    notes = {
        "NSW": "All NSW leads are sourced under Privacy Act 1988 obligations and adhere to the Australian Communications and Media Authority (ACMA) Do Not Call Register rules. NSW-specific consumer protections under Fair Trading NSW are respected across all data collection touchpoints.",
        "VIC": "Victorian leads adhere to the Privacy Act 1988, ACMA Do Not Call Register rules, and Consumer Affairs Victoria fair trading requirements. Consent is captured explicitly and time-stamped for every lead delivered.",
        "QLD": "Queensland leads follow the Privacy Act 1988, ACMA Do Not Call Register rules, and Office of Fair Trading Queensland standards. Every lead includes documented consent trail.",
        "WA": "Western Australian leads comply with the Privacy Act 1988 and ACMA Do Not Call Register requirements. Consumer Protection WA fair trading rules are applied to all consent capture processes.",
        "SA": "South Australian leads adhere to the Privacy Act 1988, ACMA Do Not Call Register rules, and Consumer and Business Services SA fair trading standards. Consent is captured, timestamped, and auditable.",
        "ACT": "ACT leads follow the Privacy Act 1988 and ACMA Do Not Call Register rules alongside Access Canberra consumer protection standards. Consent trails are documented per lead.",
        "TAS": "Tasmanian leads adhere to the Privacy Act 1988, ACMA Do Not Call Register rules, and Consumer Affairs & Fair Trading Tasmania standards.",
        "NT": "Northern Territory leads follow the Privacy Act 1988 and ACMA Do Not Call Register rules alongside NT Consumer Affairs fair trading standards.",
    }
    return notes.get(state, notes["NSW"])


def metro_context_line(suburb, metro, vertical_slug):
    if vertical_slug == "solar-leads":
        base = f"{suburb} sits inside the greater {metro} market, one of Australia's higher-density residential rooftop opportunities. Homeowners in the postcode routinely investigate solar as electricity retail prices climb and battery storage becomes viable."
    elif vertical_slug in ("mortgage-broker-leads", "financial-planning-leads", "commercial-finance-leads", "insurance-leads"):
        base = f"{suburb} is a recognised financial services corridor of the greater {metro} market. Local demand for advice, brokerage and structured finance runs consistently high — provided brokers can access buyers with real intent, not tyre-kickers."
    else:
        base = f"{suburb} is part of the greater {metro} market where residents and SMEs actively review energy retailer contracts as prices continue to shift across the NEM."
    return base


def related_suburbs(current_suburb, all_suburbs, metro, count=3):
    same_metro = [s for s in all_suburbs if s["metro"] == metro and s["suburb"] != current_suburb]
    other = [s for s in all_suburbs if s["metro"] != metro and s["suburb"] != current_suburb]
    picks = (same_metro + other)[:count]
    return picks


# ---------- PAGE TEMPLATE ----------

def location_page_html(vertical, suburb):
    slug = f"{vertical['slug']}-{slugify_suburb(suburb['suburb'])}-{suburb['state'].lower()}"
    canonical = f"{SITE}/locations/{slug}.html"

    title = f"{vertical['label']} in {suburb['suburb']}, {suburb['state']} {suburb['postcode']} | LeadEvolution"
    meta_desc = (
        f"Exclusive, consent-based {vertical['professional']} leads across {suburb['suburb']} {suburb['state']} {suburb['postcode']} "
        f"and greater {suburb['metro']}. Delivered in {vertical['delivery_hours']}. No lock-in contract. DNCR compliant."
    )
    keywords = f"{vertical['professional']} leads {suburb['suburb']}, {vertical['professional']} leads {suburb['metro']}, {vertical['label'].lower()} {suburb['state']}, pay per lead {suburb['suburb']} {suburb['postcode']}"

    metro_line = metro_context_line(suburb["suburb"], suburb["metro"], vertical["slug"])
    state_note = state_compliance_note(suburb["state"])

    related = related_suburbs(suburb["suburb"], SUBURBS, suburb["metro"], count=3)
    related_html = "".join([
        f'<a href="{vertical["slug"]}-{slugify_suburb(r["suburb"])}-{r["state"].lower()}.html" class="tag">{vertical["label"]} in {r["suburb"]}</a>'
        for r in related
    ])

    targets_html = "".join([f'<span class="tag">{t}</span>' for t in vertical["targets"]])

    # JSON-LD schema
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": vertical["label"],
        "name": f"{vertical['label']} in {suburb['suburb']}, {suburb['state']}",
        "description": meta_desc,
        "provider": {
            "@type": "Organization",
            "name": "LeadEvolution",
            "url": SITE,
            "email": "info@leadevolution.com.au",
            "logo": f"{SITE}/images/logo.png",
        },
        "areaServed": {
            "@type": "Place",
            "name": f"{suburb['suburb']}, {suburb['state_full']}",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": suburb["lat"],
                "longitude": suburb["lng"],
            },
            "address": {
                "@type": "PostalAddress",
                "addressLocality": suburb["suburb"],
                "addressRegion": suburb["state"],
                "postalCode": suburb["postcode"],
                "addressCountry": "AU",
            },
        },
        "url": canonical,
    }

    schema_json = json.dumps(schema, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="LeadEvolution">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_desc}">
<link rel="stylesheet" href="../styles.css">
<script type="application/ld+json">{schema_json}</script>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo">Lead<span>Evolution</span></a>
    <div class="nav-links" id="navLinks">
      <a href="../index.html" class="nav-link">Home</a>
      <div class="dropdown"><span class="nav-link">Verticals ▾</span><div class="dropdown-menu"><a href="../verticals/mortgage-broker-leads.html" class="dropdown-item">🏠 Mortgage Broker Leads</a><a href="../verticals/financial-planning-leads.html" class="dropdown-item">📊 Financial Planning Leads</a><a href="../verticals/solar-leads.html" class="dropdown-item">☀️ Solar Leads</a><a href="../verticals/insurance-leads.html" class="dropdown-item">🛡️ Insurance Broker Leads</a><a href="../verticals/energy-leads.html" class="dropdown-item">⚡ Energy Broker Leads</a><a href="../verticals/commercial-finance-leads.html" class="dropdown-item">🏢 Commercial Finance Leads</a></div></div>
      <a href="../faq.html" class="nav-link">FAQ</a>
      <a href="../team.html" class="nav-link">Why Us</a>
      <a href="../contact.html" class="nav-link">Contact</a>
      <a href="../contact.html" class="nav-link nav-cta">Get Started →</a>
    </div>
    <div class="hamburger" id="hamburger"><span></span><span></span><span></span></div>
  </div>
</nav>
<div class="mobile-menu" id="mobile-menu">
  <a href="../index.html" class="mobile-link">Home</a>
  <a href="../verticals/mortgage-broker-leads.html" class="mobile-link">🏠 Mortgage Broker Leads</a>
  <a href="../verticals/financial-planning-leads.html" class="mobile-link">📊 Financial Planning Leads</a>
  <a href="../verticals/solar-leads.html" class="mobile-link">☀️ Solar Leads</a>
  <a href="../verticals/insurance-leads.html" class="mobile-link">🛡️ Insurance Broker Leads</a>
  <a href="../verticals/energy-leads.html" class="mobile-link">⚡ Energy Broker Leads</a>
  <a href="../verticals/commercial-finance-leads.html" class="mobile-link">🏢 Commercial Finance Leads</a>
  <a href="../faq.html" class="mobile-link">FAQ</a>
  <a href="../team.html" class="mobile-link">Why Us</a>
  <a href="../contact.html" class="mobile-link">Contact</a>
  <a href="../contact.html" class="mobile-cta">Get Started →</a>
</div>

<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-label">{vertical['emoji']} {vertical['label']} — {suburb['suburb']} {suburb['state']}</div>
    <h1>{vertical['label']} in {suburb['suburb']}<br><em>{suburb['state']} {suburb['postcode']}</em></h1>
    <p>{vertical['hero']} Delivered exclusively to {vertical['professional']}s working across {suburb['suburb']} and greater {suburb['metro']}.</p>
    <div class="page-hero-btns">
      <a href="../contact.html" class="btn btn-primary">Get {vertical['short']} in {suburb['suburb']} →</a>
      <a href="../contact.html" class="btn btn-outline">Send an Enquiry</a>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-inner">
    <div class="info-grid">
      <div class="content-block">

        <h2>{vertical['label']} Coverage in {suburb['suburb']}, {suburb['state']}</h2>
        <p>{metro_line}</p>
        <p>LeadEvolution generates {vertical['professional']} leads across postcode {suburb['postcode']} and the surrounding radius. Every lead is 100% exclusive — never resold, never shared — and captured with explicit consent to be contacted by a {vertical['professional']} specialist.</p>

        <h2>The {suburb['metro']} {vertical['label']} Market</h2>
        <p>{vertical['market_line']}</p>
        <p>Working in {suburb['suburb']} specifically, you're operating inside one of the more active {suburb['metro']} submarkets. Our data collection focuses on residents and businesses whose intent to act is time-boxed — not researchers stuck at the top of the funnel.</p>

        <h2>What You Get With Every Lead</h2>
        <ul>
          <li>Full name, mobile number, and email address</li>
          <li>Postcode and suburb-level location detail</li>
          <li>Explicit consent to be contacted by a {vertical['professional']}</li>
          <li>Timeframe to act (ready now, 1–3 months, longer horizon)</li>
          <li>Vertical-specific qualification fields (relevant to {vertical['label'].lower()})</li>
          <li>Delivery method of your choice: CRM push, email, or spreadsheet</li>
        </ul>

        <h2>Who We Target in {suburb['suburb']}</h2>
        <div class="tag-row">{targets_html}</div>

        <h2>Why {vertical['professional'].title()}s in {suburb['suburb']} Choose LeadEvolution</h2>
        <p>Most {vertical['professional']}s in {suburb['metro']} have been through the pain: paying $100–$200 per shared lead, discovering the same prospect has been called four times, then defending the file to a compliance officer.</p>
        <p>With 100% exclusive, consent-based leads delivered inside {vertical['delivery_hours']} from onboarding, LeadEvolution changes the pipeline economics. {vertical['commission_note']}</p>

        <h2>Compliance in {suburb['state_full']}</h2>
        <p>{state_note}</p>

        <h2>Related {vertical['label']} Coverage</h2>
        <div class="tag-row">{related_html}</div>

      </div>

      <div>
        <div class="info-box">
          <h3>Lead Snapshot — {suburb['suburb']}</h3>
          <div class="info-row"><span class="info-lbl">Location</span><span class="info-val">{suburb['suburb']}, {suburb['state']} {suburb['postcode']}</span></div>
          <div class="info-row"><span class="info-lbl">Vertical</span><span class="info-val">{vertical['label']}</span></div>
          <div class="info-row"><span class="info-lbl">Exclusivity</span><span class="info-val g">100% Exclusive</span></div>
          <div class="info-row"><span class="info-lbl">Delivery time</span><span class="info-val">{vertical['delivery_hours']}</span></div>
          <div class="info-row"><span class="info-lbl">Deal value</span><span class="info-val">{vertical['avg_value']}</span></div>
          <div class="info-row"><span class="info-lbl">Consent-based</span><span class="info-val g">✓ Always</span></div>
          <div class="info-row"><span class="info-lbl">DNCR compliant</span><span class="info-val g">✓ Always</span></div>
          <div class="info-row"><span class="info-lbl">Replacement guarantee</span><span class="info-val g">✓ Yes</span></div>
          <div class="info-row"><span class="info-lbl">Lock-in contract</span><span class="info-val g">None</span></div>
          <a href="../contact.html" class="btn btn-primary" style="display:block;text-align:center;margin-top:24px">Get Leads in {suburb['suburb']} →</a>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="final-cta">
  <h2>Fill Your {suburb['suburb']} Pipeline</h2>
  <p>First leads delivered in {vertical['delivery_hours']} from onboarding. No lock-in contract.</p>
  <a href="../contact.html" class="btn btn-primary btn-lg">Get Started →</a>
</div>

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div><div class="footer-logo">Lead<span>Evolution</span></div><p class="footer-desc">Australia's specialist pay per lead agency. Exclusive, consent-based leads across six verticals.</p></div>
      <div class="footer-col"><h4>Verticals</h4><a href="../verticals/mortgage-broker-leads.html">Mortgage Broker Leads</a><a href="../verticals/financial-planning-leads.html">Financial Planning Leads</a><a href="../verticals/solar-leads.html">Solar Leads</a><a href="../verticals/insurance-leads.html">Insurance Leads</a><a href="../verticals/energy-leads.html">Energy Leads</a><a href="../verticals/commercial-finance-leads.html">Commercial Finance</a></div>
      <div class="footer-col"><h4>Company</h4><a href="../team.html">Why Us</a><a href="../faq.html">FAQ</a><a href="../contact.html">Contact Us</a></div>
      <div class="footer-col"><h4>Legal</h4><a href="../terms.html">Terms &amp; Conditions</a><a href="../privacy.html">Privacy Policy</a></div>
    </div>
    <div class="footer-bottom"><p>© 2026 LeadEvolution. A trading name of Artificial Innovations Pty Ltd (ABN 53 677 049 946).</p><div class="footer-links"><a href="../terms.html">Terms</a><a href="../privacy.html">Privacy</a><a href="../contact.html">Contact</a></div></div>
  </div>
</footer>
<script src="../main.js"></script>
</body>
</html>
"""


# ---------- MAIN ----------

def main():
    loc_dir = ROOT / "locations"
    loc_dir.mkdir(exist_ok=True)

    generated = []
    for vertical in VERTICALS:
        for suburb in SUBURBS:
            slug = f"{vertical['slug']}-{slugify_suburb(suburb['suburb'])}-{suburb['state'].lower()}"
            path = loc_dir / f"{slug}.html"
            html = location_page_html(vertical, suburb)
            path.write_text(html, encoding="utf-8")
            generated.append(f"/locations/{slug}.html")

    # Sitemap
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
    all_urls = base_pages + generated
    today = datetime.utcnow().strftime("%Y-%m-%d")

    urlset = ['<?xml version="1.0" encoding="UTF-8"?>']
    urlset.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in all_urls:
        priority = "1.0" if url == "/" else ("0.9" if "/verticals/" in url else ("0.7" if "/locations/" in url else "0.6"))
        changefreq = "weekly" if "/locations/" not in url else "monthly"
        urlset.append("  <url>")
        urlset.append(f"    <loc>{SITE}{url}</loc>")
        urlset.append(f"    <lastmod>{today}</lastmod>")
        urlset.append(f"    <changefreq>{changefreq}</changefreq>")
        urlset.append(f"    <priority>{priority}</priority>")
        urlset.append("  </url>")
    urlset.append("</urlset>")

    (ROOT / "sitemap.xml").write_text("\n".join(urlset), encoding="utf-8")

    print(f"Generated {len(generated)} location pages")
    print(f"Sitemap contains {len(all_urls)} URLs")


if __name__ == "__main__":
    main()
