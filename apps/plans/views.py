# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class PlansView(View):
    def get(self,requests):
        return render(requests,'plan.html',{})