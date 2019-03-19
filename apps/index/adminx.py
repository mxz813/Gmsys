# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import Information,Atsintroduce,Links,Notice,Banner


class InformationAdmin(object):
    list_display = ('title', 'contents','add_time')
    list_filter = ['title', 'contents','add_time']
    search_fields = ['title', 'contents']
    style_fields ={'contents':'ueditor'}
    model_icon = 'fa fa-home'

class AtsintroduceAdmin(object):
    list_display = ('title', 'contents','add_time')
    list_filter = ['title', 'contents','add_time']
    search_fields = ['title', 'contents']
    style_fields = {'contents': 'ueditor'}
    model_icon = 'fa fa-home'

class LinksAdmin(object):
    list_display = ('title', 'url')
    list_filter = ['title', 'url']
    search_fields = ['title', 'url']
    model_icon = 'fa fa-home'

class NoticeAdmin(object):
    list_display = ('title', 'contents','add_time')
    list_filter = ['title', 'contents','add_time']
    search_fields = ['title', 'contents']
    style_fields = {'contents': 'ueditor'}
    model_icon = 'fa fa-home'

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    model_icon = 'fa fa-home'


xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(Atsintroduce, AtsintroduceAdmin)
xadmin.site.register(Links, LinksAdmin)
xadmin.site.register(Notice, NoticeAdmin)
xadmin.site.register(Banner, BannerAdmin)

