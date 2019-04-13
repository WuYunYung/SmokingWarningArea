from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post

# Create your views here.


def homepage(request):
    template = get_template('blog.html')
    # 获取模板

    now = datetime.now()
    posts = Post.objects.all()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
