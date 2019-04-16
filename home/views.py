from django.shortcuts import HttpResponse
from django.template.loader import get_template
from datetime import datetime
import os


# Create your views here.
def homepage(request):
    now = datetime.now()
    template = get_template('home/index.html')
    html = template.render(locals())
    return HttpResponse(html)
