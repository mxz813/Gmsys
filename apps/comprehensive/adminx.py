# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import Scheduling

class SchedulingAdmin(object):
    list_display = ('sch_title','add_time','scheduling_year','contents')
    list_filter = ['sch_title','add_time','scheduling_year','contents']
    search_fields = ['sch_title','scheduling_year','contents']
    style_fields = {'contents': 'ueditor'}
    import_excel = False
    model_icon = 'fa fa-calendar'


    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(SchedulingAdmin, self).post(request, args, kwargs)

xadmin.site.register(Scheduling, SchedulingAdmin)

