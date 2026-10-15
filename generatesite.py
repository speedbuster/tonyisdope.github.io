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