# -*- coding:utf-8 -*-

from xadmin import views
from .models import Todo
import xadmin

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "ATS班組管理系統"
    site_footer = "通号中心信号二分中心ATS"
    # menu_style = "accordion"

class TodoAdmin(object):
    list_display = ('user_name', 'contents', 'add_time', 'priority', 'is_done','member_name','done_time','work_type')
    list_filter = ['user_name', 'contents', 'add_time', 'priority', 'is_done','member_name','done_time','work_type']
    search_fields = ['user_name', 'contents', 'priority', 'is_done','member_name','work_type']


xadmin.site.register(Todo, TodoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
