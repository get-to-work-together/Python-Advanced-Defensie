from Project.src.database import persistence
from Project.src.utils.decorators import throttle

import re
import json

import requests
from bs4 import BeautifulSoup


def get_applications():
    applications = persistence.get_all_application_records()
    temp = []
    for id, name, version in applications:
        t = version.split('.')
        if len(t) == 1:
            t += ('', '')
        elif len(t) == 2:
            t += ('',)
        major, minor, rev = [int(item) if item.isnumeric() else None for item in t]
        temp.append((name, major, minor, rev))
    return temp


def get_applications():
    applications = persistence.get_all_application_records()
    for id, name, version in applications:
        t = version.split('.')
        if len(t) == 1:
            t += ('', '')
        elif len(t) == 2:
            t += ('',)
        major, minor, rev = [int(item) if item.isnumeric() else 0 for item in t]
        yield (name, major, minor, rev)


@throttle
def get_url(url):
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception(f'No valid response from {url}')

    return r.text


def get_revisions(name):

    filename = 'config.json'
    with open(filename) as f:
        config_list = json.load(f)

    for config in config_list:
        if config['name'] == name:
            break
    else:
        return None

    name = config['name']
    url = config['url']
    items_selector = config['items_selector']
    string_selector = config['string_selector']
    regex = config['regex']

    response_body = get_url(url)

    soup = BeautifulSoup(response_body, features="html.parser")

    items = soup.select(items_selector)

    for item in items:
        if string_selector:
            title = item[string_selector]
        else:
            title = item.text

        match = re.match(regex, title)

        if match:
            name, major, minor, rev, sub = match.groups()
            major = int(major) if major else 0
            minor = int(minor) if minor else 0
            rev = int(rev) if rev else 0
            yield name, major, minor, rev, sub


def get_updateble_applications(keep_major = False):
    for name, current_major, current_minor, current_rev in get_applications():
        new_release_available = False
        for name, new_major, new_minor, new_rev, new_sub in get_revisions(name):
            if (new_major, new_minor, new_rev) > (current_major, current_minor, current_rev):
                new_release_available = True
                yield (name, current_major, current_minor, current_rev, new_major, new_minor, new_rev, new_sub)
            else:
                continue
        if not new_release_available:
            yield (name, current_major, current_minor, current_rev) + 4 * (None,)


