import requests

from pprint import pprint
from datetime import datetime
import locale

# # for Windows users
# for lang in locale.windows_locale.values():
#     print(lang)
#
# # for other operating systems
# for lang in locale.locale_alias.values():
#     print(lang)

locale.setlocale(locale.LC_ALL, 'nl_NL')


def get_data(city):

    # openweathermap api
    url = "http://api.openweathermap.org/data/2.5/forecast/daily"
    url += "?appid=d1526a9039658a6f76950cff21823aff"
    url += "&units=metric"
    url += "&mode=json"
    url += "&lang=nl"
    url += "&cnt=16"
    url += "&q=" + city

    print(url)

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    else:
        raise Exception('No data retrieved')


if __name__ == '__main__':

    data = get_data('Soesterberg')

    # pprint(data)

    for day_forecast in data['list']:
        dt = day_forecast['dt']
        day = datetime.fromtimestamp(dt)
        day_formatted = day.strftime('%d %B')
        week_day = day.strftime('%a')
        temp_day = day_forecast['temp']['day']
        temp_night = day_forecast['temp']['night']
        weather = day_forecast['weather'][0]['description']
        wind_speed = day_forecast['speed']
        wind_direction = day_forecast['deg']

        print(week_day, day_formatted, temp_day, temp_night, weather, wind_speed, wind_direction)

