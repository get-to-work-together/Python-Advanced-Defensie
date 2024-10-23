import requests
from pprint import pprint

city = input('Geef plaats: ')

url = 'http://api.openweathermap.org/data/2.5/weather'\
      '?appid=d1526a9039658a6f76950cff21823aff'\
      '&units=metric'\
      '&mode=json'\
      '&q=' + city

# print(url)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)

    temperature = data['main']['temp']

    print(f'Het is nu {temperature} graden in {city}.')

else:
    print('Kan geen data ophalen.')