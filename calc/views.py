from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def add(requset):
    a = requset.GET.get('a', 0)
    # 使用该方法，可以在没有得到‘a’的值时，赋予其默认值0
    b = requset.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))
    pass


def add2(requset, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    pass


def index(requset):
    return render(requset, 'home.html')
