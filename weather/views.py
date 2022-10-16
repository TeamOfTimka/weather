from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = "0efd99ccc7371294a461e8f9b7d74893"
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    if (request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    info = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon']
            }
            if not city_info in info:
                info.append(city_info)
        except:
            continue    
        

    context = {'info': info, 'form': form}

    return render(request, 'weather/index.html', context)