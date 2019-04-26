from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from map import models
# import os


# Create your views here.
@csrf_exempt
def mappage(request):
    now = datetime.now()
    template = get_template('map/map.html')

    all_address = models.Address.objects.all()
    print(all_address)

    if request.method == 'POST':
        try:
            user_address = str(request.POST.get('textPosition')).split(',')
            user_longi = user_address[0]
            user_lati = user_address[1]
            address = models.Address.objects.create(
                longitude=user_longi, latitude=user_lati)

            print(user_longi+','+user_lati)

        except:
            message = '好像没有检测到地址哦~'
    html = template.render(locals())
    return HttpResponse(html)
