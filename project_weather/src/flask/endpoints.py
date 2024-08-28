from flask import Flask, request, render_template

from ..models.openweathermap.get_data import get_formatted_data
from ..models.openweathermap.analyze import build_chart

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/info')
def info():
    s = "Dit is info on my OpenWeatherMap application."
    return s


@app.route('/weather_forecast', methods=['GET', 'POST'])
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


@app.route('/forecast', methods=['GET', 'POST'])
def forecast():

    days = request.args.get('days') or 14
    city = request.args.get('city')
    if city is None or city == '':
        header = 'No city specified'
        data = None
    else:
        header = f'{days} day weather forecast for {city}'
        data = get_formatted_data(city, days)
        build_chart(data)

    return render_template('base.html', header=header, data=data)
