from googlesearch import search
from urllib.parse import urlparse

query = input("Enter your query: ")
visited_domains = set()
result_urls = []

for website in search(query, tld="com", num=10, stop=100, pause=2):
    domain = urlparse(website).netloc
    if domain not in visited_domains:
        visited_domains.add(domain)
        result_urls.append(website)

output_filename = input("Enter the output file name (with .html extension): ")
if not output_filename.endswith(".html"):
    output_filename += ".html"

html_content = "<html><body>"
for url in result_urls:
    html_content += f"<p><a href='{url}'>{url}</a></p>"
html_content += "</body></html>"

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Search results saved to {output_filename}")
