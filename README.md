# City Weather App

## using Flask framework

Web app for city weather info using **Flask framework**

A web app for getting the weather info of a city by providing the name of the city.

Used API: [OpenWeather](https://openweathermap.org/).

### API Response sample:
```
{
	"coord": {
		"lon": 35.18,
		"lat": 31.89
	},
	"weather": [{
		"id": 801,
		"main": "Clouds",
		"description": "few clouds",
		"icon": "02d"
	}],
	"base": "stations",
	"main": {
		"temp": 300.97,
		"feels_like": 302.22,
		"temp_min": 298.71,
		"temp_max": 302.59,
		"pressure": 1008,
		"humidity": 66
	},
	"visibility": 10000,
	"wind": {
		"speed": 4.1,
		"deg": 320
	},
	"clouds": {
		"all": 20
	},
	"dt": 1594830742,
	"sys": {
		"type": 1,
		"id": 6845,
		"country": "PS",
		"sunrise": 1594781044,
		"sunset": 1594831563
	},
	"timezone": 10800,
	"id": 282239,
	"name": "Ramallah",
	"cod": 200
}
```
#### For educational purposes.
Made with ❤️ and Python & Meqdad.
