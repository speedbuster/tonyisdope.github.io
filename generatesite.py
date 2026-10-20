import itertools
import urllib.parse
import os

# 1. Load Master HTML Template
template_path = 'template.html'
if not os.path.exists(template_path):
    print("Error: template.html not found!")
    exit()

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# 2. Define Standalone Landing & Core Pages
standalone_pages = [
    {
        "slug": "facebook-ads-landing-page",
        "title": "Meta & Facebook Ads Agency | TIDA Ltd",
        "description": "High-ROI Facebook and Instagram advertising services by TIDA Ltd.",
        "badge": "Paid Traffic Management",
        "heading": "Meta & Facebook Ads Management",
        "subheading": "Hyper-targeted campaigns built to acquire customers and scale revenue predictably.",
        "target_market": "High-Growth Brands"
    },
    {
        "slug": "google-ads-landing-page",
        "title": "Google Ads & PPC Management | TIDA Ltd",
        "description": "Capture high-intent search traffic with expert Google Ads management.",
        "badge": "PPC Advertising",
        "heading": "Google Ads & Search PPC Management",
        "subheading": "Capture ready-to-buy search traffic and scale high-intent customer acquisition.",
        "target_market": "B2B & Service Brands"
    },
    {
        "slug": "digital-strategy-landing-page",
        "title": "Sales Funnel Architecture & Digital Strategy | TIDA Ltd",
        "description": "Custom sales funnel architecture and landing page setups by TIDA Ltd.",
        "badge": "Conversion Architecture",
        "heading": "Sales Funnel Setup & Digital Strategy",
        "subheading": "High-converting sales funnels designed to turn cold clicks into predictable clients.",
        "target_market": "Enterprise Brands"
    },
    {
        "slug": "digital-marketing-agency-port-harcourt",
        "title": "Digital Marketing Agency in Port Harcourt | TIDA Ltd",
        "description": "Top-tier performance marketing and lead generation agency headquartered in Port Harcourt, Nigeria.",
        "badge": "Port Harcourt Headquarters",
        "heading": "Digital Marketing Agency in Port Harcourt",
        "subheading": "Driving explosive growth, customer acquisition, and high-ROI ad funnels for brands in Port Harcourt and across Nigeria.",
        "target_market": "Port Harcourt & Rivers State"
    },
    {
        "slug": "digital-marketing-agency-lagos",
        "title": "Digital Marketing Agency in Lagos | TIDA Ltd",
        "description": "Leading growth marketing and performance agency scaling brands across Lagos, Nigeria.",
        "badge": "Lagos Hub",
        "heading": "Digital Marketing Agency in Lagos",
        "subheading": "Enterprise performance marketing, Meta ads, and custom sales funnels built for scaling Lagos businesses.",
        "target_market": "Lagos & Victoria Island"
    }
]

print("Generating standalone core and landing pages...")
for page in standalone_pages:
    try:
        html_content = template
        html_content = html_content.replace("{{TITLE}}", page["title"])
        html_content = html_content.replace("{{DESCRIPTION}}", page["description"])
        html_content = html_content.replace("{{SLUG}}", page["slug"])
        html_content = html_content.replace("{{BADGE}}", page["badge"])
        html_content = html_content.replace("{{HEADING}}", page["heading"])
        html_content = html_content.replace("{{SUBHEADING}}", page["subheading"])
        html_content = html_content.replace("{{TARGET_MARKET}}", page["target_market"])
        html_content = html_content.replace("{{ENCODE_TITLE}}", urllib.parse.quote(page["heading"]))

        filename = f"{page['slug']}.html"
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(html_content)
    except Exception as e:
        print(f"Error generating landing page {page['slug']}: {e}")

