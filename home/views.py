from django.shortcuts import HttpResponse
from django.template.loader import get_template
from datetime import datetime
import os


# Create your views here.
def homepage(request):
    now = datetime.now()
    filePath = '.\static\images\imageBox'
    filePathList = os.listdir(filePath)
    listNum = len(filePathList)
    List = map(str, range(listNum))  # 一个长度为100的 List
    template = get_template('home/homepage.html')
    html = template.render(locals())
    return HttpResponse(html)
