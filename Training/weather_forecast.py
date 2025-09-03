import httpx
from datetime import datetime
import json
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'nl_nl')


city = input('Welke stad? : ')

url =  "http://api.openweathermap.org/data/2.5/forecast/daily"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&cnt=14"
url += "&lang=nl"
url += "&q=" + city

print(url)

response = httpx.get(url)

if response.status_code == 200:
    content = json.loads(response.text)

    dds = []
    day_temps = []
    night_temps = []
    min_temps = []
    max_temps = []
    for day_forecast in content['list']:
        dd = datetime.fromtimestamp(day_forecast['dt'])
        min = day_forecast['temp']['min']
        max = day_forecast['temp']['max']
        day = day_forecast['temp']['day']
        night = day_forecast['temp']['night']
        weather = day_forecast['weather'][0]['description']

        dds.append(dd)
        day_temps.append(day)
        night_temps.append(night)
        min_temps.append(min)
        max_temps.append(max)

        print(dd.strftime('%a %d-%m-%Y'), day, night, min, max, weather)

    fig, ax = plt.subplots()
    ax.set_title(f'Voorspelling voor {city} voor de komende 2 weken')
    ax.grid()
    ax.fill_between(dds, min_temps, max_temps, color='lightblue')
    ax.plot(dds, day_temps, lw=2, label='Day')
    ax.plot(dds, night_temps, lw=2, label='Night')
    ax.legend()
    plt.show()

else:
    print(f'Could not get data for {city}')

