"""gun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls.conf import path
from CS411 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    path('search/',  views.search,name = "search"),
    path('insert/',  views.insert,name = "insert"),
    path('delete/',  views.delete,name = "delete"),
    path('update/',  views.update,name = "update"),
    path('regform/',  views.regform,name = "regform"),

    # url(r'^search/$', views.SearchPageView.as_view()), 
    # url(r'^insert/$', views.InsertPageView.as_view()), 
    # url(r'^delete/$', views.DeletePageView.as_view()), 
    # url(r'^update/$', views.UpdatePageView.as_view()),
    # url(r'^search/output/$', views.OutputPageView.as_view()),
    # url(r'^insert/notice/$', views.NoticePageView.as_view()), 
    # url(r'^delete/notice/$', views.NoticePageView.as_view()), 
    # url(r'^update/notice/$', views.NoticePageView.as_view()), 
]
