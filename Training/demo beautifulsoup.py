import sys
import re
import json

import requests
from bs4 import BeautifulSoup

def version_to_str(major, minor, rev):
    s = str(major)
    if minor:
        s += '.' + str(minor)
    if rev:
        s += '.' + str(rev)
    return s


filename = 'config.json'
with open(filename) as f:
    config_list = json.load(f)

for config in config_list:
    name = config['name']
    url = config['url']
    items_selector = config['items_selector']
    string_selector = config['string_selector']
    regex = config['regex']
    current_version = tuple(config['current_version']) if config['current_version'] else None

    r = requests.get(url)

    if r.status_code != 200:
        print(f'Could not get open {url}')
        continue

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
            major = int(major) if major else None
            minor = int(minor) if minor else None
            rev = int(rev) if rev else None

            if current_version:
                if len(current_version) == 1 and (major, ) == current_version:
                    print(name, version_to_str(major, minor, rev), sub)
                elif len(current_version) == 2 and (major, minor) == current_version:
                    print(name, version_to_str(major, minor, rev), sub)
                elif len(current_version) == 3 and (major, minor, rev) == current_version:
                    print(name, version_to_str(major, minor, rev), sub)
            else:
                print(name, version_to_str(major, minor, rev), sub)

