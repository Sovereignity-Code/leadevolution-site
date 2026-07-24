#!/usr/bin/env python3
"""
Build the /compare/ and /guides/ pages using a shared shell wrapper.
Each article's substantive body is passed in as unique HTML — no template
duplication across pages.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leadevolution.com.au"


def shell(url_path, title, description, body_html, article_schema=None, section_label="Guide"):
    canonical = f"{SITE}{url_path}"
    org_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "LeadEvolution",
        "url": SITE,
        "logo": f"{SITE}/images/logo.png",
        "email": "info@leadevolution.com.au",
    }
    schemas = [org_schema]
    if article_schema:
        schemas.append(article_schema)
    schema_blocks = "\n".join([
        f'<script type="application/ld+json">{json.dumps(s, indent=2)}</script>'
        for s in schemas
    ])
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="LeadEvolution">
<meta property="og:locale" content="en_AU">
<meta property="og:image" content="{SITE}/images/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="stylesheet" href="../styles.css">
{schema_blocks}
<style>
  .article-body {{ max-width: 780px; margin: 0 auto; }}
  .article-body h2 {{ font-size: 28px; margin: 44px 0 16px; letter-spacing: -0.5px; }}
  .article-body h3 {{ font-size: 20px; margin: 32px 0 12px; color: #fff; font-weight: 700; }}
  .article-body p {{ color: var(--muted); font-size: 17px; line-height: 1.85; margin-bottom: 18px; }}
  .article-body ul, .article-body ol {{ color: var(--muted); font-size: 17px; line-height: 1.85; padding-left: 22px; margin-bottom: 20px; }}
  .article-body ul li, .article-body ol li {{ margin-bottom: 10px; }}
  .article-body strong {{ color: #fff; }}
  .article-body table {{ width: 100%; border-collapse: collapse; margin: 24px 0; background: rgba(255,255,255,0.03); border-radius: 12px; overflow: hidden; }}
  .article-body th, .article-body td {{ padding: 14px 18px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 15px; color: var(--muted); }}
  .article-body th {{ background: rgba(37,99,235,0.15); color: #fff; font-weight: 700; letter-spacing: 0.02em; }}
  .article-body td:first-child {{ color: #fff; font-weight: 500; }}
  .article-body .callout {{ background: rgba(37,99,235,0.08); border-left: 3px solid var(--blue); padding: 20px 24px; margin: 24px 0; border-radius: 6px; color: #fff; }}
  .article-body .callout p {{ color: rgba(255,255,255,0.9); margin: 0; font-size: 16px; }}
  .article-body .verdict {{ background: linear-gradient(135deg, rgba(37,99,235,0.18), rgba(74,126,255,0.08)); border: 1px solid rgba(37,99,235,0.3); border-radius: 14px; padding: 28px 32px; margin: 40px 0; }}
  .article-body .verdict h3 {{ margin-top: 0; color: #fff; font-size: 22px; }}
  .article-body .verdict p {{ color: rgba(255,255,255,0.9); }}
  .article-meta {{ display: flex; gap: 20px; color: rgba(255,255,255,0.5); font-size: 14px; margin-bottom: 32px; }}
  .article-meta span::before {{ content: '• '; margin: 0 4px; color: rgba(255,255,255,0.3); }}
  .article-meta span:first-child::before {{ content: ''; margin: 0; }}
</style>
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
    <div class="page-hero-label">{section_label}</div>
    <h1>{title.split(" | ")[0]}</h1>
  </div>
</div>

<div class="section" style="padding-top:24px">
  <div class="section-inner">
    <div class="article-body">
{body_html}

      <div class="verdict">
        <h3>Ready to move?</h3>
        <p>LeadEvolution runs the exclusive, consent-based model described above across six Australian verticals. If you'd like to see how it works for your pipeline, tell us your industry and volume — we'll come back inside one business day.</p>
        <div style="margin-top:20px"><a href="../contact.html" class="btn btn-primary">Get Started →</a></div>
      </div>
    </div>
  </div>
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


def article_schema(url_path, title, description, published="2026-07-24"):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title.split(" | ")[0],
        "description": description,
        "author": {
            "@type": "Organization",
            "name": "LeadEvolution",
        },
        "publisher": {
            "@type": "Organization",
            "name": "LeadEvolution",
            "logo": {
                "@type": "ImageObject",
                "url": f"{SITE}/images/logo.png",
            }
        },
        "datePublished": published,
        "dateModified": published,
        "mainEntityOfPage": f"{SITE}{url_path}",
    }


def build(rel_out, title, description, body, section_label="Article"):
    out = ROOT / rel_out
    out.parent.mkdir(exist_ok=True)
    url_path = "/" + rel_out
    html = shell(url_path, title, description, body,
                 article_schema=article_schema(url_path, title, description),
                 section_label=section_label)
    out.write_text(html, encoding="utf-8")
    print(f"[✓] {rel_out}")


# ========================================================================
# COMPARISON PAGES
# ========================================================================

# --- 1. Exclusive vs Shared ---
body_1 = """
<div class="article-meta"><span>Comparison</span><span>10 min read</span><span>For brokers evaluating lead sources</span></div>

<p>The most common conversation we have with new brokers goes like this: <em>"Your leads are $200. My current provider is $80. Why should I pay more than double?"</em></p>

<p>It's a fair question. It's also the wrong one. The right question is which model puts more <strong>settled business</strong> on your books at the lowest <strong>total</strong> cost — and once you break that down honestly, shared leads at $80 are almost always the more expensive option, sometimes catastrophically so.</p>

<h2>What "shared" actually means in practice</h2>

<p>A shared lead is a prospect whose contact details are sold to multiple buyers. In the Australian mortgage, insurance, and solar markets, the going rate for a shared consumer lead is between $60 and $120. Providers typically sell each lead to <strong>three to five brokers</strong>, and the more aggressive operators will sell it to seven or eight.</p>

<p>The lead is delivered to all buyers at roughly the same moment. If you're broker number four in the queue, the prospect has already spoken to three of your competitors by the time your call goes out, and their patience for a fourth pitch is usually exhausted. Answer rates on shared leads collapse the further down the queue you sit — and the queue position is almost never disclosed.</p>

<h2>What "exclusive" actually means</h2>

<p>An exclusive lead is a prospect sold to <strong>one</strong> buyer. When you receive that prospect's details, no one else in the market has them. If they've been contacted at all, it was by the lead source itself during qualification — not by a competing broker.</p>

<p>Exclusive leads cost more per unit because the entire economic model of the supplier changes. A provider selling shared leads recovers cost across five buyers. A provider selling exclusive leads has to recover cost from one buyer per prospect, which forces the unit price up — usually to somewhere between $150 and $300 depending on vertical.</p>

<h2>The real math (with realistic conversion assumptions)</h2>

<p>Let's use a mortgage broker as the worked example. Assume: 100 leads, average commission $2,400 per settled loan (including trail-value adjusted upfront).</p>

<table>
<thead>
<tr><th>Model</th><th>Unit cost</th><th>Total spend</th><th>Contact rate</th><th>Conversion to settled</th><th>Settled loans</th><th>Revenue</th><th>ROI</th></tr>
</thead>
<tbody>
<tr><td>Shared (queue position 3-5)</td><td>$80</td><td>$8,000</td><td>35%</td><td>3%</td><td>3</td><td>$7,200</td><td>-10%</td></tr>
<tr><td>Shared (queue position 1-2)</td><td>$80</td><td>$8,000</td><td>55%</td><td>7%</td><td>7</td><td>$16,800</td><td>110%</td></tr>
<tr><td>Exclusive (consent-based)</td><td>$200</td><td>$20,000</td><td>82%</td><td>14%</td><td>14</td><td>$33,600</td><td>68%</td></tr>
</tbody>
</table>

<p>The problem with the shared model isn't the average outcome — it's the <strong>variance</strong>. You cannot control queue position. If you sit in position 4 for a month, you lose money. If you sit in position 1 for a month, you make money. Neither is under your control, and neither is disclosed.</p>

<p>The exclusive model has lower variance because there is no queue. Every prospect answers to you first. Whether they convert then depends on you.</p>

<h2>The costs nobody counts in the "$80 vs $200" comparison</h2>

<p>Per-lead price is only one input. The full cost stack looks more like this:</p>

<ul>
  <li><strong>Broker labour cost.</strong> A broker who spends 4 hours dialling shared leads with a 35% contact rate is burning $200-$400 of their own time per day. That labour disappears if the leads answer.</li>
  <li><strong>Compliance drag.</strong> Shared lead pools frequently include Do Not Call Register (DNCR) violations or expired consent. Every one of those creates paperwork and, if audited, ACMA exposure.</li>
  <li><strong>CRM pollution.</strong> Dead leads that keep bouncing around your pipeline distort conversion metrics, confuse reporting, and rot the productivity of the sales team.</li>
  <li><strong>Reputation.</strong> The prospect on the receiving end of the fourth broker call in a day forms an opinion about lead-fed brokers. That opinion doesn't attach to the provider — it attaches to <em>you</em>.</li>
</ul>

<h2>When shared leads genuinely work</h2>

<p>We should be honest: there are cases where shared leads are the correct choice.</p>

<ul>
  <li><strong>Volume-first operations testing new scripts.</strong> If your goal is to burn through 1,000 dials to A/B test a new call opener, shared leads are a legitimate laboratory. You want reps, not conversions.</li>
  <li><strong>Territory expansion.</strong> Cheap shared leads can validate whether a new postcode responds before you invest in exclusive supply there.</li>
  <li><strong>Overflow capacity.</strong> If your BDR team has downtime and the marginal call cost is close to zero, cheap leads can absorb slack.</li>
</ul>

<p>Outside these cases, shared leads are a false economy. The reason serious brokers eventually migrate to exclusive supply is not ideology — it's arithmetic.</p>

<h2>What to ask any exclusive lead provider</h2>

<p>Not all providers who claim "exclusive" honour it. Before you sign anything, ask:</p>

