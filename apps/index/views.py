from django.shortcuts import render
from .models import Information,Atsintroduce,Links
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class IndexView(View):
    def get(self,request):
        links = Links.objects.all()
        informations = Information.objects.all()
        introduce = Atsintroduce.objects.filter()
        return render(request,'index.html',{
            'links':links,
            'informations':informations,
            'introduce':introduce,

        })


class InformationView(View):
    def get(self,request,id):
        informations = Information.objects.filter(id=id)
        return render(request,'information.html',{
            'informations':informations,

        })

class AllinforView(View):
    def get(self,request):
        allinfor = Information.objects.all()

        # 所有information进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(allinfor, 15, request=request)

        allinformation = p.page(page)
        return render(request,'allinfor.html',{
            'allinfor':allinformation,

        })


class AtsintroduceView(View):
    def get(self,request):
        introduce = Atsintroduce.objects.filter()
        return render(request,'introduce.html',{
            'introduce':introduce,

        })