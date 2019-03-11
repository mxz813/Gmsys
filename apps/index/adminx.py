# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import Information,Atsintroduce,Links


class InformationAdmin(object):
    list_display = ('title', 'contents','add_time','image')
    list_filter = ['title', 'contents','add_time','image']
    search_fields = ['title', 'contents','image']


class AtsintroduceAdmin(object):
    list_display = ('title', 'contents','add_time','image','logo')
    list_filter = ['title', 'contents','add_time','image','logo']
    search_fields = ['title', 'contents','image','logo']


class LinksAdmin(object):
    list_display = ('title', 'url')
    list_filter = ['title', 'url']
    search_fields = ['title', 'url']


xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(Atsintroduce, AtsintroduceAdmin)
xadmin.site.register(Links, LinksAdmin)

