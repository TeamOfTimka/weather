from django.shortcuts import render
import requests

def index(request):
    appid = "0efd99ccc7371294a461e8f9b7d74893"
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
    
    city = 'London'

    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': int(res['main']['temp'])-273,
        'icon': res['weather'][0]['icon']
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)