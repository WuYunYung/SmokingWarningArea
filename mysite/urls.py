"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from learn import views as learn_views
# from calc import views as calc_views
from blog import views as blog_views
from home import views as home_views
from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.homepage,),  # 增加一条网址匹配规则
    path('blog/', blog_views.homepage,),
    path('map/', map_views.homepage,),
    # path('add/', calc_views.add, name='add'),
    # path('add/<int:a>/<int:b>/', calc_views.add2, name='add2'),
    path('blog/post/<slug:slug>/', blog_views.showpost)
    # path('', calc_views.index, name='home')
]