<ol>
  <li>Is exclusivity written into the service agreement, or just implied on the sales call?</li>
  <li>What is the replacement policy if a lead turns out to have been sold elsewhere?</li>
  <li>How is consent captured, timestamped, and audited?</li>
  <li>What proportion of leads are DNCR-checked at delivery?</li>
  <li>Can you speak to two current clients before signing?</li>
</ol>

<p>The answers to those five questions separate operators from resellers.</p>
"""

build(
    "compare/exclusive-vs-shared-leads.html",
    "Exclusive vs Shared Leads — The Real Math for Australian Brokers | LeadEvolution",
    "Cheap shared leads look attractive until you count queue position, contact rate, and compliance drag. Full ROI breakdown for Aussie mortgage, insurance, and solar brokers.",
    body_1,
    section_label="Comparison"
)


# --- 2. Consent-Based vs Form-Fill ---
body_2 = """
<div class="article-meta"><span>Comparison</span><span>9 min read</span><span>Compliance-focused</span></div>

<p>Two Australian brokers can buy leads from two different providers, pay similar prices, and end up in radically different regulatory positions. The difference usually comes down to how the lead was sourced — specifically, whether the prospect gave <strong>explicit, informed consent</strong> or filled out a form on a landing page they've since forgotten existed.</p>

<p>This is the consent-based versus form-fill distinction, and it matters more in 2026 than it did a decade ago. The Australian Communications and Media Authority (ACMA) has taken a materially harder enforcement line on unsolicited contact — and the fines are large enough to end a lead-fed business.</p>

<h2>What "form-fill" leads really are</h2>

<p>A form-fill lead is a prospect whose contact details were captured through a landing page — typically an offer page ("Compare 5 solar quotes", "Check your borrowing power", "Get an insurance quote in 60 seconds"). The prospect fills in a form and hits submit.</p>

<p>The consent language on these forms is where the entire regulatory risk sits. Most operators use catch-all consent designed to cover the widest possible resale: <em>"By submitting this form, you agree to be contacted by us and our marketing partners about products and services that may interest you."</em></p>

<p>That kind of blanket clause is legally shaky under both the Privacy Act 1988 and the Spam Act 2003. In practice, it means the prospect has consented to be contacted by <em>someone</em> about <em>something</em> — but not specifically to be phoned by a mortgage broker they've never heard of about a product they didn't ask about.</p>

<h2>What "consent-based" means when done properly</h2>

<p>A consent-based lead is one where the prospect has explicitly agreed to be contacted about a <strong>specific product category</strong> by a <strong>specific type of professional</strong>, with the agreement <strong>timestamped and stored</strong> so it can be produced under audit.</p>

<p>In our own model, that agreement is captured through a live AI voice qualification call. The prospect confirms three things during the conversation:</p>

<ul>
  <li>They are actively interested in the product category (mortgage, financial advice, solar, insurance, energy, commercial finance)</li>
  <li>They agree to be phoned by a licensed specialist within an agreed timeframe</li>
  <li>They have been shown who the company is and how their data will be used</li>
</ul>

<p>Each of those confirmations is captured, timestamped, and stored against the lead record — <strong>as audio, transcript, and structured data all at once</strong>. That's the difference between "we think it was compliant" and "we can prove it was compliant."</p>

<h2>The evidence hierarchy — from weakest to strongest</h2>

<p>Not all consent is equal in a regulator's eyes. The evidentiary weight of the different consent formats currently in market:</p>

<table>
<thead>
<tr><th>Consent format</th><th>Evidence weight</th><th>Why</th></tr>
</thead>
<tbody>
<tr><td>Form checkbox on a landing page</td><td>Weakest</td><td>Prospect may not have read the clause. Consent language is often blanket. Frequently resold across dozens of buyers.</td></tr>
<tr><td>Manual double-opt-in email</td><td>Weak-to-medium</td><td>Establishes the email was accessed but not that the person understood what they were agreeing to.</td></tr>
<tr><td>Human phone call with text-note record</td><td>Medium</td><td>Real conversation, but the record is a note written by an incentivised human. Hard to defend if challenged.</td></tr>
<tr><td>AI voice qualification with audio + transcript</td><td>Strongest</td><td>The prospect's own voice, on record, timestamped, tied to the phone number, with a machine-generated transcript for search and audit. Immutable and verifiable.</td></tr>
</tbody>
</table>

<p>When an ACMA investigator asks "produce the consent record for this call," the answer format matters as much as the content. A blanket checkbox screenshot is a signal you tried; a full audio recording of the prospect saying "yes, please have a mortgage broker call me" is a signal you documented.</p>

<h2>The regulatory picture in 2026</h2>

<p>Three regulators care about how brokers acquire and contact leads:</p>

<h3>ACMA (Australian Communications and Media Authority)</h3>

<p>ACMA runs the Do Not Call Register. Contacting an Australian number listed on the DNCR without valid consent carries civil penalties up to $2.2 million for a single course of conduct by a corporation. ACMA has increased both the number of investigations and the size of penalties in recent years.</p>

<h3>OAIC (Office of the Australian Information Commissioner)</h3>

<p>OAIC enforces the Privacy Act. In 2023 the maximum penalty for serious or repeated interference with privacy was lifted to the greater of $50 million, three times the value of any benefit obtained, or 30% of adjusted turnover during the breach period. Improper resale of personal information sits squarely in this territory.</p>

<h3>ASIC (Australian Securities & Investments Commission)</h3>

<p>ASIC cares about financial services conduct. Cold-calling under the guise of a "free assessment" while intending to sell a regulated product without appropriate disclosures is a general conduct breach — not just a privacy issue.</p>

<h2>Side-by-side comparison</h2>

<table>
<thead>
<tr><th>Attribute</th><th>Form-fill lead</th><th>Consent-based lead</th></tr>
</thead>
<tbody>
<tr><td>Prospect awareness of you</td><td>None — you're the reseller</td><td>Aware — consent was given for your call</td></tr>
<tr><td>Freshness</td><td>Often days or weeks old</td><td>Usually delivered within 24-72 hours</td></tr>
<tr><td>Exclusivity</td><td>Frequently resold 3-5 times</td><td>Sold to one broker only</td></tr>
<tr><td>DNCR check</td><td>Assumed valid, rarely re-checked</td><td>Checked at delivery</td></tr>
<tr><td>Audit trail</td><td>Blanket consent clause</td><td>Timestamped, prospect-specific</td></tr>
<tr><td>ACMA risk if audited</td><td>High</td><td>Low</td></tr>
<tr><td>Answer rate</td><td>25-45%</td><td>75-90%</td></tr>
<tr><td>Typical unit cost</td><td>$40-$100</td><td>$150-$300</td></tr>
</tbody>
</table>

<h2>How to spot recycled form-fill data</h2>

<p>If you already buy leads and want to test whether they're form-fill recycled data or genuinely consented, three quick tests reveal a lot:</p>

<ol>
  <li><strong>Ask the prospect who they expected to hear from.</strong> A consented prospect will say "the mortgage specialist" or "the solar company." A recycled form-fill prospect will typically say "I filled out a form ages ago, I don't remember."</li>
  <li><strong>Check how many other brokers have called.</strong> If the prospect says three or four, the "exclusive" claim is worthless.</li>
  <li><strong>Ask the provider for a raw consent record.</strong> A legitimate consent-based operator will produce a timestamped audio snippet or record within hours. An operator selling recycled form-fill data will stall.</li>
</ol>

<h2>The commercial argument</h2>

<p>Compliance risk is only half the story. Consent-based leads answer, engage, and convert at materially higher rates because the prospect is expecting the call. The form-fill model is cheap because the underlying data is degraded — old, over-sold, and paired with weak consent.</p>

<p>A broker doing $50k/month in commissions cannot afford a single ACMA investigation. And most brokers who've been through one will tell you the reason it happened was that they didn't ask hard questions about consent when the leads first arrived.</p>
"""

build(
    "compare/consent-based-vs-form-fill-leads.html",
    "Consent-Based Leads vs Form-Fill Lists — Australian Compliance & Conversion Reality",
    "Form-fill leads look cheap until ACMA lands. What the Spam Act, Privacy Act, and DNCR actually require, and what separates real consent from a checkbox trick.",
    body_2,
    section_label="Comparison"
)


# --- 3. Pay Per Lead vs Retainer ---
body_3 = """
<div class="article-meta"><span>Comparison</span><span>8 min read</span><span>For business owners</span></div>

<p>When a broker or advisory business decides it needs more leads, the two dominant supplier models are pay-per-lead (PPL) and monthly retainer agencies. Both work — for different problems. The failure mode is picking the wrong one for what you actually need.</p>

<h2>What a retainer agency actually delivers</h2>

<p>A traditional marketing agency on retainer charges a monthly fee (usually $4,000-$15,000) to run some combination of: paid ads, SEO, content marketing, social, and sometimes email. The deliverable is <strong>activity</strong>, not leads.</p>

<p>Retainers work well when you need:</p>

<ul>
  <li>Brand-building over a 12-month horizon</li>
  <li>SEO / content authority that compounds</li>
  <li>Multi-channel campaigns coordinated across paid, organic, and social</li>
  <li>Creative work — video, ads, editorial</li>
  <li>A partner to run marketing operations while you focus on selling</li>
</ul>

<p>The economic exchange is: <em>you pay for expertise and time; they deliver work and hopefully leads.</em> The risk sits with you. If the campaigns underperform, you paid for the effort regardless.</p>

<h2>What pay-per-lead actually delivers</h2>

<p>A PPL supplier delivers <strong>units of qualified prospect data</strong>. You pay per lead delivered to spec, and you pay nothing for anything else — no setup fees, no minimums, no monthly commitment.</p>

<p>The economic exchange is: <em>the supplier absorbs all the risk of generating a lead; you only pay for successful deliveries.</em></p>

<p>PPL works well when you need:</p>

<ul>
  <li>Direct sales pipeline volume with known unit economics</li>
  <li>Scale up or down without contract friction</li>
  <li>Clean CAC modelling — cost per lead is a single number</li>
  <li>No commitment while you're testing a new vertical or geography</li>
  <li>Predictable cost against variable pipeline size</li>
</ul>

