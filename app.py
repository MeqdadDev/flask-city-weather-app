'''
City Weather App using Flask framework
Used API: https://openweathermap.org/

By: Meqdad Darweesh
'''

from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/city', methods=['POST'])
def city():
    name = request.form['city']
    info = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={'Register in OpenWeather and get your appid'}')
    r_json = info.json()
    location_dict = r_json['coord']
    location_lon = location_dict['lon']
    location_lat = location_dict['lat']
    weather = str(r_json['weather'][0]['main']).capitalize()
    weather_description = str(r_json['weather'][0]['description']).capitalize()
    temperature_k = r_json['main']['temp']
    temperature_c = str(format((temperature_k - 273.15), '.2f')+' °C')
    pressure = r_json['main']['pressure']
    humidity = r_json['main']['humidity']
    return render_template("city.html", city_name=name, city_location_lon=location_lon,
                           city_location_lat=location_lat, city_weather=weather,
                           city_weather_description=weather_description, city_temperature=temperature_c,
                           city_pressure=pressure, city_humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True)
