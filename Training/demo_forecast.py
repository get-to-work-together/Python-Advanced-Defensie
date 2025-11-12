import requests
import datetime
# from decorators import cache, measure_time
from functools import cache


@cache
def get_forcast(city, ndays=14):
    """Get daily forecast from api.openweathermap.org"""
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
    url += '?appid=d1526a9039658a6f76950cff21823aff'
    url += f'&cnt={ndays}'
    url += '&units=metric'
    url += '&mode=json'
    url += f'&q={city}'

    response = requests.get(url)
    if response.status_code == 200:
        decoded = response.json()
        return decoded
    else:
        raise Exception(f'Error for city {city}. Status code {response.status_code}: {response.json()['message']}.')


def extract_daily_temp(daily_forecast):
    """Create a list with temperature values from the daily forecast response."""
    temps = []
    dates = []
    for day_forecast in daily_forecast['list']:
        temps.append(day_forecast['temp']['day'])
        dates.append(datetime.date.fromtimestamp(day_forecast['dt']))
    return temps, dates


# -------------------------------------------------------

if __name__ == '__main__':

    city = input('Waar wil je weten wat de temperatuur is? : ')

    data = get_forcast(city)

    temps, dates = extract_daily_temp(data)

    print(temps)
