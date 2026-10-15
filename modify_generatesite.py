import csv
import urllib.parse

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Read directly from your Google Sheet CSV export
with open('pages.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    pages_data = list(reader)

for page in pages_data:
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

print(f"Successfully generated {len(pages_data)} targeted SEO pages from CSV!")