<<<<<<< HEAD
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

# 2. Define Master Scaling Lists (Expanded to Hit 30,000 Pages)
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
    {"name": "Oil & Gas B2B Marketing", "slug": "oil-gas-marketing", "heading": "Oil & Gas B2B Marketing Agency"}
]

# Exactly 100 Geographic Micro-Markets for 30,000-page scale
locations = [
    # --- Port Harcourt & Rivers State (12 Hubs) ---
    {"name": "Trans Amadi Port Harcourt", "slug": "trans-amadi-ph", "market": "Trans Amadi"},
    {"name": "GRA Phase 1 Port Harcourt", "slug": "gra-phase1-ph", "market": "GRA Phase 1"},
    {"name": "GRA Phase 2 Port Harcourt", "slug": "gra-phase2-ph", "market": "GRA Phase 2"},
    {"name": "Rumuola Port Harcourt", "slug": "rumuola-ph", "market": "Rumuola"},
    {"name": "Peter Odili Road Port Harcourt", "slug": "peter-odili-ph", "market": "Peter Odili Road"},
    {"name": "Woji Port Harcourt", "slug": "woji-ph", "market": "Woji"},
    {"name": "Rumuokworo Port Harcourt", "slug": "rumuokworo-ph", "market": "Rumuokworo"},
    {"name": "Ada George Port Harcourt", "slug": "ada-george-ph", "market": "Ada George"},
    {"name": "Eleme Industrial Hub Port Harcourt", "slug": "eleme-ph", "market": "Eleme"},
    {"name": "Bori Camp Port Harcourt", "slug": "bori-camp-ph", "market": "Bori Camp"},
    {"name": "Old GRA Port Harcourt", "slug": "old-gra-ph", "market": "Old GRA"},
    {"name": "Choba University Hub Port Harcourt", "slug": "choba-ph", "market": "Choba"},

    # --- Lagos Commercial Hubs (25 Hubs) ---
    {"name": "Lekki Phase 1 Lagos", "slug": "lekki-phase-1-lagos", "market": "Lekki Lagos"},
    {"name": "Victoria Island Lagos", "slug": "victoria-island-lagos", "market": "Victoria Island Lagos"},
    {"name": "Ikeja GRA Lagos", "slug": "ikeja-gra-lagos", "market": "Ikeja Lagos"},
    {"name": "Ikoyi Lagos", "slug": "ikoyi-lagos", "market": "Ikoyi Lagos"},
    {"name": "Ajah Lagos", "slug": "ajah-lagos", "market": "Ajah Lagos"},
    {"name": "Surulere Lagos", "slug": "surulere-lagos", "market": "Surulere Lagos"},
    {"name": "Yaba Tech District Lagos", "slug": "yaba-lagos", "market": "Yaba Lagos"},
    {"name": "Magodo Lagos", "slug": "magodo-lagos", "market": "Magodo Lagos"},
    {"name": "Victoria Garden City Lagos", "slug": "vgc-lagos", "market": "VGC Lagos"},
    {"name": "Epe Expressway Lagos", "slug": "epe-lagos", "market": "Epe Lagos"},
    {"name": "Banana Island Lagos", "slug": "banana-island-lagos", "market": "Banana Island"},
    {"name": "Epe Lagos", "slug": "epe-town-lagos", "market": "Epe Town"},
    {"name": "Maryland Lagos", "slug": "maryland-lagos", "market": "Maryland Lagos"},
    {"name": "Gbagada Lagos", "slug": "gbagada-lagos", "market": "Gbagada Lagos"},
    {"name": "Alausa Ikeja Lagos", "slug": "alausa-lagos", "market": "Alausa Ikeja"},
    {"name": "Festac Town Lagos", "slug": "festac-lagos", "market": "Festac Town"},
    {"name": "Sangotedo Lagos", "slug": "sangotedo-lagos", "market": "Sangotedo"},
    {"name": "Chevron Drive Lagos", "slug": "chevron-lagos", "market": "Chevron Lagos"},
    {"name": "Oregun Lagos", "slug": "oregun-lagos", "market": "Oregun Lagos"},
    {"name": "Isolo Lagos", "slug": "isolo-lagos", "market": "Isolo Lagos"},
    {"name": "Apapa Port Lagos", "slug": "apapa-lagos", "market": "Apapa Lagos"},
    {"name": "Lagos Island Commercial", "slug": "lagos-island", "market": "Lagos Island"},
    {"name": "Ogudu Lagos", "slug": "ogudu-lagos", "market": "Ogudu"},
    {"name": "Ogba Lagos", "slug": "ogba-lagos", "market": "Ogba Lagos"},
    {"name": "Badagry Lagos", "slug": "badagry-lagos", "market": "Badagry"},

    # --- Abuja Federal Capital Hubs (15 Hubs) ---
    {"name": "Maitama Abuja", "slug": "maitama-abuja", "market": "Maitama Abuja"},
    {"name": "Wuse Zone Abuja", "slug": "wuse-abuja", "market": "Wuse Abuja"},
    {"name": "Asokoro Abuja", "slug": "asokoro-abuja", "market": "Asokoro Abuja"},
    {"name": "Garki Abuja", "slug": "garki-abuja", "market": "Garki Abuja"},
    {"name": "Jabi Abuja", "slug": "jabi-abuja", "market": "Jabi Abuja"},
    {"name": "Gwarinpa Abuja", "slug": "gwarinpa-abuja", "market": "Gwarinpa Abuja"},
    {"name": "Central Business District Abuja", "slug": "cbd-abuja", "market": "CBD Abuja"},
    {"name": "Utako Abuja", "slug": "utako-abuja", "market": "Utako Abuja"},
    {"name": "Katampe Extension Abuja", "slug": "katampe-abuja", "market": "Katampe"},
    {"name": "Guzape Abuja", "slug": "guzape-abuja", "market": "Guzape"},
    {"name": "Life Camp Abuja", "slug": "lifecamp-abuja", "market": "Life Camp"},
    {"name": "Lugbe Abuja", "slug": "lugbe-abuja", "market": "Lugbe"},
    {"name": "Kubwa Abuja", "slug": "kubwa-abuja", "market": "Kubwa"},
    {"name": "Apo District Abuja", "slug": "apo-abuja", "market": "Apo Abuja"},
    {"name": "Bwari Abuja", "slug": "bwari-abuja", "market": "Bwari"},

    # --- Nigerian State Capitals & Commercial Hubs (23 Hubs) ---
    {"name": "Ibadan Oyo State", "slug": "ibadan-oyo", "market": "Ibadan"},
    {"name": "Uyo Akwa Ibom", "slug": "uyo-akwa-ibom", "market": "Uyo"},
    {"name": "Aba Industrial Layout Abia", "slug": "aba-abia", "market": "Aba"},
    {"name": "Warri Delta State", "slug": "warri-delta", "market": "Warri"},
    {"name": "Benin City Edo State", "slug": "benin-city-edo", "market": "Benin City"},
    {"name": "Enugu City", "slug": "enugu-city", "market": "Enugu"},
    {"name": "Calabar Cross River", "slug": "calabar-cross-river", "market": "Calabar"},
    {"name": "Onitsha Main Market Anambra", "slug": "onitsha-anambra", "market": "Onitsha"},
    {"name": "Kaduna City", "slug": "kaduna-city", "market": "Kaduna"},
    {"name": "Kano Commercial Hub", "slug": "kano-city", "market": "Kano"},
    {"name": "Jos Plateau State", "slug": "jos-plateau", "market": "Jos"},
    {"name": "Owerri Imo State", "slug": "owerri-imo", "market": "Owerri"},
    {"name": "Asaba Delta State", "slug": "asaba-delta", "market": "Asaba"},
    {"name": "Akure Ondo State", "slug": "akure-ondo", "market": "Akure"},
    {"name": "Abeokuta Ogun State", "slug": "abeokuta-ogun", "market": "Abeokuta"},
    {"name": "Ilorin Kwara State", "slug": "ilorin-kwara", "market": "Ilorin"},
    {"name": "Makurdi Benue State", "slug": "makurdi-benue", "market": "Makurdi"},
    {"name": "Sokoto City", "slug": "sokoto-city", "market": "Sokoto"},
    {"name": "Bauchi City", "slug": "bauchi-city", "market": "Bauchi"},
    {"name": "Yenagoa Bayelsa State", "slug": "yenagoa-bayelsa", "market": "Yenagoa"},
    {"name": "Awka Anambra State", "slug": "awka-anambra", "market": "Awka"},
    {"name": "Abakaliki Ebonyi State", "slug": "abakaliki-ebonyi", "market": "Abakaliki"},
    {"name": "Umuahia Abia State", "slug": "umuahia-abia", "market": "Umuahia"},

    # --- Global & Diaspora Business Hubs (25 Hubs) ---
    {"name": "London United Kingdom", "slug": "london-uk", "market": "London UK"},
    {"name": "Manchester United Kingdom", "slug": "manchester-uk", "market": "Manchester UK"},
    {"name": "Birmingham United Kingdom", "slug": "birmingham-uk", "market": "Birmingham UK"},
    {"name": "Edinburgh Scotland UK", "slug": "edinburgh-uk", "market": "Edinburgh UK"},
    {"name": "Glasgow Scotland UK", "slug": "glasgow-uk", "market": "Glasgow UK"},
    {"name": "Toronto Canada", "slug": "toronto-canada", "market": "Toronto Canada"},
    {"name": "Vancouver Canada", "slug": "vancouver-canada", "market": "Vancouver Canada"},
    {"name": "Calgary Canada", "slug": "calgary-canada", "market": "Calgary Canada"},
    {"name": "Ottawa Canada", "slug": "ottawa-canada", "market": "Ottawa Canada"},
    {"name": "Montreal Canada", "slug": "montreal-canada", "market": "Montreal Canada"},
    {"name": "New York USA", "slug": "new-york-usa", "market": "New York USA"},
    {"name": "Houston Texas USA", "slug": "houston-usa", "market": "Houston USA"},
    {"name": "Atlanta Georgia USA", "slug": "atlanta-usa", "market": "Atlanta USA"},
    {"name": "Chicago Illinois USA", "slug": "chicago-usa", "market": "Chicago USA"},
    {"name": "Dallas Texas USA", "slug": "dallas-usa", "market": "Dallas USA"},
    {"name": "San Francisco California USA", "slug": "san-francisco-usa", "market": "San Francisco USA"},
    {"name": "Seattle Washington USA", "slug": "seattle-usa", "market": "Seattle USA"},
    {"name": "Miami Florida USA", "slug": "miami-usa", "market": "Miami USA"},
    {"name": "Dubai UAE", "slug": "dubai-uae", "market": "Dubai UAE"},
    {"name": "Abu Dhabi UAE", "slug": "abu-dhabi-uae", "market": "Abu Dhabi UAE"},
    {"name": "Johannesburg South Africa", "slug": "johannesburg-sa", "market": "Johannesburg SA"},
    {"name": "Cape Town South Africa", "slug": "cape-town-sa", "market": "Cape Town SA"},
    {"name": "Nairobi Kenya", "slug": "nairobi-kenya", "market": "Nairobi Kenya"},
    {"name": "Accra Ghana", "slug": "accra-ghana", "market": "Accra Ghana"},
    {"name": "Doha Qatar", "slug": "doha-qatar", "market": "Doha Qatar"}
]

