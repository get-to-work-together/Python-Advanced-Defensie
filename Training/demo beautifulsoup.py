import sys
import re

import requests
from bs4 import BeautifulSoup

# Kibana
url = 'https://www.elastic.co/guide/en/kibana/current/release-notes.html'
items_selector = 'li.listitem a'
string_selector = 'title'
regex = r'^(\w+) (\d+)\.(\d+)\.(\d+)-?(.*)$'

# Kibana Guides
url = 'https://www.elastic.co/guide/en/kibana/index.html'
items_selector = 'li.listitem a'
string_selector = None
regex = r'^(.*): *(\d+)\.(\d+)\.?(\d*)[- ]?(.*)$'

# Confluence Release Notes
url = 'https://confluence.atlassian.com/doc/confluence-release-notes-327.html'
items_selector = 'div.content-section ul li a'
string_selector = None
regex = r'^(Confluence) (\d+)\.(\d+)\.?(\d*) ?(.*)$'


r = requests.get(url)

if r.status_code != 200:
    print(f'Could not get open {url}')
    sys.exit()

soup = BeautifulSoup(r.text, features="html.parser")

items = soup.select(items_selector)

for item in items:
    if string_selector:
        title = item[string_selector]
    else:
        title = item.text

    match = re.match(regex, title)

    if match:
        name, major, minor, rev, sub = match.groups()

        print(name, major, minor, rev, sub)