# 3. Define 30 Services
services = [
    {"name": "Meta Ads Management", "slug": "meta-ads-agency", "heading": "Meta Ads Agency"},
    {"name": "Google PPC Agency", "slug": "google-ppc-agency", "heading": "Google PPC Agency"},
    {"name": "Sales Funnel Architecture", "slug": "sales-funnel-architects", "heading": "Sales Funnel Architecture"},
    {"name": "B2B Lead Generation", "slug": "b2b-lead-generation", "heading": "B2B Lead Generation Agency"},
    {"name": "E-Commerce Scaling", "slug": "ecommerce-scaling", "heading": "E-Commerce Scaling Agency"},
    {"name": "Conversion Rate Optimization", "slug": "cro-agency", "heading": "CRO & Funnel Optimization"},
    {"name": "Meta CAPI Setup", "slug": "meta-capi-tracking", "heading": "Server-Side Meta CAPI Tracking"},
    {"name": "Local SEO Optimization", "slug": "local-seo-agency", "heading": "Local SEO Optimization"},
    {"name": "Instagram & TikTok Ads", "slug": "social-ads-agency", "heading": "Instagram & TikTok Ad Agency"},
    {"name": "Agency White-Label Services", "slug": "white-label-agency", "heading": "White-Label Agency Services"},
    {"name": "Multi-Channel Attribution", "slug": "attribution-tracking", "heading": "Multi-Channel Attribution Setup"},
    {"name": "Programmatic Display Ads", "slug": "programmatic-display", "heading": "Programmatic Display Agency"},
    {"name": "CRM Automation Workflows", "slug": "crm-automation", "heading": "CRM Automation & Lead Nurturing"},
    {"name": "Performance Creative Testing", "slug": "creative-testing", "heading": "Performance Creative Testing"},
    {"name": "WhatsApp Marketing Funnels", "slug": "whatsapp-marketing", "heading": "WhatsApp Sales Funnel Agency"},
    {"name": "Enterprise GA4 & GTM Setup", "slug": "ga4-gtm-analytics", "heading": "Enterprise GA4 & GTM Analytics"},
    {"name": "SaaS Growth Marketing", "slug": "saas-growth-marketing", "heading": "SaaS Growth Marketing Agency"},
    {"name": "Fintech User Acquisition", "slug": "fintech-user-acquisition", "heading": "Fintech User Acquisition Agency"},
    {"name": "Real Estate Digital Marketing", "slug": "real-estate-marketing", "heading": "Real Estate Digital Marketing"},
    {"name": "Oil & Gas B2B Marketing", "slug": "oil-gas-marketing", "heading": "Oil & Gas B2B Marketing Agency"},
    {"name": "AI Lead Qualification", "slug": "ai-lead-qualification", "heading": "AI Lead Qualification & Chatbot Agency"},
    {"name": "LinkedIn B2B Advertising", "slug": "linkedin-ads-agency", "heading": "LinkedIn B2B Advertising Agency"},
    {"name": "YouTube Video Funnels", "slug": "youtube-video-funnels", "heading": "YouTube Video Ads & Funnel Agency"},
    {"name": "Email Marketing Automation", "slug": "email-automation-agency", "heading": "Klaviyo & ActiveCampaign Agency"},
    {"name": "High-Ticket Closing Funnels", "slug": "high-ticket-funnels", "heading": "High-Ticket Sales Funnel Agency"},
    {"name": "Programmatic SEO Agency", "slug": "programmatic-seo-agency", "heading": "Programmatic SEO & Content Scale"},
    {"name": "Influencer Whitelisting Ads", "slug": "influencer-whitelisting", "heading": "Creator Whitelisting & Spark Ads"},
    {"name": "App Install Campaigns", "slug": "app-install-agency", "heading": "Mobile App Install & UA Agency"},
    {"name": "B2B Demand Generation", "slug": "demand-generation-agency", "heading": "B2B Demand Generation Agency"},
    {"name": "Full-Funnel Media Buying", "slug": "full-funnel-media-buying", "heading": "Full-Funnel Media Buying Agency"}
]

