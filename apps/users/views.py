# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import View
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误","login_form": login_form})

class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))