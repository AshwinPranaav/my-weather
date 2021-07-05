from django.shortcuts import render
import json
import urllib.request
import os
from dotenv import load_dotenv
load_dotenv()

def index(request):
    context = None
    if request.method == 'POST':
        city = request.POST['city']
        my_key = str(os.environ.get('my_key'))
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&units=metric' + '&appid={}'.format(my_key)).read()
        
        res = json.loads(source)
        print(res)
        context = {
            'data':{
                "country_code": str(res['sys']['country']),
                "city": str(res['name']),
                "coordinates": str(res['coord']['lon']) + ' ' + str(res['coord']['lat']),
                "temperature": str(res['main']['temp']) + '°C feels like, ' + str(res['main']['feels_like']),
                # "type": str(res[weather.main),
                # "pressure": str(res.main.pressure),
                # "humidity": str(res.main.humidity),
            }
        }
    else:
        context = {}
    return render(request, "main/index.html", context)