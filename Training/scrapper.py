import requests
import httpx
from bs4 import BeautifulSoup
import re

# url = 'https://www.nu.nl'
url = 'https://www.telegraaf.nl'

keyword = input('Geef keyword: ')
regex = re.compile(keyword, re.IGNORECASE)

# r = httpx.get(url, follow_redirects=True)
r = requests.get(url)

if r.status_code == 200:
    print(f'Succesfully loaded "{url}"')
    # print(r.text)

    soup = BeautifulSoup(r.text, features="html.parser")

    articles = soup.find_all('article')

    for article in articles:
        text = article.text

        if regex.search(text):

            link = article.find('a')
            print(text)
            print()
            print(link['href'])
            print(80*'-')

else:
    print(r)

