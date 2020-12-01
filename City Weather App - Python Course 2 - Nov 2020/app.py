'''
**************
City Weather App using Flask Framework
By: Meqdad Darwish
Course: Python course (Purpose for Smart Education & Ministry of Telec. & IT)
**************
'''
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


def get_weather_data():
    raw_data = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=London&appid={Get your API key from OpenWeatherMap}')
    return raw_data.json()


@app.route('/city', methods=['POST'])
def city():
    name = request.form['city_name']
    data = get_weather_data()
    location_data = data['coord']
    location_long = location_data['lon']
    location_lat = location_data['lat']
    weather_main = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    temp = data['main']['temp']
    c_temp = format(float(float(temp) - 273.15), '.2f')
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    return render_template('city.html', city_name=name, longitude=location_long,
                           latitude=location_lat, weather=weather_main,
                           weather_description=weather_description, temperature=c_temp,
                           pressure=pressure, humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True)
