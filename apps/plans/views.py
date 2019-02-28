# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from .models import PlanTitle,PlanArticle,Maintain,PlanYear
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import datetime
# Create your views here.

class PlansView(View):
    def get(self,request):
        pltitles = PlanTitle.objects.filter(id=1)
        plarticles = PlanArticle.objects.all().filter(add_time__year=datetime.datetime.now().year).order_by("-add_time")
        maintains = Maintain.objects.filter(id=1).values()
        planyears = PlanYear.objects.all()

        #对年度进行筛选
        article_year = request.GET.get('year',"")
        if article_year:
            plarticles = PlanArticle.objects.all().filter(article_year_id = article_year)

        # Plans进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(plarticles, 12, request=request)

        allplart = p.page(page)

        return render(request,'plan.html',{
        "pltitles":pltitles,
        "plarticles":allplart,
        "maintains":maintains,
        "artiyear":article_year,
        "planyears":planyears,


        })