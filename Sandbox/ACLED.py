# api_key = 'SKYlSoT7kDai9BCMN!V5'
# email = 'email@peteranema.nl'

api_key = 'T9YSTnpfeSaoc8fWZnPG'
email = 'golfechooscar@protonmail.com'

country = 'Netherlands'

region = 12    # Europe

year = 2023

events_from_date = '2023-01-01'
events_to_date = '2023-12-31'
eventdate = events_from_date + '|' + events_to_date

url = 'https://api.acleddata.com/acled/read'
url += f'?key={api_key}'
url += f'&email={email}'

# url += f'&year={year}'
url += f'&eventdate={eventdate}'
#url += f'&country={country}'
url += f'&region={region}'

print(url)
