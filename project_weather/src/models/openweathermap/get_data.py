import requests

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')


class DayForecast:

    def __init__(self, day_forecast):
        self.dt = day_forecast['dt']
        self.day = datetime.fromtimestamp(self.dt)
        self.day_formatted = self.day.strftime('%d %B')
        self.week_day = self.day.strftime('%a')
        self.temp_day = day_forecast['temp']['day']
        self.temp_night = day_forecast['temp']['night']
        self.weather = day_forecast['weather'][0]['description']
        self.wind_speed = day_forecast['speed']
        self.wind_direction = day_forecast['deg']

    def __str__(self):
        return f'{self.week_day} {self.day_formatted} {self.temp_day} {self.temp_night} {self.weather} {self.wind_speed} {self.wind_direction}'



def get_data(city, days=14):

    # openweathermap api
    url = "http://api.openweathermap.org/data/2.5/forecast/daily"
    url += "?appid=d1526a9039658a6f76950cff21823aff"
    url += "&units=metric"
    url += "&mode=json"
    url += "&lang=nl"
    url += f"&cnt={days}"
    url += "&q=" + city

    # print(url)

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    else:
        raise Exception('No data retrieved')


def get_formatted_data(city, days=14):

    data = get_data(city, days)

    daily_forecasts = []
    for day_forecast in data['list']:
        daily_forecasts.append(DayForecast(day_forecast))

    return daily_forecasts



if __name__ == '__main__':

    data = get_formatted_data('Soesterberg', 7)

    for day_forecast in data:
        print(day_forecast)
