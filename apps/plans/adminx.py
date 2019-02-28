# -*- coding:utf-8 -*-

from xadmin import views
from .models import PlanTitle,PlanArticle,Maintain,PlanYear
import xadmin


class PlanAdmin(object):
    list_display = ('plan_title', 'add_time',)
    list_filter = ['plan_title', 'add_time']
    search_fields = ['plan_title']

class YearAdmin(object):
    list_display = ('plan_year', 'add_time',)
    list_filter = ['plan_year', 'add_time']
    search_fields = ['plan_year']


class ArticleAdmin(object):
    list_display = ('article_title', 'article_cont', 'article_auth','article_year', 'add_time',)
    list_filter = ['article_title', 'article_cont', 'article_auth','article_year', 'add_time']
    search_fields = ['article_title', 'article_cont','article_year', 'article_auth']


class MaintainAdmin(object):
    list_display = ('process_title', 'process_cont','add_time',)
    list_filter = ['process_title', 'process_cont','add_time']
    search_fields = ['process_title', 'process_cont']


xadmin.site.register(PlanTitle, PlanAdmin)
xadmin.site.register(PlanArticle, ArticleAdmin)
xadmin.site.register(Maintain, MaintainAdmin)
xadmin.site.register(PlanYear, YearAdmin)
