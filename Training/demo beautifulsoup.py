import sys
import re
import json

import requests
from bs4 import BeautifulSoup

filename = 'config.json'
with open(filename) as f:
    config = json.load(f)


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

        if current_version:
            if len(current_version) == 1 and (major, ) == current_version:
                print(name, major, minor, rev, sub)
            elif len(current_version) == 2 and (major, minor) == current_version:
                print(name, major, minor, rev, sub)
            elif len(current_version) == 3 and (major, minor, rev) == current_version:
                print(name, major, minor, rev, sub)
        else:
            print(name, major, minor, rev, sub)

