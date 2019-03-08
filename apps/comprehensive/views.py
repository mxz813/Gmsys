from django.shortcuts import render
from django.views.generic.base import View
from .models import Scheduling
from plans.models import PlanYear
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import datetime
# Create your views here.


class SchedulingView(View):
    def get(self,request):
        all_scheduling = Scheduling.objects.all().filter(add_time__year=datetime.datetime.now().year).order_by("-add_time")
        years = PlanYear.objects.all()

        #对年度进行筛选
        sche_year_id = request.GET.get('year', "")
        if sche_year_id:
            all_scheduling = Scheduling.objects.all().filter(scheduling_year_id=sche_year_id)

        # scheduling进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_scheduling, 12, request=request)

        sches = p.page(page)
        return render(request,'scheduling.html',{
            'all_scheduling':sches,
            'years':years,
        })