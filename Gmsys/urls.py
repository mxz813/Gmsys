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
from django.urls import path
from django.views.generic import TemplateView
from users.views import LoginView,LogoutView
from todolists.views import TodolistView,DeltodoView,DonetodoView,RetodoView
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name= "index.html"),name = "index"),
    path('login/', LoginView.as_view(),name = "login"),
    path('logout/', LogoutView.as_view(),name = "logout"),
    path('todolist/', TodolistView.as_view(),name = "todolist"),
    path('deltodo/',DeltodoView.as_view() ,name = "deltodo"),
    path('donetodo/',DonetodoView.as_view() ,name = "donetodo"),
    path('retodo/',RetodoView.as_view() ,name = "retodo"),

]
