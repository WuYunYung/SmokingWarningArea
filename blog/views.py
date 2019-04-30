from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post
from map import models as map_models
import os
import binascii

# Create your views here.


@csrf_exempt
def blogpage(request):
    if request.method == "POST":
        try:
            # print("Got it!")
            user_address = str(request.POST.get('moodPosition')).split(',')
            # print(user_address)
            user_longi = user_address[0]
            user_lati = user_address[1]
            address = map_models.Address(
                longitude=user_longi,
                latitude=user_lati,
            )

            address.save()

            user_title = str(request.POST.get("fTitle"))
            user_slug = str(binascii.b2a_hex(
                user_title.encode('utf-8')))[2:-2]

            user_mood = str(request.POST.get('mood'))
            user_text = str(request.POST.get('text'))
            user_addr_id = int(address.id)

            user_blog = Post(
                mood=user_mood,
                title=user_title,
                slug=user_slug,
                body=user_text,
                addr_id=user_addr_id,
            )

            user_blog.save()

        except:
            user_title = str(request.POST.get("fTitle"))
            user_slug = str(binascii.b2a_hex(
                user_title.encode('utf-8')))[2:-2]

            user_mood = str(request.POST.get('mood'))
            user_text = str(request.POST.get('text'))

            user_blog = Post(
                mood=user_mood,
                title=user_title,
                slug=user_slug,
                body=user_text,
            )

            user_blog.save()

    template = get_template('blog/blog.html')
    # 获取模板
    filePath = '.\static\images\imageBox'
    filePathList = os.listdir(filePath)
    listNum = len(filePathList)
    List = map(str, range(listNum))
    now = datetime.now()
    posts = Post.objects.all()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    now = datetime.now()
    template = get_template('blog/post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
