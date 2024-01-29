import sys
import re

import requests
from bs4 import BeautifulSoup

# Kibana
url = 'https://www.elastic.co/guide/en/kibana/current/release-notes.html'
items_selector = 'li.listitem a'
string_selector = 'title'
regex = r'^(\w+) (\d+)\.(\d+)\.(\d+)-?(.*)$'


r = requests.get(url)

if r.status_code != 200:
    print(f'Could not get open {url}')
    sys.exit()

soup = BeautifulSoup(r.text, features="html.parser")

items = soup.select(items_selector)

for item in items:
    title = item[string_selector]

    match = re.match(regex, title)
    name, major, minor, rev, sub = match.groups()

    print(name, major, minor, rev, sub)

