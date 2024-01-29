import sys
import re

import requests
from bs4 import BeautifulSoup

url = 'https://www.elastic.co/guide/en/kibana/current/release-notes.html'

r = requests.get(url)

if r.status_code != 200:
    print(f'Could not get open {url}')
    sys.exit()

soup = BeautifulSoup(r.text, features="html.parser")

div = soup.find('div', class_ = 'ulist itemizedlist')
ul = div.find('ul', class_ = 'itemizedlist')
li = ul.find_all('li', class_ = 'listitem')

for item in li:
    title = item.find('a')['title']

    name, version = title.split()
    if '-' in version:
        version, sub = version.split('-')
    else:
        sub = ''
    major, minor, rev = version.split('.')

    match = re.match(f'^(\w+) (\d+)\.(\d+)\.(\d+)-?(.*)$', title)
    name, major, minor, rev, sub = match.groups()

    print(name, major, minor, rev, sub)