<h2>Where the models differ commercially</h2>

<table>
<thead>
<tr><th>Attribute</th><th>Retainer agency</th><th>Pay per lead</th></tr>
</thead>
<tbody>
<tr><td>Payment structure</td><td>Fixed monthly fee</td><td>Per delivered lead</td></tr>
<tr><td>Setup cost</td><td>Often $2k-$10k</td><td>$0</td></tr>
<tr><td>Minimum commitment</td><td>3-12 months typical</td><td>None</td></tr>
<tr><td>Where risk sits</td><td>You</td><td>Supplier</td></tr>
<tr><td>What you buy</td><td>Time and expertise</td><td>Qualified leads</td></tr>
<tr><td>Attribution clarity</td><td>Often murky</td><td>Explicit per lead</td></tr>
<tr><td>Scaling up</td><td>Renegotiation</td><td>Change the volume, no contract</td></tr>
<tr><td>Scaling down</td><td>Notice period</td><td>Immediate</td></tr>
<tr><td>Best for</td><td>Brand + long horizon</td><td>Direct pipeline now</td></tr>
</tbody>
</table>

<h2>The three-scenario decision framework</h2>

<h3>Scenario A — You need pipeline this month</h3>

<p>If the answer to <em>"do I need leads within 4 weeks?"</em> is yes, PPL is almost always the correct choice. A retainer agency will take 60-90 days to spin up a campaign, generate creative, get traffic flowing, and start delivering measurable leads. A PPL supplier can start delivering within days of onboarding.</p>

<h3>Scenario B — You want to own the funnel long term</h3>

<p>If you're building a brand you plan to compound over years — say, an advisory firm building a niche around SMSF setup for medical professionals — a retainer engagement is the right structure. You're investing in an owned asset (website, ad accounts, content library) that becomes more valuable over time. PPL doesn't build that.</p>

<h3>Scenario C — You want the best of both</h3>

<p>Most established brokers run a hybrid model: <strong>PPL as the workhorse for pipeline, retainer for brand-building</strong>. The PPL supply keeps the sales team fed while the retainer agency slowly compounds an owned marketing asset. The two don't compete — they complement.</p>

<h2>The hidden cost of retainer agencies</h2>

<p>A $10,000/month retainer is $120,000/year. If that spend generates 400 leads over the year, the effective cost per lead is $300. If it generates 200 leads, the effective CPL is $600. If it generates 100 leads, the effective CPL is $1,200.</p>

<p>The problem is you don't know the ratio until you've paid for a year. PPL avoids this by pricing every unit up front — you know your CPL from the first delivery.</p>

<h2>The hidden cost of PPL</h2>

<p>PPL is not free of tradeoffs either. Because the supplier absorbs the acquisition risk, they need a per-unit margin that can look "expensive" on paper. And because you don't own the funnel, you can't easily port audiences or ad accounts if the relationship ends. You're renting pipeline.</p>

<p>For most brokers, this tradeoff is worth it. But it should be a conscious choice, not an accident.</p>

<h2>The right question isn't "which is better"</h2>

<p>It's <em>"what are you actually trying to buy?"</em> If you're buying pipeline volume with known unit economics, PPL wins on every measurable metric. If you're buying long-term brand equity, retainer wins. If you need both, run both.</p>
"""

build(
    "compare/pay-per-lead-vs-retainer-agencies.html",
    "Pay Per Lead vs Retainer Agencies — Which Model Actually Delivers Pipeline?",
    "Retainers buy expertise and hope. Pay-per-lead buys units. When each makes sense, the full commercial breakdown, and the hybrid model most brokers eventually settle on.",
    body_3,
    section_label="Comparison"
)


# --- 4. AI-Qualified vs Cold Lists (REFRAMED) ---
body_4 = """
<div class="article-meta"><span>Comparison</span><span>10 min read</span><span>How modern lead qualification actually works</span></div>

<p>Most Australian brokers still think of "cold data" and "qualified leads" as two separate products. That framing is a decade out of date. The real question in 2026 isn't whether to use cold data or qualified leads — it's <strong>who is doing the qualification, and can they prove it happened.</strong></p>

<p>This piece breaks down the two ways cold data actually gets converted into a broker-ready pipeline: the legacy human-dial model, and the modern AI voice qualification model. The compliance and quality gap between them is the biggest change to Australian lead generation since the introduction of the Do Not Call Register.</p>