# 4. Define 20 Industries
industries = [
    {"name": "Luxury Real Estate", "slug": "real-estate", "heading": "Luxury Real Estate & PropTech"},
    {"name": "Upstream Oil & Gas", "slug": "oil-and-gas", "heading": "Upstream Oil & Gas & Energy Services"},
    {"name": "Fintech & Neobanks", "slug": "fintech", "heading": "Fintech, Neobanks & Payment Gateways"},
    {"name": "B2B SaaS & Tech Startups", "slug": "saas", "heading": "B2B SaaS & Cloud Software"},
    {"name": "Global Logistics & Shipping", "slug": "logistics", "heading": "Global Logistics & Maritime Freight"},
    {"name": "Renewable Energy & Solar", "slug": "renewable-energy", "heading": "Renewable Energy & Clean Tech"},
    {"name": "E-Commerce & D2C Brands", "slug": "ecommerce", "heading": "High-Growth E-Commerce & D2C Brands"},
    {"name": "Healthcare & MedTech", "slug": "healthcare", "heading": "Private Healthcare & MedTech Clinics"},
    {"name": "Mining & Natural Resources", "slug": "mining", "heading": "Mining, Minerals & Heavy Industry"},
    {"name": "Enterprise B2B Consulting", "slug": "consulting", "heading": "Enterprise B2B Consulting & Advisory"},
    {"name": "Legal & Corporate Services", "slug": "legal-services", "heading": "Corporate Law Firms & Legal Advisory"},
    {"name": "EdTech & Online Academies", "slug": "edtech", "heading": "EdTech Platforms & E-Learning Academies"},
    {"name": "AgriTech & Agribusiness", "slug": "agritech", "heading": "AgriTech & Commercial Agribusiness"},
    {"name": "Hospitality & Luxury Hotels", "slug": "hospitality", "heading": "Luxury Hospitality & Resort Chains"},
    {"name": "Cybersecurity & IT Infrastructure", "slug": "cybersecurity", "heading": "Enterprise Cybersecurity & Managed IT"},
    {"name": "Automotive & Fleet Management", "slug": "automotive", "heading": "Commercial Automotive & Fleet Logistics"},
    {"name": "Venture Capital & Private Equity", "slug": "venture-capital", "heading": "Venture Capital & Private Equity Portfolios"},
    {"name": "Marine & Offshore Engineering", "slug": "marine-engineering", "heading": "Marine & Offshore Engineering Contractors"},
    {"name": "Biotech & Pharmaceutical", "slug": "biotech", "heading": "Biotech Laboratories & Pharma Distributors"},
    {"name": "Commercial Aviation & Aerospace", "slug": "aviation", "heading": "Commercial Aviation & Aerospace Services"}
]

# 5. Define 500 Global Markets Programmatically
base_cities = [
    ("Port Harcourt", "ph"), ("Lagos", "lagos"), ("Abuja", "abuja"), ("London", "london"), 
    ("New York", "ny"), ("Toronto", "toronto"), ("Dubai", "dubai"), ("Johannesburg", "joburg"),
    ("Nairobi", "nairobi"), ("Accra", "accra"), ("Singapore", "singapore"), ("Sydney", "sydney"),
    ("Berlin", "berlin"), ("Paris", "paris"), ("Tokyo", "tokyo"), ("Hong Kong", "hk"),
    ("Houston", "houston"), ("Atlanta", "atlanta"), ("Chicago", "chicago"), ("Montreal", "montreal")
]
districts = ["Central", "North", "South", "East", "West", "Downtown", "Metro", "Industrial", "Tech Hub", "Financial District", 
             "Commercial Zone", "Harbor", "Bay", "Heights", "Valley", "Plaza", "Airport Hub", "Energy Zone", "Free Zone", "Suburbs",
             "Phase 1", "Phase 2", "GRA", "Expressway", "Boulevard", "Waterfront", "Innovation Hub", "Export Zone", "Terminal", "Cove"]

locations = []
for city, slug_prefix in base_cities:
    for d in districts:
        locations.append({
            "name": f"{d} {city}",
            "slug": f"{slug_prefix}-{d.lower().replace(' ', '-')}",
            "market": f"{d} {city}"
        })
locations = locations[:500]

