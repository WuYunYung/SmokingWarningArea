# coding:utf-8
# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# HttpRequest是用来向页面返回内容的
# 就像print一样
# 只不过是返回给网页的

def index(request):
    return HttpResponse(u"大家好！")
    # return HttpResponse(u"欢迎光临 自强学堂!")
    # 该函数返回了一个HttpRequest对象
    # 经过处理可以将字符串返回至网页中


def test(requset):
    py_string = u"422名单"
    namelist = ['古诗渝', '胡润融', '何振业', '陈彬鸿', '杨运波', '西施霖']
    return render(requset, 'learn/test.html', {'htm_string': py_string, 'html_list': namelist})
