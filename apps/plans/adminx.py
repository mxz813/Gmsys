# -*- coding:utf-8 -*-

from xadmin import views
from .models import PlanTitle
import xadmin

class PlanAdmin(object):
    list_display = ('plan_title',)
    list_filter = ['plan_title']
    search_fields = ['plan_title']

xadmin.site.register(PlanTitle, PlanAdmin)