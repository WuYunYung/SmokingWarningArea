from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime
from .models import Post

# Create your views here.


def homepage(request):
    template = get_template('index.html')
    # 获取模板

    now = datetime.now()
    posts = Post.objects.all()
    html = template.render(locals())
    # print(posts)
    # 取得所有的数据项
    # post_lists = list()
    # # 创建一个列表。。
    # for count, post in enumerate(posts):
    #     # 遍历所有的数据项
    #     post_lists.append("No.{}:".format(str(count)) +
    #                       str(post.title) + "<hr>")
    #     post_lists.append(
    #         "<small>"+str(post.body)+"</samll><br><br>")
    #     # 获取post数和post内容，并输出
    return HttpResponse(html)
