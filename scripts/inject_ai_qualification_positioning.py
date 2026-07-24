#!/usr/bin/env python3
"""
Inject AI voice qualification positioning into vertical pages + homepage.
Idempotent — checks for the marker phrase before adding.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VERTICALS = [
    ("verticals/mortgage-broker-leads.html", "mortgage broker", "purchase, refinance and investment"),
    ("verticals/financial-planning-leads.html", "financial adviser", "superannuation consolidation, SMSF setup, wealth management and retirement planning"),
    ("verticals/solar-leads.html", "solar installer", "residential rooftop solar and battery storage"),
    ("verticals/insurance-leads.html", "insurance broker", "life insurance and income protection"),
    ("verticals/energy-leads.html", "energy broker", "residential and SME electricity/gas switching"),
    ("verticals/commercial-finance-leads.html", "commercial finance broker", "equipment finance, working capital, commercial property and trade finance"),
]


def ai_qualification_block(professional, product_context):
    return f'''
        <h2>Every {professional.title()} Lead Is AI-Voice-Qualified</h2>
        <p>Our proprietary AI voice qualification system holds a live phone conversation with every prospect before we deliver anything to you. The AI agent introduces itself, confirms the prospect is genuinely interested in {product_context}, captures explicit consent to be contacted by a {professional} in their own voice, and only forwards prospects who pass every criterion.</p>
        <p>Every qualified lead you receive arrives with the compliance evidence already attached — <strong>audio recording, machine-generated transcript, timestamped DNCR check, and structured qualification data</strong>. Not a text note from a calling agent. Real, replayable, defensible evidence in the prospect's own voice.</p>
        <p>This is why our contact rates typically sit in the 75–90% range instead of the 25–45% you'd see from form-fill leads. The prospect is expecting the call. They agreed to it. They remember. And if they ever dispute consent — or a regulator ever asks — the answer is one query away, not "we'll have to check with the calling team." <a href="../how-we-qualify.html" style="color:var(--blue);text-decoration:underline">See how our qualification process works →</a></p>
'''


for rel_path, professional, product_context in VERTICALS:
    path = ROOT / rel_path
    if not path.exists():
        print(f"[skip] missing: {rel_path}")
        continue
    content = path.read_text(encoding="utf-8")
    if "AI-Voice-Qualified" in content:
        print(f"[skip] already has AI positioning: {rel_path}")
        continue

    block = ai_qualification_block(professional, product_context)

    # Insert before the "Why [pro]s in [X] Choose LeadEvolution" heading
    # or before the FAQ section, or before Local Coverage Pages
    # Look for anchors in order of preference
    anchors = [
        '<h2>Local Coverage Pages</h2>',  # inserted by add_internal_links
        '<h2>Why Mortgage Brokers Choose LeadEvolution</h2>',
        '<h2>Why Financial Advisers Choose LeadEvolution</h2>',
        '<h2>Why Solar Installers Choose LeadEvolution</h2>',
        '<h2>Why Insurance Brokers Choose LeadEvolution</h2>',
        '<h2>Why Energy Brokers Choose LeadEvolution</h2>',
        '<h2>Why Commercial Finance Brokers Choose LeadEvolution</h2>',
    ]

    inserted = False
    for anchor in anchors:
        if anchor in content:
            content = content.replace(anchor, block + "\n        " + anchor, 1)
            inserted = True
            break

    if not inserted:
        # Fallback: insert before the vertical-specific FAQ section
        fallback = 'Lead FAQs</h2>'
        if fallback in content:
            content = content.replace(fallback, 'Lead FAQs</h2>' + block, 1)
            inserted = True
            # NOTE: this rare fallback would break — abort and warn
            print(f"[!] used fallback anchor for {rel_path} — manual review recommended")

    if inserted:
        path.write_text(content, encoding="utf-8")
        print(f"[✓] injected AI positioning: {rel_path}")
    else:
        print(f"[!] no anchor found: {rel_path}")


# ---------- Homepage — add AI qualification trust badge/hero mention ----------
index_path = ROOT / "index.html"
content = index_path.read_text(encoding="utf-8")

if "AI-Voice-Qualified" not in content and "ai-qualification-trust" not in content:
    # Insert an "AI voice qualification" trust strip below hero or as first-fold content
    # Find the hero section end (usually before ticker or first pillars section)
    # Insert a compact strip
    strip = '''
<!-- AI QUALIFICATION TRUST STRIP -->
<section class="ai-qualification-trust" style="padding:36px 0;background:linear-gradient(90deg,rgba(37,99,235,0.06) 0%,rgba(74,126,255,0.02) 100%);border-top:1px solid rgba(37,99,235,0.15);border-bottom:1px solid rgba(37,99,235,0.15);position:relative;z-index:3">
  <div class="wrap" style="max-width:1100px;text-align:center">
    <div style="display:inline-flex;align-items:center;gap:10px;color:#4A7EFF;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:12px">
      <span>⚡</span><span>Compliance by Construction</span>
    </div>
    <h2 style="font-size:clamp(22px,3vw,32px);margin:0 auto 12px;max-width:820px;color:#fff;line-height:1.3">Every LeadEvolution Lead Is Qualified by Our <span style="color:#4A7EFF">AI Voice System</span> — Not a Human Calling Centre</h2>
    <p style="color:#CBD5E1;font-size:15px;max-width:720px;margin:0 auto 20px;line-height:1.7">Full audio recording, machine-generated transcript, timestamped DNCR check and structured qualification data attached to every lead. Immutable audit trail in the prospect's own voice — because "we noted the call" isn't compliance evidence, it's a claim.</p>
    <a href="how-we-qualify.html" style="display:inline-flex;align-items:center;gap:8px;padding:12px 22px;background:rgba(37,99,235,0.15);border:1px solid rgba(37,99,235,0.4);border-radius:8px;color:#fff;font-size:14px;font-weight:600;text-decoration:none">See our AI qualification process →</a>
  </div>
</section>
'''
    # Insert immediately after the closing </section> of the hero (which contains the trust-badge / hero-stats)
    # Anchor: the ticker section start
    if '<div class="ticker">' in content:
        content = content.replace('<div class="ticker">', strip + '\n<div class="ticker">', 1)
    elif 'class="ticker"' in content:
        # Find the opening
        idx = content.find('class="ticker"')
        # Walk back to find the parent tag <div or <section
        # Simpler: find "<div class="ticker"" without quotes normalisation
        content = content.replace('<div class="ticker"', strip + '\n<div class="ticker"', 1)
    else:
        # Fallback: insert before the pillars section
        for a in ('<section id="pillars"', '<div class="pillars"'):
            if a in content:
                content = content.replace(a, strip + '\n' + a, 1)
                break

    index_path.write_text(content, encoding="utf-8")
    print("[✓] added AI qualification trust strip to index.html")
else:
    print("[skip] index.html already has AI positioning")
