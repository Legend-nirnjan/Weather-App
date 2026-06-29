import requests
from django.shortcuts import render
from .models import Weather
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def get_weather_emoji(description, temperature):
    desc = description.lower()

    if 'snow' in desc and temperature <= 0:    
        return "❄️"
    elif 'thunder and rain' in desc:           
        return "⛈"
    elif 'thunder' in desc:
        return "🌩"
    elif 'rain' in desc:
        return "🌧"
    elif 'partly cloudy' in desc:              
        return "🌥"
    elif 'cloudy' in desc:
        return "☁️"
    else:
        return "☀️"


API_KEY = "888885c74fe83f61cbc39461b40562ec"


def get_weather(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get('cod') == 200:
            emoji = get_weather_emoji(
                response['weather'][0]['description'],
                response['main']['temp']
            )

            weather_data = Weather.objects.create(
                city=city,
                temperature=response['main']['temp'],
                description=response['weather'][0]['description'],  
                humidity=response['main']['humidity'],
                wind_speed=response['wind']['speed']
            )
            weather_data.emoji = emoji

    history = Weather.objects.order_by('-fetched_at')[:5]

    return render(request, 'weather/index.html', {
        'weather': weather_data,
        'history': history
    })