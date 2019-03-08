# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import Scheduling

class SchedulingAdmin(object):
    list_display = ('sch_title', 'image','add_time','scheduling_year')
    list_filter = ['sch_title', 'image','add_time','scheduling_year']
    search_fields = ['sch_title', 'image','scheduling_year']


xadmin.site.register(Scheduling, SchedulingAdmin)