# Industries & Sub-Niches
industries = [
    {"name": "Luxury Real Estate", "slug": "luxury-real-estate", "badge": "Property Growth Partner"},
    {"name": "Commercial Real Estate & Land", "slug": "commercial-real-estate", "badge": "Real Estate Scale Partner"},
    {"name": "Oil & Gas Upstream Services", "slug": "oil-gas-upstream", "badge": "Industrial Energy Partner"},
    {"name": "Downstream Haulage & Logistics", "slug": "downstream-logistics", "badge": "Supply Chain Growth Partner"},
    {"name": "Fintech & Neo-Banks", "slug": "fintech-startups", "badge": "Fintech Growth Partner"},
    {"name": "Crypto & Web3 Gateways", "slug": "crypto-web3", "badge": "Web3 Growth Partner"},
    {"name": "Healthcare & Specialist Clinics", "slug": "healthcare-clinics", "badge": "HealthTech Partner"},
    {"name": "Private Schools & EdTech", "slug": "edtech-schools", "badge": "Education Growth Partner"},
    {"name": "Corporate Law Practices", "slug": "law-firms", "badge": "Legal Growth Partner"},
    {"name": "Hospitality & Luxury Hotels", "slug": "hospitality-hotels", "badge": "Hospitality Partner"},
    {"name": "Manufacturing & Fabrication", "slug": "manufacturing", "badge": "Industrial Manufacturing Partner"},
    {"name": "Fashion & E-Commerce Retail", "slug": "fashion-ecommerce", "badge": "Retail Growth Partner"},
    {"name": "SaaS & Software Startups", "slug": "saas-companies", "badge": "SaaS Growth Partner"},
    {"name": "Boutique Agro-Allied Exporters", "slug": "agro-allied", "badge": "Agro-Export Partner"},
    {"name": "Renewable Energy & Solar Firms", "slug": "renewable-solar", "badge": "Clean Energy Partner"}
]

