from django.shortcuts import HttpResponse
from django.template.loader import get_template
from datetime import datetime


# Create your views here.
def homepage(request):
    now = datetime.now()
    template=get_template('index.html')
    html=template.render(locals())
    return HttpResponse(html)
