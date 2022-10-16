from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = "0efd99ccc7371294a461e8f9b7d74893"
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
    
    cities = City.objects.all()

    info = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': int(res['main']['temp'])-273,
                'icon': res['weather'][0]['icon']
            }
            info.append(city_info)
        except:
            continue    
        

    context = {'info': info}

    return render(request, 'weather/index.html', context)