<h2>What cold data actually is (and isn't)</h2>

<p>A cold data list is a raw substrate — thousands of Australian contacts compiled from public records, business databases, industry registries, or purchased datasets. Cold data on its own is not a lead. It's a candidate pool.</p>

<p>Everyone in the market — every provider you're comparing, every agency, every in-house team — starts from some form of cold data. The differentiator is what happens between "raw record in a spreadsheet" and "broker-ready qualified lead in your CRM."</p>

<p>Two things can happen next: a human phones the record, or an AI voice agent phones the record. Everything downstream flows from that single choice.</p>

<h2>The legacy model — cold data + human callers</h2>

<p>Until recently, converting cold data into a qualified lead meant paying a human calling centre to dial through the list, ask a scripted set of qualification questions, tick boxes on a CRM, and hand the "qualified" record over to the broker.</p>

<p>This model has three structural weaknesses that no amount of process discipline fully fixes:</p>

<h3>The consent trail is a text note</h3>

<p>A human caller writes something like <em>"prospect confirmed interest in refinance, said yes to broker contact."</em> That note is the entire compliance record. There is no audio, no transcript, no timestamp granularity beyond when the note was saved. If ACMA ever asks for evidence that consent was properly captured, you have a text field written by an incentivised employee. That's not evidence — that's a claim.</p>

<h3>The qualification is only as honest as the human</h3>

<p>Calling centre agents are typically paid per qualified lead they produce. That creates a direct financial incentive to record ambiguous conversations as strong intent. A prospect who said "maybe, send me some info" can easily become "actively looking, ready to talk to a broker." The broker on the receiving end has no way to verify.</p>

<h3>The delivery is inconsistent</h3>

<p>Human callers have good days and bad days. Scripts get shortened when the caller is tired. Compliance disclaimers get skipped when the call is running long. Two prospects who filled the same criteria can be qualified very differently by two different agents on two different shifts.</p>

<h2>The modern model — cold data + AI voice qualification</h2>

<p>AI voice qualification replaces the human calling centre with an autonomous voice AI agent. The agent phones the prospect, holds the qualification conversation, captures explicit consent, and passes only genuinely interested prospects through as broker-ready leads.</p>

<p>The mechanics look similar on the surface. The compliance, quality, and consistency implications are radically different.</p>

<h3>Every conversation is recorded and transcribed</h3>

<p>The AI voice agent produces a full audio recording of the call plus a machine-generated transcript. Every consent confirmation is captured in the prospect's own voice, timestamped to the millisecond, tied to the phone number, and stored against the lead record. There is no "note" — there is <strong>evidence</strong>.</p>

<h3>The AI has no incentive to fake anything</h3>

<p>A voice AI is not paid per qualified lead. It doesn't hit sales targets. It doesn't have a mortgage of its own to worry about. It asks the same questions the same way every time and records the answers faithfully. A "not interested" stays as a "not interested" — because there's no human upside to marking it otherwise.</p>

<h3>Consistency is architectural, not aspirational</h3>

<p>The 500th prospect the AI qualifies on a Friday afternoon gets exactly the same script, the same disclaimers, the same consent capture flow as the first prospect Monday morning. There are no shortcuts, no bad days, no drift. Quality holds because the process is code, not people.</p>

<h2>The compliance-by-construction argument</h2>

<p>Australia's regulatory framework for outbound contact — the Privacy Act 1988, the Spam Act 2003, the Do Not Call Register scheme — assumes that the party contacting a prospect can <strong>produce evidence</strong> of consent if challenged. In a human-qualified model, that evidence is a text note. In an AI-qualified model, that evidence is a signed digital record.</p>

<p>The regulatory implications:</p>

<ul>
  <li><strong>ACMA investigations:</strong> a request for "the consent record for this phone number" can be answered in seconds — audio file, transcript, timestamp, DNCR check evidence. Everything a regulator would demand, produced without a human digging through call notes.</li>
  <li><strong>OAIC privacy complaints:</strong> the prospect's own voice confirming they agreed to be contacted eliminates ambiguity. Complaints resolve faster and with less exposure.</li>
  <li><strong>ASIC audits of lead-source practices:</strong> for regulated advice (mortgage, financial planning, insurance), being able to demonstrate that leads reached your business through a documented, consistent, non-coercive consent process is exactly what ASIC's general conduct obligation expects.</li>
</ul>

<div class="callout"><p>The compliance advantage of AI qualification is not that it's harder to breach the rules — it's that when questions come up, the answer is a file, not a story.</p></div>

<h2>Side-by-side on what actually matters</h2>

<table>
<thead>
<tr><th>Attribute</th><th>Cold data + human dial</th><th>Cold data + AI voice qualification</th></tr>
</thead>
<tbody>
<tr><td>Consent evidence format</td><td>Text note</td><td>Audio + transcript + timestamp</td></tr>
<tr><td>Auditability</td><td>Claim-based</td><td>Evidence-based</td></tr>
<tr><td>Consistency across shifts</td><td>Variable</td><td>Uniform</td></tr>
<tr><td>Incentive to overstate intent</td><td>High (paid per lead)</td><td>None</td></tr>
<tr><td>Retrieval time for a compliance request</td><td>Hours or days</td><td>Seconds</td></tr>
<tr><td>DNCR check at qualification</td><td>Manual, often skipped under time pressure</td><td>Automated, always performed</td></tr>
<tr><td>Speed to first qualified lead</td><td>Days (waiting on human capacity)</td><td>Hours</td></tr>
<tr><td>Scaling curve</td><td>Linear — needs more humans</td><td>Non-linear — capacity is infrastructure</td></tr>
</tbody>
</table>

<h2>Why "AI-qualified" has been diluted as a term</h2>

<p>Because the phrase carries weight, plenty of operators have started calling everything they do "AI-qualified" when the AI content is minimal. To separate real from marketing, it helps to know what the term should mean.</p>

<h3>What it should not mean</h3>

<p>A rules engine that scores prospects against criteria before they're phoned by a human is not AI qualification. That's just filtering. It's useful, but it's not what most brokers hear when they see "AI-qualified" on a supplier's website.</p>

<h3>What it should mean</h3>

<p>An autonomous voice AI agent holds a real conversation with the prospect, captures consent in the prospect's own voice, records the interaction end-to-end, and only forwards leads that meet the agreed criteria. Audio, transcript, and structured data all attached to the lead record. That's what qualification means when the label is accurate.</p>

<h2>How LeadEvolution runs the model</h2>

<p>We source targeted data from Australian business databases and consumer registries. Our proprietary AI voice qualification system then dials each prospect, conducts a short scripted conversation, and either:</p>

<ul>
  <li><strong>Passes them to a broker as a qualified lead</strong> — with full audio, transcript, DNCR check timestamp, and structured qualification data attached — <em>or</em></li>
  <li><strong>Politely closes the conversation</strong> without ever creating a "lead" that shouldn't exist</li>
</ul>

<p>Every qualified lead delivered to a broker carries its own audit trail. If any prospect later disputes consent, the recording answers the question. If ACMA asks how a specific number ended up being contacted, the record is one query away. That's the whole point.</p>

<h2>When cold data alone still makes sense</h2>

<p>Two cases where <strong>unqualified</strong> cold data lists remain a legitimate purchase:</p>

<ul>
  <li><strong>Direct mail campaigns.</strong> Mail doesn't fall under DNCR. If you're posting physical letters, cold data is the right substrate.</li>
  <li><strong>B2B email nurture with proper opt-in flow.</strong> Cold data can seed an outbound sequence that begins with a low-pressure email inviting the prospect to opt themselves in. Works for B2B, not consumer.</li>
</ul>

<p>Outside these cases — particularly for consumer verticals like mortgage, insurance, solar, and financial advice — cold data lists dialled directly by humans in 2026 sit on the wrong side of every trend line in Australian consumer regulation. The market is moving to AI voice qualification precisely because the compliance and quality math has become one-sided.</p>

<h2>The bottom line</h2>

<p>Cold data + human dial is a legacy model with structural compliance weaknesses that no amount of process discipline eliminates. Cold data + AI voice qualification is a modern model with the audit trail built into the architecture.</p>

<p>For any broker whose business depends on defensible pipeline hygiene — and in 2026 that's every broker — the AI-qualified model is not just faster or cheaper, it's <em>the</em> model that survives regulatory scrutiny.</p>
"""

build(
    "compare/ai-qualified-vs-cold-lists.html",
    "AI Voice Qualification vs Human-Dialled Cold Lists — Compliance & Quality Reality",
    "Cold data + human dial is the legacy model. Cold data + AI voice qualification is compliance by construction. Full breakdown for Australian brokers evaluating lead sources.",
    body_4,
    section_label="Comparison"
)


# ========================================================================
# BUYER GUIDES
# ========================================================================

# --- 5. How to Choose a Lead Provider ---
body_5 = """
<div class="article-meta"><span>Guide</span><span>12 min read</span><span>12-point evaluation checklist</span></div>

<p>Australian broker lead-generation is a crowded, opaque market. Providers oversell, contracts hide the important terms in appendices, and reference clients get quietly rotated as churn works its way through. This guide is the checklist we'd want any broker to run through <em>before</em> signing anything — whether they end up with us or with a competitor.</p>

<h2>Why choosing badly is expensive</h2>

<p>The direct cost of a bad supplier is the fee you paid. The indirect costs are much larger:</p>

<ul>
  <li>Broker time spent chasing dead numbers</li>
  <li>CRM data pollution that misleads future decisions</li>
  <li>Compliance exposure from bad consent chains</li>
  <li>Team morale damage — nothing torches confidence faster than working a broken list</li>
  <li>Opportunity cost of the pipeline you didn't build in that period</li>
</ul>

<p>A three-month engagement with the wrong provider can set a brokerage back two quarters. The checklist below is designed to catch red flags before you sign.</p>

<h2>The 12 questions to ask before signing anything</h2>

<h3>1. Where do you source your leads?</h3>

<p>You want a specific answer, not a wave of the hand toward "our proprietary network." Legitimate providers can tell you: <em>we run consented conversations with data sourced from X, filtered through Y, then qualified via Z.</em> If the answer is vague, the sourcing is usually something you wouldn't want on your compliance file.</p>

<h3>2. Are leads exclusive or shared?</h3>

<p>Straight yes/no. If shared, how many buyers per lead? If exclusive, is that written into the contract? Ask to see the specific clause.</p>

<h3>3. How is consent captured, and in what format is the evidence stored?</h3>

<p>Two questions really. First, the mechanism: is it a checkbox on a landing page, an SMS confirmation, a human phone call, or an AI voice qualification? Second, the evidence format: text notes, or audio + transcript + timestamp?</p>

<p>The strongest possible answer is <strong>AI voice qualification with full audio recording + machine-generated transcript + DNCR check timestamp attached to every lead record</strong>. That gives you immutable evidence in the prospect's own voice, retrievable in seconds if a regulator ever asks. Weaker consent formats — form checkboxes, blanket clauses, "we noted the call" — become expensive when challenged.</p>

<p>Ask the provider to walk you through what happens if you request the consent record for a specific lead delivered 30 days ago. If they can produce audio and transcript in under 60 seconds, you're dealing with a serious operator. If they need "a few days to check with the calling team," you're not.</p>

<h3>4. Are leads DNCR-checked at delivery?</h3>

<p>Not "at signup." At delivery. The DNCR is a live register — a lead qualified two months ago and DNCR-cleared then may be on the register today.</p>

<h3>5. What's the replacement policy?</h3>

<p>Every provider will have one. The question is what triggers it. Wrong number? Fair. Not interested when called? Usually not. Turned out to be already sold elsewhere? Absolutely yes. Get the specifics in writing.</p>

<h3>6. What volume can you deliver, consistently?</h3>

<p>The word to focus on is "consistently." Any provider can burst 100 leads in a week. Very few can deliver 25 leads a week for six months without dropping quality. Ask for their consistency stats.</p>

<h3>7. What's the average delivery time from sign-off to first lead?</h3>

<p>Under 48 hours is good. Under 72 hours is acceptable. Anything over a week suggests they're building the campaign after you paid, which is not what "pay per lead" is supposed to mean.</p>

<h3>8. Can I pause or stop without penalty?</h3>

<p>Real PPL should have no lock-in. If the provider requires notice periods, minimums, or spend commitments, the model is closer to a retainer with per-lead billing dressing.</p>

<h3>9. How do you handle quality complaints?</h3>

<p>Ask them to describe the process. Providers who take quality seriously will describe a specific ticket-based process with response SLAs. Providers who don't will say "we sort it out on a case-by-case basis" — code for "we hope you forget."</p>

<h3>10. Can I speak to two current clients before signing?</h3>

<p>This is the single highest-signal question in the entire process. Providers with genuinely happy clients can produce them in a day. Providers with churning client bases will stall for a week and eventually produce a hand-picked friend of the founder.</p>

<h3>11. How do you handle data delivery integration?</h3>

<p>CRM push, email, spreadsheet — what's their preference and how flexible are they? A provider that only supports email delivery in 2026 is telling you they haven't invested in their operations. That will show up in every other part of the relationship.</p>

<h3>12. What happens to my data if the relationship ends?</h3>

<p>Two questions actually. First, do they delete any records they hold about your business (client list, delivery history)? Second, do they retain the right to re-sell the same prospects to someone else after you paid to develop the relationship? The second one matters more than most brokers realise.</p>

<h2>The red flags that should end the conversation</h2>

<p>If any of the following come up in a sales call, walk away:</p>

<ul>
  <li>They quote a "guaranteed conversion rate" — no honest provider promises what happens after the lead reaches you</li>
  <li>They can't name a compliance officer or explain their consent process in specific terms</li>
  <li>They require an upfront setup fee — real PPL has zero setup cost</li>
  <li>They lock you into a 12-month minimum spend</li>
  <li>They refuse to share reference clients</li>
  <li>Their case studies use generic language ("a leading mortgage brokerage in Sydney") with no named client</li>
  <li>They mark up prices without a clear delivery volume commitment</li>
</ul>

<h2>The onboarding conversation you should insist on</h2>

<p>Before your first lead is delivered, you should have a real conversation covering:</p>

<ul>
  <li>Vertical-specific qualification criteria (loan amount minimum, geographic targeting, timeframe)</li>
  <li>Weekly volume — floor and ceiling</li>
  <li>Delivery method and CRM field mapping</li>
  <li>Replacement / dispute workflow</li>
  <li>Escalation contact and response SLA</li>
</ul>

<p>If your provider is willing to start delivering leads without this conversation, they're taking your money before they've done the work. Say no.</p>

<h2>What good looks like after 30 days</h2>

<p>Thirty days into a healthy PPL relationship, you should see:</p>

<ul>
  <li>Consistent lead volume within the agreed range</li>
  <li>Contact rate above 75% on delivered leads</li>
  <li>At least one replacement processed without friction</li>
  <li>Delivery format that plugs cleanly into your workflow</li>
  <li>A named account contact who responds within 24 hours</li>
</ul>

<p>If any of those are missing at the 30-day mark, raise it. If they aren't fixed by day 45, the relationship is not going to work. The best time to renegotiate or exit is early — not after you've spent six months hoping it improves.</p>
"""

build(
    "guides/how-to-choose-a-lead-provider.html",
    "How to Choose a Lead Provider — 12-Point Evaluation Checklist for Australian Brokers",
    "The 12 questions to ask before signing with any pay-per-lead provider, the red flags that should end a sales call, and what good looks like after 30 days.",
    body_5,
    section_label="Buyer's Guide"
)


# --- 6. DNCR Compliance Checklist ---
body_6 = """
<div class="article-meta"><span>Guide</span><span>10 min read</span><span>Compliance essentials</span></div>

<p>Every Australian broker who buys leads or dials outbound eventually asks the same question: <em>am I actually compliant?</em> This guide walks through the specific obligations under the Do Not Call Register scheme, the Privacy Act, the Spam Act, and ASIC conduct requirements — and lays out a checklist you can use to audit yourself.</p>

<p>This is not legal advice. It's an operational summary of what regulators expect from a lead-fed brokerage in 2026.</p>

<h2>The four regulators you need to know</h2>

<h3>ACMA — Australian Communications and Media Authority</h3>

<p>ACMA administers the Do Not Call Register (DNCR) and the Spam Act. If you phone Australian numbers or send commercial electronic messages, ACMA is your regulator.</p>

<p>Key exposure: contacting a DNCR-registered number without valid consent. Civil penalties up to $2.2 million per course of conduct for a corporation.</p>

<h3>OAIC — Office of the Australian Information Commissioner</h3>

<p>OAIC enforces the Privacy Act 1988. If you collect, hold, use, or disclose personal information, you're in scope.</p>

<p>Key exposure: unauthorised use or disclosure of personal information, or serious/repeated interference with privacy. Maximum penalty since late 2022 is the greater of $50 million, three times the value of any benefit obtained, or 30% of adjusted turnover.</p>

<h3>ASIC — Australian Securities & Investments Commission</h3>

<p>ASIC regulates financial services conduct. If you're a mortgage broker, financial adviser, insurance broker, or provide credit assistance, ASIC cares how you generate business.</p>

<p>Key exposure: general conduct obligations, best interests duty, and misleading representations during lead qualification.</p>

<h3>ACCC — Australian Competition and Consumer Commission</h3>

<p>ACCC enforces the Australian Consumer Law. If you make claims about your service that turn out to be misleading, the ACCC has jurisdiction — including for claims made during outbound lead calls.</p>

<h2>The Do Not Call Register — what actually applies to you</h2>

<h3>Who has to check the DNCR</h3>

<p>Anyone making a "telemarketing call" to an Australian number for the purpose of offering, supplying, or advertising goods or services. Mortgage brokers, financial advisers, insurance brokers, solar installers, and energy resellers are all clearly in scope.</p>

<h3>What's exempt</h3>

<p>Calls made with the "express" or "inferred" consent of the recipient. The two are not equivalent.</p>

<p><strong>Express consent</strong> is where the recipient has actively agreed to receive the call — usually a documented tick-box, a signed form, or an audio confirmation. This is what "consent-based" leads should carry.</p>

<p><strong>Inferred consent</strong> is where the relationship implies consent — for example, an existing client calling their broker. Inferred consent is much narrower than most brokers assume and does not cover unsolicited outbound to cold prospects.</p>

<h3>How long does consent last?</h3>

<p>The Do Not Call Register Act doesn't set a fixed expiry, but consent should be "recent" and "specific." A safe operating rule is: express consent is valid for the period the prospect would reasonably expect to be contacted about the product they consented to hear about. For a mortgage enquiry, that's typically 30-90 days. Beyond that, you should recheck.</p>

<h2>The Spam Act — the email/SMS side</h2>

<p>The Spam Act 2003 applies to commercial electronic messages (email, SMS, MMS, instant messaging). Three requirements:</p>

<ol>
  <li><strong>Consent.</strong> Same rules as DNCR — express or inferred.</li>
  <li><strong>Identification.</strong> The sender must be clearly identified in the message.</li>
  <li><strong>Unsubscribe.</strong> A functional, low-friction unsubscribe mechanism must be provided and honoured within 5 business days.</li>
</ol>

<p>The unsubscribe requirement is where a lot of brokers slip. Sending a follow-up email to a lead who unsubscribed from your previous message — even if you didn't realise — is a breach.</p>

<h2>The Privacy Act — the data-handling side</h2>

<p>Under the Australian Privacy Principles (APPs), anyone handling personal information must:</p>

<ul>
  <li>Only collect what's reasonably necessary (APP 3)</li>
  <li>Notify the individual how their data will be used (APP 5)</li>
  <li>Use the data only for the purpose it was collected for, unless the individual consents (APP 6)</li>
  <li>Keep the data secure (APP 11)</li>
  <li>Provide access on request (APP 12)</li>
  <li>Correct inaccurate information (APP 13)</li>
</ul>

<p>The specific compliance risk for a broker buying leads: <em>the purpose of collection.</em> If the lead was captured under a form that said "you'll be contacted about mortgage options," you can't then push them into a life insurance conversation without fresh consent.</p>

<h2>The 15-point self-audit</h2>

<p>Run this checklist against your operation quarterly.</p>

<h3>Lead sourcing</h3>

<ol>
  <li>Do I have written confirmation from every lead provider about how consent is captured?</li>
  <li>Can I produce a specific consent record for any single lead in my last 90 days of purchases?</li>
  <li>Is the lead's consent expressly for the product I'm calling them about?</li>
  <li>Is DNCR status re-checked at the point of delivery, not just at the point of qualification?</li>
</ol>

<h3>Contact operations</h3>

<ol start="5">
  <li>Do my callers identify themselves and the company name in the opening seconds of every call?</li>
  <li>Do my callers offer to send information about how the prospect's data will be handled?</li>
  <li>Do my callers stop and process unsubscribe requests immediately on request?</li>
  <li>Do I have a written script or call framework that covers the required disclosures?</li>
</ol>

<h3>Data handling</h3>

<ol start="9">
  <li>Is prospect data stored in a system with access controls appropriate to its sensitivity?</li>
  <li>Do I have a data breach response plan?</li>
  <li>Have I published a privacy policy that reflects my actual practices?</li>
  <li>Do I honour access, correction, and deletion requests within 30 days?</li>
</ol>

<h3>Governance</h3>

<ol start="13">
  <li>Have I nominated a specific person as the responsible privacy contact?</li>
  <li>Have I trained new team members on DNCR and privacy obligations in the last 12 months?</li>
  <li>Do I have documented processes for handling complaints from prospects who claim they didn't consent?</li>
</ol>

<h2>What actually happens if you get investigated</h2>

<p>ACMA investigations typically start with a complaint — either from a prospect who received an unwanted call, or from a competitor. The initial approach is a request for information. You'll be asked to produce:</p>

<ul>
  <li>The specific lead record for the phone number involved</li>
  <li>The consent record</li>
  <li>Your DNCR check evidence</li>
  <li>Your call log</li>
</ul>

<p>Providers who cannot produce these documents within the timeframe requested move quickly from "under review" to "enforcement action." The paper trail matters more than the intention.</p>

<h2>The two-minute audit test</h2>

<p>Pick any lead you called yesterday. Can you produce, in under two minutes: the consent record, the DNCR check timestamp, the source of the lead, and the call log? If yes, you're in a defensible position. If no, you have work to do — and the fix is almost always to demand better documentation from your lead provider, not to do the work yourself after the fact.</p>

<p>The gold-standard evidence for the consent side of that test is an audio recording of the prospect confirming interest and agreeing to be contacted. Providers running AI voice qualification produce this recording plus a machine-generated transcript for every single lead. Providers relying on human calling centres typically produce a text note written by the caller — which regulators treat as far weaker evidence. When you pressure-test a lead provider, always ask for the consent record in the strongest available format.</p>
"""

build(
    "guides/dncr-compliance-checklist-for-brokers.html",
    "DNCR Compliance Checklist for Australian Brokers — 15-Point Self-Audit",
    "The specific obligations under ACMA, OAIC, ASIC, and ACCC for any lead-fed brokerage. Practical 15-point self-audit and what actually happens in an investigation.",
    body_6,
    section_label="Buyer's Guide"
)


# --- 7. Lead Quality Metrics ---
body_7 = """
<div class="article-meta"><span>Guide</span><span>11 min read</span><span>For sales operations</span></div>

<p>"Quality" is the most overused word in lead generation, and the least measured. Most brokerages know their leads either "feel good" or "feel bad" this month, but can't put numbers on what changed or what to demand from a supplier.</p>

<p>This guide gives you the specific metrics that predict conversion, how to calculate each, and the benchmark ranges we see across our own delivered volume.</p>

<h2>The eight metrics that matter</h2>

<h3>1. Contact rate</h3>

<p>The percentage of delivered leads you can reach by phone within your standard attempt cadence (usually 3 attempts over 48 hours).</p>

<p>Formula: leads contacted ÷ leads delivered × 100.</p>

<p>Benchmarks:</p>
<ul>
  <li>Cold data list: 8-15%</li>
  <li>Form-fill lead: 25-45%</li>
  <li>Shared consent lead (queue position 3+): 30-50%</li>
  <li>Exclusive consent-based lead: 75-90%</li>
</ul>

<p>Contact rate is the single most predictive quality metric. If it's under 60%, no other metric matters — you can't convert what you can't reach.</p>

<h3>2. Meaningful conversation rate</h3>

<p>Of the leads you reach, the percentage where you had a conversation lasting 60+ seconds where the prospect confirmed interest.</p>

<p>Formula: meaningful conversations ÷ leads contacted × 100.</p>

<p>Benchmark for exclusive consent-based: 70-85%.</p>

<p>This metric strips out prospects who answered the phone but immediately said "I never asked for this call" — a strong signal of consent-chain issues.</p>

<h3>3. Appointment / next-step rate</h3>

<p>Of meaningful conversations, the percentage where the prospect agreed to a next step (meeting booked, application started, quote request confirmed).</p>

<p>Formula: appointments ÷ meaningful conversations × 100.</p>

<p>Benchmarks:</p>
<ul>
  <li>Mortgage: 40-60%</li>
  <li>Financial advice: 25-40% (longer sales cycle)</li>
  <li>Insurance: 30-45%</li>
  <li>Solar: 50-70% (in-home quote is a natural next step)</li>
  <li>Energy: 55-70%</li>
  <li>Commercial finance: 35-50%</li>
</ul>

<h3>4. Show rate</h3>

<p>Of appointments booked, the percentage where the prospect attends the scheduled meeting or takes the next step.</p>

<p>Formula: attended appointments ÷ booked appointments × 100.</p>

<p>Benchmark: 60-80% for genuinely interested prospects. Below 50% suggests either weak commitment at appointment-setting stage or long lag between booking and meeting.</p>

<h3>5. Application / proposal rate</h3>

<p>Of shown appointments, the percentage that convert into a formal application or proposal.</p>

<p>Benchmark varies wildly by vertical but usually 40-70% for a well-qualified pipeline.</p>

<h3>6. Settlement / conversion rate</h3>

<p>The end-to-end metric. Percentage of delivered leads that convert to a paying customer, settled loan, active policy, or installed system.</p>

<p>Benchmarks for exclusive consent-based leads:</p>
<ul>
  <li>Mortgage: 10-18%</li>
  <li>Financial advice: 8-15%</li>
  <li>Insurance: 12-20%</li>
  <li>Solar: 15-25%</li>
  <li>Energy: 25-40%</li>
  <li>Commercial finance: 10-18%</li>
</ul>

<h3>7. Cost per acquisition (CPA)</h3>

<p>Cost of leads to produce one settled customer.</p>

<p>Formula: (cost per lead × leads needed for one settlement) ÷ 1.</p>

<p>Worked example: mortgage at 15% settlement rate, $200/lead → 6.7 leads per settlement → $1,340 CPA. Against a $2,400 average commission, gross margin is $1,060.</p>

<h3>8. Average deal value</h3>

<p>Total commission or revenue earned per settled deal, including trail where relevant.</p>

<p>This is the counterweight to CPA. A $1,000 CPA is fine if average deal value is $3,000. It's a disaster if average deal value is $600.</p>

<h2>The metrics you should ignore</h2>

<p>Some numbers that get reported in the lead-gen industry are worse than useless — they distract from what actually matters.</p>

<h3>"Lead score"</h3>

<p>Vendor-defined lead scores are almost always vanity metrics. If a supplier tells you their leads are "A-grade" or "gold-tier" or "high-intent," ignore the label and ask for their contact rate and settlement rate on similar accounts. Those numbers can be verified.</p>

<h3>Volume delivered</h3>

<p>Every provider can spike volume in a good week. The question is whether they can hold volume across 12 consecutive weeks. Weekly consistency matters far more than headline monthly numbers.</p>

<h3>"Time to lead"</h3>

<p>Speed of delivery is table stakes, not a differentiator. Any competent supplier delivers within 24-72 hours. Faster than that isn't a meaningful advantage; slower than that is a red flag.</p>

<h2>How to build a monthly lead quality dashboard</h2>

<p>You need six lines in a spreadsheet. Track them weekly:</p>

<ol>
  <li>Leads delivered</li>
  <li>Leads contacted (call attempted 3 times within 48 hours)</li>
  <li>Meaningful conversations (60+ seconds, interest confirmed)</li>
  <li>Appointments booked</li>
  <li>Appointments attended</li>
  <li>Deals settled (usually reported 30-60 days later, so trailing metric)</li>
</ol>

<p>From these six lines, all the ratios above fall out. If any single week deviates significantly from the trailing four-week average, investigate. Consistent deviation across two weeks is a supplier conversation.</p>

<h2>When to fire a lead supplier</h2>

<p>Three signals in combination should trigger the conversation:</p>

<ul>
  <li>Contact rate drops below 60% for two consecutive weeks</li>
  <li>Meaningful conversation rate drops below 65% for two consecutive weeks</li>
  <li>Settlement rate on trailing 60 days falls below vertical benchmark</li>
</ul>

<p>Any one of these signals is a slow week. Any two is a conversation. All three is a supplier problem.</p>

<h2>The bottom line</h2>

<p>Lead quality is not a feeling. It's six numbers tracked weekly and compared against benchmarks. Any provider who can't produce, discuss, and improve those numbers is guessing — and so is any broker who buys leads without tracking them.</p>
"""

build(
    "guides/lead-quality-metrics-that-predict-conversion.html",
    "Lead Quality Metrics That Actually Predict Conversion — Broker Benchmarks",
    "The 8 metrics that predict whether a lead source is genuinely good or just cheap. Vertical benchmarks for contact rate, appointment rate, settlement rate, and CPA.",
    body_7,
    section_label="Buyer's Guide"
)


# --- 8. CPA vs CPL ROI Modelling ---
body_8 = """
<div class="article-meta"><span>Guide</span><span>9 min read</span><span>Financial modelling</span></div>

<p>Cost per lead is the price on the sales page. Cost per acquisition is the number that determines whether you have a business. Confusing the two — or worse, only tracking CPL — is one of the more expensive mistakes in the lead-fed brokerage world.</p>

<p>This guide walks through how to build an honest CPA model for a pay-per-lead engagement, what the sensitivity levers are, and how to translate that into a decision on which suppliers to expand with versus cut.</p>

<h2>The two numbers, defined</h2>

<h3>Cost per lead (CPL)</h3>

<p>The unit price you pay for a delivered lead, regardless of whether that lead converts to anything downstream. If a supplier charges $200 per delivered mortgage lead, your CPL is $200. Nothing else.</p>

<h3>Cost per acquisition (CPA)</h3>

<p>The total lead spend required to produce one settled customer, active policy, or installed system. If it takes 8 leads to settle 1 mortgage, your CPA is $200 × 8 = $1,600.</p>

<p>CPA is what matters. CPL is the input, but every downstream conversion assumption multiplies its effect on CPA.</p>

<h2>The CPA formula, with every variable named</h2>

<p>CPA = CPL ÷ (contact_rate × conversation_rate × appointment_rate × show_rate × application_rate × settlement_rate)</p>

<p>That looks like a lot. Most brokers collapse it to CPA = CPL ÷ overall_settlement_rate. Both are valid — the multi-variable version is more useful for diagnosing <em>where</em> a bad CPA comes from.</p>

<h2>Worked example — mortgage broker</h2>

<p>Assume:</p>
<ul>
  <li>CPL: $200</li>
  <li>Contact rate: 82%</li>
  <li>Meaningful conversation rate: 78%</li>
  <li>Appointment rate: 45%</li>
  <li>Show rate: 70%</li>
  <li>Application rate: 60%</li>
  <li>Settlement rate on applications: 65%</li>
</ul>

<p>Overall settlement rate = 0.82 × 0.78 × 0.45 × 0.70 × 0.60 × 0.65 = 7.9%.</p>

<p>CPA = $200 ÷ 0.079 = $2,532.</p>

<p>Against an average commission of $2,400 upfront + $1,800 trail (present-valued over 4 years), gross margin per settlement is $1,668. Positive, but tight.</p>

<h2>Sensitivity analysis — which lever moves CPA most?</h2>

<p>Using the example above, let's see what happens if each variable moves 10% in either direction:</p>

<table>
<thead>
<tr><th>Lever</th><th>Baseline</th><th>+10%</th><th>-10%</th><th>CPA impact of 10% swing</th></tr>
</thead>
<tbody>
<tr><td>CPL</td><td>$200</td><td>$220</td><td>$180</td><td>±$253</td></tr>
<tr><td>Contact rate</td><td>82%</td><td>90%</td><td>74%</td><td>±$253</td></tr>
<tr><td>Meaningful conversation rate</td><td>78%</td><td>86%</td><td>70%</td><td>±$253</td></tr>
<tr><td>Appointment rate</td><td>45%</td><td>50%</td><td>41%</td><td>±$253</td></tr>
<tr><td>Show rate</td><td>70%</td><td>77%</td><td>63%</td><td>±$253</td></tr>
<tr><td>Application rate</td><td>60%</td><td>66%</td><td>54%</td><td>±$253</td></tr>
<tr><td>Settlement rate</td><td>65%</td><td>72%</td><td>59%</td><td>±$253</td></tr>
</tbody>
</table>

<p>Every 10% move in any variable is worth about $253 in CPA. That looks even, but in practice some levers are much easier to move than others.</p>

<h2>Which levers you actually control</h2>

<h3>Broker-controlled levers (fastest to improve)</h3>

<ul>
  <li>Contact rate — call cadence and time-of-day discipline</li>
  <li>Appointment rate — script and objection handling</li>
  <li>Show rate — confirmation touches between booking and meeting</li>
  <li>Application rate — meeting preparation and product fit</li>
</ul>

<h3>Supplier-controlled levers</h3>

<ul>
  <li>CPL — negotiated at contract</li>
  <li>Meaningful conversation rate — a function of consent quality and prospect freshness</li>
</ul>

<h3>Uncontrollable levers</h3>

<ul>
  <li>Settlement rate on applications — depends on serviceability, lender appetite, macro rate cycle</li>
</ul>

<p>The most common trap is trying to negotiate CPL down when the real problem is contact rate — which is a supplier quality issue that discounting won't fix.</p>

<h2>The break-even calculation</h2>

<p>Every broker should know their break-even CPA — the point at which lead spend equals gross margin per settlement.</p>

<p>Break-even CPA = average deal value net of variable costs.</p>

<p>For a mortgage broker with $2,400 upfront + $1,800 present-valued trail, break-even is $4,200 CPA. Anything below that produces margin; anything above burns money.</p>

<p>Most healthy PPL engagements run at 40-60% of break-even CPA. That leaves margin for overhead, salaries, and profit.</p>

<h2>Modelling supplier tests</h2>

<p>When testing a new supplier, run the math both ways:</p>

<h3>Optimistic scenario</h3>

<p>Assume the supplier hits vertical benchmark on every metric. Calculate CPA. If this scenario is above break-even, don't test — the supplier can't ever be profitable.</p>

<h3>Realistic scenario</h3>

<p>Discount every conversion assumption by 20%. Recalculate. If this is still above 70% of break-even, the supplier has almost no margin for error.</p>

<h3>Pessimistic scenario</h3>

<p>Discount every conversion assumption by 40%. Recalculate. This is your worst-case CPA — the number that matters if you commit budget and hope you can improve conversion later.</p>

<h2>What most brokers get wrong</h2>

<p>Three consistent errors:</p>

<ul>
  <li><strong>Comparing suppliers on CPL only.</strong> A $80 supplier is not cheaper than a $200 supplier if the $80 leads have a 5% contact rate and the $200 leads have 82%. CPA is what you compare, always.</li>
  <li><strong>Not decomposing the funnel.</strong> "My CPA went up" is not diagnostic. "My contact rate dropped 15 points and my appointment rate is stable" tells you the supplier is delivering worse consent or older leads.</li>
  <li><strong>Ignoring trail value.</strong> For any vertical with trail commissions (mortgage, insurance, some financial advice), the deal value on your CPA model should be present-valued upfront + trail, not just upfront. Ignoring trail undervalues good leads and overvalues cheap ones.</li>
</ul>

<h2>The 90-day supplier review template</h2>

<p>At day 90 of any new PPL engagement, run this review with the supplier:</p>

<ol>
  <li>Actual leads delivered vs contracted volume</li>
  <li>Contact rate actual vs vertical benchmark</li>
  <li>Meaningful conversation rate actual vs benchmark</li>
  <li>Settlement rate on completed pipeline (trailing 60 days)</li>
  <li>Effective CPA vs modelled CPA</li>
  <li>Effective CPA vs break-even CPA</li>
</ol>

<p>If effective CPA is under 60% of break-even, expand volume. If it's between 60-90%, hold and optimise. If it's over 90%, either the supplier is wrong for you or your downstream sales process is wrong for the leads. Diagnose which before renewing.</p>
"""

build(
    "guides/cpa-vs-cpl-modelling-for-lead-fed-brokerages.html",
    "CPA vs CPL — How Australian Brokers Should Actually Model Lead ROI",
    "Cost per lead is a sticker price. Cost per acquisition is a business. Full modelling framework with sensitivity analysis and break-even calculation for lead-fed brokerages.",
    body_8,
    section_label="Buyer's Guide"
)


# --- 9. Building Consistent Pipeline ---
body_9 = """
<div class="article-meta"><span>Guide</span><span>11 min read</span><span>Operational playbook</span></div>

<p>Most brokers who move from cold-calling to a lead-fed model make the same mistake: they order too many leads too fast, overwhelm their capacity, burn through the pipeline in three weeks, then complain the leads "don't convert." The problem is almost never the leads. It's the cadence.</p>

<p>This guide walks through how to build a consistent, sustainable pipeline using pay-per-lead — from onboarding through to a stable weekly rhythm — and why the operators who get this right run circles around the ones who don't.</p>

<h2>The three phases of a healthy PPL engagement</h2>

<h3>Phase 1 — Calibration (weeks 1-4)</h3>

<p>The goal in the first month is <strong>not volume</strong>. It's calibration. You are learning what the supplier's leads look like, and the supplier is learning what your workflow can absorb.</p>

<p>Order a small batch — 10 to 25 leads in week one. Work them properly with your best callers, using your standard script. Track every metric from the previous guide (contact rate, conversation rate, appointment rate, application rate).</p>

<p>By end of week two you'll know: is this supplier delivering to spec, and can we scale?</p>

<h3>Phase 2 — Volume laddering (weeks 5-12)</h3>

<p>If phase 1 metrics land at or above vertical benchmark, ladder volume by 20-30% per week — not by 100%. Doubling volume in one week is the fastest way to break your team's capacity.</p>

<p>A typical ladder for a two-broker firm:</p>

<ul>
  <li>Week 1: 15 leads</li>
  <li>Week 2: 15 leads</li>
  <li>Week 3: 20 leads</li>
  <li>Week 4: 25 leads</li>
  <li>Week 5: 30 leads</li>
  <li>Week 6-8: hold at 30, monitor conversion</li>
  <li>Week 9: 35 leads</li>
  <li>Week 10-12: 40 leads</li>
</ul>

<p>By week 12 you're at 2.7x your starting volume with conversion metrics you can trust.</p>

<h3>Phase 3 — Steady state (week 13 onward)</h3>

<p>The goal now is <strong>weekly consistency</strong>. Same volume every week, delivered on the same days. Sales operations optimise around a predictable rhythm; they collapse under volatility.</p>

<h2>The weekly cadence that actually works</h2>

<p>The single most powerful operational change a broker can make is moving from ad-hoc bursts to a fixed weekly delivery pattern. Here's the cadence we see working across our clients:</p>

<h3>Monday</h3>

<p>Half the week's leads land Monday morning. Team dials them Monday-Tuesday. Fresh leads worked immediately convert at meaningfully higher rates than leads sitting in a queue.</p>

<h3>Wednesday</h3>

<p>Second half of the week's leads land Wednesday morning. Team dials Wednesday-Thursday.</p>

<h3>Friday</h3>

<p>Reserved for follow-ups on the week's non-answers and next-week appointment confirmation calls. No new lead ingestion.</p>

<p>This cadence keeps every lead worked within 48 hours of delivery — which is when consent is freshest and answer rates are highest.</p>

<h2>Capacity planning — the honest math</h2>

<p>How many leads can one broker actually work?</p>

<p>Time budget per broker per week (assuming 40-hour week):</p>

<ul>
  <li>Existing pipeline management: 12 hours</li>
  <li>Appointments (meeting + prep + follow-up): 12 hours</li>
  <li>Admin, compliance, reporting: 6 hours</li>
  <li>Available for new lead work: 10 hours</li>
</ul>

<p>At 10 minutes per lead cycle (3 dial attempts + notes + next-step booking), one broker can properly work 60 leads per week. But that's a ceiling, not a target. Sustainable long-term is closer to 40-45 leads per broker per week.</p>

<p>A two-broker firm should think of steady-state as 80-90 leads per week, not 150.</p>

<h2>The replacement policy — using it properly</h2>

<p>Every serious PPL supplier has a replacement policy for leads that don't meet spec (wrong number, DNCR-registered at delivery, criteria mismatch). Most brokers under-use this.</p>

<p>Rule of thumb: <strong>if a lead is off-spec, request a replacement within 5 business days.</strong> The paper trail matters — replace via the supplier's designated process, not by chasing the account manager over Slack.</p>

<p>Suppliers who dispute or delay replacement requests are telling you what the relationship will look like in month six. Watch for it early.</p>

<h2>Handling the "quality drop" week</h2>

<p>Every PPL engagement has weeks where quality feels off. Sometimes it's real — supplier's data pool has shifted. Sometimes it's noise — your best closer was sick that week.</p>

<p>Before raising it as a supplier issue, check three things:</p>

<ol>
  <li>Is contact rate genuinely down, or did you have a bad calling week? Compare against your own dial-attempt discipline.</li>
  <li>Is meaningful conversation rate down, or did you get a batch of first-attempt prospects who need a second touch to warm up?</li>
  <li>Is the drop concentrated in one lead type, one postcode, one time-of-day?</li>
</ol>

<p>If the drop persists across two weeks after these checks, it's a supplier conversation. If it's a single-week blip, don't over-index on it.</p>

<h2>The delivery method decision</h2>

<p>Most suppliers can deliver leads by CRM push, email, or spreadsheet. Choose based on what your team actually uses:</p>

<h3>CRM push (recommended)</h3>

<p>Leads land directly in your CRM (HubSpot, Zoho, Salesforce, Pipedrive, etc) with structured fields already mapped. No copy-paste, no lag, no formatting errors. This is the fastest to work and the least error-prone.</p>

<h3>Email</h3>

<p>Fine for small volume, terrible at scale. Every lead requires manual entry into your system. Introduces lag between delivery and first dial. Choose this only if you can't integrate a CRM push.</p>

<h3>Spreadsheet</h3>

<p>Batch delivery once per day or once per week. Simple for suppliers, terrible for lead freshness — a lead sitting in a spreadsheet for 24 hours before your team sees it is 24 hours less consent freshness. Only choose this if your workflow genuinely requires batch processing.</p>

<h2>The dashboards that keep engagements healthy</h2>

<p>You need two views:</p>

<h3>Weekly operations dashboard</h3>

<p>Six numbers, updated every Friday: leads delivered, leads contacted, meaningful conversations, appointments booked, appointments attended, and current-week pipeline value.</p>

<h3>Monthly commercial dashboard</h3>

<p>Trailing 60-day view: settlement rate, average deal value, actual CPA, actual CPA vs break-even, and margin generated.</p>

<p>The weekly dashboard drives operational decisions (scale up, hold, or escalate to supplier). The monthly dashboard drives commercial decisions (renew, expand, cut, or renegotiate).</p>

<h2>The 12-month view</h2>

<p>A brokerage that runs disciplined PPL for a full year looks different from one that runs bursts:</p>

<ul>
  <li>Weekly settlement volume is predictable within ±15%</li>
  <li>Broker productivity metrics are stable</li>
  <li>Compliance file is clean and audit-ready</li>
  <li>Revenue forecasts are trustworthy</li>
  <li>The team can be scaled by adding brokers, not by scrambling for leads</li>
</ul>

<p>That predictability is the entire point. Cheap lead bursts feel exciting. Consistent pipeline feels boring. Boring is what wins.</p>
"""

build(
    "guides/building-consistent-pipeline-with-pay-per-lead.html",
    "Building a Consistent Sales Pipeline with Pay Per Lead — Operational Playbook",
    "How Australian brokers actually build a stable, compounding pipeline using pay per lead. Volume laddering, weekly cadence, capacity math, and the dashboards that keep it healthy.",
    body_9,
    section_label="Buyer's Guide"
)


# ========================================================================
# HOW WE QUALIFY — dedicated authority page
# ========================================================================

body_10 = """
<div class="article-meta"><span>Our Process</span><span>Every lead, every time</span></div>

<p>Every broker who has ever bought leads eventually asks the same question: <em>how do you actually decide who gets forwarded to me?</em> This page is the honest, end-to-end walkthrough of how LeadEvolution qualifies each lead we deliver — the technology, the audit trail, and the reason we built the model this way.</p>

<h2>Why we built an AI voice qualification system</h2>

<p>When we started LeadEvolution, we spent time inside the two dominant lead-generation models: human-dialled cold data and form-fill funnels. Both had the same fundamental weakness — the "qualification" attached to each lead was <strong>a claim</strong> rather than <strong>evidence</strong>. A calling agent noted the prospect was interested; a landing page recorded a checkbox click. If a regulator or an unhappy prospect ever asked "what actually happened here?", the answer was a story, not a record.</p>

<p>We built our qualification model to eliminate that gap. Every lead we deliver comes with an <strong>immutable, replayable audit trail</strong> — the prospect's own voice confirming interest, a machine-generated transcript, a timestamped DNCR check, and structured qualification fields captured in real time. Not because it's convenient. Because it's the only way we can hand a broker a lead and say <em>this is genuine, and here is the proof.</em></p>

<h2>The four-step qualification process</h2>

<h3>Step 1 — Sourcing the candidate pool</h3>

<p>We work from targeted Australian datasets — business databases, industry registries, consumer datasets — filtered against the criteria you agreed during onboarding (state, postcode, product category, deal-size band, timeframe). No lead ever enters qualification without matching your defined targeting. This step is deliberately narrow: better to qualify 100 well-matched prospects than 1,000 loosely-matched ones.</p>

<h3>Step 2 — AI voice qualification call</h3>

<p>Our proprietary AI voice qualification system dials each prospect in the candidate pool and conducts a live phone conversation. The agent introduces itself, explains who LeadEvolution is, describes the type of specialist that would be contacting them, and asks the qualification questions relevant to your vertical (e.g. for mortgage: loan purpose, estimated amount, timeframe, current situation).</p>

<p>The call is recorded from start to finish. A machine-generated transcript is produced automatically. The recording, transcript, and timestamped structured data are stored against the prospect's record — regardless of whether they qualify or not.</p>

<h3>Step 3 — Consent capture and DNCR verification</h3>

<p>If the prospect confirms interest, the AI voice agent captures explicit consent — in the prospect's own voice — to be contacted by a specialist within an agreed timeframe. The consent statement is standardised, unambiguous, and clearly identifies LeadEvolution as the source and the broker's vertical as the destination.</p>

<p>Simultaneously, the prospect's phone number is checked against the current Do Not Call Register. If the check fails, the lead is discarded regardless of what was said on the call. If it passes, the DNCR-clear status is recorded with a timestamp.</p>

<h3>Step 4 — Delivery to the broker</h3>

<p>Only prospects who confirmed interest, provided consent, and cleared DNCR are delivered as leads. Each qualified lead arrives in your chosen format — CRM push, email, or spreadsheet — with the full structured data record attached: name, phone, email, vertical-specific qualification fields, consent timestamp, DNCR check timestamp, and delivery time.</p>

<p>The underlying audio recording and transcript remain on file. Any lead can be pulled up and replayed on demand.</p>

<h2>What every qualified lead includes</h2>

<p>A LeadEvolution qualified lead carries more evidence than most brokers realise. Every record includes:</p>

<ul>
  <li><strong>Contact fields:</strong> full name, mobile number, email address, postcode</li>
  <li><strong>Vertical-specific qualification data:</strong> loan amount for mortgage, coverage type for insurance, system size interest for solar, deal size for commercial finance, and so on</li>
  <li><strong>Timeframe indication:</strong> ready now, 1–3 months, 3–6 months, longer horizon</li>
  <li><strong>Consent record:</strong> audio recording of the prospect's own voice confirming interest and agreeing to be contacted</li>
  <li><strong>Transcript:</strong> machine-generated text version of the qualification call for search and audit</li>
  <li><strong>Timestamps:</strong> when the call happened, when consent was given, when DNCR was checked, when the lead was delivered to you</li>
  <li><strong>Source trail:</strong> which dataset the prospect originated from, ensuring you can trace the full journey</li>
</ul>

<h2>The compliance advantage — why the audit trail matters</h2>

<p>Australia's regulatory environment for outbound lead generation has three main players: <strong>ACMA</strong> (the Do Not Call Register and Spam Act), <strong>OAIC</strong> (the Privacy Act), and <strong>ASIC</strong> (financial services conduct). All three assume that any party contacting a prospect can produce evidence — not narrative — that consent was properly obtained.</p>

<p>Under a human-qualified lead model, that evidence is a text note in a CRM. Under our AI voice qualification model, that evidence is:</p>

<ul>
  <li>An audio recording of the prospect saying, in their own voice, that they wanted to be contacted</li>
  <li>A machine-generated transcript of the full conversation</li>
  <li>A millisecond-accurate timestamp of when consent was given</li>
  <li>A DNCR check performed at qualification and stored with the record</li>
</ul>

<p>If an ACMA investigator ever asks "produce the consent record for this phone number," we can retrieve it in seconds. Not "we called and the caller wrote that consent was given" — but "here is the audio, here is the transcript, here is the timestamp, here is the DNCR check receipt." That's what defensible looks like.</p>

<div class="callout"><p>The audit trail is not something we bolt on afterwards for compliance appearances. It's the byproduct of running qualification through a voice AI instead of a human calling centre. The evidence exists because the process is architecturally designed to produce it.</p></div>

<h2>Why AI qualification is more honest than human qualification</h2>

<p>The unintuitive thing about AI voice qualification is that it produces <em>more truthful</em> leads than a human calling centre would. Three reasons:</p>

<h3>No incentive to overstate</h3>

<p>A human calling agent is typically paid per qualified lead they produce. That creates a financial incentive to nudge ambiguous conversations toward "qualified." An AI voice agent has no such incentive. A "maybe" stays a "maybe." A "not interested" stays a "not interested." The lead-classification bias that exists in human calling operations simply doesn't exist in the AI model.</p>

<h3>No shortcuts under time pressure</h3>

<p>Human callers under quota pressure will skip disclaimers, abbreviate scripts, or hurry through consent language. AI voice qualification runs the full compliant script on every call regardless of volume. The 500th call of the day is identical to the first.</p>

<h3>No memory of the last call</h3>

<p>A human caller who just had a difficult conversation can carry frustration into the next call. AI voice qualification approaches every prospect fresh. There's no fatigue-driven variability in how prospects are treated.</p>

<h2>What we don't do</h2>

<p>The best way to explain a qualification model is often by describing what it isn't. LeadEvolution doesn't:</p>

<ul>
  <li><strong>Sell shared leads.</strong> Every qualified lead is delivered to one broker only. It is never resold, resupplied, or added to a common pool.</li>
  <li><strong>Use form-fill funnels.</strong> Landing-page checkbox consent is not consent. We source prospects through voice conversations, not landing pages.</li>
  <li><strong>Use human calling centres for qualification.</strong> The qualification call is always run by our AI voice system. Humans are involved in campaign design, quality assurance, and client management — not in the qualification call itself.</li>
  <li><strong>Push volume ahead of quality.</strong> If a week's candidate pool doesn't produce enough genuinely interested prospects, we deliver fewer leads that week rather than lowering the qualification bar. Consistency comes from operational discipline, not from padding.</li>
  <li><strong>Charge for leads that don't meet spec.</strong> Every delivered lead is against your defined criteria. Where an edge case slips through, our replacement policy applies and no invoice attaches.</li>
</ul>

<h2>What this means for you</h2>

<p>Working with a lead source that runs AI voice qualification changes three things about your pipeline economics:</p>

<h3>Contact and conversion rates are higher</h3>

<p>Because every prospect explicitly consented to a specialist call — in a live voice conversation, not a checkbox — they answer when you call, they remember why they're expecting to hear from you, and they engage in the conversation. Contact rates on our leads typically sit in the 75–90% range, versus 25–45% on form-fill leads and 8–15% on human-dialled cold data.</p>

<h3>Your compliance file is clean without extra work</h3>

<p>You don't need to build a separate consent-evidence workflow. Every lead we deliver arrives with the compliance artefact already attached. If a prospect ever disputes consent, or a regulator ever asks, the answer is one query away.</p>

<h3>Your CRM stays healthy</h3>

<p>Because we don't inflate qualification to hit lead-count targets, the leads that land in your pipeline are ones you can actually work. Fewer "why did you send me this?" moments, cleaner reporting, more useful trailing-conversion analysis. The signal-to-noise ratio of a well-run PPL pipeline is one of the highest-leverage improvements a broker's operations team can make.</p>

<h2>How to see it in action</h2>

<p>The fastest way to understand the model is to onboard onto a small trial — usually 10 to 25 leads across your first two weeks. During that trial you'll see the leads land in your CRM (or email, or spreadsheet), you'll work them through your normal sales process, and you can request the audio recording of the consent capture for any lead delivered. If the model works for your operation, we scale volume from there. If it doesn't, we part on good terms with no lock-in.</p>

<p>Tell us your vertical, your target volume, and your delivery preference. We'll come back to you inside one business day with a plan.</p>
"""

build(
    "how-we-qualify.html",
    "How LeadEvolution Qualifies Every Lead — AI Voice Qualification Process",
    "Every LeadEvolution lead is qualified by our AI voice system, with full audio, transcript, DNCR timestamp and structured data attached. The end-to-end process, explained.",
    body_10,
    section_label="Our Process"
)

# Fix: /how-we-qualify.html is at root, not subfolder — regenerate with root-relative asset paths
import re as _re
root_page = ROOT / "how-we-qualify.html"
if root_page.exists():
    c = root_page.read_text(encoding="utf-8")
    c = c.replace('href="../styles.css"', 'href="styles.css"')
    c = c.replace('href="../index.html"', 'href="index.html"')
    c = c.replace('href="../verticals/', 'href="verticals/')
    c = c.replace('href="../faq.html"', 'href="faq.html"')
    c = c.replace('href="../team.html"', 'href="team.html"')
    c = c.replace('href="../contact.html"', 'href="contact.html"')
    c = c.replace('href="../resources.html"', 'href="resources.html"')
    c = c.replace('href="../terms.html"', 'href="terms.html"')
    c = c.replace('href="../privacy.html"', 'href="privacy.html"')
    c = c.replace('src="../main.js', 'src="main.js')
    root_page.write_text(c, encoding="utf-8")
    print("[✓] fixed root-relative asset paths in how-we-qualify.html")

print("\n[DONE] all 4 comparison + 5 guide pages + how-we-qualify built")
