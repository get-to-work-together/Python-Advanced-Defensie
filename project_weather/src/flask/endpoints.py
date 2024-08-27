from flask import Flask, request
from ..models.openweathermap.get_data import get_formatted_data


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/info')
def info():
    s = "Dit is info on my OpenWeatherMap application."
    return s


@app.route('/weather_forecast')
def weather_forecast():
    city = request.args.get('city')
    if city is None:
        raise Exception('A city is required')
    days = request.args.get('days') or 14
    data = get_formatted_data(city, days)
    s = f'Work in progress ... {days} day weather forecast for {city} coming up!'
    for day_forecast in data:
        s += '<br>' + str(day_forecast)
    return s

