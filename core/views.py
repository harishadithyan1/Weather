from django.shortcuts import render
import requests
import json

# Function to fetch weather data
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "c49840c46169ce42e482abdc13751f3b"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    
    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        return None  # Return None if API call fails

# Main view function
def index(request):
    city = request.GET.get('city')  # Get city from URL
    weather_data = None
    icon_url='https://openweathermap.org/img/wn/10d@2x.png'
    if city:
        weather_data_result = get_weather(city)  # Call weather API

        if weather_data_result is not None:
            weather_data = {
                'icon_id':weather_data_result['weather'][0]['icon'],
                'icon_url':'https://openweathermap.org/img/wn/10d@2x.png',
                'temperature': weather_data_result['main']['temp'],
                'weather': weather_data_result['weather'][0]['main'],
                'weather_description': weather_data_result['weather'][0]['description'],
                'city': weather_data_result['name'],
                'country': weather_data_result['sys']['country'],
                'wind_speed': weather_data_result['wind']['speed'],
                'humidity': weather_data_result['main']['humidity'],
                'pressure': weather_data_result['main']['pressure'],
                'lon':weather_data_result['coord']['lon'],
                'lat':weather_data_result['coord']['lat'],
            }

    return render(request, 'pages/index.html', {'weather_data': weather_data})
