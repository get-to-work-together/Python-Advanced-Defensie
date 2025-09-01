from flask import Flask, request


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
    days = request.args.get('days')
    return f'Work in progress ... {days} day weather forecast for {city} coming up!'




app.run(port=8080)
