# -*- coding:utf-8 -*-
"""Gmsys URL Configuration

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
from django.urls import path, include, re_path
from index.views import IndexView, InformationView, AtsintroduceView, AllinforView
from users.views import LoginView, LogoutView
from todolists.views import TodolistView, UsualtodoView
from plans.views import PlansView
from comprehensive.views import SchedulingView
from question.views import QuestionsView, QuestionBankView
import xadmin
from django.views.static import serve
from Gmsys.settings import MEDIA_ROOT,STATICFILES_DIRS,STATIC_URL

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('infor/id=<int:id>', InformationView.as_view(), name="infor"),
    path('intro/', AtsintroduceView.as_view(), name="intro"),
    path('allinfor/', AllinforView.as_view(), name="allinfor"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('todolist/', TodolistView.as_view(), name="todolist"),
    path('usualtodo/', UsualtodoView.as_view(), name="usualtodo"),
    path('plan/', PlansView.as_view(), name="plan"),
    path('sche/', SchedulingView.as_view(), name="sche"),
    path('que/', include('question.urls', namespace="que")),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root': STATICFILES_DIRS}),
]