# 3. Mathematically Cross-Multiply Combinations (20 services * 100 locations * 15 industries = 30,000 pages)
print("Generating your 30,000-page enterprise programmatic matrix...")
pages_data = []
for s, l, i in itertools.product(services, locations, industries):
    slug = f"{s['slug']}-{i['slug']}-{l['slug']}"
    title = f"{s['name']} for {i['name']} in {l['name']} | TIDA Ltd"
    description = f"Drive verified revenue and scale customer acquisition for {i['name']} brands in {l['name']} with expert {s['name']} by TIDA Ltd."
    badge = i['badge']
    heading = f"{s['heading']} for {i['name']} in {l['name']}"
    subheading = f"Scale your {i['name']} operations across {l['name']} with enterprise-grade ad architectures and automated sales funnels built by TIDA Ltd."
    target_market = l['market']
    
    pages_data.append({
        "slug": slug, "title": title, "description": description, 
        "badge": badge, "heading": heading, "subheading": subheading, "target_market": target_market
    })

print(f"Total compiled enterprise pages: {len(pages_data)}. Building files...")

# 4. High-Speed HTML File Generation Loop
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

print(f"Successfully generated {success_count} enterprise HTML pages in seconds!")

# 5. Advanced Modular Sitemap Generation (Categorized by Intent & Hubs)
domain = "https://www.tonyisdope.com.ng"
os.makedirs("sitemaps", exist_ok=True) 