print(f"Generating enterprise programmatic matrix: {len(services)} services * {len(locations)} locations * {len(industries)} industries = {len(services)*len(locations)*len(industries):,} programmatic pages...")

pages_data = []
for s, l, i in itertools.product(services, locations, industries):
    slug = f"{s['slug']}-{i['slug']}-{l['slug']}"
    title = f"{s['name']} for {i['name']} in {l['name']} | TIDA Ltd"
    description = f"Drive verified revenue and scale customer acquisition for {i['name']} brands in {l['name']} with expert {s['name']} by TIDA Ltd."
    badge = i['heading']
    heading = f"{s['heading']} for {i['name']} in {l['name']}"
    subheading = f"Scale your {i['name']} operations across {l['name']} with enterprise-grade ad architectures and automated sales funnels built by TIDA Ltd."
    target_market = l['market']
    
    pages_data.append({
        "slug": slug, "title": title, "description": description, 
        "badge": badge, "heading": heading, "subheading": subheading, "target_market": target_market
    })

print(f"Total compiled enterprise pages: {len(pages_data):,}. Writing files to disk and generating modular sitemaps...")

# 6. High-Speed Batch File Generation
success_count = 0
for page in pages_data:
    try:
        html_content = template
        html_content = html_content.replace("{{TITLE}}", page["title"])
        html_content = html_content.replace("{{DESCRIPTION}}", page["description"])
        html_content = html_content.replace("{{SLUG}}", page["slug"])
        html_content = html_content.replace("{{BADGE}}", page["badge"])
        html_content = html_content.replace("{{HEADING}}", page["heading"])
        html_content = html_content.replace("{{SUBHEADING}}", page["subheading"])
        html_content = html_content.replace("{{TARGET_MARKET}}", page["target_market"])
        html_content = html_content.replace("{{ENCODE_TITLE}}", urllib.parse.quote(page["heading"]))

        filename = f"{page['slug']}.html"
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(html_content)
        success_count += 1
    except Exception as e:
        print(f"Error generating {page['slug']}: {e}")

# 7. Generate Core Sitemap
domain = "https://www.tonyisdope.com.ng"
sitemap_files = []

static_html_files = [f[:-5] for f in os.listdir('.') if f.endswith('.html') and f != 'template.html']
core_pages = [f for f in static_html_files if len(f.split('-')) <= 3 or f in ['index', 'about', 'contact', 'blog', 'services', 'courses'] or f.startswith('case-study-') or f.endswith('landing-page')]

if core_pages:
    core_sm_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    core_sm_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in core_pages:
        core_sm_content += f"  <url>\n    <loc>{domain}/{page}.html</loc>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n"
    core_sm_content += '</urlset>'
    
    with open('sitemap-core.xml', 'w', encoding='utf-8') as csm:
        csm.write(core_sm_content)
    sitemap_files.append('sitemap-core.xml')

# 8. Chunk Programmatic Pages into 50k Sitemaps (e.g., sitemap-pages-1.xml, sitemap-pages-2.xml, etc.)
chunk_size = 50000
for i in range(0, len(pages_data), chunk_size):
    chunk = pages_data[i:i + chunk_size]
    sitemap_filename = f"sitemap-pages-{i // chunk_size + 1}.xml"
    
    sm_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sm_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in chunk:
        sm_content += f"  <url>\n    <loc>{domain}/{page['slug']}.html</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
    sm_content += '</urlset>'
    
    with open(sitemap_filename, 'w', encoding='utf-8') as sf:
        sf.write(sm_content)
    sitemap_files.append(sitemap_filename)

# 9. Generate Master Sitemap Index
index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for sf in sitemap_files:
    index_content += f"  <sitemap>\n    <loc>{domain}/{sf}</loc>\n  </sitemap>\n"
index_content += '</sitemapindex>'

with open('sitemap.xml', 'w', encoding='utf-8') as idx:
    idx.write(index_content)

print(f"Master sitemap.xml index successfully generated with {len(sitemap_files)} sitemap partitions!")
print(f"Successfully built {success_count:,} enterprise programmatic HTML files and all sitemaps!")