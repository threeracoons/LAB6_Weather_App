# weather/views.py
from django.shortcuts import render
import requests

def weather(request):
    city = request.GET.get('city', 'London')  # Default city is London
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    return render(request, 'weather/weather.html', context)