service_sitemap_pages = [p for p in pages_data if "meta-ads" in p["slug"] or "google-ppc" in p["slug"]]
location_sitemap_pages = [p for p in pages_data if "london" in p["slug"] or "lagos" in p["slug"] or "abuja" in p["slug"] or "port-harcourt" in p["slug"]]
industry_sitemap_pages = [p for p in pages_data if p not in service_sitemap_pages and p not in location_sitemap_pages]

sitemap_files = []

def write_sitemap(filename, pages_chunk):
    sm_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sm_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages_chunk:
        sm_content += f"  <url>\n    <loc>{domain}/{page['slug']}.html</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
    sm_content += '</urlset>'
    
    filepath = f"{filename}.xml"
    with open(filepath, 'w', encoding='utf-8') as sm:
        sm.write(sm_content)
    sitemap_files.append(filepath)

if service_sitemap_pages:
    write_sitemap("sitemap-services", service_sitemap_pages)
if location_sitemap_pages:
    write_sitemap("sitemap-locations", location_sitemap_pages)
if industry_sitemap_pages:
    write_sitemap("sitemap-industries", industry_sitemap_pages)

all_accounted = service_sitemap_pages + location_sitemap_pages + industry_sitemap_pages
remaining_pages = [p for p in pages_data if p not in all_accounted]
if remaining_pages:
    write_sitemap("sitemap-general", remaining_pages)

index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for sf in sitemap_files:
    index_content += f"  <sitemap>\n    <loc>{domain}/{sf}</loc>\n  </sitemap>\n"
index_content += '</sitemapindex>'

with open('sitemap.xml', 'w', encoding='utf-8') as idx:
    idx.write(index_content)

print(f"Successfully generated semantic modular sitemaps ({', '.join(sitemap_files)}) and master sitemap.xml index!")
=======
import csv
import urllib.parse
import os

# 1. Load Master HTML Template
template_path = 'template.html'
if not os.path.exists(template_path):
    print("Error: template.html not found!")
    exit()

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# 2. Read Master CSV Matrix Data (with empty row filtering)
csv_path = 'pages.csv'
if not os.path.exists(csv_path):
    print("Error: pages.csv not found!")
    exit()

with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # Filter out empty rows where 'slug' is missing or None
    pages_data = [row for row in reader if row and row.get('slug')]

print(f"Loaded {len(pages_data)} valid pages from CSV. Generating HTML files...")

# 3. Generate HTML Pages
success_count = 0
for page in pages_data:
    try:
        html_content = template
        html_content = html_content.replace("{{TITLE}}", page.get("title", ""))
        html_content = html_content.replace("{{DESCRIPTION}}", page.get("description", ""))
        html_content = html_content.replace("{{SLUG}}", page.get("slug", ""))
        html_content = html_content.replace("{{BADGE}}", page.get("badge", ""))
        html_content = html_content.replace("{{HEADING}}", page.get("heading", ""))
        html_content = html_content.replace("{{SUBHEADING}}", page.get("subheading", ""))
        html_content = html_content.replace("{{TARGET_MARKET}}", page.get("target_market", ""))
        html_content = html_content.replace("{{ENCODE_TITLE}}", urllib.parse.quote(page.get("heading", "")))

        filename = f"{page['slug']}.html"
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(html_content)
        success_count += 1
    except Exception as e:
        print(f"Error generating {page.get('slug')}: {e}")

print(f"Successfully generated {success_count} HTML pages!")

# 4. Generate sitemap.xml for Google Search Console
domain = "https://www.tonyisdope.com.ng"
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for page in pages_data:
    slug = page.get("slug", "")
    if slug:
        sitemap_content += f"  <url>\n    <loc>{domain}/{slug}.html</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"

sitemap_content += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as sm:
    sm.write(sitemap_content)

print("Successfully generated sitemap.xml for Google Search Console!")
>>>>>>> 6d580218b306f8a19f130c44eb50b2d6b77d3112
