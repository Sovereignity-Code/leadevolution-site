#!/usr/bin/env python3
"""
Add contextual internal links from each vertical page to its
top 5 location variants. This helps Google discover new
/locations/ pages and gives them a legitimate PageRank flow.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Top 5 suburbs per vertical (mix of metros)
TOP_LOCATIONS = [
    ("Parramatta", "NSW"),
    ("Southbank", "VIC"),
    ("South Brisbane", "QLD"),
    ("Southport", "QLD"),
    ("Perth CBD", "WA"),
]


def slugify(s):
    return s.lower().replace(" ", "-")


VERTICALS = [
    ("verticals/mortgage-broker-leads.html", "mortgage-broker-leads", "Mortgage Broker Leads"),
    ("verticals/financial-planning-leads.html", "financial-planning-leads", "Financial Planning Leads"),
    ("verticals/solar-leads.html", "solar-leads", "Solar Leads"),
    ("verticals/insurance-leads.html", "insurance-leads", "Insurance Broker Leads"),
    ("verticals/energy-leads.html", "energy-leads", "Energy Broker Leads"),
    ("verticals/commercial-finance-leads.html", "commercial-finance-leads", "Commercial Finance Leads"),
]


for rel_path, slug, label in VERTICALS:
    path = ROOT / rel_path
    content = path.read_text(encoding="utf-8")

    if "Local Coverage Pages" in content:
        print(f"[skip] already has coverage block: {rel_path}")
        continue

    # Build coverage block
    tags = "".join([
        f'<a href="../locations/{slug}-{slugify(sub)}-{st.lower()}.html" class="tag">{label} — {sub}, {st}</a>'
        for sub, st in TOP_LOCATIONS
    ])
    block = f'''
        <h2>Local Coverage Pages</h2>
        <p>Prefer to see how we handle {label.lower()} in your specific metro? We publish location-level detail for the highest-demand corridors:</p>
        <div class="tag-row">{tags}</div>
'''

    # Insert before </div><!-- end content-block --> — locate the </ul> before the info-box or the closing tag
    # Simplest robust anchor: insert before the "<h2>...FAQ" section, or before </div> that closes content-block
    # We know content-block ends before <div class="info-box"> block.
    # Insert after the last h2 heading section — find "content-block" and inject before its close.

    # Anchor: insert immediately before the "</div>\n\n      <div>" that begins the info-box column
    anchor = '</div>\n\n      <div>\n        <div class="info-box">'
    if anchor in content:
        new = content.replace(anchor, block + "      </div>\n\n      <div>\n        <div class=\"info-box\">", 1)
    else:
        # Fallback: insert before the final-cta section
        new = content.replace("<div class=\"final-cta\">", block + "\n<div class=\"final-cta\">", 1)

    path.write_text(new, encoding="utf-8")
    print(f"[✓] injected coverage block: {rel_path}")


# Also add a small "Coverage across Australia" strip to index.html
index_path = ROOT / "index.html"
content = index_path.read_text(encoding="utf-8")

if "coverage-strip" not in content:
    strip_html = '''
<!-- COVERAGE STRIP - programmatic pages internal linking -->
<div class="section coverage-strip" style="padding:60px 0;background:rgba(255,255,255,0.02);border-top:1px solid rgba(255,255,255,0.05);border-bottom:1px solid rgba(255,255,255,0.05)">
  <div class="section-inner" style="max-width:1100px;margin:0 auto;padding:0 20px">
    <div style="text-align:center;margin-bottom:32px">
      <div style="color:rgba(255,255,255,0.5);font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin-bottom:12px">Location Coverage</div>
      <h2 style="font-size:28px;margin:0 0 8px;color:#fff">Local Lead Coverage Across Australia</h2>
      <p style="color:rgba(255,255,255,0.6);max-width:640px;margin:0 auto">Explore lead availability by suburb and vertical. We publish coverage detail for every major metropolitan corridor.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px">
      <a href="locations/mortgage-broker-leads-parramatta-nsw.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">🏠 Mortgage Leads — Parramatta</a>
      <a href="locations/mortgage-broker-leads-southbank-vic.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">🏠 Mortgage Leads — Southbank</a>
      <a href="locations/solar-leads-southport-qld.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">☀️ Solar Leads — Southport</a>
      <a href="locations/solar-leads-chermside-qld.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">☀️ Solar Leads — Chermside</a>
      <a href="locations/financial-planning-leads-north-sydney-nsw.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">📊 Financial Planning — North Sydney</a>
      <a href="locations/financial-planning-leads-south-brisbane-qld.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">📊 Financial Planning — South Brisbane</a>
      <a href="locations/commercial-finance-leads-perth-cbd-wa.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">🏢 Commercial Finance — Perth CBD</a>
      <a href="locations/insurance-leads-adelaide-cbd-sa.html" style="padding:12px 16px;background:rgba(37,99,235,0.08);border:1px solid rgba(37,99,235,0.15);border-radius:8px;color:#fff;font-size:13px">🛡️ Insurance Leads — Adelaide CBD</a>
    </div>
    <p style="text-align:center;margin-top:20px;font-size:13px;color:rgba(255,255,255,0.5)">120+ location pages across 6 verticals in all Australian metros — <a href="contact.html" style="color:#4A7EFF">tell us your suburb</a> and we'll confirm coverage.</p>
  </div>
</div>
'''
    # Insert before <footer>
    new = content.replace("<footer>", strip_html + "\n<footer>", 1)
    index_path.write_text(new, encoding="utf-8")
    print("[✓] added coverage strip to index.html")
else:
    print("[skip] index.html already has coverage strip")
